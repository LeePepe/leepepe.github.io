# v01 — 上下文比例地图

Status: R2 Designer-authored breadth candidate; the proportion map is ready for Stage2 translation, not theme freeze.
Target: desktop 1280×800; one Skills 效能与上下文 ROI card.
Coordinates: VS-007 + CL-008; X=token-share inspection, Y=exclusive Context lenses, Z=solid atlas with definition popover; AppTheme=R2.ContextAtlas.

## Visual metaphor
A cartographer’s proportional atlas, not a dashboard of equal widgets. Center a 1120×644 solid card with 28px padding inside the supplied product window. Its 704×344 plotting region sits beside a 304px reading margin with a 28px gutter. Five horizontal bands have different occupied lengths against one 50,000tok scale; a generous empty field at their right makes the largest contributor immediately legible. Use a 24px outer radius, 14px inset rounding and a soft 0 6px 20px shadow at 5% black in Light, 16% in Dark.

## Single P0 focal point
Tool results occupies 40%, or 20,000tok. That is the sole large 36px callout, positioned at the end of its band, not copied into a second summary tile. Initial band lengths on a 600px quantitative span are 72/48/96/240/144px for System / AGENTS 6,000tok 12%, Skills 4,000tok 8%, Tool schemas 8,000tok 16%, Tool results 20,000tok 40%, Conversation 12,000tok 24%. Put each exact label and token/share pair in its own 52px row, with a minimum 32px selection area independent of painted length. The caption carries only 总计 50,000tok. No five-slice pie appears beside the bands.

## P1/P2 folding
上下文 starts selected for S11. Its reading margin contains Cache 命中率 96.8% at 15px, a separate definition disclosure for 96,800/100,000 eligible token requests, and a closed S12 Tool burn entry that replaces the margin with Search P95 18,400tok · 120 calls / 7 days. The 32px card toolbar offers 质量 / 实践 / 披露 / 上下文; switching replaces the atlas footprint rather than appending content. 质量 exposes S1 Pin Drift, S2 catch and independent noise, S3 audits/evals and S9 escape attribution; 实践 houses S4 usage/review, S6 load/touch/script counts, S8 churn and S10 ROI; 披露 contains S7’s L0/L1 split and independent violations. Within each lens, single-active native disclosure rows reveal readings from ../../domain.md. 统计范围 opens the decoder coverage with S5 暂无统计. Thus every metric has a named returnable route, not a hidden menu of twelve peers.

## Color and surface polarity
AppTheme pairs canvas #F8FAFC/#0E131F, card #FFFFFF/#18202D, margin #F1F4F8/#222C3B, primary ink #172033/#F3F6FC and secondary ink #56647A/#B3C0D3. The selected band is indigo #4D59B5/#A8B0FF; other bands use neutral blue-grey shades, differentiated by labels and length rather than rainbow hue. Keep normal labels 13px, section titles 15px, card title 22px and the single 36px share. All numeric text uses tabular digits. No label falls below 4.5:1; the dark active band uses navy text if a solid pale fill is used.

## Liquid Glass optical parameters
Only the definition popover may borrow functional regular glass: 10px corner bevel, IOR 1.45, displacement capped at 4px, blur 8px, saturation 110%, light tint alpha .90 or dark tint .94. Do not refract the proportional bands. Safari and Reduce Transparency use the opaque margin tokens with a narrow top highlight; no SVG filter dependency is necessary for operation. Reduce Motion makes band selection instantaneous instead of a 120ms opacity change. There is no overlapping glass sampler.

## Inline SVG iconography
Use a 24×24 currentColor atlas glyph: three horizontal paths beginning at x4 and ending at x20/x14/x17 on y6/12/18, with 2px round caps. Its accessible control name is 上下文构成. A small solid selection dot belongs to the Tool results row and never pulses; avoid inventing a historical sparkline without chronological source data.

## Explicit anti-patterns
Reject sixth-slice cache wedges, a misleading 96.8% share of the 50,000tok total, duplicate legends and equal-length ornamental bands. Never fabricate S5, monetary ROI, token savings or new app destinations. Keep the chooser’s theme/window controls outside this card; do not add debug rulers, caustic stripes, state selectors or tiny clipped percentages. No 1px grid cage around the five rows.

## Interaction and states
Clicking a band transfers one selected-slice outline and opens its definition in the margin; Arrow Up/Down selects the next band, Enter opens it, and Esc returns focus to its band button. The 实践 > ROI > my-designer route opens 查看建议 inside the existing reading margin. 收藏 changes to 已收藏; 稍后 removes the visible proposal and reveals 已稍后 with a persistent 撤销 action. Undo restores the prior proposal and saved flag, including after lens changes in this view; closing returns to the my-designer rank entry. These are in-memory view operations without service calls. If proposal content is unavailable, show 暂无建议 and keep 返回排行; an unavailable metric displays 暂无统计, while measured zero remains 0. Focus rings are 2px, actions are 32px high, and no recovery relies on hover.

## Stage2 handoff
Render one main.topology-context-atlas with one direct section.content. Inside content, preserve figure[role=group] containing the band SVG and figcaption’s five selection buttons; beside it an aside containing a definition dl and one details disclosure; follow with details for 统计范围. The lens toolbar may sit in the main header, but do not put this tree inside a generic hero/fold-panel/secondary shell. At 1280×800, verify the 40% endpoint, all five unabbreviated labels, separate cache denominator and Tool burn return route. Writer must use the domain reference, not add records to fill the atlas; later pixel review must check both appearances and keyboard recovery.
