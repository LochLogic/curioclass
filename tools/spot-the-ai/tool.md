# Spot the AI: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: spot-the-ai

#### Built

Built the offline Grade 1 Machine Shop and ten-round AI or Not? showdown. Ten painted machines perform their jobs,
open to picture rules or learned-example piles, and keep independent page-load progress. The shelf pairs, live
screens, spotlight, three-card patterns, new examples, plain/gold bulbs and five-pair recap follow the spec.
The bundle uses the shared kit for settings, speech and tones. No commits, deployment or polish round.
All deliverables are in tools/spot-the-ai; evidence and helper scripts are in _scratch/spot-the-ai.

#### Numbers check

Independent Python: 5 AI and 5 rule machines, the required mixed order, no run longer than two of either kind,
30 art assets. Contrast ratios: white/header 11.503, ink/paper 14.854, muted/paper 6.175, brand/paper 10.744,
ink/gold 11.496, gold/navy 8.316, focus/paper 4.837. All agree with the rounded spec values.
Evidence: check_numbers.py and numbers.json in Scratch. The seven-line preview's 31-image count was my counting
error; the spec correctly lists 30. Jobs use 2400 ms and the pile uses 3000 ms with either Motion setting.

#### Facts checked

| Student-visible fact | Named source and boundary |
|---|---|
| These AI examples learn patterns from examples and use them on new inputs | [AI4K12 Big Idea 3](https://ai4k12.org/big-idea-3-overview/). This is the tool's introductory scope. |
| Face matching uses learned examples and can handle a hat | [Apple Face ID Security Guide](https://www.apple.com/business-docs/FaceID_Security_Guide.pdf). The spec's support page returned 429; the official guide verifies the claim. |
| Eyes, nose and mouth share positions in the face examples | Original conceptual scene in spec.md, not a complete face-recognition algorithm or a claim that a phone stores this crowd. |
| Speech recognition learns from speech examples | [Hinton et al., 2012](https://research.google/pubs/deep-neural-networks-for-acoustic-modeling-in-speech-recognition/). Cow, duck and cloud exchanges are original fixed examples. |
| Maps can use learned traffic patterns in route choice | [Google Maps 101, 2020](https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/). Park, after-school and rainy-day routes are original demonstrations. |
| Photo recognition can learn from labeled pictures | [Krizhevsky et al., NeurIPS 2012](https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html). Puppy and mop outcomes are the spec's demonstrations. |
| AI guesses can be wrong | AI4K12 Big Idea 3; the mop is a deliberately constructed error, not measured performance of a real product. |
| Video recommendations can learn from viewing behavior | [Covington et al., 2016](https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/). Dinosaur and space sequences are original examples. |
| Rule machines follow written steps; real machines can mix both approaches | The spec's simplified original machines and its teacher note. No claim that every real elevator, camera or remote is AI-free. |
| Code 1234, floor 3, channel 5, teddy's three phrases | Original content in spec.md. The teddy repeats the same cycle, rather than one identical phrase. |
| E1-ALG-ML-02 and E1-SOC-HU-15 | Both verified in data/standards/csta-2026-ids.txt; notes map the machine comparisons and everyday consequences to them. |

Source verification records: Scratch/sources.json. No user data, camera or microphone is used.

#### Break it

- 116 real held-click functional checks passed: every machine, immediate opening during a job, both new-example
  branches, replay, separate mode state, cancellation, resize, clean console and no network requests.
- Sweep both vote buttons before every reveal: only the last vote counts. This earned exactly five matching bulbs.
- Vote after a reveal using A: the committed vote and results did not change, for all ten rounds.
- Open without voting: disabled; no result is added. Repeat opening: the opened guard prevents a duplicate result.
- Try to advance an unopened machine: the state guard prevents skipping. Mode hopping preserves the current vote.
- Constant guesses earn 5 of 10; alternating guesses earn 6. Independent enumeration of all 1024 vote vectors has
  exactly one all-matching vector. There is no saved best, percentage, rank or mastery claim.
- Memorizing the fixed order can solve a replay. The spec requires that order, so this remains a teaching sequence,
  not an assessment that can certify reasoning. No answer clue or feedback appears before the reveal.
- Wrong door codes 1235 and 0000 are rejected by doorAccepts; 1234 is accepted. The short job includes a wrong entry
  staying shut before the correct entry opens. There is no extra keypad-entry mode.
Evidence: functional/results.json, voice/keyboard-all-ten.json, voice/how-fixes.json in Scratch.

#### Voice walk

Curio.voice with mode scope, valid serial tokens, Read priority and the prepared curious-librarian/Aoede manifest.
No recordings were made, as instructed; the kit uses the best installed browser voice. Chrome was muted in tests.

Main held-click path: welcome, door job, open, rule reveal, repeat, shelf, phone job, open, hat, cat, shelf,
showdown welcome, vote, open, result and Next instruction. Two-second tap gaps were used on the side path; the main path also
paused at first teaching moments so their narration could finish. Side path used Read, immediate Next/mode switch,
Sound off with Read, Sound on and the puppy/mop examples. Logs: voice/main-log.json and voice/side-log.json.

Initially Back and Vote were delayed behind descriptions. Fixed by retaining an already queued how-to in its
position and queuing Back at the new-example action. The focused final walk heard Back once and Vote once.
The final default-settings walk starts with a plain stage tap and hears all ten keys exactly once on one page:
wShop, pick, open, again, back, tryNew, wShow, vote, openShow, next. Evidence: voice/main-default.json.
How lines did not repeat; stale events were dropped when the class acted sooner in the earlier two-second walk.
Read events were logged with Sound on and off. The final keyboard-only run played all ten rounds using Tab,
Enter, A and N, with focus on Next after every opening and Play again at the finish.

#### Feel check

Played all ten shop machines and the whole showdown, including a five-match sweep and an all-matching keyboard run.
Best moment: the photo finder puts Dog with a check beside a clearly painted cleaning mop, then admits its mistake.
The contrast is visible before the explanation, and the dog examples remain beside it for discussion.

Flattest moment 1: the early elevator and TV jobs were mostly number changes. Added a lit elevator doorway,
remote signal arcs and a glowing television screen; kept the floor count and elevator ding.
Flattest moment 2: example cards faded again when the job redrew. Anchored animation progress to the reveal time
and stopped re-running the entrance on later jobs, so the examples stay solid and readable.

Scratch/bar-comparison.jpg puts this tool beside Snowy Mail Route. Both bar tools were bundled into Scratch to
respect the write boundary and opened in Chrome. The first bar render used an unsupported file-URI argument;
local paths fixed it. The new tool has a richly painted place, large objects and clearer cause/result pictures.
The fixed content limits replay variety; the useful repeat play is comparing partners and anticipating funny errors.

#### Done when

1. PASS: all ten jobs and correct insides, checked through real inputs and individual frames.
2. PASS: hat/cat, duck/cloud, rain, puppy/mop and space cycles; rule repeats and teddy's fixed phrase cycle.
3. PASS: exact ten-machine order, mutable pre-reveal votes, frozen revealed votes, matching bulbs only, five pairs.
4. PASS: 1366x768 and 680x425 frames show the bench machine largest; inside shares its allocated box height.
5. PASS: jobs and pile scroll can be interrupted immediately; serial tokens cancel old callbacks and speech.
6. PASS: all STANDARDS sizes, including the real 375x812 iframe, retain the machine and primary controls; 60 px targets.
7. PASS with recording limitation: ten how/welcome keys heard, event/stale/Read/Sound paths inspected; browser voice fallback.
8. PASS: all ten showdown rounds keyboard-only with visible focus. Fixed Open's hide-before-focus-transfer bug.
9. PASS: Motion off keeps timing and no infinite animations; both-mode functional console and network checks clean.

#### Wave lessons

| Lesson | Result and evidence |
|---|---|
| Hint and voice | PASS: synchronous hint updates; kit once-only narration; final Back/Vote priority checks. |
| Focus and layout | PASS: stable controls and shelf positions until Open; reserved hint height; capture focus before hiding Open. |
| Sizes and targets | PASS: seven desktop sizes and iframe phone; no horizontal overflow or undersized controls. |
| No giveaways | PASS: no answer-dependent badge or bulb until commit; last-vote sweep tested. |
| Honest numbers | PASS: bulbs correspond to committed matches; no confidence or mastery meter. |
| Standards | PASS: inspect learned patterns/new examples and compare everyday machine decisions and mistakes; no family engine. |
| Motion off | PASS: explicit animation:none for loops, still example fan, unchanged timers. |
| Choices in view | PASS for the two vote choices. Shelf uses the spec's scrolling 64 px strip on narrow stages. |
| Resize mid-animation | PASS: 760-wide flip and mode change did not revive an old job; audit stress results below. |
| Welcome not late | PASS: no welcomeAfter; first action starts immediately; queue priority corrected. |
| Unknown shown as unknown | PASS: no inside or result bulb before voting and opening. |
| One look, one meaning | PASS: rule person/pencil/card versus example fan; bulb check accompanies gold. |
| Badge truth | PASS: only exact matches light bulbs; Dog on the mop is explicitly exposed as the machine's wrong guess. |
| Hint changes back | PASS: Back restores Pick; mode changes immediately restore that mode's current action. |
| No copying answer words | PASS: voting hint gives actions and gestures, not the machine's classification. |

#### Audit leads

The single full audit completed within its 40-minute limit: 70 leads on the saved audit snapshot.
It reported no undersized controls, console errors, focus loss, infinite calm animations, or resize exceptions/stuck controls.
Five held-click repetitions were clean for every tested speaking control.

- Shelf clipping leads (#shelves, 680, 800, 760 and 375 widths, including the mop state): intentional scrolling
  64 px tiles required by the compact layout. Both voting choices and primary actions remain visible.
- #bench keep-region leads (680/1280/1366 starting views and phone opened states): the region is the whole SVG,
  including the area deliberately covered by the DOM shelf. The actual machine is unobscured in the frames.
- All Dog/Not dog hidden/overlap leads in mop and finale: fixed after this snapshot. Buried photo cards have no
  labels; exposed rightmost cards have top labels; the three front cards keep clear bottom labels. Tiny recap
  cards use pictures without word labels. Verified at 680, 760, 1366 and in the phone iframe.
- Finale 375 keypad digits touching the arrow: fixed with compact 1234 at 10 px on tiny cards; phone recap inspected.
- Welcome not heard on first tap of machine-0 through machine-9 or Open: intentional STANDARDS first-tap rule.
  The tap's own event takes priority, leaving the welcome unmarked; the reveal states the premise itself.
- Two quick mode taps cutting welcomes: fixed by making the already active mode a no-op. Both targeted traces
  preserve a whole welcome with no cut marker.
- Quick-tap event cuts on door, teddy, speaker, elevator and map: fixed the underlying moving targets. Shelf
  positions now stay fixed until Open, and the compact strip stays fixed until Back. Repeated clicks at exactly
  the same physical coordinates select the same machine and let its replacement event finish, for all five.
- The original "others moved" shelf transitions now occur on Open, away from the clicked machine tile.

No second full audit was run. Final checks target only the changed views and interactions: post/, post-art/,
phone/*-final.png, voice/main-default.json. audit-snapshot.json and final-bundle.json distinguish the two bundles.

#### Frames looked at

Art sheet, bar-snowy, bar-beat, four quick frames, all fourteen desktop size frames, all ten individual machine
trial frames, mop, ten votes, five pairs, calm reveal, grayscale, pattern at 1366 and 680, four iframe phone frames,
main/side voice frames, keyboard finales, final elevator and TV frames, all 60 audit frames, eleven targeted
post-audit captures, the corrected narrow mop captures and the final phone mop/recap.
Contact sheets were opened for full sets; phone frames and representative detail frames were also opened full size.

#### Art made

30 placed images, 931.3 KB of WebP art; 0 KB recorded voice; final bundle 1329.8 KB (1,361,665 bytes), below the 2 MB goal.

29 new assets generated individually with the built-in image tool; one existing workshop retained. Exactly three
people assets are marked. The child in the hat matches the original child by a referenced edit. Redrew the space
cartoon once to remove an unintended astronaut. No missing art or labeled stand-ins. Prompts and provenance are in
art/prompts.json; raw paintings are in art/raw; conversions used only scripts/art.py --rekey.

#### Art still to paint

None. People set remains for the following cold review and owner contact-sheet review before any shipping step.

#### Engine changes wanted

None. No shared kit or family file changed.

#### Left open

- No recorded curious-librarian voice, by the build-only prohibition on recording. The manifest is ready.
- The mandated fixed order can be memorized on replay; no claim of independently demonstrated mastery is made.
- Scope decisions, teddy-cycle wording and people-image decisions are recorded in handoff.md.
- The initial bare Python lacked image dependencies. The conversion used read-only libraries from the existing
  S:/AI/tts environment with bytecode disabled; no shared environment was changed.
- All Chrome debug ports 9980 through 9987 and host port 8785 were verified closed. host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: spot-the-ai

#### Played

Cold Grade 1 solo and projector walk: all ten shop machines, both new-example branches and all ten showdown rounds, before reading the builder's report or source. The large painted machines and mop surprise are strong.

#### Findings fixed

- Blocker, general, runJob: startup pitch encoded every answer (620 Hz AI, 360 Hz rule). Real held taps confirmed the perfect cue. All ten now start at 480 Hz.
- Should fix, general, voice: at a 2 s pace reveal descriptions swallowed action instructions. Shortened and prioritized the next-action lines, kept once-only how-to and serial validity checks; main-path recheck heard all eight action keys once.
- Should fix, general, speaker: queued questions could be spoken after the picture already showed an answer. The visible bubble now follows the question/answer that the shared voice queue actually starts.
- Should fix, general, teddy: Same every time implied an identical sentence despite the three-phrase cycle. Added a current-phrase outline and return arrow, Same three in order, cycle-specific repeat narration and accurate steps wording for all rules.
- Should fix, general, photo finder: the mop's wrong Dog guess carried a check mark. It now carries a cross; the puppy keeps its matching check. The wrong path still teaches through the same painted mop and spoken explanation.
- Should fix, general, phone: a square glyph stood for locked. Replaced it with a clear open/closed padlock, keeping the successful check separate.
- Should fix, general, privacy/facts: made Motion storage visible on screen and scoped the displayed AI definition to this shop's machine-learning examples. Notes distinguish enrolled face matching from generic facial features.
- Polish, general, art: redrew the magenta-fringed shelf with imagegen in the same house style. First candidate rejected for edge artifacts; second green-key candidate converted with art.py --rekey shelf and despill.
- Audit coverage now includes the actual machine, inside and recap drawings, plus teddy, cat and cloud states, rather than treating the entire shelf-covered SVG as an unobscured keep region.
- Should fix, general, audit voice leads: a second showdown greeting arrived after its voting instruction. Removed the redundant delayed greeting; the vote instruction is the mode entry.
- Should fix, general, audit re-selection leads: rapid taps on the pressed shelf tile restarted the same job, cutting its how-to and in-machine responses. The tile now acknowledges selection without restarting; the explicit repeat control still replays the job. Teddy bubbles also stay with their spoken saying.

#### Findings left

- Blocker, general, spec-bound: memorizing the mandated fixed order earns 10/10 without reasoning. The spec forbids changing that order. Kept it, documented the limit, and explicitly disallowed using bulbs as mastery evidence in notes.
- Should fix before shipping: recorded curious-librarian clips are absent. The build/review brief explicitly forbids recording; browser narration and a synchronized manifest remain. No narration recording service was invoked.

#### Break it

- Matching bulbs are the only score. No best score, saved result, confidence meter, reflection gate or separate mastery check exists.
- Real held-click full rounds: always AI 5/10; always Not AI 5/10; alternate 6/10; sweep both choices before each reveal 5/10; every answer wrong 0/10; memorize order 10/10 (spec conflict above).
- Open before voting and Next before opening do not advance. Changing both choices before opening records only the last one. Repeated Open adds no duplicate; mode hopping preserves the committed result.
- Post-reveal A/N and repeated reveal: all ten keyboard rounds keep their committed vote; 34 keyboard checks passed, including focus on Next and Play again, with zero exceptions or network requests. All ten startup tones remeasured at 480 Hz; the old high/low classification rule cannot distinguish answers and reduces to constant guessing.
- Independent enumeration: five AI, five rules, required mixed order, longest type run two, one all-matching vector among 1024. Teddy returns to its first phrase after three repeats; new-example cycles remain specified.

#### Voice walk

Default Sound on, held 120 ms clicks, 2 s gaps: stage, door, Open, repeat, shelf, phone, Open, hat, shelf, showdown, vote/Open/Next through ten. Cat, mop and cloud were checked as side paths.

Final spoken action keys in order: pick, open, again, back, tryNew, vote, openShow, next. Each started once on that page. A separate fresh plain-stage tap also started pick immediately.

Job, rule/AI, hat/cat and closing events were checked against their current state. Fast actions drop stale descriptions; no instruction names an unavailable control. Welcomes skipped/cut by an action remain allowed by BASELINE 16; the hint and Read retain the action.

| Line kind | Expected | Observed |
|---|---:|---:|
| Eight action how-to keys, main route | once each | once each |
| Repeat control, five actions at both 8 s and 2 s gaps | 5 | 5 |
| Six quick double selections, 0.7 s gaps | one whole how-to per selection | 6/6, no cuts |
| Repeated selected teddy/speaker tiles | preserve one complete job | saying and Q/A complete, no cuts |
| Read with Sound on/off; immediate mode switch | current hint, prompt new mode | passed |

Evidence under _scratch/spot-the-ai/: post-audit-main.json, post-audit-mode-entry.json, post-quick-machine-*.json, post-selected-machine-*.json, post-repeat-five-fast.json, voice-repeat-five.json, voice-read-switch.json and speaker-timing.json. At 680x425 a mutation trace confirmed both cowQ and cowA matched their bubble when each started. The full voice manifest equals allLines(), with no missing or extra strings. Browser narration only; no claim of listening to recorded Aoede clips.

#### Facts checked

- Learning patterns from data: [AI4K12, Big Idea 3](https://ai4k12.org/big-idea-3-overview/). This tool illustrates machine learning; it does not define all AI approaches.
- Learned facial matching, enrolled owner and hat support: [Apple Platform Security, Facial matching security](https://support.apple.com/en-om/guide/security/sece151358d1/web), checked 2026-11-07; unregionalized route returned 429. Eyes/nose/mouth are picture clues, not an identity-matching algorithm or a literal stored portrait pile.
- Speech learned from examples: [Hinton et al., IEEE SPM 2012](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/HintonDengYuEtAl-SPM2012.pdf). Cow/duck/cloud words and answers are scripted spec content.
- Traffic history, live conditions and alternative routes: [Google Maps 101, Johann Lau, 2020-09-03](https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/). Park, after-school and rain trips are illustrative cases, not measured route predictions.
- Learning labeled photo classes and making mistakes: [Krizhevsky, Sutskever and Hinton, NeurIPS 2012](https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html). Puppy/mop outcomes and legs/ears/tail are conceptual scenes, not performance claims or hand-written classifier rules.
- Learned recommendations: [Covington, Adams and Sargin, RecSys 2016](https://research.google.com/pubs/pub45530.html?hl=uk). Dinosaur/space sequences are original demonstrations.
- Code 1234, floor 3, channel 5, camera press and teddy's three sayings: original simplified rule machines in spec.md. Real products can combine rules and AI; the visible caveat and notes preserve that distinction.
- CSTA ids E1-ALG-ML-02 and E1-SOC-HU-15 exist in data/standards/csta-2026-ids.txt. Inspecting examples/new inputs and comparing everyday uses/mistakes enact the spec's stated goals; no extra standard was added.
- Recomputed all seven specified contrast pairs: 11.503, 14.854, 6.175, 10.744, 11.496, 8.316 and 4.837. Evidence: Scratch/review-numbers.json.

#### Sensitivity

Three marked people assets inspected: owner, identical owner with hat, and 12-portrait grid. Varied ages/skin tones, glasses and a headscarf are presented warmly; no named culture or religion is taught. A cultural lens should still check the grid for stock ethnic shorthand and the facial-matching explanation for implied differences in whose face works. No real biometric input is collected.

#### Flattest moment left

Later showdown rounds repeat already-known machines. The teddy's cycle now gives a visible cause/result payoff; richer replay variation would change the specified fixed sequence/content.

#### Graphics

All 30 painted assets inspected in the art sheet and machine/reveal frames; three people images also inspected separately. Kept the workshop, all machine cutouts, portraits, photos and cartoons. Shelf alone redrawn, two candidates, selected file art/shelf.webp; built-in imagegen prompt/provenance in art/prompts.json. Art about 924 KiB; bundle 1,343,767 bytes (1312 KiB). Independently inspected the existing Beat Lab and Snowy Mail Route benchmark frames; the workshop retains comparable depth, large art and clear feedback.

#### Audit

One full audit completed within the 40-minute limit, Chrome 9941 / host 8745: _scratch/spot-the-ai/review-audit/audit.md. All 84 frames inspected in sheets; critical compact/phone frames also opened full size.

- Its 55 leads: 7 specified scrolling-shelf warnings; 26 cropped-SVG bounding-box warnings (24 inside, 2 recap); 1 wood-grain path behind an opaque recap card. Confirmed visually, not layout faults.
- Eleven missing first-tap welcomes are allowed by BASELINE 16: the tap speaks for itself, and hint/Read/reveals retain the content. The one genuinely late greeting was fixed.
- Six quick-tap instruction cuts and three lost in-machine lines came from restarting the selected tile. Fixed the selection behavior, then rechecked all six quick-tap cases and the teddy/speaker chains. Repeat-button events still start five times.
- No undersized targets, actual clipped controls/hints, console exceptions, focus loss, infinite calm animations, resize exceptions or stuck controls. Grayscale and 34 independent keyboard checks also passed.
- No second full audit. Only the changed voice/selection paths were rerun: final full main voice route, slow showdown entry and nine targeted cases, all console-clean. All task Chrome/server ports verified closed; no host.html remains.

Wave lessons checked: next-action hints/Read and once-only how-to; stable focus/controls/reserved hint space; all sizes and 60 px targets; giveaways and honest bulbs (fixed-order exception above); both standard goals; Motion off with unchanged timers; both vote choices visible; resize during actions; no late welcome; unknown insides hidden; distinct rule/pattern symbols; truthful mop badge; hints restored on Back/mode switch; no answer-word copying before a vote.

Spec Done when: runtime items 1-6 and 8-9 verified; item 7 passes the tested browser-voice lifecycle, with recorded-voice identity still open. Notes begin with the three required headings; metadata remains teacher-led Grade 1, 10-20 minutes.

Final evidence: _scratch/spot-the-ai/review-validation.json records the bundle hash, bytes, voice counts and closed ports.

#### Left open

The fixed-order assessment loophole and missing recorded clips above need a later spec/recording decision. No new features, kit edits, commits, shipping or outreach. Where a choice was needed, retained the spec's order and people art and the current build brief's recording prohibition.

Process note: the initial rules/memory reads returned immediately but lacked an explicit subprocess timeout; subsequent commands used bounded wrappers (bundle 120 s, drive 300 s, audit 2400 s).

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Spot the AI build handoff

#### Structure

src.html starts from the kit starter, using kit CSS, Curio.tone and Curio.voice. A responsive SVG paints the live
bench at its actual pixel size; the DOM shelves and panel controls remain stable during jobs. ART contains each
painted asset once for bundling. MACHINES and ORDER are the content tables. Machine Shop and showdown have separate
page-load states. serial invalidates timers and speech on a newer action. No shared engine is used.

The shelf layout latches to a compact strip on Open, and expands only on Back. Selecting a machine keeps its tile
at the same position, including repeated taps. Clicking the already active mode is a no-op so it cannot cut a welcome.

#### Spec decisions and open questions

- Keep the three people assets: the owner, the identical owner in a hat and the diverse face grid. The current
  brief and BASELINE authorize Codex people art and supersede the spec's older Gemini wording.
- Keep all added new-example narration, including hat, cat, rain, puppy and space.
- The spec's listed art count is correct: 30. The seven-line preview initially miscounted 31; the independent
  script confirmed 30 before implementation.
- Build-only instructions require images despite BUILD.md's older instruction not to draw art. Current instructions win.
- Preserve the existing workshop image and add missing art in a compatible bright picture-book style.
- Read the report's validation status before shipping. No recordings are made because the build brief forbids them.
- The fixed showdown order is deliberate. Replaying can be solved by remembering the ten answers. It is a teaching
  sequence with no saved best or claimed mastery score; randomizing would contradict the spec.
- The teddy repeats its same three-phrase cycle. "Same every time" means the same written cycle, rather than one
  identical phrase on every squeeze. The notes explain the input/rule distinction for number-controlled machines.

#### Sensitivity

The three marked people paintings show a cheerful brown-skinned child and a grid of twelve people with varied ages,
skin tones and hair, including glasses and a headscarf. Review the full art sheet in Scratch for representation and
the owner/hat match. No culture or religion is taught. Faces are conceptual examples, not captured biometric data.
The space cartoon was redrawn to remove an unrequested astronaut, keeping the three intended people assets.

#### Engine changes wanted

None required. Browser speech picks the kit's best available voice; the selected bank identity becomes audible only
when a later authorized recording pass supplies clips.

#### Cold review changes, 2026-11-07

- Removed the classification-dependent startup pitch, which gave every answer away. Jobs now start at 480 Hz.
- Short how-to lines take priority on the action that makes their control available. They remain once per load;
  job/reveal events remain repeatable, with serial checks dropping speech after its state changes.
- Questions and answers from the speaker update their visible bubble when the shared voice queue starts them.
- The teddy's picture rule highlights its current phrase, has a return arrow, and says Same three in order.
  Its repeat narration describes the cycle rather than claiming each squeeze says the same sentence.
- Replaced the square phone-lock glyph with a drawn open/closed padlock. Motion privacy is visible in the panel.
- The mop's wrong Dog guess now has a cross rather than a matching check. The displayed AI definition is scoped
  to this shop, and notes distinguish machine learning from the wider field and generic face features from identity matching.
- Shelf painting redrawn with built-in imagegen in the existing house style. See prompts.json for conversion provenance.
- Kept the specified fixed showdown order. Memorization can still light all ten bulbs; removing that shortcut
  requires a spec decision. Notes explicitly prohibit treating bulbs as demonstrated mastery.
- No recordings made, in keeping with the build/review brief. Browser fallback remains an unfinished shipping item.
- The single review audit confirmed rapid re-selection cutting instructions and in-machine voices. An already
  pressed shelf tile now acknowledges the tap without restarting its selected job; the explicit repeat control
  still repeats. Teddy sayings join the speaker's speech-synchronized bubble handling.
- Showdown entry uses the vote instruction as its welcome. No separate greeting is queued behind the action line.
  Post-audit checks are scoped to these voice/selection changes; the full audit was not repeated.

#### Audit interpretation

The dedicated inside-picture SVG group contains cropped nested SVG portraits. Its DOM bounding box includes
parts of the source portrait grid that the nested viewports clip away. The mechanical keep-region sampler can
therefore report a giant covered/offscreen region even while all rendered cards and controls fit. Check the
actual ai-open, show-open and cat-lock frames, including the 375 iframe, before treating that warning as a layout bug.
The compact 64 pixel scrolling shelf is specified; the two voting buttons and primary actions never use that scroller.

#### Build boundary

Writes stay in tools/spot-the-ai and _scratch/spot-the-ai. No commits, deployment or polish round.
Ports: Chrome 9980 through 9987, host 8785. Scratch holds prompts provenance, commands, frames and validation.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
