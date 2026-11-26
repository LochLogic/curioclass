# Scene Staging Comparison: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: scene-staging-comparison
#### Built
Watch, Compare and Layers are built in one offline HTML, using kit:curio.
Includes ten timed moments per production, silhouettes, synthesized cues, five live reactions,
two separate viewers, sample viewers, split ranking, six layers, saved reason chips and six evidence-backed opinions.
All four requested paintings are present. Build only, no commit, no polish round.
Final artifact is byte-identical to the checked Scratch candidate. All required files are present,
host.html is removed, and no test Chrome or server remains listening on ports 9980 to 9987 or 8785.
#### Numbers check
Final caption word counts: 18, 15, 12, 12, 10, 9, 17, 14, 6, 15.
128 words / 2.5 plus ten seconds and pauses gives 77.7 seconds and 63.4 seconds.
The supplied counts reproduce 70.1 and 55.8 seconds; the extra 19 caption words explain the 7.6-second difference.
Full real plays measured 78.096 and 63.680 seconds, with all ten moments and boundaries checked.
Contrast: ink/background 15.64, ink/panel 14.19, muted/background 8.03, muted/panel 7.28, gold/background 10.93.
Set checks: duplicate reactions do not increase difference; disjoint sets can give 5; identical sets give 0.
Test-set top production / viewer split was moment 2, difference 3; earlier zero-score ties followed it correctly.
Theo's sample peaks at difference 2 at moments 4 and 9; the earlier-tie rule puts 4 first. Top three: 4, 9, 1.
Missing data from either viewer produces no viewer split; the final delivery check covers both missing-viewer orders.
Evidence: numbers.json, functional.json, full-play.json and content-check.json in Scratch.
#### Feel check
Best moment: opening the meadow quarrel after Lost / Laughing stamps, comparing its pauses and blocking,
then turning a reaction into a saved opinion. The parlor and bare stage have visibly different weight and mood.
Flat moment 1: the farce faint initially clipped below the floor. Raised the fallen silhouette so the whole pratfall is visible.
Flat moment 2: close blocking made the two names merge. Replaced those labels with initials and a separate name legend.
Also kept inactive captions at full contrast and froze Layers positions immediately.
Played both whole productions; checked watching, reacting, switching viewers, comparing, inspecting and writing an opinion.
Viewed feel-comparison.jpg, placing the 1366x768 frame beside Beat Lab, plus the Snowy Mail Route bar frame.
The paintings give this its own finished visual character; silhouettes remain deliberately stylized.
#### Done when
1. PASS: Watch emphasizes the active frame and five reaction buttons; Compare replaces the frames with enlarged strips.
   Looked at 1366x768 and 680x425 in Watch and Compare.
2. PASS: real 120 ms held taps stamp immediately; Next preserves play, Stop stops, and mid-play Viewer switching separates ownership.
3. PASS: both complete plays reached all ten moments; pauses and formula checked. Motion off keeps the 10.2-second opening moment
   and its 2-second pause with zero running animations. Poses, light and cue code follow the staging table.
   Targeted sound checks confirm no rain at the faint, cancellation of its rain tail, a delayed door slam and a complete blackout overlay.
   Acting is stylized; synthesized effects have not received a by-ear listening review.
4. PASS: independent symmetric-difference examples and tie order checked; no-stamp Show splits is disabled.
5. PASS: all 60 moment/layer combinations populated; both wardrobe images load; chips persist; unstamped opinions are refused.
6. PASS: both viewers' records and chips/opinions survived reload; real Cancel kept work and confirmed Reset cleared all.
7. PASS: five held taps at 2-second pace spoke how lines once and opinionAdded five times.
   No new spoken line during playback; bothDone was observed only after the second production completed.
#### Wave lessons
- PASS, hint/voice: next actions named, hints update directly, Read stops playback and reads the hint; helper controls how-line repetition.
- PASS, focus/layout: persistent primary controls, reserved hint, prevented-scroll focus for mode evidence, step limits and Add.
- PASS, sizes: all eight required sizes inspected, including 375 in a host iframe; main Watch controls stay visible.
- PASS, no giveaways: reactions have no right answer, scores or success meter.
- PASS, honest numbers: playback formula documented, differences count types, unknown reactions remain empty.
- PASS, standards: live perception, viewer comparison, evidence-backed opinion and time-context cards teach all four listed standards.
- PASS, Motion off: no ongoing loops; same pauses and timing; all final art present.
- PASS, short choices: reaction buttons and layer tabs stay visible; all seven reason chips fit together at 680 and 375 pixels.
  Secondary Reset can require scrolling at 680x425; the comparison data table can scroll, as explained under Audit leads.
- PASS, resize: final audit found no exceptions or controls left disabled after repeated resizing during actions.
- PASS, first-tap welcome: stopped reaction taps speak it; Viewer 2's own how line takes priority; Play suppresses narration.
  Play from Layers enters Watch quietly. Reset does not speak a Play instruction over its confirmation dialog.
- PASS, unknowns: no stamp is shown as no stamp, not as neutral or agreement.
- PASS, one meaning: gold top / blue edge have text keys; reactions have both symbols and word labels.
- PASS, badge truth: viewer, production, moment, save status and play status follow actual state.
- PASS, changing hints: mode, moment and viewer changes update the current hint immediately.
- PASS, no copying: opinions require a personal stamp and an authored reason, with no correct wording to copy.
#### Audit leads
The single final audit completed within its 40-minute limit: 27 leads. Motion off, repeated resizing,
five held taps and two rapid taps were clean. No JavaScript exceptions or controls stuck disabled were reported.
Every lead is individually answered in _scratch/scene-staging-comparison/audit-dispositions.md and its JSON companion.
- 9 compact Reset-scroll leads retained: Reset is a secondary confirmation control, not a response choice.
  The primary Play, stepping and reaction controls remain visible; the panel scrolls to Reset.
- 3 evidence-field-name leads fixed with an explicit aria-label; targeted check confirms it.
- 3 compact table-width leads fixed by reducing its label column to 58 pixels; horizontal overflow is now zero at 680 pixels.
- 2 phone table-scroll leads retained: ten moment columns keep 44-pixel targets. The phone now explicitly says to swipe for moments 1 to 10.
- 1 disabled-step hint lead fixed: only Next is named during play, except at moment 10, where Previous is named.
- 1 modal keep lead is expected background coverage. The fixture now keeps the dialog instead of demanding an uncovered background hint.
- 8 first-tap welcome leads: the 5 reaction cases are fixed. The 2 Play cases intentionally suppress narration;
  Viewer 2 intentionally speaks its own how line first, following STANDARDS.
Frame-led repairs also contain Layers columns, keep reason chips together, enlarge diagram labels, preserve the whole pratfall,
keep inactive captions readable and show the latest reaction word in the miniature strip.
Targeted repairs passed with no browser warnings, errors or exceptions. The full size sweep and audit were not repeated.
The first whole-play drive promise exceeded CDP's 60-second reply limit; one smaller external-polling retry passed both full plays.
A Scratch phone probe initially used the wrong host path; its corrected retry passed with real held taps and zero console errors.
#### Frames looked at
All PNGs in bar-frames, early-frames, final-frames, focused-frames, content-frames,
phone-frames, phone-final-frames and full-play-frames were opened and inspected.
Also opened every PNG in repair-frames, phone-repair-frames, phone-repair-final-frames, small-repair-frames,
sound-tail-frames, layers-play-frames, audit-repair-frames, phone-delivery-frames and delivery-frames.
All 65 audit PNGs were inspected in audit-contacts/sheet-01.jpg through sheet-11.jpg.
Final sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe.
Also looked at grayscale, keyboard focus, Motion off, near/far blocking, faint, costume art, samples, first/last moment and Reset dialog.
#### Art made
4 generated paintings, individually inspected at final size: two sets and two wardrobe displays.
Total WebP art 320,874 bytes, about 313 KB. Final bundle 514,101 bytes, about 502 KB, under 2 MB.
No redraws were needed. Raw originals, full house style, prompts and drawn_by provenance are retained.
#### Art still to paint
None. No generated people, faces or body parts. Characters are faceless code silhouettes.
#### Engine changes wanted
None. Shared engines, docs, scripts and other tool sources were not changed.
#### Left open
- The full audit was not repeated after its targeted repairs. Its 27 baseline leads and all dispositions are preserved in Scratch.
- Reset is below the initial compact panel fold at 680x425. It remains accessible by scrolling the panel.
- Viewer-to-viewer ranking unions each viewer's two production sets before comparing. The spec does not define this aggregation;
  production-specific swaps can cancel in this ranking. The four displayed rows preserve the underlying evidence.
- Short landscape keeps two frames side by side for readability; tall widths under 900 stack them. Phones show one frame.
- Phone Compare scrolls horizontally; opinion and Layers details can need vertical scrolling. Secondary controls need compact scrolling.
- Embraces and kisses are suggestive poses rather than detailed physical acting.
- Browser narration and synthesized cue timbre need listening review. No recordings were made, as instructed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: scene-staging-comparison
#### Played
Played cold as a grade 7 solo viewer: both whole productions, reactions, Compare, samples and all Layers before builder material.
Also considered projection and same-laptop pair use. Strong sets and a worthwhile comparison; the original farce acting felt flat.
#### Findings fixed
- Blocker, general, Compare/splits: unioning each viewer's productions erased opposite reactions. Compare matching productions first, then sum.
- Blocker, general, Watch/opinion voice: two quick stamps claimed "seen both", and an empty Viewer 2 row claimed they had not watched; arbitrary text earned evidence praise. Feedback now states only what is saved and asks students to check their detail.
- Should fix, general, Compare: zero differences looked like splits and personal marks appeared on sample rows. Rank ties as specified, mark only nonzero personal differences, explain blanks.
- Should fix, general, modern actors: apron/gown/cane silhouettes contradicted the overalls wardrobe. Redrew all three modern vectors with bibs, straps, pockets and brass fasteners; added identity keys.
- Should fix, general, shared caption 6: "slowly leaves" contradicted the modern crawl. Removed "slowly" and derived displayed totals from the actual caption data.
- Should fix, general, time cards: sweeping historical-audience claims implied one correct response. Framed responses as possibilities and named the theatre's 1898 founding accurately.
- Should fix, general, opinion context: inspecting another moment did not carry into the form. Compare now selects the inspected production/moment; viewer changes clear unsaved draft text.
- Should fix, general, Stop: a rapid Stop left the entrance animation running, drifting 9.125 px in 180 ms at laptop size. Cancel actor animations and freeze stopped transitions; both tested sizes now show zero animations and zero drift.
- Should fix, general, opinion prose: "feel laughing", "feel leaning in" and "its where they stand" were ungrammatical. Use natural response and cause phrases for every option.
- Should fix, general, playback/voice: stepping could retain an old sound tail; a changed viewer could retain old narration. Cancel those tails and hush stale viewer speech.
- Should fix, general, compact layout: a wrapped key crowded the strip, samples pushed opinion controls down, and reason chips sat below detail. Shortened/reserved the key and prioritized controls at every size. The audit also confirmed compact Reset below the fold and offscreen chips/tabs; both are repaired. Reserved hint height and shorter prompts prevent text touching viewer buttons.
- Polish, general, flattest/weakest art: richer modern costume vectors; a timed fall/bounce and impact, hopping around the chair, and an exit that clears the stage. Calm retains static poses and timing.
#### Findings left
No known tool-code blocker or should-fix remains after targeted checks. The audit is incomplete, and the test host could not be closed; these verification/operational limits are not a clean exit gate.
Polish left: embraces and the formal hand-kiss remain symbolic puppet poses, as described below.
#### Break it
- Swapped Laughing/Uneasy across productions with real held taps: viewer difference was 0, now 4; moment 1 alone marked.
- Identical sets and zero ties: no false difference marks. Missing same-production evidence does not become viewer disagreement.
- Duplicate spam: [0,0,1,2] retains [0,1,2]; repeated types do not inflate differences. Independent maximum is 5 per production.
- No stamps, sample-only stamps, and whitespace: Add stays disabled. Authored "x" remains free writing, with no correctness claim, score or success chime.
- All seven chips can be selected without a success claim. Repeated filler can fill six opinion slots as saved notes, not earned points; a seventh is refused. Five real held Add taps produced five save events after queue drain.
- Mid-play Next/Previous and Viewer switch: each stamp belongs to the moment/viewer showing at that tap. Stop leaves playback false.
- Both viewers' stamps/chips/opinions survived reload. Cancel retained work; confirmed Reset cleared state and localStorage.
- 12 gate assertions passed in review-gates.json; all 60 moment/layer combinations populated. Keyboard-only reactions and mode switches passed.
#### Voice walk
Sound on, 120 ms held taps, two-second pace: welcome tap, Play P1, reaction, natural ending, Play P2, reactions, natural ending, Compare, Show splits, marked moment, Layers/Costume, Compare, authored opinion.
Heard in order: welcomeWatch, bothDone, welcomeCompare, welcomeLayers, opinionAdded. Each mode how line started once; Play/mode changes cancelled stale speech.
The full recheck reached all ten moments of each production; no narration began during playback. A 760-to-1366 live resize during the hop produced no exceptions. Later hint wording was checked on its affected side path; the final rapid-Stop repair was checked separately.
| Line | Kind | Expected | Heard |
| welcomeWatch / welcomeCompare / welcomeLayers | how | 1 each | 1 each |
| opinionAdded | event | 5 | 5 |
| stampHow while playing | visible hint | 0 spoken | 0 |
Read used current hints, including Sound off. Rapid viewer/mode changes left no queued stale line. No narration started over playback.
#### Facts checked
- Plot, age 25, apron, symptoms, Oxen Meadows, Guess/Squeezer, faint and ending: [Chekhov, Julius West translation, Project Gutenberg 7986](https://www.gutenberg.org/cache/epub/7986/pg7986-images.html). Flour and specific moves are original staging, not quoted history.
- Writing 1888-1889 and premiere 1890: [spec's A Marriage Proposal reference](https://en.wikipedia.org/wiki/A_Marriage_Proposal), corroborated by the University of Zurich bibliography.
- Moscow Art Theatre founded 1898 and staging Chekhov's longer plays: [the theatre's History](https://www.art.theatre.ru/english/history/). The 1890 production remains explicitly fictional and anachronistic.
- Farce's exaggerated physical humor and accelerating action: [World Mime Organisation, Farce](https://www.worldmime.org/en/about-mime/liaisons/101-liaisons/259-farce.html); the specified Britannica endpoint was inaccessible.
- Perception, interpretation, evaluation and cultural context: [NCAS anchors 7, 8, 9, 11](https://www.nationalartsstandards.org/). Activities: stamps, viewer comparison, authored opinions and time-card inspection.
- West's 1916 edition credit: [University of Pennsylvania Online Books catalog](https://onlinebooks.library.upenn.edu/webbin/who/Chekhov%2C%20Anton%20Pavlovich%2C%201860-1904), which also lists the 1915 edition. No claim of first translation in 1916.
- Timing, split sets, sample rows and pauses: authored Curio Class spec, independently recomputed in review-numbers.json. 127 caption words; final durations 77.3 and 63.0 seconds at 2.5 words/second plus pauses and ten one-second tails. Theo independently ranks moments 4, 9, 1; earlier moments break ties.
- Contrast: [W3C WCAG 2.1 SC 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html). Ink/background 15.64, ink/panel 14.19; muted 8.03/7.28; gold/background 10.93.
#### Sensitivity
Russian literature, property/class and marriage expectations; distress and a fictional viewer with a family heart condition.
The cultural reviewer should check the deliberately borrowed 1890 style, forced engagement, and whether sample backgrounds seem deterministic.
Fixed the plain generalizations; all samples now say fictional. No feeling is graded. Faceless actors avoid caricature; no painted people assets.
#### Flattest moment left
The embraces and formal hand-kiss remain stylized; the parlor's deliberate pauses are quieter than the farce. Kept the contrast rather than speeding it up.
#### Graphics
All four finished WebPs inspected separately and at displayed sizes: two sets, two wardrobes. Cohesive, detailed paintings retained.
Redrew the weakest vectors, not the strong paintings; no art token missing. Final bundle 518,123 bytes, about 506 KiB. Compared its finish with the saved Beat Lab and Snowy Mail Route bar frames.
Viewed all cold/pre/post and targeted repair frames, every STANDARDS size, phone iframe, grayscale, Motion off, keyboard, costume and faint states. All 62 audit PNGs were inspected in 11 contact sheets; confirmed leads were also opened at full size.
#### Audit
Audit not finished: the single 40-minute run stopped during resize stress checks. Partial report: review-audit/audit.md, 21 leads.
- 11 compact Reset leads, 3 offscreen-chip leads, 1 clipped-tab lead: fixed and re-shot at every required size. A visual follow-up caught a squeezed hint; its affected modes/sizes were repaired and re-shot.
- 4 welcome leads: expected. Viewer 2 speaks its own how line; Play suppresses narration; Reset suppresses an instruction over its dialog.
- 2 phone-harness leads: iframe context missing and consequently no hint. The occupied host served the wrong harness; these are invalid audit coverage, not a product pass. Separate 375-pixel frame checks passed.
All three control walks, five-click repeats and rapid taps completed without new script/focus/voice leads. Full resize stress was not certified. The partial report's empty resize section is not evidence it finished.
Audit timeout termination was denied; its Chrome was closed through CDP, after which the audit process exited. No second audit was run. Targeted post-audit repair runs had no browser warnings, errors or exceptions.
#### Left open
No unattended questions: matched-production viewer aggregation follows the brief's evidence goal where the spec was unspecified.
The spec asks for stampHow during play but also forbids narration over playback; preserved its visible hint and the silence rule.
No recordings were made, as required; browser speech and cue timbre were checked through logs/code, not a by-ear listening review.
One verification batch lost Chrome before results; one smaller retry passed. The first phone harness had a favicon 404; corrected harness returned zero errors.
The localhost test host on 8755 remains listening: taskkill and process inspection were denied. Owner cleanup remains necessary; the scoped helper is _scratch/scene-staging-comparison/close-host.ps1. All test Chrome ports 9950-9953 are closed, and host.html is removed.
No commits or shared-kit/script edits. Authored changes and evidence stay in the permitted tool and Scratch folders. Teacher notes, voice lines, audit states, source credits and handoff are updated.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Scene Staging Comparison: handoff after cold review

#### Structure
One offline src.html with kit:curio. CSS lays out the theater-program desk; the script holds captions,
timing/staging tables, vector actors, synthesized cues, two-viewer storage, split ranking and six layers.
The four original paintings remain. The blue-overall costumes are now also visible on every modern actor.
window.__tool exposes state, content, timeline and focused verification hooks.

#### Tricky parts
- Each duration is pause + whitespace caption words / 2.5 + 1 second. Final counts are
  18, 15, 12, 12, 10, 8, 17, 14, 6, 15: 77.3 seconds and 63.0 seconds. The status derives its total.
- Next/Previous preserve playback and cancel the preceding moment's audio. Mode changes stop playback.
- Reactions keep the latest three entries including duplicates; symmetric differences count distinct types.
- Production comparisons use the current viewer's two sets, 0 to 5. Viewer comparisons compare matched
  productions first, counting only productions with both viewers' stamps at that moment, then sum, 0 to 10.
  This resolves the spec's unspecified viewer aggregation without letting production swaps cancel.
- Earlier moments break ties. Zero entries may rank in the top three, but never receive a difference mark.
  Missing stamps are unrecorded evidence. Sample rows never inherit personal split marks.
- An opinion requires the current viewer's own stamp on that production/moment and nonempty text.
  Saving is not semantic grading. Neutral feedback asks students to check their evidence; it certifies no answer.
  Compare now starts its opinion selectors at the inspected production/moment. Viewer changes clear unsaved text.
- Stamps, chips and six shared opinions save locally in try/catch. Reset uses a confirmation dialog.
- No narration over playback. bothDone describes having reactions, not having watched the whole scene.
  stampHow stays a visible hint at eight seconds because the spec forbids narration while playing.
- Read stops the scene, then the kit reads the current hint. New viewer selections hush stale viewer narration.
- Vector initials link each moving actor to its legend. The farce faint has a short fall/bounce and floor impact;
  the hopping actor travels around the chair and the crawling exit clears the stage. Calm removes motion,
  keeping the final pose, pauses and duration. The two plays remain fixed, not student-directed.

#### Spec choices
The fictional 1890 production borrows a realistic style associated with the Moscow Art Theatre a decade later;
its time card states the anachronism. Historical audience responses are framed as possible interpretations.
Short landscape keeps two frames side by side for caption readability. Tall widths under 900 stack them;
375 shows one production. Compare's ten-column evidence table scrolls on phones. Secondary details scroll.
The final audit confirmed offscreen reason chips at several sizes and compact Reset below the fold.
Reason chips and their heading now sit with the layer tabs ahead of long evidence, while reaction stamps
stay with the evidence below. The compact panel puts Reset beside its privacy note and removes the redundant
viewer heading. See the review's targeted repair frames; the full audit was not repeated.
The shared-kit engine is unchanged. No recordings were made; smooth-narrator uses browser fallback.

#### Sensitivity
Russian literature and property/marriage expectations: review framing, including the fictional 1890 label.
The characters' physical distress and forced engagement are plot elements, not medical or relationship advice.
Students can feel uneasy about the faint; no reaction is scored. Sample viewers are fictional individuals,
not stand-ins for all older people, farming communities or families with heart conditions.

#### Art
Four generated paintings retained, with original provenance in art/prompts.json. Wardrobes use empty forms
and hangers, not people. Moving characters are faceless vector silhouettes, as the spec requests.
The review improves those vectors rather than replacing strong painted art.

#### Engine changes wanted
None.

#### Verification
See codex-review.md for the cold review and current findings. Evidence is confined to
_scratch/scene-staging-comparison, with review-prefixed checks and review-audit.
Original codex-report.md is the builder's historical record, not evidence of review verification.

#### Final review verification limits
The cold review's one audit reached its 40-minute limit during resize stress checks. Its 21 recorded leads
are dispositioned in codex-review.md. The complete control walks and voice stress checks finished;
the entire resize matrix did not. Independent phone checks passed, while the audit's phone harness
could not attach on the occupied host port. No fresh full audit was run after scoped repairs.
The final compact hint rechecks require scrollHeight == clientHeight and no overlap with viewer controls.
Rapid Stop now cancels actor animations and freezes selected-moment poses immediately. Before repair,
the entrance drifted after Stop; focused 1366 and 680 tests now show zero animations and zero drift.
Opinion prose uses natural clauses for all five responses, blocking, personal experience and uncertainty.
The main voice walk reached all 20 production moments with Sound on and no narration over playback.
Read/stale checks and five held Add events are preserved in Scratch. No recorded narration was created.
All review Chrome ports are closed. The old test host on 8755 remains because process cleanup was denied;
host.html was removed. See the review report for this unresolved operational cleanup and evidence paths.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
