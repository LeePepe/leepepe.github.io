# v02 — 节律站台 · Cadence rail

Status: Designer-approved Stage 2 direction for the new R2 rail; awaiting comparative Owner selection.
Target: desktop/macOS at 1280×800, Scheduled Pulse card rather than an application navigation screen.
Coordinates: VS-007 / CL-003 / X:temporal-lanes / Y:attached-station-fold / Z:rail-action-popover / AppTheme:R2CadenceRail.

## Visual metaphor
Treat recurring work like a compact station timetable without inventing travel destinations. A 1080×604 surface begins at (100,98); use 24px corner curvature and 28px interior padding. Below a 48px title row and 24px separation, a 1024×476 temporal diagram contains a 392×476 frequent-work lane, a 28px breathing gutter and a 604×476 daily-work lane. Each lane is an ordered sequence, not a table with headers. A narrow vertical cadence rail joins only the frequent jobs; the daily entries attach to their own labelled 04:00 and 04:15 markers. Type is 36px focal time, 19px title, 15px controls and 13px schedule copy. Station padding is 16px against 8px internal spacing.

## Single P0 focal point
The due 我的 PR station is the only expanded stop. Its 04:15 time is the 36px anchor with the factual state 待运行; latest success remains 04:10. Treat the cadence as due timing, not a claim of failure. Place the 立即运行 affordance within this stop's 344×148 expansion; it must not be mirrored in a global toolbar. Other station times retreat to 13px.

## P1/P2 folding
Arrange the left lane as Linear @bot 桥接 · 每 1 分钟, 我的 PR · 每 5 分钟, PR 自动审查 · 每 5 分钟. The right lane has 个人数仓晨报 · 每日 04:00 followed by 每日学习推荐 · 每日 04:15. A selected stop grows a daughter details region below its existing title, while the formerly selected stop folds to a 64px line. Digest expansion owns a horizontal five-stop path labelled ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题, ⑤ Brief 投递; its wrapped two-line labels are still fully visible. Learning expands to 已投递 3 题 and 每日 3 题直投 Linear, not this path. Evidence is a station-local popover reached through 查看回执. Escape dismisses it without moving the schedule.

## Color and surface polarity
Use Light / Dark tokens: canvas #EDF4F7 / #0D171D; station-surface #FFFFFF / #18272F; selected-stop #E6F3F6 / #213B46; primary-ink #16303B / #E8F7FC; secondary-ink #506873 / #AEC8D2; action #16657A / #87D8EB; action-ink #FFFFFF / #102C37; pass #236B50 / #8BDDB8; failure #AF3949 / #FFB3BF; keyboard-ring #126B91 / #A3E4FF. Neutral lanes remain borderless. Cyan appears on the due station's time pin and action; connecting rails use secondary ink at 22% alpha and have no status semantics. A checkmarked green pin denotes completed evidence, not route ownership.

## Liquid Glass optical parameters
Only the 320×180 receipt popover may use glass; its radius is 18, nominal blur 10px, saturation 112%, refractive displacement at most 2px, zero chromatic fringe and a 1px top rim at 18% white. It samples the solid station lane, never another overlay. Text sits on an 88% opaque surface tint. Safari receives a completely opaque station-surface popover with the same 0 12px 32px shadow at 12% Light / 32% Dark; Reduce Transparency chooses this path too. The vertical rails and station bodies themselves have no optical filters.

## Inline SVG iconography
Draw a 24×24 schedule glyph with three differently spaced ticks, using 1.6px round-cap strokes. Each station has an explicit check, clock or rotating open arc matched to its state. The daily path uses small numbered stage pins, never generic 1..5 placeholder copy. Put any tiny pin inside its parent 344×64 or 556×64 button, so the diagram's visible geometry does not shrink the hit area. Receipt controls use an outlined document glyph with a readable 查看回执 label.

## Explicit anti-patterns
Do not build a chronological history library or a misleading minute-scale plot that compresses daily and one-minute intervals onto a single axis. Cadence lanes are categorical schedules, not measured latency traces. Ban invented train names, extra destination screens and shared fixed-width table headers. No disclaimer text, internal state dropdown, zebra overlay or Active/Matte bar belongs to this surface. Retain readable Chinese stage labels instead of rotating them vertically.

## Interaction and states
At the domain clock, focus my-pr-supervisor and derive its due pin from the 04:10 success plus the five-minute cadence. Bridge and auto-review are also due by 04:15 but remain subordinate; morning digest is completed 04:01 and learning is completed 04:15. Selecting the daily digest transfers the expanded stop to the right lane; the 我的 PR name stays only in its folded original station. Open a stage to see its source-backed passed state, or open the receipt for the selected job's latest completion. Running immediately replaces the selected station pin with 已排队, then 运行中, then a check and 刚刚完成 · 耗时 14s. Keep a busy station identifiable if selection changes; its update belongs to that stop, not the newly selected one. An unavailable receipt reads 暂无回执 in the popover. Failure recovery uses the same job's 立即运行 button. Disable translation of the rail under Reduce Motion.

## Stage 2 handoff
Use main.topology-cadence-stations with a direct section.content whose children are header and figure[temporal-diagram]. The figure parents a visually hidden accessible figcaption and two section[lane] siblings; each lane parents a heading and ol, each li contains a button and one hidden-or-expanded div[station-detail]. This nested figure/section/ordered-stop structure must remain distinct from a bento field. Required assertions: all five labels are visible once before and after station changes; opening digest exposes the exact five route labels; the two daily cadences never inherit five-minute timing; the receipt popover stays bounded inside the 1280×800 frame; the active due time is not styled as a red error. Read ../../domain.md for source IDs and shared execution limits, and preserve the station identity throughout run feedback.
