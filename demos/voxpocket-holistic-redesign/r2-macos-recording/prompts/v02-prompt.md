# v02 — Floating Glass Pill + Workspace Split Dock

Build the desktop extension of the frozen r3/v02 recording idea: a small free-floating optical pill becomes the hinge between an expansive sentence canvas and a split desktop workspace. The metaphor is a paper slip placed above a desk edge. Do not reuse the iPhone layout literally or create a universal gray card dashboard.

### Spatial score, 1280×800

Use `100vw × 100vh` inside the outer chooser's 1280×800 macOS traffic-light bezel. The bezel already supplies framing; no duplicated browser header or traffic lights. Initial quiet canvas: a single sentence at x=224, y=252, width=832, maximum two lines, with at least 160px clear space above it. The glass pill is x=510, y=506, 260×64px, radius=32. A 48px capture button lives in its trailing end, a seven-bar feedback group in the leading end. This is the one P0 instrument. Keep histories and routing absent, not muted dummy columns.

A small leading Fold control reveals the **workspace split dock**. `Command+Shift+D` does the same. In 260ms the floating pill docks into the functional bottom edge of an opaque workspace occupying x=96, y=100, width=1088, height=620. The attached dock is 88px high, flush with the workspace's lower boundary at y=632..720; it is an Owner-mandated recording instrument, NOT a bottom navigation/tab bar. The content above divides at x=800: left is the broad selected-note editorial page, right is a narrower folded “Recent” ledger exposed only after Fold. A vertical 24px gutter separates these solid content regions; no glass content cards. Native document actions sit in a compact 36px top toolbar, not a fake website header. P1 recent notes are single-selection rows; P2 Settings and route choices live behind More. The workspace contains at most the selected document, optional recent ledger and functional capture dock.

When Fold closes, the workspace collapses back toward the pill's original center and restores the same sentence. Selected history survives the round-trip; changing history does not start recording. While recording, Fold is unavailable with the label “Finish or cancel capture first.” Do not create two capture buttons when the pill is docked: move one logical control and keep its focus identity.

### Look: luminous paper, not frosted content

Lock **VS-005 Zen Paper Checklist × CL-006 Pure Paper / Sky Blue**, with the acoustic seven-bar signature retained. Taxonomy: visual-style/aesthetic-direction-mood, glass-material/liquid-glass-primitives, layout-navigation/split-view-master-detail, motion-interaction/drag-drop-spatial-choreography. **X** single capture→Insert result action; history P1, settings P2. **Y** Fold converts free pill to an attached split-workspace dock. **Z** low ambient light, grouped glass controls, solid sentence and ledger planes. The mandated bottom capture dock is a local exploration exception to the general desktop no-bottom-navigation convention.

Exact font family: `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"`. Set hero sentence 32px, weight 550, line-height 42px; selected document body 17px/400/27px; toolbar and row titles 13px/550/19px; hints/timer 11px/450/16px. Four roles; do not invent additional eyebrow labels. Digits are tabular. The rhythm is 6px within icon-label pairs, 18px internal padding, 36px section separation and 72px around the sentence. Keep labels sentence case.

Light palette: canvas #F5F7FA, content #FFFFFF, selected row #EAF1FA, ink #182B43, secondary #53657A, accent #2167BC, listening #B62E4B. Dark palette: canvas #151C28, content #1C2635, selected row #26364B, ink #EEF5FF, secondary #B0BED1, accent #8CBFFF, listening #FF93AA. Keep solid surfaces tonally close, no dark heavy box borders. Light has pale solid content with dark ink; dark flips both surfaces and ink, never simply inverts images.

Behind the pill/dock, create a static radial sky aura centered under the capture button with a 160px radius, alpha .13 light/.10 dark. It is separate from the transparent optical layer. That optical layer has a white alpha .25 tint in light, #2A3F5C alpha .34 in dark; standard and `-webkit-backdrop-filter` are exactly `blur(28px) saturate(190%)`. Use the top Fresnel `inset 0 1px 0 rgba(255,255,255,.75)`, a side rim white alpha .28 and soft shadow 0 12px 32px rgba(25,55,90,.16), dark .32. A bright upper arc fades before reaching the text. Foreground labels, bars and icons are crisp, undistorted siblings above the optical layer. Do not sample one glass control through another: the pill/dock is one grouped material. Chromium may add a clean perimeter-only Snell/Fresnel refraction of 1.5px maximum, never on content; WebKit gets clean blur and rim. State honestly that HTML is an approximation, not native macOS glass rendering.

Native focus/blur optics are automatic: when document/window focus is lost, cancel pending capture/refinement, remove aura, change shell saturation to 110%, increase neutral tint to .72 and soften top rim to .22. Done content persists. Focus regain never resumes capture. Reduce Transparency gives an opaque #F4F7FB/#243247 shell without backdrop effects.

### The note that lands on the desk

Default copy: “One clear thought at a time.” The pill includes a quiet native key-hint line: “Hold Option+Space to capture · Option+Shift+Space for Todo · Escape cancels”. The panel is not pretending to register a system-wide shortcut; it handles these only with sandbox focus. Capture physical Space with Option at keydown, freeze intent, ignore auto-repeat, and end on Space keyup even if Option was released earlier.

- **Idle → Listening:** holding the pill's capture button, or the Option chord, replaces the hero placeholder with synthetic transcription: “For the sample launch, write the welcome note and check the download link.” Seven 4px round bars with 3px gaps animate in the pill/dock through heights 7, 12, 21, 30, 21, 12, 7px, 120ms phase steps. “Listening” and 00:01 are text, not color-only signals.
- **Release → Refining:** freeze the captured line, show “Refining your note” for 900ms, lower seven bars to 5px, lock duplicate submits. No network or microphone.
- **Done:** replace the sentence with “For the sample launch, write the welcome note and verify the download link.” Promote exactly one action, “Insert into sample note.” `Command+Return` performs this in the current mock document and opens the docked workspace if needed. The mock note visibly gains that paragraph once; announce “Inserted one paragraph into Sample launch.” A second activation reports “Already inserted,” never duplicates content. Do not inject into other apps.
- **Todo intent:** result becomes “Prepare the sample launch” with two folded actions. The promoted action becomes “Add to Todo”; inserting one session-memory task shows “Added 1 task.” The actions unfold on a separate disclosure and use circular semantic button checkrings, no checkbox inputs. `Command+Z` undoes insertion/addition while the workspace is focused and restores the actionable result.

Quiet “New capture” begins the next run and preserves committed mock notes. `Command+Shift+D` or Fold expands/collapses workspace; `Command+[` returns to the pill view. Recent rows work with Up/Down plus Return; selecting a row updates only the selected document. A contextual More popover holds route/settings, including a clearly labeled local “Refinement unavailable” test case: on the next release it shows recoverable “Could not refine sample. Retry” without losing raw text. Retry re-enters Refining locally.

Escape cancels Listening/Refining to the last committed result or Idle, invalidates the run token and all delayed callbacks, and restores focus. Escape in a settings popover only dismisses it; otherwise collapse workspace without discarding notes. Pointer capture ensures an ordinary release outside the button completes recording; pointercancel, lost capture, page hiding and focus loss cancel it. A native Enter/Space click on the focused button toggles start/stop for non-hold access. Suppress post-hold click and repeated keydown. Never auto-save a cancelled or stale refinement.

### Instrument marks and access

Supply all controls with original inline SVGs. Every glyph has viewBox `0 0 24 24`, fill `none`, stroke `currentColor`, stroke-width `1.65`, round joins/caps. Exact path data, not Unicode replacements:

| Name | Path d |
|---|---|
| Record | M8 5a4 4 0 0 1 8 0v6a4 4 0 0 1-8 0V5 M5 10v1a7 7 0 0 0 14 0v-1 M12 18v4 M8 22h8 |
| Fold dock | M4 8l8 8 8-8 M4 3l8 8 8-8 |
| Insert paragraph | M5 3h10l4 4v14H5z M14 3v5h5 M8 14h8 M12 10v8 |
| Cancel | M7 7l10 10 M17 7L7 17 |
| Recent | M4 9a8 8 0 1 1 0 7 M4 4v5h5 M12 7v5l3 2 |
| More | M5 12h.01 M12 12h.01 M19 12h.01 |
| Circular checkring | M21 12a9 9 0 1 1-18 0 9 9 0 1 1 18 0 M7 12l3 3 7-7 |
| Back | M14 6l-6 6 6 6 M8 12h12 |

Draw 18px glyphs within invisible 32px targets, 48px for the primary capture. Minimum desktop target is 28×28px; coarse pointer/touch targets are at least 44px and spaced without overlap. Checkrings are semantic buttons with `aria-pressed`, an unambiguous label and separate selected-row semantics. Tab order is Fold → capture/result action → workspace document → recent disclosure → More. Use 2px blue focus rings, offset 3px. Announce state and successful insertions once, not every waveform tick. Reduced motion removes pill travel and moving bars, uses an immediate layout switch or 100ms fade plus seven fixed bars and state text. All ordinary text must reach 4.5:1 contrast. Preserve complete numbers and shortcut labels, wrap CJK naturally, and scroll the document rather than clipping.

Never modify baseline/original or baseline/interactive.html. Those references freeze iPhone zero top capsule, large whitespace/single sentence, bottom glass sheet, hold/release seven bars and bottom-leading Fold to Todo List/Settings; this desktop design takes its quietness, not new iPhone requirements. Preserve page-config and outer theme/platform messaging. No inner theme/platform/selection controls, website headers, footer disclaimers, Active/Matte controls, 28×28 ruler boxes, `.caustic-veil`, `repeating-linear-gradient` stripes, `rich-r3.css`, shared gray template, emoji control glyphs or raw checkbox inputs. Native workspace toolbars are legitimate. Use synthetic in-memory content only, no mic, network or personal data; clipboard only on explicit user Copy if provided in More.

Writer evidence must show both intents, local insert/undo, Fold round-trip, recent selection, recovery, cancellation before and during refinement, focus loss and keyboard-only completion in light/dark Chromium and WebKit. Do not label this Stage 1 prompt as browser-tested.
