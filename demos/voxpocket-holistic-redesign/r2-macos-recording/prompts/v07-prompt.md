# v07 — Bottom-Edge Full-Bleed Desktop Glass Dock

Make the lower edge of a desktop recording canvas into a broad, continuous optical instrument. This is the mandated 120px full-bleed dock and an intentional proportional homage to frozen r3/v02, not a row of mobile navigation tabs. Above it there is only one sentence, spacious enough to read across a room. No floating pill and no persistent side panes.

## A stage above an instrument

Use `100vw × 100vh` at 1280×800 inside the OUTER chooser's macOS traffic-light bezel. Do not draw another bezel, titlebar or website header. The top 680px is a solid, borderless reading stage. Place the sentence at x=180, y=252, width=920, maximum three lines, left-aligned. The initial text is “Make room for one clear thought.” Keep all upper controls absent so the desktop stage stays quiet.

The functional glass dock occupies x=0, y=680, width=1280, height=120, flush to the lower and side boundaries, with only its top two corners rounded at 28px. Its P0 capture button is x=1136, y=712, 56×56px. Seven bars and timer live at x=48, y=722. Between them is a low-contrast native hint line: “Hold Option+Space · Text    Option+Shift+Space · Todo    Escape · Cancel.” A leading Fold button at x=32, y=744 is visually subordinate and must not collide with bars; allocate separate 44px columns to Fold and waveform, moving the waveform to x=104 when Fold is visible. This is a task-local Owner-mandated bottom capture instrument, **not desktop bottom navigation**. Never add tabs or a floating bottom app toolbar.

P1 source/history is behind Fold. Clicking Fold or `Command+Shift+U` raises a **solid 188px source tray** above the dock, x=0, y=492, width=1280; the hero stage recomposes to y=168..428 rather than being covered. Tray has a 32px native action row and one horizontal, single-selection recent-capture strip. Selecting a capture replaces the stage sentence and highlights only that strip entry; no duplicate result card. P2 settings live in Fold's trailing More popover. Fold's tray is one optional group, not a permanent dashboard.

“Open workspace” after Done or `Command+Return` expands upward: the stage becomes a solid single-column 880px-wide document at x=200, y=96, height=536, while the same dock remains attached at the bottom. The tray switches to a left-edge outline INSIDE this document only when requested, not another floating panel. Back/`Command+[` returns to the sentence composition with tray expansion and selected capture intact. Only one logical capture/result action exists as layout changes.

## Visual grammar

Coordinates: **VS-008 Editorial Poster Block**, controlled rather than loud, paired with **CL-008 Editorial White / Cobalt**. Taxonomy: visual-style/aesthetic-direction-mood, glass-material/liquid-glass-primitives, layout-navigation/scroll-pinning-safe-areas, typography-copy/scale hierarchy and motion-interaction/reduced-motion-transitions. **X:** capture→Copy sole P0; P1 folded source tray; P2 More. **Y:** full-width vertical compression/reflow, then document expansion upward. **Z:** ambient edge light behind functional glass, solid stage/tray content. Glass never belongs to sentence, source rows or documents.

Exact font stack: `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"`. Stage sentence 38px/550/49px; document text 18px/400/29px; controls/source entries 13px/550/19px; hints/timer 11px/500/16px. Four roles; tabular timer, no tracked capitals or enormous decorative wordmarks. Spacing: 6px within a control, 18px capture cluster inset, 36px between dock clusters, 72px stage top/bottom breathing room. Dock outer padding is 32px horizontally and 28px vertically, greater than its 18px internal gaps. Do not let a control's clickable region reach the frame edge.

Light colors: canvas #F7F9FD, solid document/tray #FFFFFF, selected source #E7EEFA, main ink #182B46, secondary #52647B, cobalt #155EBA, recording coral #B72E48. Dark: canvas #111B2E, document/tray #1A2941, selected source #293D5D, ink #F3F7FF, secondary #B3C4DF, cobalt #8CBFFF, coral #FF98AB. Surface polarity is pale solid content/dark ink in light and navy solid content/pale ink in dark; never white labels on a merely clear dock. Chroma covers only the capture/result target and small state accents, not the whole stage.

A separate, stationary ambient radial aura is centered at (1110,800), radius 360px, cobalt alpha .12 light/.10 dark. The optical dock layer uses white alpha .24 / #395579 alpha .32 tint; both standard and WebKit backdrop filters are exactly `blur(28px) saturate(190%)`. Add the exact Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`, white .26 side/rim highlights and soft upward shadow 0 -12px 40px rgba(27,58,101,.12), dark .30. The foreground buttons/bars/hints remain a separate undistorted layer; never apply filter to the dock's entire content subtree. Group all adjacent glass controls in one sampled optical shell. Optional Chromium clean Snell/Fresnel refraction is perimeter-only, max 1.5px, and must not distort content. Safari/WebKit uses clean blur and top highlight. This is an HTML approximation, not falsely native rendering.

On real document/window blur, cancel unfinished capture/refinement, suppress aura/refraction and use neutral tint .78, saturation 110% and top rim .20; preserve committed notes. Restore only optics on focus regain. Reduce Transparency uses an opaque #EFF3FA/#273C5B dock. No Active/Matte debug controls.

## The complete capture phrase

The shortcut path is local to the focused sandbox, never an actual system-wide registration. Physical Space plus Option starts Text, with Shift starts Todo; snapshot intent at initial keydown and ignore repeat. Release Space to finish even if modifiers were released first. Pointerdown on P0 captures the pointer and starts Listening; ordinary pointerup anywhere finishes. Focused Enter/Space activation offers a toggle start/stop alternative; suppress the click generated after pointer holding.

Idle → **Listening** replaces the sentence with synthetic words: “For the sample exhibition, choose six sketches and write a short introduction.” Show seven 4px round-ended bars at 4px gaps, envelope 6/11/19/30/19/11/6px, changing at 120ms phase intervals. Show Listening and tabular 00:01, not only coral feedback. Release → **Refining** freezes the phrase, shortens all seven bars to 5px and shows “Making it clear” for 900ms. Reject repeated submit and freeze tray selection. **Done** replaces the phrase with “Choose six sketches and write a short introduction for the sample exhibition.” P0 changes to “Copy refined note” in the same trailing dock slot. Explicit Copy reports “Copied sample exhibition note”; clipboard denial selects the full stage/document text and says “Text selected; press Command+C.” No automatic copying on release.

Todo intent yields one parent “Prepare the sample exhibition” with folded steps “Choose six sketches” and “Write a short introduction.” The same P0 slot becomes “Add to Todo.” Add creates exactly one task in session memory; the source tray can reveal its two steps with semantic circular button checkrings. Check/uncheck is reversible, with a consequence such as “1 of 2 sample steps complete”; no raw checkbox inputs or automatic AI execution. Quiet New capture keeps accepted notes in source history. `Command+Z` undoes the last explicit Add or completion, never removes raw text.

`Command+Shift+U` opens/closes source tray. With the strip focused, Left/Right moves the single selected capture and Return opens its document in the stage; do not hijack text-selection arrows inside the document. `Command+Return` expands workspace, `Command+[` returns, and Escape at rest closes More, then tray, then document workspace in order. Settings include a seeded local “Refinement unavailable” case; failure preserves raw text and offers Retry in the stage. Retry re-enters local Refining without recapturing.

Escape in Listening/Refining cancels with highest priority, invalidates the run token, clears word/refinement timers, restores the prior Done state or Idle and focus to P0, and announces “Capture cancelled.” Pointercancel/lost capture, page hiding and blur do the same. Late keyup or delayed callbacks after cancellation are inert. Navigation never silently commits an unfinished recording.

## Marks, access and non-negotiables

Use inline SVGs with viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.7`, round caps and joins. Exact path d:

| Control | Path d |
|---|---|
| Capture | M9 5a3 3 0 0 1 6 0v7a3 3 0 0 1-6 0V5 M6 10v2a6 6 0 0 0 12 0v-2 M12 18v4 M9 22h6 |
| Fold source tray | M5 15l7-7 7 7 M5 20l7-7 7 7 |
| Copy | M8 8h12v13H8z M16 8V3H4v13h4 |
| Expand document | M5 9V4h5 M14 4h5v5 M19 15v5h-5 M10 20H5v-5 |
| Back | M14 5l-7 7 7 7 M7 12h13 |
| More | M5 11v2 M12 11v2 M19 11v2 |
| Cancel | M6 6l12 12 M18 6L6 18 |
| Circular checkring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |

Capture is 56px, Fold 44px, remaining controls invisible 32px desktop targets with minimum 28px. Touch/coarse pointer targets are at least 44px and reflow clusters without overlap. Checkrings are semantic buttons with `aria-pressed`. Tab follows Fold → source if open → document → capture/result → More, with hidden tray controls removed from focus order. Use 2px cobalt focus rings with 3px offset, spoken icon labels, one polite state live region and non-color feedback. Reduced motion removes tray travel, text streaming and bar movement: use instantaneous layout or 100ms fade plus seven fixed bars and state text. Normal expansion 240ms critically damped, no bounce. Text contrast at least 4.5:1; numbers and key hints never ellipsize, long text/CJK wraps, long documents scroll inside the stage rather than overflowing the frame.

Keep page-config and outer theme/platform messaging intact; the outer chooser alone owns theme/platform/gallery selection. Frozen baseline/original and baseline/interactive.html are read-only: iPhone r3/v02 stays zero top capsule, large whitespace/single sentence, bottom glass sheet, hold/release seven bars and bottom-leading Fold unfolding Todo List and Settings. Ban `.caustic-veil`, `repeating-linear-gradient` stripes, shared gray `rich-r3.css`, inner website headers, inner gallery switches, Active/Matte controls, 28×28 ruler boxes, footer disclaimers, raw checkbox inputs and emoji/Unicode glyph controls. Legitimate native document actions are allowed. No mic/network/personal data or external writes; only synthetic session memory and explicit Copy.

Downstream evidence must show dock geometry, both intent journeys, source strip selection, document/Back, Add/completion/undo, Copy fallback, failure/Retry, cancel in Listening and Refining, focus/blur and keyboard-only operation in light/dark Chromium and WebKit. This is a prompt, not rendered test evidence.
