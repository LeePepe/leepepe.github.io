# Native components — final independent source and static review

Review surface: `a7ca241db98513581487d02f20bd6e4a660de162` → `a870b9cac06a90f50155e226d2ba167af78ef8f6`, committed task delta only, in the isolated task worktree. The worktree was clean at inspection. This is an independent reviewer record; the reviewer did not edit product code, build, test, operate the simulator, inspect CI gate state, commit or push. Source Standards and task-intent passes were separate, sequential passes; no additional reviewers were spawned.

## Result and scope

**Bounded PASS for the reviewed source delta and actual static presentation of Button, Toggle and TextField.** No remaining actionable source or static visual blocker was found at this SHA. This is not full interaction/accessibility acceptance, minimum-OS certification, shipping approval or gate approval. Motion evidence is separate and was not awaited for this report.

Authority: repository `AGENTS.md`, root `docs/architecture/tech-context.md`, leaf `docs/architecture/native-design-kit/tech-context.md`, shipped `ai/` contract, and the user's `docs/prompts/native-components-design-lead.md` from the original checkout. No active Spec Kit artifacts or constitution were supplied/discovered; the user prompt and repository red lines define intent and constraints. The design documents distinguish Apple recommendations, SwiftUI API facts and team choices, and record Finesse v0.20.0 at `5050b6c71e27b829d1b3087d2be889d29c60db00`.

The discovery helper mechanically marked paths unmapped because it resolved leaf `owns` patterns relative to the nested context directory and scanned the ignored `.shared-ci` checkout. Manual routing against the root table resolves every tracked changed path: `Sources/**`, `Tests/**` and `ai/**` belong to the single NativeDesignKit layer; `CHANGELOG.md` and `docs/**` are declared support exclusions. This is not an unresolved product ownership/dependency finding. No local cross-layer dependency is added. Coverage is degraded only for absent Spec Kit artifacts, not for missing applicable task authority.

The 22 changed files were covered: the three control implementations; the three focused boards, shared review scaffold and catalog routing; UI/render tests and fixture membership/README; the three required native-host design test files; consumer contract; changelog; baseline and three component design documents. The underlying prerequisite PR stack was outside this review.

## Standards axis

NativeDesignKit: **0 findings, worst = none.** Production changes retain real SwiftUI Button, Toggle and TextField controls. No UIKit/AppKit production dependency, business screen/data, local color table, fallback theme, dependency range or token-error conversion was introduced. DesignTokens remains exact 0.1.1; the unreleased style provider is explicitly fixture-only. Button's public `role`/activity behavior is documented in `ai/CONTROLS.md` in the same delta.

Button forwards native roles, uses the supplied destructive token pair, keeps native bezel padding system-owned, puts the minimum target inside the label, and disables the actual button while loading. Symmetric adjacent indicator slots preserve centered resting text; replacing-label presentation centers the icon-only specimen. The textless indicator alone caps Dynamic Type at `.large`; action text remains unrestricted.

Toggle retains a Boolean binding and native switch style. Its growing label/minimum target stays inside the native label. Enabled/disabled text uses explicit tokens, without multiplying opacity across the native switch a second time. There is no replacement activation gesture or synthetic accessibility state.

TextField retains its native string binding, rounded-border editing, Return submission and disabled semantics. Local native appearance is derived from the explicit theme. Its simultaneous target-to-focus adapter requests native focus while preserving native selection; required host tests exercise outside-bezel targeting, caller `.focused` set/clear/observation, disabled blocking, word selection and Return. These artifacts were reviewed as source, not rerun.

## Spec/task-intent axis

**0 source findings, worst = none.** Scope is limited to the requested components and synthetic contexts. The design documents account for all eight Finesse states without inventing Toggle success/loading or library business validation. Native semantics replace web pseudo-classes. The fixture uses persistent labels/helpers and cause-plus-correction text with a symbol; hidden message measuring copies are accessibility-hidden. Shared file membership includes all focused boards and tests in the appropriate targets.

Final fixture correction `a870b9c` exposes the complete validation section after submission using the scroll reader, without dismissing focus. The UI source checks message visibility above the keyboard and helper/error offset relative to the field, accommodating intentional viewport scrolling. The absolute-screen-position assertion was not simply removed to hide the problem.

## Static visual assessment

**Button:** primary/secondary/plain/icon hierarchy is clear without an oversized desktop text button. Resting labels and the icon center appropriately. The accessibility3 loading image now has a compact spinner and clear separation from the full action label. Idle/loading/saved stills show consistent action geometry. Cancel/destructive roles are visually distinct. The iPhone floating Glass context has recognizable underlying content, readable text and clearance from the final document sentence; the macOS fallback is explicitly labeled. The large Chinese action wraps fully. The macOS viewport clips the localized section below its bottom, so the iPhone images carry that boundary evidence.

**Toggle:** on/off is distinguishable by thumb position as well as tint on iPhone. Disabled-on/off remain subdued but legible and positionally distinct. Trailing alignment and label/helper hierarchy are consistent. The large Chinese title and helper wrap without collisions. Compared with the former macOS inline switches, the full-width row composition is clearer and aligns switches consistently. The non-key bitmap's neutral switch tint is not evidence for active-window coloring or disabled runtime behavior.

**TextField:** the lighter native bezel and compact desktop proportions improve the former heavy custom border. Persistent labels retain meaning when placeholders disappear. Filled and disabled values remain distinguishable. Chinese labels/helpers grow completely; the native single-line value's hidden remainder is not proven editable by a still. The final error screenshot shows the whole sentence “Title is empty. Enter a title, then press Return.” and symbol above the software keyboard while the caret remains. The clean focused image contains the normal native keyboard, without the earlier onboarding sheet. `Draft` while the error remains is intentional validate-on-resubmit behavior documented in the board; the submitted image shows `Submitted: Draft` and restores the helper. Native placeholders are faint, especially in dark iPhone presentation; persistent labels/helpers carry purpose. No measured contrast compliance is inferred.

Earlier findings are closed at this source/capture set: undocumented role contract, off-center resting Button content, document/control overlap, oversized desktop spinner/plain typography, accessibility-size spinner overflow, keyboard-obscured error feedback and keyboard-onboarding contamination. The actual final images, rather than a test-pass claim, support these closures.

## Evidence provenance and comparison limits

Metadata: Xcode 27.0 (27A266a), Swift 6.4, DesignTokens exact 0.1.1. iPhone captures use iPhone 18 Pro / iOS 27.0, actual XCUIApplication screenshots. macOS captures use macOS 27.0.1 and a 480×1000-point native NSHostingView bitmap. The lead pins `final2` to target `a870b9cac06a90f50155e226d2ba167af78ef8f6`.

Before captures use iPhone fixture source `270cf2b1fa0fa2e1af53957735f5be9824cb7aba` and macOS fixture source `de78891b5c784398a8f78c1560f2ae4cf06f0b46`. Platform, device/viewport and appearance match the corresponding after set. Fixture labels, helpers, state grouping and neutral context also changed, so these comparisons show the resulting component-plus-review-board presentation, not a pure pixel regression with identical content. The style provider source is `18c979c62e28c005eb3b988fcaacd343e5359d66`, JSON SHA256 `772a99933fb7f2cee3fc19e2c72f2e7357464e6c3d9960d5b676a27f5f240eeb`, unreleased and fixture-only.

`review-*` images are configured state-board previews, including forced accessibility3 on iPhone. `interaction-*` stills are reported actual action-triggered captures. The macOS renderer deliberately selects bordered fallback, not compositor Glass. Its `large` files visually have the same desktop typography as ordinary files and do not establish enlarged desktop text.

## Actual images personally opened

Final images below are relative to this gallery’s `after/` directory (31 images):

```text
iphone/review-Button-light-top.png
iphone/review-Button-dark-top.png
iphone/review-Button-dark-lower.png
iphone/review-Button-large-top.png
iphone/review-Button-large-lower.png
iphone/interaction-Button-floating.png
iphone/interaction-Button-loading.png
iphone/interaction-Button-saved.png
mac/review-Button-light.png
mac/review-Button-dark.png
mac/review-Button-large.png
iphone/review-Toggle-light-top.png
iphone/review-Toggle-dark-top.png
iphone/review-Toggle-large-top.png
iphone/review-Toggle-large-lower.png
iphone/interaction-Toggle-on.png
iphone/interaction-Toggle-off.png
mac/review-Toggle-light.png
mac/review-Toggle-dark.png
mac/review-Toggle-large.png
iphone/review-TextField-light-top.png
iphone/review-TextField-dark-top.png
iphone/review-TextField-large-top.png
iphone/review-TextField-large-lower.png
iphone/interaction-TextField-focused.png
iphone/interaction-TextField-error.png
iphone/interaction-TextField-filled.png
iphone/interaction-TextField-submitted.png
mac/review-TextField-light.png
mac/review-TextField-dark.png
mac/review-TextField-large.png
```

Before images below are relative to this gallery’s `before/` directory (12 images):

```text
iphone/review-Button-light-top.png
iphone/review-Button-dark-top.png
mac/review-Button-light.png
mac/review-Button-dark.png
iphone/review-Toggle-light-top.png
iphone/review-Toggle-dark-top.png
mac/review-Toggle-light.png
mac/review-Toggle-dark.png
iphone/review-TextField-light-top.png
iphone/review-TextField-dark-top.png
mac/review-TextField-light.png
mac/review-TextField-dark.png
```

## Engineering evidence, separately reported

The lead reports `scripts/verify --all` passing with 42 macOS and 38 iOS package tests, five focused iOS UI tests passing, and the macOS render matrix captured. The reviewer did not execute or independently establish those results or any gate state. They do not substitute for the visual observations above or fill the runtime gaps below.

## Explicit remaining acceptance gaps

- Continuous press/loading/switch/focus motion has not yet been independently reviewed in this report. Recording/frame assessment is separate; static endpoints do not establish transition quality or event timing.
- macOS evidence is a non-key native-host bitmap: live compositor Glass, active-window tint, native focus-ring visibility, hover, shortcuts and Tab traversal remain unreviewed. Native-host event tests are separate from a live desktop session.
- No VoiceOver or Full Keyboard Access navigation, rendered contrast measurement, Increase Contrast, Reduce Motion or Reduce Transparency runtime acceptance is claimed.
- Chinese IME composition, editing/scrolling the hidden remainder of the long field, and minimum iOS 15/macOS 12 runtime remain unverified.
- The large-type validation error while the software keyboard is open is not demonstrated. Large static labels/helpers alone do not establish that boundary.

These are explicit evidence limits, not inferred passes or a request to expand the component scope. Source Standards: 0 findings, worst none. Source task-intent: 0 findings, worst none. Static presentation: bounded PASS for the actual images listed, with the runtime/interaction coverage limits preserved.
