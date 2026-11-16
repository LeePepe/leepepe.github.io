#!/usr/bin/env python3
"""Unit tests for TIA-464 AI-managed Xiaohongshu account ops CLI (xhs_account_ops.py)."""

from __future__ import annotations

import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import xhs_account_ops


def _make_minimal_png(width: int, height: int) -> bytes:
    """Create a valid minimal 1-bit grayscale PNG header + IDAT + IEND for dimension testing."""
    def chunk(chunk_type: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + chunk_type
            + data
            + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    raw_scanline = b"\x00" + b"\xff\xf7\xec" * min(width, 1)
    idat = zlib.compress(raw_scanline)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b"")


class XhsAccountOpsTests(unittest.TestCase):
    def test_01_login_check_auth_required_and_ready_states(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_dir = Path(tmp) / "chrome-profile"
            res_missing = xhs_account_ops.check_login_health(profile_dir=profile_dir, dry_run=True)
            self.assertFalse(res_missing["ok"])
            self.assertEqual(res_missing["status"], "AUTH_REQUIRED")
            self.assertEqual(res_missing["publish_mode"], "auto_draft_owner_confirm")
            self.assertIn("creator.xiaohongshu.com", res_missing["renewal_action"])

            profile_dir.mkdir(parents=True, exist_ok=True)
            session_file = profile_dir / "xhs_creator_session.json"
            session_file.write_text(
                json.dumps({"account_handle": "@LeePepe", "expires_at": "2099-12-31T23:59:59+00:00"}),
                encoding="utf-8",
            )
            res_ready = xhs_account_ops.check_login_health(profile_dir=profile_dir, dry_run=True)
            self.assertTrue(res_ready["ok"])
            self.assertEqual(res_ready["status"], "READY")
            self.assertIsNone(res_ready["renewal_action"])

    def test_02_plan_schedule_orthogonal_matrix_and_compliance(self):
        sched = xhs_account_ops.plan_schedule(weeks=2)
        self.assertTrue(sched["ok"])
        self.assertEqual(sched["strategy"], "multi_column_experiment")
        self.assertEqual(sched["publish_mode"], "auto_draft_owner_confirm")
        self.assertEqual(len(sched["posts"]), 6)

        columns_seen = {p["column_id"] for p in sched["posts"]}
        styles_seen = {p["visual_style"] for p in sched["posts"]}
        formulas_seen = {p["title_formula"] for p in sched["posts"]}
        self.assertEqual(columns_seen, {"smart-home", "ai-indie-dev", "hardcore-digest"})
        self.assertEqual(styles_seen, {"style-a-bento", "style-b-ai-editorial", "style-c-handdrawn"})
        self.assertEqual(formulas_seen, {"pain-point-hook", "counter-intuitive-number", "lazy-subtraction"})

        for post in sched["posts"]:
            self.assertTrue(post["compliance"]["valid"], msg=f"Post failed compliance: {post['post_id']} {post['compliance']}")
            self.assertEqual(len(post["candidate_titles"]), 3)
            for title in post["candidate_titles"]:
                self.assertLessEqual(len(title), 20, msg=f"Title > 20 chars: {title}")
            self.assertEqual(len(post["topics"]), 5)
            for para in post["body_paragraphs"]:
                lines = para.split("\n")
                self.assertLessEqual(len(lines), 3)
                for line in lines:
                    self.assertEqual(line, line.lstrip(" \t\u3000"))

    def test_03_anti_repost_and_3x4_canvas_validation_catches_violations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad_png = root / "bad.png"
            bad_png.write_bytes(_make_minimal_png(800, 800))

            invalid_post = {
                "candidate_titles": [
                    "这是一个超过二十个字限制的违规小红书测试标题会被拦截",
                    "短标题二",
                ],
                "body_paragraphs": [
                    "  首行带了两个空格缩进会被防搬运规则拦截\n第二行正常",
                    "第一行\n第二行\n第三行\n第四行超出了每段最多三行的限制",
                ],
                "topics": ["#话题1", "#话题2"],
                "cover_preview": "/bad.png",
            }
            check = xhs_account_ops.validate_post_compliance(invalid_post, repo_root=root, require_exact_canvas=True)
            self.assertFalse(check["valid"])
            joined_errors = " | ".join(check["errors"])
            self.assertIn("Expected 3 candidate_titles", joined_errors)
            self.assertIn("exceeds 20 chars", joined_errors)
            self.assertIn("leading indentation/spaces", joined_errors)
            self.assertIn("max 3 lines allowed", joined_errors)
            self.assertIn("exactly 5 official #topics", joined_errors)
            self.assertIn("violate 1080x1440 (3:4) canvas spec", joined_errors)

            good_png = root / "good.png"
            good_png.write_bytes(_make_minimal_png(1080, 1440))
            valid_post = {
                "candidate_titles": ["一秒盲开书房空调", "买多了的无线开关妙用", "砍掉米家五步找遥控器"],
                "body_paragraphs": [
                    "进书房只想开空调，不想掏手机解锁走五步。\n桌边长按一下直接出风。",
                    "Node-RED 把闲置长按绑到空调开机。\n滴一声搞定，零心智负担。",
                ],
                "topics": ["#智能家居", "#减法设计", "#书房", "#NodeRED", "#HomeAssistant"],
                "cover_preview": "/good.png",
            }
            good_check = xhs_account_ops.validate_post_compliance(valid_post, repo_root=root, require_exact_canvas=True)
            self.assertTrue(good_check["valid"], msg=str(good_check["errors"]))
            self.assertEqual(good_check["cover_dimensions"], {"width": 1080, "height": 1440})

    def test_04_story_craft_desensitization_strips_secrets_and_paths(self):
        raw = "读取 /Users/lee/Development/secret.json 和 /Volumes/SSD/handoff，带 sk-1234567890abcdef1234 与 web_session=998877665544"
        cleaned, hits = xhs_account_ops.desensitize_text(raw)
        self.assertIn("api_key", hits)
        self.assertIn("cookie_secret", hits)
        self.assertIn("private_path", hits)
        self.assertNotIn("/Users/lee", cleaned)
        self.assertNotIn("/Volumes/SSD", cleaned)
        self.assertNotIn("sk-1234567890abcdef1234", cleaned)
        self.assertNotIn("998877665544", cleaned)

    def test_05_upload_draft_state_machine_and_linear_notification(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_dir = Path(tmp) / "profile"
            # Dry-run succeeds even without active cookie session, staging draft and Linear notification
            dry_res = xhs_account_ops.upload_draft(
                post_id="seed-01-study-switch-ac",
                title_index=1,
                dry_run=True,
                notify_linear="TIA-464",
                profile_dir=profile_dir,
            )
            self.assertTrue(dry_res["ok"])
            self.assertEqual(dry_res["status"], "DRAFT_STAGED_DRY_RUN")
            self.assertTrue(dry_res["auto_publish_blocked"])
            self.assertEqual(dry_res["selected_title"], "买多了的无线开关，成了盲开空调神键")
            self.assertEqual(dry_res["linear_notification"]["issue"], "TIA-464")
            self.assertTrue(any("暂存离开" in s for s in dry_res["playwright_steps"]))

            # Live mode without session returns AUTH_REQUIRED safely
            live_unauth = xhs_account_ops.upload_draft(
                post_id="seed-01-study-switch-ac",
                dry_run=False,
                profile_dir=profile_dir,
            )
            self.assertFalse(live_unauth["ok"])
            self.assertEqual(live_unauth["status"], "AUTH_REQUIRED")

            # Live mode with valid session saves draft and awaits owner confirmation
            profile_dir.mkdir(parents=True, exist_ok=True)
            (profile_dir / "xhs_creator_session.json").write_text(
                json.dumps({"expires_at": "2099-01-01T00:00:00+00:00"}),
                encoding="utf-8",
            )
            live_ready = xhs_account_ops.upload_draft(
                post_id="seed-01-study-switch-ac",
                dry_run=False,
                profile_dir=profile_dir,
            )
            self.assertTrue(live_ready["ok"])
            self.assertEqual(live_ready["status"], "DRAFT_SAVED_AWAITING_OWNER_CONFIRM")

    def test_06_collect_metrics_and_retro_report_winner_matrix_and_question_backlog(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            collected = xhs_account_ops.collect_metrics(state_dir=state_dir)
            self.assertTrue(collected["ok"])
            self.assertEqual(collected["total_notes"], 6)
            self.assertTrue(Path(collected["ledger_path"]).exists())

            retro = xhs_account_ops.generate_retro_report(metrics_items=collected["items"])
            self.assertTrue(retro["ok"])
            winner = retro["winner_matrix"]
            self.assertEqual(winner["top_column"], "hardcore-digest")
            self.assertEqual(winner["top_visual_style"], "style-c-handdrawn")
            self.assertEqual(winner["top_title_formula"], "counter-intuitive-number")
            self.assertEqual(winner["best_post_id"], "seed-02-wifi-invisible-light")

            weights = retro["recommended_next_week_weights"]
            self.assertEqual(weights["hardcore-digest"], 0.50)
            self.assertGreaterEqual(len(retro["comment_question_backlog"]), 6)
            first_q = retro["comment_question_backlog"][0]
            self.assertIn("question", first_q)
            self.assertEqual(first_q["recommended_style"], "style-c-handdrawn")

    def test_07_collected_tools_wrapper_installation_and_cli_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            wrapper_path = xhs_account_ops.install_collected_tools_wrapper(target_dir=Path(tmp))
            self.assertTrue(wrapper_path.exists())
            env = dict(**os.environ, BLOG_XHS_OPS_ROOT=str(Path(__file__).resolve().parents[1]))
            out = subprocess.check_output(
                [sys.executable, str(wrapper_path), "retro-report", "--json"],
                text=True,
                env=env,
            )
            parsed = json.loads(out)
            self.assertTrue(parsed["ok"])
            self.assertIn("winner_matrix", parsed)


import os

if __name__ == "__main__":
    unittest.main()
