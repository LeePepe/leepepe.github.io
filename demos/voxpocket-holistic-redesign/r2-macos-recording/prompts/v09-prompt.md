# v09 — Keyboard-First Minimalist HUD

A typist's acoustic instrument: a small action matrix anchored toward the upper-left, with a precise result pane that exists only when needed. Preserve the mandated compact 28×28px button-matrix identity and zero-mouse key paths. The 28px measurement is an invisible hit-target floor, never a ruler drawing. Do not copy a terminal window or invent a browser command dashboard.

## An instrument with a folded document

At 1280×800 the page fills `100vw × 100vh` inside the OUTER chooser's macOS traffic-light bezel. Do not add a titlebar or a second set of traffic lights. Place the HUD at x=176, y=128, width=288, height=184, radius=18. It has a 24px native status line, a 3-column × 2-row icon matrix with 32×32px cells and 12px gaps at x=196..316, y=176..252, and a narrow 92px key legend to its right. The matrix contains Capture, Text intent, Todo intent, Recent, Workspace and More. Only Capture is promoted; other icons have secondary ink. The two intent controls are legitimate app commands, not gallery selection controls; their mutually exclusive state uses a tiny leading indicator and a spoken selected label, no equal-weight accent fills.

Single P0 is Capture, becoming Copy or Add at Done. The matrix's physical cells are invisible, not outlined little boxes. Seven 2px bars with 3px gaps fit a 44px status area above the matrix and never become a third row of buttons. Leave the lower 360px of desktop untouched until workspace expands. Idle has no result card. The 92px legend uses deliberate multiline key hints: break long chords after a plus sign and put their action labels on the next line, retaining the complete chord in the accessible name. Its 144px height runs y=152..296; never ellipsize or shrink the hints. In expanded workspace, move the full legend into the document's 36px native action toolbar instead of cramming text into the 56px rail.

Listening reveals one opaque result band to the HUD's right: x=496, y=128, width=544, height=184, padding=24. It holds raw words, then the refined result in the same footprint; no simultaneous raw/refined duplication. P1 Recent is a single-active accordion replacing that band with a four-row single-selection list. P2 routing/settings is a More popover, never another always-visible region. `Command+K` focuses the matrix, with roving focus and an accessible toolbar label “Capture commands.”

Workspace expansion via Workspace or `Command+Return` transforms the matrix into a **56px leading command rail** at x=176, y=128, height=544, and unfolds a solid 808×544px document to its right at x=252, y=128. The six command cells remain in the same semantic order but become one vertical stack. P1 Recent becomes an overlay list replacing the document while open, not a second sidebar. Back/`Command+[` restores compact HUD and selected result. Preserve focused command identity across this topology change. No bottom toolbar, no desktop-filling generic app shell.

## Lock the precision vocabulary

Coordinates: **VS-007 Swiss Chrono & Avionics Telemetry**, **CL-008 Avionics Navy / Linear Indigo**. Taxonomy: component/toolbars, visual-style/concentric-radii-borders, layout-navigation/spatial-scrubbing-toolbars, glass-material/vibrancy-legibility-layers, motion-interaction/reduced-motion-transitions. **X:** Capture→Copy/Add one P0; intent/history P1; settings P2. **Y:** roving command matrix, replace-in-place result/Recent lens, then a leading rail. **Z:** restrained aura behind a transparent functional HUD; solid result/document/list content above. Never blur document content or nest sampled glass.

The exact font stack is `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"`. Result title 20px/550/28px; document text 15px/400/24px; action/tool labels 13px/550/19px; key legend/timer 11px/500/16px. Four roles; tabular digits, no fake terminal monospace font or tracked capital labels. Rhythm is 4px icon-label, 12px matrix gaps, 24px HUD/document insets, 32px HUD-to-document gap. Maintain padding at least as large as internal gaps. Do not shrink hints below 11px to fit extra controls.

Light: desktop #EFF2F8, solid result #FCFDFF, selected row #E6EAF7, ink #26314D, secondary #55637C, indigo #5055AF, recording #B83553. Dark: desktop #131B2B, result #202C43, selected row #303F5D, ink #EFF4FF, secondary #B7C4DC, indigo #B0B5FF, recording #FF9BB5. Light uses dark ink over pale solid result content; dark uses pale ink over navy solid content. The key legend stays readable but never as contrast-heavy as the result. Reserve saturation for P0 and the thin focus/selection indicator.

A stationary indigo radial ambient aura, radius 180px centered at (300,200), opacity .09 light/.10 dark, is distinct from the optical HUD/rail shell. Shell tint is white .22 / #415276 .30; use standard and `-webkit-backdrop-filter` `blur(28px) saturate(190%)`, exact Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`, side rim white .26 and shadow 0 12px 32px rgba(32,45,77,.15), dark .30. Matrix icons, legend and bars are unfiltered foreground, no nested glass buttons. Optional clean Chromium Snell/Fresnel max 1px displacement belongs only on the HUD/rail perimeter, not on content or key hints. WebKit falls back to clean blur/rim. HTML approximates Liquid Glass; do not falsely claim native macOS rendering.

Automatic real window/document blur cancels unfinished capture/refinement and removes aura/refraction, then uses saturation 110%, tint alpha .78 and rim .20. Keep completed results, selected intent and roving-focus token. Focus regain restores optics without capture. Reduce Transparency uses an opaque #EDF1F9/#2C3B59 functional shell. No manual Active/Matte controls.

## The complete no-mouse route

Keep these native hints readable in the HUD legend and in expanded rail tooltips: “Option+Space · Text”, “Option+Shift+Space · Todo”, “Escape · Cancel”, “Command+K · Commands”. These shortcuts work only with page focus, never real global registration. Physical Space plus Option snapshots Text or Shift+Todo at first keydown, ignoring repeat; Space keyup finishes independently of modifier-release order. The visible Text/Todo commands set intent for the next pointer or toggle capture, while the two Option chords explicitly override that next-run intent. A mode change cannot alter an active recording.

`Command+K` focuses the last matrix cell. ArrowLeft/Right moves by column and Up/Down by row with wrap; Home focuses Capture, End focuses More, Enter activates the focused command. In the expanded vertical rail, Up/Down moves sequentially and Left/Right does nothing. Tab leaves the nonmodal toolbar for result/document, never traps the user in the matrix. Use an actual roving-tabindex toolbar model, not an ARIA grid full of fake form cells. Native Enter/Space activation on the Capture button toggles start/stop as an alternative to holding. Pointer hold on the same button captures the pointer, begins immediately and finishes on ordinary release anywhere; suppress post-hold click.

Idle → **Listening:** reveal the right result band, stream synthetic words “For the sample release, compare the draft, fix the headings, and prepare a short summary.” Seven 2px round bars with 3px gaps run through 4/8/13/20/13/8/4px heights at 110ms phase intervals. Show Listening and tabular 00:01. Release → **Refining:** retain raw words, settle seven bars to 4px, show “Refining sample note” for 700ms; disable duplicate capture/commit. **Done:** replace raw words with “Compare the sample draft, fix its headings, and prepare a short summary.” P0 changes to Copy. With result focused, Return copies; explicit Copy reports “Copied sample release note.” Clipboard denial selects the full result with “Text selected; press Command+C.” Do not hijack Command+C outside focused result selection.

Todo mode yields one parent “Prepare the sample release summary” with folded actions “Compare draft”, “Fix headings”, “Write summary”. P0 becomes Add 1 task. Activation adds one in-memory parent by capture ID, never duplicates it; its steps unfold via ArrowRight only when the task disclosure has focus. Completion uses semantic circular button checkrings with reversible `aria-pressed`. `Command+Z` undoes the last explicit Add/completion. No real runner starts. New capture is a quiet contextual command after Done, preserving accepted results in the four-item synthetic Recent history.

Recent opens with the current row selected, Up/Down changes selection, Return loads and returns focus to result. Escape closes the list without changing the prior selection until Return has committed it. Workspace/`Command+Return` unfolds the document rail; Back/`Command+[` returns. More includes a local seeded unavailable-refinement case; preserve raw words on failure and offer Retry, which only re-runs local Refining. No user should require a pointer to recover.

Escape in Listening/Refining has priority: invalidate run token, stop every word/refinement timer, restore previous Done or Idle, announce “Capture cancelled” and focus Capture. Pointercancel, lost capture, page hiding and blur take the same route. A late release/callback after cancel does nothing. During a transient run, matrix navigation may move focus to Cancel but no history/intent/workspace action may silently commit or mutate the run. At rest Escape closes More, then Recent, then expanded workspace, never deletes a committed note.

## Exact miniature SVGs

Inline SVG viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.7`, round caps and joins. Render 16px marks; do not substitute keyboard glyph fonts or emoji. Exact path d values:

| Matrix/control | Path d |
|---|---|
| Capture | M10 5a2 2 0 0 1 4 0v7a2 2 0 0 1-4 0V5 M7 10v2a5 5 0 0 0 10 0v-2 M12 17v4 M9 21h6 |
| Text intent | M5 5h14 M12 5v14 M8 19h8 |
| Todo intent / completion ring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |
| Recent | M4 8a8 8 0 1 1-1 6 M4 3v5h5 M12 7v5l3 2 |
| Workspace | M4 5h16v14H4z M9 5v14 |
| More | M5 11v2 M12 11v2 M19 11v2 |
| Copy | M8 8h12v13H8z M16 8V3H4v13h4 |
| Cancel | M6 6l12 12 M18 6L6 18 |
| Back | M14 5l-7 7 7 7 |

Matrix desktop targets are invisible 32×32px areas, never smaller than 28×28px; no ruler, dashed frame or dimension labels. Coarse-pointer/touch mode expands cells to 44×44px and increases HUD height to 208px, moves result/document down if necessary, without shrinking content or overlapping targets. Completion is a semantic button, not a checkbox input. Every icon has a spoken label and visible native key-equivalent tooltip on hover/focus. Focus ring is 2px indigo, offset 3px; selected intent is announced separately from keyboard focus. One polite state live region, no timer/bar announcements. Reduced motion removes HUD-to-rail morphs, streaming and bar movement: use direct layout changes, seven fixed bars and textual Listening/Refining. Normal expansion 180ms critically damped. All text at least 4.5:1 contrast; preserve whole numeric values, shortcut labels and CJK wrapping; use internal document scrolling, no page overflow.

Preserve page-config and outer theme/platform message hooks. Only outer chooser owns platform/theme/gallery selection. Frozen baseline/original and baseline/interactive.html remain read-only: iPhone r3/v02 retains zero top capsule, large whitespace/single sentence, bottom glass sheet, seven-bar hold/release and bottom-leading Fold unfolding Todo List/Settings. Prohibit `.caustic-veil`, `repeating-linear-gradient` stripes, shared gray `rich-r3.css`, inner website header, footer disclaimer, Active/Matte controls, 28×28 ruler boxes, raw checkbox inputs and Unicode/emoji control glyphs. Native command toolbar/navigation is legitimate. No microphone/network/personal data or external writes; only synthetic session memory and explicit Copy.

Writer evidence must later include a complete no-mouse Text and Todo route, matrix/rail roving focus, Recent selection/cancel, Add/undo, workspace/Back, failure/Retry, cancel in both transient states, blur fallback, touch-target adaptation and light/dark Chromium/WebKit screenshots. Design prose is not proof of rendered tests.
