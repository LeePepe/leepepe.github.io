# v02 — 待办工单 · One Open Work Order
Status: Designer-approved for Stage 2 demo implementation; Owner selection pending.
Target: desktop/macOS; 1280x800; scheduled-pulse.
Coordinates: VS-005 / CL-006 / X-ReceiptDecision Y-TicketFlap Z-SolidPaper / AppTheme-PulseWorkOrder

Candidate only: this is open-direction exploration, NOT final AppTheme selection or production approval. Active route: desktop × visual-style, layout-navigation, chart-dataviz, motion-interaction. VS/CL are reference-family IDs; X/Y/Z and AppTheme names here are explicit candidate-local coordinates, not new global taxonomy IDs. The 1280×800 is **iframe content**, excluding all outer portal window chrome. Do not add a second macOS frame.

## Visual metaphor
五张待处理工单只有一张放在书写垫上，其余是四张可读的侧签。把“需要你核对什么”作为纸面中心，不把所有输出拼成仪表盘。没有仿真胶带、污渍、手写字体或装饰邮戳。

外边距 32px；(32,28) 标题区高 48px。左纸面 (32,104) 760×632，右侧唯一签条组 (824,104) 424×632，中缝 32px。左内边距 32px，右内边距 20px。左任务名所在纸页标头高 52px；P0 问题区高 200px、最多三行 30px 半粗字；说明 15px、标签 13px，系统等宽只用于时间。右侧四条各 128px、间距 16px、组内上下 36px。每条名称/节奏/文字状态充分换行，不再套嵌套卡。纸页角 6px，内项间距 12px，原子 4px。

## Single P0 focal point
B 的一项演示决策：核对 14m20s 前的旧回执；大字问题而非 KPI。

No competing KPI tiles, repeated task strip or second prominent CTA. P0 is a display/decision in the selected record, P1 its single next contextual control, P2 evidence/stages on demand, P3 advanced context omitted from this public demo. One collection of five records is one visual group, not five unrelated modules; cap the overall screen at two content groups plus at most one transient in-context intent surface. P0 显示“这份旧回执，需要再核对吗？”；14m20s 作为 15px 说明，不另造数字 hero。右签的告警全部用次级文字而非四个强调色。尚未核对，证据页关闭。

## P1/P2 folding
默认 B 在左，其名字只出现于左工单标头。右侧按 A、C、D、E 排序。P1 的“已核对（模拟）”为问题下方唯一填色提交按钮；Run Now 始终轮廓样式且位于“更多操作”展开后同一纸面右上角。P2“翻看证据”把左侧问题正文替换为证据页，页内可返回；不要再造右侧 inspector。D 的五阶段或 E 的三个候选只在其成为左页时出现。

Default uniqueness invariant: five distinct selectable job records, each with its display name **once**, not the same name repeated on a summary chip and again in a list and inspector. Selected context is a continuation or replacement projection of that same record, never another named job card or second five-job dataset. Leave job IDs in data bindings, not as UI headings. When a role moves between regions, remove its old occurrence before presenting the new one; accessible names reference the existing visible name rather than duplicating visible labels.

## Color and surface polarity
Mint archive paper / forest-night paper; dark green ink and restrained sage accent.

平面薄荷纸主角；活动纸面与签条用亮度而非阴影隔离。暗色仍是有色档案纸，不是黑字纸张套在黑底上。

| Semantic role | Light | Dark |
|---|---|---|
| canvas / L0 | #EAF1ED | #101E18 |
| group / L1 | #F5F9F5 | #192A22 |
| focus surface / L2 | #FFFFFF | #22372B |
| ink | #17382B | #EDF6E9 |
| secondary ink | #496253 | #B3C9B6 |
| accent / focus ring | #236044 | #B4D8A5 |
| on-accent | #FFFFFF | #172C1C |
| separator (not text) | #C6D9CD | #425B49 |

Status ink pairs (Light / Dark, on normal L0/L1 surfaces only): success #166534 / #86EFAC; warning #92400E / #FCD34D; failure #9F1239 / #FDA4AF. Neutral/unknown uses secondary ink and explicit words; coalesced is neutral. Reserve at least 90% of the viewport for neutral solid surfaces; chromatic accent is for selection/P0 and keyboard focus, never all five jobs. Use text + distinct SVG shapes as well as color. Target normal-text contrast ≥4.5:1 and control/focus boundary contrast ≥3:1; decorative separators may be quieter, never the only affordance. Verify these pairs in rendered light and dark states rather than reducing opacity on text. Use system UI (-apple-system/BlinkMacSystemFont/system-ui) and local system serif/monospace where explicitly specified. No imported fonts. Use tabular numerals for time and ratios. Container padding is never less than internal gap. At most four font sizes per viewport; all non-display text remains ≥13px. Keep evidence within the declared region; do not shrink the entire layout to fit.

## Liquid Glass optical parameters
Explicitly NO Liquid Glass. This design reads receipts, schedules and evidence; a refractive substrate would compete with its chosen visual metaphor and harm small-text legibility. All content and functional controls are opaque semantic surfaces. Optical parameters: blur 0px, saturation 100%, IOR 1.0, refraction/displacement 0px, no backdrop-filter and no faux specular shader. Safari fallback is therefore the exact same opaque treatment, not a degraded screenshot. Reduced transparency is identical; reduced motion removes the nonessential 120ms opacity change. No content-on-glass and no glass-on-glass.

## Inline SVG iconography
Use this bespoke 24×24 currentColor stroke semantic icon for 含一个核对动作的折角工单, only once near the relevant region heading:

```svg
<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h9l3 3v15H6z M14 3v5h4 M9 12l2 2 4-4 M9 18h6"/></svg>
```

Other action icons use the same 24×24 viewBox / 1.75px rounded stroke: play triangle for Run Now, simple chevron for disclosure, outlined clock for stale, check for passed, warning triangle for warning, x-in-circle for failed, open circle + question text for unknown. SVGs inherit semantic ink, no gradients/external <use>/external assets. Decorative SVGs are aria-hidden; icon-only buttons receive an explicit readable aria-label and ≥28px target, with adjacent text for consequential actions. Never use emoji as UI substitutes, and do not download an icon set.

## Explicit anti-patterns
Ban .caustic-veil and repeating-linear-gradient zebra stripes; no striped filters, ruler/debug bars (including 28×28 dashed ruler boxes), inner web topbars, inner traffic lights, Active/Matte pills, decorative tracked-capital eyebrows, duplicate gallery/theme/viewport/selection controls, or bottom floating macOS action bar. Legitimate job selection and in-context evidence lenses are product controls, not forbidden gallery controls. No shared grey boilerplate, rainbow card grid, boxed KPI summary, fake live ticker, numeric truncation, raw localization keys, decorative emoji, stock imagery, external fonts/assets, glass content cards, glass-on-glass or opaque imitation system toolbar. No repeated task in a top summary + list + inspector. Never manufacture operational capabilities from this demo or interpret a sample warning as a real incident. Share only resets/state helpers across variants; build each layout, proportions, typography and color system independently, not one dashboard with alternate CSS colors.

## Interaction and states
选择右侧签条时，所选工单与左工单交换位置；右侧四个位置固定，保留原点击位置以便返回，屏幕仍只有五个命名对象。“已核对（模拟）”先在原位要求确认，确认后该处显示“已在本页标记；未提交到任何服务”，可撤销。翻页只是内容交叉淡化，不旋转纸张。

### Safe action state machine and supporting evidence states
Run Now is a **pure in-memory simulation** for the selected record: idle → intent → committing → settled. The idle control reads “Run Now · 模拟” (minimum 120×32px, permit two-line label if needed). Clicking opens an in-context intent panel saying “仅在本页模拟，不启动任务、不发送内容”, with “确认模拟” and “取消”. Cancel or Escape returns unchanged to idle and restores focus. Confirm immediately sets aria-busy, disables duplicate submission and job switching for a bounded 800ms, then settles to “已生成本页模拟回执 · 未发送到外部服务”. Nothing invokes launchd, shell commands, a network endpoint, file access or real job execution. Use a timer only for this simulation, not as evidence of actual runtime. A second click while committing must not enqueue anything. Settled feedback persists in the selected surface until “返回” or selecting another job; do not rely on an ephemeral toast. No undo claim for a real operation: only reset the local sample.

In the selected evidence fold, a small “证据示例” selector may expose ready / failed / empty / stale locally. These are **evidence** states, not alternate Run Now outcomes: failure shows “演示证据不可用” + “重试示例”; empty shows “暂无演示回执，不等于失败”; stale shows a full timestamp and “旧回执，不能推断当前状态”. Ready restores the fixture. Retry changes only the sample evidence. Show no five-job second dashboard; no credentials, account names, machine paths, real PR titles or user content.

### Keyboard, appearance and accessibility
Every job name is visible without hover and each job has one selection owner. Use real buttons, aria-expanded/aria-controls on disclosures and aria-pressed or aria-current for selection; no nested button elements. Tab follows the declared visual flow, Enter/Space activate, Escape cancels intent/closes the current fold, and focus returns to its opener. On committing, move focus into the retained inline status rather than losing it to a disabled button; on settle, focus the local return control. Use a 2px focus ring with 2px offset in the accent role; no hover-only functions or single-letter global shortcuts. Changes use aria-live=polite and never announce a ticking clock every second.

Support data-theme="light" and data-theme="dark" at the document root; an explicit value overrides prefers-color-scheme, and an absent value follows the system, including changes. There is NO inner appearance toggle. If Coding later supplies a parent appearance-message protocol, validate the documented origin and payload, allow only light/dark, and update the same root attribute; do not invent an incompatible message schema or send external telemetry. The outer chooser owns appearance, viewport and gallery navigation. With prefers-reduced-motion, all transitions become immediate and no spinner/orbit/paper movement is essential; with reduced transparency use the declared opaque fallback. All normal UI text, including metadata, is at least 13px with 1.4 line-height (display lines may use 1.15–1.2). All pointer targets ≥28×28px, default 32px high. Never truncate numbers, timestamps or CJK names with ellipsis; wrap prose, keep numeric tokens intact, and scroll only the bounded selected detail region if necessary. At 1280×800, all five names must remain visible with no page scroll. At 200% zoom use accessible internal scroll rather than clipping, hiding jobs or shrinking fonts.


## Stage 2 handoff
### Canonical five-job fixture (public, simulated; A–E are design references, not UI labels)
Use this exact five-record dataset. Frozen demo clock: **2026-03-16 03:59:20 CST (UTC+08:00)**, not the current time. Every displayed status, timestamp, output and action receipt must be visibly scoped by “演示数据 · 非实时”; no live/online indicators. Keep “模拟” on any subsequently generated receipt. Cadence is a schedule, not proof of actual successful execution.

| Ref | Stable binding ID | Display name, exactly once per default viewport | Cadence | Synthetic last receipt / initial state | Next planned time |
|---|---|---|---|---|---|
| A | linear-bot-bridge | Linear @bot 桥接 | Every 1 min / 每 1 分钟 | 2026-03-16 03:59:00; 示意正常 | 2026-03-16 04:00:00 CST |
| B | my-pr-supervisor | 我的 PR | Every 5 min / 每 5 分钟 | 2026-03-16 03:45:00; 回执较旧，非已证实失败 | 2026-03-16 04:00:00 CST |
| C | pr-auto-review | 特定人 PR | Every 5 min / 每 5 分钟 | 2026-03-16 03:55:00; 合并跳过，非成功/失败证明 | 2026-03-16 04:00:00 CST |
| D | aidata-digest | 每日简报 | Daily 04:00 CST / 每日 04:00 | 2026-03-15 04:00:00; 示例 4/5、阶段 5 警告 | 2026-03-16 04:00:00 CST |
| E | daily-learning | 每日学习推荐 | Daily 04:15 CST / 每日 04:15 | 尚无状态产出；不是失败；每天 3 题候选 → Linear & AIDash | 2026-03-16 04:15:00 CST |

Only D has the five-stage demo. Use **“示意阶段 1” through “示意阶段 5”**, not claims about production stage names; stages 1–4 passed, 5 warning are invented sample data. E has three candidate slots, not five stages. A/B/C have receipt/evidence details, not a copied five-stage template. D source-as-of, if exposed, is synthetic 2026-03-15 03:50 CST; distinguish it from last-run/receipt time. B's age is 14m20s; A's next tick is 00:40; E's next window is 15m40s away. Do not silently sort by unsupported health scores.


### Concrete implementation and acceptance
- Implement the measurements and region ownership above directly as this candidate's self-contained demo; this Stage 1 deliverable contains no executable product/HTML implementation. No production code, package installation, backend changes, service configuration or real-data access is authorized. Owner selection is still pending.
- 默认 B 仅在左纸面命名、四个不同 sibling 在右；执行两次交换和返回后仍五项无重复。模拟核对可撤销；打开 Run Now 后仅运行选中工单，不同时确认核对。
- Required initial state: P0 显示“这份旧回执，需要再核对吗？”；14m20s 作为 15px 说明，不另造数字 hero。右签的告警全部用次级文字而非四个强调色。尚未核对，证据页关闭。
- Treat the canonical table as the single data model. It is not a request to render another table beside the bespoke design. The stable IDs bind the one visible representation per record. Selection never drops any of the five registered jobs from the default view, and none becomes a duplicate summary card. Need-actions remain inside the selected record, never a global second dashboard.
- Exercise default light, default dark, selected evidence-empty/stale/failed, intent cancel, committing double-click and settled return. Assert five unique job selection owners; five display names visible once; only one selected detail/intent surface; no page-level horizontal overflow; zero numeric truncation and no raw localization keys. Inspect actual pixels at 1280×800, keyboard focus order and both accessibility fallbacks; prompt approval does not certify rendered quality.
- No fetch/XHR/WebSocket/EventSource, real issue links, telemetry, local filesystem reads or account data. All evidence is synthesized in memory. Respect a parent appearance message if a validated protocol is later supplied; do not add theme buttons inside the page. Outer portal provides traffic lights, window border and chooser controls. Stop at demo implementation; do not imply this candidate has been selected for the final product.
