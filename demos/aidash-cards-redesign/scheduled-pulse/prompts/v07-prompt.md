# v07 — 候选信封 · Three Questions, Two Destinations
Status: Designer-approved for Stage 2 demo implementation; Owner selection pending.
Target: desktop/macOS; 1280x800; scheduled-pulse.
Coordinates: VS-004 / CL-004 / X-CandidateHandoff Y-FolderPocket Z-SolidFolderFunctionalHandle / AppTheme-PulseEnvelope

Candidate only: this is open-direction exploration, NOT final AppTheme selection or production approval. Active route: desktop × visual-style, layout-navigation, chart-dataviz, motion-interaction. VS/CL are reference-family IDs; X/Y/Z and AppTheme names here are explicit candidate-local coordinates, not new global taxonomy IDs. The 1280×800 is **iframe content**, excluding all outer portal window chrome. Do not add a second macOS frame.

## Visual metaphor
五个任务像五只归档信封，只有一封打开。E 的内页让人看懂“会产生三题、送往两处”这一件事，不把三个空候选当作三项失败，也不把两个接收端画成可登录的真实集成。

边距 32px，标题 (32,28) 1216×48。五名签分别位于 x=32/276/520/764/1008、y=104/116/128/140/152，各 240×72，确保名称、cadence 两行和状态第三行均可见；名签绝不互相覆盖。选中内页 (32,248) 1216×488，圆角 16px，padding 24px。内页左侧 688px，右侧收件目标说明 416px，中间留白 64px。三个候选槽在左竖排，各 80px、高间距 12px；末端 15px 一行“交给 Linear & AIDash · 仅模拟”。P0“等待 3 题候选”32px，名称/目的地 15px，其余 13px。

## Single P0 focal point
E 的 3 题候选将交给 Linear & AIDash；目前尚无回执，所以呈“等待候选”而非伪造完成数。

No competing KPI tiles, repeated task strip or second prominent CTA. P0 is a display/decision in the selected record, P1 its single next contextual control, P2 evidence/stages on demand, P3 advanced context omitted from this public demo. One collection of five records is one visual group, not five unrelated modules; cap the overall screen at two content groups plus at most one transient in-context intent surface. 五个名签都能看见，E 下方的候选槽标“候选 1/2/3 · 等待生成（演示）”。不是 0/3 成功率，也没有假问题内容。收件目标仅两行静态目的地说明，不是另一套任务列表。

## P1/P2 folding
E 默认在前景，E 名称只在第五名签，内页没有第二个标题。P1 是内页三个带序号的空槽和两处接收端说明；不显示真实 issue 链接。P2“证据”把整块内页的候选布局替换成单份证据；切回“候选”恢复，不垂直追加。选择 D 才把同一内页改为五阶段，而不是保留三个候选再叠五阶段。其余任务内页仅是简短回执。

Default uniqueness invariant: five distinct selectable job records, each with its display name **once**, not the same name repeated on a summary chip and again in a list and inspector. Selected context is a continuation or replacement projection of that same record, never another named job card or second five-job dataset. Leave job IDs in data bindings, not as UI headings. When a role moves between regions, remove its old occurrence before presenting the new one; accessible names reference the existing visible name rather than duplicating visible labels.

## Color and surface polarity
Warm amber stock / walnut night with brass focus; content stays solid, not translucent parchment.

暖琥珀实体归档纸，暗色是胡桃木色实体；用 12px 错层页边表达 Z 深度，不用玻璃内容卡。

| Semantic role | Light | Dark |
|---|---|---|
| canvas / L0 | #F5EEE2 | #261D14 |
| group / L1 | #FFF8EC | #34291C |
| focus surface / L2 | #FFFDF6 | #443522 |
| ink | #46331C | #FFF4E2 |
| secondary ink | #766044 | #D9C3A2 |
| accent / focus ring | #805016 | #EEC78E |
| on-accent | #FFFFFF | #3D260C |
| separator (not text) | #DDCCB1 | #6C573B |

Status ink pairs (Light / Dark, on normal L0/L1 surfaces only): success #166534 / #86EFAC; warning #92400E / #FCD34D; failure #9F1239 / #FDA4AF. Neutral/unknown uses secondary ink and explicit words; coalesced is neutral. Reserve at least 90% of the viewport for neutral solid surfaces; chromatic accent is for selection/P0 and keyboard focus, never all five jobs. Use text + distinct SVG shapes as well as color. Target normal-text contrast ≥4.5:1 and control/focus boundary contrast ≥3:1; decorative separators may be quieter, never the only affordance. Verify these pairs in rendered light and dark states rather than reducing opacity on text. Use system UI (-apple-system/BlinkMacSystemFont/system-ui) and local system serif/monospace where explicitly specified. No imported fonts. Use tabular numerals for time and ratios. Container padding is never less than internal gap. At most four font sizes per viewport; all non-display text remains ≥13px. Keep evidence within the declared region; do not shrink the entire layout to fit.

## Liquid Glass optical parameters
Only the small “详情/收起” functional handle may use restrained regular-glass optics, never job-name tabs, nodes, charts, candidate slots, inspector content or the canvas. Place the handle within blank canvas space reserved for it, not over readable content, and keep it separate from other controls. Optical design target: IOR 1.45, blur 8px, saturation 108%, rim 0.5px at white 18% Light / 12% Dark; no chromatic fringe, no moving specular sweep. Demo refraction/displacement is explicitly 0px, an approximation, not physical ray tracing; do not introduce SVG displacement to fake it. Use both backdrop-filter and -webkit-backdrop-filter when available. Safari-safe @supports fallback is an opaque L1 surface, separator rim and ordinary ink; no browser-specific url() backdrop filters. Reduced transparency always takes the opaque path; reduced motion removes the 120ms opacity transition. No glass-on-glass or content-on-glass. The default focus/Run Now controls remain solid or outline as specified, not a second glass layer.

## Inline SVG iconography
Use this bespoke 24×24 currentColor stroke semantic icon for 一只容纳三份候选的打开文件夹, only once near the relevant region heading:

```svg
<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h7l2 2h9v11H3z M3 7V4h7l2 3 M7 13h10M7 16h6"/></svg>
```

Other action icons use the same 24×24 viewBox / 1.75px rounded stroke: play triangle for Run Now, simple chevron for disclosure, outlined clock for stale, check for passed, warning triangle for warning, x-in-circle for failed, open circle + question text for unknown. SVGs inherit semantic ink, no gradients/external <use>/external assets. Decorative SVGs are aria-hidden; icon-only buttons receive an explicit readable aria-label and ≥28px target, with adjacent text for consequential actions. Never use emoji as UI substitutes, and do not download an icon set.

## Explicit anti-patterns
Ban .caustic-veil and repeating-linear-gradient zebra stripes; no striped filters, ruler/debug bars (including 28×28 dashed ruler boxes), inner web topbars, inner traffic lights, Active/Matte pills, decorative tracked-capital eyebrows, duplicate gallery/theme/viewport/selection controls, or bottom floating macOS action bar. Legitimate job selection and in-context evidence lenses are product controls, not forbidden gallery controls. No shared grey boilerplate, rainbow card grid, boxed KPI summary, fake live ticker, numeric truncation, raw localization keys, decorative emoji, stock imagery, external fonts/assets, glass content cards, glass-on-glass or opaque imitation system toolbar. No repeated task in a top summary + list + inspector. Never manufacture operational capabilities from this demo or interpret a sample warning as a real incident. Share only resets/state helpers across variants; build each layout, proportions, typography and color system independently, not one dashboard with alternate CSS colors.

## Interaction and states
点击任一名签保持五个名签坐标不动，仅切换最前景内页与一个 2px 选中沿；z-index 只作用于无文字的页边，不遮挡签条。左右键导航名签，Enter 选择。选中 E 后 Run Now 模拟成功，在三个槽内生成“示例候选一/二/三”与“只在本页生成，未发送”回执；这三个演示字符串不是实际学习建议。

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
- 验证五个名签边界互不相交、没有裁切。模拟运行前只有三个等待槽，确认后仅替换这三槽；Linear 与 AIDash 从未变成真实可点击外链或“已投递”承诺。更换任务后原模拟内容仅留于其本地内页。
- Required initial state: 五个名签都能看见，E 下方的候选槽标“候选 1/2/3 · 等待生成（演示）”。不是 0/3 成功率，也没有假问题内容。收件目标仅两行静态目的地说明，不是另一套任务列表。
- Treat the canonical table as the single data model. It is not a request to render another table beside the bespoke design. The stable IDs bind the one visible representation per record. Selection never drops any of the five registered jobs from the default view, and none becomes a duplicate summary card. Need-actions remain inside the selected record, never a global second dashboard.
- Exercise default light, default dark, selected evidence-empty/stale/failed, intent cancel, committing double-click and settled return. Assert five unique job selection owners; five display names visible once; only one selected detail/intent surface; no page-level horizontal overflow; zero numeric truncation and no raw localization keys. Inspect actual pixels at 1280×800, keyboard focus order and both accessibility fallbacks; prompt approval does not certify rendered quality.
- No fetch/XHR/WebSocket/EventSource, real issue links, telemetry, local filesystem reads or account data. All evidence is synthesized in memory. Respect a parent appearance message if a validated protocol is later supplied; do not add theme buttons inside the page. Outer portal provides traffic lights, window border and chooser controls. Stop at demo implementation; do not imply this candidate has been selected for the final product.
