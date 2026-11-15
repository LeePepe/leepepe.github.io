# v03 — 翡翠行动矩阵 · #VoxPocket / #AI / #iOS Swimlane Matrix + Action Tree

画廊一句话：三条真实领域泳道归置待办，预览先露下一枝，点击在原任务下展开可勾选行动树。

## Three areas, one identity per task
Current B5 has exactly four candidates; v03 combines an area matrix with a record-owned action tree. Use `briefs/T6-design-c.md` C1–C7/fixture and `spec.md` Section 5.5 as relative authorities. Its exact mirror is `r3-dual-todo/prompts/v03-prompt.md`. Historical root-only v03 is superseded; no new research or theme freeze.

VS-007 / CL-008 alignment is remixed with CL-003's precision, but LIGHT is jade and DARK is lifted indigo, not another blue stream. X focuses demo-01 in #VoxPocket only once; Y changes visible area on mobile and opens a task-to-child tree inside that lane; Z is solid task content with glass solely on capture. Lanes are actual #VoxPocket / #AI / #iOS associations, not renamed status boards. The first recognized tag is primary area; extra tags stay in the row, no cross-lane duplicate. Unknown tags use a reachable 未分类 recovery band, not a fourth fake project.

## Matrix and branching content architecture
Header precedes a local area selector and main matrix. The matrix contains persistent lane-heading/group regions and one bank of record articles; each article owns five-field root header, a short preview-branch slot, and a growing action-branch region. That region owns a nested ordered list of real AI child check-buttons followed by its own editor fieldset and export/receipt section. A child is NOT another Todo or runner stage; never invent extra dependencies to fill the tree.

Use a single shared CSS grid for all lane headings and article placement. Primary-area association determines each article's lane column and vertical order, with accessible heading association matching the visible group. Initially #VoxPocket contains demo-01/05, #AI demo-02/04, #iOS demo-03/06. Mobile selector changes lane visibility, not route; desktop shows all three columns. This matrix stylesheet is independently authored: group grid + persistent record bank + nested branch tracks, not a card-board template. On tag edit preserve open article allocation until collapse settles; then update grid membership/heading association without remove/reappend/reparent. Physical grid allocation and computed positions must prove real area grouping, not decorative headings over one list.

Root summaries always display status todo/inprogress/done, priority P0/P1/P2, full title, <=3 tag/area pills and time. Primary area remains one of those tags, never a sixth field. Initial active mobile area #VoxPocket; all task drawers closed. Area change cancels capture, collapses old expanded row with stable nodes, moves focus to surviving selector, then changes visible grid allocation. Preview alone does not choose an expanded record.

## Measured lane and branch geometry
390×844: side inset18px (354px matrix), native44px header following max(top safe inset,54px). Area selector is a three-part local text control with each target>=44px, each label wraps rather than running into another. Selector height auto/min44px, gap24px into active lane; inactive heading controls remain reachable. Root summary min128px, padding16px, row air16px, atom gap6px. Status44px at leading edge; priority alongside title; tags/time below, stack at<=350px. Action tree indent24px,1px solid guide with12px elbows in empty gutter, child rows>=56px; reduce indent to12px at320px/200% before squeezing text. Guide stops at last child, never crosses labels or resembles a waveform/ruler.

Desktop1280×800: >=1040px matrix max1120px, three fluid columns (about357px) separated24px; lane heading/record starts share the same grid lines. Each branch grows DOWN inside its lane, not sideways into a global inspector. Editor controls use two columns only if each target/label fits, otherwise stack. Under1040px use the one-active-lane mode rather than narrow three columns. Main is one vertical scroll well; no lane-internal wheel scroll, no page horizontal scrollbar. Capture footer width available minus36px mobile /max680px desktop, readable body>=72px with16px padding, auto-height,16px air and max(bottom safe inset,34px). Expanded branch and long held title reallocate main height; scroll-padding16px, all content bounds above capture reservation.

## Jade/indigo :root contract
All role hex values must be consumed by computed styles on named regions. LIGHT lane backdrop is jade-neutral, active roots and branches approach white; DARK root and branch planes lift above indigo. Unselected lane records use surface; selected root/branch/preview backing use focus, root canvas/footer backing bg. Content is opaque.

| Role | LIGHT | DARK | Functional paint |
|---|---|---|---|
| bg | #EDF6F2 | #151C33 | Matrix canvas and solid footer backing |
| surface | #F6FCF9 | #202C45 | Ordinary lane roots and opaque glass fallback |
| focus | #FFFFFF | #2D3E59 | Selected root, branch and preview slot |
| ink | #183D35 | #F1F7FF | Root/leaf titles and action text |
| muted | #486D63 | #BBCCE2 | Area/time/tag labels and secondary actions |
| accent | #006F58 | #80E0C6 | Active area underline and keyboard focus |
| statusTodo | #28638D | #AFD5FF | Blue pending ring and 待处理 label |
| statusInprogress | #88530D | #F6CA82 | Amber progress arc and 进行中 label |
| statusDone | #166A49 | #97E0BA | Green check and 已完成 label |
| priorityP0 | #AA3A43 | #FFA7B4 | Red P0 label/control stroke |
| priorityP1 | #88530D | #F6CA82 | Amber P1 label/control stroke |
| priorityP2 | #486D63 | #BBCCE2 | Muted P2 label/control stroke |

Separate state and priority colors plus literal labels are mandatory; green accent is NOT every state. Solid strokes/text use exact tokens, optional tint<=8% cannot stand in for them. Ordinary and semantic text>=4.5:1 on bg/surface/focus, boundaries>=3:1; do not dim done child/parent text below AA. Native SF stack: mobile focal24/650/33, root/leaf17/500/26, selector17/600/26, meta13/500/19; desktop focal26/650/36, root/leaf15/500/24, control13/550/20, meta12/500/18. Max four sizes, tabular time and natural CJK wrapping, root-relative scaling; no truncation or imported typeface.

## A preview branch, not a tooltip-only promise
Each root pre-mounts a noninteractive preview branch beneath title metadata. It reads `剩余 N / 共 M 步 · 下一步：<首个未勾选项>` or `共 M 步 · 子任务已完成`; child counts are derived, not an extra always-visible column. Mouse entering title/preview affordance for160ms reveals the small branch; early leave cancels, leaving entire article100ms hides. Focus on title or 预览任务 button reveals immediately, blur outside/Escape hides; title Enter/Space expands directly. Touch uses a separate>=44px preview affordance inside the title field: first tap toggles snippet, second/outside tap/scroll dismisses; first tap on title still opens the full action tree. Touch-generated hover is ignored. Switching preview/article/area cancels stale timers, no frozen snippet from previous lane. Expanded tree hides its preview. None of these previews mutates task data or expanded ID; counts/next step refresh using the same mounted nodes after checks. Zero removals on preview/expand/collapse/switch/check across lane changes.

## Tree spring and restrained optical footer
Nested branch container expands measured height/0fr→1fr with response .38s/damping .86; guide reveal<=160ms, check stroke120ms. No external graph library or dependency. Reduce Motion instantly allocates branch/grid, no connector draw/translation/bounce, <=80ms opacity; capture semantics unchanged. Capsule radius26/blur26px/saturate180%, LIGHT white .28 / DARK #3A5475 .40 tint over solid bg backing, top Fresnel .72/rim .24, shadow0/10/30px indigo .15. Optional Chromium edge displacement<=2px on backdrop only; WebKit uses clean prefixed blur/saturate without displacement. Reduce Transparency is opaque surface with solid rim. No glass roots/tree text or sampling glass from glass.

Use currentColor24px SVG circle radius9/stroke1.7, empty/partial/check state plus localized label. Each leaf is independently checkable with role=checkbox/aria-checked; no raw square inputs. Hit targets>=44px touch/>=28px desktop, visible2px focus/3px offset, keyboard selector arrows and title focus return. All field controls and tags<=3/time validation follow C2. Expanded actions are 一键转 Linear Issue and 复制 Markdown: current five fields and checked children produce the C5 synthetic DEMO object/receipt and actual clipboard result or mounted selectable fallback.

## Required lane witnesses
Collapsed mobile shows #VoxPocket's two complete rows; other lane selectors reveal their actual records, desktop simultaneously shows all six once. Preview demo-01 grows one read-only next-step branch. Expanded demo-01 exposes three existing checkable child leaves plus live status/priority/tag/time and export controls under that root. Preserve article/child/editor identities, removedElements=0 and no reparenting for every preview/open/close/switch/check interval.

For held capture, exact `🎙️ 正在继续补充至：<当前 Todo Title>` uses full expanded title; release adds `检查反馈结论是否对应主题` once to THAT ID, never the active area's first task. Without expansion, including preview-only, exact `🎙️ 正在新建语音待办…` release creates full demo-07 in its declared #AI primary lane, collapsed; reveal and scroll there above footer after safe cancellation/settle. Escape/pointercancel/blur/selection change invalidate the session with no children/parents added. Synthetic DEMO export/actual clipboard fallback follow C5, no private account or backend claim.

Ban Notes, raw transcript, playback/listening waveform, runner/action execution rail, fake routes and decorative rail/ruler/zebra effects. Preserve legitimate outer chooser controls, shared fixture fidelity, completion/Undo, theme trust and long-title dock clearance. Matrix/tree prose is an upstream obligation, not rendered topology proof.
