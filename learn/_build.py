#!/usr/bin/env python3
"""
Build script for /learn/ (Knowledge Vault Web Blog Series).
Renders ~/Development/Personal/knowledge-vault/ markdown cards into zero-dependency
Strata-Yellow HTML reader pages under learn/.
"""

from __future__ import annotations

import hashlib
import html
import re
from pathlib import Path
from typing import Any

LEARN_DIR = Path(__file__).resolve().parent
REPO_ROOT = LEARN_DIR.parent
VAULT_DIR = Path.home() / "Development" / "Personal" / "knowledge-vault"

LINK_MAP = {
    "wwdc27-liquid-glass-and-motion-map.md": "/learn/wwdc27-glass-motion/",
    "concepts/wwdc27-liquid-glass-and-motion-map.md": "/learn/wwdc27-glass-motion/",
    "../concepts/wwdc27-liquid-glass-and-motion-map.md": "/learn/wwdc27-glass-motion/",
    "liquid-glass-optics-and-swiftui-26-27.md": "/learn/liquid-glass-optics/",
    "concepts/liquid-glass-optics-and-swiftui-26-27.md": "/learn/liquid-glass-optics/",
    "../concepts/liquid-glass-optics-and-swiftui-26-27.md": "/learn/liquid-glass-optics/",
    "swiftui-27-shader-and-motion-pipeline.md": "/learn/swiftui-shader-pipeline/",
    "concepts/swiftui-27-shader-and-motion-pipeline.md": "/learn/swiftui-shader-pipeline/",
    "../concepts/swiftui-27-shader-and-motion-pipeline.md": "/learn/swiftui-shader-pipeline/",
    "swiftui-27-scrolling-and-drag-drop-motion.md": "/learn/swiftui-scroll-drag/",
    "concepts/swiftui-27-scrolling-and-drag-drop-motion.md": "/learn/swiftui-scroll-drag/",
    "../concepts/swiftui-27-scrolling-and-drag-drop-motion.md": "/learn/swiftui-scroll-drag/",
    "appkit-uikit-27-modernization.md": "/learn/appkit-uikit-27/",
    "concepts/appkit-uikit-27-modernization.md": "/learn/appkit-uikit-27/",
    "../concepts/appkit-uikit-27-modernization.md": "/learn/appkit-uikit-27/",
    "wwdc-pipeline-and-optical-metaphor-craft.md": "/learn/wwdc-storytelling-craft/",
    "craft/wwdc-pipeline-and-optical-metaphor-craft.md": "/learn/wwdc-storytelling-craft/",
    "../craft/wwdc-pipeline-and-optical-metaphor-craft.md": "/learn/wwdc-storytelling-craft/",
    "wifi-invisible-light.md": "/learn/wifi-invisible-light/",
    "concepts/wifi-invisible-light.md": "/learn/wifi-invisible-light/",
    "../concepts/wifi-invisible-light.md": "/learn/wifi-invisible-light/",
    "science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#section-5",
    "craft/science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#section-5",
    "../craft/science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#section-5",
}

CATEGORIES = [
    {
        "id": "wwdc27",
        "title": "🍎 专题一：WWDC 25/26 (OS 26 → OS 27) Liquid Glass 与动效（8 节课精华）",
        "short_nav": "🍎 WWDC 25/26 · Liquid Glass 与动效",
        "subtitle": "5 篇概念痛点卡 · 贯通光学凸透镜、Metal Shader 扭曲、LazyStack 预取与跨端自由窗口",
    },
    {
        "id": "craft",
        "title": "🎬 专题三：叙事与表达技法（好内容是怎么讲懂的）",
        "short_nav": "🎬 叙事与表达技法",
        "subtitle": "拆解苹果官方与顶级科普的叙事骨架：玩具靶子、物理教具、故意翻车与两行代码破局",
    },
    {
        "id": "physics",
        "title": "📡 专题二：物理与硬件（看不见的世界可视化）",
        "short_nav": "📡 物理与硬件 · 看不见的世界",
        "subtitle": "把抽象电磁波与硬件损耗转化为肉眼可见的生活教具（含完整概念卡 + 九步科普脚本拆解）",
    },
]

# Ordered for index display (专题一 -> 专题二 -> 专题三 per spec 3.1)
INDEX_CATEGORY_ORDER = ["wwdc27", "physics", "craft"]

ARTICLES: list[dict[str, Any]] = [
    {
        "num": "01",
        "slug": "wwdc27-glass-motion",
        "category_id": "wwdc27",
        "title": "WWDC25/26 (OS 26 → OS 27) Liquid Glass 与动效 8 节课全景导读地图",
        "short_title": "WWDC 8 节课全景导读地图",
        "reading_time": "约 8 分钟",
        "updated": "2026-11-09",
        "teaser": "把 UI 拆成「浮在上面的液态光学控制层（Liquid Glass）」与「沉在底下的全画幅内容流（Pipeline）」——8 节课寻宝图、OS 26→27 进化矩阵与按研发场景 10 分钟精准切入指南。",
        "sources": ["concepts/wwdc27-liquid-glass-and-motion-map.md"],
        "tags": ["WWDC25", "WWDC26", "Liquid Glass", "SwiftUI", "OS 27"],
    },
    {
        "num": "02",
        "slug": "liquid-glass-optics",
        "category_id": "wwdc27",
        "title": "Liquid Glass 光学第一性原理与 SwiftUI 26→27 实战破案",
        "short_title": "Liquid Glass 光学与 SwiftUI 实战",
        "reading_time": "约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "为什么 Liquid Glass 是实时弯折光线的「液态凸透镜」而非磨砂毛玻璃？为什么严禁玻璃叠玻璃？详解 GlassEffectContainer 共享采样区、有色玻璃映射、Toolbar 防挤爆与 @State Macro。",
        "sources": ["concepts/liquid-glass-optics-and-swiftui-26-27.md"],
        "tags": ["Liquid Glass", "Lensing", "GlassEffectContainer", "ToolbarOverflowMenu", "@State Macro"],
    },
    {
        "num": "03",
        "slug": "swiftui-shader-pipeline",
        "category_id": "wwdc27",
        "title": "SwiftUI 27 高级图形与动效管线：Metal Shader 扭曲、时间流与图钉对齐",
        "short_title": "SwiftUI 27 Metal Shader 与动效管线",
        "reading_time": "约 9 分钟",
        "updated": "2026-11-09",
        "teaser": "拆解 Apple Music 级流体封面与实时歌词：三大 Shader 修饰符选型、Domain Warping 二次噪声采样、TimelineView 无状态时间注入，以及 alignmentGuide 图钉孔位反转法。",
        "sources": ["concepts/swiftui-27-shader-and-motion-pipeline.md"],
        "tags": ["Metal Shader", "layerEffect", "Domain Warping", "TimelineView", "alignmentGuide"],
    },
    {
        "num": "04",
        "slug": "swiftui-scroll-drag",
        "category_id": "wwdc27",
        "title": "SwiftUI 27 高性能滚动与多元素拖拽：LazyStack 帧预取与纸牌级重排",
        "short_title": "LazyStack 帧预取与纸牌级拖拽重排",
        "reading_time": "约 11 分钟",
        "updated": "2026-11-09",
        "teaser": "揪出 LazyVStack 子视图 if 过滤导致内存暴涨、onAppear 废掉帧间预取（Prefetching）三大掉帧元凶；用 .reorderContainer + .dragContainer 解锁纸牌接龙级成叠拖拽与非法弹回。",
        "sources": ["concepts/swiftui-27-scrolling-and-drag-drop-motion.md"],
        "tags": ["LazyVStack", "Prefetching", "reorderContainer", "dragContainer", "ScrollView"],
    },
    {
        "num": "05",
        "slug": "appkit-uikit-27",
        "category_id": "wwdc27",
        "title": "macOS 27 AppKit 与 iOS 27 UIKit 现代化：自由缩放窗口、同心圆角与手势革命",
        "short_title": "AppKit 与 UIKit 27 窗口与手势现代化",
        "reading_time": "约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "iOS 27 让 iPhone 窗口在 Mac 镜像与 iPad 上任意拉伸（UIScreen.main、idiom 与 orientation 彻底失效）；macOS 27 AppKit 告别 mouseDown 阻塞循环，拥抱 NSControl.Events 与容器同心圆角。",
        "sources": ["concepts/appkit-uikit-27-modernization.md"],
        "tags": ["AppKit", "UIKit", "macOS 27", "iOS 27", "Concentricity", "UIScene"],
    },
    {
        "num": "06",
        "slug": "wwdc-storytelling-craft",
        "category_id": "craft",
        "title": "WWDC 视觉化与架构讲法拆解：水管数据流、图钉几何与贴纸叙事法",
        "short_title": "WWDC 视觉化与架构讲法拆解",
        "reading_time": "约 8 分钟",
        "updated": "2026-11-09",
        "teaser": "提炼 6 节高分 WWDC 视觉动效课的 8 步剧本骨架：先亮出贴纸/折纸/纸牌玩具靶子，用水管/图钉/透镜替掉公式，故意展示直觉写法翻车，再用 2 行代码完成画面质变。",
        "sources": ["craft/wwdc-pipeline-and-optical-metaphor-craft.md"],
        "tags": ["WWDC 讲法", "水管模型", "图钉对齐", "技术叙事", "渐进式披露"],
    },
    {
        "num": "07",
        "slug": "wifi-invisible-light",
        "category_id": "physics",
        "title": "如果能看见 WiFi：看不见的光、室内信号破案与科普脚本技法",
        "short_title": "如果能看见 WiFi（概念破案 + 脚本技法）",
        "reading_time": "约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "把可见光波长放大 25 万倍，穿过客厅只需 30 多纳秒——用冰箱反射、鱼缸吸收、微波炉 1 万倍同频轰炸破案室内断网，并附上「把不可见变成可见」的九步科普脚本拆解。",
        "sources": [
            "concepts/wifi-invisible-light.md",
            "craft/science-video-invisible-to-visible.md",
        ],
        "companion_note": "🎬 附篇：科普视频拆解 —— 把不可见变成可见的痛点叙事法（源自 craft/science-video-invisible-to-visible.md）",
        "tags": ["WiFi", "电磁波", "2.4GHz / 5GHz", "无线感知", "科普脚本拆解"],
    },
]


def asset_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def strip_frontmatter_and_h1(md_text: str) -> str:
    text = md_text.strip()
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2].strip()
    lines = text.splitlines()
    out_lines = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.startswith("# "):
            skipped_h1 = True
            continue
        out_lines.append(line)
    return "\n".join(out_lines).strip()


def format_inline(text: str) -> str:
    """Convert inline markdown (code, links, bold, italic, math) safely to HTML."""
    code_spans: list[str] = []

    def save_code(match: re.Match[str]) -> str:
        idx = len(code_spans)
        code_spans.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{idx}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)
    text = html.escape(text)

    # Inline math like $10^{-9}$ or $10^9$
    def replace_math(match: re.Match[str]) -> str:
        expr = match.group(1)
        expr = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", expr)
        expr = re.sub(r"\^(\d+)", r"<sup>\1</sup>", expr)
        return f"<span class=\"math-expr\">{expr}</span>"

    text = re.sub(r"\$([^$]+)\$", replace_math, text)

    # Markdown links [label](url)
    def replace_link(match: re.Match[str]) -> str:
        label_raw = match.group(1)
        url_raw = html.unescape(match.group(2)).strip()
        mapped_url = LINK_MAP.get(url_raw, url_raw)
        label_html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", label_raw)
        return f'<a href="{html.escape(mapped_url, quote=True)}">{label_html}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, text)

    # Bold **...**
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # Italic *...*
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for idx, span in enumerate(code_spans):
        text = text.replace(f"\x00CODE{idx}\x00", span)

    return text


def render_blocks(lines: list[str], in_checklist: bool = False) -> str:
    """Render standard markdown block lines (paragraphs, code blocks, tables, lists, blockquotes)."""
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_escaped = html.escape("\n".join(code_lines))
            lang_attr = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{lang_attr}>{code_escaped}</code></pre>")
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_lines: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(f"<blockquote><p>{format_inline(' '.join(bq_lines))}</p></blockquote>")
            continue

        # Table
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|\s*[-:]+", lines[i + 1].strip()):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2  # skip header and separator
            rows: list[list[str]] = []
            while i < n and lines[i].strip().startswith("|"):
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row_cells)
                i += 1
            th_html = "".join(f"<th>{format_inline(c)}</th>" for c in header_cells)
            trs_html = []
            for row in rows:
                tds = "".join(f"<td>{format_inline(c)}</td>" for c in row)
                trs_html.append(f"<tr>{tds}</tr>")
            out.append(
                f'<div class="table-wrap"><table><thead><tr>{th_html}</tr></thead>'
                f'<tbody>{"".join(trs_html)}</tbody></table></div>'
            )
            continue

        # Heading h3
        if stripped.startswith("### "):
            out.append(f"<h3>{format_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        # Unordered or Ordered List
        ul_match = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        ol_match = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if ul_match or ol_match:
            is_ol = bool(ol_match)
            tag = "ol" if is_ol else "ul"
            items_html: list[str] = []
            item_idx = 0

            while i < n:
                cur = lines[i]
                cur_strip = cur.strip()
                if not cur_strip:
                    i += 1
                    continue
                m_ul = re.match(r"^(\s*)[-*]\s+(.*)$", cur)
                m_ol = re.match(r"^(\s*)(\d+)\.\s+(.*)$", cur)
                if is_ol and m_ol and len(m_ol.group(1)) == 0:
                    item_idx += 1
                    item_body = format_inline(m_ol.group(3))
                    i += 1
                    # Check nested indented lines (code blocks or sub-bullets)
                    sub_lines: list[str] = []
                    while i < n and (lines[i].startswith("  ") or lines[i].startswith("\t") or not lines[i].strip()):
                        if not lines[i].strip():
                            # Peek ahead to see if next non-empty line is still indented
                            j = i + 1
                            while j < n and not lines[j].strip():
                                j += 1
                            if j < n and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                                sub_lines.append("")
                                i += 1
                                continue
                            else:
                                break
                        sub_lines.append(re.sub(r"^(?: {1,4}|\t)", "", lines[i]))
                        i += 1
                    sub_html = render_blocks(sub_lines) if sub_lines else ""
                    if in_checklist:
                        badge = '<span class="check-badge" aria-hidden="true">✓</span>'
                        items_html.append(f"<li>{badge}{item_body}{sub_html}</li>")
                    else:
                        items_html.append(f"<li>{item_body}{sub_html}</li>")
                elif (not is_ol) and m_ul and len(m_ul.group(1)) == 0:
                    item_idx += 1
                    raw_text = m_ul.group(2)
                    # Check if this is a "直答：" bullet inside a Q&A card
                    direct_m = re.match(r"^\*\*直答\*\*[：:]\s*(.*)$", raw_text)
                    i += 1
                    sub_lines = []
                    while i < n and (lines[i].startswith("  ") or lines[i].startswith("\t") or not lines[i].strip()):
                        if not lines[i].strip():
                            j = i + 1
                            while j < n and not lines[j].strip():
                                j += 1
                            if j < n and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                                sub_lines.append("")
                                i += 1
                                continue
                            else:
                                break
                        sub_lines.append(re.sub(r"^(?: {1,2}|\t)", "", lines[i]))
                        i += 1
                    sub_html = render_blocks(sub_lines) if sub_lines else ""
                    if direct_m:
                        ans_html = format_inline(direct_m.group(1))
                        out.append(
                            f'<div class="qa-direct-answer"><span class="qa-direct-label">直答</span>'
                            f"{ans_html}{sub_html}</div>"
                        )
                    else:
                        item_body = format_inline(raw_text)
                        items_html.append(f"<li>{item_body}{sub_html}</li>")
                else:
                    break

            if items_html:
                out.append(f"<{tag}>{''.join(items_html)}</{tag}>")
            continue

        # Regular paragraph
        para_lines: list[str] = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt == "---"
                or nxt.startswith("#")
                or nxt.startswith("```")
                or nxt.startswith(">")
                or nxt.startswith("|")
                or re.match(r"^[-*]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
            ):
                break
            para_lines.append(nxt)
            i += 1
        out.append(f"<p>{format_inline(' '.join(para_lines))}</p>")

    return "\n".join(out)


def render_section(h2_title: str, sec_id: str, body_lines: list[str]) -> str:
    """Render an H2 section using specialized Knowledge-Digest visual cards."""
    heading_html = f'<h2 id="{sec_id}" tabindex="-1">{format_inline(h2_title)}</h2>'

    # 1. ⚡ TL;DR Hero Card
    if "一句话本质" in h2_title or "一句话公式" in h2_title:
        inner_html = render_blocks(body_lines)
        badge_text = "⚡ 一句话公式 · TL;DR" if "公式" in h2_title else "⚡ 一句话本质 · TL;DR"
        return (
            f"{heading_html}\n"
            f'<div class="tldr-hero-card">'
            f'<div class="tldr-badge">{badge_text}</div>'
            f'<div class="tldr-body">{inner_html}</div>'
            f"</div>"
        )

    # 2. 🎯 Pain-Point Q&A Cards
    if "核心痛点直答" in h2_title:
        cards: list[str] = []
        cur_q_title: str | None = None
        cur_q_lines: list[str] = []

        def flush_q() -> None:
            if cur_q_title is None:
                return
            m = re.match(r"^(Q\d+)[：:]\s*(.*)$", cur_q_title)
            if m:
                q_badge = html.escape(m.group(1))
                q_rest = format_inline(m.group(2))
            else:
                q_badge = "Q"
                q_rest = format_inline(cur_q_title)
            body_html = render_blocks(cur_q_lines)
            cards.append(
                f'<section class="qa-card">'
                f'<h3 class="qa-question"><span class="qa-q-badge">{q_badge}</span><span>{q_rest}</span></h3>'
                f"{body_html}"
                f"</section>"
            )

        for line in body_lines:
            if line.strip().startswith("### "):
                flush_q()
                cur_q_title = line.strip()[4:].strip()
                cur_q_lines = []
            else:
                cur_q_lines.append(line)
        flush_q()
        return f'{heading_html}\n<div class="qa-stack">{"".join(cards)}</div>'

    # 3. ✅ Actionable Checklist
    if "立即可用清单" in h2_title:
        inner_html = render_blocks(body_lines, in_checklist=True)
        return f'{heading_html}\n<div class="checklist-card">{inner_html}</div>'

    # 4. 🛠 Reusable Craft Patterns (H3 cards)
    if "可复用视觉化技巧" in h2_title or "可复用制作技巧" in h2_title:
        cards = []
        cur_c_title: str | None = None
        cur_c_lines: list[str] = []

        def flush_c() -> None:
            if cur_c_title is None:
                return
            body_html = render_blocks(cur_c_lines)
            cards.append(
                f'<section class="craft-pattern-card">'
                f"<h3>{format_inline(cur_c_title)}</h3>"
                f"{body_html}"
                f"</section>"
            )

        for line in body_lines:
            if line.strip().startswith("### "):
                flush_c()
                cur_c_title = line.strip()[4:].strip()
                cur_c_lines = []
            else:
                cur_c_lines.append(line)
        flush_c()
        return f'{heading_html}\n<div class="craft-grid">{"".join(cards)}</div>'

    # Standard section (e.g., 🧰 核心教具与量级速览, 🎬 叙事流, 🔭 延伸视野)
    return f"{heading_html}\n{render_blocks(body_lines)}"


def parse_markdown_article(article: dict[str, Any]) -> tuple[list[tuple[str, str]], str]:
    """Parse one or more source markdown files into (sections_outline, body_html)."""
    sections_outline: list[tuple[str, str]] = []
    rendered_sections: list[str] = []
    sec_counter = 0

    for src_idx, rel_path in enumerate(article["sources"]):
        full_path = VAULT_DIR / rel_path
        raw_md = full_path.read_text(encoding="utf-8")
        body_md = strip_frontmatter_and_h1(raw_md)

        if src_idx > 0 and article.get("companion_note"):
            rendered_sections.append(
                f'<div class="companion-divider">'
                f'<strong>{html.escape(article["companion_note"])}</strong>'
                f'<span>好内容是怎么讲懂的 · 脚本结构与视觉化技法</span>'
                f"</div>"
            )

        lines = body_md.splitlines()
        cur_h2: str | None = None
        cur_lines: list[str] = []

        def flush_sec() -> None:
            nonlocal sec_counter
            if cur_h2 is None:
                return
            sec_counter += 1
            sec_id = f"section-{sec_counter}"
            clean_outline_title = re.sub(r"（[^）]*）|\([^)]*\)", "", cur_h2).strip()
            sections_outline.append((sec_id, clean_outline_title or cur_h2))
            rendered_sections.append(render_section(cur_h2, sec_id, cur_lines))

        for line in lines:
            if line.startswith("## "):
                flush_sec()
                cur_h2 = line[3:].strip()
                cur_lines = []
            else:
                cur_lines.append(line)
        flush_sec()

    return sections_outline, "\n".join(rendered_sections)


def build_nav_html(
    current_slug: str | None,
    outline: list[tuple[str, str]] | None,
    is_mobile: bool = False,
) -> str:
    """Build grouped chapter navigation for desktop rail or mobile dialog."""
    groups_html: list[str] = []
    for cat_id in INDEX_CATEGORY_ORDER:
        cat = next(c for c in CATEGORIES if c["id"] == cat_id)
        cat_articles = [a for a in ARTICLES if a["category_id"] == cat_id]
        items_html: list[str] = []
        for art in cat_articles:
            is_curr = art["slug"] == current_slug
            li_cls = "chapter is-current" if is_curr else "chapter"
            aria_curr = ' aria-current="page"' if is_curr else ""
            outline_html = ""
            if is_curr and outline:
                ol_items = []
                for idx, (sec_id, sec_title) in enumerate(outline):
                    loc_attr = ' aria-current="location"' if idx == 0 else ""
                    ol_items.append(f'<li><a href="#{sec_id}"{loc_attr}>{html.escape(sec_title)}</a></li>')
                aria_lbl = "手机本篇小节" if is_mobile else "本篇小节"
                outline_html = (
                    f'<ol class="outline" aria-label="{aria_lbl}">{"".join(ol_items)}</ol>'
                    f'<div class="reading-status"><p><span>本篇阅读进度</span><span data-progress-label>0%</span></p>'
                    f'<div class="progress-track" role="progressbar" aria-label="本篇阅读进度" '
                    f'aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">'
                    f'<span class="progress-fill" data-progress-fill></span></div></div>'
                )
            items_html.append(
                f'<li class="{li_cls}">'
                f'<a class="chapter-link" href="/learn/{art["slug"]}/"{aria_curr}>'
                f'<span class="chapter-number">{art["num"]}</span>'
                f'<span>{html.escape(art["short_title"])}</span></a>'
                f"{outline_html}</li>"
            )
        groups_html.append(
            f'<div class="nav-group">'
            f'<p class="nav-caption">{html.escape(cat["short_nav"])}</p>'
            f'<ol class="timeline">{"".join(items_html)}</ol>'
            f"</div>"
        )
    return "".join(groups_html)


def render_page_shell(
    *,
    title: str,
    permalink: str,
    mobile_pos: str,
    current_slug: str | None,
    outline: list[tuple[str, str]] | None,
    main_inner_html: str,
    css_v: str,
    js_v: str,
) -> str:
    desktop_nav = build_nav_html(current_slug, outline, is_mobile=False)
    mobile_nav = build_nav_html(current_slug, outline, is_mobile=True)
    rail_intro = (
        '<p class="rail-intro">先给反常识本质，再用生活教具破案，最后给可执行清单。</p>'
        if current_slug is None
        else ""
    )

    return f"""---
layout: null
title: "{html.escape(title, quote=True)}"
permalink: {permalink}
---
<!doctype html>
<html lang="zh-CN" data-lp-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#EEECE5"><title>{html.escape(title)} | Knowledge Vault · Lee Pepe</title>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@chinese-fonts/hcqyt@2.0.0/dist/ChillRoundFRegular/result.css">
<link rel="stylesheet" href="/learn/reader.css?v={css_v}"><script src="/learn/reader.js?v={js_v}" defer></script></head><body>
<a class="skip-link" href="#main">跳到正文</a>
<header class="mobile-bar"><div class="mobile-bar-inner"><button class="open-series" type="button" aria-label="打开专栏目录" aria-haspopup="dialog" aria-controls="series-sheet" aria-expanded="false">
<span>直击痛点的求知笔记</span><span class="mobile-position">{html.escape(mobile_pos)}</span><span class="chevron" aria-hidden="true"></span></button>
<button class="theme-toggle" type="button" data-theme-toggle aria-label="切换深浅色">🌙 深色</button></div>
<div class="progress-track" aria-hidden="true"><span class="progress-fill" data-progress-fill></span></div></header>
<div class="reader-frame"><aside class="rail" aria-label="专栏导航"><div class="rail-top">
<div><a class="series-brand" href="/learn/">直击痛点的求知笔记</a><p class="series-subtitle">Knowledge Vault · 原理与好内容拆解</p></div>
<button class="theme-toggle" type="button" data-theme-toggle aria-label="切换深浅色">🌙 深色</button></div>
<div class="rail-scroll">{rail_intro}<nav aria-label="专栏文章">{desktop_nav}</nav></div>
<div class="rail-footer"><a class="rail-home" href="/">← Lee Pepe 首页</a><a class="rail-home" href="/ai-workflow/">带一群 AI 干活 →</a></div></aside>
<main id="main" tabindex="-1">{main_inner_html}</main></div>
<dialog class="series-sheet" id="series-sheet" aria-labelledby="sheet-title"><header class="sheet-header"><h2 id="sheet-title">直击痛点的求知笔记</h2><button class="close-sheet" type="button" autofocus>关闭</button></header>
<div class="sheet-content"><p class="series-subtitle">先给反常识本质，再用生活教具破案，最后给可执行清单</p><nav aria-label="手机专栏文章">{mobile_nav}</nav><a class="sheet-home" href="/">← Lee Pepe 首页</a></div></dialog>
</body></html>
"""


def build_index_page(css_v: str, js_v: str) -> None:
    cat_sections: list[str] = []
    for cat_id in INDEX_CATEGORY_ORDER:
        cat = next(c for c in CATEGORIES if c["id"] == cat_id)
        cat_articles = [a for a in ARTICLES if a["category_id"] == cat_id]
        cards_html: list[str] = []
        for art in cat_articles:
            tags_html = "".join(f'<span class="tag-pill">{html.escape(t)}</span>' for t in art["tags"][:4])
            cards_html.append(
                f'<li><a class="story-card" href="/learn/{art["slug"]}/">'
                f'<span class="story-no">{art["num"]}</span>'
                f'<div><h3>{html.escape(art["title"])}</h3>'
                f'<p class="story-teaser">{html.escape(art["teaser"])}</p>'
                f'<div class="story-meta-row"><span class="story-time">{html.escape(art["reading_time"])}</span>{tags_html}</div></div>'
                f'<span class="story-arrow" aria-hidden="true">→</span></a></li>'
            )
        cat_sections.append(
            f'<section class="category-section" aria-labelledby="cat-{cat_id}">'
            f'<div class="category-heading"><h2 id="cat-{cat_id}">{html.escape(cat["title"])}</h2>'
            f'<span>{len(cat_articles)} 篇</span></div>'
            f'<p class="story-teaser" style="margin-top:-6px;margin-bottom:14px;">{html.escape(cat["subtitle"])}</p>'
            f'<ol class="story-list">{"".join(cards_html)}</ol>'
            f"</section>"
        )

    main_html = f"""<section class="paper" aria-labelledby="series-title"><div class="reading-column"><header class="index-header">
<p class="eyebrow">PERSONAL KNOWLEDGE VAULT · 7 篇深度痛点卡</p>
<h1 id="series-title">直击痛点的求知笔记</h1>
<p class="index-intro">拒绝按教科书目录平铺直叙。每一篇笔记都严格遵循同一套认知破案闭环：<strong>先给一句话反常识本质（TL;DR），再用生活教具拆穿 3–5 个真痛点（Q&amp;A），最后落到明天就能照着改的行动清单（Checklist）与叙事技法拆解</strong>。</p>
<div class="pillar-strip">
  <div class="pillar-chip"><strong>⚡ 一句话本质</strong>抛出量级数字与反直觉结论，3 秒建立全局坐标系</div>
  <div class="pillar-chip"><strong>🎯 核心痛点直答</strong>用透镜、水管、图钉、冰箱等生活教具替代晦涩公式</div>
  <div class="pillar-chip"><strong>✅ 立即可用清单</strong>提炼 ≤3 条零门槛工程/生活实操处方与表达模板</div>
</div>
<p class="article-meta" style="margin-top:16px;"><span>7 篇完整专题（覆盖 WWDC 25/26 八节课 + WiFi 科普标杆）</span><span class="meta-dot" aria-hidden="true"></span><span>约 66 分钟</span><span class="meta-dot" aria-hidden="true"></span><span>Strata 麦芽黄双色阅读器</span></p></header>
<nav aria-label="分类文章目录">{"".join(cat_sections)}</nav>
</div></section>"""

    page_html = render_page_shell(
        title="直击痛点的求知笔记",
        permalink="/learn/",
        mobile_pos="目录 / 7",
        current_slug=None,
        outline=None,
        main_inner_html=main_html,
        css_v=css_v,
        js_v=js_v,
    )
    (LEARN_DIR / "index.html").write_text(page_html, encoding="utf-8")


def build_article_pages(css_v: str, js_v: str) -> None:
    total = len(ARTICLES)
    for idx, art in enumerate(ARTICLES):
        outline, body_html = parse_markdown_article(art)
        prev_art = ARTICLES[idx - 1] if idx > 0 else None
        next_art = ARTICLES[idx + 1] if idx + 1 < total else None

        pager_links: list[str] = []
        if prev_art:
            pager_links.append(
                f'<a class="page-card" rel="prev" href="/learn/{prev_art["slug"]}/">'
                f"<small>← 上一篇 · {prev_art['num']}</small>"
                f'<span>{html.escape(prev_art["title"])}</span></a>'
            )
        if next_art:
            pager_links.append(
                f'<a class="page-card" rel="next" href="/learn/{next_art["slug"]}/">'
                f"<small>下一篇 · {next_art['num']} →</small>"
                f'<span>{html.escape(next_art["title"])}</span></a>'
            )

        tags_html = "".join(f'<span class="tag-pill">{html.escape(t)}</span>' for t in art["tags"])
        cat_obj = next(c for c in CATEGORIES if c["id"] == art["category_id"])

        main_html = f"""<article class="paper"><div class="reading-column"><header class="article-header">
<p class="eyebrow">第 {art["num"]} 篇 · {html.escape(cat_obj["short_nav"])}</p>
<h1>{html.escape(art["title"])}</h1>
<p class="article-meta"><time datetime="{art["updated"]}">{art["updated"]}</time><span class="meta-dot" aria-hidden="true"></span><span>{html.escape(art["reading_time"])}</span><span class="meta-dot" aria-hidden="true"></span>{tags_html}</p></header>
<div class="prose" data-reading-body>
{body_html}
</div>
<footer><div class="article-end">本篇完 · Knowledge Vault</div>
<nav class="pager" aria-label="相邻文章">{"".join(pager_links)}</nav>
<a class="back-index" href="/learn/">← 回到专栏总览（/learn/）</a></footer></div></article>"""

        page_html = render_page_shell(
            title=art["title"],
            permalink=f'/learn/{art["slug"]}/',
            mobile_pos=f'{idx + 1} / {total}',
            current_slug=art["slug"],
            outline=outline,
            main_inner_html=main_html,
            css_v=css_v,
            js_v=js_v,
        )
        out_dir = LEARN_DIR / art["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_html, encoding="utf-8")


def main() -> None:
    css_v = asset_hash(LEARN_DIR / "reader.css")
    js_v = asset_hash(LEARN_DIR / "reader.js")
    build_index_page(css_v, js_v)
    build_article_pages(css_v, js_v)
    print(f"Built /learn/ index + {len(ARTICLES)} articles (css={css_v}, js={js_v})")


if __name__ == "__main__":
    main()
