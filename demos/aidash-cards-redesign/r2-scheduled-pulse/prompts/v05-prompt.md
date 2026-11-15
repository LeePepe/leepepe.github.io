# v05 — 快慢双页 · Two-speed workbench

Status: Designer-approved new R2 Stage 2 composition; the two-speed split is a card lens, not new product screens.
Target: desktop/macOS 1280×800, one Scheduled Pulse parent surface.
Coordinates: VS-007 / CL-002 / X:fast-versus-daily / Y:owned-inline-well / Z:receipt-lid-only / AppTheme:R2TwoSpeedBench.

## Visual metaphor
A wide workbench separates minute cadence from morning cadence so different clocks stop competing. The 1104×576 card starts at (88,112), with 28px radius and 24px padding. After a 1056×44 title strip and 20px gap, two benches occupy 1056×464: a 424px frequent bench, 24px aisle and 608px daily bench. The frequent bench has three 88px records with 12px gaps and one 164px owned expansion below the selected record; daily work initially uses two stacked 608×220 horizontal records with a 24px gap. When a daily record is selected, allocate it 364px height, the other record 88px, and their gap 12px; the bench remains exactly 464px high. This is two groups inside one surface. Use SF Pro 32/20/15/13px, 6px within labels, 20px within benches and a restrained 8% Light / 28% Dark parent shadow.

## Single P0 focal point
PR 自动审查 owns the focused result well in the frequent bench: 04:10 完成 at 32px with the exact 每 5 分钟 cadence beside its original title. It is the only item with the primary 立即运行 control. The well begins directly below that record; use 最新回执 as its heading, never repeat the job name. The daily bench remains visibly useful but its 5/5 and 3 题 indicators are small 15px companions, not competing hero metrics.

## P1/P2 folding
Fast records are Linear @bot 桥接 · 每 1 分钟, 我的 PR · 每 5 分钟 and PR 自动审查 · 每 5 分钟; slow records are 个人数仓晨报 · 每日 04:00 and 每日学习推荐 · 每日 04:15. Every title sits only in its record header. Selection moves the single owned well to the chosen record, across the aisle if needed, and folds the old one before opening the new one. Digest's well first contains a 5/5 summary figure; 阶段详情 replaces that figure rather than retaining it above the route, and reveals ① 个人源采集 / ② L2-L3 入仓 / ③ Retro-ROI / ④ 学习寻题 / ⑤ Brief 投递 as a three-plus-two arrangement. Learning's well instead exposes 每日 3 题直投 Linear and 04:15 完成. 查看回执 toggles a lid over the same well, not a third permanent pane.

## Color and surface polarity
Light / Dark roles: desk #F4F1EB / #111A17; card #FFFEFA / #1C2923; fast-well #ECF2ED / #2A3B31; daily-inset #F7F3EA / #24302A; ink #25352B / #F0F5ED; secondary #5D6B60 / #B9CBBB; accent #31694E / #A4DAB8; on-accent #FFFFFF / #183A27; success #276B48 / #94DFB3; failure #A63A48 / #FFB1BE; focus #3C7457 / #B9EDC9. Tempo groups are distinguished by spacing and headings, not red/green category fills. A thin warm seam divides the benches; forest accent belongs only to the selected record and run control. No brass decoration is needed to justify the paper palette.

## Liquid Glass optical parameters
The receipt lid alone may be a 340×164 functional popover with radius 16, blur 8px, tint opacity 92%, saturation 105%, 1px displacement cap and no spectral channel split. Its shadow is 0 8px 24px at 11% Light / 30% Dark. It samples the opaque result well and is not layered above another glass item. In Safari or Reduce Transparency use the card token at full opacity and omit all backdrop filters. Benches and record tiles remain solid; don't interpret a workbench as frosted acrylic.

## Inline SVG iconography
A 24×24 split-clock glyph uses two open clock halves, 1.7px rounded strokes; it communicates cadence contrast without claiming comparative performance. Fast rows use a clock/check state glyph, while daily rows use a tray or open-book glyph with labelled outcome. Digest's route is five small connected checkpoints inside its well; each is a selectable 32×32 target with its complete two-line label beside it. Buttons should never require clicking a 6px status dot to reach the record.

## Explicit anti-patterns
The split must not invent fast/slow service SLAs, add latency charts or claim one group is less reliable. Reject equal-sized panels with mirrored copies of the selected job. Neither bench is an app sidebar or a separate detail page. Do not leave an empty inspector permanently reserving a third column. Avoid nested content glass, global run buttons, rainbow status chips and any internal test-state switch. Keep complete names and values even if evidence wraps.

## Interaction and states
Initialize pr-auto-review selected with its known 04:10 success, and other records from ../../domain.md at 04:15. A single selection token moves the result well when the morning digest is clicked; the review record's title remains once in the folded fast stack. Its five stage checkpoints expand inside the daily row footprint, with no stage durations invented. Choosing learning replaces that route with the delivered-three result. Activating 立即运行 locks the target record through 已排队 and 运行中, then updates its well to 刚刚完成 · 耗时 14s. Selecting another record during that operation does not redirect the callback. Receipt absence produces 暂无回执 under the selected record; failure recovery returns the same run control with 运行失败. Escape closes the receipt lid before changing selection; Reduce Motion eliminates well travel across the aisle.

## Stage 2 handoff
main.topology-two-speed-bench contains one direct section.content; its direct children are header and div[group:tempo-bench]. The tempo-bench has section[frequent] and section[daily]; frequent parents h2 and div[record-stack] with three article children, daily parents h2 and div[daily-pair] with two article children. Every article contains header, button[choose] and div[owned-well]; only the selected well is visible. Inside a well use figure[outcome], details[stages] and div[actions]. Preserve this nested bench/stack/pair topology rather than transplanting the accordion candidate. Verify the five exact labels and cadences at launch, one expanded well at every click step, digest stages reachable, and learning fixed to three questions. Screenshot both tempo groups without clipping, then hand actual rendered topology and copy validation to Stage 2.
