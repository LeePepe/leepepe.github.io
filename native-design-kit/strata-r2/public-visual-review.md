# Independent final Card and List visual review

**Card R5 and List R3 both pass visual fidelity and theme/source compliance for the supplied iOS captures and exact candidate provider.** No open findings or material coverage gaps remain.

| Component | Frozen source | Visual fidelity | Theme/source | Independent image coverage |
| --- | --- | --- | --- | --- |
| Card R5 | `ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7` | PASS | PASS | 51 images, personally viewed by fresh R5 reviewer |
| List R3 | `fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3` | PASS | PASS | 35 images, personally viewed by the prior independent R3 reviewer; result preserved |

The final Card assessment confirms the approved 32pt shell / 24pt reading plane / 16pt nesting, restrained Glass, readable semantic typography and five real surface families. Solid and forced/actual-system reduction preserve layout, palette and semantics while removing material decoration. The narrow statistics-header observation **CARD-VIS-01 is closed**: whole-word wrapping at narrow width and a complete stacked Synthetic data disclosure at accessibility3. Caller-owned actions and complete large-text content are visible across complementary scroll captures.

List retains R3's accepted neutral selected surface, checkmark + 已选, caller-owned identity/selection and readable disabled/read-only states. The complete narrow accessibility copy, marker and count are visible. **LIST-CAP-01 remains closed** in the settled selection image. List has not been re-reviewed or reimplemented by the R5 Card reviewer; its result, numbers and limitations are inherited from the independent R3 report.

| Supplied exact-head evidence | Card R5 | Preserved List R3 |
| --- | --- | --- |
| Runtime tests | 21 passed, 0 failed/skipped | 15 passed, 0 failed/skipped |
| Matrix contrast | 420 checks; minimum 6.0386:1 | 510 checks; minimum 5.3569:1 |
| Other contrast | 8 legacy checks; minimum 5.3399:1 | 61 extra-state checks; minimum 5.6116:1 |
| Contrast failures | 0 | 0 |
| Forced fallback | 10 sampled surface comparisons, delta 0 | 10 specimen-region comparisons, 0 changed pixels |
| Actual Settings | 0 → 1 → 0; restored SwiftUI OFF asserted | 0 → 1 → 0; restored SwiftUI full asserted |

Card additionally has two actual-system landmark deltas of 0, eight legacy inner/outer fallback deltas of 0 and outer Glass deltas 10/8/7/7. All 51 Card raw PNGs match their exported XCTest attachments, and matrix/system PNG hash bindings were checked. Numerical methods were inspected without rerunning them. Card fallback comparisons sample landmarks; List's reported specimen-region identity is a separate R3 measurement.

Representative actual images:

| State | Card | List |
| --- | --- | --- |
| Glass | [Blue light](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-strata-blue-light-glass.png) | [Blue light](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-blue-light-glass.png) |
| Dark palette | [Purple dark](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-strata-purple-dark-glass.png) | [Purple dark](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-purple-dark-glass.png) |
| Narrow/accessibility | [Narrow](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-specimen-narrow.png) · [Accessibility statistics](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-specimen-accessibility3-bottom.png) | [Complete narrow accessibility](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-accessibility-narrow.png) |
| Interaction result | [Caller action](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-specimen-action.png) | [Settled selection](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-interaction-selection.png) |
| Actual system reduction | [Card](card/ae42cb0923a1a5b90d5ad2e47de2bf3b9c04f2e7/card-strata-blue-light-system-fallback.png) | [List](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-system-reduced-transparency.png) |

Full component reports: [Card](public-review-card.md) · [Preserved List R3](public-review-list.md) · [Combined evidence and image hashes](public-visual-review.json). The original List-only reports remain unchanged; their earlier Card-pending note is superseded here by the final R5 verdict.

Reference `b4bff430517ed2e2944f814d8b5ab89a1866ee33`; accepted Button `0b1a92ef7713a9520d59f2ffb26c03e7f10854cc`; foundation `ad3ddc73e069d136590ccb6f033faac2d43e33d7`; exact provider `0c38a28e56c5326a0ed9141db2a03d446e27acb3`. Accepted Button remains the consistency reference. **Provider 0.2.0 is an unpublished local candidate.** These verdicts do not establish public dependency resolution, publication, release readiness or required remote checks.

Both reviews cover supplied iPhone 18 Pro / iOS 27.0 Simulator renderings. Neither establishes observed hover/pointer, focus/keyboard, VoiceOver, physical-device, minimum-OS or native macOS acceptance. Contrast checks sample actual composites using the documented fixture methods; they do not certify arbitrary caller backdrops or overrides. List extra-state markers were visually inspected; their numerical marker coverage comes from the matrix report. No builds/tests/CI, simulator operations or source edits were performed by the final Card reviewer. Root owns gallery publication and PR updates.
