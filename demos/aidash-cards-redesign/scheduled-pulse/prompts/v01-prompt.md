# v01 — 晨报磁场 · Unequal job magnets

Status: Designer-approved for Stage 2; fresh R2 Scheduled Pulse exploration, not an Owner-frozen production design.
Target: desktop/macOS, 1280×800; one card within the outer window frame.
Coordinates: VS-007 / CL-008 / X:direct-job-magnets / Y:tile-substitution / Z:solid-raised-focus / AppTheme:R2PulseMagnet.

## Visual metaphor
An unequal bento behaves like a set of job magnets: the selected object attracts space, not duplicated metadata. Center a 1040×584 card at (120,108), radius 26, padding 24. A 992×44 header precedes a 24px gap and a 992×468 magnet field. The field has a 536px lead and a 432px satellite area separated by 24px; satellites occupy four 210×222 cells with 12px gutters. These five items form one collection, not five independent dashboard panels. Use SF Pro at 40/20/15/13px, 4px atom spacing and 16px tile padding; lead content gets 24px padding. The lead rises with a 0 10px 30px shadow at 7% black in Light, 24% in Dark.

## Single P0 focal point
Make the completed morning digest's 5/5 stage result the unmistakable 40px anchor. Its title, cadence, latest completion and single 立即运行 button belong to that same enlarged article. The default selected ID is aidata-digest; do not put its title in a separate selector or repeat it in the header. Satellite numerals must stay 15px so they cannot compete with 5/5. A five-notch success trace represents actual stage outcomes, never an invented historical sparkline.

## P1/P2 folding
Place Linear @bot 桥接 with 每 1 分钟 in the upper-left satellite, 我的 PR with 每 5 分钟 upper-right, PR 自动审查 with 每 5 分钟 lower-left, and 每日学习推荐 with 每日 04:15 lower-right. The selected magnet says 个人数仓晨报 and 每日 04:00 exactly once. Satellites expose only status and cadence, no repeated run controls. A lead-only disclosure labelled 阶段详情 replaces the notch trace with the ordered digest route: ① 个人源采集 → ② L2-L3 入仓 → ③ Retro-ROI → ④ 学习寻题 → ⑤ Brief 投递. A second lead control, 查看回执, switches that same 200px inner region to completion evidence; it does not append a bottom inspector. Selecting learning instead shows 每日 3 题直投 Linear, with no five-stage route.

## Color and surface polarity
Role pairs are Light / Dark: canvas #F3F6FA / #0C111B; card #FFFFFF / #171E2B; lead #EDF2FC / #222D41; ink #162033 / #EFF4FF; muted #596579 / #B4C0D4; accent #4059AD / #AFC2FF; on-accent #FFFFFF / #111A30; success #236B49 / #86DDB0; danger #AB3348 / #FFACB8; focus #3457CA / #C0D1FF. Use the accent only on the selected magnet edge and its commit button. Success notches use labelled checkmarks rather than five green filled tiles. Keep the canvas visible around the single parent card; do not outline all satellites.

## Liquid Glass optical parameters
Choose solid-only magnets: refraction would wrongly make content look draggable or translucent. Set content blur, displacement and chromatic separation to zero. Even the lead's action is an opaque 112×36 button, radius 12; depth comes from the measured elevation, not backdrop sampling. Inactive-window styling reduces the lead shadow to 3% and removes its accent rim, while keeping labels unchanged. Safari and reduced-transparency rendering therefore use the identical solid hierarchy.

## Inline SVG iconography
Give the digest a 24×24 tray glyph with an entering arrow, 1.7px currentColor rounded strokes. Satellites use bridge/link, branching PR, review/check and learning/open-book glyphs at the same optical weight. The five-notch trace has one check per recorded stage, no heartbeat line. Each entire satellite is a minimum 210×64 click target; icon-only disclosure affordances still reserve 32×32 and expose their textual accessible names.

## Explicit anti-patterns
Reject equal-weight bento tiles, a second digest title above the field, and any floating bottom bar. Magnets are selectors, not a drag/reorder feature. Do not make the lead a glass content card or fill every satellite with a different bright color. Prohibit internal theme controls, rulers, striped optical overlays and debug pills. Preserve full 5/5 and time strings without numeric ellipsis; source identifiers must remain off card pixels.

## Interaction and states
Initialize from ../../domain.md at 11月15日 04:15: morning digest completed 04:01; the three frequent jobs retain their respective 04:14/04:10/04:10 successes, and learning has three delivered questions at 04:15. Clicking a satellite swaps that same article into the lead footprint and moves the previous lead into the vacated satellite position; there are always exactly five named articles. Enter activates a focused magnet, and Escape closes its local details. Clicking 立即运行 changes only that article through 已排队, 运行中 and 刚刚完成 · 耗时 14s; guard repeat clicks while busy. Announce feedback in the lead status line. If a record is absent show 暂无回执 there, not a sixth card. A failed selected result shows 运行失败 with 立即运行 available again. Respect Reduce Motion by replacing the 180ms size transition with immediate placement.

## Stage 2 handoff
Implement the inner tree as header plus div[group:magnet-field], directly under main.topology-pulse-magnets → section.content. The field parents one article[selected-magnet] with header, output, figure, details and div[actions], beside a div[group:satellites] parenting four buttons, each with span[label], time and span[status]. No sole generic hero wrapper may swallow these siblings. Use the accompanying v01 topology outline as the structural contract, not cosmetic class renaming. Acceptance: at launch every exact job label has one visible occurrence; choosing learning removes the digest stage route; returning to digest restores its five named stages; evidence stays inside the lead; two rapid run clicks yield one pending operation. Capture both appearances and expanded details for downstream Visual Traceback; actual service access is outside this handoff.
