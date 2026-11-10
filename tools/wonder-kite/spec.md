# Wonder Kite

## One idea
The child picks one big question they really want to know (Why does our town have a library?) and says why it matters to them, then ties small questions to the kite's tail as bows, each marked with a badge (a map for where, a clock for when, a rule for who decides, a coin for who pays); a small question that helps answer the big one ties on, shows its fact and lifts the kite higher, while one that doesn't help ("What color is the sky?") drifts away, so a first grader learns that a big question is answered by small questions from different subjects that add up.

## Not like
- inquiry-ladder (4, concept): the grade 4 version with sources and words people argue about. Here a first grader's first big and small questions.
- how-do-you-know (2, spec, this batch): judging two sources, fact or opinion. Here making questions, not judging sources.
- capsule-from-1965 (1, spec): questions about one set of objects. Here questions sorted by subject that build one answer.
- my-life-timeline (1, spec, this batch): ordering events. Here linking questions.

## Who and how
- Grade 1, Social Studies (Inquiry), module "Wonder Kite". Standards: D1.1.K-2 (explain why a compelling question is important to the student), D1.2.K-2 (identify disciplinary ideas associated with a compelling question), D1.3.K-2 (identify facts and concepts associated with a supporting question), D1.4.K-2 (make connections between supporting questions and compelling questions).
- Driver: one child alone by default (the idea card's fit note), or the teacher on the projector with the class choosing; every question, badge and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- One kite at a time; three kites to choose from. tool.json `modes: ["Fly a kite", "Class kite"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D1.1.K-2 | Pick a big question and tap a picture reason why it matters to you | the kite's sail with the question and the child's reason pinned on it | 2 |
| D1.2.K-2 | Read each small question's badge (map, clock, rule, coin) and fill all four on the tail | the four badge slots on the tail filling | 3 |
| D1.3.K-2 | Tie on a helpful small question and hear the fact its bow holds | the bow opening to its fact card | 4 |
| D1.4.K-2 | Keep only bows that help the big question; pick which bow helped most | the kite rising per helpful bow; off-topic bows drifting away with a hint | 5, 6 |

## Screens and modes
Header (kit): title "Wonder Kite"; `Fly a kite`, `Class kite`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A grassy hill under a big sky. Three kites lie on the grass, each with a picture and a big question: a library ("Why does our town have a library?"), a crossing guard ("Why do we have a crossing guard?"), a market stand ("Why do people go to the farmers market?"). The welcome is queued (`welcomeAfter: true`): "Three kites, three big questions. Which one do you want to know most? Tap a kite to hear its question." First hint: "Tap a kite to hear its question." The first tap reads that kite's question and cuts the welcome; a second tap on the same kite picks it.

**Why it matters (focus: four picture reasons).** "Why do you want to know?" Four picture choices, each spoken: "I go there", "Someone I know works there", "I'm curious", "I want to help". The chosen one pins to the sail. Any choice is right; the reason is the child's.

**Tie the bows (focus: the pile of small questions).** At 1366x768 the kite is held low at the left with an empty tail of four badge slots (map, clock, rule, coin, each an icon plus a word: Where, When, Who decides, Who pays); a pile of six small question cards is at the right, each with its badge. At 680x425 the pile becomes a row of three cards with `More` to swap.
- The child drags a card to the tail. A helpful card ties on as a bow in its badge slot, opens to its fact (spoken), and the kite rises one step. An off-topic card drifts away on the wind: "Does that help us know why our town has a library? Try another." A card dropped in the wrong badge slot slides to its own slot (the badge is the subject, so the child sees which kind it is).
- Each kite has four helpful cards (one per badge) and two that don't help.
- Library:
  - Where: "Where is our library?" Fact: "Near the school and the park, so people can walk there."
  - When: "When did towns start having free libraries?" Fact: "Long ago. In 1833 a town called Peterborough, in New Hampshire, opened the first free library paid for by the town."
  - Who decides: "Who decides what books it has?" Fact: "Librarians choose books for everyone, and people can ask for books too."
  - Who pays: "Who pays for the library?" Fact: "The town pays with taxes, money everyone shares. So the library is free to use."
  - Don't help: "What color is the sky?"; "Do cats like milk?"
- Crossing guard:
  - Where: "Where does the crossing guard stand?" Fact: "At a busy street near the school, where kids cross."
  - When: "When does the crossing guard work?" Fact: "Before school and after school, when lots of kids walk."
  - Who decides: "Who decides we need one?" Fact: "The town and the school look at busy crossings and decide."
  - Who pays: "Who pays the crossing guard?" Fact: "In many towns, the town or the school district pays them."
  - Don't help: "How fast can a cheetah run?"; "What is my favorite song?"
- Farmers market:
  - Where: "Where does the food come from?" Fact: "From farms near our town."
  - When: "When is the market open?" Fact: "On the same day each week, mostly in summer and fall when food is growing."
  - Who decides: "Who decides where the market goes?" Fact: "A market manager asks the town, and the town says yes to a spot."
  - Who pays: "Who gets the money people spend?" Fact: "The farmers who grew the food."
  - Don't help: "How many legs does a spider have?"; "Is the moon made of cheese?"
- With four bows tied, the kite flies high. The four facts line up on the tail and the narrator puts them together: "Our town has a library so everyone can borrow books for free. It's near where people walk, towns have had them for a long time, librarians choose the books, and the town pays with taxes." Then: "Which bow helped you most?" The child taps one; it glows gold and the narrator says why that kind of question matters ("Who pays questions tell us how a town shares.").
- `Fly another` picks a new kite. `Print` prints the kite, reason, four questions and facts.

**Class kite (focus: an empty kite).** For the teacher: a text box for a big question and four text boxes for small questions, each with a badge picker. No facts or off-topic cards; the class answers each small question aloud and the teacher taps `Tie it` to lift the kite. A class vote option shows the three built-in kites with tally buttons.

## Content
- Three kites, each with one big question, four helpful small questions (one per badge) with a fact each, and two off-topic cards.
- Four reasons. Four "why it matters" lines for the most-helpful pick (one per badge).

## Interactions in detail
- Every tap acts at once; a new line stops the old one; dropping a card during a fact plays the new card's line.
- `Fly another` shows only after the most-helpful pick. `Tie it` shows only in Class kite once a small question is typed.
- Keyboard: Tab to a card, Enter to pick it up, Enter again to drop it on the tail.
- With Motion off the kite steps up without swaying and off-topic cards fade instead of drifting.

## Look
- Accent `--brand` #1d5f99 sky blue (header, the tail, badge slots); gold #f4c542 (the tied bow ring, the most-helpful glow); paper #eef6fc; ink #08223a; muted #4b5b68. The kite sails use the badge colors only with icons and words.
- Contrast (WCAG 2.1, computed): white on brand 6.67:1; brand on paper 6.10:1; ink on paper 14.78:1; muted on paper 6.42:1; ink on gold 9.93:1.
- Never color alone: every badge carries an icon and a word.
- Different from this batch (timeline terracotta, council green, changemaker purple, backpack mustard).

## Art
- Local FLUX (`scripts/localart.py`): the hill and sky (16:9, painted with room above for the kite to rise); three kites on the grass (1); kite pictures for the sails: a library, a crossing with a guard seen from far away (no face), a market stand (3, 1:1); four reason pictures (4, 1:1); small pictures on fact cards: a map-like town, an old library, books, coins, a school crossing, a clock, a farm, a market (8, 1:1).
- Drawn in code: the kite, the tail and bows, badges (map, clock, gavel, coin), cards, the drift.
About 20 images. No people art.

## Voice
Bank voice `upbeat-guide` as the narrator (unique in this batch), style: bright and breezy. `Curio.voice` with `scope: () => state.kite + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Three kites, three big questions. Which one do you want to know most? Tap a kite to hear its question."
- event `big-q`: the kite's question, then "Tap it again to pick it."
- how `why`: "Why do you want to know? Tap a picture."
- how `tie` (once): "Drag a small question to the kite's tail. If it helps, it ties on."
- event, whole, `fact`: each fact.
- event `drift`: "Does that help us know [big question]? Try another."
- event `slot`: "That's a [badge] question. It goes here."
- event, whole, `answer`: the four facts put together.
- how `most`: "Which bow helped you most? Tap it."
- event, whole, `most-why`: the badge's line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the kite and tail with four badge slots, card drop with helpful or drift, the rise per bow, and the Class kite text boxes.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Bows | Drag every card | Off-topic cards drift away with the big question read back; only four cards tie on. |
| Bows | Ignore badges | Badges place themselves; the child sees each kind fill, so all four subjects show. |
| Most helpful | Tap any bow | Any is fine; the line then says why that kind of question matters. |
| Why it matters | Tap any reason | The reason is the child's own; there is no wrong one. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a kite: `big-q`.
2. Pick: `why`; tap a reason: it pins.
3. `tie` (once). Each drop: `fact` (whole), `drift`, or `slot` then `fact` (whole).
4. Four bows: `answer` (whole), waits; then `most`; tap: `most-why` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D1.1 to D1.4 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Peterborough, New Hampshire, opened the first tax-supported free public library in the United States in 1833 | Wikipedia, Peterborough, New Hampshire (checked 2026-11-09) | Peterborough Town Library, "History" | yes |
| Public libraries are paid for by taxes and free to use | Wikipedia, Public library (checked 2026-11-09) | American Library Association, "Public library funding" | yes |
| Crossing guards help children cross busy streets near schools before and after school; towns, police or school districts hire them | National Center for Safe Routes to School, "Adult School Crossing Guard Guidelines" | Wikipedia, Crossing guard (checked 2026-11-09) | yes |
| At a farmers market, farmers sell food they grew directly to shoppers | Wikipedia, Farmers' market (checked 2026-11-09) | USDA Agricultural Marketing Service, "Farmers markets" | yes |
| Librarians select books for a library's collection | American Library Association, collection development | Wikipedia, Collection development (checked 2026-11-09) | yes |
Backed twice: 6. Cut: 0.

The library's "near the school and park" and the market's "same day each week" lines describe the made-up town in the art, not a real one.

Checks run (Python, scratchpad r3, 2026-11-09): each kite has exactly one helpful card per badge and two off-topic cards; every fact is 25 words or fewer; the three "answer" lines use all four facts; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 kite, tail and pile fit; at 680x425 the pile shows three cards with `More`.
2. Picking a kite asks why it matters and pins the child's reason. (D1.1.K-2)
3. All four badge slots fill on each kite; a card in the wrong slot moves to its own. (D1.2.K-2)
4. Each helpful card's fact plays and shows. (D1.3.K-2)
5. Off-topic cards drift away with the big question read back; the kite rises only for helpful ones. (D1.4.K-2)
6. The answer line joins the four facts; the most-helpful pick explains its kind. (D1.4.K-2)
7. `Fly another` and `Tie it` are never named before they show.
8. Tap while it plays: a drop during a fact plays the new line at once; no older line plays after a newer one.
9. Motion off: no sway or drift; no network requests.

## Open questions
- None for Cory.
