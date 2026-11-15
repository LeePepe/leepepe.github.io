# v01 — 矿物光流 · Borderless Luminance Stream + Inline Spring Drawer

画廊一句话：无框矿物色阶串起完整待办，轻触看下一步，点击后抽屉沿原任务流弹簧下推。

## B5 intention — a river, not a board
Only one of FOUR current B5 candidates. Read goal-relative `briefs/T6-design-c.md` C1–C7 and fixture; source authority is `spec.md` Section 5.5. This prompt and `r3-dual-todo/prompts/v01-prompt.md` are byte-identical upstream instructions, not rendered approval. No winner or frozen AppTheme.

Cool Mineral Air uses VS-005 / CL-006 as a borderless reading river. A small status ring is the leading punctuation; luminance, not a perimeter, reveals attention. X gives demo-01's P0 text first attention without a hero card; Y opens a drawer within one ordered stream; Z leaves all task content opaque and reserves optics for capture. No priority buckets, area panels, segmented lens or detached detail pane. Fixture order is the only ordering rule.

## Content tree and independent spatial stylesheet
Semantic outline: root header / main scroll well / reserved capture footer; main contains one ordered list; each list item owns a five-field summary grid, a permanent noneditable preview slot and a permanent drawer track. The drawer contains an AI sub-task ordered list, a fieldset for status/priority/tag/time and an export/receipt region. There are no article cards or shared detail hosts. The layout stylesheet is authored for this stream: full-width luminance bands, a leading 44px ring column, flexible text column and vertically growing grid track; do not import a board stylesheet with renamed selectors.

Closed state shows status todo/inprogress/done, priority P0/P1/P2, full title, one <=3-pill tag/area field and time. Preview/disclosure buttons belong to the title field, not a sixth field. All rows are fully legible; no hidden status groups. Hovered/previewed row changes from bg to surface; expanded summary and its drawer use focus. Nonselected rows remain bg, without alternating zebra washes, shadows or borders.

Mobile 390×844: side gutters24px, native header44px following max(top safe inset,54px); list inner width342px. Summary minimum112px; demo-01 uses the same grid, title22/600/30 rather than oversized card geometry. Ring target44×44px; title/priority wrap beside it; tags and tabular time share a lower line that stacks at <=350px. Atom gap6px, row padding16px, inter-row air12px. Drawer indents44px on ordinary widths, removes indentation at <=350px/200% text, uses16px inner padding and >=56px growing sub-task rows. Main is the sole vertical scroll region; no independently scrolling drawer.

Desktop1280×800: >=900px center a760px reading river; ring column32px and title region flex, metadata wraps at trailing edge. Open track remains under the same row with32px indent. At smaller widths use the mobile stream without scaling type. Footer width is available minus48px mobile (342px at reference), max600px desktop; readable capsule body minimum72px, padding16px. Reserve its actual auto-height plus16px air and max(bottom safe inset,34px); it grows with a full held title. Main min-height0 and scroll-padding16px prevent dock occlusion; 320px and 200% text wrap all titles/tags/numbers, never clamp or ellipsize.

## Exact :root role map and rendered polarity
Each table row declares the required semantic custom property, not implementation CSS. Both appearance maps are complete; computed body/root background equals bg, stream rows bg, preview surface, expanded drawer focus. All role values must actually be consumed, never parked as uniqueness tokens.

| Role | LIGHT | DARK | Visible consumption |
|---|---|---|---|
| bg | #F2F6F7 | #14232B | Root, middle stream, solid footer backing |
| surface | #F8FAFB | #21343F | Preview band and opaque capture fallback |
| focus | #FFFFFF | #2D4552 | Selected summary, drawer and editor backing |
| ink | #203840 | #F0F7FA | Titles, child text, ordinary controls |
| muted | #52656D | #B5C8D0 | Tag/time labels and secondary action copy |
| accent | #176F89 | #91D9ED | Focus ring and preview/disclosure affordances |
| statusTodo | #176F89 | #91D9ED | Blue pending circle + 待处理 label |
| statusInprogress | #875409 | #F5C879 | Amber partial arc + 进行中 label |
| statusDone | #226847 | #9AD9B6 | Green checked ring + 已完成 label |
| priorityP0 | #AC3D36 | #FFA49C | Red P0 text and priority control stroke |
| priorityP1 | #875409 | #F5C879 | Amber P1 text and priority control stroke |
| priorityP2 | #52656D | #B5C8D0 | Slate P2 text and priority control stroke |

LIGHT steps toward brighter content; DARK uses brighter opaque focus above deep mineral bg. Use solid role-colored text/strokes on these backings; optional semantic fill<=8% must not be the only distinction. All ordinary text, status and priority labels >=4.5:1 against every declared content surface; boundaries/focus>=3:1. No blue-for-every-state coding or opacity-dimmed completed title. Native SF stack, mobile title22/600/30, row/control17/500/26, meta13/500/19; desktop title24/600/33, row15/500/24, control13/550/20, meta12/500/18. Root-relative scaling and tabular time; max four sizes per pane.

## Read-only preview with explicit input transitions
A mounted slot under the metadata reveals `剩余 N / 共 M 步 · 下一步：<首个未勾选子任务>`; all done becomes `共 M 步 · 子任务已完成`. This derives from current child state, never authored Notes or speech. Desktop mouse entering title/preview affordance starts160ms dwell; leaving before dwell cancels. Leave the entire row for100ms hides preview; re-entry cancels hide. Keyboard focus on title or its separately named 预览任务 button reveals immediately; blur outside row/Escape hides, Enter/Space on title expands directly. Touch: one light tap on the >=44px preview affordance toggles the slot, second tap/outside tap/scroll/Escape dismisses; tapping title directly expands on the first tap, never requires a preview tap first. Touch-generated mouse events cannot reopen it. Preview adds only transient in-flow height and no editable/focusable content; it does not set expanded ID. Only one preview across rows; opening any drawer hides preview. Timers invalidate on input/platform/selection changes. removedElements=0 on preview show/hide, expand/collapse/switch/check; pre-mount slots, text nodes, circles, controls and receipts.

## Drawer motion, optics and controls
Row track changes 0fr→1fr with response .30s/damping .92, opacity<=180ms, translating no siblings independently: real track growth pushes later rows. Capsule radius24, blur24px/saturate170%; white tint .26 LIGHT, #2A4C61 .40 DARK over solid backing, white rim .22/top .70, shadow 0/8/26px navy .12. Optional Chromium edge-only displacement<=1.5px; WebKit disables displacement and uses equal prefixed blur/saturate. No blur/filter on task or preview text. Reduce Transparency uses opaque surface; Reduce Motion instant geometry/<=80ms fade, no bounce/scale, same capture timings. Custom SVG circle center12/12 radius9, currentColor stroke1.7 with state arc/check; child buttons role=checkbox with aria-checked. Title and actions >=44px mobile/>=28px desktop, visible 2px focus with3px offset; no raw square checks.

## Five required showcase outcomes
Collapsed: six complete ungrouped rows, all five fields. Preview: demo-01 exposes count/next step in its own luminance slot. Expanded: its existing AI children are independently checkable; live status/priority/<=3 tags/time and 一键转 Linear Issue / 复制 Markdown are available in the mounted drawer, matching C2/C5. Expand/collapse/switch/check never removes, reparents or rebuilds existing nodes.

Append holds the anchored capsule with exact `🎙️ 正在继续补充至：<当前 Todo Title>` (full selected title); release adds `核对反馈分类是否齐全` once to that same expanded ID. Preview alone is NOT selection: with no expanded row the label is exactly `🎙️ 正在新建语音待办…`, release appends complete demo-07 at river end, still collapsed. C4 short-tap/repeat/pointercancel/Escape/blur/selection-change cancellation mutates nothing. Stable DEMO issue object/receipt and clipboard-dependent success/fallback must follow C5, no real API or fake sync.

Zero audio playback/listening waveform, raw transcript, Notes DOM/text/data, runner or extra route. Preserve full held-title wrapping, theme trust hooks, undo/reopen and child state. This is individually authored upstream stream architecture; palette/topology text is not a screenshot PASS.
