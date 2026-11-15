# v04 — 行内展开页 · Quiet hinged register

Status: Designer-approved Stage 2 handoff; R2 compact-register proposal authored independently from the other nine.
Target: desktop/macOS, exact 1280×800 viewing area with external gallery chrome.
Coordinates: VS-005 / CL-006 / X:single-row-ownership / Y:one-active-accordion / Z:flat-paper-hinge / AppTheme:R2HingedRegister.

## Visual metaphor
Make a calm register with one page hinged open inside its original row. At (240,104), a 800×616 parent card with radius 22 leaves generous horizontal air. A 752×40 header, 24px gap and 752×504 register consume the 24px inset budget. Four folded rows are 60px tall; one selected row is 240px; 6px row gaps finish the 504px height. The selected summary occupies 60px, leaving 180px for its body: 16px top/bottom padding, a 112px reading slot and a 36px action line. The selected row's interior has a 184px label column, 24px gutter and 496px reading area with 16px edge padding. Use 28px outcome, 18px title, 15px primary rows and 13px supporting copy; CJK line-height is 1.45. No row needs an enclosing border or a deep shadow.

## Single P0 focal point
每日学习推荐 is the open row, and 已投递 3 题 is its one 28px outcome. The row title remains the selector title; the opened reading area must not repeat it. Below that outcome show 每日 3 题直投 Linear and the 04:15 completion, followed by a modest 立即运行 button. The folded rows are context, not additional action stations. A trio of checked small markers corresponds to delivered question count, not fabricated named lessons.

## P1/P2 folding
Order the register by the declared inventory: Linear @bot 桥接 (每 1 分钟), 我的 PR (每 5 分钟), PR 自动审查 (每 5 分钟), 个人数仓晨报 (每日 04:00), 每日学习推荐 (每日 04:15). Clicking a folded summary opens its own row and closes the previous one. In the digest row, a 阶段详情 button replaces the outcome and result paragraph in its 112px reading slot with a two-column compact stage sequence: ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题, ⑤ Brief 投递. Rows 1–3 and 4–5 wrap with 13px type and no abbreviated labels. 查看回执 swaps that body to the last result rather than extending the register. No separate master list and detail pane is allowed to duplicate the selected name.

## Color and surface polarity
Paper roles Light / Dark: background #F4F6F8 / #10161B; register #FFFFFF / #1B232B; opened-row #EDF4FA / #26333F; text #21303B / #EDF5FA; quieter #586B79 / #B5C8D5; interaction-blue #285F96 / #A9D4FF; filled-button-ink #FFFFFF / #152F46; completion #2B7053 / #94DFB8; error #A6384C / #FFB4C0; focus #276DA9 / #B5DDFF. Give the open row one blue 3px leading rule and a 2% luminance step. Secondary controls stay text-on-solid. The white paper is not a low-contrast gray-on-gray dashboard: the open outcome has full ink contrast.

## Liquid Glass optical parameters
Use no glass at the hinge, since the contents are the paper itself. Blur 0, displacement 0, saturation 100%; a 0 2px 8px shadow at 3% black separates the open row in Light and at 18% in Dark. Radius 14 for its inset surface is below the parent 22. There is no material-dependent Safari branch. Reduced Transparency leaves the exact same pixels, and reduced motion disables the 150ms height interpolation while retaining single-row expansion.

## Inline SVG iconography
Use a 24×24 folded-page icon, drawn with a 1.5px rounded stroke and one open fold corner. The learning row's outcome shows three discrete check circles beside its labelled count, not a decorative confetti burst. Summary buttons have a trailing chevron whose visual size is 16px inside a 32×32 interaction area; the whole 752×60 summary is operable. Document-outline and play-arrow controls use currentColor at 24×24, each with explicit text rather than anonymous glyph-only actions.

## Explicit anti-patterns
Do not implement two synchronized copies of the selected row or stack five expanded rows. Reject a browser-like sidebar, page routing, numbered fake question titles and an unrelated lesson library. Empty record handling must not create a sixth register entry. Avoid universal 1px cell cages, tiny 11px captions, stripes, rulers and in-card theme toggles. No historical sparkline can be sourced from these single latest records; the three outcome marks are the truthful compact visualization.

## Interaction and states
Initial state is daily-learning selected, completed 04:15 with three deliveries; digest stays folded with its 04:01 completion and 5/5 status. Resolve the frequent jobs' latest timestamps from ../../domain.md, without making due work red. Tab visits the five summaries and then the selected row's controls; Space selects a summary while keeping exactly one row open, and Escape returns an open evidence body to the outcome. Run activation affects only the opened record: show 已排队 immediately, 运行中 while busy, and 刚刚完成 · 耗时 14s in its same outcome line. Keep a closed busy row's status visible if another opens. A missing receipt uses 暂无回执 in the body; a failed attempt uses 运行失败 beside the retry-capable 立即运行. No modal confirmation is needed for this non-destructive action.

## Stage 2 handoff
Under main.topology-hinged-register → section.content place header and ul[register] as direct siblings. Each of the five li parents an article containing button[summary] and div[row-body]; row-body parents output, p[result], div[mode-content] and div[actions], and only one body is expanded. This li→article→summary/body shape is required; do not replace it with a generic hero and satellite grid. Test that all five labels are visible once in the launch frame, a digest expansion produces exactly the five real stage names, and the learning row never inherits those stages. Switching evidence must keep the 616px parent height stable. Deliver screenshot evidence of the learning outcome, digest disclosure and a failure recovery for the downstream gates.
