# v06 — Dual-Pane Live Raw & AI Refined Glass Workbench

Design a recording workbench whose main experience is the transformation from spoken rough material on the left to a useful document on the right. The two-pane relationship is the mandated identity. This is not a floating quick-capture toy enlarged to window size: it is a solid, spacious desktop writing instrument, with a narrow functional glass bridge at its head.

## Draw the transformation, not a dashboard

The page uses `100vw × 100vh` at 1280×800, framed only by the OUTER chooser's macOS traffic-light bezel. An opaque workbench content area occupies x=96, y=100, width=1088, height=600. Its native 48px action toolbar lies at y=100..148. Two borderless content panes begin at y=184 and end at y=652: left x=128, width=432, right x=608, width=544, leaving 48px for the transformation gutter. Each pane has 24px internal padding and at most two visual groups: label plus one document. The toolbar's leading capture button is the only P0 in Idle/Listening. Seven bars and a timer sit beside it, not centered between two competing CTAs. A subdued horizontal arrow in the gutter communicates direction, not an interactive third pane.

Idle left: “Speak the rough version.” Idle right: a quiet empty document with “A clearer version will appear here.” These are not two boxed cards. Listening fills the left document only. Refining writes the right document in paragraphs, never duplicates the raw text there. Done retreats the left raw document to secondary contrast and promotes the right “Accept refined note” action in the same toolbar P0 slot. No always-tinted action in each pane.

P1 source revisions are folded behind “Source” in the left pane label; `Command+Option+R` toggles its single-active accordion. P2 settings live in toolbar More. Workspace expansion is a genuine editing mode: “Expand workspace” or `Command+Return` at rest grows the content area to x=32, y=40, width=1216, height=720 and reveals an optional 176px leading session-history rail. The raw and refined panes retain a 44:56 share of remaining width with a 32px gutter; recalculate rather than clipping fixed widths. The history rail begins collapsed and is revealed by its toolbar button. Back/`Command+[` returns to the compact workbench and the same selected revision. Selected history loads both versions by capture ID. No second window bezel or website header.

## Tone, metrics and surface polarity

Coordinates are **VS-003 Precision Acoustic & AI Studio** remixed with **VS-002 Warm Editorial & Swiss Ledger** for document content, paired with **CL-002 Warm Ivory Paper / Deep Forest Ink**. Taxonomy: layout-navigation/split-view-master-detail, visual-style/aesthetic-direction-mood, glass-material/vibrancy-legibility-layers, motion-interaction/micro-feedback-haptics-symbols. **X:** capture then Accept is single P0; source/history P1; route/settings P2. **Y:** side-by-side transformation with source accordion and optional history rail. **Z:** one functional glass toolbar over two solid documents. Never blur raw/refined content.

The exact font stack is `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"` throughout; no serif substitution despite editorial pacing. Refined document heading 26px/600/35px; document prose 16px/400/26px; pane labels/actions 13px/600/19px; key hints/timer 11px/500/16px. Four roles; changing digits are tabular. Spacing: 4px icon-label, 12px row gap, 24px pane padding, 48px transformation gutter, 32px between document sections. Maximum prose width is 58 characters; paragraphs wrap naturally. No uppercase telemetry labels.

Light: canvas #F4F1EB, documents #FFFCF6, selected/history #ECEEE4, ink #26372D, secondary #5B685D, forest accent #235D43, recording #B63145. Dark: canvas #171E1B, documents #222C26, selected #324137, ink #F1F4EB, secondary #BBC8B9, forest accent #91D4AA, recording #FF9AA7. Light uses deep green-black ink on warm solid paper; dark uses ivory ink on green-charcoal paper. Refined/right document is one subtle luminance step above raw, not a glass card. The warm brass #8A671F/#E7CA86 may appear as a tiny source-revision marker, never a second accent CTA.

A stationary ambient sage radial wash behind the toolbar spans 640×180px, alpha .09 light/.08 dark. Separate its optical layer: white .23 / #385141 .31 tint, standard and WebKit `blur(28px) saturate(190%)`, exact top Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`, white .26 side rim, soft shadow 0 10px 30px rgba(38,61,44,.12), dark .28. Keep buttons, labels and seven bars as undistorted foreground. Adjacent controls share one optical group and never sample glass through glass. Chromium may add a clean Snell/Fresnel rim displacement no more than 1px, on the toolbar optical background only. WebKit uses clean blur/rim fallback. This HTML optical approximation must not be described as native macOS rendering.

Real document/window blur cancels active capture/refinement, dims toolbar to neutral tint alpha .76 and saturation 110%, top rim .20, removes aura/refraction and keeps committed documents readable. On focus return restore active optics but never resume capture. Reduce Transparency uses opaque #F1F2E9/#2D3C31 toolbar with all text contrast preserved. No Active/Matte UI.

## Material becomes a note

Show native key hints within the toolbar: “Hold Option+Space · Text”, “Option+Shift+Space · Todo”, and during capture “Escape · Cancel”. Shortcuts are focused-sandbox simulations, not system-wide registration. Use physical Space with modifiers, ignore auto-repeat, freeze Text/Todo mode at first keydown, release on Space keyup independent of Option release order. Pointer hold on Capture enters Listening with pointer capture; Enter/Space activation on the focused button gives a non-hold start/stop toggle. Suppress duplicate click after holding.

**Idle → Listening:** show seven 4px rounded bars at 4px gaps and heights 6/12/20/28/20/12/6px, changing at 120ms phase steps. Announce Listening once and show tabular 00:01. Stream synthetic raw text left: “So, for the sample garden, maybe group the seedlings by light, and then write the watering notes before Friday.” No real mic or network. **Release → Refining:** stop raw stream, retain full raw text, change seven bars to 5px and show “Refining structure” for 1000ms. Reveal two right-side paragraphs with a soft opacity change, not fake typing for every character. **Done:** right document reads “Sample garden plan” followed by “Group seedlings by light requirements. Write watering notes before Friday.” P0 becomes Accept refined note. It saves one selected refined document into session memory, shows “Saved Sample garden plan,” and quietly exposes Copy and New capture; no automatic overwrite of a previous accepted note.

Todo mode yields one parent “Prepare the sample garden plan” with three folded substeps: “Group seedlings by light”, “Write watering notes”, “Review before Friday”. The parent Add action remains the sole P0; substeps expand only after explicit disclosure. Checkrings are semantic buttons with reversible `aria-pressed` completion, never checkbox inputs. No AI runner is actually invoked. `Command+Z` undoes Accept/Add without deleting the raw source. `Command+E` focuses the refined document for selection/copy; `Command+C` is handled only with a focused result selection, never hijacked globally. Clipboard denial selects the full refined text and displays “Text selected; press Command+C.” `Command+Return` expands workspace at rest; Accept has its own focused Return action, so the two cannot double-submit.

Source accordion has three local revision rows with timestamps. Up/Down moves one row, Return loads that revision's raw text and derived refined note as a pair; never mismatches sources across captures. Keep the current active recording locked against revision/history changes. Escape at rest closes More, then Source, then expanded workspace, in that order, restoring focus. More offers a seeded “Refinement unavailable” case; a failure preserves raw text and shows Retry on the right rather than a blank result. Retry only re-runs local Refining.

Escape in Listening/Refining invalidates the run token and all pending callbacks, restores the last accepted pair or Idle, announces “Capture cancelled,” returns focus to Capture. Pointercancel, lost pointer capture, page hide and blur use the same path. An ordinary pointer release outside the control still finishes through captured pointer. No stale delayed completion, no lost accepted document, no recording resumed after focus gain.

## Exact line icon vocabulary

All are inline SVG: viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.6`, round joins/caps. Exact path d data:

| Control | Path d |
|---|---|
| Capture | M8 5a4 4 0 0 1 8 0v7a4 4 0 0 1-8 0V5 M5 11v1a7 7 0 0 0 14 0v-1 M12 19v3 |
| Accept | M5 12l4 4L19 6 |
| Source accordion | M5 9l7 7 7-7 |
| Transformation direction | M4 12h16 M14 6l6 6-6 6 |
| Expand workbench | M4 9V4h5 M15 4h5v5 M20 15v5h-5 M9 20H4v-5 |
| History rail | M4 5h16v14H4z M9 5v14 M12 9h5 M12 13h5 |
| Copy | M8 8h12v13H8z M16 8V3H4v13h4 |
| Cancel | M6 6l12 12 M18 6L6 18 |
| Circular checkring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |
| More | M5 11v2 M12 11v2 M19 11v2 |

Default icons 18px in invisible 32×32px desktop targets, minimum 28px, primary Capture 40px. Touch/coarse pointer targets expand to at least 44px with real layout clearance. Give icon labels, 2px forest focus ring plus 3px offset, and a single polite live region for state/save/cancel. Tab order follows toolbar → raw source disclosure → refined document → history if open → More; it must not jump to hidden controls. Reduced motion removes streaming/morph animation and bar movement, shows the raw text at once and seven fixed bars with explicit state text; refinement still has a cancellable state. Normal pane expansion is 220ms critically damped. All text reaches 4.5:1 contrast; no numeric ellipses, no clipped CJK, no page overflow. Longer documents scroll inside their panes with independent visible scrollbars when needed.

Preserve outer page-config and theme/platform message hooks. Do not put theme/platform/gallery-selection controls inside the page. Baseline/original and baseline/interactive.html are read-only; frozen iPhone r3/v02 remains zero top capsule, huge whitespace/single sentence, bottom glass sheet, seven-bar hold/release and bottom-leading Fold to Todo List/Settings. Prohibit `.caustic-veil`, `repeating-linear-gradient` stripes, shared gray `rich-r3.css`, raw checkbox inputs, inner website headers, footer disclaimers, Active/Matte controls, 28×28 ruler boxes and emoji/Unicode glyph controls. Legitimate native app action toolbars are allowed. All records are synthetic session-memory only; no mic/network/personal data or external writes, clipboard only on explicit Copy.

Writer evidence later must include both intents, paired source/refined revisions, Accept/Add/undo, expanded workspace/history round-trip, Copy fallback, failure/Retry, cancel in both transient states, automatic blur fallback and light/dark Chromium/WebKit screenshots at 1280×800. Stage 1 does not claim rendered test success.
