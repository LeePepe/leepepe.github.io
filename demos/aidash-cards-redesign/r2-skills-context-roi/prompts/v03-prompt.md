# v03 — Pin 对齐检修道

Status: R2 original alignment direction, specified around the decoder’s aggregate pin count.
Target: desktop1280×800 within the existing macOS card host.
Coordinates: VS-003 + CL-003; X=alignment evidence, Y=longitudinal lane with one hinged readout, Z=solid instrument bed; AppTheme=R2.PinLane.

## Visual metaphor
A maintenance alignment lane: two short unjoined contact marks at the left, followed by six connected contacts. This is an aggregate counting diagram, not eight invented skill identities or commit versions. The 1144×620 card uses 24px padding; a 1056×224 instrument bed sits above one 1056×232 hinged evidence region with 28px separation. Keep the bed borderless, radius 18px inside a 26px card, and place a restrained inset top highlight instead of grey rules across every contact.

## Single P0 focal point
S1 Pin Drift’s 2/8 behind anchors the initial 40px reading. The eight contact positions are equally spaced along a 768px span, each given a 64px mark zone; two open gaps are amber and explicitly labelled 落后 2, while the connected bracket is labelled 已对齐 6. Do not assign names, severity or version distances to those dots. A 13px Pin Drift definition button sits near the main numeral, not a second number card. The dotted pattern is a count, never a fabricated time trend.

## P1/P2 folding
质量 is selected with Pin 对齐 active. Its hinged region starts closed, revealing only 查看对齐依据; opening shows the aggregate reading and decoder definition, with 暂无统计 for absent per-pin evidence. Other Quality items replace this hinge: S2 catches/noise, S3 audits/evals, S9 implementation/specification escapes. 实践 switches the whole instrument to an inline group selector for S4 usage and fresh R1 review, S6 touches vs loads vs scripts, S8 edits/retries and S10 reported ROI. 披露 owns S7 L0/L1 and independent deep-read violations. 上下文 includes S11 composition/Cache and S12 Search P95 through separate subviews. Their labels and readings come from ../../domain.md; 统计口径 at the hinge’s edge discloses S5 暂无统计. There is one instrument active, never a stack of lanes for every metric.

## Color and surface polarity
Slate/cyan precision with no neon dashboard glow: window #F3F6F8/#0E1117; outer card #FFFFFF/#191F28; lane #EEF3F6/#25303B; main text #152631/#EEF6FB; secondary #536674/#B2C5D2. Cyan selection is #076B87/#8FD7EA; amber gaps #8A570C/#E9C47C use accompanying gap shapes. Body is SF Pro 13px, lane label 15px, title 21px and reading 40px; identifiers, units and slash counts are tabular at a minimum of 13px. Use a 0 3px 14px shadow at .05/.18 beneath the card.

## Liquid Glass optical parameters
A pin-definition popover may use blur 10px, saturation 112%, IOR 1.46, 8px bevel, 3px maximum lensing and .92/.95 light/dark opacity. It samples only the opaque lane, not another floating control. The hinge and contacts are never translucent. Safari’s CSS-only fallback is an opaque slate panel with a .08 specular edge; reduced transparency follows that branch. Reduced motion replaces the 160ms hinge reveal with an instant open and stops all mark movement.

## Inline SVG iconography
Use a 24px disconnected-link glyph, two rounded bracket paths on x4..10 and x14..20 with a deliberate 4px center gap, 2px stroke. The associated button’s accessible name is Pin 对齐依据. Tiny filled/slashed contact indicators reinforce the count without becoming clickable 8px targets; the enclosing evidence button is 32px high and has a visible 2px focus halo.

## Explicit anti-patterns
Do not invent eight pin names, upstream hashes, elapsed drift history, repair controls or synchronization jobs. A warning gap is not a failed audit. Never add an 执行修复 CTA. Reject cloned chart+table layouts, cyan glow washes, glass contacts, duplicate 2/8 summaries, numbered rulers or internal readiness toggles. Normal missing values cannot be replaced with zero.

## Interaction and states
The evidence hinge opens with Enter or Space and closes with its own 返回对齐 button or Esc, restoring focus to 查看对齐依据. Arrow keys inside the Quality selector switch metrics without acting on them. 实践 > ROI > my-designer reveals 查看建议 as a hinged readout, not a command console. 收藏 marks 已收藏 locally; 稍后 tucks the recommendation out of the hinge and leaves 已稍后 plus 撤销 in its header. Undo restores the prior open readout and saved flag, even after visiting Pin; closing does not erase that state. When evidence is absent, 暂无统计 remains beside an enabled return control. Suggestion absence shows 暂无建议; presentation failure offers 重试 without dropping selection. Nothing communicates with a service, and Reduce Motion leaves keyboard order unchanged.

## Stage2 handoff
Give main.topology-pin-lane exactly one immediate section.content. Its children are div[role=group] > header with the ratio, figure > svg contact track and figcaption; then details > summary/button and a nested section[role=region] containing an evidence dl; finally a small footer with 统计口径. The hinge must be a real child, not an empty generic hero wrapper. The first screenshot must show exactly two gaps and six connected positions inside the 224px lane with no fabricated labels. Later review checks missing-evidence wording, all eleven defined metric routes, dark cyan contrast and a complete keyboard return through the hinge.
