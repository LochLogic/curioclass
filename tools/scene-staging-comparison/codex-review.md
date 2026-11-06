# Codex review: scene-staging-comparison
## Played
Played cold as a grade 7 solo viewer: both whole productions, reactions, Compare, samples and all Layers before builder material.
Also considered projection and same-laptop pair use. Strong sets and a worthwhile comparison; the original farce acting felt flat.
## Findings fixed
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
## Findings left
No known tool-code blocker or should-fix remains after targeted checks. The audit is incomplete, and the test host could not be closed; these verification/operational limits are not a clean exit gate.
Polish left: embraces and the formal hand-kiss remain symbolic puppet poses, as described below.
## Break it
- Swapped Laughing/Uneasy across productions with real held taps: viewer difference was 0, now 4; moment 1 alone marked.
- Identical sets and zero ties: no false difference marks. Missing same-production evidence does not become viewer disagreement.
- Duplicate spam: [0,0,1,2] retains [0,1,2]; repeated types do not inflate differences. Independent maximum is 5 per production.
- No stamps, sample-only stamps, and whitespace: Add stays disabled. Authored "x" remains free writing, with no correctness claim, score or success chime.
- All seven chips can be selected without a success claim. Repeated filler can fill six opinion slots as saved notes, not earned points; a seventh is refused. Five real held Add taps produced five save events after queue drain.
- Mid-play Next/Previous and Viewer switch: each stamp belongs to the moment/viewer showing at that tap. Stop leaves playback false.
- Both viewers' stamps/chips/opinions survived reload. Cancel retained work; confirmed Reset cleared state and localStorage.
- 12 gate assertions passed in review-gates.json; all 60 moment/layer combinations populated. Keyboard-only reactions and mode switches passed.
## Voice walk
Sound on, 120 ms held taps, two-second pace: welcome tap, Play P1, reaction, natural ending, Play P2, reactions, natural ending, Compare, Show splits, marked moment, Layers/Costume, Compare, authored opinion.
Heard in order: welcomeWatch, bothDone, welcomeCompare, welcomeLayers, opinionAdded. Each mode how line started once; Play/mode changes cancelled stale speech.
The full recheck reached all ten moments of each production; no narration began during playback. A 760-to-1366 live resize during the hop produced no exceptions. Later hint wording was checked on its affected side path; the final rapid-Stop repair was checked separately.
| Line | Kind | Expected | Heard |
| welcomeWatch / welcomeCompare / welcomeLayers | how | 1 each | 1 each |
| opinionAdded | event | 5 | 5 |
| stampHow while playing | visible hint | 0 spoken | 0 |
Read used current hints, including Sound off. Rapid viewer/mode changes left no queued stale line. No narration started over playback.
## Facts checked
- Plot, age 25, apron, symptoms, Oxen Meadows, Guess/Squeezer, faint and ending: [Chekhov, Julius West translation, Project Gutenberg 7986](https://www.gutenberg.org/cache/epub/7986/pg7986-images.html). Flour and specific moves are original staging, not quoted history.
- Writing 1888-1889 and premiere 1890: [spec's A Marriage Proposal reference](https://en.wikipedia.org/wiki/A_Marriage_Proposal), corroborated by the University of Zurich bibliography.
- Moscow Art Theatre founded 1898 and staging Chekhov's longer plays: [the theatre's History](https://www.art.theatre.ru/english/history/). The 1890 production remains explicitly fictional and anachronistic.
- Farce's exaggerated physical humor and accelerating action: [World Mime Organisation, Farce](https://www.worldmime.org/en/about-mime/liaisons/101-liaisons/259-farce.html); the specified Britannica endpoint was inaccessible.
- Perception, interpretation, evaluation and cultural context: [NCAS anchors 7, 8, 9, 11](https://www.nationalartsstandards.org/). Activities: stamps, viewer comparison, authored opinions and time-card inspection.
- West's 1916 edition credit: [University of Pennsylvania Online Books catalog](https://onlinebooks.library.upenn.edu/webbin/who/Chekhov%2C%20Anton%20Pavlovich%2C%201860-1904), which also lists the 1915 edition. No claim of first translation in 1916.
- Timing, split sets, sample rows and pauses: authored Curio Class spec, independently recomputed in review-numbers.json. 127 caption words; final durations 77.3 and 63.0 seconds at 2.5 words/second plus pauses and ten one-second tails. Theo independently ranks moments 4, 9, 1; earlier moments break ties.
- Contrast: [W3C WCAG 2.1 SC 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html). Ink/background 15.64, ink/panel 14.19; muted 8.03/7.28; gold/background 10.93.
## Sensitivity
Russian literature, property/class and marriage expectations; distress and a fictional viewer with a family heart condition.
The cultural reviewer should check the deliberately borrowed 1890 style, forced engagement, and whether sample backgrounds seem deterministic.
Fixed the plain generalizations; all samples now say fictional. No feeling is graded. Faceless actors avoid caricature; no painted people assets.
## Flattest moment left
The embraces and formal hand-kiss remain stylized; the parlor's deliberate pauses are quieter than the farce. Kept the contrast rather than speeding it up.
## Graphics
All four finished WebPs inspected separately and at displayed sizes: two sets, two wardrobes. Cohesive, detailed paintings retained.
Redrew the weakest vectors, not the strong paintings; no art token missing. Final bundle 518,123 bytes, about 506 KiB. Compared its finish with the saved Beat Lab and Snowy Mail Route bar frames.
Viewed all cold/pre/post and targeted repair frames, every STANDARDS size, phone iframe, grayscale, Motion off, keyboard, costume and faint states. All 62 audit PNGs were inspected in 11 contact sheets; confirmed leads were also opened at full size.
## Audit
Audit not finished: the single 40-minute run stopped during resize stress checks. Partial report: review-audit/audit.md, 21 leads.
- 11 compact Reset leads, 3 offscreen-chip leads, 1 clipped-tab lead: fixed and re-shot at every required size. A visual follow-up caught a squeezed hint; its affected modes/sizes were repaired and re-shot.
- 4 welcome leads: expected. Viewer 2 speaks its own how line; Play suppresses narration; Reset suppresses an instruction over its dialog.
- 2 phone-harness leads: iframe context missing and consequently no hint. The occupied host served the wrong harness; these are invalid audit coverage, not a product pass. Separate 375-pixel frame checks passed.
All three control walks, five-click repeats and rapid taps completed without new script/focus/voice leads. Full resize stress was not certified. The partial report's empty resize section is not evidence it finished.
Audit timeout termination was denied; its Chrome was closed through CDP, after which the audit process exited. No second audit was run. Targeted post-audit repair runs had no browser warnings, errors or exceptions.
## Left open
No unattended questions: matched-production viewer aggregation follows the brief's evidence goal where the spec was unspecified.
The spec asks for stampHow during play but also forbids narration over playback; preserved its visible hint and the silence rule.
No recordings were made, as required; browser speech and cue timbre were checked through logs/code, not a by-ear listening review.
One verification batch lost Chrome before results; one smaller retry passed. The first phone harness had a favicon 404; corrected harness returned zero errors.
The localhost test host on 8755 remains listening: taskkill and process inspection were denied. Owner cleanup remains necessary; the scoped helper is _scratch/scene-staging-comparison/close-host.ps1. All test Chrome ports 9950-9953 are closed, and host.html is removed.
No commits or shared-kit/script edits. Authored changes and evidence stay in the permitted tool and Scratch folders. Teacher notes, voice lines, audit states, source credits and handoff are updated.
