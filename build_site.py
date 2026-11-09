#!/usr/bin/env python3
"""
Unified static site builder for LeePepe/leepepe.github.io.
1. Invokes learn/_build.py and thoughts/_build.py so all /learn/ and /thoughts/ pages are fresh.
2. Collects unified metadata across all 7 /learn/ articles and all /thoughts/ essays.
3. Generates:
   - /index.html (Magazine Portal Home: Hero + Dual-Series Bento + Filterable Stream & Aside)
   - /archive/index.html (Shared-Geometry Timeline Archive, DC-005)
   - /tags/index.html (Interactive Tag Atlas)
   - /about/index.html (Personal Editorial Profile)
   - /404.html (Warm Editorial 404 Page)
   - /feed.xml (Valid Atom XML Feed)
"""

from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent
ASSETS_DIR = REPO_ROOT / "assets"
SITE_URL = "https://leepepe.github.io"

NAV_ITEMS = [
    ("home", "首页", "/"),
    ("learn", "求知笔记", "/learn/"),
    ("thoughts", "思考与感悟", "/thoughts/"),
    ("archive", "归档", "/archive/"),
    ("tags", "标签", "/tags/"),
    ("about", "关于", "/about/"),
]


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module {name} from {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def asset_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def slugify_tag(tag: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "-", tag.strip()).strip("-").lower()
    return f"tag-{clean or 'item'}"


def render_theme_switcher() -> str:
    return (
        '<div class="theme-segmented" role="group" aria-label="主题外观切换" data-theme-toggle>'
        '<button type="button" class="theme-seg-btn" data-theme-val="light" aria-pressed="false" title="浅色模式">☀️ 浅</button>'
        '<button type="button" class="theme-seg-btn" data-theme-val="dark" aria-pressed="false" title="深色模式">🌙 深</button>'
        '<button type="button" class="theme-seg-btn" data-theme-val="auto" aria-pressed="true" title="跟随系统自动切换">◐ 自</button>'
        "</div>"
    )


def render_site_shell(
    *,
    title: str,
    description: str,
    permalink: str,
    active_nav: str,
    main_html: str,
    search_index_json: str,
    css_v: str,
    js_v: str,
) -> str:
    nav_links: list[str] = []
    mobile_links: list[str] = []
    for key, label, href in NAV_ITEMS:
        is_curr = key == active_nav
        curr_attr = ' aria-current="page"' if is_curr else ""
        cls = "site-nav-link is-active" if is_curr else "site-nav-link"
        nav_links.append(f'<a class="{cls}" href="{href}"{curr_attr}>{html.escape(label)}</a>')
        mobile_links.append(
            f'<li><a class="mobile-nav-link" href="{href}"{curr_attr}>'
            f'<span>{html.escape(label)}</span><span aria-hidden="true">→</span></a></li>'
        )

    theme_html = render_theme_switcher()
    full_title = title if "Lee Pepe" in title else f"{title} | Lee Pepe"

    return f"""---
layout: null
title: "{html.escape(title, quote=True)}"
permalink: {permalink}
---
<!doctype html>
<html lang="zh-CN" data-lp-theme="light" data-lp-theme-pref="auto">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#EEECE5">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <title>{html.escape(full_title)}</title>
  <link rel="alternate" type="application/atom+xml" title="Lee Pepe · 全站订阅 (Atom/RSS)" href="/feed.xml">
  <link rel="stylesheet" href="/assets/site.css?v={css_v}">
  <script>window.SITE_SEARCH_INDEX = {search_index_json};</script>
  <script src="/assets/site.js?v={js_v}" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">跳到正文</a>
  <div class="sr-only" aria-live="polite" data-copy-live></div>

  <header class="site-header">
    <div class="site-header-inner">
      <a class="site-brand" href="/" aria-label="Lee Pepe 首页">
        <span class="site-brand-monogram" aria-hidden="true">L</span>
        <span class="site-brand-text">
          <span class="site-brand-name">Lee Pepe</span>
          <span class="site-brand-tag">写代码，也写生活</span>
        </span>
      </a>

      <nav class="site-nav" aria-label="全站主导航">
        {"".join(nav_links)}
      </nav>

      <div class="site-actions">
        <button type="button" class="search-trigger-btn" data-open-search aria-label="搜索全站文章与痛点问答 (快捷键 /)">
          <span aria-hidden="true">🔍</span>
          <span class="search-trigger-label">搜索全站…</span>
          <kbd class="search-kbd" aria-hidden="true">/</kbd>
        </button>
        {theme_html}
        <button type="button" class="mobile-menu-btn" data-open-nav aria-label="打开全站导航菜单" aria-haspopup="dialog" aria-controls="site-nav-dialog" aria-expanded="false">
          <span>菜单</span>
        </button>
      </div>
    </div>
  </header>

  <main id="main" class="site-main" tabindex="-1">
    {main_html}
  </main>

  <footer class="site-footer">
    <div class="site-footer-inner">
      <div>
        <strong>Lee Pepe</strong> · 写代码，也写生活 · Warm Editorial × Strata 麦芽黄阅读体系
      </div>
      <nav class="site-footer-links" aria-label="页脚导航">
        <a href="/">首页</a>
        <a href="/learn/">求知笔记</a>
        <a href="/thoughts/">思考与感悟</a>
        <a href="/archive/">归档</a>
        <a href="/tags/">标签</a>
        <a href="/about/">关于</a>
        <a href="/feed.xml">RSS 订阅</a>
        <a href="https://github.com/LeePepe" target="_blank" rel="noopener">GitHub</a>
      </nav>
    </div>
  </footer>

  <dialog class="site-dialog" id="site-search-dialog" aria-labelledby="search-dialog-title">
    <div class="dialog-head">
      <label id="search-dialog-title" class="sr-only" for="site-search-input">搜索全站文章、痛点 Q&amp;A 与随笔感悟</label>
      <input id="site-search-input" type="search" class="dialog-search-input" data-site-search-input placeholder="输入关键词搜索全站笔记、痛点 Q&amp;A、API 或感悟随笔…" autocomplete="off">
      <button type="button" class="dialog-close-btn" data-close-search>关闭</button>
    </div>
    <div class="dialog-body" data-site-search-results role="listbox" aria-label="全站搜索结果"></div>
  </dialog>

  <dialog class="site-dialog" id="site-nav-dialog" aria-labelledby="nav-dialog-title">
    <div class="dialog-head" style="justify-content:space-between;">
      <strong id="nav-dialog-title" style="font-size:15px;">全站导航 · Lee Pepe</strong>
      <button type="button" class="dialog-close-btn" data-close-nav>关闭</button>
    </div>
    <div class="dialog-body">
      <ul class="mobile-nav-list">
        {"".join(mobile_links)}
      </ul>
    </div>
  </dialog>
</body>
</html>
"""


def collect_site_data(learn_mod: Any, thoughts_mod: Any) -> dict[str, Any]:
    learn_items: list[dict[str, Any]] = []
    for art in learn_mod.ARTICLES:
        outline, body_html, questions = learn_mod.parse_markdown_article(art)
        cat_obj = next(c for c in learn_mod.CATEGORIES if c["id"] == art["category_id"])
        learn_items.append(
            {
                "series": "learn",
                "series_label": "直击痛点的求知笔记",
                "series_badge": f"求知 · {art['num']}",
                "num": art["num"],
                "slug": art["slug"],
                "url": f"/learn/{art['slug']}/",
                "title": art["title"],
                "short_title": art["short_title"],
                "date": art["updated"],
                "reading_time": art["reading_time"],
                "category_title": cat_obj["short_nav"],
                "teaser": art["teaser"],
                "tags": list(art["tags"]),
                "questions": [{"id": q["id"], "badge": q["badge"], "q": q["q"]} for q in questions],
                "sections": [{"id": s["id"], "title": s["title"]} for s in outline],
                "body_html": body_html,
            }
        )

    thoughts_raw = thoughts_mod.load_all_thoughts()
    thought_items: list[dict[str, Any]] = []
    for art in thoughts_raw:
        thought_items.append(
            {
                "series": "thoughts",
                "series_label": "思考与感悟",
                "series_badge": f"感悟 · {art['num']}",
                "num": art["num"],
                "slug": art["slug"],
                "url": f"/thoughts/{art['slug']}/",
                "title": art["title"],
                "short_title": art["title"],
                "subtitle": art.get("subtitle") or "",
                "date": art["date"],
                "reading_time": art["reading_time"],
                "category_title": f"💭 {art['category']}",
                "teaser": art.get("insight") or art.get("subtitle") or "",
                "tags": list(art["tags"]),
                "questions": [],
                "sections": art["outline"],
                "body_html": art["body_html"],
            }
        )

    # Chronological stream: featured thought reflection first on same date, then learn articles in order
    all_writings = thought_items + learn_items
    all_writings.sort(key=lambda x: (x["date"], 1 if x["series"] == "thoughts" else 0), reverse=True)

    # Tag aggregation preserving first appearance order
    tag_map: dict[str, list[dict[str, Any]]] = {}
    for item in learn_items + thought_items:
        for t in item["tags"]:
            tag_map.setdefault(t, []).append(item)

    return {
        "learn": learn_items,
        "thoughts": thought_items,
        "all": all_writings,
        "tags": tag_map,
    }


def build_home_page(data: dict[str, Any], search_json: str, css_v: str, js_v: str) -> None:
    learn_items = data["learn"]
    thought_items = data["thoughts"]
    all_items = data["all"]
    tag_map = data["tags"]
    total_qa = sum(len(x["questions"]) for x in learn_items)
    featured_thought = thought_items[0] if thought_items else None

    learn_samples_html = "".join(
        f'<li><a class="bento-sample-link" href="{html.escape(a["url"])}">'
        f'<span><span class="bento-sample-num">{a["num"]}</span>{html.escape(a["short_title"])}</span>'
        f'<span class="bento-sample-meta">{len(a["questions"])} 问 · {html.escape(a["reading_time"])}</span>'
        f"</a></li>"
        for a in learn_items[:3]
    )

    thought_quote_html = ""
    thought_samples_html = ""
    if featured_thought:
        thought_quote_html = (
            f'<blockquote class="bento-quote">'
            f'<span class="bento-quote-title">💡 最新随笔 · {html.escape(featured_thought["title"])}</span>'
            f'{html.escape(featured_thought["teaser"])}'
            f"</blockquote>"
        )
        thought_samples_html = (
            f'<ul class="bento-sample-list">'
            f'<li><a class="bento-sample-link" href="{html.escape(featured_thought["url"])}">'
            f'<span><span class="bento-sample-num">{featured_thought["num"]}</span>{html.escape(featured_thought["title"])}</span>'
            f'<span class="bento-sample-meta">{html.escape(featured_thought["date"])} · {html.escape(featured_thought["reading_time"])}</span>'
            f"</a></li></ul>"
        )

    stream_cards_html: list[str] = []
    for item in all_items:
        is_thought = item["series"] == "thoughts"
        pill_cls = "series-pill series-pill--thoughts" if is_thought else "series-pill"
        pill_txt = f"💭 思考与感悟 · {item['num']}" if is_thought else f"📚 求知笔记 · {item['num']}"
        q_info = f'<span class="meta-dot" aria-hidden="true"></span><span>{len(item["questions"])} 个痛点 Q&amp;A</span>' if item["questions"] else ""
        tags_spans = "".join(
            f'<span class="tag-pill">{html.escape(t)}</span>'
            for t in item["tags"][:4]
        )
        stream_cards_html.append(
            f'<li data-item-series="{item["series"]}">'
            f'<a class="stream-card" href="{html.escape(item["url"])}">'
            f'<div class="stream-card-top">'
            f'<span class="{pill_cls}">{html.escape(pill_txt)}</span>'
            f'<time datetime="{html.escape(item["date"])}">{html.escape(item["date"])}</time>'
            f'<span class="meta-dot" aria-hidden="true"></span>'
            f'<span>{html.escape(item["reading_time"])}</span>'
            f"{q_info}"
            f"</div>"
            f'<h3 class="stream-card-title">{html.escape(item["title"])}</h3>'
            f'<p class="stream-card-teaser">{html.escape(item["teaser"])}</p>'
            f'<div class="stream-card-tags">{tags_spans}</div>'
            f"</a></li>"
        )

    top_tags_html = "".join(
        f'<a class="tag-pill" href="/tags/?tag={html.escape(t, quote=True)}">{html.escape(t)} <span>({len(arts)})</span></a>'
        for t, arts in list(tag_map.items())[:16]
    )

    main_html = f"""
    <section class="hero-editorial" aria-labelledby="home-hero-title">
      <div>
        <p class="eyebrow">PERSONAL EDITORIAL PORTAL · LEE PEPE</p>
        <h1 id="home-hero-title" class="hero-title">写代码，也写生活。</h1>
        <p class="hero-lead">
          你好，我是 <strong>Lee Pepe</strong>。这里没有教科书式的概念堆砌——在
          <strong>「直击痛点的求知笔记」</strong>里，我用凸透镜、水管、图钉与冰箱把抽象的工程原理拆成肉眼可见的生活教具；在
          <strong>「思考与感悟」</strong>里，我把日常折腾智能家居、做减法工具与生活习惯里的真实顿悟记下来。
        </p>
        <div class="hero-actions">
          <a class="btn-primary" href="/learn/">📚 进入求知笔记 ({len(learn_items)}) →</a>
          <a class="btn-secondary" href="/thoughts/">💭 阅读思考与感悟 ({len(thought_items)})</a>
          <a class="btn-secondary" href="/archive/">🗂 全站时间轴归档</a>
        </div>
      </div>
      <aside class="hero-stats-card" aria-label="全站内容速览">
        <div class="hero-stat-row">
          <span class="hero-stat-label">📚 求知笔记专栏</span>
          <span class="hero-stat-val">{len(learn_items)} 篇深度长文</span>
        </div>
        <div class="hero-stat-row">
          <span class="hero-stat-label">🎯 痛点直答 Q&amp;A</span>
          <span class="hero-stat-val">{total_qa} 个真问题破案</span>
        </div>
        <div class="hero-stat-row">
          <span class="hero-stat-label">💭 思考与感悟随笔</span>
          <span class="hero-stat-val">{len(thought_items)} 篇生活洞察</span>
        </div>
        <div class="hero-stat-row">
          <span class="hero-stat-label">🏷 知识与工具标签</span>
          <span class="hero-stat-val">{len(tag_map)} 个主题索引</span>
        </div>
      </aside>
    </section>

    <section class="series-bento" aria-label="双专栏精选導览">
      <article class="bento-card bento-card--learn">
        <div>
          <div class="bento-head">
            <span class="bento-badge">📚 专栏一 · Knowledge Vault</span>
            <span class="bento-count">共 {len(learn_items)} 篇 · {total_qa} 个痛点 Q&amp;A</span>
          </div>
          <h2 class="bento-title"><a href="/learn/">直击痛点的求知笔记</a></h2>
          <p class="bento-desc">
            拒绝平铺直叙的 API 罗列。每一篇都严格遵循「一句话反常识本质 → 生活教具痛点直答 → 明天就能照着改的行动清单」三段式闭环。
          </p>
          <div class="bento-pillars">
            <div class="bento-pillar"><strong>⚡ 一句话本质</strong>3 秒建立反直觉全局坐标系</div>
            <div class="bento-pillar"><strong>🎯 痛点直答</strong>用透镜/水管/图钉替代公式</div>
            <div class="bento-pillar"><strong>✅ 行动清单</strong>≤3 条零门槛工程实操处方</div>
          </div>
          <ul class="bento-sample-list">
            {learn_samples_html}
          </ul>
        </div>
        <div class="bento-foot">
          <span class="bento-count">覆盖 WWDC 25/26 八节课 + WiFi 物理可视化</span>
          <a class="bento-cta" href="/learn/">浏览全部 {len(learn_items)} 篇笔记 →</a>
        </div>
      </article>

      <article class="bento-card bento-card--thoughts">
        <div>
          <div class="bento-head">
            <span class="bento-badge">💭 专栏二 · Thoughts &amp; Reflections</span>
            <span class="bento-count">共 {len(thought_items)} 篇随笔 · 持续记录</span>
          </div>
          <h2 class="bento-title"><a href="/thoughts/">思考与感悟</a></h2>
          <p class="bento-desc">
            记录日常折腾、工具设计与生活裂缝里的直觉瞬间——不追求大而全的系统宏图，只写那些真正让手头工作和生活变顺手的一点顿悟。
          </p>
          {thought_quote_html}
          {thought_samples_html}
        </div>
        <div class="bento-foot">
          <span class="bento-count">少一个遥控器，多一次顺手的肌肉记忆</span>
          <a class="bento-cta" href="/thoughts/">进入思考与感悟专栏 →</a>
        </div>
      </article>
    </section>

    <div class="home-layout">
      <section class="stream-panel" aria-labelledby="stream-heading">
        <div class="stream-header">
          <h2 id="stream-heading" class="stream-title">最新文章与随笔</h2>
          <div class="series-tabs" role="toolbar" aria-label="按专栏筛选文章" data-series-filter-bar>
            <button type="button" class="series-tab is-active" data-series-filter="all" aria-pressed="true">全部 ({len(all_items)})</button>
            <button type="button" class="series-tab" data-series-filter="learn" aria-pressed="false">📚 求知笔记 ({len(learn_items)})</button>
            <button type="button" class="series-tab" data-series-filter="thoughts" aria-pressed="false">💭 思考与感悟 ({len(thought_items)})</button>
          </div>
        </div>
        <ol class="stream-list">
          {"".join(stream_cards_html)}
        </ol>
      </section>

      <aside class="home-aside" aria-label="作者简介与快捷索引">
        <section class="aside-card" aria-labelledby="aside-author-title">
          <div class="aside-profile-head">
            <span class="aside-avatar" aria-hidden="true">L</span>
            <div>
              <h2 id="aside-author-title" class="aside-card-title" style="margin:0;">Lee Pepe</h2>
              <span style="font-size:12px;color:var(--muted);">iOS / 前端 / 智能家居 / 认知拆解</span>
            </div>
          </div>
          <p class="aside-bio">
            生活中从 210 斤减到 150 斤，喜欢健身、跑步与篮球；工作里深耕 Apple 生态（SwiftUI / AppKit / UIKit）、前端与全屋智能自动化，着迷于「把复杂系统讲得人人秒懂」。
          </p>
          <div class="aside-links">
            <a class="aside-link-chip" href="/about/">👤 关于我</a>
            <a class="aside-link-chip" href="https://github.com/LeePepe" target="_blank" rel="noopener">🐙 GitHub</a>
            <a class="aside-link-chip" href="/feed.xml">📡 RSS 订阅</a>
          </div>
        </section>

        <section class="aside-card" aria-labelledby="aside-tags-title">
          <div class="aside-card-title">
            <span id="aside-tags-title">🏷 热门主题标签</span>
            <a href="/tags/" style="font-size:12px;font-weight:500;">全部 {len(tag_map)} 个 →</a>
          </div>
          <div class="aside-tag-cloud">
            {top_tags_html}
          </div>
        </section>

        <section class="aside-card" aria-labelledby="aside-search-title">
          <h2 id="aside-search-title" class="aside-card-title">⌨️ 快捷键与阅读提示</h2>
          <p class="aside-bio" style="margin-bottom:10px;">
            在全站任意页面按 <kbd class="search-kbd">/</kbd> 或 <kbd class="search-kbd">⌘K</kbd> 即可唤起全局搜索，直达任意痛点 Q&amp;A；右上角支持 <strong>浅色 / 深色 / 跟随系统</strong> 三态切换并全站自动同步。
          </p>
          <a class="aside-link-chip" href="/archive/">🗂 查看按年份对表归档 →</a>
        </section>
      </aside>
    </div>
    """

    page_html = render_site_shell(
        title="Lee Pepe · 写代码，也写生活",
        description="Lee Pepe 的个人博客：收录「直击痛点的求知笔记」与「思考与感悟」，采用 Warm Editorial × Strata 麦芽黄阅读体系。",
        permalink="/",
        active_nav="home",
        main_html=main_html,
        search_index_json=search_json,
        css_v=css_v,
        js_v=js_v,
    )
    (REPO_ROOT / "index.html").write_text(page_html, encoding="utf-8")


def build_archive_page(data: dict[str, Any], search_json: str, css_v: str, js_v: str) -> None:
    all_items = data["all"]
    learn_count = len(data["learn"])
    thought_count = len(data["thoughts"])

    by_year: dict[str, list[dict[str, Any]]] = {}
    for item in all_items:
        yr = item["date"][:4]
        by_year.setdefault(yr, []).append(item)

    year_blocks_html: list[str] = []
    for yr in sorted(by_year.keys(), reverse=True):
        rows_html: list[str] = []
        for item in by_year[yr]:
            is_thought = item["series"] == "thoughts"
            pill_cls = "series-pill series-pill--thoughts" if is_thought else "series-pill"
            pill_txt = "💭 思考与感悟" if is_thought else "📚 求知笔记"
            rows_html.append(
                f'<tr data-item-series="{item["series"]}">'
                f'<td class="cell-date"><time datetime="{html.escape(item["date"])}">{html.escape(item["date"])}</time></td>'
                f'<td><span class="{pill_cls}">{html.escape(pill_txt)}</span></td>'
                f'<td>'
                f'<a class="archive-row-link" href="{html.escape(item["url"])}">{html.escape(item["title"])}</a>'
                f'<span class="archive-row-sub">{html.escape(item["teaser"])}</span>'
                f"</td>"
                f'<td class="cell-time">{html.escape(item["reading_time"])}</td>'
                f"</tr>"
            )
        year_blocks_html.append(
            f'<section class="archive-year-block" data-archive-year="{yr}" aria-labelledby="year-{yr}">'
            f'<div class="archive-year-head">'
            f'<h2 id="year-{yr}" class="archive-year-title">{yr} 年</h2>'
            f'<span class="archive-year-count" data-year-count>共 {len(by_year[yr])} 篇</span>'
            f"</div>"
            f'<div class="archive-table-wrap">'
            f'<table class="archive-table">'
            f"<colgroup>"
            f'<col class="col-date"><col class="col-series"><col class="col-title"><col class="col-time">'
            f"</colgroup>"
            f"<thead><tr>"
            f'<th scope="col">发布日期</th>'
            f'<th scope="col">所属专栏</th>'
            f'<th scope="col">文章标题与核心痛点摘要</th>'
            f'<th scope="col" class="cell-time">阅读时长</th>'
            f"</tr></thead>"
            f'<tbody>{"".join(rows_html)}</tbody>'
            f"</table></div></section>"
        )

    main_html = f"""
    <article class="page-paper" aria-labelledby="archive-title">
      <header class="page-header">
        <p class="eyebrow">CHRONOLOGICAL ARCHIVE · 全站时间轴归档</p>
        <h1 id="archive-title" class="page-title">全站文章归档</h1>
        <p class="page-intro">
          按年份与专栏对表汇总全站共 <strong>{len(all_items)}</strong> 篇作品（含 {learn_count} 篇「直击痛点的求知笔记」与 {thought_count} 篇「思考与感悟」）。支持按专栏一键筛选。
        </p>
        <div class="series-tabs" role="toolbar" aria-label="按专栏筛选归档" data-series-filter-bar>
          <button type="button" class="series-tab is-active" data-series-filter="all" aria-pressed="true">全部 ({len(all_items)})</button>
          <button type="button" class="series-tab" data-series-filter="learn" aria-pressed="false">📚 求知笔记 ({learn_count})</button>
          <button type="button" class="series-tab" data-series-filter="thoughts" aria-pressed="false">💭 思考与感悟 ({thought_count})</button>
        </div>
      </header>
      {"".join(year_blocks_html)}
    </article>
    """

    page_html = render_site_shell(
        title="全站归档 · Archive",
        description="Lee Pepe 个人博客全站时间轴归档：汇总所有求知笔记与思考感悟随笔。",
        permalink="/archive/",
        active_nav="archive",
        main_html=main_html,
        search_index_json=search_json,
        css_v=css_v,
        js_v=js_v,
    )
    (REPO_ROOT / "archive" / "index.html").write_text(page_html, encoding="utf-8")


def build_tags_page(data: dict[str, Any], search_json: str, css_v: str, js_v: str) -> None:
    tag_map = data["tags"]
    all_items = data["all"]

    chips_html = [
        f'<button type="button" class="tag-filter-chip is-active" data-atlas-tag="all" aria-pressed="true">'
        f'全部标签 <span>({len(tag_map)})</span></button>'
    ]
    groups_html: list[str] = []

    for tag_name, items in tag_map.items():
        tag_id = slugify_tag(tag_name)
        esc_tag = html.escape(tag_name)
        chips_html.append(
            f'<button type="button" class="tag-filter-chip" data-atlas-tag="{esc_tag}" aria-pressed="false">'
            f'{esc_tag} <span>({len(items)})</span></button>'
        )
        cards_html: list[str] = []
        for item in items:
            is_thought = item["series"] == "thoughts"
            pill_cls = "series-pill series-pill--thoughts" if is_thought else "series-pill"
            pill_txt = f"💭 思考与感悟 · {item['num']}" if is_thought else f"📚 求知笔记 · {item['num']}"
            cards_html.append(
                f'<li><a class="bento-sample-link" href="{html.escape(item["url"])}">'
                f'<span><span class="{pill_cls}" style="margin-right:8px;">{html.escape(pill_txt)}</span>'
                f'<strong>{html.escape(item["title"])}</strong></span>'
                f'<span class="bento-sample-meta">{html.escape(item["date"])} · {html.escape(item["reading_time"])}</span>'
                f"</a></li>"
            )
        groups_html.append(
            f'<section class="tag-group-card" id="{tag_id}" data-tag-group="{esc_tag}" aria-labelledby="heading-{tag_id}">'
            f'<div class="tag-group-head">'
            f'<h2 id="heading-{tag_id}" class="tag-group-title"># {esc_tag}</h2>'
            f'<span class="tag-group-count">{len(items)} 篇文章</span>'
            f"</div>"
            f'<ul class="bento-sample-list">{"".join(cards_html)}</ul>'
            f"</section>"
        )

    main_html = f"""
    <article class="page-paper" aria-labelledby="tags-title">
      <header class="page-header">
        <p class="eyebrow">TOPIC &amp; CONCEPT ATLAS · 全站标签索引</p>
        <h1 id="tags-title" class="page-title">主题与技术标签索引</h1>
        <p class="page-intro">
          共收录 <strong>{len(tag_map)}</strong> 个技术概念、视觉技法与生活思考标签，横跨全站 {len(all_items)} 篇笔记与随笔。点击任意标签可即时筛选对应文章。
        </p>
        <div class="tag-filter-bar" role="toolbar" aria-label="按标签筛选" data-tag-atlas-bar>
          {"".join(chips_html)}
        </div>
        <p data-tag-atlas-status hidden style="margin:12px 0 0;font-size:13px;color:var(--accent);font-weight:600;"></p>
      </header>
      <div class="tag-group-grid">
        {"".join(groups_html)}
      </div>
    </article>
    """

    page_html = render_site_shell(
        title="标签索引 · Tags",
        description="Lee Pepe 个人博客全站主题与技术标签索引。",
        permalink="/tags/",
        active_nav="tags",
        main_html=main_html,
        search_index_json=search_json,
        css_v=css_v,
        js_v=js_v,
    )
    (REPO_ROOT / "tags" / "index.html").write_text(page_html, encoding="utf-8")


def build_about_page(data: dict[str, Any], search_json: str, css_v: str, js_v: str) -> None:
    learn_count = len(data["learn"])
    thought_count = len(data["thoughts"])

    main_html = f"""
    <article class="page-paper" aria-labelledby="about-title">
      <header class="page-header">
        <p class="eyebrow">ABOUT THE AUTHOR · 关于我</p>
        <h1 id="about-title" class="page-title">你好，我是 Lee Pepe。</h1>
        <p class="page-intro">
          如果非要用一句话描述自己：<strong>一个喜欢把复杂工程和生活摩擦都「做减法」的人</strong>。写代码，也写生活；在屏幕上打磨顺手的交互，在现实里保持身体与好奇心的轻盈。
        </p>
      </header>

      <section class="about-bento-grid" aria-label="个人三面速写">
        <div class="about-pillar-card">
          <span class="about-pillar-icon" aria-hidden="true">🛠</span>
          <h2>工程与设计：把复杂留给幕后</h2>
          <p>
            毕业后一路折腾过 iOS（SwiftUI / AppKit / UIKit）、自然语言处理、现代前端与全屋智能家居（绿联 NAS + Home Assistant + Node-RED）。比起堆砌炫技的参数，我更在意「按下去那一秒是不是零心智负担」。
          </p>
        </div>

        <div class="about-pillar-card">
          <span class="about-pillar-icon" aria-hidden="true">🏃</span>
          <h2>身体与习惯：从 210 斤到 150 斤</h2>
          <p>
            生活中曾一路从 210 斤减到现在的 150 斤。喜欢健身、跑步、打篮球，也一直想去尝试跑酷。这段经历让我深刻体会到：真正可持续的改变，靠的从来不是某天突击式的意志力，而是把环境改造成「顺手就能做到」。
          </p>
        </div>

        <div class="about-pillar-card">
          <span class="about-pillar-icon" aria-hidden="true">🧠</span>
          <h2>好奇心与输入：直击痛点</h2>
          <p>
            对认知心理学、物理可视化与顶级技术叙事（如 WWDC 动效课、科普视频脚本）充满兴趣。学懂一个新东西的标志，是能不能用生活里的凸透镜、水管、图钉或冰箱把它给外行讲明白。
          </p>
        </div>
      </section>

      <section aria-labelledby="site-guide-heading">
        <h2 id="site-guide-heading" style="font-family:var(--font-serif);font-size:24px;margin-bottom:14px;">这座博客是怎么组织的？</h2>
        <div class="about-guide-grid">
          <div class="about-guide-card">
            <h3>📚 直击痛点的求知笔记（/learn/ · 共 {learn_count} 篇）</h3>
            <p style="font-size:14.5px;color:var(--muted);line-height:1.8;margin-bottom:14px;">
              每一篇都针对一个硬核技术或科学主题，砍掉八股文铺垫，严格按「<strong>一句话反常识本质 → 生活教具痛点直答 Q&amp;A → 明天就能照着改的行动清单</strong>」三步呈现，并提供自测折叠模式。
            </p>
            <a class="btn-secondary" href="/learn/">前往求知笔记专栏 →</a>
          </div>

          <div class="about-guide-card">
            <h3>💭 思考与感悟（/thoughts/ · 共 {thought_count} 篇）</h3>
            <p style="font-size:14.5px;color:var(--muted);line-height:1.8;margin-bottom:14px;">
              记录日常折腾工具、改造家居或生活习惯时的微小顿悟——比如为什么「家里少了一个空调遥控器，我给书房按键加了长按开空调，而且每次只需要开就行」。
            </p>
            <a class="btn-secondary" href="/thoughts/">前往思考与感悟专栏 →</a>
          </div>
        </div>
      </section>

      <section style="padding-top:22px;border-top:1px solid var(--line);" aria-labelledby="contact-heading">
        <h2 id="contact-heading" style="font-family:var(--font-serif);font-size:20px;margin-bottom:12px;">保持联系与订阅</h2>
        <div class="hero-actions">
          <a class="btn-secondary" href="https://github.com/LeePepe" target="_blank" rel="noopener">🐙 GitHub (@LeePepe)</a>
          <a class="btn-secondary" href="mailto:1105208297@qq.com">✉️ 邮箱 (1105208297@qq.com)</a>
          <a class="btn-secondary" href="/feed.xml">📡 Atom / RSS 全站订阅</a>
        </div>
      </section>
    </article>
    """

    page_html = render_site_shell(
        title="关于我 · About Lee Pepe",
        description="关于 Lee Pepe：从 210 斤到 150 斤，写代码也写生活，专注 iOS/SwiftUI、前端、智能家居与直击痛点的知识拆解。",
        permalink="/about/",
        active_nav="about",
        main_html=main_html,
        search_index_json=search_json,
        css_v=css_v,
        js_v=js_v,
    )
    (REPO_ROOT / "about" / "index.html").write_text(page_html, encoding="utf-8")


def build_404_page(data: dict[str, Any], search_json: str, css_v: str, js_v: str) -> None:
    learn_count = len(data["learn"])
    thought_count = len(data["thoughts"])

    main_html = f"""
    <article class="page-paper error-card" aria-labelledby="error-title">
      <p class="eyebrow">HTTP 404 · PAGE NOT FOUND</p>
      <p class="error-code">404</p>
      <h1 id="error-title" class="page-title" style="font-size:28px;">这页笔记似乎移位了，或者旧链接已归档清理。</h1>
      <p class="page-intro">
        全站已完成 Warm Editorial 改版升级。你可以在下方直接搜索关键词，或从四个核心入口继续阅读：
      </p>

      <div data-inline-search-wrap style="margin:20px 0 26px;position:relative;">
        <label for="error-search-input" class="sr-only">搜索全站文章与痛点问答</label>
        <input id="error-search-input" type="search" class="dialog-search-input" style="width:100%;" data-inline-search-input placeholder="输入关键词（如 Liquid Glass、Shader、WiFi、书房空调）直接查找…">
        <div data-inline-search-results hidden style="margin-top:8px;padding:8px;border-radius:16px;border:1px solid var(--accent);background:var(--inset-bg);"></div>
      </div>

      <div class="recovery-grid">
        <a class="recovery-card" href="/">
          <strong>🏠 返回首页（/）</strong>
          <span>双专栏精选导览与全站最新文章流</span>
        </a>
        <a class="recovery-card" href="/learn/">
          <strong>📚 直击痛点的求知笔记（/learn/）</strong>
          <span>{learn_count} 篇深度原理破案卡与可执行清单</span>
        </a>
        <a class="recovery-card" href="/thoughts/">
          <strong>💭 思考与感悟（/thoughts/）</strong>
          <span>{thought_count} 篇日常工具、智能家居与生活直觉随笔</span>
        </a>
        <a class="recovery-card" href="/archive/">
          <strong>🗂 全站时间轴归档（/archive/）</strong>
          <span>按年份与专栏对表检索全部文章</span>
        </a>
      </div>
    </article>
    """

    page_html = render_site_shell(
        title="404 页面未找到 | Lee Pepe",
        description="页面未找到 — 搜索全站求知笔记与思考感悟随笔。",
        permalink="/404.html",
        active_nav="",
        main_html=main_html,
        search_index_json=search_json,
        css_v=css_v,
        js_v=js_v,
    )
    (REPO_ROOT / "404.html").write_text(page_html, encoding="utf-8")


def build_feed_xml(data: dict[str, Any]) -> None:
    all_items = data["all"]
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
  <subtitle>直击痛点的求知笔记（/learn/）与思考与感悟（/thoughts/）</subtitle>
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
    learn_mod = load_module("learn_build", REPO_ROOT / "learn" / "_build.py")
    thoughts_mod = load_module("thoughts_build", REPO_ROOT / "thoughts" / "_build.py")

    # 1. Rebuild /learn/* and /thoughts/*
    learn_mod.main()
    thoughts_mod.main()

    # 2. Collect unified site index
    data = collect_site_data(learn_mod, thoughts_mod)
    search_index = [
        {
            "series": item["series"],
            "series_label": item["series_label"],
            "series_badge": item["series_badge"],
            "url": item["url"],
            "title": item["title"],
            "short_title": item["short_title"],
            "teaser": item["teaser"],
            "tags": item["tags"],
            "questions": item["questions"],
            "sections": item["sections"],
        }
        for item in data["all"]
    ]
    search_json = json.dumps(search_index, ensure_ascii=False, separators=(",", ":"))

    css_v = asset_hash(ASSETS_DIR / "site.css")
    js_v = asset_hash(ASSETS_DIR / "site.js")

    # 3. Generate all top-level routes
    build_home_page(data, search_json, css_v, js_v)
    build_archive_page(data, search_json, css_v, js_v)
    build_tags_page(data, search_json, css_v, js_v)
    build_about_page(data, search_json, css_v, js_v)
    build_404_page(data, search_json, css_v, js_v)
    build_feed_xml(data)

    print(
        f"Built unified site: /index.html, /archive/, /tags/, /about/, /404.html, /feed.xml "
        f"({len(data['all'])} total writings, {len(data['tags'])} tags, css={css_v}, js={js_v})"
    )


if __name__ == "__main__":
    main()
