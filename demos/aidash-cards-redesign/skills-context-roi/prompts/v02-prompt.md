# v02 — ROI 阶梯索引

Status: Independently composed for R2; this candidate prioritizes a low-ranked skill rather than context volume.
Target: desktop 1280×800, fixed card-space exploration for AIDash.
Coordinates: VS-002 + CL-002; X=reported-score reading, Y=ordered-rank accordion, Z=paper staircase with attached suggestion leaf; AppTheme=R2.RankStair.

## Visual metaphor
Build a quiet Swiss editorial staircase: an ascending sequence of three broad reading steps, with the lowest score nearest the viewer. The 1088×660 card has 32px outer padding, a 672×360 stepped rank field and a 280px side leaf separated by 32px. The left edges advance 0/36/72px without turning score into an invented geometric unit. Step height is 96px with 16px air; 20px container rounding and 12px step corners keep it tactile rather than cartoonish. One 0 4px 18px 4%-opacity shadow lifts the proposal leaf, not every row.

## Single P0 focal point
my-designer 0.4 is the starting focus, printed at 44px on the first step with 查看建议 beside its name. Above it in ascending score order sit code-review 1.2 and team-lead 1.8 at 15px; all are S10 reported ROI scores, not currency or calculated efficiency multipliers. Each score appears once and its order is explicitly labelled 按 ROI 升序. The 13px registered skill names receive at least 176px, so my-designer is never clipped beside its score. No rank cutoff, target score, savings arrow or quantitative staircase height is implied. On selection the enlarged score follows the chosen step; only one reading remains typographically dominant.

## P1/P2 folding
Start in 实践 > ROI 排行. A 36px top lens picker replaces this staircase with 质量, 披露 or 上下文 within the same 432px content depth. 实践’s subordinate 使用与触达 fold owns S4 loads and fresh R1 review evidence plus S6’s distinct load/touch/execution readings; 后续修改 owns S8. 质量 uses compact single-active sections for S1 alignment, S2 catch/noise, S3 health/evals and S9 attribution. 披露 opens S7. 上下文 presents S11’s exact five composition labels and eligible-request cache denominator in mutually exclusive 构成 / Cache views, with S12 Search burn below a closed definition. 覆盖范围 reveals S5 暂无统计; leave it off the rank face. The shared input ../../domain.md supplies every number without repeating a twelve-metric board.

## Color and surface polarity
Warm paper becomes carbon paper, not a black-and-gold luxury panel. Canvas #FAF7F2/#14181A, card #FFFFFF/#202628, selected step #F0F5F1/#2B3933, text #202820/#F1F5EF, supporting text #5B685E/#B8C4BA, forest accent #246343/#99D4B1. The proposal leaf is #F8F5ED/#30332D. Use SF Pro with a restrained New York 22px title; body 13px, step headings 15px, my-designer score 44px tabular. Do not color code-review or team-lead as bad/good scores without thresholds.

## Liquid Glass optical parameters
The suggestion leaf is solid. Its small action-menu popover alone can use regular glass, blur 6px and saturation 105%, IOR 1.4, 6px bevel and at most 2px optical displacement. Light/dark tint opacity .94/.96 keeps forest text readable. Safari receives a fully opaque paper popover; Reduce Transparency selects the same token directly. Inactive-window accents soften without making the focus ring disappear. Reduce Motion removes the 140ms leaf-slide and retains an immediate layout change.

## Inline SVG iconography
Draw an ordered-step symbol at 24×24: a rounded path M4 18 H10 V12 H16 V6 H20, stroke 1.75px, with a short baseline from x4 to x20. The 查看建议 action pairs a 24px open bookmark outline with text; a filled bookmark is reserved for 已收藏. Both use currentColor, and neither is an external image or decorative emoji.

## Explicit anti-patterns
Do not express 0.4 as money saved, interpolate missing skills between three ranks, or equate script executions with touches. Avoid a leaderboard trophy, progress-to-goal bars or false percentile ranks. The stepped articles cannot collapse into a common bar-chart/table template. No inner appearance switch, preview-state dropdown, thick cell borders or redundant selected-skill headline above the same row.

## Interaction and states
The ordered list is keyboard-addressable with 32px minimum row buttons; Tab reaches each name and Enter selects without navigating away. 查看建议 extends only the selected step’s side leaf. 收藏 stores its local saved state and shows 已收藏; 稍后 folds the leaf into a slim 已稍后 · 撤销 receipt beside that step. 撤销 reinserts the same leaf, restores its bookmark state and puts focus on 稍后. Reopening a deferred item offers that receipt, not a new proposal. Esc dismisses the menu first, then returns from leaf to step; lens changes retain selection and local actions until reload. Missing suggestions read 暂无建议 with 返回排行 available; failed local presentation must preserve the step and offer 重试. No backend remediation or dispatch is allowed.

## Stage2 handoff
The structure is main.topology-rank-stair with section.content directly beneath it. Content owns ol[role=list] with three li > article > header/button plus score p; a sibling aside[role=region] contains the suggestion article, footer buttons and status output; one details holds coverage. Put the native-style lens picker in the header outside the quantitative list. Preserve the visible 36px lateral stepping in both themes and cap the open leaf at 280×336. Acceptance compares the three reported scores, ascending order, the active-only 44px score and saved→later→undo behavior; it does not compare scaffold bytes or invent additional skill rows.
