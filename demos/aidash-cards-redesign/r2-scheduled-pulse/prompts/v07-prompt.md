# v07 — 脉冲坐标纸 · Evidence matrix

Status: Designer-approved R2 Stage 2 specification for a semantic status matrix; no starter topology is being reused.
Target: desktop/macOS 1280×800, card-sized evidence view with no additional app pages.
Coordinates: VS-007 / CL-006 / X:job-by-evidence-grid / Y:cell-replacement / Z:solid-grid-paper / AppTheme:R2EvidenceMatrix.

## Visual metaphor
A coordinate sheet answers which job, what cadence and what result through one aligned matrix. Center a 1080×568 surface at (100,116), radius 24, padding 24. Its 1032×36 header precedes 20px air and a 1032×464 matrix. Three shared column tracks are 248px title, 176px cadence and 560px outcome, separated by two 24px gutters. Column labels consume 32px; four ordinary records are 52px high, the active digest record 176px high, with four 12px record gaps. Use 34/19/15/13px SF Pro, tabular digits and 16px cell inset. The selected cell receives a gentle 0 3px 12px shadow at 4% Light / 20% Dark; there are no full cell borders.

## Single P0 focal point
Only the digest result cell displays 5/5 in 34px with 阶段通过. Its source row owns 个人数仓晨报 and 每日 04:00; do not restate them in a hero above the matrix. Within the same cell place its small 04:01 completion and one 立即运行 button. A five-check mini trace encodes the passed digest stages, not historical runs or overall uptime. All other result values use 15px text and a single state mark.

## P1/P2 folding
Matrix rows retain the inventory order: Linear @bot 桥接 / 每 1 分钟; 我的 PR / 每 5 分钟; PR 自动审查 / 每 5 分钟; 个人数仓晨报 / 每日 04:00; 每日学习推荐 / 每日 04:15. Clicking any row chooses it and transfers the large outcome cell, reducing the old row to 52px. The digest cell's 阶段详情 replaces its large outcome and mini trace with a compact three-row sequence of ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题 and ⑤ Brief 投递; use two labelled stages on the first two lines and the last alone. 查看回执 uses the same cell body. Learning's cell holds 每日 3 题直投 Linear and 已投递 3 题, with no route copied from digest.

## Color and surface polarity
Matrix role colors Light / Dark: canvas #F1F4F7 / #101821; paper #FFFFFF / #1D2936; focal-cell #EDF2FA / #2A3A50; text #202D40 / #F0F6FF; label #566A81 / #B8CCE4; selection #344F91 / #AAC9FF; button-label #FFFFFF / #1C3152; passed #286D4F / #93E1B5; failed #B0394C / #FFB8C6; keyboard #3A62B0 / #C0D8FF. Grid headings use the label token; numeric outcomes get text. Completion icons pair green with 通过 or 完成. Neutral background steps delineate one selected cell; never saturate an entire row or create a heatmap color legend without a numeric denominator.

## Liquid Glass optical parameters
The matrix is deliberately solid because aligned values must not move optically across shared columns. Refraction and blur are both 0px; saturation is native 100%. A 16px focal-cell radius and 24px parent radius supply nesting without glass. Evidence replacement is also opaque, so WebKit and reduced-transparency paths have no alternate coordinate geometry. The matrix is not a shader showcase: eliminate specular sweeps and luminous borders that would suggest live signal amplitude.

## Inline SVG iconography
Use a 24×24 three-column matrix icon with only its center crossing emphasized, 1.65px currentColor rounded strokes. Each outcome has a clock, check or open running arc with a textual status. The digest's five-notch figure has an accessible value of 5/5 阶段通过 and no second legend below it. Make each choose target cover its 248×52 title cell, not just the tiny icon; cell disclosure controls are at least 32×32, and 立即运行 is 112×36. Outline keyboard focus around the title control and separately around the action.

## Explicit anti-patterns
Reject faux heat intensity, fake historical sample columns, repeated selected-row names and a twelve-tile dashboard. Grid labels and records must share the exact three track widths; never independently size headers and rows. Do not replace full Chinese stage names with clipped tokens or lower font size to fit. No generic gray 1px cage, script console, raw job ID, state-selector dropdown, ruler or glass-covered result cell is allowed. Due times are not failures.

## Interaction and states
Use the shared 04:15 snapshot from ../../domain.md and initialize aidata-digest as the expanded row. Ordinary outcomes are their factual latest successes; learning retains three delivered questions. Pointer selection or Enter on a title transfers the one expanded cell without changing inventory order. Use roving keyboard focus: Up/Down moves among title buttons; Enter selects, and Tab then reaches the selected cell's actions. The receipt and stage views are alternative cell contents; Escape returns to the large outcome. Starting a run updates the selected record in that cell through 已排队, 运行中 and 刚刚完成 · 耗时 14s. Keep the other rows selectable while busy, but never attach the old operation to the new cell owner. Missing evidence appears as 暂无回执 in the result cell; 运行失败 retains 立即运行 recovery. Under Reduce Motion perform a discrete row-height replacement and leave all column coordinates fixed.

## Stage 2 handoff
Build main.topology-job-evidence-matrix with a direct section.content whose children are header and div[role=grid:evidence-matrix]. The grid contains div[row:column-labels] and five div[row:job-record]; every job-record has div[rowheader] parenting a choose button, div[gridcell:cadence] parenting time, and div[gridcell:result] parenting output, figure, div[replacement-detail] and div[actions]. Do not approximate this role-parented shape with the register's ul/li tree. Validate exactly one job-name occurrence per row, one active result cell, shared track boundaries, digest's full five stages and learning's three-question result. Screenshot the disclosure at 1280×800 and verify no horizontal overflow in either appearance; rendered matrix semantics and pixels remain a downstream acceptance responsibility.
