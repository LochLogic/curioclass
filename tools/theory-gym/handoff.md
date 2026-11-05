# Theory Gym build handoff

## Structure
src.html starts from the kit starter and links the kit plus the grade 9-12 theme. Tool CSS sets the maple, cream and court-line blue world. The score is responsive SVG at real pixel size; the live keyboard is HTML. content.json is loaded through a bundle token and contains all spelled scales, chord vocabularies, 17 passages, four-voice realizations and 8 intervals. The final HTML has no external dependencies.

## Musical rules
Numerals compare complete spelled chord-note sets, never pitch classes. Melody membership also accepts the minor raised sixth and seventh. Set 1 lock-in checks each note and the final tonic, independently from the chord fit counter. Pivot answers compare position after both keys are locked, so later shared chords still give tooLate. Fixed soprano octaves are chosen to keep the score legible while preserving the named pitches and close voicing. Bass roots stay E2 through D4 and choose the closest previous bass; the first bass is nearest C3.

## Open questions and decisions
The spec has no open-question list. Its Art: none plan is extended with two generated material images as explicitly requested by the build brief and owner. Notation stays in code. The minor tonic order uses C sharp and G sharp, as the spec directs. Compact Workout shows the four rep rows in the Reps dialog; the score, lenses and current answer choices stay in the workbench.

The independent computation found one omission in the spec's numerical commentary: Set 3 rep 3 also ends with a chord fitting both lenses. Its final D is V in G major and I in D major. The listed pivot is still Em and all later taps still give tooLate, including this D. spec.md is unchanged. Bass-distance ties choose the lower root. The exact nearest-root rule is retained. Cold review raised the upper register of three passages so the written bass stays the lowest sounding voice.

## Sound and voice
The piano follows melody-maker's triangle pluck recipe with five partials, 1.4 second decay and 15 millisecond bass-up chord roll. Every oscillator is tracked so interruption and Sound off cut the whole passage. Lens moves leave the passage running. Curio.voice owns narration, once-only how lines, Read and event lines. There are no recorded clips; the firm-captain bank style is specified in voice/lines.json and the current build uses browser narration.

Read requested during a passage waits for the passage to finish. Any subsequent action that stops the passage drops that pending Read so it cannot speak a stale hint. Other queued narration also waits for music. The phone moves Play passage into the answer action row. In a short landscape Workout it sits in the header. The phone warm-up uses its actual width so the noteheads retain their physical size and both notes fit without horizontal scrolling.

Workout's welcome names Reps before asking for a rep tile, so the next named control is visible on compact screens. This follows the standing action-instruction rule. Opening Reps from Lens changes mode quietly before showing the dialog, then queues the welcome, so opening the picker cannot immediately cut its own welcome.

The build brief's ban on solving a puzzle by sweeping a slider conflicts with the spec's required exact live fit counter: some key reps have only one all-fitting lens. The prescribed counter and lock-in rule are retained. Cold review should judge this explicitly rather than assume the puzzle resists exhaustive key search.

## Engine changes wanted
None. No shared kit edits.

## Final build verification
The single full audit finished in 30.07 minutes with 244 leads. Motion off, resize recovery, held-click runtime checks and repeated how/event checks were clean. All 73 audit frames were reviewed. The disposition for every lead is in Scratch audit-dispositions.json and summarized in codex-report.md. The full audit was not repeated after final targeted repairs.

Final repairs preserve native notehead size on the phone, reclaim score space at 1000x625, place Play and Two lenses in the short-preview header, keep toggled utility buttons at stable widths, correct standard ghost-signature octaves, name the two Lock in controls distinctly, and let the welcome finish across repeated single-chord auditions. A wrong pivot tap now plays and highlights the selected chord before its position feedback.

Compact landscape Workout puts the two lenses beside each other to preserve readable notation and full answer targets, following the standing size rule. Full-size school laptops and phones stack them. The short landscape preview hides the piano strip; ordinary laptop and phone views retain it. At 1000x625 the cadence view hides the duplicate keyboard caption while retaining the keyboard itself.

Validation includes 972 browser assertions, all 25 reps through held clicks, a separate keyboard-only solve, five rep taps at a 2-second pace, repeated error events, deferred Read during music, a real jittered lens drag and post-audit compact frames. The final official bundle is 251,720 bytes. Art is 92,696 bytes. src.html has 1,103 readable lines, at most 157 characters per line. No em dashes, no recordings, no commits and no polish round. Every started test Chrome and server is closed; host.html is absent.

## Review next
Read codex-report.md and Scratch evidence. This is Build only, with no commits or polish round.

## Cold review changes
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
