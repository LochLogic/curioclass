# Codex report: spot-the-ai

## Built

Built the offline Grade 1 Machine Shop and ten-round AI or Not? showdown. Ten painted machines perform their jobs,
open to picture rules or learned-example piles, and keep independent page-load progress. The shelf pairs, live
screens, spotlight, three-card patterns, new examples, plain/gold bulbs and five-pair recap follow the spec.
The bundle uses the shared kit for settings, speech and tones. No commits, deployment or polish round.
All deliverables are in tools/spot-the-ai; evidence and helper scripts are in _scratch/spot-the-ai.

## Numbers check

Independent Python: 5 AI and 5 rule machines, the required mixed order, no run longer than two of either kind,
30 art assets. Contrast ratios: white/header 11.503, ink/paper 14.854, muted/paper 6.175, brand/paper 10.744,
ink/gold 11.496, gold/navy 8.316, focus/paper 4.837. All agree with the rounded spec values.
Evidence: check_numbers.py and numbers.json in Scratch. The seven-line preview's 31-image count was my counting
error; the spec correctly lists 30. Jobs use 2400 ms and the pile uses 3000 ms with either Motion setting.

## Facts checked

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

## Break it

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

## Voice walk

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

## Feel check

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

## Done when

1. PASS: all ten jobs and correct insides, checked through real inputs and individual frames.
2. PASS: hat/cat, duck/cloud, rain, puppy/mop and space cycles; rule repeats and teddy's fixed phrase cycle.
3. PASS: exact ten-machine order, mutable pre-reveal votes, frozen revealed votes, matching bulbs only, five pairs.
4. PASS: 1366x768 and 680x425 frames show the bench machine largest; inside shares its allocated box height.
5. PASS: jobs and pile scroll can be interrupted immediately; serial tokens cancel old callbacks and speech.
6. PASS: all STANDARDS sizes, including the real 375x812 iframe, retain the machine and primary controls; 60 px targets.
7. PASS with recording limitation: ten how/welcome keys heard, event/stale/Read/Sound paths inspected; browser voice fallback.
8. PASS: all ten showdown rounds keyboard-only with visible focus. Fixed Open's hide-before-focus-transfer bug.
9. PASS: Motion off keeps timing and no infinite animations; both-mode functional console and network checks clean.

## Wave lessons

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

## Audit leads

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

## Frames looked at

Art sheet, bar-snowy, bar-beat, four quick frames, all fourteen desktop size frames, all ten individual machine
trial frames, mop, ten votes, five pairs, calm reveal, grayscale, pattern at 1366 and 680, four iframe phone frames,
main/side voice frames, keyboard finales, final elevator and TV frames, all 60 audit frames, eleven targeted
post-audit captures, the corrected narrow mop captures and the final phone mop/recap.
Contact sheets were opened for full sets; phone frames and representative detail frames were also opened full size.

## Art made

30 placed images, 931.3 KB of WebP art; 0 KB recorded voice; final bundle 1329.8 KB (1,361,665 bytes), below the 2 MB goal.

29 new assets generated individually with the built-in image tool; one existing workshop retained. Exactly three
people assets are marked. The child in the hat matches the original child by a referenced edit. Redrew the space
cartoon once to remove an unintended astronaut. No missing art or labeled stand-ins. Prompts and provenance are in
art/prompts.json; raw paintings are in art/raw; conversions used only scripts/art.py --rekey.

## Art still to paint

None. People set remains for the following cold review and owner contact-sheet review before any shipping step.

## Engine changes wanted

None. No shared kit or family file changed.

## Left open

- No recorded curious-librarian voice, by the build-only prohibition on recording. The manifest is ready.
- The mandated fixed order can be memorized on replay; no claim of independently demonstrated mastery is made.
- Scope decisions, teddy-cycle wording and people-image decisions are recorded in handoff.md.
- The initial bare Python lacked image dependencies. The conversion used read-only libraries from the existing
  S:/AI/tts environment with bytecode disabled; no shared environment was changed.
- All Chrome debug ports 9980 through 9987 and host port 8785 were verified closed. host.html was removed.
