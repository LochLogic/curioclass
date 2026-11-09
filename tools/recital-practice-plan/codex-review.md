# Codex review: recital-practice-plan
## Played
Reviewed as a grade 9-12 student and a projected classroom tool. The painted rooms, brass program board and audible practice budget feel worth keeping.
Cold play covered Set, Rubric, four weeks and the final recital piece before reading builder materials. Its 75-second wait ended before the automatic sheet; the later keyboard-only recheck reached natural completion in about 98 seconds with no exceptions.
## Findings fixed
- **Blocker, general, Listen/Recital:** x marks, timing references and measured BPM exposed ear-rating answers. Diagnostics, velocity shading and readiness readouts now wait for judgment and reveal; unplayed notes stay unknown. Recital shows captured target BPM until its tempo judgment is revealed.
- **Blocker, general, rubric changes:** a global reveal exposed newly added criteria before rating. Each criterion now has its own reveal record and gate.
- **Blocker, general, agreement:** copying the revealed answer could masquerade as hearing correctly. Feedback compares immutable first ear; the same reveal cannot be farmed.
- **Blocker, general, recital:** skipping every passage could claim completion. Skips/missing takes are named; changes invalidate the record; old completion-only saves lose that badge; fewer than two pieces cannot begin.
- **Should fix, general, voice:** the main path dropped Listen's how line. Shorter Practice/Listen/Recital instructions and a completion-time rating instruction now start in the proper sequence.
- **Should fix, general, compact Listen:** five revealed criteria overlapped. Content-height feedback rows and a shared toolbar keep the controls clear; all five initial rating groups fit at 680x425 and 375x812.
- **Should fix, general, long introductions:** 200 wide characters covered the title/program/keyboard. Long text now scrolls in its own bounded area, with the presentation controls visible.
- **Should fix, general, focus:** revealing the meter disabled its focused button. Focus now goes to the scrollable comparisons; stale meter instructions are hushed.
- **Should fix, general, hints:** a fitted set and finished week 4 did not clearly lead onward. Hints now name Rubric/Notes or Recital as appropriate.
- **Should fix, general, final audit frames:** phone programs hid reorder buttons; the 1280x720 board clipped Flow. Program rows now expand, Notes moves to the phone header, and compact practice spacing exposes Flow. Venue paintings remain in the choices/full recital scene.
- **Polish, general, numbers:** a 0.257-second overrun said Over by 0:00. It now says Just over 10:00; the under-limit counterpart is also handled.
- **Polish, general, words:** one wrong note is singular; rating endpoints recall the student's descriptions; the discussion question no longer assumes neglect.
- **Polish, graphics/play:** rekeyed the metronome's green fringe and added a shaded, pitch-accurate recital keyboard driven by the saved audio events. No new mode, topic or score.
## Findings left
- **Spec conflicts:** exact note-for-note engraving versus the explicit ornament-free Minuet; approximate model examples versus the written equation; full passages versus 8-15 seconds/about one minute. The explicit content/formula remains unchanged.
- **Judgment calls:** the senior-center notes assume childhood/film familiarity. These fictional venue suggestions need the cultural review named below.
## Break it
- Right notes/beat/tempo/dynamics: tried no-listen clicks, partial play then Stop, constant guesses, option sweeps, copying revealed answers, repeat reveal, swapping criteria and opening the sheet. Completion gates hold; first judgments survive; new meters remain hidden; copied revisions earn no first-ear agreement.
- Readiness/minutes/method/Flow: swept every allocation to maximum, tried zero-minute weeks and replayed old takes. Budget never exceeded 270 minutes; a zero-minute week applies an 8% readiness reduction; a replay is immutable; the sheet labels the simple simulation assumptions. No best score exists.
- Recital: Skip-all, Skip mid-take, Stop, changed program and an unrated sheet. Audio stops immediately; skip-all records four skips and no completion; an unrated sheet reveals no meter.
- Final shortcut regression: **28/28 passed**, `_scratch/recital-practice-plan/break-final-results.json`.
- Keyboard-only Tab/Enter/arrow run: program, rubric, allocation, four weeks, take/rating/meter and uninterrupted recital to the sheet passed, with no runtime exceptions.
## Voice walk
Sound on, Motion on, held 120 ms clicks at a two-second action pace: venue, four Add buttons, Rubric/three criteria, Practice/sliders, practice week, Play take, ratings, meter, next three weeks, Recital/Begin.
Started in order: welcomeSet, setFits, welcomeRubric, welcomePractice, listenHow, rateHow, meterHow, welcomeRecital. Each how started once. Some completed actions cut their instruction; none of these how lines was lost unstarted on this path.
| Side-path line | Expected | Spoken |
|---|---:|---:|
| setFits, genuine fit entries | 5 | 5 |
| listenHow, five Listen entries | 1 | 1 |
| tired, five matching budgets | 5 | 5 |
| agree, five known-correct first judgments | 5 | 5 |
Evidence: `review-voice/recital-skipped.json`, `review-events/results.json`, `review-keyboard/result.json` in Scratch. The fatigue line names a budget/model assumption, including when minutes are unused.
All ten fixed strings match voice/lines.json and allLines. Chrome was muted as required; these are utterance-start/scheduling checks, not a headphone judgment. Umbriel recordings remain absent under the no-recording rule.
## Facts checked
- **Petzold/Minuet:** Christian Petzold attribution, former Bach credit and the circa-1725 notebook context: [IMSLP work record](https://imslp.org/wiki/Minuet_(Pezold,_Christian)). Checked both-hand attacks against the saved Waldersee score and explicit spec sequence; omitted ornaments remain a stated conflict.
- **Bach/Prelude:** BWV 846, 1722, WTC Book I: [IMSLP work record](https://imslp.org/wiki/Prelude_and_Fugue_in_C_major,_BWV_846_(Bach,_Johann_Sebastian)). The four attack shapes match the explicit brief; no claim of literal engraved sustain durations.
- **Satie:** 1888, Lent et douloureux, 78 bars in 3/4, bars 5-12 including the tied F sharp: [IMSLP score](https://vmirror.imslp.org/files/imglnks/usimg/0/0d/IMSLP08284-Satie_-_Trois_Gymnopedies_%28typeset%29.pdf), compared with saved page 1.
- **Joplin:** 1902, Not fast, both hands of A-section bars 5-8/printed bars 9-12 and 152 performed bars: [first-edition score](https://s9.imslp.org/files/imglnks/usimg/8/80/IMSLP02607-Joplin_-_The_Entertainer.pdf). The 1973 film association is confirmed by [AFI](https://catalog.afi.com/Film/54391-THE-STING).
- **Invented content:** Night Bus notes, dates, venues/audience size, difficulties, targets and numerical model are defined by the spec and labeled fictional/model content. They are not research findings about a musician.
- **Numbers:** independent Python gives piece lengths 1:39, 2:07, 3:15, 4:00, 1:14 and exactly the three listed-tempo sets 9:54, 9:29, 9:35, including 20 seconds per introduction. Four-week ranges match the equation; 60x7 has 357 effective minutes, slightly less than 60x6's 360.
- **Contradictory examples:** Entertainer even allocation gives 63.01%, 35% allocation gives 87.91%, and the other hard passages give 84.96%/72.38%. The spec's 64%/85%/72-79% narrative is approximate or wrong; formula wins. Evidence: numbers.json and review-math.json in Scratch.
- **Contrast:** independently recomputed brass/panel 10.74:1, brass/section 10.18:1, dark/brass 11.46:1, body/panel 14.70:1, muted/section 7.71:1. Grayscale frame inspected.
- **Practice rest:** [BAPAM](https://www.bapam.org.uk/when-the-curtain-goes-up-again-building-our-fitness-to-perform/) supports practice breaks; it does not validate this tool's invented seven-day/0.85 rule. The spoken line now makes that distinction.
- **Standards:** selection/context/introductions, allocation/revision, presentation, authored criteria/listening and personal reflection provide actions for Pr4, Pr5, Pr6, Re9 and Cn10: [NCAS Harmonizing Instruments](https://nationalartsstandards.org/content/harmonizing-instruments-introduction). This is a simulation, not evidence of actual instrumental performance proficiency.
## Sensitivity
European/American piano examples do not represent all music cultures. A cultural reviewer should check Petzold/Bach attribution, Joplin's authorship before the later film, and assumptions about older audiences. Five paintings have no people; the code audience uses faceless silhouettes. No Native, religious or hard-history content.
## Flattest moment left
Writing rubric descriptors is deliberately quiet. The recital's long listening stretches now have a synchronized keyboard; full required passages and modeled slow tempos still make neglected programs take longer.
## Graphics
All five finished WebPs inspected; the four warm interiors were retained. The metronome was reprocessed from its raw painting with free art.py --rekey and holes:true. No raster redraw/addition or people asset was needed.
Compared frames with existing Beat Lab and Snowy Mail Route bundles without rebundling or changing them. The recital retains depth, material, light and its brass accent. Final bundle size: 827 kB (826,598 bytes).
## Audit
Single final audit completed within 40 minutes: all STANDARDS sizes/states, Motion off, held/repeat/quick clicks and mid-action resize; no exceptions or stuck controls. All 100 frames inspected through nine contact sheets, with native frames for confirmed faults. Evidence: `review-audit/audit.md` in Scratch.
Its 16 leads: one phone reorder defect repaired; three rubric-table and three program-notes editor scroll leads are intentional long editors; the hidden background hint is inert behind the modal; two disabled prerequisite mode buttons are expected; five first-Add welcomes are deliberately canceled as stale per spec; the Recital disabled-Begin lead refers to canceled narration (runtime cancellation rechecked). No short choice list remains clipped.
After the audit, twelve focused frames passed with zero console errors: phone programs with 0/1/2/4/5 pieces (all Add/order/venue/Notes targets visible, at least 44 px, no scroll); Notes resize/modal focus restoration; unjudged recital BPM at 680/1366/375 and revealed BPM; 1280 board/Listen. All twelve opened at native size. `review-close-checks.json` records assertions. No second audit or broad review was run.
## Left open
No kit or spec edits, commits, external uploads or registrations. All authored changes/evidence are inside the two permitted folders. All browser/server commands exited; the temporary host is removed and ports 8755/9950-9957 are closed. WMI process inventory was denied, so cleanup verification uses command exit/driver cleanup and port checks.
Procedural limits: the cold run stopped before its automatic sheet; later full keyboard validation completed it. The first required-doc read used the tool's wait bound rather than an explicit subprocess timeout; subsequent commands have explicit limits. A long drive evaluation timed out at its 60-second CDP cap; the uninterrupted recital was then checked with bounded separate polling.
The formula/example, engraving/explicit-sequence and recital-duration conflicts require spec decisions, not an improvised new feature. Recorded-voice naturalness and piano timbre remain unverified acoustically.
