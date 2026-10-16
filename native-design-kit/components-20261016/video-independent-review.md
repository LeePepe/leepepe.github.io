# Independent interaction-video review

Source: `a870b9cac06a90f50155e226d2ba167af78ef8f6`. Device: iPhone 18 Pro, iOS 27.0, light appearance, default text size.

This is a decoded-frame sequence review, **not continuous playback**. The independent reviewer personally inspected 177 requested samples at 0.2-second intervals in 16 chronological contact sheets, plus 11 individual frames. Some stationary intervals returned repeated encoded frames, so the sample request spacing is not a guarantee of continuous visual coverage. Timestamps below refer to actual returned frames in the supplied trimmed videos, not exact input-event timing.

| Recording | Duration | SHA256 |
| --- | ---: | --- |
| Button.mp4 | 11.870 s | `ef74ba374e93395b4276ca6c8e169e11776da99758b5a11795a16286be05c785` |
| Toggle.mp4 | 13.063 s | `3b30298ded4839be48ba76e1870555a306778b1369c951099147f4a03dd54c61` |
| TextField.mp4 | 10.050 s | `bbf24767ed335c235696e877e3ad9ad8781f8f676cf7bb52dad0df868753d44e` |

- **Button:** native pressed feedback is visible at 1.958–2.158 s. Loading retains the Save a Copy label with adjacent progress and `Actions: 2`; completion shows “Copy saved” at 7.160 s with the same count. No obvious button/label displacement or spinner collision appears in the sampled states. The subsequent role-result changes and floating native Glass context are visible.
- **Toggle:** sampled native intermediate states lead to the expected on/off positions. The neutral context shows “Details included” at 9.388 s and “Details excluded” at 11.188 s, with stable row layout. Disabled specimen positions remain unchanged in the samples. The video has no touch markers, so attempted disabled tap coordinates are not independently established.
- **TextField:** native keyboard and caret are visible, followed by the complete cause-and-correction error above the keyboard at 4.990/5.198 s. `Draft` remains editable; the documented error persists until resubmission. At 7.988/8.168 s the helper and “Submitted: Draft” are visible as the keyboard withdraws. No persistent error occlusion or text collision appears in the inspected samples.

No new component defect or persistent feedback/layout blocker was found in these frames. They support the visible state sequence; **continuous animation quality, responsiveness and exact timing remain unverified**. Test-pass metadata does not fill those gaps.

The clips retain some launch/exit footage: Toggle and TextField start with white/fading launch frames, and all three end with a brief simulator Home Screen view. This is a recording-boundary issue, not a component defect. Any later trimming produces new video hashes and should be documented separately.

This review does not establish macOS live keyboard focus/hover/Glass, hardware keyboard/Tab/shortcuts, VoiceOver/Full Keyboard Access, rendered contrast, Reduce Motion/Transparency or Increase Contrast behavior, Chinese IME composition, large-type error with the keyboard open, or minimum iOS 15/macOS 12 runtime. The static review's native macOS bitmap and desktop text-scaling limits still apply. No full interaction/accessibility or shipping approval is claimed.
