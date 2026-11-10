# Playground Rules

## One idea
A busy playground with no rules plays on the screen (kids bump on the slide, the swing line is a crowd, a ball rolls toward the street), and the child hangs one rule sign at each trouble spot and watches that spot replay calmer, or not, then finishes "We need this rule because..." with a picture reason, so a kindergartner sees that a rule is there to fix a real problem.

## Not like
- town-council (2, concept): a town government deciding about land. Here classroom and playground rules.
- school-fix-it-meeting (3, concept): a survey and a deliberation. Here hang a sign, watch a replay, give a reason.
- backpack-pack (K, concept, this batch): what you pack changes a trip. Here what rule you hang changes a scene, and you give its reason.
- symbol-spotter (K, concept, this batch): finding symbols that stand for ideas. Here making the rules a group lives by.
- friend-moves-practice (K-2 SEL, spec): words to join and share. Here rules for a whole group, and a vote.

## Who and how
- Kindergarten, Social Studies (Civics), module "Rules and Responsibilities". Standards: D2.Civ.3.K-2 (the need for and purposes of rules inside and outside school), D2.Civ.12.K-2 (how rules work in public settings), D2.Civ.7.K-2 (civic virtues at school), D4.1.K-2 (an argument with reasons), D2.Civ.11.K-2 (working together to decide), D4.8.K-2 (listening, consensus and voting).
- Driver: teacher on the projector with the class calling out, or one child alone; every sign, reason card and classmate line is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three trouble spots, then the swing rule meeting. tool.json `modes: ["Playground", "Swing meeting", "Our rules"]`, `minutes: "15-20"`, `grades_label: "Grade K"`.
- Nothing is saved; `Print` prints "Our rules" (each hung sign with its picture reason). Teacher notes say how to rename rules to match the school's own.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.3.K-2 | Tap a trouble spot and choose the sign that fixes that problem, at school (slide, swings) and outside school (the ball by the street gate) | the three signs and the spot | 2 |
| D2.Civ.12.K-2 | Watch the spot replay with the sign: calmer with the right sign, the same with a silly one, a different spot changes with a wrong-spot one | the replay states | 3 |
| D4.1.K-2 | Finish "We need this rule because..." with a picture reason card | the sign with its reason | 4 |
| D2.Civ.11.K-2, D4.8.K-2 | Hear four classmates, pick the swing rule most can live with, and see the vote | the classmates' hands and the count | 5 |
| D2.Civ.7.K-2 | Choose what a good friend does when Leo's rule loses | Leo's face and what happens next | 6 |

## Screens and modes
Header (kit): title "Playground Rules"; `Playground`, `Swing meeting`, `Our rules`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A sunny school playground loops a 6-second busy scene: two kids climb up the slide while one slides down and they bump; five kids crowd the swings at once; a ball bounces toward the open gate by the street. Three trouble spots pulse. The welcome is queued (`welcomeAfter: true`): "This playground has no rules, and it's a mess! Tap a problem you see." First hint: "Tap a problem you see. It's pulsing." The first tap on a spot zooms to it and cuts the welcome.

**Playground (focus: the zoomed trouble spot).** At 1366x768 the spot fills the center, with three sign cards below it (picture plus words, each read on tap) and `Hang it` under them. At 680x425 the cards are a row under the spot and Ms. Okafor folds away. `Back to playground` returns to the whole scene.
- Slide: signs "One at a time on the slide. Go up the ladder, slide down feet first." (helps), "Slide down backwards" (silly), "Stay behind the line at the swings" (fixes a different spot).
- Swings: signs "Wait in line for the swings." (helps), "Everybody swing at once" (silly), "Keep the ball inside the fence" (different spot).
- Ball by the street: signs "If the ball goes out, stop and get a grown-up." (helps), "Run fast to get the ball" (silly), "One at a time on the slide" (different spot).
- Hang it: the sign hangs on a post and the spot replays (4 to 6 seconds). Right sign: the scene is calmer (kids line up, one slides, the ball stops at the gate and a teacher gets it). Silly sign: the same trouble plays again and Ms. Okafor says "Hmm. Did that fix it?" Different-spot sign: the sign hangs, nothing changes here, and a small arrow points to the spot it belongs to. Every replay outcome is its own painted state, different at a glance.
- After a right sign: four reason cards appear: a bandage (so nobody gets hurt), two kids and a turn arrow (so everyone gets a turn), a car (to stay safe from cars), a crown (so I win). Ms. Okafor: "We need this rule because... Tap the reason." The right reason glows on the sign; a mismatched reason gets "Is that why we need this rule? Listen again." and the sign's line replays. "So I win" is never right.
When all three spots are fixed, the whole scene replays calm, and `Swing meeting` lights.

**Swing meeting (focus: four classmates around a rug).** Mia, Leo, Ava and Sam sit in a circle; four rule cards lie in the middle. Each classmate's face is a big tap target; a tap plays what they care about:
- Mia: "I'm little. I never get a turn."
- Leo: "I want a really long turn."
- Ava: "I don't like waiting a long time."
- Sam: "I want it to be fair for everybody."
Rule cards: "Big kids first", "Whoever runs fastest", "Ten pushes each, then the next kid", "One turn a day". The child picks one and taps `Vote`. Each classmate raises a hand or not, one at a time, with a short reason, and the count shows with hands and a number. The keyed votes (child counts as one yes): Ten pushes: 4 of 5 yes (Leo no, "That's short!"); Big kids first: 2 yes; Whoever runs fastest: 2 yes; One turn a day: 2 yes. Only "Ten pushes" wins; any other choice loses and Ms. Okafor says "Not many friends could live with that one. Who said what? Tap a friend to listen again."

**When your rule loses.** Leo frowns: "I wanted a long turn." Three choices, each a picture and words: "Laugh at Leo" (Leo looks sadder; "How would that feel?"), "Tell Leo: your turn is next, I'll push you" (Leo smiles and they swing), "Walk away" (Leo sits alone). Every choice plays honestly and `Try another` rewinds.

**Our rules.** A poster with every hung sign and its reason, ready to print.

## Content
- Three spots, nine signs, four reason cards, four classmates, four swing rules and the keyed votes above, and the three friend choices, all written for Curio Class.
- Teacher note: rules here match common playground safety guidance (one at a time on the slide, feet first; never chase a ball into the street); a school may have its own rules, and the teacher can rename signs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; tapping another spot during a replay stops it and zooms there.
- `Hang it` shows only after a sign is picked; before that the hint says "Tap a sign to hear it." and never names `Hang it`.
- `Vote` shows only after a rule card is picked.
- A sign can be swapped any time; the replay updates.
- With Motion off each replay shows two still pictures (before and after) and votes show all at once.

## Look
- Accent `--brand` #1f5fa8 playground blue (header, sign posts, the vote board); gold #f4c542 (pulsing trouble spots, the chosen card); paper #eef4fb; ink #0b1d33; muted #4a5868. Scene: a school playground with a slide, swings and a fence by a quiet street.
- Contrast (WCAG 2.1, computed): white on brand 6.44:1; brand on paper 5.82:1; ink on paper 15.32:1; muted on paper 6.57:1; ink on gold 10.43:1.
- Never color alone: signs have pictures and words; votes show hands and a number.
- Different from this batch (forest green, brick red, sepia, festival purple).

## Art
- Local FLUX (`scripts/localart.py`): the playground wide (1, 16:9); slide, swings and gate close-ups each in three states: busy, calm, unchanged (9, 4:3); the rug circle (1, 16:9).
- People art goes to Gemini (`people: true`): Ms. Okafor (a Nigerian American teacher in her forties), 4 poses; playground kids about five years old, 8 kids with action poses for the replays (climbing, sliding, waiting in line, swinging, pointing at the ball, a teacher getting the ball); Mia (a Vietnamese American girl), Leo (a white boy with freckles), Ava (a Black girl with braids), Sam (a Puerto Rican boy who uses a wheelchair), each 4 expressions (talking, hand up, frowning, smiling) as separate cutouts; "illustrated kindergarten child <pose>, soft gouache, plain white background, big clear face"; 3:4; cutout yes.
- Sign text stays in code over a blank painted sign board (1).
About 52 images. Drawn in code: sign words, reason icons, vote count.

## Voice
Bank voice `warm-teacher` as Ms. Okafor and the narrator (unique in this batch); Mia by `playful-friend`, Leo by `hero-coach`, Ava by `big-sister`, Sam by `soft-breath`, all styled as five-year-olds (each unique in this batch). `Curio.voice` with `scope: () => state.mode + ':' + state.spot + ':' + state.step`, `welcomeAfter: true`.
- how `welcome` (whole first time unless cut by a tap): "This playground has no rules, and it's a mess! Tap a problem you see."
- event `spot`: the spot's problem ("Kids are bumping on the slide.").
- event `sign`: the sign's words, every tap.
- event, whole, `fixed`: "Look! That helped." then the replay.
- event `silly`: "Hmm. Did that fix it?"
- event `elsewhere`: "That rule is for a different spot."
- how `reason`: "We need this rule because... Tap the reason."
- event `reason-ok`: the full sentence ("We need this rule so nobody gets hurt.").
- event `reason-no`: "Is that why we need this rule? Listen again."
- event, whole, `all-fixed`: "All three rules are up. Now let's decide a swing rule together. Tap Swing meeting."
- how `meeting`: "Tap each friend to hear what they want. Then tap a rule card and tap Vote."
- event `care`: each classmate's line.
- event `vote-voice`: each classmate's yes or no reason, one at a time, whole.
- event `win`: "Ten pushes each wins! Most friends can live with that rule."
- event `lose`: "Not many friends could live with that one. Who said what? Tap a friend to listen again."
- how `friend`: "Leo's rule lost. What does a good friend do? Tap a picture."
- event `friend-result`: the result line for each choice.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: trouble spots with three signs, replay states, reason cards, the classmate meeting with keyed votes, friend choices, the poster.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sign | Always pick the first card | Card order is shuffled per spot and per load. |
| Sign | Pick by elimination after a miss | Allowed; each miss plays a replay that shows why, so even elimination watches the problem. |
| Sign | The sign that is used elsewhere | It hangs and changes nothing here; the arrow shows where it belongs. |
| Reason | "So I win" | Never accepted; the sign's line replays. |
| Vote | Pick the longest card | Card lengths are close and shuffled; only the fair rule wins the keyed vote. |
| Vote | Mash Vote | `Vote` needs a picked card; each loss names who to listen to. |
| Friend | Any picture | Each plays its own honest result; only "your turn is next" ends with both kids swinging, and there is no score. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut by the first tap).
2. Tap a spot: `spot`. Tap a sign: `sign`. Hang it: `fixed` (whole) then the replay, or `silly`, or `elsewhere`.
3. After `fixed`: `reason` (first time), then per tap `reason-ok` or `reason-no`, each before the next tap counts.
4. Third spot fixed: `all-fixed` (whole).
5. Meeting: `meeting` (first time); `care` per face tap; Vote: `vote-voice` for each classmate in turn (whole), then `win` or `lose`.
6. After `win`: `friend`, then `friend-result`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.3, 7, 11, 12 and D4.1, D4.8, grades K-2 | C3 Framework for Social Studies State Standards (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt (Curio Class copy of the C3 list) | yes |
| On a slide, one child at a time, climbing the ladder and sliding down feet first, is the safe way | U.S. Consumer Product Safety Commission, Public Playground Safety Handbook | Nemours KidsHealth, Playground Safety | yes |
| Young children should not run into the street after a ball; they should stop and get an adult | NHTSA, child pedestrian safety | Safe Kids Worldwide, pedestrian safety tips | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-09): the keyed votes from each classmate's stated care give Ten pushes 4 of 5 and every other rule 2 of 5, so exactly one rule wins a majority; each spot has exactly one helping sign and its different-spot sign belongs to another spot; each sign has exactly one keyed reason; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the zoomed spot and its signs fit; at 680x425 cards sit below and Ms. Okafor folds.
2. Each spot offers three spoken signs, at school and outside it. (D2.Civ.3.K-2)
3. Right, silly and different-spot signs replay three different ways. (D2.Civ.12.K-2)
4. Each hung sign gets a spoken picture reason. (D4.1.K-2)
5. The swing meeting plays each classmate, and only the fair rule wins. (D2.Civ.11.K-2, D4.8.K-2)
6. The friend choice plays honest results with rewind. (D2.Civ.7.K-2)
7. Hang it and Vote are never named before they show.
8. Tap while it plays: any tap during a replay or vote acts at once; no older line plays after a newer one.
9. Motion off: before and after stills; no network requests.

## Open questions
- None for Cory.
