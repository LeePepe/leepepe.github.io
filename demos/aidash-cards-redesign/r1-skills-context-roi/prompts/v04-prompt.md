# v04 — Selective Read Gate · 渐进阅读闸口
Status: Designer-approved for Stage 2 demo implementation; Owner selection pending.
Target: desktop/macOS; 1280x800; skills-context-roi.
Coordinates: VS-003 / CL-003 / X-selective-reading Y-chart-reverse-face Z-solid-studio / AppTheme-ReadGate

## Visual metaphor
An acoustic studio gate that decides how much signal enters, with separate meters for intended reading depth and a violation warning. This is measured usage, not a fantasy execution pipeline.

This is bespoke open exploration, not a frozen product theme. Dimensions: visual-style, color-palette, chart-dataviz, layout-navigation. Numbered VS/CL families follow the design vocabulary; the descriptive X/Y/Z and AppTheme names here are local exploration coordinates, not new global taxonomy IDs. Keep this design’s topology and rhythm independent of the other variants.

## Single P0 focal point
**Deep-read violations · 15%** is the initial one P0. Initial Lens: **Disclosure**. Main verb: **Review selective reading**. The quantity is an observation to inspect, not a fabricated health score. Supporting status is P1; other measures are P2 until their Lens is selected. One primary reading and one filled primary action at a time; do not render twelve equal competitors. P0 action opens a safe local review, never operates on production.

Quantitative design: Plot L0-only 55% and L1-selective 45% as two adjacent bars on a shared vertical 0…100% axis; heights are 154px and 126px within a 280px plot. They describe the two exclusive reading outcomes in this illustrative fixture, not sequential surviving counts. Put deep-read violations on a separate horizontal 0…100% meter, fill 15%, labelled “6 / 40 observed loads; separate flag, may overlap L1”. Avg context 6,800 tok is a compact annotation. Do not add violation width to 55%+45%; do not draw a third L2 funnel stage. The one large P0 is 15%, not the two reading-depth rates.

## P1/P2 folding
Topology: Centered branching reading plane with a shallow left lens index and an inset right intervention column.

Intro x32 y24 w1216 h72. Lens index x32 y120 w160 h648. The reading plane x216 y120 w1032 h648 is one solid stage with 24px padding. Inside it, chart x240 y248 w656 h336 and intervention text x928 y248 w296 h336 share the same surface, without nested card borders. A domain-specific subview row at y192 is 36px high. This is one integrated plane plus navigation, not three floating dashboards.

P1 is the active selection’s window/sample and next safe review. P2 behavior: The 32px “Turn to evidence” button replaces the chart face with a solid definition table in the exact same 656×336 footprint. Use a simple 120ms crossfade, not unreadable 3D text. “Return to chart” restores it; Escape returns and refocuses the opener. Churn/Escapes leaves replace that face. Intervention copy stays in its own column and has only one selected proposal.

Other Lens layouts: Quality uses an eight-consumer strip switchable to Gate/Audit details; Practice uses loads/R1 and execution evidence under a selected skill; Context uses a five-slice stacked bar with tool burn as a separate leaf. Reuse the reading plane geometry, not the visual motif of a funnel for unrelated populations.

P3 source-method details use the same evidence surface, not an unrelated settings screen. Diagram annotations and legends form one group with their chart. Intro is unboxed; no extra framing card. Never add a fourth visual group just to fit coverage.

## Color and surface polarity
CL-003 · acoustic slate / cyan / restrained coral. Every canvas and content region is opaque. Light uses paper with dark ink; dark uses the paired deep surface with bright ink, never an inverted screenshot. Exact local semantic role pairs:

| Role | Light | Dark |
|---|---|---|
| Canvas | #EDF4F7 | #0E1720 |
| Solid content | #FFFFFF | #172630 |
| Elevated/selected solid | #E3EDF2 | #213641 |
| Primary ink | #122632 | #EAF5F8 |
| Inverse/high-key ink | #FFFFFF | #0E1720 |
| Secondary ink | #4C6370 | #ABC4CF |
| Action/focus accent | #075D77 | #8CDEED |
| Ink on action | #FFFFFF | #0E1720 |
| Success text / subtle fill | #176144 / #EAF4ED | #A8DFC3 / #213B31 |
| Warning text / subtle fill | #70470D / #FFF1D6 | #F1CF93 / #3D3020 |
| Error text / subtle fill | #963446 / #FCECF0 | #F0B6C2 / #412832 |

Use these categorical mark colors and solid tint fills for S11, in authentic slice order. Text stays in primary ink on the tint, not white text on a low-contrast swatch. Small lines/bars may use the mark; broad mosaic areas use the solid tint. Selected outline uses action accent plus a contrasting moat.

| Slice | Mark light | Mark dark | Solid tint light | Solid tint dark |
|---|---|---|---|---|
| System / AGENTS | #475569 | #94A3B8 | #E9EBED | #2B3A46 |
| Skills | #6D28D9 | #C4B5FD | #EDE5FA | #333D51 |
| Tool schemas | #0369A1 | #7DD3FC | #E1EDF4 | #274251 |
| Tool results | #B45309 | #FCD34D | #F6EAE1 | #3C4235 |
| Conversation | #0F766E | #5EEAD4 | #E2EFEE | #22454A |

Typography: 48 / 20 / 15 / 13px; system sans with ui-monospace rate labels, deliberate studio pauses; line heights 54 / 26 / 22 / 19px. All metrics use tabular-nums; numeric strings never ellipsize. Maximum four sizes in the viewport. Keep ordinary captions and axes at 13px, line height ≥19px; primary text is reserved for focal values, supporting text uses the secondary role. Spacing tokens 4/8/16/24/32px, with 4px atomic gaps, 16–24px internal padding and 24–32px structural gaps (padding ≥ internal row gaps). Follow the explicit geometry above when it overrides generic spacing. Solid group radius 16px, nested controls 8px; concentric inner radius max(4, outer radius minus padding). Use luminance, not a cage of borders. 1px hairlines only at structural dividers. No decorative shadows; focus is visible in both appearances. A broad diagram tint is not an extra saturated accent. Keep strong accent to selection and primary action.

## Liquid Glass optical parameters
Deliberately no Liquid Glass over these closely spaced scales. All chart, intervention and lens controls are solid, IOR=1, displacement=0px, blur=0px. Safari sees the same surface. Reduced-transparency does not change any data layer; reduced-motion removes the chart-face crossfade and any hover movement. No neon bloom, pulsating background or glass-on-glass.

Glass, if explicitly permitted above, is functional control optics only at Z=10; solid content is Z=0, focus ring Z=20. Do not place data labels or content cards on glass, and never let glass sample another glass layer. Opaque Safari/reduced-transparency fallback must preserve click/keyboard behavior and contrast; no visual feature may be the only state cue.

## Inline SVG iconography
Author inline stroke SVG with viewBox="0 0 24 24", width/height 24, fill="none", stroke="currentColor", stroke-width="1.7", stroke-linecap="round", stroke-linejoin="round". The bespoke domain glyph uses path d="M5 4v16M19 4v16M5 8h7M12 8l-3-3M12 8l-3 3M19 16h-7M12 16l3-3M12 16l3 3". Additional functional paths: evidence circle cx=12 cy=12 r=9 plus M12 11v6 M12 7h.01; disclosure M8 5l7 7-7 7; approval M5 12l4 4L19 6; undo M8 5L3 10l5 5 M3 10h9a7 7 0 0 1 7 7. These describe icons, not a complete HTML scaffold. Use visible text beside core actions; icon-only evidence control gets a 32px target and an accessible name. No external fonts/assets, SF Symbol download dependency or emoji substitutes. Chart geometry is separately quantity-faithful, not an icon repurposed as a fake meter.

## Explicit anti-patterns
No .caustic-veil, repeating stripes, repeating-linear-gradient zebra texture or striped overlays through SVG filters. No inner web topbars, macOS traffic lights/titlebars, Active/Matte pills, 28×28 ruler/debug bars, inner gallery/theme/viewport/selection controls, or floating bottom macOS action bar. The outer portal owns that chrome. No shared grey boilerplate or uniform twelve-metric tile wall. No glass-on-glass or content-on-glass. No numeric ellipsis/truncation (including “…”) or raw localization keys in visible UI; permit label wrapping and full exact numeric values. No chart whose size is decorative rather than proportional, fictitious L2 stage, cache-as-sixth-slice, hidden observed zeros, inflated ROI money claim, causal claim from association, real identities, local paths, external fonts/assets, emoji UI substitutes or actual task dispatch. No duplicate full chart plus a second progress-bar copy of the same dataset. Primary headline plus its one annotated chart is acceptable; avoid repeating every value in cards, legends AND tables.


## Interaction and states
Variant-specific path: Disclosure initial; select Reading depth/Churn/Escapes leaves; flip chart to evidence using a text button; simulate selective-read proposal.

Proposal rationale: Low-ROI Proposals: Atlas “Request reference sections only when needed”. Evidence is Atlas ROI 0.4 plus the separate 15% violation observation; display “Association only; effect not measured”. Approve/defer is a local review simulation and does not change the violation meter.

### Operative controls and states
- Start at the declared initial Lens and selected subview with evidence closed; show the illustrative window and label without adding a health-pill strip. Lens click changes actual content and selected semantics immediately. Use an accessible tablist (aria-selected and associated tabpanels) or the variant’s exposed pocket headers with equivalent tab semantics. Left/right arrows or up/down for vertical rails move between Lenses; Home/End reach first/last; Enter/Space activate. Roving focus never traps Tab. Retain selected skill/subview per Lens for this iframe lifetime only.
- Evidence uses a real button at least 32×32px with aria-expanded and a named controlled region. The variant’s fold/replacement geometry is mandatory. Escape closes it and restores focus; nested disclosures close nearest first. Do not hide essential definitions only on hover. Chart selections have matching labelled buttons or list options; pointer and keyboard expose identical values. Decorative SVG icons are aria-hidden; icon-only buttons have visible tooltip AND accessible name.
- Low-ROI Proposals is a named product region in every candidate. Each proposal includes hypothesis, observed evidence, unknown effect, and a visible “Simulation only; no dispatch” notice. “Review…” is the only filled primary action initially; it opens the local review state in the designated evidence/decision footprint. In review, show “Approve simulation” and quiet “Defer simulation”; the approve button replaces the initial primary rather than adding a second competing CTA. Enter/Space activates only the focused button, never auto-approves on Lens change.
- State machine: suggested → reviewing → approved-simulation OR deferred-simulation; Cancel → suggested. Approve feedback is exactly “演示：已批准此提案；未执行任何任务。” Defer feedback is “演示：已暂缓；未更改数据。” An inline aria-live=polite receipt names the proposal and includes Undo (≥32px). Undo returns it to suggested. The current review status survives Lens changes within memory, but resets on iframe reload. No network, command execution, filesystem write, automation dispatch or storage persistence; do not fake a production run animation or change observed metric values after approval.
- Loading: a bounded 250ms fixture load may show “Loading illustrative observations” with stable region geometry; no shimmering content, invented progressive percentages or indefinite spinner. Reduced motion makes loading text static.
- Empty: no observations means value “Unknown · no observed samples”, sample 0/unknown as appropriate; no 0%/all-clear chart. Preserve Lens navigation and coverage definitions; disable proposal approval when its necessary evidence is absent, with a stated reason. An actually observed numeric zero with nonzero sample (Cedar executions/touch; Shell >10k) MUST remain 0/0% and plot at zero, not become Unknown.
- Stale: fixture state says “Stale illustrative snapshot · last as-of 2026-10-08 00:00 UTC”; retain numbers but visibly mark them non-current. Treat stale as a scenario flag, not wall-clock computation. Proposals can be reviewed/deferred, but simulated approval is disabled until “Reload illustrative fixture” restores the base state.
- Failed: “Illustrative source failed · retained observations are not current health”; keep old observations dimmed but legible and labelled retained, show inline Retry that reloads the LOCAL fixture only, and disable approval. If there are no retained values, show Unknown. Partial coverage is labelled “Incomplete”; row-local missing fields never become 0 or a green badge.
- Stage 2 may select loading/empty/stale/failed/partial through a private test harness initial-state hook, not visible diagnostic buttons or theme controls inside the design. Retry is a legitimate product action; the parent chooser owns appearance and viewport UI.
- Appearance resolves explicit data-theme="light"|"dark" first, then prefers-color-scheme when absent; Coding later binds the parent’s existing appearance-message protocol without inventing an incompatible message name or wildcard trust. No inner theme switch. Every style in the tables is a semantic token, not a second frozen product AppTheme; Owner selection is pending.
- All pointer targets ≥28×28px (use 32px default); main review buttons 36px high. Body/labels/ticks ≥13px. Focus ring is 2px accent with 2px offset and a contrasting opaque moat; keep it unclipped. Tab order follows the reading hierarchy; do not intercept browser shortcuts. At 200% text zoom allow local panel scrolling/reflow, never clip numbers or shrink below the type floor. Respect prefers-reduced-motion and prefers-reduced-transparency; when the transparency media query is unavailable, the opaque fallback is always available without requiring an inner setting.


## Stage 2 handoff
### Public illustrative fixture — implement locally, not from a service
Every visible state carries the persistent text **演示数据 / illustrative**. All skill, workspace, case and tool labels below are invented generic fixtures, not extracted telemetry. Observation window W7 is 2026-10-01 00:00 through 2026-10-08 00:00 UTC (half-open, 7 days); W30 is 2026-09-08 00:00 through 2026-10-08 00:00 UTC. Source as-of is 2026-10-08 00:00 UTC, an explicitly illustrative timestamp. Do not compare it with the wall clock or imply live freshness. “Fresh” means the base fixture scenario, not current production health.

The report has no universal cross-metric sample count. Every evidence fold shows its metric’s window, unit, sample/population, coverage, estimated flag and method/definition. Base coverage is “Illustrative observed” except declared missing fields. Ratios in S2/S4/S6/S7 are stored as 0…1 and displayed as percentages; S11 shares/cache and S12 shares are already percentage points. Never multiply those by 100 again.

| Metric | Complete fixture and definition; use the stated population, not a guessed one |
|---|---|
| S1 · Pin Drift | Snapshot at source as-of; 8 inspected consumers, each with one inspected shared pin in this fixture; 2 outdated pins (Workspace A/B), 6 synchronized (C–H), all-up-to-date=false. The source field is an outdated-pin count, not a commit distance; the one-pin-per-consumer correspondence and sample=8 are explicit fixture assumptions, not a guaranteed production denominator. Version distance unknown. |
| S2 · Gate Catch Rate | W7, 40 gate runs; true-positive catches=8, configuration/rerun noise=4. Catch rate=8/40=20%; noise rate=4/40=10% in this declared fixture method. They are independent observations, not an exhaustive partition; overlap unspecified. Do not label catch rate precision, recall or defect prevention. Metric sample=40. |
| S3 · Skill Health & Evals | Snapshot: 12 inspected skills, audit passes=9; audit sample=12. Eval inventory=48 cases, weekly delta=+6 from a prior inventory of 42; inventory sample=48 cases, NOT 48 successful evaluation runs. Audit failed entries are synthetic items 04/08/12; failure reasons unknown. |
| S4 · Usage & R1 | Three active skills in W7; Delta is idle over W30. Atlas: loads W7/W30=40/120, R1 pass=12/16=75% (review sample=16). Beacon: 28/96, R1=9/10=90% (n=10). Cedar: 12/42, R1 unknown (no reviews, n=0), NOT 0%. Loads are observed events, NOT unique sessions; 7d is a subset of 30d and must never be added to it. Active=3 is not total installed skills. |
| S5 · Unknown / not instrumented | No S5 definition or decoder is present in the bounded source contract. Show “S5 · Not instrumented / definition unavailable” in Quality evidence, value unknown, sample unknown. Never rename R1, proposals, daily populations, or any invented metric as S5. |
| S6 · Load vs Script Touch | W7, separate script observations: Atlas script executions=12, script touch=20% (8/40 eligible load sessions), unpracticed=50% (20/40 eligible sessions). Beacon executions=20, touch=60% (12/20 eligible sessions), unpracticed=25% (5/20). Cedar executions=0 observed, touch=0% (0/12 observed eligible sessions); unpracticed unknown/missing (n unknown). These session denominators are illustrative fixture methods, NOT guaranteed source instrumentation. Execution counts are repeatable events, not touch numerators. Touch is not executions÷loads; touch and unpracticed are not complements and may use different eligibility. Keep S4 event loads/R1 distinct from S6 script practice. Production touch/unpracticed denominator formulas are not exposed by the decoder; preserve “method unavailable” when not supplied. |
| S7 · Disclosure Funnel L0/L1 | W7 Atlas, sample=40 illustrative load observations. L0-only=55% (22/40); L1-selective=45% (18/40), exclusive in this fixture only. Deep-read violation=15% (6/40), an independent flag that may overlap L1; never normalize all three into one 100% stack. Avg context=6,800 tok over those 40 observations. No measured L2 completion count; no inferred L2 conversion or sequential survival claim. |
| S8 · Post-Skill Churn | W7 Atlas: 18 edit events and 6 retry-command events associated with 20 observed post-skill sessions. Sessions may contribute several events. Counts are association after use; no causal treatment effect, before/after improvement, success rate or “wasted effort” is measured. |
| S9 · Escape Attribution | W7 Atlas: 3 [IMPL_BUG] and 5 [SPEC_GAP] escape records. This fixture explicitly declares 8 distinct records and one attribution per record; sample=8. E01…E03 implementation deviation; E04…E08 specification omission. Source decoder supplies attributed counts, not causal proof or guaranteed deduplication. Never sum real populations unless exclusivity is known. |
| S10 · Skill ROI Ranking | W7 reported dimensionless scores: Beacon 1.3, Cedar 0.8, Atlas 0.4; sample=3 scored skills. Sort scores descending for the Ranking view; pin Atlas as the low-score investigation candidate, not an automatic retirement. Formula, score normalization, monetary value, confidence interval and savings counterfactual unavailable. These are fixture reported scores, not an invented model or a percentage. |
| S11 · Context Composition & KV Cache Hit % | W7 sample=20 context snapshots; estimated mean total=50,000 tok per snapshot, not an aggregate over all 20. The FIVE rows below are that same composition. Separate cache population: 100,000 eligible input tokens, 72,000 cache-read tokens → KV Cache Hit 72% (sample=100,000 tokens; cache method is an explicit illustrative fixture). Source cache-denominator formula is unavailable otherwise. Compressed saved tokens=9,000 tok, estimated by a separate illustrative compression comparison; NOT a cache-derived saving, NOT 72% of context, NOT added to total. |
| S12 · Tool Context Burn P95 | W7, sample=120 tool calls across Search/Read/Shell; total=800,000 output-context tokens. Search: 60 calls, total=480,000 tok, P95=18,400 tok/call, calls strictly >10,000 tok=9, token share=60%, associated dominant skill Atlas. Read: 40 calls, total=240,000, P95=12,000, >10,000=4, share=30%, Beacon. Shell: 20 calls, total=80,000, P95=4,800, >10,000=0 OBSERVED, share=10%, Cedar. P95 is the nearest-rank 95th percentile of per-call context-token sizes (sorted index ceil(0.95×n)); fixture values are precomputed, not reconstructed from the mean. Token share is tool total÷800,000, NOT its call share. Dominant skill is association, not causation. No outlier filtering that hides an observed zero. |

S11 authentic five-slice contract — exactly these display names, in this order; no “other”, “reasoning”, “memory” or invented sixth slice:

| Slice | Estimated mean tokens | Share of the same 50,000 tok |
|---|---:|---:|
| System / AGENTS | 6,000 | 12% |
| Skills | 4,000 | 8% |
| Tool schemas | 8,000 | 16% |
| Tool results | 20,000 | 40% |
| Conversation | 12,000 | 24% |
| Total | 50,000 | 100% |

The Total is a checksum label, NOT a sixth slice. Cache hit and saved tokens are separate measures, NOT additional slices. For a standard 500px composition bar, widths are 60/40/80/200/120px with no data-reducing gaps. Put small-slice names and exact token values in one text legend, not a second set of progress bars. Variant-specific area geometry supersedes this bar only for the initial chart explicitly designed above. Missing any slice produces “Incomplete composition” and no normalized 100% claim; never rescale the remaining pieces to fill the whole.

Daily populations are an optional Practice evidence fold, not S5: synthetic Day 2026-10-07, Atlas attribution 4 calls/2 sessions, tool-source 6/3, slash-source 2/1. They may overlap; never sum across sources or add them to S4 loads. Their source windows/samples remain row-local. Do not show actual log paths, user identities, account names or workspace identifiers.

### Complete Lens contract and S1–S12 traceability
The product Lenses are **Quality / Practice / Disclosure / Context**. They are real mutually exclusive analytical perspectives, not inner gallery controls. The variant-specific placement, initial Lens, chart and evidence mechanism above are authoritative; do not flatten them into a shared dashboard shell. The active Lens’s primary stage replaces the previous one: never keep the original giant P0 above a second competing Lens hero.

| Metric | Reachable location and minimum retained information |
|---|---|
| S1 | Quality → Pins → consumer evidence: behind count, synchronized state, inspected consumers and metric provenance. |
| S2 | Quality → Gates: catches, noise, total runs and both separately defined rates. |
| S3 | Quality → Audit: passed/inspected; eval case inventory and weekly delta as distinct units. |
| S4 | Practice → Usage: active count, 30d idle names, each skill’s 7d/30d loads and R1 pass with separate review sample. |
| S5 | Quality → Definitions & coverage: explicit unknown/not-instrumented label; no fabricated value or renamed R1. |
| S6 | Practice → Script practice: per-skill executions, touch rate, unpracticed rate, independent denominators/missing methods; show Cedar’s observed execution zero. |
| S7 | Disclosure → Reading depth: L0-only, L1-selective, independently measured deep-read violations, mean context tokens; explicitly no L2 count. |
| S8 | Disclosure → Churn: edit and retry-command counts, post-skill session sample and association-only explanation. |
| S9 | Disclosure → Escapes: both [IMPL_BUG] and [SPEC_GAP], distinct definitions, sample and non-dispatching case evidence. |
| S10 | Practice → Ranking: three reported scores, descending score order, diagnosis “effect unknown”, load/R1 evidence accessible by row. Formula unavailable is visible in evidence. |
| S11 | Context → Composition: exactly five named slices with counts/shares/estimated total; KV Cache Hit % and compressed saved tokens separate with independent methods and samples. |
| S12 | Context → Tool burn: each tool’s calls, total tokens, P95, >10k call count, token share, associated dominant skill and provenance. Retain the zero-outlier Shell row. |

Non-initial Lens rendering is also decided here. For any table use one semantic table with identical header/body column geometry, never independently flexed rows. A Practice Usage/Script table uses columns Skill 26%, Loads 7d/30d 18%, R1 16%, Script executions 16%, Touch 12%, Evidence 12%; reserve 32px targets, wrap headers, align numeric cells right. Unpracticed and diagnosis live in row evidence, not a seventh crammed column. Ranking can replace that table, not duplicate it. Quality subviews are single-active; Disclosure’s Churn/Escapes are single-active tables with Name 40% / Counts 40% / Evidence 20%. Metric values always have their units. Context Composition uses the five-slice bar specified above unless this variant explicitly uses an area atlas; Tool burn uses the declared three-row zero-based P95 plot with an evidence fold for counts/share/total. Short content labels wrap naturally; all normal UI, footnotes and axis labels remain at least 13px. Do not shrink values to fit.

### Stage 2 measurable acceptance — not a claim that UI has already passed
1. Implement only a self-contained public demo, with embedded synthetic fixtures, inline SVG and system fonts. No private paths, data-source reads, analytics, external asset fetches, production APIs or real telemetry. Coding implements the decisions here, not a generic gallery starter. Do not copy one variant’s layout CSS into the other nine and recolor it. No production code is requested by this prompt.
2. Render iframe CONTENT at 1280×800 CSS px. Verify the declared coordinates, chart dimensions, type floor, target sizes, safe 24/32px outer insets and no outer horizontal/vertical overflow in base state. No browser/window/device chrome inside. At most three visual container groups per pane, including any opened evidence; navigation labels do not become metric cards. Evidence may scroll locally within its declared fixed footprint. If translated text wraps, grow the row within that footprint or scroll locally; never place actionable text under another region.
3. Click and keyboard-test all four Lenses, the domain subviews in the coverage table, one evidence fold, all accessible chart selections, and a full proposal review→approve→undo→defer cycle. Confirm numbers never change after approval and no requests/dispatch/storage writes occur. Confirm focus returns correctly after Escape and all inactive panels are inert. Verify metric window/sample/definition is reachable for every S row, including S5 unknown.
4. Check arithmetic: S11 6,000+4,000+8,000+20,000+12,000=50,000; 12+8+16+40+24=100%. S12 totals 60+40+20=120 calls; 480,000+240,000+80,000=800,000 tok and shares 60+30+10=100%. S7 L0/L1=100% in the fixture; its 15% violation rate stays independent. Distinguish S4 from S6, reported ROI from a financial return, cache hit from compression saved tokens, and a missing R1 sample from a zero pass rate.
5. Capture both light/dark base, empty, stale and failed states (8 real screenshots); separately exercise loading/partial and reduced-motion/transparency. Inspect Safari/WebKit geometry and any declared optical fallback. Assert text ≥4.5:1 contrast, non-text controls/selection ≥3:1, and all full numbers visible. Chart tint alone is not a text background substitute; use semantic ink on tint. Document actual measured outcomes later; this Stage 1 prompt supplies acceptance, not fabricated screenshot evidence.
6. Stop for TL/Owner if implementation needs to change domain meaning or a declared composition. No final variant selection, AppTheme freeze, rollout, production mutation or dispatch is authorized. Owner selection remains pending after these ten explorations.

