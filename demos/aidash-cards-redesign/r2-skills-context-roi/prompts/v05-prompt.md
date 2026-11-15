# v05 — Cache 请求计量器

Status: R2 cache-first instrument, authored separately from the token-composition atlas.
Target: desktop 1280×800; one existing Context ROI card, no new analysis page.
Coordinates: VS-007 + CL-008; X=eligible-request hit ratio, Y=radial readout with replaceable denominator panel, Z=opaque dial and definition popover; AppTheme=R2.CacheMeter.

## Visual metaphor
A single avionics dial sits left of a precise denominator placard. The 1064×640 card uses 32px padding, a 432×416 dial well and a 504×416 placard with 24px separation. A 300px-diameter annulus has 20px stroke and one 3.2% open segment; round ends must not inflate the encoded angle. Outer radius 28px, dial well 20px, placard 16px, with a calm 0 8px 24px shadow (.045 Light/.14 Dark). No decorative radial graduations.

## Single P0 focal point
Cache 命中率 96.8% sits inside the dial at 48px; it is S11’s eligible-request measure. On a 360-degree circle the hit arc covers 348.48 degrees and the remainder 11.52, starting at twelve o’clock. The placard states 命中 96,800 / 可缓存请求 100,000 and shows the residual 3,200 only as its arithmetic complement, not a second hero. These quantities refer to eligible token requests, never the 50,000tok context composition total. A static labelled indicator marks the selected Cache lens; it must not imply live streaming or weekly improvement.

## P1/P2 folding
上下文 > Cache is the boot subview. 构成 replaces the dial/placard with S11’s five exact slice entries and total from ../../domain.md; Tool burn replaces it with S12 Search P95 18,400tok, 120 calls / 7 days and an explanation that this is not duration. The card-level 质量 view holds S1, S2 catch plus independent noise, S3 health/evals and S9 escapes in disclosure groups; 实践 selects S4 usage/fresh R1 evidence, S6 distinct touches/loads/executions, S8 churn or S10 reported ROI; 披露 opens S7. A denominator-focused 统计覆盖 link gives S5 暂无统计. The cache dial and five-slice composition never occupy the viewport simultaneously.

## Color and surface polarity
Adopt alabaster #F8FAFC/#0E131F canvas, #FFFFFF/#192335 card, #F0F4FA/#263249 dial well, text #182A44/#EEF4FF, secondary #546781/#B5C6DF. Arc blue is #2567AF/#8DC1FC and neutral remainder #D9E2ED/#42506A. Keep numbers readable on the well itself, not on a saturated arc. Typography has just 13px body, 15px denominator headings, 22px title and 48px ratio, with monospaced digits. Shade the arc’s neutral gap, not the whole surface with a blue gradient.

## Liquid Glass optical parameters
The denominator info popover is functional regular glass with IOR 1.47, 9px bevel, 3px lens displacement, blur 9px, saturation 115%, and white/navy tint alpha .91/.96. Do not blur the request counts or put glass in the annulus. On Safari, use a solid placard-color popover and a 1px translucent top highlight; controls remain functional if backdrop filters are unsupported. Reduce Transparency also selects solid, while Reduce Motion omits the 180ms arc fade on entering Cache. No dial spin or bounce is allowed.

## Inline SVG iconography
Provide a 24×24 cache-stack glyph using three open rounded rectangles at y4/9/14, with a small check stroke at the lower-right, 1.75px currentColor lines. The 32px info button has the explicit name Cache 统计口径. The annulus is separately named Cache 命中率 96.8%，96,800 / 100,000 and does not expose hundreds of decorative path nodes to assistive technology.

## Explicit anti-patterns
Cache is neither a context slice nor proof of cost savings; never combine request and tok denominators. Reject an animated racing needle, fake cache trend, invented hit latency or a P95 time unit. Avoid repeated gauges for Quality/Practice, internal selection chrome, opaque shadows as thick frames and false S5 data. No external cache-clearing command may appear.

## Interaction and states
Arrow keys move among 构成 / Cache / Tool burn; pressing the selected subview does not spawn another card. Definition popover closes on Esc with focus restored to the info button. 实践 > ROI > my-designer gives 查看建议 in the placard footprint: 收藏 updates to 已收藏, 稍后 swaps the proposal for 已稍后 with 撤销, and undo restores the proposal plus its exact saved state. Return-to-Cache preserves those local states; proposal dismissal leaves the my-designer selection available for reopening. 暂无建议 retains 返回排行, and 暂无统计 renders an unfilled neutral instrument with text rather than 0%. A presentation error exposes 重试 without altering the denominator. All local buttons are 32px, use visible focus, and do not invoke network or scheduler operations.

## Stage2 handoff
Keep main.topology-cache-meter with a direct section.content holding article[role=group] > figure > SVG annulus and figcaption; a sibling section[role=region] > dl with request operands and details for definitions; then footer > button for coverage. Do not hide the figure inside a generic hero shell excluded by topology inspection. At the target viewport, preserve a 432px dial footprint and separate request operands without truncation. Writer verifies 348.48-degree encoding, composition exclusivity and P95 tok units before later Safari/light/dark pixel checks; canonical starter byte identity is irrelevant to this authored topology.
