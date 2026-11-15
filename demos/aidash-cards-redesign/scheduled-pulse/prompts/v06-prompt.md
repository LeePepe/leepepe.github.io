# v06 — 胶囊节拍器 · Capsule spine

Status: Designer-approved Stage 2 R2 capsule-spine design, with its own selection and disclosure geometry.
Target: desktop/macOS 1280×800; outer chooser supplies the window and appearance controls.
Coordinates: VS-003 / CL-003 / X:cadence-capsule-spine / Y:shared-definition-well / Z:single-action-lens / AppTheme:R2CapsuleSpine.

## Visual metaphor
A horizontal spine holds five job capsules; one definition hangs below its selected capsule like a precise annotation. Locate the 1120×500 card at (80,150), radius 28 and 24px padding. Below a 40px heading and 24px gap, a 1072×88 spine uses widths 210/180/196/220/218 with four 12px gaps, so all labels fit without a scroller. A 24px breathing interval separates it from a 1072×276 shared definition well. Inside the well, a 416px readout, 32px gap and 576px detail body fill the 24px inset. Use 40px schedule time, 20px heading, 15px labels and 13px evidence. The parent has a 0 8px 28px shadow at 8% Light / 30% Dark, with capsules relying on luminance rather than individual shadows.

## Single P0 focal point
Linear @bot 桥接 starts selected; 04:15 is the sole 40px due-time reading beneath the spine. Show 到点了 and the factual latest success 04:14 in small type. The capsule owns the job title and 每 1 分钟 cadence; the annotation never repeats that title. An active capsule gets one solid cyan underline, not a dancing waveform. The readout communicates next scheduled time, not unobserved service freshness or failure.

## P1/P2 folding
The spine's other capsules read 我的 PR with 每 5 分钟, PR 自动审查 with 每 5 分钟, 个人数仓晨报 with 每日 04:00, and 每日学习推荐 with 每日 04:15. The bottom well exposes summary first; 查看回执 exchanges the right-hand body for that job's receipt. Digest selection changes the left reading from due time to 5/5 阶段通过 with 04:01 完成. Only digest selection makes 阶段详情 available, opening a two-column ordered route in the right-hand body: ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题, ⑤ Brief 投递. The fifth stage occupies a full-width last line. Learning selection instead reads 每日 3 题直投 Linear and its delivered-three result. Never add a second selected capsule or another inspector row below the well.

## Color and surface polarity
Token pairs Light / Dark: page #EDF5F8 / #0C181E; spine-card #FFFFFF / #192B34; active-capsule #E3F0F5 / #29424F; well #F4F8FA / #21353F; main-ink #17313D / #EDF8FD; quiet-ink #526C79 / #B6D0DC; primary #145E7C / #9BDAF2; primary-ink #FFFFFF / #143140; positive #2B6C50 / #99E0BA; negative #AA3C50 / #FFB7C5; focus #216E96 / #C1EBFF. All capsule fills are neutral except the selected one. Use positive text with a check glyph for completed work; cyan belongs to selection, not health. Reserve the deepest text contrast for the due-time readout and run action.

## Liquid Glass optical parameters
A single 116×36 立即运行 lens attaches to the readout's trailing edge, not to the card bottom. Its radius is 18px, tint 90% of the well token, blur 6px, saturation 118%, bevel 4px and refraction limited to 1.5px with no channel dispersion. Sample only the solid well under this one functional control. For Safari, inactive window or reduced transparency, use an opaque primary-colored button with primary-ink and a 6% Light / 24% Dark soft shadow. Never spread this lens material across the capsules or their connecting spine.

## Inline SVG iconography
The card mark is a 24×24 line with five discrete attached ticks, 1.6px round-capped currentColor. Use one hollow clock for due and a check circle for complete; status meaning is carried by text beside each glyph. In digest mode the route has five check notches but no imaginary minute trend. Capsule glyphs fit a 24px square with 6px name separation; each 88px-high capsule is keyboard-selectable with a 3px focus outline. The action lens has a 24×24 play arrow and the visible 立即运行 label.

## Explicit anti-patterns
Do not turn the spine into an unbounded horizontal carousel or five floating glass pills. A tiny underscore is not a sufficiently accessible selection state without aria-pressed. Avoid repeating the bridge name in the large annotation, mixing daily and minute jobs on a linear duration scale, or adding a fabricated heartbeat trace. Prohibit any debug material toggle, preview-only state menu, striped blur layer and bottom floating toolbar. No setting to change job cadence is part of this design.

## Interaction and states
Start with linear-bot-bridge due at 04:15, using ../../domain.md's latest success rather than a new fabricated run. Capsule selection updates a single definition slot; its tab order follows the visible left-to-right spine. Digest opens its stage route in place and learning gives the three-question outcome. Escape reverses receipt or stage disclosure to summary without clearing capsule selection. Run feedback changes the readout from due time to 已排队, then 运行中, then 刚刚完成 · 耗时 14s; keep the capsule's title stationary. A second activation while pending is ignored and visibly disabled. Updates arriving after another capsule is selected belong to the original job record. 暂无回执 replaces missing evidence in the well, while 运行失败 retains a retry path through 立即运行. Reduce Motion keeps the underline stationary and substitutes states without sliding the well.

## Stage 2 handoff
Require main.topology-capsule-definition → direct section.content with header and dl[capsule-spine]. Five div[definition-item] children of dl each parent dt[button:choose-job] and dd[definition-body]. The selected dd occupies the measured shared well; its children are section[readout] with output and button, plus section[detail-slot] with details and dl[evidence]. Unselected dd elements are hidden, not duplicated elsewhere. Assertions must cover full five-name visibility within 1072px, single selected definition, digest-only stage disclosure, and completion feedback inside the originating record. Inspect Light and Dark screenshots with the action fallback, ensuring the 04:15 reading and 13px schedule copy retain contrast. This capsule/definition hierarchy is not a list cloned from another prompt.
