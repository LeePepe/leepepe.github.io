# v08 — 到点画报 · Editorial due moment

Status: Designer-approved Stage 2 editorial candidate, independently authored for R2 rather than recoloring a table.
Target: desktop/macOS 1280×800; one operating card in the existing framed chooser.
Coordinates: VS-008 / CL-008 / X:due-time-poster / Y:under-number-shutter / Z:opaque-ink-block / AppTheme:R2DuePoster.

## Visual metaphor
Compose a punctuality poster with large numerals and a narrow job register on its side. At (112,100), a 1056×600 parent uses radius 28 and 28px insets. A 1000×40 header leads into a 1000×480 body after 24px. Split that body into a 640px poster, 32px gutter and 328px secondary register. The poster has 28px padding and a 584px reading width: reserve 56px for title/cadence, a 12px gap, an 88px number line, a 20px clock caption, a 16px gap, a 36px action row, another 16px gap and a 176px shutter region. These consume 476px including insets. The register fits four 328×108 sibling selectors separated by 16px. Typography is 64px monospaced due counter, 24px selected title, 15px actions and 13px factual annotation. Large type has no tracking tricks or decorative all-caps eyebrow.

## Single P0 focal point
The default focus is the bridge's due-now 00:00 counter, not a fictional countdown to a future run. Its latest success is 04:14 and its next scheduled moment is 04:15 at the shared clock; show 到点了 beside the counter. The poster alone owns Linear @bot 桥接 and 每 1 分钟. 立即运行 is the only accented action below it. Do not also place the selected name in the side register or a header subtitle. A short clock arc has an explicit due-now caption, not invented recent-run history.

## P1/P2 folding
The side register carries 我的 PR — 每 5 分钟, PR 自动审查 — 每 5 分钟, 个人数仓晨报 — 每日 04:00, and 每日学习推荐 — 每日 04:15. Choosing one exchanges it with the poster object; the previous focus moves into its vacated side slot. Below the big number, 查看回执 lifts an opaque shutter within the poster's existing 176px space. When digest becomes selected, the focal number is 5/5, and 阶段详情 changes that shutter into five labelled steps: ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题, ⑤ Brief 投递. For learning, use a single 3 题 headline and 每日 3 题直投 Linear, never the digest shutter sequence. Retain the same poster footprint for every object.

## Color and surface polarity
Light / Dark pairs: backdrop #F2F3F7 / #121625; parent #FFFFFF / #1D243B; poster #EEF0FC / #2B3354; primary-text #242745 / #F2F1FF; secondary-text #5F647F / #BEC4E1; primary-action #6541A1 / #D3BCFF; action-text #FFFFFF / #30204E; successful #2B6B4E / #9DE0BC; failed #AA354E / #FFB2C5; focus-ring #7751B7 / #E2D1FF. Ink, not saturated background, carries the editorial weight. Keep the poster pastel in Light and deep desaturated violet in Dark, with one violet action. The 00:00 counter uses primary-text even though it is due, not alert red.

## Liquid Glass optical parameters
Choose an opaque editorial block: numberforms cannot tolerate refractive jitter. All blur/displacement values are zero, and the shutter is a solid poster-colored region. Parent elevation is 0 12px 36px at 7% Light / 29% Dark; side selectors have radius 16 and no shadow. The shutter gets one 0.5px inset highlight at 6%, never a gradient veil. Reduced Transparency and Safari therefore render the same deliberate ink surface; Reduce Motion turns its 180ms reveal into an instant replacement.

## Inline SVG iconography
Draw a 24×24 open clock arc with a single terminal tick, 1.8px rounded stroke; its caption says 到点了 in the bridge poster. The side selector glyphs are outlined forks, review check, digest tray and learning book. In completion mode substitute a check circle instead of implying a live timer. The receipt shutter control combines a 24px document outline with 查看回执; all side entries expose their entire 328×108 hit area. Focus outlines must remain visible against the violet poster without a glowing halo.

## Explicit anti-patterns
No imaginary 05:00 countdown at launch, giant fake efficiency percentage or auto-advancing slideshow. The large counter must never claim elapsed run duration before a run. Reject decorative poster text that displaces actual job names, repeated selected titles, saturated full-card purple, caustic stripes and internal appearance toggles. Side entries are existing job choices, not navigation to new product screens. Never shrink or ellipsize the headline to fit; this measured 584px line accommodates 00:00, 5/5 and 3 题.

## Interaction and states
At 11月15日 04:15, select linear-bot-bridge with the shared due moment and resolve sibling records from ../../domain.md. Clicking the digest swaps its article into the poster, showing 5/5 from 04:01; learning produces the recorded three deliveries at 04:15. Escape lowers the shutter without undoing job selection. Run activation replaces the counter with 已排队, then 运行中, then 刚刚完成 · 耗时 14s; do not continue a made-up ticking timer underneath that result. Bind pending feedback to the chosen job even after a swap. 暂无回执 occupies only the shutter when evidence is absent; a failed run shows 运行失败 and the same 立即运行 action becomes usable. The announcement is a short factual line, not a proof essay or a silent color change.

## Stage 2 handoff
The shape is main.topology-editorial-due-poster → direct section.content with header, article[poster] and aside[sibling-register]. The poster parents h2, p[cadence], output[due-or-result], figure[clock-state], div[action-row] and details[receipt-shutter] whose body contains ol[stage-route]. Aside parents nav with four buttons, each parenting span[label], time and span[latest]. This direct article/aside split must not be wrapped in a sole hero or transplanted into the orbit's nav/center tree. Assert initial counter equals 00:00 from real cadence inputs, every job name stays single after swapping, and digest and learning outcomes have different denominators. Downstream snapshots must include the large-number Dark appearance and the open five-stage shutter with full CJK labels.
