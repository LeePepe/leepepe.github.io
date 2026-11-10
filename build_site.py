#!/usr/bin/env python3
"""
Unified static site builder for LeePepe/leepepe.github.io.
Strictly follows the approved prototype in /Volumes/SSD/Development/handoff/blog-design/:
- Single asset source of truth: /assets/{colors.css, strata-theme.css, blog.css, theme.js}
- Zero YAML frontmatter on any generated .html file (line 1 is always <!doctype html>)
- 100% unified floating capsule header (header.site-header.shell > div.site-header__bar)
  with 首页(/) · 求知(/learn/) · 思考(/thoughts/) · 归档(/archive/) · 标签(/tags/) · 关于(/about/)
  and Light / Dark / System theme toggle
- Quiet editorial list layout (section.page-intro + .layout > .card.card--flush > ol.post-list + aside.aside)
- Quiet editorial article layout (.post-layout > article.card.article > .prose + aside.toc)
  with zero Emoji noise and zero nested box-in-box cards.
"""

from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent
LEARN_DIR = REPO_ROOT / "learn"
THOUGHTS_DIR = REPO_ROOT / "thoughts"
VAULT_DIR = Path.home() / "Development" / "Personal" / "knowledge-vault"
VAULT_THOUGHTS_DIR = VAULT_DIR / "thoughts"
SITE_URL = "https://leepepe.github.io"

NAV_ITEMS = [
    ("home", "首页", "/"),
    ("learn", "求知", "/learn/"),
    ("thoughts", "思考", "/thoughts/"),
    ("archive", "归档", "/archive/"),
    ("tags", "标签", "/tags/"),
    ("about", "关于", "/about/"),
]

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
    "science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#sec-8",
    "craft/science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#sec-8",
    "../craft/science-video-invisible-to-visible.md": "/learn/wifi-invisible-light/#sec-8",
}

LEARN_ARTICLES: list[dict[str, Any]] = [
    {
        "num": "01",
        "slug": "wwdc27-glass-motion",
        "aliases": [],
        "category": "WWDC 25/26 · Liquid Glass 与动效",
        "title": "WWDC25/26 (OS 26 → OS 27) Liquid Glass 与动效 8 节课全景导读地图",
        "short_title": "WWDC 8 节课全景导读地图",
        "reading_time": "阅读约 8 分钟",
        "updated": "2026-11-09",
        "teaser": "把 UI 拆成「浮在上面的液态光学控制层（Liquid Glass）」与「沉在底下的全画幅内容流（Pipeline）」——8 节课寻宝图、OS 26→27 进化矩阵与按研发场景 10 分钟精准切入指南。",
        "sources": ["concepts/wwdc27-liquid-glass-and-motion-map.md"],
        "tags": ["SwiftUI", "Liquid Glass", "WWDC26"],
    },
    {
        "num": "02",
        "slug": "liquid-glass-optics",
        "aliases": ["swiftui-liquid-glass-wwdc25"],
        "category": "WWDC 25/26 · Liquid Glass 与动效",
        "title": "Liquid Glass 光学第一性原理与 SwiftUI 26→27 实战破案",
        "short_title": "Liquid Glass 光学与 SwiftUI 实战",
        "reading_time": "阅读约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "为什么 Liquid Glass 是实时弯折光线的「液态凸透镜」而非磨砂毛玻璃？为什么严禁玻璃叠玻璃？详解 GlassEffectContainer 共享采样区、有色玻璃映射、Toolbar 防挤爆与 @State Macro。",
        "sources": ["concepts/liquid-glass-optics-and-swiftui-26-27.md"],
        "tags": ["Liquid Glass", "SwiftUI", "光学设计"],
    },
    {
        "num": "03",
        "slug": "swiftui-shader-pipeline",
        "aliases": [],
        "category": "WWDC 25/26 · Liquid Glass 与动效",
        "title": "SwiftUI 27 高级图形与动效管线：Metal Shader 扭曲、时间流与图钉对齐",
        "short_title": "SwiftUI 27 Metal Shader 与动效管线",
        "reading_time": "阅读约 9 分钟",
        "updated": "2026-11-09",
        "teaser": "拆解 Apple Music 级流体封面与实时歌词：三大 Shader 修饰符选型、Domain Warping 二次噪声采样、TimelineView 无状态时间注入，以及 alignmentGuide 图钉孔位反转法。",
        "sources": ["concepts/swiftui-27-shader-and-motion-pipeline.md"],
        "tags": ["SwiftUI", "Metal Shader", "动效管线"],
    },
    {
        "num": "04",
        "slug": "swiftui-scroll-drag",
        "aliases": [],
        "category": "WWDC 25/26 · Liquid Glass 与动效",
        "title": "SwiftUI 27 高性能滚动与多元素拖拽：LazyStack 帧预取与纸牌级重排",
        "short_title": "LazyStack 帧预取与纸牌级拖拽重排",
        "reading_time": "阅读约 11 分钟",
        "updated": "2026-11-09",
        "teaser": "揪出 LazyVStack 子视图 if 过滤导致内存暴涨、onAppear 废掉帧间预取（Prefetching）三大掉帧元凶；用 .reorderContainer + .dragContainer 解锁纸牌接龙级成叠拖拽与非法弹回。",
        "sources": ["concepts/swiftui-27-scrolling-and-drag-drop-motion.md"],
        "tags": ["SwiftUI", "ScrollView", "性能优化"],
    },
    {
        "num": "05",
        "slug": "appkit-uikit-27",
        "aliases": [],
        "category": "WWDC 25/26 · Liquid Glass 与动效",
        "title": "macOS 27 AppKit 与 iOS 27 UIKit 现代化：自由缩放窗口、同心圆角与手势革命",
        "short_title": "AppKit 与 UIKit 27 窗口与手势现代化",
        "reading_time": "阅读约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "iOS 27 让 iPhone 窗口在 Mac 镜像与 iPad 上任意拉伸（UIScreen.main、idiom 与 orientation 彻底失效）；macOS 27 AppKit 告别 mouseDown 阻塞循环，拥抱 NSControl.Events 与容器同心圆角。",
        "sources": ["concepts/appkit-uikit-27-modernization.md"],
        "tags": ["AppKit", "UIKit", "窗口适配"],
    },
    {
        "num": "06",
        "slug": "wwdc-storytelling-craft",
        "aliases": [],
        "category": "叙事与表达技法",
        "title": "WWDC 视觉化与架构讲法拆解：水管数据流、图钉几何与贴纸叙事法",
        "short_title": "WWDC 视觉化与架构讲法拆解",
        "reading_time": "阅读约 8 分钟",
        "updated": "2026-11-09",
        "teaser": "提炼 6 节高分 WWDC 视觉动效课的 8 步剧本骨架：先亮出贴纸/折纸/纸牌玩具靶子，用水管/图钉/透镜替掉公式，故意展示直觉写法翻车，再用 2 行代码完成画面质变。",
        "sources": ["craft/wwdc-pipeline-and-optical-metaphor-craft.md"],
        "tags": ["技术叙事", "WWDC26", "视觉隐喻"],
    },
    {
        "num": "07",
        "slug": "wifi-invisible-light",
        "aliases": [],
        "category": "物理与硬件可视化",
        "title": "如果能看见 WiFi：看不见的光、室内信号破案与科普脚本技法",
        "short_title": "如果能看见 WiFi（概念破案 + 脚本技法）",
        "reading_time": "阅读约 10 分钟",
        "updated": "2026-11-09",
        "teaser": "把可见光波长放大 25 万倍，穿过客厅只需 30 多纳秒——用冰箱反射、鱼缸吸收、微波炉 1 万倍同频轰炸破案室内断网，并附上「把不可见变成可见」的九步科普脚本拆解。",
        "sources": [
            "concepts/wifi-invisible-light.md",
            "craft/science-video-invisible-to-visible.md",
        ],
        "tags": ["WiFi", "物理可视化", "技术叙事"],
    },
]

_EMOJI_STRIP_RE = re.compile(
    r"[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]+"
)


def strip_emoji(text: str) -> str:
    return re.sub(r"\s+", " ", _EMOJI_STRIP_RE.sub("", text)).strip()


def format_cn_date(iso_date: str) -> str:
    parts = iso_date.split("-")
    if len(parts) == 3:
        return f"{int(parts[0])} 年 {int(parts[1])} 月 {int(parts[2])} 日"
    return iso_date


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


def strip_html_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


_SYNTAX_KEYWORDS = {
    "swift", "func", "let", "var", "struct", "enum", "class", "protocol", "extension",
    "if", "else", "for", "in", "while", "switch", "case", "default", "return", "break",
    "continue", "guard", "where", "import", "private", "public", "internal", "fileprivate",
    "open", "static", "mutating", "async", "await", "throws", "try", "catch", "some", "any",
    "self", "Self", "super", "init", "deinit", "true", "false", "nil", "inout", "override",
    "final", "lazy", "weak", "unowned", "as", "is",
    "kernel", "vertex", "fragment", "constant", "device", "threadgroup", "thread",
    "float", "float2", "float3", "float4", "half", "half2", "half3", "half4", "int",
    "uint", "uint2", "bool", "void", "include", "using", "namespace", "metal", "const",
    "def", "from", "lambda", "with", "yield", "None", "True", "False", "and", "or", "not",
    "export", "function", "local", "echo", "fi", "then", "do", "done",
}

_TOKEN_RE = re.compile(
    r"(?P<cmt>//[^\n]*|/\*[\s\S]*?\*/|#(?![include\w])[^\n]*)"
    r"|(?P<str>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')"
    r"|(?P<attr>@[A-Za-z_][A-Za-z0-9_]*|\[\[[A-Za-z0-9_:]+\]\])"
    r"|(?P<num>\b\d+(?:\.\d+)?(?:f|h|u|L|ms|s|px|rem|em|deg|%)?\b)"
    r"|(?P<ident>\b[A-Za-z_][A-Za-z0-9_]*\b)"
)


def highlight_code(code_str: str) -> str:
    """Syntax highlighter producing prototype Rouge classes (.c1, .s, .kd, .kt, .nf, .mi)."""
    out: list[str] = []
    last = 0
    for m in _TOKEN_RE.finditer(code_str):
        if m.start() > last:
            out.append(html.escape(code_str[last:m.start()]))
        tok = m.group(0)
        escaped = html.escape(tok)
        if m.group("cmt"):
            out.append(f'<span class="c1">{escaped}</span>')
        elif m.group("str"):
            out.append(f'<span class="s">{escaped}</span>')
        elif m.group("attr"):
            out.append(f'<span class="kd">{escaped}</span>')
        elif m.group("num"):
            out.append(f'<span class="mi">{escaped}</span>')
        elif m.group("ident"):
            after = code_str[m.end():m.end() + 1]
            before = code_str[max(0, m.start() - 1):m.start()]
            if tok in _SYNTAX_KEYWORDS:
                out.append(f'<span class="kd">{escaped}</span>')
            elif tok[0].isupper():
                out.append(f'<span class="kt">{escaped}</span>')
            elif after == "(" or before == ".":
                out.append(f'<span class="nf">{escaped}</span>')
            else:
                out.append(escaped)
        else:
            out.append(escaped)
        last = m.end()
    if last < len(code_str):
        out.append(html.escape(code_str[last:]))
    return "".join(out)


def format_inline(text: str) -> str:
    code_spans: list[str] = []

    def save_code(match: re.Match[str]) -> str:
        idx = len(code_spans)
        code_spans.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{idx}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)
    text = html.escape(strip_emoji(text))

    def replace_math(match: re.Match[str]) -> str:
        expr = match.group(1)
        expr = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", expr)
        expr = re.sub(r"\^(\d+)", r"<sup>\1</sup>", expr)
        return expr

    text = re.sub(r"\$([^$]+)\$", replace_math, text)

    def replace_link(match: re.Match[str]) -> str:
        label_raw = match.group(1)
        url_raw = html.unescape(match.group(2)).strip()
        mapped_url = LINK_MAP.get(url_raw, url_raw)
        label_html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", label_raw)
        return f'<a href="{html.escape(mapped_url, quote=True)}">{label_html}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for idx, span in enumerate(code_spans):
        text = text.replace(f"\x00CODE{idx}\x00", span)

    return text


def normalize_h2_title(raw_h2: str, is_companion: bool = False) -> str:
    t = strip_emoji(raw_h2)
    t_no_paren = re.sub(r"（[^）]*）|\([^)]*\)", "", t).strip()
    if "一句话本质" in t or "一句话公式" in t:
        return "附篇一句话结论" if is_companion else "一句话结论"
    if "核心痛点直答" in t:
        return "核心痛点问答"
    if "立即可用清单" in t:
        return "立即可用清单"
    if "叙事" in t or "制作技巧" in t or "视觉化技巧" in t or "迁移套用" in t:
        if "九步" in t or "八步" in t:
            return "叙事与制作拆解"
        return t_no_paren or t
    return t_no_paren or t


def normalize_h3_title(raw_h3: str) -> str:
    t = strip_emoji(raw_h3)
    m = re.match(r"^Q(\d+)[：:.．\s]+(.*)$", t)
    if m:
        return f"Q{m.group(1)}. {m.group(2).strip()}"
    return t


def render_blocks(
    lines: list[str],
    *,
    force_ul_top: bool = False,
    toc_accumulator: list[dict[str, str]] | None = None,
    h3_prefix: str = "sub",
) -> str:
    out: list[str] = []
    i = 0
    n = len(lines)
    h3_counter = 0

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

        # Code block -> prototype Rouge structure
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            raw_code = "\n".join(code_lines)
            lang_norm = (lang or "text").lower()
            lang_badge = html.escape(lang_norm.upper() if lang else "CODE")
            code_highlighted = highlight_code(raw_code)
            out.append(
                f'<div class="language-{html.escape(lang_norm)} highlighter-rouge">'
                f'<span class="code-label" aria-hidden="true">{lang_badge}</span>'
                f'<div class="highlight"><pre class="highlight"><code>{code_highlighted}</code></pre></div>'
                f"</div>"
            )
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_lines: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(f"<blockquote><p>{format_inline(' '.join(bq_lines))}</p></blockquote>")
            continue

        # Table -> direct <table> inside .prose (matching prototype post.html)
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|\s*[-:]+", lines[i + 1].strip()):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < n and lines[i].strip().startswith("|"):
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row_cells)
                i += 1
            th_html = "".join(f"<th>{format_inline(c)}</th>" for c in header_cells)
            trs_html = [
                f'<tr>{"".join(f"<td>{format_inline(c)}</td>" for c in row)}</tr>'
                for row in rows
            ]
            out.append(
                f'<table><thead><tr>{th_html}</tr></thead>'
                f'<tbody>{"".join(trs_html)}</tbody></table>'
            )
            continue

        # Heading h3
        if stripped.startswith("### "):
            h3_counter += 1
            raw_h3 = stripped[4:].strip()
            clean_h3 = normalize_h3_title(raw_h3)
            h3_id = f"{h3_prefix}-{h3_counter}"
            h3_inline = format_inline(clean_h3)
            out.append(
                f'<h3 id="{h3_id}">{h3_inline}'
                f'<a class="anchor" href="#{h3_id}" aria-label="本节链接">#</a></h3>'
            )
            if toc_accumulator is not None:
                short_toc = strip_html_tags(h3_inline)
                if len(short_toc) > 26:
                    short_toc = short_toc[:25] + "…"
                toc_accumulator.append({"id": h3_id, "level": "l3", "title": short_toc})
            i += 1
            continue

        # Unordered or Ordered List
        ul_match = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        ol_match = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if ul_match or ol_match:
            is_ol = bool(ol_match)
            tag = "ul" if force_ul_top else ("ol" if is_ol else "ul")
            items_html: list[str] = []

            while i < n:
                cur = lines[i]
                cur_strip = cur.strip()
                if not cur_strip:
                    i += 1
                    continue
                m_ul = re.match(r"^(\s*)[-*]\s+(.*)$", cur)
                m_ol = re.match(r"^(\s*)(\d+)\.\s+(.*)$", cur)
                if is_ol and m_ol and len(m_ol.group(1)) == 0:
                    item_body = format_inline(m_ol.group(3))
                    i += 1
                    sub_lines: list[str] = []
                    while i < n and (lines[i].startswith("  ") or lines[i].startswith("\t") or not lines[i].strip()):
                        if not lines[i].strip():
                            j = i + 1
                            while j < n and not lines[j].strip():
                                j += 1
                            if j < n and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                                sub_lines.append("")
                                i += 1
                                continue
                            break
                        sub_lines.append(re.sub(r"^(?: {1,4}|\t)", "", lines[i]))
                        i += 1
                    sub_html = render_blocks(sub_lines) if sub_lines else ""
                    items_html.append(f"<li>{item_body}{sub_html}</li>")
                elif (not is_ol) and m_ul and len(m_ul.group(1)) == 0:
                    raw_text = m_ul.group(2)
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
                            break
                        sub_lines.append(re.sub(r"^(?: {1,2}|\t)", "", lines[i]))
                        i += 1
                    sub_html = render_blocks(sub_lines) if sub_lines else ""
                    items_html.append(f"<li>{format_inline(raw_text)}{sub_html}</li>")
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


def parse_learn_article(art: dict[str, Any]) -> tuple[list[dict[str, str]], str, int]:
    """Parse a /learn/ article into quiet editorial prose (blockquote TL;DR + h2/h3 Q&A + ul checklist + h2/table)."""
    toc_items: list[dict[str, str]] = []
    prose_parts: list[str] = []
    sec_counter = 0
    total_chars = 0

    for src_idx, rel_path in enumerate(art["sources"]):
        full_path = VAULT_DIR / rel_path
        raw_md = full_path.read_text(encoding="utf-8")
        body_md = strip_frontmatter_and_h1(raw_md)
        total_chars += len(re.sub(r"\s+", "", body_md))

        lines = body_md.splitlines()
        cur_h2: str | None = None
        cur_lines: list[str] = []

        def flush_sec() -> None:
            nonlocal sec_counter
            if cur_h2 is None:
                return
            clean_h2 = normalize_h2_title(cur_h2, is_companion=(src_idx > 0))

            # 1. TL;DR -> quiet blockquote at the top of the article (or companion section)
            if clean_h2 == "一句话结论":
                bq_text_lines: list[str] = []
                for ln in cur_lines:
                    s = ln.strip()
                    if s and s != "---":
                        bq_text_lines.append(re.sub(r"^>\s?", "", s))
                joined = format_inline(" ".join(bq_text_lines))
                prose_parts.append(
                    f"<blockquote><p><strong>一句话结论</strong>：{joined}</p></blockquote>"
                )
                return

            if clean_h2 == "附篇一句话结论":
                sec_counter += 1
                sec_id = f"sec-{sec_counter}"
                toc_items.append({"id": sec_id, "level": "l2", "title": "叙事与制作拆解"})
                bq_text_lines = []
                for ln in cur_lines:
                    s = ln.strip()
                    if s and s != "---":
                        bq_text_lines.append(re.sub(r"^>\s?", "", s))
                joined = format_inline(" ".join(bq_text_lines))
                prose_parts.append(
                    f'<h2 id="{sec_id}">叙事与制作拆解<a class="anchor" href="#{sec_id}" aria-label="本节链接">#</a></h2>\n'
                    f"<blockquote><p><strong>一句话结论</strong>：{joined}</p></blockquote>"
                )
                return

            sec_counter += 1
            sec_id = f"sec-{sec_counter}"
            toc_items.append({"id": sec_id, "level": "l2", "title": strip_html_tags(format_inline(clean_h2))})
            heading_html = (
                f'<h2 id="{sec_id}">{format_inline(clean_h2)}'
                f'<a class="anchor" href="#{sec_id}" aria-label="本节链接">#</a></h2>'
            )
            is_checklist = clean_h2 == "立即可用清单"
            body_html = render_blocks(
                cur_lines,
                force_ul_top=is_checklist,
                toc_accumulator=toc_items,
                h3_prefix=sec_id,
            )
            prose_parts.append(f"{heading_html}\n{body_html}")

        for line in lines:
            if line.startswith("## "):
                flush_sec()
                cur_h2 = line[3:].strip()
                cur_lines = []
            else:
                cur_lines.append(line)
        flush_sec()

    approx_words = max(800, round(total_chars / 100) * 100)
    return toc_items, "\n".join(prose_parts), approx_words


def unquote_yaml(val: str) -> str:
    v = val.strip()
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
        return v[1:-1]
    return v


def parse_thought_markdown(path: Path) -> dict[str, Any]:
    raw_text = path.read_text(encoding="utf-8").strip()
    meta: dict[str, Any] = {
        "title": path.stem,
        "subtitle": "",
        "slug": path.stem,
        "date": "2026-11-09",
        "category": "思考与感悟",
        "reading_time": "阅读约 3 分钟",
        "tags": [],
        "insight": "",
    }
    body = raw_text
    if raw_text.startswith("---"):
        parts = raw_text.split("---", 2)
        if len(parts) == 3:
            fm_lines = parts[1].splitlines()
            body = parts[2].strip()
            current_list_key: str | None = None
            for raw_line in fm_lines:
                line = raw_line.rstrip()
                if not line.strip() or line.strip().startswith("#"):
                    continue
                m_item = re.match(r"^\s*-\s+(.*)$", line)
                if m_item and current_list_key:
                    meta.setdefault(current_list_key, []).append(unquote_yaml(m_item.group(1)))
                    continue
                m_kv = re.match(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$", line)
                if m_kv:
                    key = m_kv.group(1).strip()
                    val = m_kv.group(2).strip()
                    if not val:
                        current_list_key = key
                        meta[key] = []
                    elif val.startswith("[") and val.endswith("]"):
                        current_list_key = None
                        inner = val[1:-1].strip()
                        meta[key] = [unquote_yaml(x) for x in inner.split(",") if x.strip()] if inner else []
                    else:
                        current_list_key = None
                        meta[key] = unquote_yaml(val)

    out_lines: list[str] = []
    skipped_h1 = False
    for line in body.splitlines():
        if not skipped_h1 and line.startswith("# "):
            if meta["title"] == path.stem:
                meta["title"] = line[2:].strip()
            skipped_h1 = True
            continue
        out_lines.append(line)

    clean_body = "\n".join(out_lines).strip()
    total_chars = len(re.sub(r"\s+", "", clean_body))
    approx_words = max(500, round(total_chars / 100) * 100)

    toc_items: list[dict[str, str]] = []
    prose_parts: list[str] = []

    if meta.get("insight"):
        prose_parts.append(
            f"<blockquote><p><strong>一句话结论</strong>：{format_inline(str(meta['insight']))}</p></blockquote>"
        )

    intro_lines: list[str] = []
    cur_h2: str | None = None
    cur_lines: list[str] = []
    sec_idx = 0

    def flush_sec() -> None:
        nonlocal sec_idx
        if cur_h2 is None:
            return
        sec_idx += 1
        sec_id = f"sec-{sec_idx}"
        clean_title = strip_emoji(cur_h2)
        toc_items.append({"id": sec_id, "level": "l2", "title": strip_html_tags(format_inline(clean_title))})
        heading_html = (
            f'<h2 id="{sec_id}">{format_inline(clean_title)}'
            f'<a class="anchor" href="#{sec_id}" aria-label="本节链接">#</a></h2>'
        )
        body_html = render_blocks(cur_lines, toc_accumulator=toc_items, h3_prefix=sec_id)
        prose_parts.append(f"{heading_html}\n{body_html}")

    for line in clean_body.splitlines():
        if line.startswith("## "):
            if cur_h2 is None and intro_lines:
                prose_parts.append(render_blocks(intro_lines))
                intro_lines = []
            else:
                flush_sec()
            cur_h2 = line[3:].strip()
            cur_lines = []
        else:
            if cur_h2 is None:
                intro_lines.append(line)
            else:
                cur_lines.append(line)

    if cur_h2 is None and intro_lines:
        prose_parts.append(render_blocks(intro_lines))
    else:
        flush_sec()

    rt = str(meta.get("reading_time") or "约 3 分钟")
    if not rt.startswith("阅读"):
        rt = f"阅读{rt}"

    return {
        "series": "thoughts",
        "series_label": "思考",
        "slug": str(meta["slug"]),
        "aliases": [],
        "url": f"/thoughts/{meta['slug']}/",
        "title": strip_emoji(str(meta["title"])),
        "short_title": strip_emoji(str(meta["title"])),
        "lede": strip_emoji(str(meta.get("subtitle") or meta.get("insight") or "")),
        "teaser": strip_emoji(str(meta.get("insight") or meta.get("subtitle") or "")),
        "date": str(meta.get("date") or "2026-11-09"),
        "reading_time": rt,
        "category": strip_emoji(str(meta.get("category") or "思考与感悟")),
        "tags": [strip_emoji(t) for t in (meta.get("tags") or [])],
        "toc": toc_items,
        "prose_html": "\n".join(prose_parts),
        "words": approx_words,
    }


def render_shell_page(*, title: str, description: str, active_nav: str, main_html: str) -> str:
    """Render prototype HTML shell (strictly starting with <!doctype html>, zero YAML frontmatter)."""
    nav_links: list[str] = []
    for key, label, href in NAV_ITEMS:
        curr = ' aria-current="page"' if key == active_nav else ""
        nav_links.append(f'<a href="{href}"{curr}>{html.escape(label)}</a>')

    full_title = title if "Lee Pepe" in title else f"{title} · Lee Pepe"

    return f"""<!doctype html>
<html lang="zh-CN" data-lp-theme="light" data-strata-brand="yellow" data-strata-material="glass">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<link rel="alternate" type="application/atom+xml" title="Lee Pepe · RSS 订阅" href="/feed.xml">
<script src="/assets/theme.js"></script>
<link rel="stylesheet" href="/assets/colors.css">
<link rel="stylesheet" href="/assets/strata-theme.css">
<link rel="stylesheet" href="/assets/blog.css">
</head>
<body>
<a class="skip-link" href="#main">跳到正文</a>
<div class="ambient" aria-hidden="true"><span class="a1"></span><span class="a2"></span></div>
<header class="site-header shell">
  <div class="site-header__bar">
    <a class="brand" href="/"><span class="brand__mark" aria-hidden="true">L</span>Lee Pepe</a>
    <nav class="nav" aria-label="主导航">{"".join(nav_links)}</nav>
    <div class="theme-toggle" role="group" aria-label="外观"><button type="button" data-theme-choice="light" aria-pressed="false" title="浅色"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="8" cy="8" r="3"/><path d="M8 1.5v1.5M8 13v1.5M1.5 8H3M13 8h1.5M3.4 3.4l1 1M11.6 11.6l1 1M3.4 12.6l1-1M11.6 4.4l1-1"/></svg><span class="label">浅色</span><span class="visually-hidden">主题</span></button><button type="button" data-theme-choice="dark" aria-pressed="false" title="深色"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><path d="M13.5 9.5A5.5 5.5 0 0 1 6.5 2.5a5.5 5.5 0 1 0 7 7Z"/></svg><span class="label">深色</span><span class="visually-hidden">主题</span></button><button type="button" data-theme-choice="system" aria-pressed="true" title="系统"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><rect x="1.75" y="2.75" width="12.5" height="8.5" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg><span class="label">系统</span><span class="visually-hidden">主题</span></button></div>
  </div>
</header>
<main id="main" class="shell">
{main_html}
</main>
<footer class="site-footer">
  <div class="shell">
    <span>© 2026 Lee Pepe · 写代码，也写生活</span>
    <nav aria-label="页脚"><a href="/feed.xml">RSS 订阅</a><a href="https://github.com/LeePepe">GitHub</a><a href="#main">回到顶部</a></nav>
  </div>
</footer>
</body>
</html>
"""


def render_post_list_items(items: list[dict[str, Any]], tag_id_map: dict[str, str]) -> str:
    lis: list[str] = []
    for item in items:
        cn_date = format_cn_date(item["date"])
        tags_li = "".join(
            f'<li><a class="tag" href="/tags/#{tag_id_map[t]}">{html.escape(t)}</a></li>'
            for t in item["tags"][:3]
            if t in tag_id_map
        )
        lis.append(
            f'<li class="post-item">\n'
            f'  <div class="post-meta"><time datetime="{html.escape(item["date"])}">{html.escape(cn_date)}</time>'
            f'<span class="dot" aria-hidden="true">·</span><span>{html.escape(item["series_label"])}</span>'
            f'<span class="dot" aria-hidden="true">·</span><span>{html.escape(item["reading_time"])}</span></div>\n'
            f'  <h2><a href="{html.escape(item["url"])}">{html.escape(item["title"])}</a></h2>\n'
            f'  <p>{html.escape(item["teaser"])}</p>\n'
            f'  <ul class="tags" aria-label="标签">{tags_li}</ul>\n'
            f"</li>"
        )
    return "\n".join(lis)


def render_top_tags_ul(
    sorted_tags: list[tuple[str, list[dict[str, Any]]]],
    tag_id_map: dict[str, str],
    limit: int | None = 8,
) -> str:
    slice_tags = sorted_tags[:limit] if limit is not None else sorted_tags
    lis = [
        f'<li><a class="tag" href="/tags/#{tag_id_map[t]}">{html.escape(t)} <span class="count">{len(arts)}</span></a></li>'
        for t, arts in slice_tags
    ]
    return f'<ul class="tags">{"".join(lis)}</ul>'


def build_home_page(
    all_items: list[dict[str, Any]],
    learn_items: list[dict[str, Any]],
    thought_items: list[dict[str, Any]],
    sorted_tags: list[tuple[str, list[dict[str, Any]]]],
    tag_id_map: dict[str, str],
) -> None:
    list_html = render_post_list_items(all_items, tag_id_map)
    top_tags_html = render_top_tags_ul(sorted_tags, tag_id_map, limit=8)

    main_html = f"""  <section class="page-intro">
    <h1>写代码，也写生活</h1>
    <p>记录苹果生态开发、AI 多智能体工程、求知拆解与日常思考。</p>
  </section>
  <div class="layout">
    <section class="card card--flush" aria-labelledby="latest">
      <h2 id="latest" class="visually-hidden">最新文章</h2>
      <ol class="post-list">
{list_html}
      </ol>
    </section>
    <aside class="aside" aria-label="侧栏">
      <section class="card">
        <div class="profile"><span class="avatar" aria-hidden="true">L</span><div><h2>Lee Pepe</h2><div class="post-meta">iOS · 前端 · 跑步</div></div></div>
        <p>做过 iOS、自然语言和前端。从 210 斤减到 150 斤，喜欢健身、跑步和篮球。</p>
        <a class="btn btn--secondary" href="/about/">关于我</a>
      </section>
      <section class="card">
        <h2>专栏</h2>
        <p>「求知」用生活教具拆穿技术原理（{len(learn_items)} 篇）；「思考」记录日常工具与生活随笔（{len(thought_items)} 篇）。</p>
        <div class="links">
          <a class="btn btn--secondary" href="/learn/">求知笔记 ({len(learn_items)})</a>
          <a class="btn btn--secondary" href="/thoughts/">思考与感悟 ({len(thought_items)})</a>
        </div>
      </section>
      <section class="card">
        <h2>热门标签</h2>
        {top_tags_html}
        <p style="margin-top:16px;margin-bottom:0"><a href="/tags/">查看全部标签 →</a></p>
      </section>
    </aside>
  </div>"""

    html_out = render_shell_page(
        title="首页 · Lee Pepe",
        description="Lee Pepe 的个人博客：记录苹果生态开发、AI 多智能体工程、求知拆解与日常思考。",
        active_nav="home",
        main_html=main_html,
    )
    (REPO_ROOT / "index.html").write_text(html_out, encoding="utf-8")


def build_series_list_page(
    *,
    out_path: Path,
    active_nav: str,
    title: str,
    intro: str,
    items: list[dict[str, Any]],
    aside_title: str,
    aside_desc: str,
    tag_id_map: dict[str, str],
) -> None:
    list_html = render_post_list_items(items, tag_id_map)

    series_tags: dict[str, int] = {}
    for it in items:
        for t in it["tags"]:
            series_tags[t] = series_tags.get(t, 0) + 1
    series_tag_lis = "".join(
        f'<li><a class="tag" href="/tags/#{tag_id_map[t]}">{html.escape(t)} <span class="count">{cnt}</span></a></li>'
        for t, cnt in series_tags.items()
        if t in tag_id_map
    )

    main_html = f"""  <section class="page-intro">
    <h1>{html.escape(title)}</h1>
    <p>{html.escape(intro)}</p>
  </section>
  <div class="layout">
    <section class="card card--flush" aria-labelledby="series-list-heading">
      <h2 id="series-list-heading" class="visually-hidden">{html.escape(title)}文章列表</h2>
      <ol class="post-list">
{list_html}
      </ol>
    </section>
    <aside class="aside" aria-label="侧栏">
      <section class="card">
        <h2>{html.escape(aside_title)}</h2>
        <p>{html.escape(aside_desc)}</p>
        <div class="links">
          <a class="btn btn--secondary" href="/archive/">查看全站归档</a>
          <a class="btn btn--ghost" href="/">回首页</a>
        </div>
      </section>
      <section class="card">
        <h2>本栏标签</h2>
        <ul class="tags">{series_tag_lis}</ul>
        <p style="margin-top:16px;margin-bottom:0"><a href="/tags/">查看全部标签 →</a></p>
      </section>
      <section class="card">
        <h2>订阅</h2>
        <p>新文章通过 RSS 推送，没有邮件、没有追踪。</p>
        <a class="btn btn--primary" href="/feed.xml">订阅 RSS</a>
      </section>
    </aside>
  </div>"""

    html_out = render_shell_page(
        title=f"{title} · Lee Pepe",
        description=intro,
        active_nav=active_nav,
        main_html=main_html,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_out, encoding="utf-8")


def build_post_pages(
    items: list[dict[str, Any]],
    *,
    active_nav: str,
    back_href: str,
    back_label: str,
    base_dir: Path,
    tag_id_map: dict[str, str],
) -> None:
    total = len(items)
    for idx, item in enumerate(items):
        prev_item = items[idx - 1] if idx > 0 else None
        next_item = items[idx + 1] if idx + 1 < total else None

        tags_li = "".join(
            f'<li><a class="tag" href="/tags/#{tag_id_map[t]}">{html.escape(t)}</a></li>'
            for t in item["tags"]
            if t in tag_id_map
        )
        cn_date = format_cn_date(item["date"])
        words_str = f"约 {item['words']:,} 字"

        toc_lis: list[str] = []
        for t_idx, toc_entry in enumerate(item["toc"]):
            curr_attr = ' aria-current="true"' if t_idx == 0 else ""
            toc_lis.append(
                f'<li class="{toc_entry["level"]}"><a href="#{toc_entry["id"]}"{curr_attr}>{html.escape(toc_entry["title"])}</a></li>'
            )

        nav_cards: list[str] = []
        if prev_item:
            nav_cards.append(
                f'<a class="prev" href="{html.escape(prev_item["url"])}">'
                f'<span class="dir">← 上一篇</span><span class="t">{html.escape(prev_item["title"])}</span></a>'
            )
        if next_item:
            nav_cards.append(
                f'<a class="next" href="{html.escape(next_item["url"])}">'
                f'<span class="dir">下一篇 →</span><span class="t">{html.escape(next_item["title"])}</span></a>'
            )
        post_nav_html = (
            f'<nav class="post-nav" aria-label="上一篇和下一篇">{"".join(nav_cards)}</nav>'
            if nav_cards
            else ""
        )

        main_html = f"""  <div class="post-layout">
    <div>
      <a class="btn btn--ghost back-link" href="{html.escape(back_href)}"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3.5 5.5 8l4.5 4.5"/></svg>{html.escape(back_label)}</a>
      <article class="card article">
        <header class="article-header">
          <ul class="tags" aria-label="标签">{tags_li}</ul>
          <h1>{html.escape(item["title"])}</h1>
          <p class="lede">{html.escape(item["lede"])}</p>
          <div class="post-meta"><time datetime="{html.escape(item["date"])}">{html.escape(cn_date)}</time><span class="dot" aria-hidden="true">·</span><span>{html.escape(words_str)}</span><span class="dot" aria-hidden="true">·</span><span>{html.escape(item["reading_time"])}</span></div>
        </header>
        <div class="prose">
{item["prose_html"]}
        </div>
        {post_nav_html}
        <div class="post-end"><a class="btn btn--secondary" href="{html.escape(back_href)}"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3.5 5.5 8l4.5 4.5"/></svg>{html.escape(back_label)}</a></div>
      </article>
    </div>
    <aside class="toc" aria-label="本文目录">
      <p class="section-label">目录</p>
      <ol>{"".join(toc_lis)}</ol>
    </aside>
  </div>"""

        html_out = render_shell_page(
            title=f"{item['title']} · Lee Pepe",
            description=item["teaser"],
            active_nav=active_nav,
            main_html=main_html,
        )
        slug_dir = base_dir / item["slug"]
        slug_dir.mkdir(parents=True, exist_ok=True)
        (slug_dir / "index.html").write_text(html_out, encoding="utf-8")

        for alias in item.get("aliases", []):
            alias_dir = base_dir / alias
            alias_dir.mkdir(parents=True, exist_ok=True)
            (alias_dir / "index.html").write_text(html_out, encoding="utf-8")


def build_archive_page(
    all_items: list[dict[str, Any]],
    sorted_tags: list[tuple[str, list[dict[str, Any]]]],
    tag_id_map: dict[str, str],
) -> None:
    by_year: dict[str, list[dict[str, Any]]] = {}
    for item in all_items:
        by_year.setdefault(item["date"][:4], []).append(item)

    year_sections: list[str] = []
    for yr in sorted(by_year.keys(), reverse=True):
        yr_items = by_year[yr]
        lis: list[str] = []
        for it in yr_items:
            mm_dd = it["date"][5:]
            tags_li = "".join(
                f'<li><a class="tag" href="/tags/#{tag_id_map[t]}">{html.escape(t)}</a></li>'
                for t in it["tags"][:2]
                if t in tag_id_map
            )
            lis.append(
                f'<li><time datetime="{html.escape(it["date"])}">{html.escape(mm_dd)}</time>'
                f'<a class="title" href="{html.escape(it["url"])}">{html.escape(it["title"])}</a>'
                f'<ul class="tags" aria-label="标签">{tags_li}</ul></li>'
            )
        year_sections.append(
            f'<section class="year" aria-labelledby="y{yr}">'
            f'<h2 id="y{yr}">{yr}<span class="count">{len(yr_items)} 篇</span></h2>'
            f'<ol class="archive-list">{"".join(lis)}</ol></section>'
        )

    all_tags_html = render_top_tags_ul(sorted_tags, tag_id_map, limit=None)

    main_html = f"""  <section class="page-intro">
    <h1>归档</h1>
    <p>共 {len(all_items)} 篇，按年份倒序排列。</p>
  </section>
  <div class="layout">
    <div class="card archive">{"".join(year_sections)}</div>
    <aside class="aside" aria-label="侧栏">
      <section class="card"><h2>按标签找</h2><p>点标签只看这一类文章。</p>
        {all_tags_html}
      </section>
    </aside>
  </div>"""

    html_out = render_shell_page(
        title="归档 · Lee Pepe",
        description="Lee Pepe 的个人博客文章时间轴归档。",
        active_nav="archive",
        main_html=main_html,
    )
    (REPO_ROOT / "archive" / "index.html").write_text(html_out, encoding="utf-8")


def build_tags_page(
    sorted_tags: list[tuple[str, list[dict[str, Any]]]],
    tag_id_map: dict[str, str],
) -> None:
    filter_lis: list[str] = []
    sections_html: list[str] = []

    for idx, (tag_name, items) in enumerate(sorted_tags):
        tid = tag_id_map[tag_name]
        curr = ' aria-current="true"' if idx == 0 else ""
        filter_lis.append(
            f'<li><a class="tag" href="#{tid}"{curr}>{html.escape(tag_name)} <span class="count">{len(items)}</span></a></li>'
        )

        by_year: dict[str, list[dict[str, Any]]] = {}
        for it in items:
            by_year.setdefault(it["date"][:4], []).append(it)

        year_blocks: list[str] = []
        for yr in sorted(by_year.keys(), reverse=True):
            lis = "".join(
                f'<li><time datetime="{html.escape(it["date"])}">{html.escape(it["date"][5:])}</time>'
                f'<a class="title" href="{html.escape(it["url"])}">{html.escape(it["title"])}</a></li>'
                for it in by_year[yr]
            )
            year_blocks.append(
                f'<h3 class="section-label" style="margin-top:12px">{yr}</h3>'
                f'<ol class="archive-list">{lis}</ol>'
            )

        sections_html.append(
            f'<section class="year tag-section" id="{tid}" aria-labelledby="h{tid}">'
            f'<h2 id="h{tid}">#{html.escape(tag_name)}<span class="count">{len(items)} 篇</span></h2>'
            f'{"".join(year_blocks)}</section>'
        )

    main_html = f"""  <section class="page-intro">
    <h1>标签</h1>
    <p>{len(sorted_tags)} 个标签，每个标签下按年份分组。</p>
  </section>
  <div class="card filter-bar"><p class="section-label">全部标签</p><ul class="tags">{"".join(filter_lis)}</ul></div>
  <div class="card archive">{"".join(sections_html)}</div>"""

    html_out = render_shell_page(
        title="标签 · Lee Pepe",
        description="Lee Pepe 的个人博客标签索引。",
        active_nav="tags",
        main_html=main_html,
    )
    (REPO_ROOT / "tags" / "index.html").write_text(html_out, encoding="utf-8")


def build_about_page(learn_count: int, thought_count: int) -> None:
    main_html = f"""  <div class="about">
    <article class="card article">
      <div class="about-head">
        <span class="avatar avatar--lg" aria-hidden="true">L</span>
        <div><h1>你好，我是 Lee Pepe</h1><p>iOS 开发者，也写前端和 AI 工作流。</p></div>
      </div>
      <ul class="facts">
        <li><span class="k">减重</span><span class="v">60 斤</span></li>
        <li><span class="k">写博客始于</span><span class="v">2016 年</span></li>
        <li><span class="k">全站专栏文章</span><span class="v">{learn_count + thought_count} 篇</span></li>
      </ul>
      <div class="prose">
        <p>描述一下我？我也不太知道怎么描述。生活里从 210 斤减到现在的 150 斤，喜欢健身、跑步、篮球，想去试试跑酷。</p>
        <p>毕业后一直在写代码：iOS、自然语言、前端都做过。最近在用多个 AI agent 协作做个人项目，也在学心理学。</p>
        <h2 id="columns">博客专栏</h2>
        <ul>
          <li><strong><a href="/learn/">求知笔记（{learn_count} 篇）</a></strong>：把抽象的工程架构与科学原理拆成生活教具，按「一句话结论 → 核心痛点问答 → 立即可用清单 → 叙事与制作拆解」沉淀。</li>
          <li><strong><a href="/thoughts/">思考与感悟（{thought_count} 篇）</a></strong>：记录日常折腾智能家居、减法工具设计与生活习惯时的真实随笔。</li>
        </ul>
        <h2 id="now">现在在做</h2>
        <ul>
          <li><strong>VitalStride</strong>：记录训练和身体数据的 App。</li>
          <li><strong>AIDash</strong>：每天一份 AI 资讯简报。</li>
          <li><strong>Strata</strong>：给这些项目共用的一套设计系统，也是这个博客的样子。</li>
        </ul>
        <h2 id="contact">联系我</h2>
        <p>最快的方式是在 GitHub 上提 issue，或者订阅 RSS 看新文章。</p>
      </div>
      <div class="links">
        <a class="btn btn--primary" href="https://github.com/LeePepe">GitHub @LeePepe</a>
        <a class="btn btn--secondary" href="/feed.xml">订阅 RSS</a>
      </div>
    </article>
  </div>"""

    html_out = render_shell_page(
        title="关于 · Lee Pepe",
        description="关于 Lee Pepe：从 210 斤到 150 斤，写代码也写生活。",
        active_nav="about",
        main_html=main_html,
    )
    (REPO_ROOT / "about" / "index.html").write_text(html_out, encoding="utf-8")


def build_404_page() -> None:
    main_html = """  <section class="card card--flush">
    <div class="empty-state">
      <span class="empty-state__mark" aria-hidden="true">404</span>
      <h1>找不到这一页</h1>
      <p>链接可能写错了，或者文章已经挪走。回首页看看最新的几篇，或者按标签翻。</p>
      <div class="empty-state__actions"><a class="btn btn--primary" href="/">回首页</a><a class="btn btn--secondary" href="/archive/">看归档</a><a class="btn btn--ghost" href="/tags/">按标签找</a></div>
    </div>
  </section>"""

    html_out = render_shell_page(
        title="页面不存在 · Lee Pepe",
        description="页面不存在 — 返回首页、查看归档或按标签浏览。",
        active_nav="",
        main_html=main_html,
    )
    (REPO_ROOT / "404.html").write_text(html_out, encoding="utf-8")


def build_feed_xml(all_items: list[dict[str, Any]]) -> None:
    updated_iso = f"{all_items[0]['date']}T08:00:00+08:00" if all_items else datetime.now(timezone.utc).isoformat()
    entries_xml: list[str] = []
    for item in all_items:
        full_url = f"{SITE_URL}{item['url']}"
        item_iso = f"{item['date']}T08:00:00+08:00"
        cats = "".join(f'<category term="{html.escape(t, quote=True)}"/>' for t in item["tags"])
        entries_xml.append(
            f"""  <entry>
    <title>{html.escape(item["title"])}</title>
    <link href="{html.escape(full_url, quote=True)}" rel="alternate" type="text/html"/>
    <id>{html.escape(full_url)}</id>
    <published>{item_iso}</published>
    <updated>{item_iso}</updated>
    <author><name>Lee Pepe</name></author>
    {cats}
    <summary type="html">{html.escape(item["teaser"])}</summary>
  </entry>"""
        )

    feed_xml = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Lee Pepe · 写代码，也写生活</title>
  <subtitle>求知笔记（/learn/）与思考与感悟（/thoughts/）</subtitle>
  <link href="{SITE_URL}/feed.xml" rel="self" type="application/atom+xml"/>
  <link href="{SITE_URL}/" rel="alternate" type="text/html"/>
  <id>{SITE_URL}/</id>
  <updated>{updated_iso}</updated>
  <author>
    <name>Lee Pepe</name>
    <email>1105208297@qq.com</email>
  </author>
{chr(10).join(entries_xml)}
</feed>
"""
    (REPO_ROOT / "feed.xml").write_text(feed_xml, encoding="utf-8")


def main() -> None:
    learn_items: list[dict[str, Any]] = []
    for art in LEARN_ARTICLES:
        toc, prose_html, words = parse_learn_article(art)
        learn_items.append(
            {
                "series": "learn",
                "series_label": "求知",
                "num": art["num"],
                "slug": art["slug"],
                "aliases": art.get("aliases", []),
                "url": f"/learn/{art['slug']}/",
                "title": strip_emoji(art["title"]),
                "short_title": strip_emoji(art["short_title"]),
                "lede": strip_emoji(art["teaser"]),
                "teaser": strip_emoji(art["teaser"]),
                "date": art["updated"],
                "reading_time": art["reading_time"],
                "category": strip_emoji(art["category"]),
                "tags": [strip_emoji(t) for t in art["tags"]],
                "toc": toc,
                "prose_html": prose_html,
                "words": words,
            }
        )

    thought_items: list[dict[str, Any]] = []
    for md_path in sorted(VAULT_THOUGHTS_DIR.glob("*.md")):
        thought_items.append(parse_thought_markdown(md_path))
    thought_items.sort(key=lambda x: x["date"], reverse=True)

    all_items = thought_items + learn_items
    all_items.sort(key=lambda x: (x["date"], 1 if x["series"] == "thoughts" else 0), reverse=True)

    tag_map: dict[str, list[dict[str, Any]]] = {}
    for item in all_items:
        for t in item["tags"]:
            tag_map.setdefault(t, []).append(item)

    sorted_tags = sorted(tag_map.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    tag_id_map = {t: f"t{idx}" for idx, (t, _) in enumerate(sorted_tags)}

    build_home_page(all_items, learn_items, thought_items, sorted_tags, tag_id_map)

    build_series_list_page(
        out_path=LEARN_DIR / "index.html",
        active_nav="learn",
        title="求知笔记",
        intro="用生活教具拆穿抽象技术与物理原理：先给一句话结论，再答核心痛点，最后附立即可用清单。",
        items=learn_items,
        aside_title="关于求知笔记",
        aside_desc="每篇笔记围绕一个具体技术或科学主题，砍掉八股铺垫，按「一句话结论 · 核心痛点问答 · 立即可用清单 · 叙事与制作拆解」四段式整理。",
        tag_id_map=tag_id_map,
    )

    build_series_list_page(
        out_path=THOUGHTS_DIR / "index.html",
        active_nav="thoughts",
        title="思考与感悟",
        intro="记录日常折腾智能家居、减法工具设计与生活习惯时的真实随笔。",
        items=thought_items,
        aside_title="关于思考与感悟",
        aside_desc="不追求大而全的系统宏图，只记录那些真正让手头工作和生活变顺手的一点顿悟。",
        tag_id_map=tag_id_map,
    )

    build_post_pages(
        learn_items,
        active_nav="learn",
        back_href="/learn/",
        back_label="返回求知笔记",
        base_dir=LEARN_DIR,
        tag_id_map=tag_id_map,
    )

    build_post_pages(
        thought_items,
        active_nav="thoughts",
        back_href="/thoughts/",
        back_label="返回思考与感悟",
        base_dir=THOUGHTS_DIR,
        tag_id_map=tag_id_map,
    )

    build_archive_page(all_items, sorted_tags, tag_id_map)
    build_tags_page(sorted_tags, tag_id_map)
    build_about_page(len(learn_items), len(thought_items))
    build_404_page()
    build_feed_xml(all_items)

    print(
        f"Built unified quiet editorial site: {len(learn_items)} learn posts, "
        f"{len(thought_items)} thought posts, {len(sorted_tags)} tags."
    )


if __name__ == "__main__":
    main()
