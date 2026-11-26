# Theory Gym: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: theory-gym

Build complete. No git commits, branch changes, deployment or polish round.

#### Built
Offline Lens explorer and 25-rep Workout: 8 intervals, 6 key puzzles, 6 cadences, 5 pivot passages. All 17 passages, spelled major/minor lenses, grand staff, dual numerals, gold shared-chord brackets, live piano strip, synthesized piano, two hints per rep and local progress are implemented. No commits or polish round.
#### Numbers check
Independent Python recomputed all 24 spelled scales and chord vocabularies, interval letters and half steps, Set 1 membership and unique tonic endings, cadence soprano membership, pivot numerals, root ranges and upper voicings. See Scratch numbers.md and prepare.py.

One omission: the final D in Set 3 rep 3 also fits both keys (V in G major, I in D major). The spec's parenthetical list names 1, 2, 4 and 5 but omits 3. Em remains the correct pivot; every later chord gives tooLate. The spec is unchanged.

Contrast on paper: brand 5.79:1, ink 14.68:1, muted 6.02:1, fits 5.53:1, outside 5.58:1. White on brand is 6.78:1. The non-text gold bracket is 3.10:1, with its label in ink.
#### Feel check
A complete held-click student path solved all 25 reps with zero runtime/log errors. It included a wrong Perfect-authentic choice on the imperfect example and a late final shared chord before the correct pivot. A separate keyboard-only path solved an interval and retained Check focus.

Best moment: lock the two keys, see the shared chord's two functions, then catch the last shared chord before the new dominant. The visible gold bracket and the played chord make the change specific.

Flattest moment 1: the first dual-lens layout hid the numeral boxes, so sliding felt disconnected from the music. Reduced control chrome and a responsive staff restored the score-to-numeral relationship.

Flattest moment 2: phone pivot locks crowded the lens arrows and made trying a key feel fiddly. Each lock now has a full target on its own row, and Play passage joins the answer row.

Compared with Beat Lab and Snowy Mail Route. Theory Gym has a quieter, score-led density, with generated maple and piano materials rather than production controls or characters. The notation remains the dominant graphic.

![Theory Gym beside Beat Lab](../../_scratch/theory-gym/feel-comparison.jpg)
#### Done when
1. PASS: every Set 1 passage checked against all 24 keys in independent Python and browser lock-in tests; only the specified home key is accepted.
2. PASS: 408 passage/key numeral and degree arrays match independent Python. Both lenses use the same exact spelled-note rules.
3. PASS: all 30 cadence/choice combinations checked. Perfect-versus-imperfect and Half-versus-deceptive feedback checked separately.
4. PASS: every chord position in all five pivots checked, including later shared chords. Both locked keys and the accepted pivot's two functions were exercised.
5. PASS: all 280 interval number/quality combinations checked. Missing choices and independently correct number or quality checked.
6. PASS: score and lens dominate both modes; answer controls sit under the lens. Main and compact frames inspected.
7. PASS: held Play, lens arrow and chord tap left playback running through the lens move, then stopped the passage and played the tapped chord. Read waited until music ended.
8. PASS: a hinted solve saved a hollow-dot status; unhinted solves saved filled status. Cancel preserved progress; confirmed Clear emptied state and storage. Full student run saved all 25 reps.
9. PASS: five held rep taps at 2-second gaps spoke warmupHow once; the next four were silent because heard. Three repeated missing-choice events started separately. Read and stale-event paths checked.
10. PASS at 1280x720 and 1366x768: staff, numerals, lenses and answer controls visible without page scrolling. Final 680x425 two-lens, 1000x625 cadence/pivot and phone warm-up repairs were inspected. A phone notehead measured 16.92 px high.
#### Wave lessons
- PASS, hint and voice: immediate state-owned hints, Curio.voice, once-only how lines, event lines, current-hint Read, valid/needs checks and held-click voice evidence.
- PASS, focus and layout: no focus on load; stable panel controls; score hit targets retained across redraw; keyboard-only solve ends on Check. Hints reserve height in the desktop panel.
- PASS, sizes and targets: full size run and phone iframe inspected. Compact controls retain at least 44 px targets; Sound off and Motion off do not crowd the 680 px header.
- FAIL under the build brief's literal no-sweeping rule: the spec requires an exact live fit counter, and some key reps have only one fully fitting key. Exhaustive lens search is possible. The specified counter is retained; no answer title or answer-valued picker label is added.
- PASS, honest numbers: exact fit membership rather than confidence; half-step count is exact. No estimates.
- PASS, standards: solo students analyze structure and interpret phrase endings through harmony and soprano evidence. No family engine is specified.
- PASS, Motion off: CSS ambient life is explicitly disabled; piano timing is unchanged. Mechanical calm check is clean.
- PASS, short choices: number, quality and cadence choices stay together under the score; rep rows have a separate compact picker.
- PASS, resize behavior: score uses current state and playback token; hit targets remain stable. Mechanical resize check found no exceptions or controls left disabled.
- PASS, welcome timing: no welcomeAfter; first-tap Play owns the audio path and skips the welcome.
- PASS, unknown states: unmatched chords and notes are shown as question marks and outside rings, never as fitting.
- PASS, one look/one meaning: blue lens 1, green lens 2, gold fits-both bracket, red ring plus x. Two-lens x markers identify which lens excludes the note.
- PASS, truthful badges: fit counts are recomputed from the current spelled chord or note, and moving a locked key unlocks it.
- PASS, reversible hints: mode, rep, lens, choice and result actions update the hint synchronously.
- PASS, no answer copying: puzzle instructions give the action, not the key or cadence answer. Answers and definitions appear after success.
#### Audit leads
The single full audit completed in 30.07 minutes, within its 2400-second limit, using Chrome 9991 and host 8795. It reported 244 leads. All 73 frames were inspected in 13 labeled contact sheets, with critical views opened at full size. No full audit was repeated after the targeted repairs.

Every lead has a disposition in `_scratch/theory-gym/audit-dispositions.json`:

- 192 overlap leads: expected transparent SVG hit areas over their own note, accidental, numeral and bracket graphics. These are intentional targets, not opaque boxes hiding text.
- 34 hidden-text leads: expected coverage of the inert score by the rep picker or confirmation dialog.
- 3 sideways-choice leads: expected score scrolling at 375 px, explicitly required by the spec. The short answer-choice rows remain visible.
- 2 keep-region leads: fixed the audit-state definitions so modal states require the modal, rather than the intentionally covered score, to remain visible.
- 6 missing-welcome leads: Reps was fixed by entering Workout quietly, then welcoming after opening its picker. The other five are specified behavior: lens moves stale the welcome, Play owns the music, and Two lenses owns its own how line.
- 6 quick-chord welcome-cut leads: fixed by letting an in-progress welcome finish across single-chord auditions. A targeted 0.7-second double tap logged no cuts.
- 1 warm-up Play no-change lead: a timing false positive. Three 820 ms beats finish in 2.46 seconds, before the audit's 2.5-second snapshot. The final keyboard state matches the initial helper. A targeted live check showed playing=true, five audio nodes and Stop passage.

The audit's Motion off, resize recovery, runtime/focus walk and five-click repetition checks were clean. Visual review also found compact score crowding that the transparent-hit-area leads did not distinguish: final targeted frames confirm corrected spacing at 680x425 and 1000x625. Ghost key-signature octaves, distinct Lock in labels and the phone's actual-width warm-up were also checked.

One Scratch file-iframe probe hit a cross-origin browser restriction in its test code. It was replaced with a same-origin srcdoc host; the successful rerun measured the phone notehead above. The official host-port phone checks and all final repair shots had no tool console errors.
#### Frames looked at
Bar tools: Beat Lab and Snowy Mail Route at 1366x768. All current early, target, debug, check, final, extra, student, last-target, candidate, repair and audit PNGs were inspected directly or in labeled contact sheets; critical compact and phone frames were opened full size. Final repair evidence is in `candidate-repair-frames/` and `final-repair-frames/` under Scratch.

Final full-size run covers 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 through the iframe host. It includes both modes, all four workout sets, two lenses, grayscale, Motion off, key extremes, a real whole-pixel jittered lens drag and the rep picker. The drag moved C to D major with no errors.
#### Art made
2 images: maple-court and piano-detail, generated with the built-in image tool using the imagegen skill. Full prompts and provenance are in art/prompts.json. Raw PNGs are in art/raw; final WebPs were made only with art.py --rekey and inspected at final size. No redraws. Art totals 92,696 bytes (90.52 KiB). Final official bundle: 251,720 bytes (245.82 KiB), below 2 MB.
#### Art still to paint
None.
#### Engine changes wanted
None.
#### Left open
- The audit is a pre-repair snapshot. Final targeted repairs passed; the full audit was not repeated, as required by the build brief.
- Narration uses browser fallback. Recording audio was prohibited for this build; the bank voice/style and all 37 lines are supplied for later recording.
- The piano was exercised in muted Chrome, as required. The pluck recipe and note frequencies were checked; no audible listening test is claimed.
- At the shortest landscape previews, the keyboard strip is hidden to preserve the staff and answer targets. It remains visible on school laptops and phones.
- The required live fit counter permits exhaustive key search in some reps. See the Wave lessons conflict and handoff.
- Compact landscape Workout places the two lenses beside each other to meet the standing size and target rules. Full-size laptop and phone layouts stack them.

Final source: 1,103 readable lines, maximum line length 157. Required artifacts and stage=built verified. No em dashes in authored artifacts. Every started test Chrome and server is closed, and host.html is absent. No shared kit, scripts, docs, other tool, git branch or commit was changed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: theory-gym

#### Played

Played Lens and all 25 Workout reps cold as a grade 9-12 student before reading the builder's report, handoff, notes or source. Also checked the projection layouts. The two-lens pivot is the strongest moment; the exact spelled-note model and maple workbench stay.

#### Findings fixed

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

#### Findings left

- Should fix under the gameplay rule, general, spec conflict: exact live fit feedback permits exhaustive key search. Retained the specified core mechanic as the review brief requires; changing it needs a spec decision.

#### Flattest moment left

Some key reps can still be solved by cycling the exact fit counter. The checked-answer moment now points to musical evidence; no new scoring or tasks were added.

#### Graphics

Checked both raster assets in the tool at final sizes and the code-drawn score and keyboard. Replaced piano-detail using the built-in image tool; prompt and provenance are in art/prompts.json and the selected raw image is art/raw/piano-detail.png. Maple painting retained. No people assets or missing art tokens.
Two final WebPs total 95,340 bytes. Bundle: 258,811 bytes (252.7 KiB). Compared with Beat Lab and Snowy Mail Route frames; the score-led finish stays distinct.

#### Audit

The single audit finished in 33.20 minutes, within its 40-minute limit, Chrome 9951 and host 8755. All 77 frames were inspected. Its 210 leads are dispositioned in `_scratch/theory-gym/review-audit/review-dispositions.json`: 167 transparent-hit-area overlaps, 34 intentional modal coverages, 3 required phone score scrolls, 5 specified welcome skips, and 1 warm-up playback snapshot timing lead. Runtime, focus, Motion off, repetition, quick taps and resize recovery were clean. The Sound movement row prompted a stable-width fix, verified at zero header shift.
Independent checks: 2,455 Python music checks; 911 browser assertions; all 25 reps played before source review; keyboard-only solve retained Check focus. All standard sizes, phone iframe, grayscale and Motion off frames inspected. Held voice: warmupHow 1/1 with four silent repeats, missing-choice events 5/5; Read, Sound, fast mode changes and real jittered dragging checked.

| Line | Kind | Expected in five actions | Spoken |
|---|---|---|---|
| warmupHow | how | 1 | 1, four silent repeats |
| missing | event | 5 | 5 |

The audit snapshot predates the last voicing/stem, stale-feedback and Sound-width corrections. Recomputed the changed voicings and inspected 12 focused final frames plus 2 header repair frames, with no tool console errors. No second full audit or review round. Hinted saving, cancellation and confirmed Clear were also checked. Every started Chrome and host is closed; host.html is absent.

#### Left open

Browser narration remains the fallback; recording was prohibited. Muted Chrome verifies audio state and timing, not audible timbre. The short landscape keyboard is hidden to retain notation and full answer targets, as in the build. No commits or shared-file changes.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Theory Gym build handoff

#### Structure
src.html starts from the kit starter and links the kit plus the grade 9-12 theme. Tool CSS sets the maple, cream and court-line blue world. The score is responsive SVG at real pixel size; the live keyboard is HTML. content.json is loaded through a bundle token and contains all spelled scales, chord vocabularies, 17 passages, four-voice realizations and 8 intervals. The final HTML has no external dependencies.

#### Musical rules
Numerals compare complete spelled chord-note sets, never pitch classes. Melody membership also accepts the minor raised sixth and seventh. Set 1 lock-in checks each note and the final tonic, independently from the chord fit counter. Pivot answers compare position after both keys are locked, so later shared chords still give tooLate. Fixed soprano octaves are chosen to keep the score legible while preserving the named pitches and close voicing. Bass roots stay E2 through D4 and choose the closest previous bass; the first bass is nearest C3.

#### Open questions and decisions
The spec has no open-question list. Its Art: none plan is extended with two generated material images as explicitly requested by the build brief and owner. Notation stays in code. The minor tonic order uses C sharp and G sharp, as the spec directs. Compact Workout shows the four rep rows in the Reps dialog; the score, lenses and current answer choices stay in the workbench.

The independent computation found one omission in the spec's numerical commentary: Set 3 rep 3 also ends with a chord fitting both lenses. Its final D is V in G major and I in D major. The listed pivot is still Em and all later taps still give tooLate, including this D. spec.md is unchanged. Bass-distance ties choose the lower root. The exact nearest-root rule is retained. Cold review raised the upper register of three passages so the written bass stays the lowest sounding voice.

#### Sound and voice
The piano follows melody-maker's triangle pluck recipe with five partials, 1.4 second decay and 15 millisecond bass-up chord roll. Every oscillator is tracked so interruption and Sound off cut the whole passage. Lens moves leave the passage running. Curio.voice owns narration, once-only how lines, Read and event lines. There are no recorded clips; the firm-captain bank style is specified in voice/lines.json and the current build uses browser narration.

Read requested during a passage waits for the passage to finish. Any subsequent action that stops the passage drops that pending Read so it cannot speak a stale hint. Other queued narration also waits for music. The phone moves Play passage into the answer action row. In a short landscape Workout it sits in the header. The phone warm-up uses its actual width so the noteheads retain their physical size and both notes fit without horizontal scrolling.

Workout's welcome names Reps before asking for a rep tile, so the next named control is visible on compact screens. This follows the standing action-instruction rule. Opening Reps from Lens changes mode quietly before showing the dialog, then queues the welcome, so opening the picker cannot immediately cut its own welcome.

The build brief's ban on solving a puzzle by sweeping a slider conflicts with the spec's required exact live fit counter: some key reps have only one all-fitting lens. The prescribed counter and lock-in rule are retained. Cold review should judge this explicitly rather than assume the puzzle resists exhaustive key search.

#### Engine changes wanted
None. No shared kit edits.

#### Final build verification
The single full audit finished in 30.07 minutes with 244 leads. Motion off, resize recovery, held-click runtime checks and repeated how/event checks were clean. All 73 audit frames were reviewed. The disposition for every lead is in Scratch audit-dispositions.json and summarized in codex-report.md. The full audit was not repeated after final targeted repairs.

Final repairs preserve native notehead size on the phone, reclaim score space at 1000x625, place Play and Two lenses in the short-preview header, keep toggled utility buttons at stable widths, correct standard ghost-signature octaves, name the two Lock in controls distinctly, and let the welcome finish across repeated single-chord auditions. A wrong pivot tap now plays and highlights the selected chord before its position feedback.

Compact landscape Workout puts the two lenses beside each other to preserve readable notation and full answer targets, following the standing size rule. Full-size school laptops and phones stack them. The short landscape preview hides the piano strip; ordinary laptop and phone views retain it. At 1000x625 the cadence view hides the duplicate keyboard caption while retaining the keyboard itself.

Validation includes 972 browser assertions, all 25 reps through held clicks, a separate keyboard-only solve, five rep taps at a 2-second pace, repeated error events, deferred Read during music, a real jittered lens drag and post-audit compact frames. The final official bundle is 251,720 bytes. Art is 92,696 bytes. src.html has 1,103 readable lines, at most 157 characters per line. No em dashes, no recordings, no commits and no polish round. Every started test Chrome and server is closed; host.html is absent.

#### Review next
Read codex-report.md and Scratch evidence. This is Build only, with no commits or polish round.

#### Cold review changes
Played Lens and all 25 Workout reps before reading the build report. Review evidence is under
`_scratch/theory-gym/`, separate from the builder's evidence. No shared files or git history were changed.

Replaced piano-detail with a newly generated painting whose keyboard has the correct two/three black-key groups.
The full prompt and provenance remain in art/prompts.json; art.py --rekey produced the final WebP.
The maple floor, cream workbench, notation, exact key rules and piano synthesis were retained.

Correct checks now frame the deciding notes and show them on the live keyboard. Frames clear when the answer changes.
Numerals stay near the grand staff on tall displays, and long raised-degree labels use their intended smaller type.
Workout re-entry uses the current rep's instruction; a locked pivot hint names the pivot action. Completion is announced
only on the transition to a completed set, with separate last-set and all-25 messages and controls visible on compact screens.
Current result events take priority over old narration while Read retains its kit priority. Enharmonic octave crossings
in the MIDI helper now preserve written octaves, although the current passages do not require B sharp or C flat.

The spec's live exact fit counter still permits exhaustive key search. Changing it would change the specified mechanic,
so that conflict is left open. Narration still uses browser fallback; this review did not record audio.

The cold review also caught sounding inversions in Set 2 reps 1 and 5 and Set 3 rep 4. Their upper three voices now
sit one octave higher, with the same specified pitch spellings, soprano pitch classes, nearest-root bass and close
upper spacing. High notes have downward stems and compact scores reserve their headroom. All chord basses were
checked as the lowest sounding pitch. The single full audit precedes this targeted voicing/stem repair; its affected
compact and laptop frames were rechecked afterward. The Sound button now reserves its toggled width to prevent
header controls shifting. A held score press defers redraw so playback cannot swallow the chord's click; same-set
rep changes let a still-relevant how-to finish.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
