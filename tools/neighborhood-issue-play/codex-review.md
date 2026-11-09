# Codex review: neighborhood-issue-play

## Played

- Cold Grade 4 solo play through Street, Characters, Theater, all three scenes, Perform, Bow and reflection before reading builder notes/source. Also considered the projected class path. The handmade theater and live role reading are strong.
- Kept the street, proscenium, paper palette, set building, student pacing, flat preview and saved play. One review pass; no commits or shared-file edits.

## Findings fixed

- Should fix, general, art/prompts.json and all modes: six placeholders replaced by individually painted human puppets, all people: true. Tuned costume anchors, removed magenta fringes, and corrected Gail's blank paddle to an octagon.
- Should fix, general, restored story: Fern now speaks as a member of the newly arrived family, with ideas to share. Communication is reciprocal; a painted courtyard replaces the empty-lot set choice. The family is never the problem.
- Should fix, general, Street (school): removed the claims that a guard cannot stop cars without paint and that every town must count cars before painting. Proposals now ask the town to study crossings and traffic conditions.
- Blocker, general, misleading checks: blank/punctuation wants and fixes no longer pass. On-screen reasons and a note explain that these are plan-choice checks, not a judgment of custom dialogue or real-world effectiveness. The counter now reports views opened, not comprehension.
- Should fix, general, Characters/Scenes: removing a character could leave one-line scenes and no proposal. Restored the two-line starter minimum while preserving a setup/proposal before a reply.
- Should fix, general, Perform/Theater voice: removed the automatic preview over Perform's welcome; shortened the theater welcome; stopped the first role line cutting the Perform welcome; invalidated role speech on curtain-close. Category hints speak once and current-tab re-taps preserve speech. Own-role speech stops when another role or a scene card takes over; closed and bowed stages have no stale speaker cue.
- Should fix, general, craft: costumes sit on the painted heads/bodies; small ball artwork scales separately from its 44-pixel target; long unbroken text wraps; wheelchair movement labels describe rolling.
- Polish, general, flattest moment: the blank casting screen is now a painted audition lineup. The closing card names the student's issue.
- Should fix, general, phone Street and compact Scene 3: compacted problem-card spacing; hid the duplicate custom-fix field until needed; grouped beneficiaries. The fix and all three 44-pixel beneficiary inputs now fit together, including 375 wide. Custom fix reveal, editing and restoration passed.
- Should fix, general, Perform keyboard: Space after Curtain closed it instead of advancing. Curtain now focuses Next line without scrolling; Space then Enter advances two lines at 680 and 1366. The closing hint names the visible answer field.
- Should fix, general, Flat Preview: explicitly labeled the forced Okay-only example so it does not claim to evaluate the student's custom scene. Kept its three bubbles inside the proscenium; 680, 1366 and phone rechecks passed.

## Findings left

- No confirmed blocker or should-fix remains. Nit, voice: browser narration has no recordings and does not guarantee the voice-bank timbre; this review did not record audio.
- Nits: secondary fields in long compact editors require scrolling. Main actions stay visible; authoring is still slower than performance.

## Break it

- Repeated the same neighbor five times: one distinct view, Make the play stays disabled. Rapidly opening three different views opens material, not a claimed listening/comprehension score.
- Wants: empty, spaces and punctuation fail. Self, Nobody and Time-only blockers fail the interpersonal-clash rule. A real character blocker changes the plan check immediately.
- Fix: empty/punctuation, no beneficiary, or a beneficiary outside the cast fail. Arbitrary custom dialogue can satisfy a declared plan, explicitly labeled as such; the tool awards no writing/mastery score or best score.
- Repeated Add line stops at six; costumes stop at two; props and cast stop at three. Early Bow is disabled. The final reflection is an open question, not a scored gate or an assumed mistake.
- 1,459 browser assertions covered the check cases, all 1,440 template combinations, fix coverage and voice registry; held-input limit checks, prop keys and character removal were also run. See behavior-results.json and recheck-frames in Scratch.
- Actual reload, cancel reset, confirmed New play, problem-change retention, entrance skip, curtain-close and From the top passed in persistence/results.json.

## Voice walk

- Real held input at a two-second action pace: welcome tap, problem C, six views, Make the play, two characters, blocker, Theater, backdrop, prop and costume, Scenes, three scenes/fix/help, Stage check, Perform, Curtain, Next line, Bow.
- Expected spoken order: welcomeStreet, heardHow, welcomeCharacters, blockerHow, welcomeTheater, propsHow, costumesHow, welcomeScenes, writeFix, checkPass, welcomePerform, yourLine, bow. Log: voice-check/walk-progress.json.
- Final main-path mode welcomes: each once, with no cuts. Other how lines stopped after the student completed their action or left an own-role line. These are deliberate stale-state interruptions.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Five mode welcomes | welcome | 1 each | 1 each |
| yourLine | how | 1 | 1 |
| Props after five tab taps | how | 1 | 1 |
| checkFail | event | 5 | 5 |
| flat after five completed previews | event | 5 | 5 |

- Neighbors and the student's script remain silent for live reading. Read, Sound off/on, rapid mode changes and closed-curtain stale speech were exercised.

## Facts checked

- Fictional neighbors, feelings, wants, dates and proposed fixes are authored material, not empirical promises; notes state this. The school proposals are ideas for town review, not crossing-safety instructions.
- Crossing studies consider traffic/pedestrian volumes, speed and road conditions, and paint alone is insufficient: [FHWA STEP guide](https://highways.dot.gov/safety/data-analysis-tools/rsdp/rsdp-tools/guide-improving-pedestrian-safety-uncontrolled-crossing), [FHWA STEP Studio](https://highways.dot.gov/sites/fhwa.dot.gov/files/2022-06/step_studio.pdf).
- Crossing guard and paddle framing: [FHWA current MUTCD, 11th edition with Revision 1, December 2025](https://mutcd.fhwa.dot.gov/kno_11th_Editionr1.htm), Part 7D. The paddle is a blank toy prop, not a usable traffic sign.
- Authorized temporary play streets: [NACTO, Temporary Street Closures](https://nacto.org/publication/urban-street-design-guide/interim-design-strategies/temporary-street-closures/).
- Paper theater tradition and credit: [V&A, The story of pantomime](https://www.vam.ac.uk/articles/the-story-of-pantomime), [Pollock's Toy Museum history](https://www.pollockstoymuseum.co.uk/about-us/the-history-of-pollocks-toy-museum/). Replaced the inaccessible museum citation with its current route.
- Spolin's book/date: [Viola Spolin's publications](https://spolin.com/?page_id=212), Theater Games for the Classroom, Northwestern University Press, 1986. Conflict is this exercise's focus, not a universal claim that agreement is dull.
- TH:Cr1, Pr6, Cn10 and Cn11: [NCAS Theatre at a Glance](https://www.nationalartsstandards.org/sites/default/files/Theater_resources/Theatre%20at%20a%20Glance.pdf). Practiced through character/set choices, live performance, the community issue and personal reflection.
- Reciprocal family communication and interpreter support: [Office of Head Start, Creating Father-friendly Environments](https://headstart.gov/family-engagement/birth-5-father-engagement-guide/creating-father-friendly-environments-early-childhood-programs). Specific welcome ideas remain fictional options.
- Independent contrast calculation matches all seven spec ratios: 6.18, 5.18, 13.20, 5.56, 15.75, 12.21, 6.02. Six neighbors give 15 unordered pairs; every neighbor appears in at least one proposed fix per problem. No numerical scoring model.

## Sensitivity

- Review the reciprocal language framing, Fern's family viewpoint, and whether character blockers encourage blame. No language, nation, ethnicity or accent is assigned; appearance is not a language clue. Notes forbid accent imitation and asking students to represent a community.
- All six people were inspected, including hands, faces, wheelchair and stroller. The contact sheet is art-contact.png in Scratch. Walking stick, wheelchair and stroller are ordinary cast details. Bramble's movement choices describe rolling.
- Owner's decision overrides the animal/empty-lot passages in the unchanged spec. No unattended question was needed; choices followed that decision and the brief.

## Flattest moment left

- Drafting Scene 2 remains the slowest part. Starter lines support revision; the student still has to make the clash worth performing.

## Graphics

- Six people plus the courtyard painted; Gail's paddle redrawn once; several old cutouts re-keyed. All 28 preserved WebP files inspected on the contact sheet and active images in stage frames. Six people assets are marked people: true.
- Final art 1,234.8 KB; final bundle 1,636.0 KB, below 2 MB. Compared against opened Snowy Mail Route and Beat Lab frames; feel-comparison.png places the finished theater beside Beat Lab. Strong painted settings remain intact.
- Looked at all cold, repair, calm, grayscale, phone, long-text, audition, storage and bar frames. Audit frames/disposition below.

## Audit

- One audit completed in under 23 minutes, within the 40-minute limit: review-audit/audit.md, 50 leads, 76 frames. All frames inspected through ten sheets, with native-size lead frames opened.
- Fixed from the frames: phone Street's partly cut third card, Scene 3's hidden chosen fix/beneficiaries, and the closing hint naming a hidden restart control. Targeted post-audit frames cover 680, 800, 1000, 1280, 1366 and 375 for the editor, plus long phone views. No second audit was run.
- Retained/answered: secondary editor fields, sign wording, removal, optional cast management and New play can scroll; main actions and short scenery shelves remain visible. Modal coverage of an inert page is intentional.
- Voice leads answered: a problem tap speaks the next listening action instead of the stale Street welcome; New play suppresses speech behind its dialog. The fast closing script drops a stale own-line prompt; the two-second main walk hears it. Reached tabs sit outside the header, so explicit states cover all five modes despite zero automatic mode discoveries.
- Audit Motion off, resize, button errors, focus, repeats and quick-tap checks were clean. Tool checks had no console errors/warnings; the optional phone host alone requests a missing favicon, a harness 404.

## Left open

- No semantic grader for arbitrary student writing was added. The spec defines structural plan checks; performance and discussion test the meaning.
- No recordings, uploads, deployment or commits. Initial documentation/memory reads returned immediately but lacked an explicit subprocess deadline; subsequent shell commands used hard limits.
