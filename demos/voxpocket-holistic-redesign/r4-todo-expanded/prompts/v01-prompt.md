# v01 — 原地毛玻璃抽屉 · In-Place Frosted Glass Drawer

画廊一句话：点击待办在列表原位丝滑生长出内嵌毛玻璃双区抽屉，展示子任务勾选与五要素操作栏且上下文不断流。

## 设计身份与交接边界

Treat this candidate as a quiet glacier-slate reading stream that opens a working drawer, not a sheet pushed over the list. Category `todo-expanded`, round 4, candidate `v01`, selection key `todo-expanded/v01`. Consume this prompt together with `receipts/t7-d-design-contract.json`; authoritative direction is `briefs/T7-designer-d.md` and `spec.md` Section 6. Stage 1 supplies design instructions only. Stage 2 hand-crafts the page; no shared visual template, automatic prompt compiler, production change or publication is authorized here. This is an exploration candidate, not an Owner-selected AppTheme.

Lock mobile as the primary platform and use the exact Crisp Glacier Slate owner palette below. The archetype is VS-005 / CL-006 with a VoxPocket VS-003 precision accent, named AppTheme `D01.GlacierDrawer`. X reserves one focal object, demo-01; Y nests one open working drawer between its summary and the next row; Z refracts the drawer's functional perimeter and the two capture/navigation buttons while the actual reading surfaces stay opaque. Things/Bear's contextual checklist rhythm is a routing reference, not an instruction to copy their UI or to substitute their palette.

## 首帧：列表中已经长出的双区抽屉

Initialize page=todo_list and expandedId=demo-01 before first paint. Display `整理星桥样稿的反馈`, status todo/待处理, priority P0, tags #VoxPocket and #AI, time 今天 18:00. The open drawer has three unchecked children: 收集三条反馈, 按主题归类, 写一段结论. Below it, preserve the other five complete records from the contract fixture in their declared order. The first frame must show the first following row or a clear list continuation below the drawer, rather than an isolated full-screen detail panel. Do not animate from a closed shared startup frame.

A summary consists of exactly five fields: custom-ring status, priority, full title with its disclosure affordance, one field holding no more than three tags/areas, and time. Use one semantic ordered list; each stable list item owns its summary and a permanently mounted drawer track. Inside that track place two zones: an upper ordered checklist and a lower structured property/action workbench. There is no shared detail host, modal portal, priority board or sideways inspector. The lower workbench represents the same five values, including an ordinary one-line title editor that can grow; it does not invent a description field. Linear/Copy are detail actions, not sixth collapsed-row fields.

## 空间尺寸与独立布局规则

At 390×844 use 22px outer gutters, a plain `待办` heading after max(top safe inset,54px), and a main scroll well occupying the space above the bottom reservation. Summary ring occupies a 44px leading column; title/priority occupy the flexible center; tag/time metadata wraps to a second line. Summary minimum height104px, atom gap6px, padding18px, row-to-row gap12px. Drawer indentation is44px, radius22px, shell padding18px, child row minimum56px. The upper/lower zones are separated by24px whitespace and a leading-indented hairline, not two boxed cards. Use four type sizes: heading/title22px/600/30px, child/body17px/500/26px, controls15px/550/23px, metadata13px/500/20px. Native SF family only, tabular time, maximum four type sizes in view.

The page frame is header auto, main minmax(0,1fr), footer auto. Main alone scrolls vertically; a drawer grows within it and never creates its own nested scroll well. At320px or200% text remove the drawer indentation, stack metadata and property controls, keep44px targets, and let all titles/tags/counters wrap. At desktop1280×800 center a780px reading river; body16px, labels14px and meta13px with title24px, targets at least32px. Do not stretch a scaled phone or add desktop navigation chrome. Natural height, min-width:0 and16px scroll-padding keep the bottom of every expanded child reachable without horizontal page overflow or numeric ellipses.

## Crisp Glacier Slate — exact consumed roles

| Role | Light | Dark | Placement |
|---|---|---|---|
| bg | #F3F6FA | #0E1722 | Canvas and solid optical backing |
| surface | #FFFFFF | #162332 | Ordinary rows and readable fallback |
| focus | #EBF2FA | #1E3044 | Active summary and opaque drawer islands |
| ink | #142230 | #EDF4FC | Titles, children, input text |
| muted | #526477 | #9EB2C7 | Time, tags, subordinate labels |
| accent | #0F6292 | #6CC0F5 | Disclosure, active outline, focus |
| statusTodo | #0F6292 | #6CC0F5 | Empty ring and 待处理 |
| statusInprogress | #94580A | #F5C469 | Partial ring and 进行中 |
| statusDone | #1D6E47 | #7AD9A6 | Checked ring and 已完成 |
| priorityP0 | #B8323A | #FF8F96 | P0 token |
| priorityP1 | #94580A | #F5C469 | P1 token |
| priorityP2 | #526477 | #9EB2C7 | P2 token |

Paint the root/body with bg in both appearances; surface/focus must be actual visible surfaces, not unused uniqueness variables. Keep roughly90% neutral area and10% semantic accent. Status/priority text uses full-strength role colors over opaque surfaces; any badge tint is at most8% and must separately pass contrast. Use shape plus localized text, not color alone. Completed titles retain ink contrast. Ordinary text must reach4.5:1 and focus/state outlines3:1 on their real backing; compare blended values in the browser rather than citing these hex values as rendered proof.

## 毛玻璃：功能边缘折射，内容不被滤镜采样

The drawer is an authorized T7 interactive frosted shell, not a glass list row. Reserve a16–18px optical perimeter around opaque focus-colored checklist and workbench planes. Apply blur22px/saturate160%, light surface tint0.30 and dark surface tint0.48, top Fresnel rim white0.68/0.18 respectively, all-edge rim0.16/0.10, and shadow0/8/24px with ink opacity0.10/0.24. A single faint nonrepeating radial illumination may light the backing. Chromium may use edge-only signed Snell/Fresnel displacement up to1.5px with chromatic separation0.35px; never filter foreground text. WebKit disables displacement and uses matching backdrop-filter and -webkit-backdrop-filter blur/saturate with the clean rim. The two bottom buttons sample their own solid footer backing, never this drawer or each other. Reduced Transparency/no-filter support substitutes opaque surface and a solid rim. This describes an HTML optical approximation, not native Liquid Glass equivalence.

For drawer growth use a clipped inner wrapper within grid-template-rows:0fr→1fr, perceptual spring response0.30s/damping0.92, with an180ms opacity change. Geometry pushes later rows in normal flow; do not translate siblings independently. Clicking an open title collapses that track; selecting another title closes the old track and opens the new track as one continuous transaction. Reduced Motion uses immediate track allocation and at most80ms fading, without bounce, lens travel or scale; data and hold timings do not change.

## 仅两键的干净底部与双页侧滑

Only two interactive descendants belong to the bottom bar: left `切至录音页` / `返回待办`, right the persistent recording button. Left is a56×56px glass squircle; right is a min-height64px expanding glass capsule. Footer side padding22px, gap14px, bottom padding max(bottom safe inset,34px), and clear air16px above it. The right label wraps at full length and increases the reservation's actual height; never cover the last child or put the holding label in a third toast-button. There is no solid common dock plaque, tab strip, top pill, settings button or extra footer control.

Two permanent sibling canvases implement Todo⇄Recorder with a horizontal translate of one viewport over320ms, spring response0.32/damping1.0. A gesture beginning on unused canvas can switch after60px predominantly horizontal movement; vertical scrolling, child checks and hold gestures must not become paging. Left-button activation has equivalent behavior and accessible destination text. Switching first cancels any capture, remembers the previous expansion, sets visible expandedId=null on Recorder, and keeps the Todo subtree mounted/inert offscreen; returning restores the remembered expansion and scroll offset. Recorder is a sparse sentence canvas headed `录音`, using the same two buttons and no additional route; D does not modify the frozen production recorder, and introduces neither waveform nor transcript here. With Recorder active, capture makes a new Todo, not an append to an invisible selection.

## 行为事务、属性与结构化导出

Show recording intent immediately on pointerdown or focused Space down: when an expanded Todo is visible use exactly `🎙️ 正在继续补充至：<当前 Todo Title>` with its complete live title; otherwise use exactly `🎙️ 按住新建语音待办…`. Accept a hold at180ms, commit once on valid release, suppress the synthetic click, and append `核对反馈分类是否齐全` to that snapshotted Todo without changing its existing children or five fields. Keep the drawer open and announce `已补充 1 个步骤 · <完整任务标题>`. A no-selection release creates the complete demo-07 fixture, then monotonically numbered new records; these stay collapsed. Recorder stays visible after creation; on Todo the new row scrolls above the footer. Short taps, repeats, pointercancel, invalid pointer leave, unexpected capture loss, Escape, blur/pagehide, page switch or selection/edit change cancel without a delayed mutation. Normal capture loss after a committed release is harmless. No microphone permission or external service call; the synthetic capture transaction is deliberately local.

Status ring cycles todo→inprogress→done→todo without toggling the drawer; independently checkable children never auto-change the parent. Priority supports P0/P1/P2, title must stay nonempty, three reusable tag slots reject a fourth with `最多 3 个标签`, and a blank/invalid time retains the previous time with local guidance. Preserve a five-second status-completion Undo and later reopen; each row owns a mounted feedback slot OUTSIDE its five-field summary and clipped drawer, visible even while collapsed, never top/bottom chrome. Undo restores the prior parent value without losing independently checked children; invalidate any older undo timer/snapshot after another parent edit. Menus and title editing use ordinary inputs, never a Notes textarea.

Detail buttons read `一键转 Linear Issue` and `复制 Markdown`. Snapshot current five fields and children into a readable, mounted structured export preview. Linear generates a stable local DEMO-001 for demo-01, following the fixture ordinal for others, and reports `演示：已生成 Linear Issue · DEMO-001（未联网）`; repeat exports keep the identifier. Markdown contains title heading, Status/Priority/Tags/Time and checked task lines only. Report `已复制 Markdown（演示数据）` only after actual clipboard success; otherwise expose selectable plain text and `未复制：请选中文本后复制`. Never pretend to sync a real account or hide a failed clipboard call.

## 图标、身份、验收与禁止项

Use inline SVG viewBox0 0 24 24, currentColor, stroke1.7, round caps/joins, no external images or fonts. Drawer-specific disclosure is a small down chevron; status ring has center12,12 radius9, with an arc for inprogress and a short check for done. Child ring buttons use role=checkbox/aria-checked. Switch icon is two opposing horizontal arrows, record icon a static microphone outline, Copy two offset outline rectangles, Linear an ascending line with two short parallel strokes. Accessible labels identify task and destination; hide decorative vectors from the accessibility tree. Enter/Space on the title toggles; Escape collapses nearest transient layer and restores title focus; hidden drawers are inert. Mobile44px targets, desktop32px, focus2px with3px offset, polite single feedback announcements.

Before any expand/collapse/switch/check/slide, observe the whole page subtree through settlement plus two frames: removedElements = 0 and original node references survive. Initialize summaries, drawer bodies, editor slots, child rings and receipt text nodes up front. Edit existing Text.data/control properties; do not replace text elements, innerHTML, replaceChildren, remove, reparent or remount. New authorized Todo/child creation may add nodes, never rebuild the old stream. Verify default-open anatomy, child check, switching to demo-02, returning to demo-01, append/new distinction, two-way paging, cancellation, exports, both themes and320px/200% text. Preserve page-config, query theme=light|dark/platform=mobile|desktop|macos and trusted parent hooks; reject foreign source/origin and malformed enum payloads. Chooser owns bezel, summaries and SELECT/STAR/NOTES. Its card must show the exact escaped Chinese summary above the bezel.

Reject every audio playback/listening waveform bar, raw transcript comparison, Notes field/text/data, runner screen, three-tab navigation, top segmented pills, ruler, Active/Matte toggle, repeating caustic stripe and square native checkbox. Do not clone the other three candidates' DOM or CSS with a palette/radius swap. Actual Stage2 CSS rule and selector Jaccard overlap must be≤35% for all six pairs; static prompt agreement is not proof of rendered identity, geometry or optical quality.
