# Codex report: monologue-rehearsal

## Built

Built the five-mode offline acting studio from the kit starter: four monologues, six circumstances, three independent
scores, sixteen tactics, a live prompter, four audiences, a real listener's script and saved comparison records.
Includes automatic device saving, immutable performance plans, reflection boxes and confirmed Clear all.
No commits, branch changes, recordings, shared-file edits or polish round.

## Numbers check

PASS: spoken words 207 / 179 / 208 / 161. Mrs Hale has 163 space tokens including two unspoken cut markers.
The Shakespeare source line counts are 25 / 24 / 26; Viola's spec says 24, but its exact source text has 25.
At 150 words/minute, displayed estimates are 83 / 72 / 83 / 64 seconds, rather than the spec's rounded card estimates.
PASS: marks 30, 62, 110, 150 and flags 33, 147 give one of four matches, with flag 147 unplanned.
PASS: teal/panel 8.96:1, teal/section 8.49:1, ink/teal 9.56:1; script/background 16.32:1; gold/background 13.49:1.
Evidence: Scratch content.py, numbers.txt and direct Gutenberg source downloads. The spec was not edited.

## Feel check

Walked the full actor/listener workflow with held pointer input and with keys only, and inspected the resulting frames.
Best moment: the pale bracket connects a gold listener flag to a teal planned change while an unplanned flag remains
visible as separate evidence. Want agreement and the partner's own word turn the overlay into a specific rehearsal record.
Flat moment 1: crowded compact controls consumed the prompter. Changed short landscape to A/B/C buttons and a shorter
script heading; the 20-pixel prompter now has 181 pixels of height at 680x425, with Start/Back/Next in view.
Flat moment 2: the score desk opened with intent boxes before actionable beat controls. Moved the word tools and current
beat editor first, kept whole-speech want/obstacle lower, and made the phone sheet explicit.
Compared painted Choose and rehearsal frames with Snowy Mail Route and Beat Lab. The paintings, typographic script and
rehearsal lighting have comparable finish; rewards remain evidence and a clearer performance, appropriate to grades 9-12.
Side-by-side frame: _scratch/monologue-rehearsal/bar-comparison.jpg. No human classroom performance was evaluated.

![Monologue Rehearsal beside Beat Lab](S:/CurioClass-codex/_scratch/monologue-rehearsal/bar-comparison.jpg)

## Done when

1. PASS: Choose cards, Prepare script, Rehearse prompter, partner script and Compare overlay are the largest regions at
   1366x768 and 680x425. Final compact frames and the audit matrix are listed below.
2. PASS: direct source extraction preserves the three Shakespeare texts and their line endings. The Glaspell cut follows
   the exact supplied wording, commas, ellipses and cut markers; no voice narrates the texts.
3. PASS: marks, stresses and pauses place/remove; all three versions are independent. Held-input checks cover copying to
   both destinations and keyboard word/gap navigation. Keyboard-only workflow adds a beat and reaches a saved reflection.
4. PASS: partner DOM has no active stress, pause, gap, beat-editor or actor-bar markup. Read's logged text is only the
   current listener instruction. No microphone/camera API or network call is present.
5. PASS: sample gives one of four and the correct extra word. Zero-plan and zero-flag frames show their specified lines;
   31 attempted flags stay capped at 30 and the strongest-moments message appears. Tapping a flag again removes it.
6. PASS: Start, Next and Back update immediately. Space advances and Shift+Space returns without scrolling the page;
   switching versions preserves the available beat number. The elapsed timer continues with Motion off.
7. PASS: saved take and reflection survive reload. Earlier and later records open separately; Clear all cancel retains
   work, and confirmation removes the localStorage key. All storage access is guarded.
8. PASS: five runs at held-click, two-second action spacing give every how line once, landed five times and wantRead five
   times while Compare stays current. Leaving Compare drops unstarted result lines. Targeted first-handoff check confirms
   welcomeCirc and the first Start's breath cue now begin immediately in their intended phases.
9. PASS: nine generated images load, with no people or lettering. Final-size inspection caught a figurative stone relief
   on the first Roman painting; one redraw replaced it with geometric and leaf ornament.

## Wave lessons

- Hint and voice: PASS. Synchronous hints name the next control; Read uses that hint. Curio.voice owns heard-state,
  stale scopes, Read priority and Sound behavior. See voice-results.json and handoff-voice-results.json in Scratch.
- Focus and layout: PASS in keyboard workflow. No focus is taken on load; roving word targets avoid hundreds of Tab stops.
  Local mark changes keep the script node; rebuilt version/tab/history controls restore focus with preventScroll.
- Sizes: PASS for main controls and hints across the required matrix, including 375 through the host. Dense preparation
  panels and long records scroll; the phone uses a beat sheet. Caption scrolling at the smallest preview is noted below.
- No giveaways: PASS. Listener text contains no actor marks; wants shuffle, and no option is marked correct.
- Honest numbers: PASS. Reader names the 150-word/minute assumption; comparison explains its matching window and is not a grade.
- Standards: PASS. Circumstances and score teach TH:Pr4, the audience/live performance teaches TH:Pr6, Connect teaches TH:Cn10.
- Motion off: PASS. The quiet indicator explicitly stops; timing and rehearsal state continue. Motion-off frame inspected.
- Short choice sets: PASS. Four pieces, four audiences, three versions and seven listener wants remain selectable in view;
  the short landscape response layout keeps Save visible. Long circumstances and records are intentional scroll panels.
- Resize mid-action: PASS. The full audit resized after inputs in every state and walk click; no exception or stuck control.
- Delayed welcome: PASS. No welcomeAfter. First mode/action changes invalidate old instructions; targeted handoff passed.
- Unknown as unknown: PASS. No listener evidence is invented. Before a take there is no Compare; unset closest want is stated.
- One look, one meaning: PASS. Actor bars, listener triangles and pale brackets remain distinct in grayscale.
- Badge truth: PASS. Counts come from saved flags and unique matched marks; no planned changes is explicitly named.
- Hint restores with state: PASS. Mode/tab switches and Clear all restore the current action instruction.
- No answer by copying: PASS. Wants are hypotheses chosen privately by the actor, then independently by the real listener.

## Audit leads

The single full audit finished in 586 seconds with 27 leads. All 73 audit PNGs were inspected.
Ten field-naming leads: FIXED with explicit aria-labels, in addition to the existing enclosing labels. Targeted names pass.
Twelve scroll-panel leads: retained by design. These are six long circumstances with fact disclosures and the long
comparison/history/reflection form, rather than a hidden short answer set. The spec places the script first and asks
for all these fields; long forms scroll while the script, mode controls and hint remain visible.
Four first-card welcomes not heard: expected. The spec explicitly makes welcomeChoose stale when any card is tapped.
The reader and Choose this one appear immediately, with no delayed welcome or narrated monologue.
One quick active-Choose interruption: FIXED. Tapping the current mode leaves its running welcome intact; a fresh held
two-tap check logs one uninterrupted welcome. One-beat hints were also fixed to omit disabled Back/Next instructions;
the added conditional instruction, first breath and visible phone privacy notice passed targeted checks.
Runtime, resize recovery, Motion off and repetition checks were clean. The full audit was not repeated after these
targeted fixes. No console errors, warnings or exceptions occurred in the final targeted drive runs.

## Frames looked at

Inspected every image in first-frames (6), functional-frames (5), matrix-frames (26), phone-frames (9), targeted-frames (4),
final-frames (2), the keyboard frames (2), voice-final.png, all nine final WebPs, the art sheet and both reference frames.
Contact sheets are in Scratch; representative 680x425 and 375 frames were also inspected at native size.
Also inspected all 73 audit PNGs through audit-sheet-0.jpg to audit-sheet-19.jpg, and all three post-audit-frames.
The final phone Choose, Score and Rehearse frames verify the common privacy footer after its targeted change.

## Art made

Nine environment paintings made with the built-in OpenAI image tool; one Roman-street redraw. Final raw PNGs are in
art/raw, final 1200-pixel WebPs in art, complete prompts and provenance in art/prompts.json. No downloaded images.
Total final art: 1126.2 KiB. Final bundle: 1,642,247 bytes, about 1603.8 KiB, under 2 MB.
Used only the free art.py --rekey form. The ten-line voice manifest is unrecorded, as instructed.

## Art still to paint

None. No people assets were requested or deferred. The browser narration manifest has no recordings by instruction.

## Engine changes wanted

None. No family engine is specified and no shared file needed a change.

## Left open

- Browser speech cannot reproduce the specified soft-breath / Enceladus bank voice without recordings. None were made.
- Some dense Choose captions at 680x425 scroll within their cards. All four card targets remain visible. Long preparation
  settings, performance history and reflection panels also require scrolling, especially in compact layouts.
- Live paired performance quality has not been classroom tested. Scripted partner evidence validates the mechanism only.
- The source heading for Helena places the scene in a palace room; the supplied circumstance says by the palace and asks
  for an outdoor garden painting. The build follows the supplied Content and art; the discrepancy is in handoff.md.
- A mode change after two seconds may discard an unstarted result line, correctly, once its result is no longer current.
