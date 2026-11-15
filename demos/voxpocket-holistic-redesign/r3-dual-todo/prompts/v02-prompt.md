# v02 — 羊皮焦点 · P0 Hero Focus Card + Priority Lanes

画廊一句话：暖纸面上的唯一 P0 焦点卡统领真实优先级泳道，摘要藏在卡内，行动抽屉就地展开。

## Focus as an editorial object
This is B5 candidate two of four, not the previous v02 stream. Consume `briefs/T6-design-c.md` C1–C7 and the synthetic fixture relative to the Goal root; `spec.md` Section 5.5 supersedes historical ten-design requirements. Mirror: `r3-dual-todo/prompts/v02-prompt.md`. No theme winner, generated HTML or rendered acceptance is supplied here.

Warm parchment in LIGHT and almost-black obsidian in DARK follow VS-002 / CL-002, borrowing VS-005 task legibility. An actual P0 record becomes a generous editorial card; the remaining work is organized by actual priority, not by renamed strips. X makes the unique P0 hero primary; Y gives its lower edge an internal unfolding action drawer and gives lane cards shorter local drawers; Z keeps cards opaque with a neutral glass capture foot. P0 is red, P1 amber, P2 slate; status uses a separate blue/amber/green system.

## Hero ownership and genuine priority board
The main priority board contains three semantic groups P0/P1/P2, each with its own heading and ordered member list. Each member is one article owning summary, preview-footer and drawer; demo-01 is the first P0 article, NEVER copied into a separate banner above the P0 list. Desktop board uses a shared grid: the first P0 article spans the top row, P0's remaining members occupy the lower left lane, P1/P2 lists the lower middle/right lanes. The P0 semantic list participates in the board's shared/subgrid tracks rather than being duplicated; preserve list semantics if display-contents fallback is necessary. Initial P0 tail may have a mounted `暂无其他 P0` group message, not a fake task. Additional user-assigned P0 records remain compact, never become second oversized heroes.

Each summary retains status todo/inprogress/done, priority P0/P1/P2, full title, <=3 tag/area pills and time. Group membership derives from the edited priority; defer visual regrouping until collapse settles, then change stable grid allocation and accessible heading association, never remove/reappend the article. Do not replace the board or use three cosmetic labels above a single undifferentiated list. Independently author the card/grid stylesheet: spanning hero, compact priority lanes, opaque rounded card planes and local drawer tracks are its substance.

390×844 mobile: gutters20px (350px content),44px header beneath max(top safe inset,54px), P0 hero minimum208px/padding24px/radius24. Status and priority sit first, a28px serif title occupies its own line, tag/time wrap beneath; hero remains exactly five fields. Lower P0/P1/P2 lane headings have44px targets,32px section gaps, compact cards minimum120px/padding16px/radius16/gap12px. All three priority groups are reachable in the same vertical scroll, no horizontal board swipe or hidden P2 default. Hero drawer grows from its lower interior edge with24px content padding; lane drawers use16px, all sub-tasks minimum56px and grow for CJK.

At1280×800 / >=1000px: board max1120px, lower lane widths approximately336/344/344px with24px gaps (fluid, not fixed beyond the cap); hero top row spans full board and has28px padding. Expanded hero has a two-column INTERIOR: child checklist min280px, editor/export region min280px, gap32px; it is not a side inspector. Below1000px and at200% text stack both regions. Only root main scrolls vertically; card drawers have no nested wheel trap. Capture footer max560px desktop /350px mobile, body>=72px plus16px padding, auto-height,16px air and max(bottom safe inset,34px). Long held labels reduce available main height, never cover lanes. Titles and times wrap at320px, no ellipsis or horizontal page overflow.

## Parchment/obsidian :root palette
Roles below are exact LIGHT/DARK custom-property expectations. Body/root and gutters consume bg, compact lane cards surface, hero and drawer interiors focus. The current preview strip uses surface inside focus. In LIGHT the hero is lighter than parchment; in DARK it is a warm lifted plane above obsidian, not sonic blue.

| Role | LIGHT | DARK | Required painted role |
|---|---|---|---|
| bg | #F5F0E7 | #171513 | Board canvas and solid capture backing |
| surface | #FCF8F0 | #24201C | Compact cards, preview strip, opaque fallback |
| focus | #FFFDF7 | #332B25 | Hero, selected lane card and drawers |
| ink | #392F2A | #FAF2E7 | Card/child text and primary action labels |
| muted | #756253 | #D1BBA5 | Time, tags and secondary control labels |
| accent | #8E4D2B | #FFC39B | Copper disclosure and keyboard focus |
| statusTodo | #365E88 | #AECFFF | Pending blue ring and 待处理 |
| statusInprogress | #8C5718 | #F5CB86 | Amber progress arc and 进行中 |
| statusDone | #376747 | #A9DDB2 | Green check and 已完成 |
| priorityP0 | #AD3C35 | #FFA89E | Urgent red P0 badge/control text |
| priorityP1 | #8C5718 | #F5CB86 | Amber P1 badge/control text |
| priorityP2 | #756253 | #D1BBA5 | Slate-brown P2 badge/control text |

Every role must be used by the listed visible region/control and confirmed by computed style; no idle tokens to pass uniqueness. Status/priority labels use role-colored solid strokes/text, optional <=8% tint only behind, maintain readable labels and custom arcs/checks. Check ordinary/semantic text>=4.5:1 against bg/surface/focus, focus boundaries>=3:1 and actual optical blends later. Completed card text remains ink, not faded. Hero title uses local Georgia, 'New York', 'Songti SC', serif (CJK local serif fallback; no download); every field/control uses native SF stack. Mobile hero28/600/38, card17/550/26, control17/550/26, meta13/500/19; desktop hero32/600/44, card15/550/24, control13/550/20, meta12/500/18. Max four sizes, root-relative scaling, tabular times. Serif hero is an intentional exception to generic C6 sans typography.

## Preview footer, direct click and focus
A permanent footer slot INSIDE each article's summary boundary shows `剩余 N / 共 M 步 · 下一步：<首个未勾选项>`; completed children yield `共 M 步 · 子任务已完成`. It is noneditable and hidden initially, not a sixth always-visible field. Mouse title/preview hover160ms opens the strip, leaving article100ms closes, early leave cancels dwell. Focus on title or 预览任务 control shows instantly; Escape/blur outside article hides. Enter/Space on title always opens the drawer. Touch preview affordance>=44px toggles only this strip; second tap/outside tap/scroll dismisses. First title tap opens directly, no double-tap requirement; ignore synthesized mouse hover after touch. Expanded cards suppress preview, switching row previews never selects/expands or targets voice. Persistent slots and count/next-step text nodes update in place, including after a child check. All pending preview timers cancel on selection/platform/capture cancellation; C7 supplies shared edge rules.

## Local drawer, glass foot and motion
Hero unfolds a lower internal track, response .36s/damping .88; compact cards use .30s/.94. Only real content height pushes the priority board. Capture radius28/blur27px/saturate165%, LIGHT white .30 / DARK #584739 .40 tint, white top rim .75/edge .26; shadow0/12/32px warm-black .14. Optional Chromium Fresnel rim displacement<=2px, no content distortion; WebKit prefixed equal blur/saturate without displacement. Reduce Transparency yields opaque surface, never glass cards. Reduce Motion instant track/<=80ms opacity, no hero scale or lift; capture180ms acceptance remains unchanged. Custom 24px SVG rings stroke1.7/radius9.5, pending empty/progress arc/done check plus readable labels; individual child buttons role=checkbox/aria-checked. Mobile hit targets>=44px, desktop>=28px; two-column controls stack before clipping, native2px focus with3px offset.

## State evidence demanded of downstream implementation
Collapsed: only demo-01 is oversized, each priority lane contains its actual records once. Preview: hero's read-only next-step strip appears without changing expanded ID or counts. Expanded: hero or compact article retains its summary and unfolds checkable AI children, working status/priority/<=3 tags/time, 一键转 Linear Issue and 复制 Markdown with current-state previews/receipts. Node identities survive preview/expand/collapse/switch/check with removedElements=0 and no reparenting.

Held capsule in expanded demo-01 says exactly `🎙️ 正在继续补充至：<当前 Todo Title>`; release appends `补写一条反馈的对应修改` to that ID once, no new hero or parent. With no expanded card, even if one is previewed, exact `🎙️ 正在新建语音待办…` release creates complete demo-07 in P1, collapsed. Short tap, keyboard repeat, Escape, pointercancel/invalid leave/blur/selection change cancel without additions. C5 export is synthetic DEMO issue generation, never real sync; Copy Markdown follows actual clipboard outcome with mounted selectable fallback.

Reject cloned stream DOM, decorative wrapper boards, Notes, transcript, audio playback/listening bars, runner, extra routes, caustic stripes, rulers and raw checkboxes. Preserve Undo/reopen, independent parent/child checks, trusted theme hooks and dock-safe long titles. This prompt is a hand-crafted upstream direction only.
