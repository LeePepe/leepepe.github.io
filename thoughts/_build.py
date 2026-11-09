#!/usr/bin/env python3
"""
Build script for /thoughts/ (思考与感悟 · Thoughts & Reflections).
Pure display renderer: automatically scans all *.md files in
~/Development/Personal/knowledge-vault/thoughts/, parses YAML frontmatter and
Markdown essay prose, and generates zero-dependency Warm Editorial HTML pages
under thoughts/index.html and thoughts/<slug>/index.html.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path
from typing import Any

THOUGHTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THOUGHTS_DIR.parent
VAULT_THOUGHTS_DIR = Path.home() / "Development" / "Personal" / "knowledge-vault" / "thoughts"


def asset_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def unquote_yaml(val: str) -> str:
    v = val.strip()
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
        return v[1:-1]
    return v


def parse_frontmatter_and_body(md_text: str, fallback_slug: str) -> tuple[dict[str, Any], str]:
    text = md_text.strip()
    meta: dict[str, Any] = {
        "title": fallback_slug,
        "subtitle": "",
        "slug": fallback_slug,
        "date": "2026-11-09",
        "category": "思考与感悟",
        "reading_time": "约 3 分钟",
        "tags": [],
        "insight": "",
    }
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
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

    # Strip leading H1 if present (rendered in article header)
    out_lines: list[str] = []
    skipped_h1 = False
    for line in body.splitlines():
        if not skipped_h1 and line.startswith("# "):
            if meta["title"] == fallback_slug:
                meta["title"] = line[2:].strip()
            skipped_h1 = True
            continue
        out_lines.append(line)

    return meta, "\n".join(out_lines).strip()


_SYNTAX_KEYWORDS = {
    "swift", "func", "let", "var", "struct", "enum", "class", "protocol", "extension",
    "if", "else", "for", "in", "while", "switch", "case", "default", "return", "break",
    "continue", "guard", "where", "import", "private", "public", "internal", "fileprivate",
    "open", "static", "mutating", "async", "await", "throws", "try", "catch", "some", "any",
    "self", "Self", "super", "init", "deinit", "true", "false", "nil", "inout", "override",
    "final", "lazy", "weak", "unowned", "as", "is",
    "def", "from", "lambda", "with", "yield", "None", "True", "False", "and", "or", "not",
    "export", "function", "local", "echo", "fi", "then", "do", "done", "const",
}

_TOKEN_RE = re.compile(
    r"(?P<cmt>//[^\n]*|/\*[\s\S]*?\*/|#(?![include\w])[^\n]*)"
    r"|(?P<str>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')"
    r"|(?P<attr>@[A-Za-z_][A-Za-z0-9_]*|\[\[[A-Za-z0-9_:]+\]\])"
    r"|(?P<num>\b\d+(?:\.\d+)?(?:f|h|u|L|ms|s|px|rem|em|deg|%)?\b)"
    r"|(?P<ident>\b[A-Za-z_][A-Za-z0-9_]*\b)"
)


def highlight_code(code_str: str) -> str:
    out: list[str] = []
    last = 0
    for m in _TOKEN_RE.finditer(code_str):
        if m.start() > last:
            out.append(html.escape(code_str[last:m.start()]))
        tok = m.group(0)
        escaped = html.escape(tok)
        if m.group("cmt"):
            out.append(f'<span class="tok-cmt">{escaped}</span>')
        elif m.group("str"):
            out.append(f'<span class="tok-str">{escaped}</span>')
        elif m.group("attr"):
            out.append(f'<span class="tok-attr">{escaped}</span>')
        elif m.group("num"):
            out.append(f'<span class="tok-num">{escaped}</span>')
        elif m.group("ident"):
            after = code_str[m.end():m.end() + 1]
            before = code_str[max(0, m.start() - 1):m.start()]
            if tok in _SYNTAX_KEYWORDS:
                out.append(f'<span class="tok-kw">{escaped}</span>')
            elif tok[0].isupper():
                out.append(f'<span class="tok-type">{escaped}</span>')
            elif after == "(" or before == ".":
                out.append(f'<span class="tok-fn">{escaped}</span>')
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
    text = html.escape(text)

    def replace_link(match: re.Match[str]) -> str:
        label_raw = match.group(1)
        url_raw = html.unescape(match.group(2)).strip()
        label_html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", label_raw)
        return f'<a href="{html.escape(url_raw, quote=True)}">{label_html}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for idx, span in enumerate(code_spans):
        text = text.replace(f"\x00CODE{idx}\x00", span)

    return text


def render_blocks(lines: list[str]) -> str:
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

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
            lang_attr = f' class="language-{html.escape(lang_norm)}"' if lang else ' class="language-text"'
            out.append(
                f'<figure class="code-figure">'
                f'<figcaption class="code-topbar">'
                f'<span class="code-lang">{lang_badge}</span>'
                f'<button class="copy-code-btn" type="button" data-copy-code aria-label="复制代码">复制代码</button>'
                f"</figcaption>"
                f"<pre><code{lang_attr}>{code_highlighted}</code></pre>"
                f"</figure>"
            )
            continue

        if stripped.startswith(">"):
            bq_lines: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(f"<blockquote><p>{format_inline(' '.join(bq_lines))}</p></blockquote>")
            continue

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
                f'<div class="table-wrap"><table><thead><tr>{th_html}</tr></thead>'
                f'<tbody>{"".join(trs_html)}</tbody></table></div>'
            )
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{format_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        ul_match = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        ol_match = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if ul_match or ol_match:
            is_ol = bool(ol_match)
            tag = "ol" if is_ol else "ul"
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
                    items_html.append(f"<li>{item_body}</li>")
                elif (not is_ol) and m_ul and len(m_ul.group(1)) == 0:
                    item_body = format_inline(m_ul.group(2))
                    i += 1
                    items_html.append(f"<li>{item_body}</li>")
                else:
                    break
            if items_html:
                out.append(f"<{tag}>{''.join(items_html)}</{tag}>")
            continue

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


def parse_essay_sections(body_md: str) -> tuple[list[dict[str, str]], str]:
    lines = body_md.splitlines()
    outline: list[dict[str, str]] = []
    rendered_parts: list[str] = []
    intro_lines: list[str] = []
    cur_h2: str | None = None
    cur_lines: list[str] = []
    sec_idx = 0

    def flush_sec() -> None:
        nonlocal sec_idx
        if cur_h2 is None:
            return
        sec_idx += 1
        sec_id = f"section-{sec_idx}"
        clean_title = re.sub(r"^[一二三四五六七八九十]+、\s*", "", cur_h2).strip() or cur_h2
        outline.append({"id": sec_id, "title": clean_title})
        heading_html = (
            f'<h2 id="{sec_id}" tabindex="-1">'
            f'<span>{format_inline(cur_h2)}</span>'
            f'<button type="button" class="sec-anchor-btn" data-copy-anchor="#{sec_id}" '
            f'title="复制本节直达链接" aria-label="复制 {html.escape(clean_title)} 直达链接">#</button>'
            f"</h2>"
        )
        rendered_parts.append(f"{heading_html}\n{render_blocks(cur_lines)}")

    for line in lines:
        if line.startswith("## "):
            if cur_h2 is None and intro_lines:
                rendered_parts.append(render_blocks(intro_lines))
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
        rendered_parts.append(render_blocks(intro_lines))
    else:
        flush_sec()

    return outline, "\n".join(rendered_parts)


def load_all_thoughts() -> list[dict[str, Any]]:
    md_files = sorted(VAULT_THOUGHTS_DIR.glob("*.md"))
    raw_items: list[dict[str, Any]] = []
    for path in md_files:
        meta, body_md = parse_frontmatter_and_body(path.read_text(encoding="utf-8"), path.stem)
        outline, body_html = parse_essay_sections(body_md)
        raw_items.append(
            {
                "filename": path.name,
                "slug": str(meta.get("slug") or path.stem),
                "title": str(meta.get("title") or path.stem),
                "subtitle": str(meta.get("subtitle") or ""),
                "date": str(meta.get("date") or "2026-11-09"),
                "category": str(meta.get("category") or "思考与感悟"),
                "reading_time": str(meta.get("reading_time") or "约 3 分钟"),
                "tags": list(meta.get("tags") or []),
                "insight": str(meta.get("insight") or ""),
                "outline": outline,
                "body_html": body_html,
            }
        )

    # Sort by date descending, then filename ascending
    raw_items.sort(key=lambda x: x["filename"])
    raw_items.sort(key=lambda x: x["date"], reverse=True)

    for idx, item in enumerate(raw_items, start=1):
        item["num"] = f"{idx:02d}"
    return raw_items


def render_theme_switcher() -> str:
    return (
        '<div class="theme-segmented" role="group" aria-label="主题外观切换" data-theme-toggle>'
        '<button type="button" class="theme-seg-btn" data-theme-val="light" aria-pressed="false" title="浅色模式">☀️ 浅</button>'
        '<button type="button" class="theme-seg-btn" data-theme-val="dark" aria-pressed="false" title="深色模式">🌙 深</button>'
        '<button type="button" class="theme-seg-btn" data-theme-val="auto" aria-pressed="true" title="跟随系统自动切换">◐ 自</button>'
        "</div>"
    )


def render_search_box(is_mobile: bool = False) -> str:
    kbd_html = "" if is_mobile else '<kbd class="search-kbd" aria-hidden="true">/</kbd>'
    return (
        '<div class="rail-search-wrap">'
        '<div class="rail-search-field">'
        '<input type="search" class="rail-search" data-learn-search '
        'placeholder="搜索感悟随笔、核心洞察或标签… (按 /)" aria-label="搜索思考与感悟">'
        f"{kbd_html}"
        "</div>"
        '<div class="search-results" data-search-results hidden role="listbox" aria-label="搜索结果"></div>'
        "</div>"
    )


def build_nav_html(
    articles: list[dict[str, Any]],
    categories: list[str],
    current_slug: str | None,
    outline: list[dict[str, str]] | None,
    is_mobile: bool = False,
) -> str:
    groups_html: list[str] = []
    for cat_name in categories:
        cat_articles = [a for a in articles if a["category"] == cat_name]
        items_html: list[str] = []
        for art in cat_articles:
            is_curr = art["slug"] == current_slug
            li_cls = "chapter is-current" if is_curr else "chapter"
            aria_curr = ' aria-current="page"' if is_curr else ""
            outline_html = ""
            if is_curr and outline:
                ol_items = []
                for idx, sec in enumerate(outline):
                    loc_attr = ' aria-current="location"' if idx == 0 else ""
                    ol_items.append(
                        f'<li><a href="#{sec["id"]}"{loc_attr}>{html.escape(sec["title"])}</a></li>'
                    )
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
                f'<a class="chapter-link" href="/thoughts/{art["slug"]}/"{aria_curr}>'
                f'<span class="chapter-number">{art["num"]}</span>'
                f'<span>{html.escape(art["title"])}</span></a>'
                f"{outline_html}</li>"
            )
        groups_html.append(
            f'<div class="nav-group">'
            f'<p class="nav-caption">💭 {html.escape(cat_name)}</p>'
            f'<ol class="timeline">{"".join(items_html)}</ol>'
            f"</div>"
        )
    return "".join(groups_html)


def render_page_shell(
    *,
    title: str,
    permalink: str,
    mobile_pos: str,
    articles: list[dict[str, Any]],
    categories: list[str],
    current_slug: str | None,
    outline: list[dict[str, str]] | None,
    main_inner_html: str,
    search_index_json: str,
    css_v: str,
    js_v: str,
) -> str:
    desktop_nav = build_nav_html(articles, categories, current_slug, outline, is_mobile=False)
    mobile_nav = build_nav_html(articles, categories, current_slug, outline, is_mobile=True)
    theme_switcher_html = render_theme_switcher()
    desktop_search_html = render_search_box(is_mobile=False)
    mobile_search_html = render_search_box(is_mobile=True)
    rail_intro = (
        '<p class="rail-intro">记录日常折腾、工具设计与生活裂缝里的直觉瞬间。</p>'
        if current_slug is None
        else ""
    )

    return f"""---
layout: null
title: "{html.escape(title, quote=True)}"
permalink: {permalink}
---
<!doctype html>
<html lang="zh-CN" data-lp-theme="light" data-lp-theme-pref="auto"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#F4EFE7"><title>{html.escape(title)} | 思考与感悟 · Lee Pepe</title>
<link rel="stylesheet" href="/thoughts/reader.css?v={css_v}"><script>window.THOUGHTS_INDEX = {search_index_json};</script><script src="/thoughts/reader.js?v={js_v}" defer></script></head><body>
<a class="skip-link" href="#main">跳到正文</a>
<div class="sr-only" aria-live="polite" data-copy-live></div>
<header class="mobile-bar"><div class="mobile-bar-inner"><button class="open-series" type="button" aria-label="打开随笔目录" aria-haspopup="dialog" aria-controls="series-sheet" aria-expanded="false">
<span>思考与感悟</span><span class="mobile-position">{html.escape(mobile_pos)}</span><span class="chevron" aria-hidden="true"></span></button>
{theme_switcher_html}</div>
<div class="progress-track" aria-hidden="true"><span class="progress-fill" data-progress-fill></span></div></header>
<div class="reader-frame"><aside class="rail" aria-label="专栏导航"><div class="rail-top">
<div><a class="series-brand" href="/thoughts/">思考与感悟</a><p class="series-subtitle">Thoughts &amp; Reflections · 日常与工具随笔</p></div>
{theme_switcher_html}</div>
{desktop_search_html}
<div class="rail-scroll">{rail_intro}<nav aria-label="随笔文章">{desktop_nav}</nav></div>
<div class="rail-footer"><a class="rail-home" href="/">← Lee Pepe 首页</a><a class="rail-home" href="/learn/">直击痛点的求知笔记 (/learn/) →</a></div></aside>
<main id="main" tabindex="-1">{main_inner_html}</main></div>
<dialog class="series-sheet" id="series-sheet" aria-labelledby="sheet-title"><header class="sheet-header"><h2 id="sheet-title">思考与感悟</h2><button class="close-sheet" type="button" autofocus>关闭</button></header>
<div class="sheet-content"><p class="series-subtitle">记录日常折腾、工具设计与生活裂缝里的直觉瞬间</p>{mobile_search_html}<nav aria-label="手机随笔文章">{mobile_nav}</nav><div class="sheet-footer"><a class="sheet-home" href="/">← Lee Pepe 首页</a><a class="sheet-home" href="/learn/">求知笔记 (/learn/) →</a></div></div></dialog>
</body></html>
"""


def build_index_page(
    articles: list[dict[str, Any]],
    categories: list[str],
    search_index_json: str,
    css_v: str,
    js_v: str,
) -> None:
    tag_counts: dict[str, int] = {}
    for art in articles:
        for t in art["tags"]:
            tag_counts[t] = tag_counts.get(t, 0) + 1

    filter_chips_html = [
        f'<button type="button" class="tag-filter-chip is-active" data-filter-tag="all" aria-pressed="true">'
        f'全部 <span class="chip-count">({len(articles)})</span></button>'
    ]
    for tag_name, cnt in tag_counts.items():
        esc_t = html.escape(tag_name)
        filter_chips_html.append(
            f'<button type="button" class="tag-filter-chip" data-filter-tag="{esc_t}" aria-pressed="false">'
            f'{esc_t} <span class="chip-count">({cnt})</span></button>'
        )
    tag_bar_html = (
        f'<div class="tag-filter-wrap">'
        f'<div class="tag-filter-bar" data-tag-bar role="toolbar" aria-label="按标签筛选随笔">'
        f'{"".join(filter_chips_html)}'
        f"</div>"
        f'<p class="tag-filter-status" data-filter-status aria-live="polite" hidden></p>'
        f"</div>"
    )

    cat_sections: list[str] = []
    for cat_idx, cat_name in enumerate(categories, start=1):
        cat_id = f"cat-{cat_idx}"
        cat_articles = [a for a in articles if a["category"] == cat_name]
        cards_html: list[str] = []
        for art in cat_articles:
            tags_attr = html.escape("|".join(art["tags"]), quote=True)
            tags_html = "".join(
                f'<span class="tag-pill" role="button" tabindex="0" data-filter-tag="{html.escape(t, quote=True)}">{html.escape(t)}</span>'
                for t in art["tags"]
            )
            subtitle_html = (
                f'<p class="story-subtitle">{html.escape(art["subtitle"])}</p>'
                if art.get("subtitle")
                else ""
            )
            teaser_html = (
                f'<p class="story-teaser">{html.escape(art["insight"])}</p>'
                if art.get("insight")
                else ""
            )
            cards_html.append(
                f'<li class="story-item" data-story-tags="{tags_attr}" data-story-slug="{art["slug"]}">'
                f'<a class="story-card" href="/thoughts/{art["slug"]}/">'
                f'<span class="story-no">{art["num"]}</span>'
                f'<div><h3>{html.escape(art["title"])}</h3>'
                f"{subtitle_html}"
                f"{teaser_html}"
                f'<div class="story-meta-row"><span class="story-time">{html.escape(art["date"])}</span>'
                f'<span class="meta-dot" aria-hidden="true"></span>'
                f'<span class="story-time">{html.escape(art["reading_time"])}</span>'
                f"{tags_html}</div></div>"
                f'<span class="story-arrow" aria-hidden="true">→</span></a></li>'
            )
        cat_sections.append(
            f'<section class="category-section" data-category-section="{cat_id}" aria-labelledby="heading-{cat_id}">'
            f'<div class="category-heading"><h2 id="heading-{cat_id}">💭 {html.escape(cat_name)}</h2>'
            f'<span data-category-count>{len(cat_articles)} 篇</span></div>'
            f'<ol class="story-list">{"".join(cards_html)}</ol>'
            f"</section>"
        )

    main_html = f"""<section class="paper" aria-labelledby="series-title"><div class="reading-column"><header class="index-header">
<p class="eyebrow">THOUGHTS &amp; REFLECTIONS · 思考与感悟</p>
<h1 id="series-title">思考与感悟 · Thoughts &amp; Reflections</h1>
<p class="index-intro">记录日常折腾、工具设计与生活裂缝里的直觉瞬间——不追求大而全的系统宏图，只把那些真正让生活或手头工作变顺手的一点顿悟写下来。</p>
<p class="article-meta"><span>共 {len(articles)} 篇随笔</span><span class="meta-dot" aria-hidden="true"></span><span>数据源同步自 Knowledge Vault · thoughts/</span><span class="meta-dot" aria-hidden="true"></span><span>Warm Editorial 阅读器</span></p>
{tag_bar_html}</header>
<nav aria-label="分类随笔目录">{"".join(cat_sections)}</nav>
</div></section>"""

    page_html = render_page_shell(
        title="思考与感悟 · Thoughts & Reflections",
        permalink="/thoughts/",
        mobile_pos=f"目录 / {len(articles)}",
        articles=articles,
        categories=categories,
        current_slug=None,
        outline=None,
        main_inner_html=main_html,
        search_index_json=search_index_json,
        css_v=css_v,
        js_v=js_v,
    )
    (THOUGHTS_DIR / "index.html").write_text(page_html, encoding="utf-8")


def build_article_pages(
    articles: list[dict[str, Any]],
    categories: list[str],
    search_index_json: str,
    css_v: str,
    js_v: str,
) -> None:
    total = len(articles)
    for idx, art in enumerate(articles):
        prev_art = articles[idx - 1] if idx > 0 else None
        next_art = articles[idx + 1] if idx + 1 < total else None

        pager_links: list[str] = []
        if prev_art:
            pager_links.append(
                f'<a class="page-card" rel="prev" href="/thoughts/{prev_art["slug"]}/">'
                f"<small>← 上一篇 · {prev_art['num']}</small>"
                f'<span>{html.escape(prev_art["title"])}</span></a>'
            )
        if next_art:
            pager_links.append(
                f'<a class="page-card" rel="next" href="/thoughts/{next_art["slug"]}/">'
                f"<small>下一篇 · {next_art['num']} →</small>"
                f'<span>{html.escape(next_art["title"])}</span></a>'
            )

        tags_html = "".join(
            f'<a class="tag-pill" href="/thoughts/?tag={html.escape(t, quote=True)}">{html.escape(t)}</a>'
            for t in art["tags"]
        )
        subtitle_html = (
            f'<p class="article-subtitle">{html.escape(art["subtitle"])}</p>'
            if art.get("subtitle")
            else ""
        )
        insight_html = (
            f'<aside class="insight-card" aria-label="核心感悟">'
            f'<div class="insight-badge">💭 核心感悟 · Insight</div>'
            f'<p class="insight-body">{format_inline(art["insight"])}</p>'
            f"</aside>"
            if art.get("insight")
            else ""
        )

        main_html = f"""<article class="paper"><div class="reading-column"><header class="article-header">
<p class="eyebrow">第 {art["num"]} 篇 · {html.escape(art["category"])}</p>
<h1>{html.escape(art["title"])}</h1>
{subtitle_html}
<p class="article-meta"><time datetime="{html.escape(art["date"])}">{html.escape(art["date"])}</time><span class="meta-dot" aria-hidden="true"></span><span>{html.escape(art["reading_time"])}</span><span class="meta-dot" aria-hidden="true"></span>{tags_html}</p></header>
{insight_html}
<div class="prose" data-reading-body>
{art["body_html"]}
</div>
<footer><div class="article-end">本篇完 · 思考与感悟</div>
<nav class="pager" aria-label="相邻随笔">{"".join(pager_links)}</nav>
<a class="back-index" href="/thoughts/">← 回到思考与感悟（/thoughts/）</a></footer></div></article>"""

        page_html = render_page_shell(
            title=art["title"],
            permalink=f'/thoughts/{art["slug"]}/',
            mobile_pos=f"{idx + 1} / {total}",
            articles=articles,
            categories=categories,
            current_slug=art["slug"],
            outline=art["outline"],
            main_inner_html=main_html,
            search_index_json=search_index_json,
            css_v=css_v,
            js_v=js_v,
        )
        out_dir = THOUGHTS_DIR / art["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_html, encoding="utf-8")


def main() -> None:
    articles = load_all_thoughts()
    categories: list[str] = []
    for art in articles:
        if art["category"] not in categories:
            categories.append(art["category"])

    search_index = [
        {
            "num": art["num"],
            "slug": art["slug"],
            "url": f'/thoughts/{art["slug"]}/',
            "category": art["category"],
            "title": art["title"],
            "subtitle": art["subtitle"],
            "insight": art["insight"],
            "tags": art["tags"],
            "sections": art["outline"],
        }
        for art in articles
    ]
    search_index_json = json.dumps(search_index, ensure_ascii=False, separators=(",", ":"))
    css_v = asset_hash(THOUGHTS_DIR / "reader.css")
    js_v = asset_hash(THOUGHTS_DIR / "reader.js")
    build_index_page(articles, categories, search_index_json, css_v, js_v)
    build_article_pages(articles, categories, search_index_json, css_v, js_v)
    print(f"Built /thoughts/ index + {len(articles)} essay(s) (css={css_v}, js={js_v})")


if __name__ == "__main__":
    main()
