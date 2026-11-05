# Codex report: theory-gym

Build complete. No git commits, branch changes, deployment or polish round.

## Built
Offline Lens explorer and 25-rep Workout: 8 intervals, 6 key puzzles, 6 cadences, 5 pivot passages. All 17 passages, spelled major/minor lenses, grand staff, dual numerals, gold shared-chord brackets, live piano strip, synthesized piano, two hints per rep and local progress are implemented. No commits or polish round.
## Numbers check
Independent Python recomputed all 24 spelled scales and chord vocabularies, interval letters and half steps, Set 1 membership and unique tonic endings, cadence soprano membership, pivot numerals, root ranges and upper voicings. See Scratch numbers.md and prepare.py.

One omission: the final D in Set 3 rep 3 also fits both keys (V in G major, I in D major). The spec's parenthetical list names 1, 2, 4 and 5 but omits 3. Em remains the correct pivot; every later chord gives tooLate. The spec is unchanged.

Contrast on paper: brand 5.79:1, ink 14.68:1, muted 6.02:1, fits 5.53:1, outside 5.58:1. White on brand is 6.78:1. The non-text gold bracket is 3.10:1, with its label in ink.
## Feel check
A complete held-click student path solved all 25 reps with zero runtime/log errors. It included a wrong Perfect-authentic choice on the imperfect example and a late final shared chord before the correct pivot. A separate keyboard-only path solved an interval and retained Check focus.

Best moment: lock the two keys, see the shared chord's two functions, then catch the last shared chord before the new dominant. The visible gold bracket and the played chord make the change specific.

Flattest moment 1: the first dual-lens layout hid the numeral boxes, so sliding felt disconnected from the music. Reduced control chrome and a responsive staff restored the score-to-numeral relationship.

Flattest moment 2: phone pivot locks crowded the lens arrows and made trying a key feel fiddly. Each lock now has a full target on its own row, and Play passage joins the answer row.

Compared with Beat Lab and Snowy Mail Route. Theory Gym has a quieter, score-led density, with generated maple and piano materials rather than production controls or characters. The notation remains the dominant graphic.

![Theory Gym beside Beat Lab](../../_scratch/theory-gym/feel-comparison.jpg)
## Done when
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
## Wave lessons
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
## Audit leads
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
## Frames looked at
Bar tools: Beat Lab and Snowy Mail Route at 1366x768. All current early, target, debug, check, final, extra, student, last-target, candidate, repair and audit PNGs were inspected directly or in labeled contact sheets; critical compact and phone frames were opened full size. Final repair evidence is in `candidate-repair-frames/` and `final-repair-frames/` under Scratch.

Final full-size run covers 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 through the iframe host. It includes both modes, all four workout sets, two lenses, grayscale, Motion off, key extremes, a real whole-pixel jittered lens drag and the rep picker. The drag moved C to D major with no errors.
## Art made
2 images: maple-court and piano-detail, generated with the built-in image tool using the imagegen skill. Full prompts and provenance are in art/prompts.json. Raw PNGs are in art/raw; final WebPs were made only with art.py --rekey and inspected at final size. No redraws. Art totals 92,696 bytes (90.52 KiB). Final official bundle: 251,720 bytes (245.82 KiB), below 2 MB.
## Art still to paint
None.
## Engine changes wanted
None.
## Left open
- The audit is a pre-repair snapshot. Final targeted repairs passed; the full audit was not repeated, as required by the build brief.
- Narration uses browser fallback. Recording audio was prohibited for this build; the bank voice/style and all 37 lines are supplied for later recording.
- The piano was exercised in muted Chrome, as required. The pluck recipe and note frequencies were checked; no audible listening test is claimed.
- At the shortest landscape previews, the keyboard strip is hidden to preserve the staff and answer targets. It remains visible on school laptops and phones.
- The required live fit counter permits exhaustive key search in some reps. See the Wave lessons conflict and handoff.
- Compact landscape Workout places the two lenses beside each other to meet the standing size and target rules. Full-size laptop and phone layouts stack them.

Final source: 1,103 readable lines, maximum line length 157. Required artifacts and stage=built verified. No em dashes in authored artifacts. Every started test Chrome and server is closed, and host.html is absent. No shared kit, scripts, docs, other tool, git branch or commit was changed.
