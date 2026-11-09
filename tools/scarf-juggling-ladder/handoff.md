# Scarf Juggling Ladder handoff

Build only, 2026-11-07. Run every command from `S:\CurioClass-codex`.
Only this tool and `_scratch/scarf-juggling-ladder/` were written. No commits or polish round.

## Layout and logic

`src.html` starts from the kit starter. It keeps the kit header, Motion, Sound, Read and Curio.voice.
Tool-local CSS lays out the painted gym, six-rung navigation, SVG performer, HTML timer and log cards,
and a real-size SVG chart. Compact landscape stays side by side. Portrait screens stack.
The controls precede scene items in DOM tab order. Modal setup and clear dialogs use native focus trapping.

The `R` table contains exact rung content and tips. `pattern(n)` supplies beat and flight timelines:
rung 4 has three falling flights and no catches; rung 5 is toss, toss, claw, toss, claw, claw;
rung 6 continues alternating throws. Painted body and six arms are keyed assets.
SVG scarves carry stripes, dots or a border plus an ink outline. Hand mirroring affects the complete group and beat words.
Motion off quantizes flight positions without changing any timer or demonstration pacing.

`demoToken` cancels a demonstration immediately on a rung change, cue tap, restart, Step or try.
`timerToken` prevents a stopped countdown or ending narration from opening an old log card.
Practice elapsed time is measured from performance.now after Go begins. Entry and Save both enforce ten seconds.
The partner history stores run, previous best and drops before each action, so Undo also undoes a Drop.

The localStorage schema is versioned and validated on reading. Storage errors leave the same in-memory log
and show the session-only warning. Sessions are global to the log, not separate per rung.
The fictional sample is a separate array and immutable goal; it never writes to the personal log.
Every chart dot has equal visible size and a 44-pixel input region. Narrow charts scroll rather than overlap input regions.
Screen-reader names include dot coordinates as the nonvisual equivalent of the graph.

Chart reading records whether the first/latest selection was correct, but has no score.
The explicit Interactions rule explains wrong taps and advances; a wrong dot is never recorded as correct.
The sentence has one attempt, shuffled placement, then an explained result. Dip checks compare session bests.
Cue tallies remain hidden until both reflection choices. Yes and A little reset answers are counted separately.

## Checks and evidence

Scratch contains the number recomputation, generated-image paths, art contact sheet, two reference-tool bundles,
frames, functional assertions, 2,187 counter sequences, timed held-click play walk and voice logs.
The full report is `codex-report.md`. It records the final audit leads and any unfinished verification.
The single mechanical audit failed during its first DevTools connection with WinError 64 and produced no leads or frames.
The audit was not rerun. Targeted release-pose, keyboard-focus, resize and blocked-on-load checks followed;
the final bundle has no completed mechanical audit. See Scratch `audit/audit-failure.md`.
Build and test helpers in Scratch are evidence, not runtime dependencies.
The distributed HTML bundles the kit and nine WebP images and makes no network requests.
Build-stage narration had 75 fixed lines, easy-coach / Umbriel. No audio was recorded, per the build brief.
Variable chart results use browser speech. Recordings can be added in a later authorized stage.

## Decisions and open questions

- People art: took the spec's clear leaning and painted the child and all six arm poses. All seven assets carry
  `people: true`. OpenAI gpt-image replaces the older Gemini wording, as explicitly authorized by CODEX-BUILD.
- Independent people/representation review and Cory's contact-sheet review remain for the cold review and shipping
  workflow. No approval was requested in this unattended Build. Contact sheet: `_scratch/scarf-juggling-ladder/art-contact.png`.
- The spec requests welcomeAfter true, while BUILD and KIT restrict it to one-mode tools. Used false for these two modes
  to prevent a late welcome, following the standing voice rules and BASELINE rule 16.
- Welcome wording uses "the pattern" and "Read my chart" so it remains true on a resumed rung and in stacked layouts.
- CODEX-BUILD asks for an early report scaffold; the direct prompt says to stop when the report is written.
  Kept intermediate evidence in Scratch and wrote the final report only at completion.
- Done when 7 says the dot steps accept only correct dots; Interactions explicitly advances after an explained wrong dot.
  Followed the detailed interaction, with a separate correctness record and no success score.
- Session numbers belong to the whole log. For a rung first practiced after session 1, its first visible session is used,
  with that actual number in the prompt, rather than asking for a nonexistent session 1.
- At narrow widths the chart can scroll before ten sessions to keep 44-pixel hit regions from overlapping.
- The no-motion-on-load requirement takes precedence over the general request for quiet idle movement.
- The ten-session maximum is only for choosing the goal deadline. Actual logs can extend past ten sessions.
- Rung 6's ready line invites continued cascade practice, rather than naming a nonexistent rung 7.
- A goal larger than the largest logged result expands the y axis so its dashed line stays visible. This resolves
  the conflict between the prescribed data-only axis maximum and the requirement to display every chosen goal.

## Sensitivity

The tool depicts a child's body in ordinary PE clothing and teaches a movement skill. Review the assembled arms,
finger shapes, range of reach and representation without treating one body type as a performance ideal.
The child is friendly and fully clothed; the tool does not judge appearance or compare students.
The reset question includes I'd rather not say. Teacher notes identify the SHAPE body/movement standards,
the adult-only scope of the brain study, comfortable reach, and the disagreement about catch height.

## Engine changes wanted

None. No shared file was changed.

## Cold review changes, 2026-11-07

The review preserved the painted gym, child and patterned scarves. A hand holding a caught scarf retains its
claw while an empty throwing hand lowers. Two scarves held together remain separately visible. Cutouts were rekeyed with despill
enabled after a generated cleanup introduced worse edge artifacts and was rejected.
Entry locks the underlying rung/demo/mode controls and keyboard mode shortcuts until Save, preventing a saved
try from changing rungs behind its card. The reset reflection has a Not needed choice, stored without adding
to helped counts. Countdown extension is disabled; the running timer accepts +30 once and uses an accurate
thirty-seconds-left line on an extended try.

Phone entry fills the area below the header, keeps Save and all five reset responses in view, and repeats the
device-only privacy line inside the card. Compact landscape keeps the same controls at 44 pixels.
Chart progression still follows the spec's detailed explain-and-advance rule. Its final card now distinguishes
an independent response from an answer shown or corrected after help, with no mastery score. Ren's chart and
prediction name Ren. A curved recovery link lifts the dip moment and is still in Motion off. Completed chart
reading names Ladder as the next action. Small charts center the dip and next session together. A reading-generation
token prevents old feedback from advancing a newly selected chart. Answering hushes the prior prompt, and Save hushes
entry narration before its cue tip. Goal narration now names the disclosure students must open first.
The practice-spacing sentence now says can help, matching the limits of the cited motor-learning research.
See codex-review.md for independent evidence and the final audit disposition.

The review audit completed once within its 40-minute limit. Its raw leads include closed native disclosure
geometry, intentional modal/background coverage and deliberate fast-tap speech cuts. Confirmed layout leads
were corrected with explicit closed-content hiding, overlay label cleanup, clock line height, chart label
clearance and a visible phone-entry hint. Saved cards now leave rung navigation accessible and dismiss on
Show, Step, cue or rung actions. See my log explicitly returns to personal data after sample viewing.
Goal feedback distinguishes no tries from a real zero, and edit narration names Change goal. Current fixed
narration count: 78. The final contact sheet is `_scratch/scarf-juggling-ladder/review-final-art-contact.png`.

Final scoped chart rechecks preserve 44px dot targets at all eight required sizes, including the horizontal
scrollbar case. The chart uses explicit SVG pixel dimensions rather than shrinking its hit regions to fit.
All six post-audit partner frames and the phone-entry, saved-to-Show and saved-to-next-rung paths were re-shot.
The bundle is 511.23 KB. Source syntax and the nine-asset manifest pass the final static check.
The review leaves the prescribed self-report limitation explicit: invented counts can produce best/ready
marks, and the tool cannot certify physical skill. Changing that requires a product/spec decision.
The final real-clock main-path voice recheck and edited-goal Read check passed; all 78 runtime lines match
the voice manifest. Temporary host.html is removed and Chrome ports 9950-9957 are closed. Port 8755 still
serves this tool directory; Windows denied process lookup, so its unidentified owner was not terminated.
