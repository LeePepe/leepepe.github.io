#!/usr/bin/env python3
"""Build the ai-workflow design lab pages (fonts + 3 layouts) from the real stories.

Usage: _build.py <stories-dir>   (files are written next to this script)
Pages have no front matter, so Jekyll copies them verbatim.
"""
import html
import pathlib
import re
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
STORIES = pathlib.Path(sys.argv[1])

GF = "https://fonts.googleapis.com/css2?family="
JSD = "https://cdn.jsdelivr.net/npm/@chinese-fonts"
FONT_LINKS = {
    "Noto Sans SC": GF + "Noto+Sans+SC:wght@400;500;700&display=swap",
    "Yozai": JSD + "/yozai@3.0.0/dist/Yozai-Regular/result.css",
    "LXGW Marker Gothic": GF + "LXGW+Marker+Gothic&display=swap",
    "Long Cang": GF + "Long+Cang&display=swap",
    "Ma Shan Zheng": GF + "Ma+Shan+Zheng&display=swap",
    "Zhi Mang Xing": GF + "Zhi+Mang+Xing&display=swap",
    "ZCOOL KuaiLe": GF + "ZCOOL+KuaiLe&display=swap",
    "ZCOOL XiaoWei": GF + "ZCOOL+XiaoWei&display=swap",
    "ChillRound": JSD + "/hcqyt@2.0.0/dist/ChillRoundFRegular/result.css",
}
FAMILY = {"ChillRound": "寒蝉全圆体", "Yozai": "Yozai"}

SERIES = "带一群 AI 干活"
INTRO = "这组文章写的是我用 AI 搭一个开发团队、再把它理成六条 workflow 的过程。每篇从一件真实发生的事讲起，按顺序读最顺。"

PALETTE = """
:root{--bg:#F6EFE6;--paper:#FFFDF9;--accent:#B7773D;--accent-soft:#F1E2CF;--ink:#4A3A2E;
--muted:#8B7766;--line:#E8DCCB;--code:#F3E9DC;
--hand:"LXGW Marker Gothic","Yozai","Noto Sans SC",sans-serif;
--title:"Long Cang","Yozai",cursive;
--body:"Noto Sans SC",-apple-system,"PingFang SC",sans-serif}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.9;
-webkit-text-size-adjust:100%;overflow-wrap:anywhere}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}
code{font-family:"SF Mono",Menlo,monospace;font-size:.86em;background:var(--code);padding:.1em .35em;border-radius:5px}
pre{background:var(--code);padding:14px 16px;border-radius:10px;overflow-x:auto;font-size:14px;line-height:1.6}
pre code{background:none;padding:0}
blockquote{margin:1.4em 0;padding:.2em 1.1em;border-left:3px solid var(--accent);color:var(--muted)}
.prose h2{font-family:var(--hand);font-weight:400;font-size:1.45em;line-height:1.5;margin:2.2em 0 .7em;color:var(--ink)}
.prose p{margin:0 0 1.15em}
"""

DOODLE_CUP = """<svg class="cup" viewBox="0 0 120 110" aria-hidden="true"><g fill="none" stroke="#B7773D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
<path d="M22 46c2 30 12 46 36 46s34-16 36-46z"/><path d="M94 54c14-2 18 18 2 22"/><path d="M14 98c20 6 70 6 92 0"/>
<path d="M44 34c-6-8 6-12 0-22"/><path d="M60 32c-6-9 7-13 0-24"/><path d="M76 34c-6-8 6-12 0-22"/></g></svg>"""
WAVE = """<svg class="wave" viewBox="0 0 220 14" preserveAspectRatio="none" aria-hidden="true"><path d="M2 8c18-8 36 8 54 0s36-8 54 0 36 8 54 0 36-8 54 0" fill="none" stroke="#B7773D" stroke-width="2.5" stroke-linecap="round"/></svg>"""


def load_stories():
    out = []
    for p in sorted(STORIES.glob("[0-9][0-9]-*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"#\s+(.+)\n+", text)
        title, body = m.group(1).strip(), text[m.end():]
        first = next(l for l in body.splitlines() if l.strip() and not l.startswith("#"))
        teaser = re.split(r"(?<=[。？])", first)[0]
        if len(teaser) > 52:
            teaser = teaser[:50] + "…"
        out.append({"n": int(p.name[:2]), "title": title, "body": body, "teaser": teaser,
                    "html": markdown.markdown(body, extensions=["fenced_code"])})
    return out


def head(title, extra_css, fonts=("Noto Sans SC", "LXGW Marker Gothic", "Long Cang")):
    links = "\n".join(f'<link rel="stylesheet" href="{FONT_LINKS[f]}">' for f in fonts)
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | Lee Pepe</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{links}
<style>{PALETTE}{extra_css}</style></head>"""


def headings(story):
    return re.findall(r"^## (.+)$", story["body"], re.M)


def add_ids(h, prefix="s"):
    i = 0

    def rep(m):
        nonlocal i
        i += 1
        return f'<h2 id="{prefix}{i}">'
    return re.sub(r"<h2>", rep, h)


# ---------- fonts.html ----------
def build_fonts(stories):
    s4 = stories[3]
    para = s4["body"].split("\n\n")[1] if not s4["body"].split("\n\n")[1].startswith("#") else s4["body"].split("\n\n")[2]
    para = re.sub(r"`([^`]+)`", r"\1", para)
    h2 = headings(s4)[1]
    rows = [
        ("Yozai", "悠哉字体", "日常手写风，亲和；和霞鹜文楷同源，观感接近文楷", "SIL OFL 1.1（npm 包 @chinese-fonts/yozai, MIT 打包）", "jsDelivr 切片；本篇标题 ≈510KB，全文 ≈860KB", True, True),
        ("LXGW Marker Gothic", "霞鹜漫黑", "马克笔写的黑体，笔画有手作的毛边，标题很有个性", "SIL OFL 1.1", "Google Fonts 切片；标题 ≈460KB", True, False),
        ("Long Cang", "龙藏体", "真实的钢笔行书手写，最有“亲笔”的味道，只适合大标题和装饰", "SIL OFL 1.1", "Google Fonts 切片；标题 ≈670KB", True, False),
        ("ZCOOL KuaiLe", "站酷快乐体", "圆润活泼，很轻，偏可爱", "SIL OFL 1.1", "Google Fonts；标题 ≈210KB（最轻）", False, False),
        ("ZCOOL XiaoWei", "站酷小薇", "带书法笔意的宋体，温和文艺，可做标题", "SIL OFL 1.1", "Google Fonts；标题 ≈440KB", False, False),
        ("Ma Shan Zheng", "马善政毛笔楷", "毛笔楷书，墨感很重，适合封面大字", "SIL OFL 1.1", "Google Fonts；标题 ≈750KB", False, False),
        ("Zhi Mang Xing", "志莽行书", "行书，潇洒但小字号不易读", "SIL OFL 1.1", "Google Fonts；标题 ≈550KB", False, False),
        ("ChillRound", "寒蝉全圆体", "圆体，柔和，可以做正文", "SIL OFL 1.1（npm 包 @chinese-fonts/hcqyt）", "jsDelivr 切片；全文 ≈840KB", False, True),
    ]
    cards = []
    for name, cn, desc, lic, size, top, body_ok in rows:
        fam = FAMILY.get(name, name)
        badge = '<span class="top">推荐</span>' if top else ""
        body_demo = (f'<p class="demo-body" style="font-family:\'{fam}\'">{html.escape(para)}</p>'
                     if body_ok else
                     f'<p class="demo-body">{html.escape(para)}</p><p class="note">正文仍用 Noto Sans SC，这款只用于标题。</p>')
        cards.append(f"""<section class="spec">
<header><h3>{name} · {cn} {badge}</h3><p class="meta">{desc}<br>授权：{lic} · 加载：{size}</p></header>
<div class="demo-series" style="font-family:'{fam}'">{SERIES}</div>
<div class="demo-title" style="font-family:'{fam}'">{html.escape(s4['title'])}</div>
<div class="demo-h2" style="font-family:'{fam}'">{html.escape(h2)}</div>
{body_demo}</section>""")
    css = """
main{max-width:860px;margin:0 auto;padding:40px 16px 80px}
h1{font-family:var(--title);font-weight:400;font-size:44px;margin:.2em 0}
.lead{color:var(--muted)}
.spec{background:var(--paper);border-radius:18px;padding:22px 24px;margin:22px 0;box-shadow:0 6px 24px rgba(120,80,40,.08)}
.spec h3{margin:0;font-size:18px;font-weight:700}
.top{display:inline-block;margin-left:6px;padding:0 10px;border-radius:99px;background:var(--accent);color:#fff;font-size:13px;vertical-align:2px}
.meta{margin:.3em 0 1em;color:var(--muted);font-size:14px;line-height:1.7}
.demo-series{font-size:22px;color:var(--accent)}
.demo-title{font-size:34px;line-height:1.35;margin:.2em 0}
.demo-h2{font-size:24px;margin:.4em 0 .5em}
.demo-body{font-size:17px;margin:.4em 0 0}
.note{font-size:13px;color:var(--muted);margin:.2em 0 0}
"""
    page = head("字体样张", css, tuple(FONT_LINKS)) + f"""<body><main>
<p><a href="./">← 设计实验室</a></p>
<h1>字体样张</h1>
<p class="lead">同一段真实内容，换不同的手写感字体。背景是咖啡色系。所有字体都按用到的字切片加载，下面的体积是一篇文章页实际要下载的量（估算）。</p>
{''.join(cards)}</main></body></html>"""
    (HERE / "fonts.html").write_text(page, encoding="utf-8")


# ---------- layout 1: magazine cover ----------
def build_layout1(stories):
    s4 = stories[3]
    cards = "".join(f"""<a class="card" href="#read"><span class="no">{st['n']:02d}</span>
<span class="t">{html.escape(st['title'])}</span><span class="teaser">{html.escape(st['teaser'])}</span></a>""" for st in stories)
    nxt = stories[4]
    css = """
.wrap{max-width:1040px;margin:0 auto;padding:0 16px}
.cover{position:relative;margin:24px auto 0;max-width:1040px;border-radius:28px;background:linear-gradient(160deg,#EAD7BF,#F6EFE6 60%);padding:64px 48px 56px;overflow:hidden}
.cover .cup{position:absolute;right:48px;bottom:36px;width:150px;opacity:.9}
.kicker{letter-spacing:.3em;color:var(--accent);font-size:14px}
.cover h1{font-family:var(--title);font-weight:400;font-size:84px;line-height:1.05;margin:.15em 0 .1em;color:#3D2E23}
.cover .wave{display:block;width:260px;height:16px;margin:0 0 18px}
.cover p{max-width:520px;font-size:17px;color:#6B5646;margin:0}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin:36px 0 64px}
.card{display:flex;flex-direction:column;gap:6px;background:var(--paper);border-radius:20px;padding:22px 24px;text-decoration:none;color:var(--ink);
box-shadow:0 6px 22px rgba(120,80,40,.08);transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(120,80,40,.14)}
.card .no{font-family:var(--title);font-size:34px;line-height:1;color:var(--accent)}
.card .t{font-family:var(--hand);font-size:22px;line-height:1.4}
.card .teaser{font-size:14px;color:var(--muted);line-height:1.7}
.divider{text-align:center;color:var(--muted);margin:24px 0;letter-spacing:.4em}
.article{max-width:760px;margin:0 auto 80px;background:var(--paper);border-radius:28px;overflow:hidden;box-shadow:0 8px 34px rgba(120,80,40,.1)}
.a-hero{background:linear-gradient(160deg,#EAD7BF,#F3E6D5);padding:56px 48px 40px;position:relative}
.a-hero .big{font-family:var(--title);font-size:120px;line-height:.8;color:rgba(183,119,61,.35);position:absolute;right:36px;top:26px}
.a-hero .series{font-size:14px;color:var(--accent);letter-spacing:.15em}
.a-hero h1{font-family:var(--hand);font-weight:400;font-size:40px;line-height:1.35;margin:.3em 0 .2em;max-width:85%}
.a-hero .date{color:#8B7766;font-size:14px}
.prose{padding:24px 48px 40px}
.next{display:block;margin:0 48px 48px;padding:22px 24px;border-radius:20px;background:var(--accent-soft);text-decoration:none;color:var(--ink)}
.next small{color:var(--accent)}
.next b{display:block;font-family:var(--hand);font-weight:400;font-size:22px}
@media (max-width:640px){
.cover{border-radius:0;margin:0;padding:48px 20px 150px}
.cover h1{font-size:44px;white-space:nowrap}.cover .cup{right:24px;bottom:24px;width:110px}
.grid{grid-template-columns:1fr;gap:14px}
.article{border-radius:0}
.a-hero{padding:40px 20px 28px}.a-hero h1{font-size:30px;max-width:100%}.a-hero .big{position:static;display:block;font-size:56px;margin-bottom:6px}
.prose{padding:16px 20px 28px}.next{margin:0 20px 32px}}
"""
    page = head("布局一：杂志封面", css) + f"""<body>
<header class="cover"><div class="kicker">LEE PEPE · 系列</div><h1>{SERIES}</h1>{WAVE}<p>{INTRO}</p>{DOODLE_CUP}</header>
<div class="wrap"><nav class="grid">{cards}</nav><div class="divider">· · ·　文章页　· · ·</div></div>
<article class="article" id="read"><div class="a-hero"><span class="big">04</span><div class="series">{SERIES} · 第 4 篇</div>
<h1>{html.escape(s4['title'])}</h1><div class="date">2026 年 10 月 14 日 · 约 8 分钟</div></div>
<div class="prose">{s4['html']}</div>
<a class="next" href="#read"><small>下一篇 →</small><b>{html.escape(nxt['title'])}</b></a></article>
</body></html>"""
    (HERE / "layout-1.html").write_text(page, encoding="utf-8")


# ---------- layout 2: letter / notebook ----------
def build_layout2(stories):
    s4 = stories[3]
    toc = "".join(f"""<li><a href="#read"><span class="t">{html.escape(st['title'])}</span><span class="dots"></span><span class="no">{st['n']}</span></a></li>""" for st in stories)
    steps = "".join(f'<a class="step{" on" if st["n"]==4 else (" done" if st["n"]<4 else "")}" href="#read" title="{html.escape(st["title"])}">{st["n"]}</a>' for st in stories)
    body = add_ids(s4["html"])
    marg = "".join(f'<span class="margin-note" style="--i:{i}">{t}</span>' for i, t in enumerate(["六点", "命令", "白天", "修法", "傍晚", "修复", "后来"], 1))
    css = """
.desk{padding:40px 16px 80px}
.letter{position:relative;max-width:720px;margin:0 auto 48px;background:var(--paper);border-radius:6px;padding:64px 64px 56px 88px;
box-shadow:0 1px 0 #E8DCCB,0 18px 40px -18px rgba(120,80,40,.25);
background-image:linear-gradient(90deg,transparent 60px,rgba(183,119,61,.35) 60px,rgba(183,119,61,.35) 61px,transparent 61px),
repeating-linear-gradient(transparent 0 31px,rgba(183,119,61,.09) 31px 32px)}
.letter::before{content:"";position:absolute;top:-10px;left:50%;width:120px;height:26px;transform:translateX(-50%) rotate(-2deg);background:rgba(234,215,191,.85)}
.hello{font-family:var(--title);font-size:30px;color:var(--accent);margin:0}
.letter h1{font-family:var(--hand);font-weight:400;font-size:42px;line-height:1.3;margin:.2em 0 .4em}
.letter .intro{font-size:17px}
.toc{list-style:none;padding:0;margin:28px 0 8px;counter-reset:x}
.toc li a{display:flex;align-items:baseline;gap:8px;padding:9px 0;text-decoration:none;color:var(--ink)}
.toc .t{font-family:var(--hand);font-size:20px}
.toc .dots{flex:1;border-bottom:2px dotted rgba(183,119,61,.45);transform:translateY(-6px)}
.toc .no{font-family:var(--title);font-size:24px;color:var(--accent)}
.sign{font-family:var(--title);font-size:26px;text-align:right;color:var(--muted);margin:24px 0 0}
.stepper{position:sticky;top:0;z-index:5;background:rgba(246,239,230,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.stepper .in{max-width:720px;margin:0 auto;display:flex;align-items:center;gap:10px;padding:10px 16px;overflow-x:auto}
.stepper .label{font-family:var(--hand);font-size:15px;white-space:nowrap;color:var(--muted)}
.step{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-size:13px;text-decoration:none;border:1.5px solid var(--accent);color:var(--accent)}
.step.done{background:var(--accent-soft)}
.step.on{background:var(--accent);color:#fff}
.progress{height:3px;background:var(--accent);width:38%}
.post{position:relative}
.post .series{font-size:14px;color:var(--accent);letter-spacing:.12em}
.post h1{font-size:38px}
.post .date{color:var(--muted);font-size:14px;margin-bottom:12px}
.margin-note{display:none}
@media (min-width:1100px){.margin-note{display:block;position:absolute;left:-150px;width:110px;text-align:right;font-family:var(--title);font-size:22px;color:var(--accent);transform:rotate(-4deg)}}
.pager{display:flex;justify-content:space-between;gap:12px;border-top:2px dotted rgba(183,119,61,.45);margin-top:32px;padding-top:18px;font-family:var(--hand);font-size:18px}
.pager a{text-decoration:none}
@media (max-width:640px){.desk{padding:24px 10px 56px}
.letter{padding:48px 18px 36px 34px;background-image:linear-gradient(90deg,transparent 22px,rgba(183,119,61,.35) 22px,rgba(183,119,61,.35) 23px,transparent 23px),repeating-linear-gradient(transparent 0 31px,rgba(183,119,61,.09) 31px 32px)}
.letter h1{font-size:32px}.post h1{font-size:28px}.toc .t{font-size:18px}}
"""
    # place margin notes next to h2s
    notes = ["六点", "原因", "白天", "修法", "傍晚", "修复", "后来"]
    k = 0

    def note(m):
        nonlocal k
        t = notes[k] if k < len(notes) else ""
        k += 1
        return f'{m.group(0)}<span class="margin-note">{t}</span>'
    body = re.sub(r'<h2 id="s\d+">', note, body)
    page = head("布局二：信笺", css) + f"""<body><div class="desk">
<section class="letter"><p class="hello">读到这里的你：</p><h1>{SERIES}</h1><p class="intro">{INTRO}</p>
<ol class="toc">{toc}</ol><p class="sign">—— Lee Pepe</p></section>
</div>
<div class="stepper" id="read"><div class="in"><span class="label">第 4 / 8 篇</span>{steps}</div><div class="progress"></div></div>
<div class="desk"><article class="letter post"><div class="series">{SERIES} · 第 4 篇</div><h1>{html.escape(s4['title'])}</h1>
<div class="date">2026 年 10 月 14 日</div><div class="prose">{body}</div>
<nav class="pager"><a href="#read">← {html.escape(stories[2]['title'])}</a><a href="#read">{html.escape(stories[4]['title'])} →</a></nav></article></div>
</body></html>"""
    (HERE / "layout-2.html").write_text(page, encoding="utf-8")


# ---------- layout 3: two-pane reader ----------
def build_layout3(stories):
    s4 = stories[3]
    body = add_ids(s4["html"])
    outline = "".join(f'<li><a href="#s{i}">{html.escape(h)}</a></li>' for i, h in enumerate(headings(s4), 1))
    chapters = []
    for st in stories:
        cls = "on" if st["n"] == 4 else ("done" if st["n"] < 4 else "")
        mark = "✓" if st["n"] < 4 else str(st["n"])
        sub = f'<ol class="outline">{outline}</ol>' if st["n"] == 4 else ""
        chapters.append(f'<li class="{cls}"><a href="#top"><span class="m">{mark}</span><span>{html.escape(st["title"])}</span></a>{sub}</li>')
    nav = "".join(chapters)
    css = """
.shell{display:grid;grid-template-columns:300px 1fr;min-height:100vh}
.side{position:sticky;top:0;height:100vh;overflow-y:auto;padding:28px 22px;background:#EFE4D6;border-right:1px solid var(--line)}
.side .brand{font-family:var(--title);font-size:34px;line-height:1.1;color:#3D2E23;margin:0 0 4px}
.side .meta{font-size:13px;color:var(--muted);margin:0 0 14px}
.bar{height:6px;border-radius:99px;background:#E3D3BF;overflow:hidden;margin:0 0 18px}.bar i{display:block;height:100%;width:44%;background:var(--accent);border-radius:99px}
.chapters{list-style:none;margin:0;padding:0}
.chapters>li>a{display:flex;gap:10px;align-items:flex-start;padding:9px 10px;border-radius:12px;text-decoration:none;color:var(--ink);font-family:var(--hand);font-size:16px;line-height:1.45}
.chapters .m{flex:none;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-family:var(--body);font-size:12px;border:1.5px solid var(--accent);color:var(--accent)}
.chapters li.done .m{background:var(--accent);color:#fff}
.chapters li.on>a{background:var(--paper);box-shadow:0 4px 14px rgba(120,80,40,.1)}
.outline{margin:6px 0 10px 44px;padding:0;list-style:none;border-left:2px solid var(--line)}
.outline a{display:block;padding:4px 0 4px 12px;font-size:13px;color:var(--muted);text-decoration:none;line-height:1.5}
.outline a:hover{color:var(--accent)}
.main{padding:48px 32px 80px}
.paper{max-width:700px;margin:0 auto;background:var(--paper);border-radius:22px;padding:48px 56px;box-shadow:0 8px 30px rgba(120,80,40,.08)}
.paper .series{display:inline-block;padding:2px 12px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font-size:13px}
.paper h1{font-family:var(--hand);font-weight:400;font-size:38px;line-height:1.35;margin:.4em 0 .2em}
.paper .date{color:var(--muted);font-size:14px}
.ends{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:36px}
.ends a{display:block;padding:16px 18px;border-radius:16px;background:var(--accent-soft);text-decoration:none;color:var(--ink);font-family:var(--hand);font-size:17px}
.ends small{display:block;font-family:var(--body);color:var(--accent);font-size:12px}
.drawer{display:none}
@media (max-width:860px){
.shell{display:block}.side{display:none}
.drawer{display:block;position:sticky;top:0;z-index:5;background:rgba(239,228,214,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.drawer summary{list-style:none;display:flex;justify-content:space-between;align-items:center;padding:12px 16px;font-family:var(--hand);font-size:16px;cursor:pointer}
.drawer summary::-webkit-details-marker{display:none}
.drawer summary b{font-weight:400;color:var(--accent)}
.drawer .bar{margin:0 16px 10px}
.drawer .chapters{padding:0 10px 14px;max-height:70vh;overflow-y:auto}
.main{padding:16px 10px 56px}.paper{padding:28px 18px;border-radius:16px}.paper h1{font-size:28px}
.ends{grid-template-columns:1fr}}
"""
    page = head("布局三：双栏阅读", css) + f"""<body id="top">
<details class="drawer"><summary><span>{SERIES} · 第 4 / 8 篇</span><b>目录 ▾</b></summary><div class="bar"><i></i></div><ol class="chapters">{nav}</ol></details>
<div class="shell"><aside class="side"><p class="brand">{SERIES}</p><p class="meta">8 篇 · 已读 3 篇</p><div class="bar"><i></i></div><ol class="chapters">{nav}</ol></aside>
<main class="main"><article class="paper"><span class="series">第 4 篇</span><h1>{html.escape(s4['title'])}</h1><div class="date">2026 年 10 月 14 日 · 约 8 分钟</div>
<div class="prose">{body}</div>
<nav class="ends"><a href="#top"><small>← 上一篇</small>{html.escape(stories[2]['title'])}</a><a href="#top"><small>下一篇 →</small>{html.escape(stories[4]['title'])}</a></nav></article></main></div>
</body></html>"""
    (HERE / "layout-3.html").write_text(page, encoding="utf-8")


def build_index():
    css = """main{max-width:720px;margin:0 auto;padding:48px 16px 80px}
h1{font-family:var(--title);font-weight:400;font-size:52px;margin:.1em 0}
.item{display:block;background:var(--paper);border-radius:18px;padding:18px 22px;margin:14px 0;text-decoration:none;color:var(--ink);box-shadow:0 6px 20px rgba(120,80,40,.08)}
.item b{font-family:var(--hand);font-weight:400;font-size:22px;display:block}.item span{color:var(--muted);font-size:15px}"""
    items = [("fonts.html", "字体样张", "8 款手写感／温暖字体放在同一段真实内容上对比，标了授权和加载体积，前 3 款是推荐。"),
             ("layout-1.html", "布局一：杂志封面", "系列有一张封面大图和手绘咖啡杯，文章是带章节大号码的卡片，适合当“一本小册子”。"),
             ("layout-2.html", "布局二：信笺", "像一封写在格子纸上的信：手写称呼、目录虚线引导、顶部 8 个圆点的进度条、页边手写批注。"),
             ("layout-3.html", "布局三：双栏阅读", "左边固定的系列目录和本篇小标题、阅读进度；右边正文。手机上目录收进顶部抽屉。")]
    links = "".join(f'<a class="item" href="{u}"><b>{t}</b><span>{d}</span></a>' for u, t, d in items)
    page = head("设计实验室", css) + f"""<body><main><p><a href="/ai-workflow/">← 回到系列</a></p><h1>设计实验室</h1>
<p>保留咖啡色系，换手写感字体，重新设计布局。三个布局都用同一篇真实文章（第 4 篇）。</p>{links}</main></body></html>"""
    (HERE / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    st = load_stories()
    build_fonts(st)
    build_layout1(st)
    build_layout2(st)
    build_layout3(st)
    build_index()
    print("built", sorted(p.name for p in HERE.glob("*.html")))
