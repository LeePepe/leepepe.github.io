# v01 — Notch-Hugging Liquid Glass Island

Design a macOS acoustic instrument that seems suspended from the upper edge of the display, not a centered dialog. Preserve the mandated notch-hugging identity and live transcription stream. This is Stage 1 design direction for a synthetic, local HTML sandbox; do not interpret this document as production SwiftUI or permission to change the frozen iPhone recording screen.

## The upper-edge composition

The page is exactly `100vw × 100vh`, composed at **1280×800** inside the OUTER chooser's macOS traffic-light bezel. Do not draw another window bezel or gallery header. Use a quiet cool desktop field. At x=480..800, y=0..36 reserve an empty camera-clearance zone: no fake black notch, no text behind the camera. Two short shoulders meet below that zone in one continuous optical instrument, x=410, y=36, width=460, height=76, radius=30. The center holds the single P0 capture target and its seven-bar response. The idle line, “A thought, before it slips away,” sits at x=410, y=144, width=460, aligned left, not centered on the whole desktop.

Listening unfolds one hanging transcript strip from the island's lower lip to x=410, y=124, width=460, height=168. This is an opaque content strip connected visually by alignment, not a second glass lens. Use the same strip for the result, never duplicate live text in another card. Leave the entire lower 60% of the page undisturbed. P1 recent captures stay behind the island's downward disclosure button. P2 routing/settings live in its contextual menu. No visible sidebar initially.

Workspace expansion is a downward reveal, not a zoomed-up pill: `Command+Return` or the “Open workspace” trailing icon after Done unfolds a solid window-content region x=280, y=148, width=720, height=560. Its 160px leading history rail is collapsed to a single “Recent captures” disclosure until requested. The remaining document is the selected result; a 36px native action toolbar contains Back, Copy and More, all subordinate to the selected document action. Back or `Command+[` restores the island and its previous result, focus and selection. No new traffic lights. Selection in the revealed history changes the document, never starts capture; current selection is a subtle luminance band plus a leading rule, not a filled accent pill.

## Coordinate and material lock

Coordinates: **VS-003 Precision Acoustic & AI Studio**, **CL-003 Sonic Cyan / Deep Slate** with a high-key light counterpart. Taxonomy dimensions: visual-style/elevation-shadows-depth, glass-material/glass-refraction-specular, layout-navigation/scroll-pinning-safe-areas, motion-interaction/threshold-commit-safety. **X:** P0 capture then Copy result, P1 workspace/history, P2 settings. **Y:** top-edge hanging disclosure; workspace replaces the transcript instead of stacking modules. **Z:** aura behind optical instrument, transparent functional shell, opaque transcript content above it.

Use the exact native font stack `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"`. Four roles only: thought/result 26px/600/34px, transcript 15px/400/23px, action labels 13px/550/18px, key hints/timer 11px/500/16px (size/weight/line-height). Use tabular numerals for the timer; no decorative tracked capitals. Spacing is 4px icon-to-label, 12px between related controls, 24px content padding and 48px before a new spatial region. Tool padding must be at least its internal 12px gap.

Light: canvas #EEF4F8, opaque content #FFFFFF, main ink #122238, secondary #526276, interactive cyan #006B8F, recording coral #B52D4B. Dark: canvas #101722, content #182331, ink #F0F6FF, secondary #AFBED0, cyan #71D7FA, coral #FF8DA3. Light is dark ink on pale material; dark is light ink on navy material, not white text over transparent wallpaper. At most the one P0 target is strongly tinted. Result and history are solid, borderless luminance tiers.

Separate a stationary radial cyan ambient aura at (640,70), radius 240, opacity .12 light/.10 dark from the island's optical layer. The optical layer uses a white tint alpha .22 light / navy #1E3348 alpha .32 dark, `blur(28px) saturate(190%)` for both standard and WebKit backdrop paths, a 1px rim white alpha .34/.20 and the exact inset top Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`. Soft shadow: 0 14px 36px rgba(20,46,74,.16), dark .30. Put text/buttons in a separate undistorted foreground. Adjacent controls share one optical group: glass never samples glass. Optional Chromium Snell/Fresnel displacement is confined to the background perimeter, maximum 2px, never applied to text, icons or the waveform. Safari uses clean blur/rim fallback. This HTML material is an approximation, not falsely native rendering.

On actual window/document blur, cancel an unfinished recording/refinement, soften shell saturation to 110%, use tint alpha .65 light/.72 dark and a .22 top rim; retain completed text and focus-restoration token. Regain focus without resuming capture. No Active/Matte switches. Reduce Transparency uses an opaque #F4F7FA/#1A2635 shell and keeps contrast.

## Capture choreography and keys

Place real native-style hints inside the island's expanded lip: “Hold Option+Space · Text”, “Option+Shift+Space · Todo”, “Escape · Cancel”; do not use footer chrome. The shortcut works only while this sandbox has focus, never claim system-wide registration. Detect physical Space plus modifiers, snapshot Text/Todo intent at keydown, ignore repeat and release Space to stop. Releasing Option first must not strand recording.

Idle → Listening: hold the P0 button or Option+Space. Pointer down captures the pointer; seven 3px round-ended bars at 4px gaps move deterministically through heights 6/11/19/27/19/11/6px at 100ms steps, with “Listening” and a tabular 00:01 timer. Feed synthetic words into the hanging strip: “Let's move the sample review to Thursday, and bring the checklist.” Release → Refining for 800ms, bars settle to seven 6px marks and label becomes “Refining”; disable duplicate submission. Done replaces raw text with “Move the sample review to Thursday and bring the checklist.” The sole promoted action becomes Copy. Todo intent instead yields one task “Prepare the sample review” with two folded substeps, “Move review to Thursday” and “Bring the checklist”; no automatic completion or execution.

`ArrowDown` when the island disclosure is focused opens the live/result strip and moves focus to its document; `ArrowUp` returns to the island. `Command+Return` opens workspace; `Command+C` copies only when the result document is focused, with selectable-text fallback and “Text selected; press Command+C” if clipboard access fails. Copy reports “Copied sample note” locally. A quiet “New capture” resets without losing the previous result from the session's in-memory recent list. Completion of a Todo uses a **semantic button** with a circular SVG checkring (`aria-pressed`), reversible by pressing it again; never a checkbox input.

Escape in Listening or Refining invalidates the run token, stops all timers, restores the last committed result or Idle, announces “Capture cancelled” and returns focus to P0. Pointer cancellation, lost pointer capture, page hiding and blur take the same cancellation route. Workspace/disclosure navigation is deferred until capture ends. Escape at rest closes the innermost popover first, then workspace; it never deletes a committed note. Accessible Enter/Space activation of the focused primary button is a start/stop toggle alternative to holding; suppress the synthetic click following pointer hold so it cannot start another run.

## Icon drawing contract

All icons are bespoke inline SVG instructions: viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.7`, round caps and joins. Render 18px icons in invisible 32×32px hit areas; never draw hit-area rulers. Exact path data:

| Control | Path d |
|---|---|
| Capture microphone | M9 5a3 3 0 0 1 6 0v7a3 3 0 0 1-6 0V5 M6 10v2a6 6 0 0 0 12 0v-2 M12 18v4 M9 22h6 |
| Unfold transcript | M5 8l7 7 7-7 |
| Open workspace | M4 10V4h6 M14 4h6v6 M20 14v6h-6 M10 20H4v-6 |
| Copy result | M8 8h12v13H8z M16 8V3H4v13h4 |
| Cancel | M6 6l12 12 M18 6L6 18 |
| Back | M14 5l-7 7 7 7 M7 12h13 |
| Todo checkring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |
| More | M5 11v2 M12 11v2 M19 11v2 |

## Accessibility and refusal boundaries

Tab order follows P0 → disclosure → workspace → contextual actions. Give every icon a spoken label, visible 2px cyan focus ring with 3px offset, and a non-color status. Announce state changes politely, not every bar or timer tick. Minimum desktop target 28×28px, default 32px, and 44px for touch/coarse pointers with no overlap. With reduced motion, remove morphs and moving bars; show seven fixed bars plus the state text, no loss of meaning. Otherwise unfold in 220ms, critically damped, no bounce. Text contrast must be at least 4.5:1; wrap long CJK and English, never ellipsize numeric/status content, scroll only within history/document.

Keep outer page-config and theme/platform message hooks intact; only the outer chooser controls theme, platform or gallery selection. No microphone, network, OS injection, personal content or persistence outside session memory; clipboard write happens only after Copy. No inner website headers, inner theme/selection controls, debug Active/Matte controls, 28×28 ruler boxes or footer disclaimers. No `.caustic-veil`, no `repeating-linear-gradient` stripes, no `rich-r3.css` or shared gray-template styling, no emoji/Unicode control glyphs, no raw checkbox inputs. Legitimate native app action toolbars are allowed. The read-only r3/v02 references inform restraint, not markup reuse; never change baseline files. Frozen iPhone composition in baseline/original and baseline/interactive.html stays zero top capsule, huge whitespace/single sentence, bottom glass sheet, hold/release seven bars and bottom-leading Fold unfolding Todo List and Settings.

Downstream acceptance: demonstrate Idle → Listening → Refining → Done in both intents, cancel during both transient states, disclosure and workspace round-trip, selected-result Copy, real focus/blur fallback, keyboard-only operation and light/dark screenshots in Chromium and WebKit at 1280×800. Stage 1 itself claims no rendered validation.
