# Codex review: theory-gym

## Played

Played Lens and all 25 Workout reps cold as a grade 9-12 student before reading the builder's report, handoff, notes or source. Also checked the projection layouts. The two-lens pivot is the strongest moment; the exact spelled-note model and maple workbench stay.

## Findings fixed

- Blocker, general, sounding harmony: Set 2 reps 1 and 5 and Set 3 rep 4 crossed an upper part below the written root bass, making the perfect-authentic example sound inverted. Moved those passages' upper three voices up one octave, retaining all specified pitch spellings, soprano pitch classes, close upper spacing and nearest bass roots. High notes use downward stems. Independent root/voicing checks and compact/laptop frames verify the correction.
- Blocker, general, score playback: an 820 ms redraw during a held chord press could swallow the click and keep the passage running. Deferred score replacement until pointer release. A held Play, lens move and chord tap now leaves playback stopped on the selected note.
- Should fix, general, instructions: returning to Workout named Warm-up rep 1 regardless of the current set. Now uses the current rep's action. Locked pivot hints now ask for a pivot tap.
- Should fix, general, completion: rechecking an already completed set repeated its completion event; the last set named a nonexistent next set. Now announces only the completion transition and gives current Next rep or Reps instructions, with a specific all-25 result.
- Should fix, general, voice: preserve a still-relevant how-to across same-set rep changes; newer result events take priority over old narration. Turning Two lenses off stops its stale green-lens instruction. Read retains kit priority.
- Should fix, general, state: changing a key clears stale check/lock feedback and checked evidence while preserving saved progress. Lens exploration clears Workout lock badges. A later wrong pivot no longer retains solved status. Re-locking an already solved pivot retains its next action.
- Should fix, general, art: the painted piano had a continuous, incorrect black-key pattern. Replaced it with a generated ebony/maple painting with standard groups of two and three.
- Polish, general, payoff and score: correct checks frame the deciding interval notes, tonic ending, cadence pair or pivot and light the corresponding keyboard. Staff and numerals stay together on tall displays. Long raised-degree labels now use their intended smaller type.
- Polish, general, header: Sound reserves its toggled width and stays on one line; held Sound off moves no other header control.
- Polish, general, MIDI: preserve written octaves across B-sharp and C-flat spellings. Current passages do not use those edge spellings.

## Findings left

- Should fix under the gameplay rule, general, spec conflict: exact live fit feedback permits exhaustive key search. Retained the specified core mechanic as the review brief requires; changing it needs a spec decision.

## Flattest moment left

Some key reps can still be solved by cycling the exact fit counter. The checked-answer moment now points to musical evidence; no new scoring or tasks were added.

## Graphics

Checked both raster assets in the tool at final sizes and the code-drawn score and keyboard. Replaced piano-detail using the built-in image tool; prompt and provenance are in art/prompts.json and the selected raw image is art/raw/piano-detail.png. Maple painting retained. No people assets or missing art tokens.
Two final WebPs total 95,340 bytes. Bundle: 258,811 bytes (252.7 KiB). Compared with Beat Lab and Snowy Mail Route frames; the score-led finish stays distinct.

## Audit

The single audit finished in 33.20 minutes, within its 40-minute limit, Chrome 9951 and host 8755. All 77 frames were inspected. Its 210 leads are dispositioned in `_scratch/theory-gym/review-audit/review-dispositions.json`: 167 transparent-hit-area overlaps, 34 intentional modal coverages, 3 required phone score scrolls, 5 specified welcome skips, and 1 warm-up playback snapshot timing lead. Runtime, focus, Motion off, repetition, quick taps and resize recovery were clean. The Sound movement row prompted a stable-width fix, verified at zero header shift.
Independent checks: 2,455 Python music checks; 911 browser assertions; all 25 reps played before source review; keyboard-only solve retained Check focus. All standard sizes, phone iframe, grayscale and Motion off frames inspected. Held voice: warmupHow 1/1 with four silent repeats, missing-choice events 5/5; Read, Sound, fast mode changes and real jittered dragging checked.

| Line | Kind | Expected in five actions | Spoken |
|---|---|---|---|
| warmupHow | how | 1 | 1, four silent repeats |
| missing | event | 5 | 5 |

The audit snapshot predates the last voicing/stem, stale-feedback and Sound-width corrections. Recomputed the changed voicings and inspected 12 focused final frames plus 2 header repair frames, with no tool console errors. No second full audit or review round. Hinted saving, cancellation and confirmed Clear were also checked. Every started Chrome and host is closed; host.html is absent.

## Left open

Browser narration remains the fallback; recording was prohibited. Muted Chrome verifies audio state and timing, not audible timbre. The short landscape keyboard is hidden to retain notation and full answer targets, as in the build. No commits or shared-file changes.
