# v06 — 回执账簿 · The Coalesced Receipt
Status: Designer-approved for Stage 2 demo implementation; Owner selection pending.
Target: desktop/macOS; 1280x800; scheduled-pulse.
Coordinates: VS-002 / CL-002 / X-SkipMeaning Y-ReceiptLeaf Z-InverseSolidReceipt / AppTheme-PulseLedger

Candidate only: this is open-direction exploration, NOT final AppTheme selection or production approval. Active route: desktop × visual-style, layout-navigation, chart-dataviz, motion-interaction. VS/CL are reference-family IDs; X/Y/Z and AppTheme names here are explicit candidate-local coordinates, not new global taxonomy IDs. The 1280×800 is **iframe content**, excluding all outer portal window chrome. Do not add a second macOS frame.

## Visual metaphor
像一册已经盖好回执的登记簿：左边确认每个任务在哪里，右边只解释被指向的那一份结果。“合并跳过”是一种独立结果，不是红色失败卡也不是绿色成功奖章。

总外边距 32px，顶端标题占 48px。双页区域 (32,104) 1216×632，左右分别 608px 与 576px，中间书脊留白 32px。左页内边距 24px，共享 Grid 列为名称 248、cadence 168、查看 144（总 560px）；表头 48px，五行各 104px，底余 16px。右回执内边距 32px，顶部结果句 32px/1.2，正文 15px/1.5，label 与等宽时刻 13px；右页不再放任务标题。两页均 6px 小圆角，无穿孔/锯齿/厚阴影。

## Single P0 focal point
C 的合并跳过不是失败；单张大回执解释这个结果，不制造未证实的重试需求。

No competing KPI tiles, repeated task strip or second prominent CTA. P0 is a display/decision in the selected record, P1 its single next contextual control, P2 evidence/stages on demand, P3 advanced context omitted from this public demo. One collection of five records is one visual group, not five unrelated modules; cap the overall screen at two content groups plus at most one transient in-context intent surface. C 选中；右反相纸显示“重复意图已合并”，次行“本条不是失败，也不证明执行成功”。没有巨型 exit 0 或绿色完成对勾。Run Now 是右上角 120×32 的轮廓按钮，不与结果语句争主导。

## P1/P2 folding
C 默认指向右页；左账簿仅给名称与 cadence，第三列是“查看回执”按钮，不重复右页结果或时刻。P1 为右页一段“演示中同一启动意图已合并”的解释；不宣称真实锁、PID 或实际运行中的兄弟进程。P2“证据”替换该段并露出模拟 event kind 与时间；“需要处理”为空时只写“没有演示待办”，不加大空态插画。D 被选中才有五阶段折签。

Default uniqueness invariant: five distinct selectable job records, each with its display name **once**, not the same name repeated on a summary chip and again in a list and inspector. Selected context is a continuation or replacement projection of that same record, never another named job card or second five-job dataset. Leave job IDs in data bindings, not as UI headings. When a role moves between regions, remove its old occurrence before presenting the new one; accessible names reference the existing visible name rather than duplicating visible labels.

## Color and surface polarity
Ivory and forest ledger with an inverse forest/pale receipt; the focal content intentionally flips polarity.

关键差异是 L2 反相实体纸：Light 为森林色纸浅字，Dark 为浅象牙纸深字；不是把文字放在玻璃或照片上。

| Semantic role | Light | Dark |
|---|---|---|
| canvas / L0 | #EDEEE7 | #171D17 |
| group / L1 | #F8F9F1 | #232D22 |
| focus surface / L2 | #183524 | #EAF0D8 |
| ink | #233926 | #F1F5E9 |
| secondary ink | #52644C | #BECCB3 |
| accent / focus ring | #2C6035 | #BDE0A0 |
| on-accent | #FFFFFF | #20351B |
| separator (not text) | #C9D0BD | #4E6047 |

Inverse receipt exception: on-focal ink = #F1F5E9 / #183524; on-focal secondary = #C7D7C2 / #3F5E3A (Light / Dark). On the inverse L2 receipt use only these inks for all text and glyphs; status meaning comes from words and shape, not the ordinary colored status inks. Keep normal ink/secondary ink on L0/L1 only.

Status ink pairs (Light / Dark, on normal L0/L1 surfaces only): success #166534 / #86EFAC; warning #92400E / #FCD34D; failure #9F1239 / #FDA4AF. Neutral/unknown uses secondary ink and explicit words; coalesced is neutral. Reserve at least 90% of the viewport for neutral solid surfaces; chromatic accent is for selection/P0 and keyboard focus, never all five jobs. Use text + distinct SVG shapes as well as color. Target normal-text contrast ≥4.5:1 and control/focus boundary contrast ≥3:1; decorative separators may be quieter, never the only affordance. Verify these pairs in rendered light and dark states rather than reducing opacity on text. Use system UI (-apple-system/BlinkMacSystemFont/system-ui) and local system serif/monospace where explicitly specified. No imported fonts. Use tabular numerals for time and ratios. Container padding is never less than internal gap. At most four font sizes per viewport; all non-display text remains ≥13px. Keep evidence within the declared region; do not shrink the entire layout to fit.

## Liquid Glass optical parameters
Explicitly NO Liquid Glass. This design reads receipts, schedules and evidence; a refractive substrate would compete with its chosen visual metaphor and harm small-text legibility. All content and functional controls are opaque semantic surfaces. Optical parameters: blur 0px, saturation 100%, IOR 1.0, refraction/displacement 0px, no backdrop-filter and no faux specular shader. Safari fallback is therefore the exact same opaque treatment, not a degraded screenshot. Reduced transparency is identical; reduced motion removes the nonessential 120ms opacity change. No content-on-glass and no glass-on-glass.

## Inline SVG iconography
Use this bespoke 24×24 currentColor stroke semantic icon for 登记簿内的一张结果回执, only once near the relevant region heading:

```svg
<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3h14v18l-3-2-4 2-4-2-3 2z M8 8h8M8 12h8M8 16h4"/></svg>
```

Other action icons use the same 24×24 viewBox / 1.75px rounded stroke: play triangle for Run Now, simple chevron for disclosure, outlined clock for stale, check for passed, warning triangle for warning, x-in-circle for failed, open circle + question text for unknown. SVGs inherit semantic ink, no gradients/external <use>/external assets. Decorative SVGs are aria-hidden; icon-only buttons receive an explicit readable aria-label and ≥28px target, with adjacent text for consequential actions. Never use emoji as UI substitutes, and do not download an icon set.

## Explicit anti-patterns
Ban .caustic-veil and repeating-linear-gradient zebra stripes; no striped filters, ruler/debug bars (including 28×28 dashed ruler boxes), inner web topbars, inner traffic lights, Active/Matte pills, decorative tracked-capital eyebrows, duplicate gallery/theme/viewport/selection controls, or bottom floating macOS action bar. Legitimate job selection and in-context evidence lenses are product controls, not forbidden gallery controls. No shared grey boilerplate, rainbow card grid, boxed KPI summary, fake live ticker, numeric truncation, raw localization keys, decorative emoji, stock imagery, external fonts/assets, glass content cards, glass-on-glass or opaque imitation system toolbar. No repeated task in a top summary + list + inspector. Never manufacture operational capabilities from this demo or interpret a sample warning as a real incident. Share only resets/state helpers across variants; build each layout, proportions, typography and color system independently, not one dashboard with alternate CSS colors.

## Interaction and states
点击左行/其按钮更新同一右页，左侧选中以 leading 2px 线和 aria-current 标记。右页证据折签开启后焦点转到页内 heading，Esc 返回摘要。Run Now 若生成新模拟回执，用“本次模拟”折签替换原右页，旧的合并结果仅在历史折签中保存，不修改真实 Job 状态。

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
- 右页全程不重写任务名/cadence；左右列宽由一个 Grid 定义，表头行共用几何。验证合并跳过、失败、无回执三种文字不会被同一个绿点替代；反相纸的所有正文采用 on-focal 墨色。
- Required initial state: C 选中；右反相纸显示“重复意图已合并”，次行“本条不是失败，也不证明执行成功”。没有巨型 exit 0 或绿色完成对勾。Run Now 是右上角 120×32 的轮廓按钮，不与结果语句争主导。
- Treat the canonical table as the single data model. It is not a request to render another table beside the bespoke design. The stable IDs bind the one visible representation per record. Selection never drops any of the five registered jobs from the default view, and none becomes a duplicate summary card. Need-actions remain inside the selected record, never a global second dashboard.
- Exercise default light, default dark, selected evidence-empty/stale/failed, intent cancel, committing double-click and settled return. Assert five unique job selection owners; five display names visible once; only one selected detail/intent surface; no page-level horizontal overflow; zero numeric truncation and no raw localization keys. Inspect actual pixels at 1280×800, keyboard focus order and both accessibility fallbacks; prompt approval does not certify rendered quality.
- No fetch/XHR/WebSocket/EventSource, real issue links, telemetry, local filesystem reads or account data. All evidence is synthesized in memory. Respect a parent appearance message if a validated protocol is later supplied; do not add theme buttons inside the page. Outer portal provides traffic lights, window border and chooser controls. Stop at demo implementation; do not imply this candidate has been selected for the final product.
