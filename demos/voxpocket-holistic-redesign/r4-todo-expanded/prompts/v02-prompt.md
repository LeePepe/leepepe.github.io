# v02 — 顶部聚焦舞台 · Top Hero Focus Stage

画廊一句话：点击待办将其抬升锁定至屏幕上方 60% 聚焦舞台并配进度环，其余待办收敛为下方紧凑可切换托盘。

## 聚焦隐喻与候选坐标

Design an editorial work table with one elevated subject: warm linen, terracotta punctuation, a generous title and a completion dial. This is `todo-expanded/v02`, the second of four round4 D candidates. Its VS-002 / CL-002 coordinates are overridden by the supplied Warm Editorial Linen & Terracotta map, AppTheme `D02.LinenFocus`; do not fall back to a generic orange dashboard. X makes the selected Todo the sole object of attention, Y allocates60% of the usable content stage to it and40% to remaining tasks, Z keeps the hero and tray solid while glass belongs to the bottom pair and transient property menus. Source decisions come from `briefs/T7-designer-d.md`, `spec.md` Section6 and `receipts/t7-d-design-contract.json`. No production or gallery code, release permission or winner freeze is part of Designer delivery.

The first paint is already a focused work session. Active screen todo_list, selected/expanded Todo demo-01, hero title `整理星桥样稿的反馈`, P0, todo, #VoxPocket #AI and 今天 18:00. Its children 收集三条反馈 / 按主题归类 / 写一段结论 start unchecked, so the dial honestly reads0/3. The compact lower tray shows the five other complete fixture records. Every tray item retains all five fields; do not replace the tray with title-only navigation chips. The hero must appear recognizably different from an inline drawer even when shown inside a small chooser card.

## 双舞台组成，不搬移节点

Compose a fixed-ratio content stage after the plain page title and before the bottom reservation. The upper region owns permanently mounted per-record hero articles; the lower region owns a scrollable ordered bank of permanently mounted compact summaries. Both presentations bind to one record, never to divergent copies. On selection exactly one hero article is visible; that record's tray summary is hidden/inert and consumes no space, so no task is visibly duplicated. Other hero articles are hidden/inert. These representations are mounted once at initialization, not cloned, reparented or rebuilt during a swap. A new Todo mounts its own pair only once when authorized creation occurs.

Each hero reads as an editorial title block beside an SVG dial, a five-value badge/editor line, a checklist and a quiet export footer. The title IS the title field, not a second repeated title badge. Status, priority, tags/areas and time complete the five-value presentation; all five remain editable inside the hero. Collapsed tray summaries keep the order status→priority→title→tags→time, with disclosure inside the title hit area. The lower40% is a compact switching tray, not three priority lanes or an additional filter toolbar. Tapping any tray title transfers visual focus to its mounted hero representation; tapping the focused title or Escape returns to a full-height tray with no expanded record.

## 60/40 几何与文字节奏

At390×844 reserve top safe clearance max(env,54px), a36px plain heading and an auto-height bottom zone. Compute S as the remaining content height after these reservations,16px dock air and the24px interstage gutter; hero gets0.60S and tray0.40S. This60/40 split excludes footer, safe areas and the separating gutter. Hero and tray have min-height:0 with separate, bounded vertical scroll wells, but the page itself never scrolls or overflows horizontally. Render title/dial first, then checklist, with exports reachable by scrolling inside the upper stage. Do not claim that all fields always fit in a fixed60vh box; at200% text scrolling is the deliberate accessibility solution.

Margins are24px, hero title30px/650/40px, checklist17px/500/26px, fields/actions15px/550/23px, captions13px/500/20px. All use local SF Pro/SF Text; create editorial character through weight and line spacing, not remote font downloads. Dial diameter68px, line5px, label tabular13px, atom spacing6px, interior padding18px, section gaps28px. Tray rows minimum92px with44px status/title targets and multiline metadata. A quiet24px open gutter separates the two planes; no bordered hero cage. At320px the dial stays visible beside a wrapping title when space permits and sits below the title at200% text. Never clamp task titles, timestamps, counts or held speech-intent text.

On1280×800 the content stage caps at1000px wide and retains the top/bottom60/40 allocation, unlike a master-inspector screen. Within the hero, title/dial occupy the left45%, checklist/editor/export the right55%; the lower tray stays one scrollable list with aligned five-field rows. Intermediate widths below760px revert to vertical hero composition without scaling the frame. Desktop titles32px, content17px, controls15px, metadata13px, targets32px minimum. These dimensions change layout only; selected IDs, check states, focus and scroll offsets survive resizing.

## Warm Editorial Linen & Terracotta palette

| Semantic token | Light value | Dark value | Used for |
|---|---|---|---|
| bg | #F7F2EA | #181411 | Entire page and footer optical backing |
| surface | #FFFDF9 | #241E19 | Hero reading plane, tray items |
| focus | #EFE7DA | #322922 | Five-field workbench and focused tray affordance |
| ink | #2B211B | #FAF2E8 | Editorial title and checklist text |
| muted | #6E5C4F | #C8B5A4 | Labels, time and ring track caption |
| accent | #9C4A24 | #F5A97F | Completion arc and selected affordances |
| statusTodo | #2B5B84 | #95C4F0 | Pending status ring/text |
| statusInprogress | #8F5612 | #F4C47C | In-progress arc/text |
| statusDone | #2D6A46 | #8CD9A7 | Completed check/text |
| priorityP0 | #B5382E | #FF9B91 | Literal P0 badge |
| priorityP1 | #8F5612 | #F4C47C | Literal P1 badge |
| priorityP2 | #6E5C4F | #C8B5A4 | Literal P2 badge |

Light mode feels like a bright warm table; dark mode steps from brown-black canvas to brighter warm solid surfaces without collapsing into black. Consume every role in actual rendered content. At least90% of the composition is neutral linen, with terracotta restricted to the selected edge/dial and functional emphasis. Give semantic pills no more than8% tint; text/strokes retain full role color and must pass4.5:1 ordinary text and3:1 meaningful boundaries after blending. Use ink, not opacity-faded gray, for done titles. The dial's pale track may be decorative, but its count text is the authoritative completion representation; do not add a redundant progress bar or large metric card.

## 进度环、聚焦交换和属性编辑

SVG dial uses a single radius27 circle in a68px viewBox, clockwise arc beginning at12 o'clock, round caps, and stroke length derived from checked children/total children. Zero children reads0/0 without NaN; an appended unchecked child increases the denominator and recalculates the arc. Its accessible label says `已完成 N / 共 M 步`; child checks update it immediately, while parent status remains an independent user choice. Custom status rings use empty/partial/check shapes. No automatic parent completion, no delete-on-check animation and no array replacement disguised as progress refresh.

The focus exchange is a340ms upward cross-slide, outgoing hero opacity120ms and incoming translateY18px→0 over280ms, spring response0.34/damping0.95. Animate each record's already-mounted visual plane; no motion clone, DOM move or shared title portal. Give the target hero a visible focus outline and move keyboard focus to its title after a keyboard-initiated swap; pointer selection need not steal focus. Collapse restores the initiating tray title and stored tray scroll. Reduced Motion suppresses lift and dial drawing, reallocates regions immediately, and fades within80ms. Selection changes first cancel a capture, so a held session cannot be redirected to the next hero.

A title input, status menu, priority menu, maximum-three tag slots and time input live in the hero workbench. Invalid title/time edits preserve the previous accepted value and explain the issue locally. A fourth tag attempt leaves existing tags unchanged with `最多 3 个标签`. Completing a parent offers a five-second Undo in its mounted feedback line: hero feedback when selected, or a separate tray-row slot outside the five summary fields when collapsed. Only the visible presentation exposes the Undo control. Undo/reopen leaves independently checked children intact; later parent edits invalidate older undo snapshots/timers. Menus close on Escape and restore their initiating control; all inactive hero controls are inert and absent from the tab sequence.

## 两枚液态玻璃底键及 Recorder 双画布

Keep the footer radically simple: a56px round-square page-switch button at bottom-left and a min64px recording capsule at bottom-right, separated by16px. Footer padding24px horizontally and max(env(bottom safe inset),34px) vertically. Exactly two bottom-bar buttons; show no third cancel button, no tabs, no top segmented controls and no page-level settings action. Full holding labels wrap within the right button; its height growth reduces S and recomputes60/40 instead of occluding the tray. Maintain16px clearance and scroll-padding above the footer. Desktop keeps this bounded content-attached accessory, not a native macOS tab/navigation bar.

For both keys specify blur20px/saturate145%, surface tint0.34 light/0.50 dark, Fresnel top highlight0.62/0.18, side rim0.14/0.10 and shadow0/7/22px ink0.10/0.26. Restrict optional Chromium refraction to background edges with displacement1.2px/chromatic offset0.25px; WebKit drops displacement and uses equal prefixed/unprefixed blur/saturation. Their solid canvas backing is separate from the opaque hero, and no glass samples glass. Without backdrop support or with Reduce Transparency use surface-filled shapes; the icon/text plane is never blurred. Glass is an HTML approximation, not native API certification.

The left key announces `切至录音页` on Todo and `返回待办` on Recorder. Translate the permanent pair of canvases horizontally for300ms; a60px horizontal intent gesture on unused stage performs the same move, but scrolling, ring clicks and press-holds do not. Before leaving Todo remember its expanded record, cancel recording, and clear visible expandedId; Recorder has only a sparse `录音` sentence stage and the same bottom keys. Returning recovers the prior hero and scroll, unless Todo had been deliberately collapsed. Offscreen content stays mounted/inert. Recorder does not expose a waveform/transcript or settings/history destination, and is not a redesign of the frozen native recorder. Its no-visible-selection capture creates a Todo instead of targeting the hidden hero.

## 录音补充与导出后果

On initial press show the exact full-title intent `🎙️ 正在继续补充至：<当前 Todo Title>` if the hero is expanded; otherwise display `🎙️ 按住新建语音待办…`. Arm after180ms and transact once on valid pointerup/Space keyup. A focused append adds `确认结论与反馈主题对应` to that captured ID, preserves five fields and earlier checks, keeps hero open, and reports one added step. With no expansion create demo-07's declared five fields and children, then use sequential IDs for later creations; keep each new Todo collapsed in the tray. No preview/Apply stage, no extra parent duplication and no clipboard or network side effect from recording.

Short presses, keyboard repeats, pointer cancellation/leaving the valid target, abnormal lostpointercapture, Escape, focus loss, pagehide, page/record switch and property editing cancel the token before any mutation. Release-generated click is consumed; expected capture loss after commit cannot trigger a second result. In-place capture is local synthetic fixture interaction, never a microphone permission prompt. Timing stays unchanged with accessibility motion preferences.

Export buttons occupy the hero detail footer and read `一键转 Linear Issue` / `复制 Markdown`. A current snapshot carries only the five fields and checked sub-tasks. Generate deterministic local DEMO-001 for demo-01 and corresponding ordinal IDs for others, presenting `演示：已生成 Linear Issue · DEMO-001（未联网）` alongside a selectable structured object preview. Re-export must reuse the ID. Markdown heading/Status/Priority/Tags/Time and task lines reflect current edits. Actual clipboard success alone permits `已复制 Markdown（演示数据）`; denied/unavailable clipboard reveals selectable output with `未复制：请选中文本后复制`. No real Linear URL, account synchronization or invented successful service receipt.

## Writer 必须兑现的身份与质量门禁

Draw inline SVG at24×24 using currentColor/stroke1.8/round joins: the dial is the sole aggregate visualization, status uses a9px-radius ring, children use circular role=checkbox buttons, focus-collapse a small upward chevron, page-switch two opposing arrows, microphone a static outline, Copy overlapping rounded outlines, Linear a diagonal line motif. Labels include full task context; decorative SVGs are aria-hidden. Use44px mobile/32px desktop targets,2px focus rings with3px offset, Enter/Space title selection, Escape nearest layer and polite announcements. No external icons/fonts and no raw square checkbox.

Observe root mutation records over expand/collapse/hero switch/status-child check/page slide plus settlement and two frames: removedElements = 0, unchanged object/node identities, no reparenting or conditional remounting. Existing text must update through persistent Text nodes, not element textContent replacement. Store export, feedback and editor slots from initialization. Verify the focused0/3 initial hero, tray swap to demo-02, collapse/new, append/dial denominator, navigation restoration, abort paths, clipboard success/fallback, root/body appearance parity, short heights,320px and200% text. Preserve page-config and query theme=light|dark/platform=mobile|desktop|macos; only a trusted parent with allowed origin/source and valid enums may change appearance/platform. The external chooser owns all bezel, SELECT/STAR/NOTES and the escaped one-sentence card summary.

Exclude playback/listening waveform bars, original/AI transcript comparison, Notes/备注/笔记 data or textarea, runner/detail/history routes, top/bottom utility clutter, caustic-veil stripes, Active/Matte/debug rulers and copied drawer/tree/sheet CSS. All four D pages require six actual CSS rule and selector Jaccard comparisons≤35%, not just renamed classes or distinct roots. Prompt-stage PASS proves neither a browser screenshot nor a native implementation.
