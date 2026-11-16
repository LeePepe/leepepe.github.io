# v03 — 半屏景深悬浮玻璃卡 · Half-Screen Z-Depth Floating Glass Card

画廊一句话：点击待办使背景列表景深微缩退后，中下部浮起带拖拽条与编号子任务卡的高折射半屏悬浮玻璃大卡。

## 一张从背景中浮出的执行卡

Build a jade-and-pearl spatial composition, as if an execution lens has lifted toward the hand while the task list recedes. Candidate key `todo-expanded/v03`; mobile-primary round4 exploration, not a production sheet or a chosen winner. Coordinates VS-003 / CL-003 are remixed with VS-006 calm spatial restraint and the exact owner Deep Botanical Jade & Pearl override, AppTheme `D03.JadeDepth`. X centers one active task, Y folds its working detail into a half-height overlay, Z distinctly separates the recessed solid list, functional optical shell, opaque reading islands and always-reachable bottom keys. Load `receipts/t7-d-design-contract.json` with this prompt; `briefs/T7-designer-d.md` and `spec.md` Section6 supply scope. Implementing or publishing HTML belongs to Stage2, not this handoff.

At startup the Todo canvas is already recessed, expandedId=demo-01 and its floating card is already raised. The card carries todo/待处理, P0, `整理星桥样稿的反馈`, #VoxPocket #AI and 今天 18:00. Number the three unchecked steps01 收集三条反馈,02 按主题归类,03 写一段结论. Behind it retain the other fixture records in a recognizable list; do not start with the same empty recorder or closed list used by other candidates. First-frame hierarchy must unmistakably show two Z-depth planes and a middle/lower card with a grabber, not an in-flow drawer or top hero.

## 三层内容树与可用性

The Todo viewport has a scrollable background ordered list plus a sibling floating-card layer containing one pre-mounted article per record. Every record has one backing data identity; its background summary and card header are two bound presentations, not runtime clones. While selected, hide that record's background summary from sight/accessibility to avoid a duplicate title; the remaining background list is inert during expansion. Exactly one card is visible and focusable. All cards and export/editor regions exist before interaction; resize, selection and collapse change geometry/visibility only. A newly authorized Todo creates its own summary and card article once.

The floating shell has a static horizontal grabber on top, an opaque five-field header, a vertically scrollable numbered-step region and a quiet property/export section. Header order is status, priority, title, tags/areas, time; collapse affordance belongs to the title, so no sixth field is added. Background summaries keep those same five fields and custom status circles. Step cards carry only number, circular check, task text; no transcript snippet, description, playback widget or Notes slot. Group the header and work area as two content islands within ONE optical shell, not multiple glass cards nested inside glass.

## 真正半屏、底键不遮挡

Reference frame390×844: root top safe padding max(env(top),54px), plain heading36px, content stage height S after footer actual height and16px air. Card height is0.54S, lower edge10px above the content-stage bottom, width available minus32px, side inset16px, corner radius30px. At the reference font this is an approximately half-screen working lens in the middle/lower field; it is NOT an80vh sheet. Header is natural height; body min-height:0 and scrollable, so long titles and controls never become clipped. Scale the background list to0.94 about50%35% and apply blur3px only to that inert plane. Opaque card text and the footer are never scaled or blurred. Preserve the background scroll offset for return.

Use14px optical shell padding,18px opaque-island padding,8px intra-card spacing and28px separation between major zones. Grabber is36×4px with a44px-high gesture hit zone, not an extra button in page/header/footer chrome. Numbered row minimum68px with44px circle target. Type sizes24px/650/32px title,17px/500/26px children,15px/550/23px controls and13px/500/20px time/number, local SF family; numbers have tabular width. At320px use side inset12px and stack metadata; at200% text the header grows but the card remains bounded to0.54S with its entire interior scrollable when necessary. Never ellipsize or shrink type to save the half-height effect.

At desktop1280×800 center a920px background list and float a760px card at the same lower/middle54% of usable stage, rather than moving detail to a side inspector. The card body may divide numbered steps and structured actions into60/40 columns; below820px use the compact stack. Desktop title26px, body17px, controls15px, meta13px, minimum32px hit areas. Maintain the same two footer corners and reserve their full wrapping-label height; short windows reduce the interior scroll region instead of overlapping capture. Assert every card bound remains above the footer reservation, with at least16px accessible clearance and no screen-wide horizontal scroll.

## Deep Botanical Jade & Pearl role bindings

| Color role | LIGHT | DARK | Visible region |
|---|---|---|---|
| bg | #EEF6F2 | #0E1D19 | Solid background and footer backing |
| surface | #F9FCFA | #162B25 | Background summaries, opaque fallback |
| focus | #E2F0EA | #1F3B33 | Card reading islands and current editor |
| ink | #14332A | #ECF9F4 | All task titles and step text |
| muted | #496A60 | #A5C7BC | Numbers, time, area labels |
| accent | #0D6E57 | #66DFBE | Selected rim, focus and grabber |
| statusTodo | #1E6087 | #8EC8F6 | Pending circle/label |
| statusInprogress | #8C540D | #F5C77E | Progress arc/label |
| statusDone | #146B48 | #82E0B0 | Done check/label |
| priorityP0 | #AE3640 | #FF96A0 | P0 text/stroke |
| priorityP1 | #8C540D | #F5C77E | P1 text/stroke |
| priorityP2 | #496A60 | #A5C7BC | P2 text/stroke |

Use the palette as a luminous neutral green field, never a saturated green panel. Root/body bg match; brighter surface/focus distinguish depth in both polarities. Nine-tenths of the view remains near-neutral. State colors are readable text and vector strokes with optional≤8% tints; they must not be opaque rainbow pills. Keep completed text at ink strength. Measure4.5:1 text and3:1 meaningful controls on actual opaque/blended backings. Background blur intentionally makes that plane noninteractive; it is not a contrast exception for the active card, and keyboard focus must never remain on a blurred inaccessible row.

## 高折射 shell 的光学分工

Use a clean optical perimeter sampled from the SOLID canvas underneath the overlay, not from a blurred/glass DOM ancestor. The visual background list may be blurred, but the card's dedicated backdrop sample plane is bg plus faint nonrepeating jade radial illumination. Shell blur26px/saturate170%, light tint0.24/dark0.46, top Fresnel highlight0.72/0.22, edge0.18/0.12, shadow0/18/42px ink0.14/0.32. Chromium's optional signed Snell/Fresnel background-edge displacement caps at2.5px, chromatic separation0.45px; reserve the14px perimeter so rays do not distort text. WebKit has zero displacement, matching backdrop-filter/-webkit-backdrop-filter blur/saturate, and a calm specular rim. Reduced Transparency removes refraction and fills surface, while retaining opaque focus text islands. No caustic banding, zebra overlay, shiny duplicated card or claim of native Liquid Glass rendering.

Bottom buttons use their own bg sample plane, blur22px/saturate150%, surface tint0.32/0.50, rim0.60/0.20 and displacement≤1.2px only in Chromium. They sit in a separate reservation, never overlap or sample the card. There is no shared glass plaque behind these two glass shapes. Keep controls crisp above all filter layers; the optical shell is a functional transient container explicitly allowed by T7, not permission to glass every task row or numbered card.

## 展开、拖拽退回与无障碍

Opening applies background scale0.94/blur3px over300ms and raises the card translateY36px→0 with response0.36s/damping0.90, fading within180ms. Collapsing reverses those properties without touching DOM identity. A downward drag beginning on the grabber collapses after64px; below that distance the card springs back. The entire44px grabber zone accepts pointer drag, but title click/Enter/Space and Escape offer equal collapse behavior without dragging. Vertical child-list scrolling must not trigger dismissal. There are no medium/large detent controls, full-screen upsell or second overlay state to confuse this half-screen study.

While open, move keyboard focus into the card title and keep background inert. This is a named detail region, not an aria-modal dialog: the two bottom buttons remain in the tab order. Escape closes the closest menu first, then the card, returning to its background title and restoring scale1/blur0. The user can then select a sibling to reopen a different card. Reduced Motion leaves the background at scale1/blur0, uses an immediate lower/middle card placement with≤80ms opacity and no displacement animation; do not conceal the signature half-height architecture. Detail fields and sub-task state remain identical across these modes.

## 单任务补录及新建契约

Footer contains exactly a bottom-left56×56px glass page-switch and a bottom-right recording capsule of at least64px height;16px side padding,14px gap, bottom safe padding max(env,34px). The right capsule grows naturally for full CJK intent text. No top segmented pills, bottom three tabs, separate close/cancel utility button or extra Settings entry. Left label alternates `切至录音页` / `返回待办`; its two permanent page canvases slide one width over340ms. A horizontal60px intent gesture on free background space can page, but when card is open use the explicit left key so child scroll/grabber gestures cannot accidentally navigate.

Page switch first aborts capture and card drag, remembers selected Todo and list scroll, clears visible expandedId and keeps the offscreen card/list mounted/inert. Recorder shows a minimal `录音` sentence surface and the same pair of keys, without waveform or transcript. A return restores the previous card unless the user collapsed it before leaving. D's preview recorder is not a modification of frozen production r3/v02. Capture on Recorder therefore enters new-Todo mode, never appending silently to a hidden card.

Immediately upon valid pointer/Space press present `🎙️ 正在继续补充至：<当前 Todo Title>` when the card is visible; otherwise present `🎙️ 按住新建语音待办…`. A180ms hold arms one token containing the expanded ID and title; valid release adds `核对三个步骤的执行先后` as the next numbered unchecked child, preserving every previous child/property and keeping the card open. A no-expanded release creates demo-07 and its complete declared five-field/three-child fixture; later creations advance IDs. Keep new records collapsed and visible above the footer when Todo is active, or announce creation without navigating away from Recorder. No temporary result drawer, Apply button or parent duplication.

Abort on short tap, key repeat, pointercancel/out-of-target release, unexpected pointer-capture loss, Escape, blur/pagehide, selection/page switch, title/property edits or grabber dismissal. Invalidate pending tokens so waiting past timers cannot add a child. Suppress post-hold click and treat ordinary post-commit capture loss as inert. These transactions use local synthetic data, require neither microphone permission nor a remote API, and do not change timing when reduced motion is enabled.

## 五字段编辑、输出与 SVG 品质

The header workbench edits nonempty title, status todo/inprogress/done, priority P0/P1/P2, no more than three reusable tag slots and valid nonempty time. An invalid edit rolls back with local guidance; a fourth tag says `最多 3 个标签`. Status click is separate from expansion; child checks do not auto-set parent status and parent done/reopen does not overwrite them. Retain a five-second Undo for completion in the visible card feedback line, or a mounted background-row feedback slot outside its five fields when no card is open; neither is top/footer chrome. Expose only the currently visible Undo presentation and cancel stale undo timers after further parent edits. All state updates must propagate to the background summary without reconstructing it.

Inside the card, `一键转 Linear Issue` serializes current five fields and checked children into a mounted selectable local object with stable DEMO-001-style identifier. Its exact receipt for demo-01 is `演示：已生成 Linear Issue · DEMO-001（未联网）`; never claim real sync or open a real issue URL. `复制 Markdown` exports title heading, Status/Priority/Tags/Time and checked task list. Only actual clipboard write completion permits `已复制 Markdown（演示数据）`; failure exposes selectable plain text and `未复制：请选中文本后复制`. No Notes, original speech, raw transcript or audio property may leak into either payload.

Vector vocabulary is bespoke:24×24 currentColor paths, stroke1.6 with rounded endpoints,9px status circles, numbered-step check rings with role=checkbox/aria-checked, a static microphone, two-direction switch arrows, offset outline Copy rectangles and diagonal Linear strokes. Grabber is a36px rounded line, never waveform bars. Accessible labels use complete titles; decorative numbers/vector art are hidden when equivalent text labels exist. Mobile44px and desktop32px targets,2px/3px-offset focus outline, ordinary keyboard menu navigation and one polite feedback per transaction are compulsory. No remote icon pack or raw square checkbox.

## 证据范围与硬性反模式

Writer records removedElements = 0 across card open/close, task switch, parent/child checks, drag-dismiss and page slide, through settling plus two animation frames. Pre-mount card bodies, children, field slots, receipt/export text nodes and the background summaries; use retained Text.data/property changes, never innerHTML/replaceChildren/removal/reparenting/remounting. New creation adds only its own nodes. Assert same element references, background inert/focus return, blur applied only to background, both bottom keys hit-testable, same-ID append, collapsed/new paths, cancellation and320px/200% text clearance in Chromium and WebKit. Query theme=light|dark/platform=mobile|desktop|macos and page-config/trusted parent messages survive; validate message source, allowed parent origin and enum payload, rejecting foreign/malformed inputs. External chooser alone owns bezel, SELECT/STAR/NOTES and exact escaped Chinese card summary.

Never introduce audio playback/listening bars, raw transcript comparison blocks, Notes field/textarea/text, fabricated runner/history/detail route, top/bottom tab clutter, caustic-veil/repeating stripes, Active/Matte controls or rulers. Independent CSS and semantic topology—not renamed classes—must keep all six D pairwise CSS rule/selector Jaccard overlaps≤35%. This Stage1 description does not certify actual blur, CSS, screenshots or published URLs.
