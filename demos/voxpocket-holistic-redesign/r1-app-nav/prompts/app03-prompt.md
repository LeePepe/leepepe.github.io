# app03 — Dual-Mode Lens & Command Palette

## HTML sandbox · A single optical stage, commanded rather than browsed

The product question for this scheme is: can capture, action and memory occupy **one stable stage** instead of requiring a spatial tour? Keep the finalized iPhone capture root untouched. After Fold, an optical segmented lens changes which content occupies the same quiet footprint. On macOS, the quick recorder and a Spotlight-like command palette share one anchored panel, with keyboard selection leading to a distraction-free workspace. The defining gestures are choosing a mode and issuing a command, not paging a deck, dragging a tall drawer or scanning a long activity feed.

This is a stand-alone Stage 1 prompt for a synthetic, handoff-only HTML exploration. Produce no native product implementation from this document. Direction coordinates: **VS-007 Swiss Chrono Telemetry × VS-003 Precision Acoustic & AI Studio**, **CL-008 Swiss Alabaster / Avionics Navy with restrained CL-003 cyan**. Dimensions: layout-navigation, typography-copy, glass-material, motion-interaction. **X:** one active P0 operation; mode choice and Back are P1, receipts/filters are P2, configuration/export P3. **Y:** segmented single-stage replacement with details-on-demand, never stacked modules. **Z:** opaque reading plane at 0, ambient light behind a separate functional optical lens at 10, unfiltered labels at 11, settings and receipts at 20. The proposed coordinates do not freeze an AppTheme.

### Invariant mobile recording plane

Consult baseline/original/v02.html, baseline/original/round3.css and baseline/interactive.html read-only. Their root geometry is authoritative; their stripe-generating adapters, old click handler and square inputs are not to be carried into this rebuild. The live inner page fills **100vw × 100vh**, framed only by the outer chooser's **390×844 Dynamic Island** device. Do not draw another phone, top capsule, header, mode lens or logo on the opening root.

One sentence occupies the baseline stage x=24..366,y=0..694, center about y=347, max-width 330. Keep 25px/650/33.75px type and -0.03em tracking, huge whitespace and no secondary card. The inherited idle cue “准备好时，轻触底部玻璃。” may be retained, with hold/release guidance placed in the existing bottom feedback instead of a new instruction block. Bottom glass is a full-width 148px sheet at y=696, with 24px top corners and square bottom corners. Waveform stays at left=22,bottom=28: exactly seven 4px bars, 4px gaps, height 10 at rest and ≤29 listening. Hold control stays right=22,bottom=24,44×44. Bottom-leading Fold stays left=18,bottom=84,min-height=44, label “Fold”. Root P0 is only recording.

Frozen root light colors: #EAF5F8 to #DCE8F4 to #EEF8F7, white radial air at upper left, #122033 ink/#607287 muted. Dark: #142837 to #1A293C, #EBF3F9 ink/#B6C7D5 secondary. Candidate-specific indigo and typography never override those inherited root tokens. The root must look identical to the approved r3/v02 arrangement before and after a round trip through navigation. The inherited 25px muted cue qualifies as large text (minimum 3:1); keep small feedback/control labels in the existing primary root ink on a stable readable backing for 4.5:1, without adding or moving any root element.

### What Fold reveals: the actual lens, not persistent gallery chrome

Fold's in-place expansion initially reveals **Todo List** and **Settings**; a collapsed “速记与更多” affordance reveals Notes. Selecting Todo or Notes enters a **single flat stage** from y=112 to y=660, with 24px side padding and no raised content card. A native iOS navigation row offers Back at y=72 only while this stage is visible. The optical lens sits x=24,y=716,w=342,h=56; it contains 待办 / 速记 / 模型. Its first two choices are mutually exclusive content modes. 模型 is a utility button that opens settings_sheet and never masquerades as a third content root; the current content selection stays selected underneath. “返回录音” sits as an unfilled Fold/Back affordance with a 44px target. Navigation is revealed only after Fold, and all of it disappears when recording regains the root.

The lens changes one content stage in place, without a card flyover, persistent drawer or a stack of three panels. Preserve content selection/history per destination and give each mode its own semantic heading. The moving optical selection highlight is the only tinted object besides the current P0. Keep it separate from its sharp labels, with a 180ms critically damped translation; Reduce Motion switches selection instantly. Do not put a real translucent lens over the task text.

**Todo mode:** put the focus statement in the upper-middle stage, x=24,y≈218,w=342: “整理会议决定”. A 24px semantic checkring in a 44px target aligns to its first line. It is the only P0 in Todo overview. The stage uses 29/650/36 focus type with substantial air below. Beneath the title, a plain text P1 “语音拆解成三步” opens details, not a second primary fill. A small “待处理 · 3” status lens near the native navigation row opens a compact menu for 待处理 / 执行中 / 已完成; the numeric value is full, never ellipsized. “其余行动” folds the remainder; expand temporarily replaces the focus body with a simple list, preserving selection rather than displaying both. Runner receipt remains under an inline details disclosure.

**Detail mode:** todo_detail is a NavigationStack push **within the selected stage's history**. Keep the bottom lens visible but subdued; choosing another mode preserves this depth for return. Display exactly three borderless action rows “确认输入 / 复核摘要 / 留下回执”, each with a custom circular checkring, one short acceptance sentence and one P0 Run action. Show the source note as a collapsed provenance row, never a duplicate large transcript. Back pops the real caller; note conversions must return to the selected note. With no source history the graph's todo_list fallback applies.

**Notes mode:** one selected synthetic note is a reading surface, not a gallery of cards. Default note title “下周发布准备”, body two short sentences, one P0 “转为行动项” anchored at the lower end of that reading group. “所有速记” opens a single-active plain list of three items in the same footprint; choosing a row closes it and replaces the preview. Recent/All filtering is P2 behind its filter button, and empty results have “清除筛选”. The P1 New action returns to frozen recording. P3 export is in this mode's overflow and exposes a selectable synthetic text preview only.

**Model utility:** selecting 模型 or Fold Settings invokes settings_sheet, not switchTab. Use actual medium 45vh / large 80vh geometry, height and max-height both explicit, rounded functional header and solid L1 body. Local model reads 就绪, cloud 未配置, no account, key input or network setup. A labeled P1 local selection commits and dismisses with “已选本地模型 · 下一段使用离线模拟”. P2 model route opens runner_status; suspend the sheet and restore it after dismissing that receipt. The lens does not change content selection merely because the utility was opened.

**Runner receipt:** compact dialog max-width 342px, max-height 45vh, one received/running/completed path with a specific synthetic result. Anchor to the invoking run/receipt control where possible; otherwise use a bottom presentation with 24px margins. Underlying stage and lens become inert while modal. Refresh advances phase deterministically. Outside/Close/Escape dismisses this top layer only and returns focus to its opener, including within settings.

### macOS keyboard-first capture and command locus

In the outer **1280×800 traffic-light bezel**, the inner page uses the full viewport without an additional window border or traffic lights. Start with a synthetic neutral desktop and a centered native-style optical command panel at **x=320,y=104,w=640,h=112**, radius 26. The leading icon and sentence cue align at x=344; a 32px hold control is trailing, while shortcut labels are small and readable. ⌥Space starts text, ⌥⇧Space starts Todo. Do not imply global OS hotkey registration; these shortcuts act in the focused HTML preview only, with visible pointer/toggle equivalents.

Idle capture is the one P0. A P1 “命令” disclosure expands the same panel to h=388 into navigation-command mode, with an input labeled “查找操作” and a list of only relevant actions: 打开待办, 最近速记, 模型与设置, 返回工作台. Command-search mode owns focus and its P0 selection; the recorder is suppressed/inert there, so input and recording do not compete. Filter the list as the user types, provide a no-result clear action, ArrowUp/Down selection with aria-activedescendant, Enter to invoke, Escape to leave command mode. Keyboard focus does not require the mouse. Do not place a fake search input whose Enter does nothing.

Listening keeps the panel's x/top anchor and adds a transcript line plus seven bars, h=168. Release shows Refining, then Done. A Todo-intent Done offers “复核三步行动” as the primary command; it creates/reselects the draft detail, never starts execution automatically. Text-intent Done offers “在速记中查看”. A quiet “返回捕获” command exists, but no second filled CTA. The row selection invokes the same graph-bound navigation as a pointer click. The menu-bar app icon reopens the command/capture panel; a native “打开工作台” action moves into the workspace and hides/inerts the floating panel.

Workspace is a **single reading canvas**, with a 44px native action toolbar, no permanent sidebar and no bottom bar. Its left portion is 888px when the optional 392px inspector is open; otherwise content reads at a comfortable maximum 720px centered in the full width. Toolbar has the current route's plain native title, command button, Back, and “返回快捷面板”. Capture body is one sentence plus a top-trailing hold action. Todo overview shows the one focus statement, folded queue and context filter; selecting an object opens the right inspector as todo_detail, preserving object identity and source. Notes selection opens its preview in that same inspector. While inspecting, Run or Convert becomes the one prominent P0 and the center's completion/capture is visually demoted. Settings is an attached 440px-wide sheet with a solid body; runner is a 340px anchored popover. Closing inspector restores the stage's previous primary action. “返回快捷面板” saves route, inspector and scroll and returns to the previous capture/command panel mode. Reopen workspace restores that snapshot.

Use native menu/command equivalents Cmd+1 Todo, Cmd+2 Notes, Cmd+, Settings and Cmd+K command disclosure while this sandbox is focused; ignore editable fields except the command-search input's own navigation. A menu item / pointer action provides each command, so interception by the browser or host OS never blocks the journey. These are native app navigation controls, not gallery selections.

### Type and appearance measured for a stable stage

Use exactly **-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text"** with a final sans-serif fallback; use tabular-number features rather than changing the font for shortcuts or counts. Root sentence: 25px/650/33.75px. Mobile stage focus 29/650/36; body 17/450/25; lens/action labels 15/550/21; metadata 12/500/17. Desktop workspace title 25/600/31; body/command rows 13/450/20; selected command 13/600/20; shortcuts 11/500/16. Command capture sentence 20/550/27. Only the panel or canvas's relevant four sizes appear together; do not make five sizes compete in one pane. Use full readable words and natural CJK wrap, not raw localization keys, forced uppercase tracking or clipped labels. Numbers cannot truncate with an ellipsis.

Spacing is deliberately **open within one plane**: atoms 4px, control padding 12px desktop/16px mobile, mode content margin 24px, focus-to-folded-context gap 48px, reading text line spacing supplied by the above leading. Popover padding 16px with 8px row spacing; padding never less than row spacing. No surrounding hero box. At most three visual groups per pane: route context, active object, folded utility/control. Never display raw transcript, refined transcript, queue and model status as four flat sections.

Post-Fold/workspace light palette: L0 **#F8FAFC**, L1 **#FCFDFE**, L2 **#FFFFFF**, primary ink **#15243A**, secondary **#586B81**, indigo ink **#4553A6**, cyan utility ink **#096B86**, completed ink **#21684B**. Dark palette: L0 **#0E131F**, L1 **#172132**, L2 **#202D43**, primary **#EDF2FA**, secondary **#B6C4D8**, indigo accent **#B2BAFF**, cyan **#79DDF0**, completed **#88DBAE**. Recording coral **#AE2849** light / **#FF9DB9** dark. Both themes brighten from L0 to L2. Indigo occupies selection/command focus, cyan is transient feedback only; do not color every utility. Use ≤10% chromatic emphasis. Text needs ≥4.5:1 on resolved solid surfaces and ≥3:1 for large text; state always has words/shape, not color alone.

### The optical lens is a functional layer, not a content treatment

Behind the bottom lens/command shell, paint a static nonrepeating indigo radial aura at 14% and an ice-blue radial aura at 10%, blurred 36px. This ambient background is separate from shell geometry and never contains readable text. Optical shell fill is white/.32 light or #263958/.58 dark, clipped to a continuous capsule/26px panel radius. Specify **backdrop-filter blur(28px) saturate(190%)** and **-webkit-backdrop-filter blur(28px) saturate(190%)**. Top Fresnel is **inset 0 1px 0 rgba(255,255,255,.75)**, rim .5px white/.38 light or .20 dark, shadow 0 14px 36px rgba(27,48,84,.14) light / rgba(0,0,0,.34) dark. The moving selected lens fill is a single opaque/tinted insert, not a second backdrop sample. All text/SVG is a sharp sibling above the optical layer. Notes, action rows, command results and reading backgrounds are solid L1/L2, never glass.

WebKit fallback is pure blur/saturation/rim plus ambient light. Chromium may add a clean signed-squircle Snell/Fresnel backdrop effect only on the shell edge, max displacement 2px; never put the filter on the command list, text, icons or whole app. Adjacent optical controls share one sampling group, with no glass sampling another glass. HTML is an approximation, not falsely native rendering. Inactive window automatically lowers rim/selection intensity; no user-facing Active/Matte toggle. Reduce Transparency replaces shell with opaque L1, preserving sharp content and contrast.

### Exact command/lens control drawings

For each glyph use inline SVG with **24×24 viewBox (0 0 24 24)**, **currentColor stroke**, **fill none**, stroke-width **1.6**, rounded linecap and linejoin. Data below is literal SVG path data; semicolons mean separate paths, not a combined Unicode symbol. Draw at 24px, do not rasterize.

| Control | Path data |
|---|---|
| Voice capsule | `M9 5a3 3 0 0 1 6 0v7a3 3 0 0 1-6 0V5Z`; `M6.5 10v2a5.5 5.5 0 0 0 11 0v-2M12 17.5V21M9 21h6` |
| Fold / open stage | `M4 5h16v5H4z`; `M6 10v9h12v-9M9 14h6` |
| Optical lens selector | `M20.5 12a8.5 5.5 0 1 1-17 0 8.5 5.5 0 0 1 17 0Z`; `M12 6.5v11` |
| Search / command list | `M15.5 10a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0Z`; `M14 14l6 6` |
| Focus checkring | `M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z`; checked `M7.5 12l3 3 6-6` |
| Notes | `M5.5 3.5h13v17h-13zM9 7.5h6M9 11.5h6M9 15.5h4` |
| Model route | `M5 6h5v5H5zM14 13h5v5h-5zM10 8.5h6.5V13M7.5 11v4.5H14` |
| Run | `M8 5.5 18.5 12 8 18.5z` |
| Back | `M15 5l-7 7 7 7` |
| Close / cancel | `M6.5 6.5l11 11M17.5 6.5l-11 11` |

A checkring is a **semantic button** with aria-pressed and a specific task name, never a raw checkbox input. Draw the circle and checked path; do not use a font checkmark. Icon-only controls have names; decorative SVG is hidden from assistive technology. Mobile hit area is **≥44×44px**, desktop **≥28×28px** with 32px preferred in command chrome, invisible rather than ruler-decorated. Row selection and row completion are sibling controls, never nested. Active focus gets a 3px accent outline with 3px offset, including lens segments and command rows.

### Exact graph compliance and route restoration

This candidate binds scheme **3**, not a graph invented by the writer. Keep **page-config** application/json, schema navigation-page/v3, id app03, supplied platform, full scheme and any coordinates/provenance/style fields. `architecture.kind=lens`; root r3v02_capture; destinations [r3v02_capture,todo_list,voice_notes]; primary r3v02_capture/0; sheet settings_sheet; collapse_title=true; overflow references r3v02_capture/3 and voice_notes/3. Keep the supplied dispatch/currentScreen/navigationDemo inspection API when available. Collapse only the native route title after 32px content scroll; never install a top capsule on the frozen root.

Every row below is an executable binding with zero-based action index, on both platforms:

| Screen / action | Frequency | Commit, transition, feedback |
|---|---|---|
| `r3v02_capture/0` | P0 | `voice_capture` on Done only, one note per finished capture |
| `r3v02_capture/1` | P1 | `pushScreen(todo_list)` from Fold Todo, preserving capture origin |
| `r3v02_capture/2` | P2 | `switchTab(voice_notes)` from Fold's recent disclosure |
| `r3v02_capture/3` | P3 | `toggleSheet(settings_sheet)` from Fold Settings/overflow |
| `todo_list/0` | P0 | `todo_completed`; toggle selected focus with 5-second Undo and updated counts |
| `todo_list/1` | P1 | `todo_decomposed`, `pushScreen(todo_detail)`; three steps exactly once |
| `todo_list/2` | P1 | `switchTab(r3v02_capture)`; suppress lens and recover exact root |
| `todo_list/3` | P2 | `togglePopover(runner_status)` from folded receipt |
| `todo_detail/0` | P0 | `runner_started`, `togglePopover(runner_status)` only after explicit review |
| `todo_detail/1` | P1 | `popScreen(todo_list)` fallback or actual caller when history exists |
| `voice_notes/0` | P0 | `note_to_todo`, `pushScreen(todo_detail)`; same note converts idempotently |
| `voice_notes/1` | P1 | `switchTab(r3v02_capture)` new-note intent |
| `voice_notes/2` | P2 | `notes_filtered`; Recent/All visibly changes list and filter summary |
| `voice_notes/3` | P3 | `notes_exported`; overflow reveals synthetic text export preview |
| `settings_sheet/0` | P1 | `model_local`, `dismissOverlay`; specific local-selection consequence |
| `settings_sheet/1` | P2 | `togglePopover(runner_status)`; suspend settings caller |
| `settings_sheet/2` | P3 | `dismissOverlay`; restore exact opener |
| `runner_status/0` | P1 | `runner_receipt`; update current simulated receipt/phase |
| `runner_status/1` | P3 | `dismissOverlay`; restore preceding modal or content |

The post-Fold Todo/Notes lens choices themselves are destination switches with destination-local histories; do not rewrite the declared capture/1 push into a switch. Keep origin history for note conversion and root entry distinct from mode switching. Switching to another mode and back restores its pushed detail and scroll. Closing the lens deliberately returns capture, while normal Back first unwinds within the current mode. Overlay model/receipt presentation never erases a destination's history. A modal P1 selection can be its sole prominent action; do not manufacture a P0 model mutation absent from the graph. Suppress the capture primary control wherever another route owns focus.

### Full interaction and accessibility contract

Idle → Listening on pointer-down with pointer capture; seven deterministic bars animate at different phases. Release → Refining immediately, stop bar motion, show progress in the existing feedback line; after 900ms → Done, render “整理发布决定，确认下一步行动。” in the one sentence area and commit voice_capture once. Text mode adds a synthetic note, Todo mode offers a draft for review; neither records real sound or executes a real runner. Do not request microphone, use media/audio APIs, send model/network/analytics traffic, read personal data, read clipboard or load remote fonts/assets.

Pointercancel, lost capture, window blur, page hidden and Escape cancel uncommitted capture/refinement and invalidate pending timers, restoring Idle with no appended note or steps. Preserve previously committed results. Ignore reentry while Refining and repeated keydown; suppress the synthetic click following pointer-up. Focused Space down/up supplies hold parity, Enter/assistive activation toggles start/stop as a non-hold alternative. Do not intercept text editing keys; command input has its own focused navigation. Cursor or key focus must never accidentally start the recorder beneath an overlay.

Decomposition is idempotent and always three steps. Completion produces a concrete receipt plus Undo, not a silent visual tick. Runner follows accepted/running/completed with 600ms simulated phase ticks; Refresh advances or refreshes one current receipt without duplication. Route changes preserve selected task/note ID, filter, progress and completed status. Empty Todo offers capture, empty Notes filter offers Clear, command no-results offers clear query. A local state failure has an inline retry, never a fictional network service failure.

Escape order: cancel uncommitted recorder, close receipt, close settings, leave command-search mode, pop detail, close post-Fold lens. Focus returns to its precise opener and hidden modes have no tab stops. Mobile native Back mirrors this order except a capture cancel is explicit when the recorder owns input. Tab/Shift+Tab stay within a modal, not a permanently trapped app. VoiceOver names express selection/checked state; live progress is polite and not announced every waveform frame. Hover is supplemental, never the only affordance. Lens choices have visible labels, not cryptic glyph-only tabs.

Respect prefers-reduced-motion: no waveform loop, sliding lens, spring or parallax; use static unequal bars and immediate state selection or ≤100ms opacity. Reduce Transparency uses solid surfaces. At enlarged text, grow/scroll the stage and sheet bodies; keep 44px touch targets, bottom safe-area clearance 34px, and no clipped task or numeric truncation. Settings has a labeled Expand/Collapse action in addition to its grabber; mobile list scroll cannot trigger mode selection.

Keep the outer chooser's hooks: same-origin parent **postMessage** `rich-theme` with theme light/dark, `rich-platform` with platform phone/desktop (mobile/macos aliases may map internally). Validate source===parent and event origin; file: null is only a local preview exception. Ignore unknown payloads. Also respond to direct data-theme on documentElement/body from gallery-chooser and resize when no explicit platform is set. Map logical route and selections between mobile stage and desktop inspector without committing again. Preserve existing rich-nav notification format if supplied; do not invent star/selection messages. Platform/theme/gallery selection controls belong exclusively to the outer chooser.

### Implementation evidence and exclusions

Require Chromium and WebKit screenshots/interactions for both light/dark at 390×844 and 1280×800. Exercise capture hold/release/cancel and all four recorder states; Fold Todo/Settings; lens mode restoration; notes conversion and Back; nested settings/runner; completion Undo; three-step idempotence; Notes filter/export; command query/no-result, Arrow/Enter/Escape and pointer equivalents; panel↔workspace return; host theme/platform changes. Check screenshot dimensions, one P0, target sizes, no horizontal overflow/clipping/numeric ellipsis and sharp foreground outside filters. Do not claim browser/native optical certification from this text.

Absolute exclusions: **no `.caustic-veil`**, **no `repeating-linear-gradient` stripes**, no shared `rich-r3.css`/shared gray template, no raw checkbox inputs, no inner website headers, no Active/Matte controls, no 28×28 ruler boxes, no footer disclaimers, no nested device frame or duplicate traffic lights, no inner platform/theme/selection controls. Native app navigation, the actual command panel, route titlebars and action toolbars are allowed. This prompt contains the entire candidate; implementation must not depend on a shared prompt-template or another variant's design.
