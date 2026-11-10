# Partner Skill Coach

## One idea
A gym has three stations, the overhand throw, the instep kick and the set shot, each with a stack of cue cards (step with the foot opposite your throwing hand, plant your foot beside the ball, keep your elbow under the ball), and Coach Dani (made up, labeled "illustration") asks the child to be the coach: a clip of a player plays at full speed, then slowed with a scrubber, and the child flips the cue cards and taps the one cue that was missed and the moment it happened, Malik stepping with the same-side foot, Ana planting her foot behind the ball, Jo's elbow flaring out; then the child picks a tip from three, a vague "do better", a harsh "that was terrible", or a kind, specific "step toward the target with your left foot", or writes one from parts, and the player's next clip shows what happens: the specific tip fixes the cue, the vague one changes nothing, and the harsh one gets a slumped player and a worse try; levels get harder, with later clips missing a subtle cue and one clip that does everything right, where the child has to say so; at the end the child gets a cue checklist for their own attempts and a partner mode for real pairs; at the end the child sees that seeing a skill means breaking it into cues, and coaching works when the tip names one cue and is said with respect, so a student in grades 6 to 12 learns to analyze a partner's skill against its cues and give respectful feedback.

## Not like
- scarf-juggling-ladder (3, spec): a self-practice log. Here coaching someone else.
- target-toss (Grades K-2, spec): a throwing experiment. Here analyzing a throw's cues.
- playbook (Grades 3-5, spec): team tactics. Here one skill, one cue.
- recess-upstander (3, spec): words to stand up for someone. Here words to coach someone.

## Who and how
- Grades 6-12, Physical Education, module "Peer Skill Coaching". Standards: SHAPE.S1 (develops a variety of motor skills), SHAPE.S3 (develops social skills through movement), SHAPE America National PE Standards (2024).
- Format: puzzle (changed from cards; the cue cards are a tool, and the play is finding the missed cue level by level). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three skills, five cues each, nine clips over three levels, three tip types, the checklist. Extra: Partner mode (two students take turns performing and coaching with the same cards). tool.json `modes: ["Coach", "Partner"]`, `minutes: "20-30"`, `grades_label: "Grades 6-12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SHAPE.S1 | Scrub each clip; tap the missed cue and the moment | the cue lighting on the frame | 2 |
| SHAPE.S3 | Pick or write a specific, kind tip; take both roles | the next try changing | 3 |

## Screens and modes
Header (kit): title "Partner Skill Coach"; `Coach`, `Partner`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The gym with three stations, cue card stacks, and Coach Dani with a clipboard. The welcome is queued (`welcomeAfter: true`): "You're the coach today. Tap a station to watch a player." First hint: "Tap a station."

**Watch (focus: the clip).** At 1366x768 the clip is left with the cue cards right; at 680x425 the cards are a sheet. The clip plays at full speed, then slowed; the scrubber steps frame by frame. The child taps a cue card, then the frame where it was missed.

**Coach it.** Three tip cards; or `Write a tip` builds one from parts (one cue, one body part, a kind opener). The next clip plays with the result; a harsh tip shows the player slumping.

**Levels.** Level 1 misses an obvious cue; level 2 a subtle one; level 3 includes a clip with nothing missed, and the child taps `All cues met`.

**One cue, said kindly (the aha).** Coach Dani: "Find the one cue. Say it clearly. Say it kindly. That's coaching."

**The end.** A coach's card of the cues found and the tips given, plus a blank checklist. `Print` prints them.

**Partner (extra).** Real pairs.

## Content
- Players vary in body size, skin tone and ability, including a player with a prosthetic leg at the kick station; all are labeled "illustration".
- Cues follow common critical elements; one cue is missed per clip.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Clips can be replayed and scrubbed freely; tips can be retried.
- Keyboard: Tab to stations, the clip (arrows step frames), cue cards, tip cards and parts; Enter picks.
- With Motion off clips show as a strip of still frames.

## Look
- Accent `--brand` #5a3d8a gym purple (header, cue cards, buttons); gold #f4c542 (the frame in focus, the cue found); paper #f4f0fa; ink #1a0f2e; muted #554f60.
- Contrast (WCAG 2.1, computed): white on brand 8.50:1; brand on paper 7.57:1; ink on paper 16.23:1; muted on paper 6.99:1; ink on gold 11.21:1.
- Never color alone: found cues carry a check and the frame number; tip types carry labels.
- Different from this batch (range sage, parachute red, fridge blue, playground orange).

## Art
- People (illustrated): Coach Dani and nine players, labeled "illustration" (Gemini, `people: true`, 10; cutout yes).
- Local FLUX (`scripts/localart.py`): the gym with three stations (1, 16:9).
- Drawn in code: players animated in slow motion with clear joints, the scrubber, cue cards.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Coach Dani; `casual-peer` as the players' reactions and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.clip + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `station`: "Tap a station."
- how `scrub`: "Drag the scrubber to find the moment."
- how `cue`: "Tap the missed cue card, then the frame."
- how `tip`: "Pick a tip or tap Write a tip."
- how `allmet`: "If nothing is missed, tap All cues met."
- event, whole, one cue, said kindly.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: joint-pose clips with one missed cue, the scrubber, cue matching with a frame window, tip effects.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Cue | Tap every card | Each wrong card shows the frame where that cue was met. |
| Moment | Tap any frame | The frame must fall inside the missed cue's window. |
| Tip | Always pick the first tip | Tip order changes; only the specific, kind tip fixes the next try. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `station`; `scrub`.
2. `cue`.
3. `tip`; `allmet`.
4. One cue, said kindly (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SHAPE 2024 S1 and S3 wording | data/standards/shape-pe-2024.txt | data/modules.csv module line | yes |
| Critical cues for the overhand throw and kick (opposite-foot step; plant foot beside the ball) | Ulrich (2019), Test of Gross Motor Development, 3rd edition, performance criteria | PE Central, skill cue cards for throwing and kicking | yes |
| Set shot cues (elbow under the ball, follow through) | USA Basketball, youth shooting fundamentals | PE Central, basketball shooting cues (BEEF) | yes |
| Specific, task-focused feedback helps learning more than vague or harsh comments | Hattie and Timperley (2007), "The Power of Feedback", Review of Educational Research | Shute (2008), "Focus on Formative Feedback", Review of Educational Research | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s26, 2026-11-10): nine clips over three levels with one all-met clip leaves eight missed cues across three skills; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clip and cards; at 680x425 cards as a sheet.
2. Nine clips are analyzed, each missed cue and moment found, and the all-met clip named. (SHAPE.S1)
3. Each clip gets a specific, kind tip, and partner mode works with both roles. (SHAPE.S3)
4. Players vary in body and ability.
5. The checklist prints blank for real practice.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames; no network requests.

## Open questions
- Format change from cards to puzzle, as the idea card proposes (default used: puzzle).
