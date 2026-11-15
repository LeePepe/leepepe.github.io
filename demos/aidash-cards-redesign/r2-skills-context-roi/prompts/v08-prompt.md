# v08 — 加载与触达分读台

Status: R2 original practice instrument, defining touches separately from script executions.
Target: desktop1280×800 inside the existing Skills ROI surface.
Coordinates: VS-003 + CL-003; X=touch/load ratio, Y=orthogonal operand split with local inspection drawer, Z=solid slate workbench; AppTheme=R2.TouchDesk.

## Visual metaphor
A split reading desk separates a load/touch equation from a detached execution counter. Use a 1112×650 card with 28px padding: the 656×324 operand field and 368×324 counter wing share a 32px gutter; a 1056×214 drawer lives below with 24px air. A straight eight-of-forty meter under the operands is functional quantity ink, not a trend. Outer corners are 22px, operand inset 14px and drawer 12px; micro-shadows stay at 0 5px 18px .04/.16.

## Single P0 focal point
my-designer’s touch rate is 20%: touch 8 / loads 40. Print 20% at 44px once above a 560px track whose filled length is 112px. Put 8 touches and 40 loads in 15px operand slots; the right wing reports 12 script executions at 15px with the explicit caption 脚本执行次数. Never place 12 above a slash with 40, and do not describe it as a 30% touch ratio. The registered skill name receives a 184px text span at 13px. The 12-execution wing is secondary, not another large dashboard hero.

## P1/P2 folding
实践 > 加载与触达 is active. The bottom drawer is closed at a 40px 查看使用依据 handle; it includes S4 usage and fresh R1 review evidence plus S6 load/touch definition when opened. 后续修改 switches to S8’s aggregate edits/retries and ROI switches to S10’s reported three-skill score order. 质量 exposes S1 drift, S2 catches/independent noise, S3 audits/evals and S9 escapes one group at a time. 披露 carries S7 without converting violations into funnel exits. 上下文 selects S11 构成 or Cache and S12 Tool burn; those retain ../../domain.md’s exact labels, tok units, window and eligible-request denominator. Decoder coverage resides at the drawer’s end with S5 暂无统计, not a fabricated practice statistic.

## Color and surface polarity
Tokens are canvas #F4F7F9/#10171D, card #FFFFFF/#1C2931, operand bed #EDF3F5/#2A3A43, execution wing #F6F7F8/#243139, text #17303A/#EDF8FB, secondary #536D76/#B4CBD3 and teal selection #146B74/#98D7DD. Font scale is 13px/15px/22px/44px, tabular for ratios and counts. Use a 14%-alpha selection tint only on the meter; this is neither all-cyan content nor a glass work surface. A 32px divider gap separates independent counts more clearly than a vertical 1px border.

## Liquid Glass optical parameters
The inspection drawer remains a solid sheet of slate. Its tiny explanatory info popover can use IOR 1.45, 8px bevel, displacement 2px, blur 6px, saturation 106% and .94/.97 opacity. Disable refraction entirely for Safari and Reduce Transparency, preserving the token surface and shadow; no unsupported filter may block a definition. Reduced Motion opens the drawer in place instead of the default 140ms height easing. Glass never samples the control picker or any other glass.

## Inline SVG iconography
Create a 24×24 split-operands glyph: left bracket from (8,4) through (4,4)/(4,20)/(8,20), right bracket mirrored at x16/20, with a small tap dot at (12,12). Stroke 1.75px currentColor with round corners. The adjacent control reads 使用与触达; the execution wing uses an unfilled play triangle with the text 脚本执行次数, never an executable Run button.

## Explicit anti-patterns
Do not confuse touch count with scripts, infer successful executions, forecast cost savings or invent named consumers. AIDash/user-skills may appear only where the supplied evidence actually names them; otherwise show aggregate readings. Reject a formula that treats 12/40 as touch rate, duplicate meter legends, generic histogram copies, internal state switchers and fake run/remediation actions.

## Interaction and states
The drawer handle is a 40px disclosure control with aria-expanded; Enter/Space opens it and Esc returns to the handle. The 实践 selector is keyboard-operable with a retained my-designer selection. ROI > 查看建议 reuses the drawer: 收藏 persists 已收藏 locally, 稍后 replaces the content with 已稍后 · 撤销, and undo restores both the prior recommendation visibility and saved flag. Changing to the operand view then back to ROI must keep that receipt until undone; closing a drawer merely closes it. If R1 evidence is missing show 暂无统计, not a fake review verdict. 暂无建议 keeps 返回排行 available, while a reveal error exposes 重试 without mutating counts. Controls default to 32px with a visible focus ring and perform no external work.

## Stage2 handoff
Use main.topology-touch-desk and its one immediate section.content. That section contains dl[role=group] with three dt/dd operand pairs, the touch dd owning a meter and textual label; aside[role=note] holds the independent script p; details contains summary plus an evidence section and a footer output. This semantic operand tree must survive implementation rather than becoming a reusable hero/table component. Check 112px of a 560px meter, 8/40=20%, the independent 12 count and the registered name at full width. Later screenshot acceptance must include the open drawer and both appearances, with no numeric ellipsis or raw localization keys.
