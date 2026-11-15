# v06 — 修改余波口袋

Status: R2 independently authored count-and-pocket direction, anchored in post-skill churn.
Target: desktop 1280×800, AIDash card body only.
Coordinates: VS-006 + CL-007; X=aggregate edits reading, Y=two count rows with tucked ROI pocket, Z=solid warm leaves; AppTheme=R2.ChurnPocket.

## Visual metaphor
A calm outcome pocket holds two rows of count beads above one tucked analytical leaf. The 1096×652 outer card is padded 28px; the count article is 1040×268 and the folded leaf occupies 1040×220 beneath a 28px gap. Edits and retries are parallel rows, not a chronological swarm. Make the front leaf radius 18px and the exposed back edge radius 22px, with only a 12px offset and a .045/.14 0 6px 20px shadow. This depth signals a reachable companion, not an imaginary history library.

## Single P0 focal point
S8’s 18 edits is the only 46px value, paired with 修改 in the first row. Paint 18 discrete 12px circles at 24px pitch; each circle counts one edit but does not identify a session. A second 13px caption 重试 6 accompanies six small squares on the next row. A shared footer says 20 sessions. No distribution across those sessions is implied, and 18+6 must not become 24 affected sessions. The circles are static; their pattern does not claim skill-caused churn or a temporal trend.

## P1/P2 folding
Boot at 实践 > 后续修改. The tucked leaf’s visible 40px lip reads ROI 排行 and opens a replace-in-place leaf for S10 my-designer/code-review/team-lead reported scores. The 实践 selector also reaches S4 usage and fresh R1 review evidence plus S6 loads/touches/script executions, replacing rather than stacking bead charts. Quality’s one-active-fold interior contains S1 alignment, S2 catch/noise, S3 audits/evals and S9 escapes. 披露 gives S7; 上下文’s 构成 / Cache / Tool burn pages within this card own S11/S12. 统计覆盖 is a closed leaf disclosure with S5 暂无统计. All measurements and actual registered names are inherited from ../../domain.md; no consumers beyond AIDash/user-skills or aggregate counts are introduced.

## Color and surface polarity
Keep the warmth in neutral paper, not orange backgrounds. Canvas #FBF7EF/#1B1A20, card #FFFFFF/#28262D, pocket lip #F4EEE4/#35313A, main ink #302A28/#F8F1E9 and subordinate ink #6D625B/#C9BCB2. Edit beads use terracotta #975635/#E8B093; retry squares use mauve #705D7D/#CBB9D8 with text labels. SF Pro sizes are 13/15/22/46px and no smaller dot labels are permitted. Saturation is limited to bead marks and the active control, with 28px whitespace between reading groups.

## Liquid Glass optical parameters
The pocket leaves deliberately use no refraction: IOR 1.0, displacement 0, blur 0 and saturation 100% on content. An optional count-definition popover can use blur 5px, .95/.97 adaptive tint, IOR 1.42 and a 5px bevel with 1px maximum lens displacement. Safari/reduced transparency makes that popover solid warm paper. Reduce Motion opens the pocket without the ordinary 150ms 12px translation; no beads drift or orbit. Functional chrome never overlaps another glass layer.

## Inline SVG iconography
Use a 24×24 return-loop glyph with a path from (18,7) through a rounded U to (7,18), then a left arrow returning toward (4,12), at 1.75px currentColor. Pair it with 后续修改 rather than a magic-wand icon. The ROI leaf uses a small labelled bookmark; count beads are hidden from screen readers in favor of the figure’s aggregate caption.

## Explicit anti-patterns
Do not assign a bead to a named session, create a session-by-session timeline or imply edits were caused by my-designer. Avoid a 24-session sum, fake sparklines and invented consumer repositories. The pocket cannot flatten into an equal-tile dashboard or overflow its card. Reject a floating macOS bottom action bar, internal appearance/debug controls, invented metric definitions, and tiny text inside dots.

## Interaction and states
The 40px pocket lip opens by click, Enter or Space; Esc retucks it and restores lip focus. ROI > my-designer > 查看建议 turns the front leaf into the existing proposal view. 收藏 produces 已收藏 without changing its score. 稍后 hides the proposal face and leaves 已稍后 · 撤销 on the lip; undo reopens exactly that leaf with its prior bookmark and focus on the proposal’s 稍后 button. Fold and lens changes preserve local selection and action state until reload. If no proposal is available, 暂无建议 occupies the face with 返回排行; missing churn data renders 暂无统计 and no bead counts, distinct from genuine zero counts. A reveal failure keeps the lip reachable with 重试. Every control has a 32px-or-larger target, a clear 2px keyboard ring and no network side effect.

## Stage2 handoff
Create main.topology-churn-pocket with one direct section.content. Its immediate tree is article[role=group] > header plus two figure elements, each with its own bead SVG and figcaption, followed by a shared session p; a sibling div[role=region] holds a front section, a lip button and status output; details provides coverage. Only two content containers are active even when the front leaf is open. Test 18 circle marks, six square marks, the shared 20-session denominator and pocket saved→defer→undo restoration. The downstream pixel pass must verify both solid appearances and that the raised lip never hides numbers.
