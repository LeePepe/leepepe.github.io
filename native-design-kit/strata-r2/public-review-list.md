# Independent List visual review

**Visual fidelity: PASS. Theme/source compliance: PASS for the reviewed candidate-provider scope.** No open List findings remain at `fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3`.

All **35 final actual images** were personally inspected: five palettes × light/dark × Glass/solid/forced reduction, plus disabled, read-only, settled selection, narrow accessibility and actual-system reduction. Surface hierarchy, palette variation, typography and selection match the approved reference and accepted Button. The complete narrow title/supporting sentence, checkmark + 已选 and count are visible. The stale selection-metadata observation **LIST-CAP-01 is closed**.

Supplied evidence: **15/15 runtime tests passed**, zero failed/skipped; **510 matrix contrast checks**, minimum **5.3569:1**; **61 extra-state checks**, minimum **5.6116:1**; no contrast failures. All ten solid/forced-fallback comparisons are identical in the specimen region. Actual Settings reduction followed **0 → 1 → 0**, with restored SwiftUI full transparency asserted.

Representative actual images:

- [Glass](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-blue-light-glass.png)
- [Dark palette](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-purple-dark-glass.png)
- [Narrow accessibility](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-accessibility-narrow.png)
- [Settled selection](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-interaction-selection.png)
- [Actual system reduction](list/fdb7494f9e2de5ef7a477b6a7e61f13909e39ee3/list-system-reduced-transparency.png)

Reference `b4bff430517ed2e2944f814d8b5ab89a1866ee33`; accepted Button `0b1a92ef7713a9520d59f2ffb26c03e7f10854cc`; foundation `ad3ddc73e069d136590ccb6f033faac2d43e33d7`; exact provider `0c38a28e56c5326a0ed9141db2a03d446e27acb3`. **Provider 0.2.0 remains an unpublished local candidate**; remote resolution, publication, release readiness and required gates are separate.

This review covers iPhone 18 Pro / iOS 27.0 Simulator renderings. It does not establish observed hover/pointer, focus/keyboard, VoiceOver, physical-device, minimum-OS or native macOS acceptance. Extra-state markers were visually inspected; numerical marker sampling comes from the matrix report. The reviewer ran no builds/tests/CI, edited no source and read no implementer self-verdicts. Card final review is pending.
