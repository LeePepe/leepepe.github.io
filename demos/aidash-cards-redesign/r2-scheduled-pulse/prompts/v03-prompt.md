# v03 — 五点观测环 · Discrete health orbit

Status: Designer-approved for Stage 2 execution of this independently composed R2 orbit candidate.
Target: desktop/macOS 1280×800; a single bounded Scheduled Pulse instrument card.
Coordinates: VS-006 / CL-008 / X:orbital-job-choice / Y:radial-evidence-turn / Z:opaque-instrument / AppTheme:R2FivePointOrbit.

## Visual metaphor
An observatory has five selectable stations around one quiet center. Place a 1000×620 instrument at (140,90), radius 30 and 28px inset. Its 944×508 orbit region sits below a 36px header with 20px clearance. Within the orbit, a 320×250 center readout occupies (480,294) in window coordinates. Five 228×76 station buttons sit at local (54,32), (636,32), (688,230), (358,416) and (0,230) relative to the orbit. These measured offsets keep names apart; do not distribute long CJK labels along a circular text path. Use 44/20/15/13px SF Pro, a 4px label/status gap and 20px center padding. A 6% Light / 26% Dark soft shadow lifts the parent instrument only.

## Single P0 focal point
The central 5/5 readout belongs to the selected morning digest and reports its recorded five passed stages. Do not call it system health, uptime or scheduler reliability: those denominators are unavailable. The selected job's name appears solely on its orbit station; the center uses 阶段通过, 04:01 完成 and 立即运行 without another title. A thin five-segment ring around the center maps the digest stages, not the five jobs. Place its 340×270 rounded perimeter at window (470,284), radius 34, outside the readout's flow; it fits between the measured stations. Station connectors carry selection only, avoiding false causal pipeline edges between jobs.

## P1/P2 folding
Bind top-left to Linear @bot 桥接 / 每 1 分钟, top-right to 我的 PR / 每 5 分钟, right to PR 自动审查 / 每 5 分钟, bottom to 个人数仓晨报 / 每日 04:00, and left to 每日学习推荐 / 每日 04:15. Labels remain once even when the center changes. Clicking 阶段详情 replaces the central summary value and ring with a compact ordered definition list: ① 个人源采集; ② L2-L3 入仓; ③ Retro-ROI; ④ 学习寻题; ⑤ Brief 投递, each paired with 通过. This replaces the ring instead of adding a legend elsewhere. 查看回执 rotates the same center slot to its record. Selecting learning changes the center denominator to 3 题 and shows 每日 3 题直投 Linear; hide the stage ring entirely for non-digest jobs.

## Color and surface polarity
Optical roles in Light / Dark: outer-canvas #EEF2F8 / #0B1221; instrument #FFFFFF / #172136; center #EFF2FD / #253251; text #20283F / #F0F3FF; subdued #5B6380 / #B9C5E0; selected #53429B / #C8B9FF; button-text #FFFFFF / #261C4D; passed #286C50 / #91DFB7; failed #B33B51 / #FFB1C0; focus-outline #6550BA / #DCCEFF. Place violet on one selected station and the run control. All unselected stations use the instrument surface with no saturated category fill. Ring checks need a textual 5/5 equivalent, so colorblind users never have to count hues.

## Liquid Glass optical parameters
An instrument's data must not blur when station focus moves; therefore every radial content plane is opaque. Specify 0px backdrop blur, 0px refraction and no Fresnel flare. Center radius 24 sits concentrically inside the 30px parent, with 1px top-edge luminance at 5% rather than a translucent lens. Safari fallback is simply the same opaque instrument. When the window is inactive, the violet connector becomes subdued ink but state checks retain their role colors. No breathing sphere animation is borrowed from the VS-006 source metaphor.

## Inline SVG iconography
Provide a 24×24 open circular locator with five small tick marks as the card glyph, 1.8px stroke and no compass direction labels. Stage progress uses five true arcs with explicit checkmarks; render it as an accessible figure, labelled 5/5 阶段通过, not as an icon font. Job buttons get bridge, fork, review, tray and book outlines. A focused station receives a 3px keyboard ring outside its 16px corner; the station's full rectangular hit area remains at least 228×76 despite the orbit visual.

## Explicit anti-patterns
Forbid a fabricated 100% 健康 score, a ring dividing unrelated job frequencies, and redundant ring-plus-list representations in the same center. No rotating carousel, radial app navigation or clickable connectors. Do not make all five stations glow continuously. Keep every station within the card and disallow decorative star fields, emoji labels, fake history traces, internal preview switches and numeric clipping. The ring's stages must not be reused for learning's three-question outcome.

## Interaction and states
Launch aidata-digest selected with the ../../domain.md completion at 04:01; the remaining station statuses reflect the shared 04:15 clock. Pointer or keyboard station selection changes only the anonymous central readout and one selected connector. Stage-detail and receipt modes are mutually exclusive; Escape returns to the central summary and retains the selected station. Run feedback reads 已排队 in the center, then 运行中 beside a single open running arc, then 刚刚完成 · 耗时 14s with digest 5/5 or learning's 3 题 as appropriate. Busy operations stay bound to their original job if another station is chosen; never transfer completion to it. For an absent record put 暂无回执 in the center; for failure show 运行失败 and a reachable 立即运行 recovery. Reduced Motion uses static arc-state substitutions without continuous rotation.

## Stage 2 handoff
The direct content children are header, div[group:orbit-map] and p[status-announcement] under main.topology-five-point-orbit. That final p is a visually hidden live region; visible feedback stays inside the center or originating station, so it adds no height to the orbit budget. The orbit-map parents a decorative svg[connections], nav[job-stations] with five buttons, and article[central-readout] with output, figure[stage-ring], dl[stage-detail] and footer[actions]; keep the nav and article siblings, not wrapped inside hero. SVG connections are aria-hidden and have no pointer handling. Assert only five visible job names, one center value, and five stage labels after disclosure; selection of daily-learning removes all stage arcs and shows 3 题. Review focus traversal around the five rectangular stations in both appearances. This is an outline for the Writer, not a rendered or independently reviewed topology receipt.
