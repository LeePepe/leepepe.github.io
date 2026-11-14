# v05 — Corner-Pinned Whisper Orb & Expandable Transcript Ribbon

Design a peripheral companion, not a small app window. The mandated 56px glass orb waits in the lower-right corner; holding it pulls a horizontal transcript ribbon to its left. The desktop's center should remain available for the user's imaginary work. No centered overlay, no bottom-wide dock, no dashboard.

## The corner owns the geometry

Fill the 1280×800 outer chooser macOS canvas with `100vw × 100vh`; the OUTER traffic-light bezel is not part of this page. Start with a solid soft desktop field and only a 56×56px orb at x=1192, y=696, with a 32px right and 48px lower margin. Its center contains the capture SVG, never a Unicode dot. A subdued, two-line native hint immediately above/left of it reads “Hold Option+Space · Text” and “Option+Shift+Space · Todo”; Escape guidance joins this local hint during capture. Hints fade to secondary contrast, never become a page footer. P0 is the orb, and there is no other accented control.

On Listening, the orb's left tangent grows into a 608×92px ribbon at x=640, y=678, ending at x=1248. The orb remains a 56px terminal control in the same fixed position. Reserve the trailing 144px for its control collar so text never goes beneath controls. The 416px text area starts at x=664 and ends at x=1080 inside a **solid** transcript strip, visually joined to the glass control collar only; raw words scroll horizontally only as needed within that single strip, with a full wrap-readable expansion available. Seven bars occupy a 56×28px band at x=1120, y=710, to the left of the orb, with no text beneath them. P1 previous captures are hidden behind a small chevron exposed only after Done. P2 settings reside in the orb's secondary-click menu, also reachable by a visible More button once the ribbon is pinned.

`Command+Shift+R` or “Pin ribbon” locks the result open after Done; the same command retracts it to the orb. Pinned ribbon is the selection surface, not another recorder. `Command+Return` or the “Open workspace” arrow opens a **right-edge document drawer**, x=812, y=104, width=436, height=556, separated 18px above the ribbon. The drawer is solid with a 36px native action toolbar, 28px content insets and a collapsed “Previous captures” accordion at its foot. Its single selected note replaces the current document on row selection. Back/`Command+[` closes the drawer but keeps the pinned ribbon. Fold/retract restores focus to the orb. Do not scatter additional floating windows.

## Atmospheric lens, solid words

Coordinates: **VS-006 Mindful Focus Recovery** with **CL-007 Calm Sky Hue Arc**, using cool rather than butter-cream colors. Taxonomy: visual-style/hero-3d-spatial-canvas, glass-material/glass-refraction-specular, layout-navigation/spatial-scrubbing-toolbars, motion-interaction/gesture-physical-manipulation. **X:** capture→Copy single P0; P1 pin/history; P2 settings. **Y:** leftward ribbon growth and a separate upward right-edge drawer. **Z:** quiet ambient aura, a transparent orb/collar, and solid content planes. No glass transcript cards.

Exact font stack: `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"`. Drawer result 24px/550/33px; ribbon transcript/body 15px/400/23px; controls/history 13px/500/19px; hints/timer 11px/500/16px. Four roles, tabular timer. Spacing cadence is 4px icon-label, 12px related controls, 24px ribbon padding and 48px untouched corner clearance. Drawer insets 28px are larger than its 12px row gaps. Do not use tracked capitals or decorative giant metrics.

Light: canvas #EEF7FA, opaque content #FCFEFF, history selection #E0EFF7, ink #18374B, secondary #516C7B, cyan #006C91, recording #AE3153. Dark: canvas #122435, content #193347, selection #27485E, ink #EDF9FF, secondary #ABC7D7, cyan #7CDBF4, recording #FF9BBA. Polarity is always dark ink on pale solid content in light and pale ink on deep blue solid content in dark. Keep chroma concentrated at the orb; never paint rows with the full hue arc.

A stationary radial aura behind the orb is a smooth sky-to-indigo hue arc, #38BDF8 → #2A6FD6 → #4F46E5, radius 140px, alpha .13 light/.12 dark, no black gradient stops or pulsing breathing background. The orb/collar's distinct optical layer uses white .20 / #3A657C .30 tint, both standard and WebKit `blur(28px) saturate(190%)`, top Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`, a white .30 outer rim and a 0 12px 30px rgba(16,65,91,.18) shadow, dark .32. A broad top-left highlight gives spherical volume without a shiny plastic icon. Group the orb and collar as one sampled glass surface; do not blur through another glass element. Text, SVGs and bars are separate unfiltered foreground. Optional clean Chromium Snell/Fresnel affects the orb's outer 8px only with max 2px displacement, never content. WebKit uses blur plus rim, no noisy caustics. This HTML is an approximation, not falsely native rendering.

On actual window/document blur the orb automatically loses aura and refraction, switches to 110% saturation, tint .74 and rim .20, while committed ribbon text remains. Cancel Listening/Refining on blur and never resume on focus gain. Reduce Transparency makes the orb/collar opaque #E9F3F8/#24475D. Do not expose Active/Matte controls.

## Whisper and keep it

Only the focused page handles Option shortcuts; it does not register global hotkeys. Physical Option+Space keydown snapshots Text intent, Option+Shift+Space snapshots Todo intent, repeated keydowns do nothing, and Space keyup finishes regardless of modifier-release order. Pointer hold on the orb begins immediately with pointer capture; normal release anywhere finishes. Native keyboard Enter/Space activation on the focused orb toggles start/stop for non-hold access. Suppress the synthetic click after pointer hold.

**Idle → Listening:** grow the ribbon leftward in 240ms without moving the orb. Show seven 3px round bars, 3px gaps, envelope 5/9/16/24/16/9/5px at 130ms phase offsets; show Listening and tabular 00:01 as readable text. Reveal synthetic words: “After the sample walk, sketch the riverside route and label the three stops.” **Release → Refining:** keep the ribbon width, settle all seven bars to 5px and show “Tidying your thought” for 950ms. Prevent pin/history/navigation changes from mutating this run. **Done:** ribbon says “Sketch the sample riverside route and label its three stops.” P0 becomes Copy, at the same orb terminal location with a copy SVG and accessible “Copy refined note” label. Copy announces “Copied sample route note”; if clipboard unavailable, pin/open the full text, select it and show “Text selected; press Command+C.” New capture is a quiet secondary action in the pinned collar, preserving the previous committed note in session memory.

Todo intent yields one “Sketch the sample riverside route” task with the folded step “Label three stops.” P0 becomes “Add to Todo”; only activation adds one task to memory, then offers its reversible circular completion button. No task auto-runs. The right-edge drawer's “Previous captures” reveals three synthetic rows; Up/Down selects and Return loads a row into the drawer/ribbon without recording. `Command+Shift+R` pin/retract preserves selected note and focus. `Command+Return` opens the drawer; `Command+[` returns to the pinned ribbon. Escape at rest closes the innermost menu, then drawer, then retracts ribbon; it never deletes committed notes.

Escape while Listening/Refining cancels to the previous result or Idle, invalidates the run token, clears delayed words/refinement callbacks and announces “Capture cancelled” with focus on the orb. Pointercancel, lost pointer capture, page hiding or blur also cancel. Release after any cancellation is inert. Offer a settings-menu local “Refinement unavailable” sample; on failure preserve raw words in the pinned ribbon and show Retry, which performs only local refinement. No error automatically copies or adds data.

## Bespoke controls and safe access

Use inline SVG viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.7`, round caps/joins. Give these exact path d values to the implementer:

| Name | Path d |
|---|---|
| Whisper capture | M10 5a2 2 0 0 1 4 0v7a2 2 0 0 1-4 0V5 M7 10v2a5 5 0 0 0 10 0v-2 M12 17v4 M9 21h6 |
| Pin ribbon | M8 3h8 M9 3v6l-3 4v2h12v-2l-3-4V3 M12 15v7 |
| Open drawer | M4 5h16v14H4z M14 5v14 M7 9l3 3-3 3 |
| Copy | M8 8h12v13H8z M16 8V3H4v13h4 |
| Retract | M6 5l7 7-7 7 M12 12h9 |
| Cancel | M7 7l10 10 M17 7L7 17 |
| Completion ring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |
| More | M5 11v2 M12 11v2 M19 11v2 |

The orb is a semantic button with 56px hit area; other desktop controls default to invisible 32px areas, minimum 28px. Coarse-pointer/touch targets are at least 44px and reflow the pinned collar so they do not overlap. Completion uses a semantic circular button with `aria-pressed`, not a checkbox. Tab order orb/result → pin → workspace → More, then drawer content. Secondary-click actions always have a visible More alternative. Focus is a 2px cyan ring, offset 3px. Announce state changes politely, not every word/bar. Reduced motion removes growth, pulse and bar movement: reveal ribbon instantly, retain seven fixed bars and textual Listening/Refining labels. Regular motion is 240ms critically damped, no floating/bobbing orb. Ensure 4.5:1 text contrast, full shortcut and numeric labels, natural CJK wrapping and a full-text drawer, never inaccessible clipped ribbon text or page overflow.

Keep page-config and outer chooser postMessage theme/platform hooks. Only outer chooser owns appearance/platform/gallery selection. Read baseline/original and baseline/interactive.html without modifications; frozen iPhone composition remains zero top capsule, large single-sentence whitespace, bottom glass sheet, seven-bar hold/release and bottom-leading Fold to Todo List/Settings. No `.caustic-veil`, `repeating-linear-gradient` stripes, shared gray `rich-r3.css`, inner website header, footer disclaimer, Active/Matte controls, 28×28 ruler boxes, raw checkbox inputs or emoji/Unicode control glyphs. Native app menus/toolbars are legitimate. No microphone, network or personal data; use session-memory synthetic notes and explicit user Copy only.

Writer must later demonstrate both intents, corner geometry, release outside/cancel, pin/retract, drawer/Back/history selection, Copy fallback, failure/Retry and automatic blur fallback in light/dark Chromium and WebKit, with keyboard and touch-safe targets. No browser validation is claimed by this design-only artifact.
