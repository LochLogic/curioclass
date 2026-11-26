# Dance Hall Decades: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: dance-hall-decades

#### Built

Build only in S:/CurioClass-codex. Only this tool and its Scratch folder were written. No git commit, branch action,
or polish round. Offline single-file explorer for grades 6-8: eight painted halls and object markers, counted
footprints, the temporary kit figure, original grooves, historical source cards and a saved comparison mode.
Files: src.html, tool.draft.json (stage built), notes.md, voice/lines.json, audit-states.json, handoff.md,
art/prompts.json, sixteen WebPs and the generated HTML. Report prepared in Scratch and finalized last to honor the
owner's instruction to stop when codex-report.md is written.

#### Numbers check

Scratch setup.py / numbers.json independently recompute counts, ratings, date differences and WCAG contrast.
Phrase beats: 4, 6, 8, 8, 8, 4, 3, 18. Lindy has eight placements over six swung beats. Hustle includes a half-beat
pickup within its three-beat cycle. Musical meter continues across dance phrase boundaries.
Contrast matches the spec: ink 15.50:1 / 13.86:1; muted 8.81:1 / 7.88:1; violet on background 6.97:1.
Electric Slide counts 15-18 conflict with the supplied prose: the verified eighteen-count teaching sheet controls.
Ballard's recording session was in 1958; the screen correctly says released in 1959. The spec conflated those dates.
The 1973 event was a fundraiser; free-admission wording is not repeated. Silver's 1976 origin date is attributed.
The generic closed-hotel-ballroom claim and universal wedding-access claim are qualified. See notes.md for evidence.

#### Feel check

Played every hall, both modes and the comparison writing path. Best moment: following the Electric Slide through
count 18 as the demonstrator turns to a new wall, with the next loop still on the same groove.
Two flattest early moments: repeated stamps obscured the path on long / repeated-position phrases, and choosing
evidence did little for the student's closing text. Fixed with a single live stamp, numbered phrase strip and
an editable sentence that can use the selected evidence. Also made kicks legible with a quarter-view figure.
The painted rooms have foreground, floor and architectural depth, with specific period objects and warm light.
Scratch feel-comparison.jpg places this tool beside Beat Lab. The room painting matches the reference's care;
the temporary figure remains visibly simpler, as explicitly directed. No people were generated.
Both bar tools were bundled to Scratch, opened and inspected. No bar tool folder was written.
Browser checks were muted, so this is not a headphone judgment of timbre or an embodied expert dance review.

#### Done when

1. PASS: hall and footprint scene dominate at 1366x768 and 680x425, timeline above. Full-size and targeted frames.
2. PASS for timing: Charleston / mambo at Learn and Party, trace intervals continuous, visual lag at most 17.7 ms
   in the recorded check. Pattern totals all match. Teaching adaptations and the pending embodied check are explicit.
3. PASS in tested live paths: speed edits preserve time continuity, Mirror changes immediately, tabs keep music going.
   A request inside the 35 ms lookahead can affect the following unscheduled interval; not claimed sample-exact.
4. PASS for sourced explorer content and no reward system. Fact cards are summaries, not fabricated quotations.
   FAIL for complete independent content verification: full teaching-video / embodied and fresh cultural review remain.
5. PASS: four Me rows and two distinct dances; selected criterion, strengths, evidence and writing save / restore.
   Reset removes the profile; Copy returns exactly the displayed sentence (clipboard stub test, no OS clipboard changed).
6. PASS: no spoken line during the tested groove; all eight story keys start once and stay once on reentry.
   Held clicks at two-second spacing and queued-story-after-Stop paths checked. No audio recordings were made.
7. PASS: projector count is 90 px at 1920x1080, exceeding 72 px. Compact footprint labels are at least 14 px.

#### Wave lessons

- Hint / voice: PASS, synchronous hints, kit Read, heard-key selection, no welcome delay before Play.
- Focus / layout: PASS in held-click and keyboard checks; controls stay mounted, main controls precede timeline in DOM.
- Sizes: PASS hall controls at every required size. Compact comparison was tightened so four sliders and both
  judgment sets fit at 680x425. Phone comparison and secondary writing / history text use scrolling.
- No giveaways: PASS / not a quiz. No hidden right answer, scores, prize meters or cultural rankings.
- Honest numbers: PASS, tempos and comparison positions labeled as Curio Class teaching descriptions.
- Standards: PASS activities for all five standards mapped in notes.md, with solo comparison and evidence writing.
- Motion off: PASS, no perpetual CSS animation; poses hold per count and timing stays intact.
- Short choice sets: PASS compact comparison targeted frame; phone sections follow one another in the page.
- Resize mid-animation: PASS, full audit stress found no exceptions or stuck controls; the current event survives relayout.
- Late welcome: PASS, no welcomeAfter; Play does not wait for narration.
- Unknown shown as unknown: not applicable; historical summary cards and authored positions are identified plainly.
- One look / one meaning: PASS, L/R letters, count numbers, and Me / A / B shapes supplement color.
- Badge truth: PASS, hall numbers identify places; visited dots mean navigation only, no completion award.
- Hint changes back: PASS, hall, tab and mode hints are updated immediately in both directions.
- No answer by copied words: not applicable to this explorer; evidence chips support a student-authored judgment.

#### Audit leads

One full audit completed: Scratch audit/audit.md, 52 captured PNGs, 276 original leads. All frames inspected.
Motion off and resize stress were clean, with no runtime exceptions or stuck disabled controls. The full held-click
walk and its five-click / two-second voice checks completed. Repairs were checked in affected states, not a second audit.

- Fixed narrow Halls targets with a 44 px minimum; textarea names with explicit aria-labels; last-hall focus by
  moving focus to Previous hall; badge bounds with separate unrotated rows; Sound widths to prevent phone wrapping.
- Most footprint leads counted text inside invisible SVG ancestor groups. Inactive crowded stamps now use
  display:none. Compact diagrams and Hustle also use a single live stamp. Five post-repair snapshots have no
  target, overlap, clipping, hidden-text, name, hint, line-crossing or horizontal-scroll findings.
- The compact chart keep-region lead is fixed: all four Me rows and both complete judgment sets fit at 680x425.
- Rapid repeated mode / hall taps no longer hush a line for an unchanged view. The rechecked Halls, My way of moving
  and mambo-marker pairs speak once without cuts. First Play / hall / tab actions deliberately skip the welcome
  when they have their own action or instruction, as STANDARDS requires; welcomeAfter is not used.
- Retained: the phone timeline scrolls sideways by explicit spec. Phone judging and writing follow the chart in
  the page. Source links at the ends of long history articles require internal scrolling; these are citations,
  not a hidden short answer set. The visible action hint and hall transport remain available.
- The first custom host run logged a host favicon 404. The host was repaired; the subsequent phone check was clean.
  No tool runtime warning or exception was found in the drive batches.

The audit captures precede final targeted repairs, so this is not a claim of a second clean full audit. Final
evidence: post-frames, quick-frames, welcome-fixed, their saved JSON checks, and closing_checks.py. The complete
original audit remains available for the cold reviewer, including all retained scrolling and welcome leads.

#### Frames looked at

Scratch bar-frames (2), early-frames (3), early-fixed (3), layout-frames (1), functional-frames (6),
full-frames (12), hall-frames (12), targeted-frames (6), final-frames (5), post-frames (6), quick-frames (4), welcome-fixed (1), and all 52 audit frames in nine audit-sheets.
All captured PNGs inspected directly or in named contact sheets; all eight background WebPs inspected individually,
and all sixteen final assets checked on the dark art sheet. Full standards-size set run once late; repairs re-shot
only in the affected states. Grayscale, Motion off, a hosted 375-wide view and keyboard Play are included.

#### Art made

Sixteen people-free paintings made with the built-in OpenAI image tool: eight halls and eight isolated markers.
Full prompts and provenance are in art/prompts.json. Raw PNGs in art/raw; only art.py --rekey used for processing.
No downloaded art, recorded audio or paid art.py generation. No redraw needed after inspection.
Art: 1,183,058 bytes (1,155.3 KiB). Bundle: 1,782,461 bytes (1740.7 KiB), below 2 MB. All art is used visibly; missing people tokens stay hidden.

#### Art still to paint

42 people:true pose assets reserved for the owner's next painter. PAINTED_POSES and figureRenderer provide the
swap point. Whole-body weight, partner connections, scuff / turn directions and mirror orientation need that pass.
The kit's faceless figure is the intended temporary renderer. Painted poses will hold per count until extended.

#### Engine changes wanted

None required. A reusable future music / clock API could accept explicit audio times and a cancellable output bus.
No kit, docs, scripts or neighboring tool source was changed.

#### Left open

- Painted people, exact painted-facing integration and owner review of those images.
- Browser speech fallback in place of recorded Vindemiatrix narration; no recordings requested or made.
- Embodied accuracy and full video checks, especially the requested short Hustle and adapted mambo / Stroll patterns.
- Headphone review of synthesized groove balance and historical character; these are original teaching sketches.
- Fresh cultural / historical review before publication, including access and credit wording.
- Long source cards and secondary comparison writing scroll on compact screens; phone comparison is sequential.
- The full audit was not repeated after repairs. Targeted results are listed above.

Cleanup: every Chrome and server started for this Build is closed. Ports 9990, 9991 and 8795 were verified closed.
host.html is removed. No commit, deployment or polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: dance-hall-decades

#### Played

Cold as a grade 6-8 student: all eight halls, Play/Stop, Learn/Party, Mirror, room/credit tabs, then My way of moving, before reading builder prose or source. The rooms feel inviting; the access questions give movement a reason.
Best moment: contrasting Cotton Club and Savoy after trying their patterns. Kept the rich halls, timeline objects, grooves and unscored exploration. The two flat spots were the buried question and abstract demonstrator: raised Talk about it and painted dancers. Finish comparison: Scratch feel-comparison-review.jpg beside Beat Lab; Snowy Mail Route was also inspected as a finish reference.

#### Findings fixed

- **Blocker, comparison:** changing Charleston to Lindy kept "kicks need space" as Lindy evidence (cheap-before-stale.json). Dance changes now clear tied reasons/writing; criterion changes clear judgment evidence. Retested: stale-fixed.json, criterion-fixed.json.
- **Should fix, art/teaching:** replaced code figure with two painted adults, four people assets, seventeen selected poses and an explicit figureRenderer swap seam. Distinct touch, behind-cross, back-tap, grounded-turn and scuff studies separate unlike weight actions. Redrew the standing/dipping Twist pair.
- **Should fix, teaching:** Electric Slide left turn now occurs on 17, scuff on 18, matching Salerno. Cue, wall label and pose agree. Notes explain the spec's incomplete ending and the build's existing common-version adaptation.
- **Should fix, voice:** shortened three action instructions to fit the required pace; stopped the Halls instruction in Moving. First Dance-tab tap now speaks; quick Next taps preserve the still-valid shared instruction. Stop can deliver an unheard instruction; narration does not play over the groove.
- **Should fix, craft:** corrected mirrored arrow origins, paired L/R placement, repeated Mambo count labels, paused support feet, last Twist label drift and clipped Georgia 4/7 descenders. Keyboard focus exposes each row's authored rationale.
- **Should fix, history:** replaced broken Palladium source, linked the actual Manning recollection, credited Bunny Wailer and Van McCoy, and attributed the disco-backlash interpretation in voice as on screen.
- **Polish:** placed Talk about it first and reset historical scroll on hall change; labeled comparison as a draft. Restored judge spacing after my overbroad CSS edit; moved select focus rings inside their controls to keep labels visible, then checked affected layouts.

#### Findings left

- **Should fix, spec decision, Hustle:** required tap-left/step-left/back-right/in-place-left does not establish a verified continuous partner basic. Kept the requested sequence, labeled it a short tap introduction, added a right-weight reset cue. A replacement needs a spec decision and embodied teaching check; this review does not certify the loop for publication.
- **Polish, voice:** browser speech is the fallback; no recordings of the named bank actor exist here. No headphone listening or professional dance-teacher validation is claimed.

#### Break it

No score, success meter, timer, badge, quiz or win gate exists. Visited dots record navigation, not mastery.
- Sliders: real end-to-end drag and arrow keys (real-sweep.json); extremes move Me only. The 32 dance positions remain authored, explicitly "not measured"; no reward is farmed.
- Judgments: tried every strength/reason in turn, then changed criteria/dances. They remain student drafts, with no correctness or completion reward. The genuine stale-evidence exploit now clears instead of fabricating support (review-cheap/).
- Duplicate picks: tried the same dance twice; other selection is disabled, picks stay distinct (distinct-fixed.json). Changing the stronger choice clears/replaces tied evidence.
- Blank/nonsense reflection: Copy may copy an incomplete draft with blanks, never marks it correct. Exact clipboard payload checked with a local stub (copy-fixed.json). Persistence and Reset checked; Reset clears only this comparison.
- Five held taps 2 s apart, paired 0.7 s taps, native Enter, tempo/Mirror/tabs during play and resize stress: no stuck controls or false success. Quick Next's cut instruction was repaired and retested.

#### Voice walk

Default Sound/Motion on, real 0.12 s held clicks at 2 s gaps: marker, Play, Stop, The room, Who made it, Next, The dance; repeat all eight, then My way of moving. Read __tool.vlog, not merely line registration.
main-after-audit.json: Press Play -> Open Who made it -> Discuss Talk about it -> stories 0-7 -> Set where you stand on each line. Each action instruction and Moving welcome starts once and finishes without a cut. Stories cut when the student leaves their hall/tab at this accelerated pace; no stale story continues on another screen.
First marker's own instruction intentionally replaces Halls welcome under BASELINE; premise remains in hint/Read. First current-tab tap and quick Next finish Press Play (selected-tab-first.json, quick-next.json). Five-repeat audit clean. Read speaks current hint with Sound off and stops music (read-side.json). All 13 runtime lines exactly match voice/lines.json.

#### Facts checked

- Charleston Black Southern/Charleston roots and 1923 Runnin' Wild spread: [Charleston County Public Library](https://www.ccpl.org/charleston-time-machine/tracing-roots-charleston-dance), [LOC recording essay](https://loc.gov/static/programs/national-recording-preservation-board/documents/Charleston.pdf). Cotton Club 1923, Black performers/white clientele: [National Archives Foundation](https://archivesfoundation.org/newsletter/sights-and-sounds/) and spec's Britannica Cotton Club entry; not every Harlem venue.
- Savoy 596 Lenox, 1926-1958, block-long/about 4,000, Cats' Corner, integrated policy, Lindy around 1927 and Manning dancing/skin recollection: [Savoy history and reproduced recollection](https://en.wikipedia.org/wiki/Savoy_Ballroom), [Brooklyn Public Library](https://www.bklynlibrary.org/blog/2022/12/01/cutting-rug-evidences), [NEA Manning biography](https://www.arts.gov/honors/heritage/frankie-manning). Fact card explicitly paraphrases.
- Mambo Cuban roots, Puente/Machito/Rodriguez, Cuban/Puerto Rican bands and mixed Black/Jewish/Italian/Latino New York floor: [Lincoln Center](https://www.lincolncenter.org/feature/legacies-of-san-juan-hill/latin-jazz-and-san-juan-hill), [TeachRock Palladium handout](https://teachrock.org/wp-content/uploads/Handout_3_-_1950s_Manhattan_2.pdf?x81697=). Unsupported closed-hotel generalization remains softened; no "first integrated floor" claim.
- Bandstand local 1952, ABC August 5, 1957, LA 1964: [American Bandstand chronology](https://en.wikipedia.org/wiki/American_Bandstand). Ticket exclusion by 1954, Black music/white televised dancers: [Matthew Delmont admission-policy evidence](https://nicestkids.com/nehvectors/nicest-kids/protesting-segregation-on-bandstand), The Nicest Kids in Town (UC Press, 2012). Stroll facing lines, Black R&B context, central strut: [Richard Powers reconstruction](https://socialdance.stanford.edu/Syllabi/Stroll); eight-count side-touch is labeled adaptation.
- Twist: Ballard recorded November 1958, released January 1959; Checker hit 1960: [LOC essay](https://www.loc.gov/static/programs/national-recording-preservation-board/documents/TheTwist.pdf). Screen correctly says released 1959. Sock-hop gym/shoes-off and dancing apart: spec's Chubby Checker reference and [Library of Dance](https://www.libraryofdance.org/dances/twist/). This did not invent dancing apart; adult criticism is historical context.
- Bronx: Cindy Campbell fundraiser/Kool Herc, August 11, 1973, 1520 Sedgwick/community room: [Birthplace of Hip Hop](https://birthplaceofhiphop.nyc/our-story/), [Herc/Cindy interview](https://hiphopandpolitics.com/2012/08/11/august-11th-1973-hip-hop-had-its-first-party-an-intv-w-kool-herc-his-sister-cindy/). Charged admission, not free: [Smithsonian](https://www.smithsonianmag.com/smithsonian-institution/how-the-block-party-became-an-urban-phenomenon-180980560/). Neighborhood disruption: spec's Cross Bronx Expressway history. Landmark is not an invention date for every breaking element.
- Disco Loft from 1970, Black/Latino/gay communities: [Richard Powers](https://socialdance.stanford.edu/syllabi/disco_lifestyle.htm). Latino Hustle before Van McCoy's 1975 hit: [Smithsonian Hustle history](https://www.smithsonianmag.com/smithsonian-institution/fifty-years-ago-this-irresistible-disco-song-and-dance-craze-swept-the-nation-and-changed-the-music-landscape-180986460/). Chicago 1979 destruction/contested meanings: [PBS The War on Disco](https://www.pbs.org/wgbh/americanexperience/films/war-disco/); "many saw" retained in screen/voice.
- Electric Slide attributed/disputed Silver 1976 date, 22 original/18 common, Bunny Wailer writer/Marcia Griffiths recording: [Electric Slide history](https://en.wikipedia.org/wiki/Electric_Slide). 2007 claim/dispute: [EFF annual report, p6](https://www.eff.org/files/eff-2007-annual-report.pdf). No current legal or universal-access claim.
- Footwork: Charleston four actions [CLDAA](https://www.cldaa.org/home/what-is-line-dance/line-dance-terminology/); Lindy rock/step, 3-and-4/5-and-6 [SwingHop](https://swinghop.ch/moves/10-six-count-basic); Mambo break/replace/close/pause and historical on-one/on-two [Library of Dance](https://www.libraryofdance.org/dances/mambo/). Stroll adaptation: Powers above. Twist pivot/dip/rise: Library of Dance above; optional opposed shoulders [Noah Rabotin, Decibel Dance](https://www.decibel-danse.com/en/advice/dance-choreography/).
- Toprock alternating cross/return: Alpha Trion's Bboy Zone basics, spec's Moses Mwanjelwa tutorial; [Red Bull BC One](https://www.redbull.com/int-en/understand-the-basic-elements-of-breaking) names cross step. Bboy Zone has dated offensive terminology, so is not added as a student link. Hustle loop remains unverified. Electric Slide eighteen counts, specifically 15 back/16 touch/17 turn/18 scuff: [Mike Salerno sheet](https://www.wesquaredance.com/KSDCA/Lines/ElectricSlide.pdf), [Dance With Me](https://dancewithmeusa.com/how-to-do-the-electric-slide/).
- Recomputed review-computation.json/review-numbers.json: beat totals 4,6,8,8,8,4,3,18; Lindy eight placements/six beats; Hustle .5+1+1+.5=3; all 32 chart positions match spec. Tempos/ratings are Curio Class choices. Five clave attacks over eight beats: [University of Puget Sound](https://musictheory.pugetsound.edu/mt21c/ThreeTwoClave.html); grooves are synthesized sketches, not recordings.
- WCAG luminance recomputation: ink/background 15.50, ink/panel 13.86, muted/background 8.81, muted/panel 7.88, brand/background 6.97, brand/panel 6.23. Count 46 px at preview/90 px at 1920; diagram labels at least 14 px. Shared-clock traces verify Mambo tempo .6667 -> .3333 s, maximum observed visual lag 27.205 ms in that sample, not a universal latency guarantee.
- [NCAS](https://www.nationalartsstandards.org/): Re7 counted patterns/context; Re8 access interpretation; Re9 criterion/evidence; Cn10 personal experience; Cn11 creator/venue history. Notes retain required three opening headings and practical home support.

#### Sensitivity

Fresh cultural review: Black American/Cuban/Puerto Rican/Latino credit; Savoy recollection versus broader racism; Philadelphia TV exclusion; Cindy Campbell's agency; gay communities' disco role and attributed backlash; disputed Silver origin/ownership. Modern summaries are not passed off as primary quotations.
Cross step avoids the stereotyped Native American alternate name, explained only for adults. No segregation reenactment or representing a whole community. Modern varied adults are practice models, not historical portraits. Both ambulant; seated tracing/observation offered. Jo's requested hearing aid is too small to count as a strong visible access cue. Anatomy, support weight and representation still merit embodied/cultural review.

#### Flattest moment left

Comparison asks for a written claim after dancing's sensory payoff; it needs a real reason, not an automated grade. Visible discussion and draft framing help. Retained the quieter evidence-making moment without adding prizes or turning hard history into a game.

#### Graphics

Inspected eight halls/eight markers in rendered contexts and all four people assets against dark backgrounds. Kept the consistent rich halls with foreground, depth and warm light; imagined settings, not exact architecture. No baked-in text.
Avery (young Black man, violet) and Jo (fuller middle-aged East Asian woman, amber) vary in age, skin tone/build, in ordinary practice clothes. Seventeen selected poses from three sheets and one grounded-turn study; mirrors reuse them. All four assets people:true, generated by Codex. No code-drawn person remains. Swap seam: figureRenderer. Contact: Scratch painted-people-contact.png.
Twenty assets total, 1,497.0 KiB art; final bundle 2,089.8 KiB (2,139,919 bytes), slightly above the 2 MB goal to retain the strong hall set and readable painted people. No missing art token. Final review verification: final-review-verification.json.

#### Audit

One final audit completed: review-audit/audit.md; 50 PNGs inspected in nine contact sheets. Seventeen leads: phone context/hint (2), scroll-panel citation (1), welcome warnings (13), quick Next cut (1).
Confirmed fixes: first Dance tap and quick Next instruction. Other welcome warnings are intentional own-line/Play/Read/Sound behavior under BASELINE; premise remains accessible. Secondary citation follows a deliberately scrollable history article, not a hidden answer choice. Phone context failure is a harness gap, separately checked with a same-origin phone host.
All seven ordinary sizes, held inputs, five repeats, focus/Enter twice, motion-off and resize stress had no mechanical errors. Only touched states re-shot after audit; no second full audit. audit-states.json now includes Mambo labels, grounded turn/scuff and last Twist count for future reviewers; this audit did not cover the added definitions.
Focused final rechecks: post-audit-poses/ (10 frames), post-audit-moving/ (12), post-audit-voice/ (3), plus closed-focus/. All inspected; no console errors. Turn 17 verified at 1366, 680 and 375; scuff 18 and Twist 8 at 1366/680. Moving rechecked at all seven ordinary sizes plus phone top/judgments/draft; no horizontal overflow, both preview judgment sets fit by y416. An initial timed Twist shot caught count 3; the corrected check waited for count 8 rather than assuming elapsed timing.
Wave lessons checked: immediate hint/Read and heard-based voice; stable focus/control identity; 44 px targets; no reward/giveaway or false measurements; all five NCAS strands; no infinite Motion-off animation; complete short choice sets; live resize; no late welcome; consistent L/R/Me legends and state-restored hints. Unknown-state/diagnostic-answer rules do not apply to this ungraded explorer.

#### Left open

Hustle spec decision and fresh embodied/cultural review above. No new feature, kit change, commit, deployment or outreach. Unattended choices follow the brief and owner's painted-person direction; this is not owner approval of the paintings.
Procedural exception: initial short read-only commands used runner wait rather than a child-process cutoff; subsequent commands used explicit deadlines. Browser voice/clock evidence does not replace listening or professional dance validation.
Cleanup limit: all assigned Chrome ports are closed and host.html removed. Port 8755 still serves this tool after child cleanup; Windows exposes no owning listener PID, so closure could not be verified without killing an unidentified process. Recorded in cleanup-verified.json.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Dance Hall Decades handoff

Cold review, November 5, 2026. Work stays in this tool and _scratch/dance-hall-decades.
No commit or deployment. Read codex-review.md for the final evidence and audit disposition.

#### Source map

- src.html uses kit:curio. HALLS holds the eight source-backed cards; ROWS holds the 32 authored chart positions.
- buildPattern holds counts, active feet, relative floor positions, subdivisions and cues. The same audio clock
  drives the groove, count, footprint and painted pose. Lindy has eight placements in six beats; Hustle has a pickup.
- figureRenderer is the painted-person rendering seam. PAINTED_DANCERS selects two 4-by-2 character sheets;
  PAINTED_DETAILS holds behind-cross, touch, back-tap and scuff studies, with Avery on row one and Jo on row two.
  PAINTED_TURN is the separate grounded-turn study, before the lifted scuff.
- HALL_DANCER and paintedPose map a count to a character, cell and mirror. Sheet coordinates are 384 by 512.
  Replace the four WebPs or this mapping without changing the clock, footprints, content or comparison.
- The former code figure is removed. Seventeen selected painted poses are reused across the eight dances. The
  source sheets retain unused candidate cells; these are not additional classroom poses.
- Painted poses hold on each count, including Motion off. A rear-view teaching model demonstrates relative steps;
  the Electric Slide wall label follows the quarter turn on 17, with a right scuff on 18. Exact footwork remains
  in the labeled diagram. The demonstrator is not a reconstruction of a historical patron or costume.
- The scheduler has a 35 ms lookahead. Tempo changes affect the next unscheduled interval. Tabs leave music running;
  hall/mode changes, Read and hiding the page stop it. No voice plays over the groove.
- Curio.voice handles narration, Read and Sound. Short how-to lines fit the two-second action pace; stories
  are dropped or cut when their hall/tab no longer fits. No recordings were made; browser speech is the fallback.
- Comparison controls stay mounted. Dance changes clear writing tied to that dance; criterion changes clear
  the comparison reason. Writing is explicitly a draft, not a machine-graded cultural judgment. Copy can copy a draft.
- localStorage and clipboard access are guarded. Privacy is stated on screen. Reset clears only this comparison.
- __tool exposes state, setters, pattern, clock trace, voice log, sentence and renderer for inspection.

#### Review changes

Painted two varied adult demonstrators and extra touch/turn studies, with people:true on all four assets.
Redrew Avery's two Twist cells to distinguish standing and shallow-dip counter-rotation.
Preserved all eight rich halls and eight object markers. Contact sheet:
_scratch/dance-hall-decades/painted-people-contact.png, on a contrasting background at classroom figure sizes.

Moved Talk about it above the history card, reset historical scrolling on hall changes, repaired stale comparison
evidence, shortened movement/room how-to lines, fixed mirrored arrow origins and paired L/R labels, raised the
Georgia count glyph to prevent descender clipping, corrected the Electric Slide turn count, replaced the broken
Palladium source link, and qualified the spoken disco-backlash interpretation to match the screen.
The final audit confirmed a quiet first Dance-tab tap and a how-to interrupted by quick Next taps. The current
tab now narrates, and the still-valid shared Play instruction finishes across hall changes without stale stories.
Restored the original judge spacing after an overbroad review CSS edit, and separated repeated footprint labels.
The select focus ring sits inside its control so it cannot cover the label above it.

#### Sensitivity

Fresh cultural review should check creator credit and institutional exclusion across Black American, Cuban,
Puerto Rican and Latino dance histories; gay communities' role in disco; the attribution of backlash interpretations;
and the disputed Electric Slide origin date. The cross step avoids a stereotyped Native American label, explained
only in teacher notes. Do not reenact segregation or ask a learner to stand for a whole community.

The painted modern demonstrators vary in skin tone, age and body shape. Both are ambulant; the prompt requests
a hearing aid for Jo, but its small scale is not a strong visual accessibility cue. Notes allow seated tracing and
observation. Review anatomy, support weight and stereotyping, including at the actual display sizes.
The contact sheet is ready for the owner; this unattended run makes no claim of owner approval.

#### Source conflicts and limits

- Salerno's Electric Slide teaching sheet controls the corrected ending: 15 right back, 16 left touch,
  17 left forward with the quarter turn, 18 right scuff. The supplied spec's ending is inconsistent with it.
- The Stroll remains the specified eight-count side-touch adaptation. Powers's reconstruction uses six-count patterns.
- Mambo remains on one as requested. Library of Dance documents historical on-one as well as on-two timing.
- The requested Hustle tap sequence is not verified as a complete continuous partner basic. It now says short tap
  introduction, and count 3 asks for a right-weight reset before the next left tap. A full replacement would disagree
  with the exact spec sequence, so it is left for a spec decision and an embodied dance-teaching check.
- The fundraiser wording for 1973, attributed 1976 origin date, Ballard recording/release distinction,
  qualified venue access and modern-summary fact-card labels are preserved and checked again.
- Synthetic grooves are original learning sketches. No headphone or professional embodied dance review is claimed.
- No points, timers, completion prizes, cultural rankings or win states were added.

#### Engine changes wanted

None. No kit, script, docs or neighboring tool changes were made.

#### Evidence

All paths below are in Scratch. Cold play: cold/, cold-play/, cold-hall-*.json and cold-moving.json.
Reproduced stale evidence: cheap-before-stale.json. Fixed comparison: stale-fixed.json and review-cheap/.
Painted integration: review-quick/. Final sizes, keyboard, grayscale and Motion off: review-sizes/.
Main voice path and counts: main-after-audit.json, selected-tab-first.json, quick-next.json and read-side.json.
Focused final rechecks: post-audit-voice/, post-audit-poses/ and post-audit-moving/ with corresponding JSON proofs.
One final audit: review-audit/audit.md and its frames. See codex-review.md for confirmed leads and limits.

#### Cleanup limit

Assigned Chrome ports are closed and host.html was removed. Port 8755 still serves this tool after the child
cleanup attempts; Windows exposes no owning listener PID. Closure could not be verified without stopping an
unidentified process. Scratch cleanup-verified.json records the final observation.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
