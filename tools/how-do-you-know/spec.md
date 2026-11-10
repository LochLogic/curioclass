# How Do You Know?

## One idea
Pockets, a talking backpack, has one question (What do pandas eat?) and two things to read (a zoo keeper's fact page with headings, a photo and a caption, and a bright toy shop poster), and the child picks which to read first by who made it and how it looks, calls each line Fact or Opinion, and taps "How do you know?" to hear whether that line could be checked, then asks questions about the poster's argument and answers Pockets' questions about the zoo page, so the final answer card uses only facts that can be checked, with the source named.

## Not like
- source-scout (5, concept): many sources and how much to trust each at grade 5. Here two sources and fact or opinion at grade 2.
- wonder-kite (1, spec, this batch): building questions. Here judging sources.
- capsule-from-1965 (1, spec): who made an old object, when and where. Here which of two sources helps answer a question.
- changemaker-cards (2, spec, this batch): questions about people who made change. Here questions about a claim.

## Who and how
- Grade 2, Social Studies (Inquiry), module "How Do You Know?". Standards: D3.1.K-2 (gather relevant information from one or two sources), D3.2.K-2 (evaluate a source by distinguishing between fact and opinion), D4.4.K-2 (ask and answer questions about arguments).
- Driver: one child alone by default (the idea card's fit note), or the teacher on the projector with the class calling Fact or Opinion; every line, card and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Format: mystery, three cases. tool.json `modes: ["Pandas", "Leaves", "Firefighters"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`. Pandas is the main case; the other two use the same steps.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D3.1.K-2 | Pick which source to read first by who made it and how it is built, then pull the line that answers the question | the two sources with "Who made it?" tags; the answer line moving to the answer card | 2, 6 |
| D3.2.K-2 | Call each line Fact or Opinion, then tap "How do you know?" | each line stamped Fact (a check list icon) or Opinion (a heart icon), with Pockets' check | 3, 4 |
| D4.4.K-2 (ask) | Pick two good questions to ask about the poster's argument | the question cards and the poster's empty answers | 5 |
| D4.4.K-2 (answer) | Answer Pockets' question about how the zoo page knows | the three answer choices and Pockets' nod | 5 |

## Screens and modes
Header (kit): title "How Do You Know?"; `Pandas`, `Leaves`, `Firefighters`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A table with Pockets (a round yellow backpack with button eyes and a zipper smile) and two sources lying face up. Above them, a question card: "What do pandas eat?" The welcome is queued (`welcomeAfter: true`): "Hi, I'm Pockets! I have a question: what do pandas eat? We have two things to read. Tap one to see who made it." First hint: "Tap a source to see who made it." The first tap shows that source's "Who made it?" tag and cuts the welcome.

**Pick a source (focus: the two sources).** At 1366x768 the two sources sit side by side, Pockets at the left, the question card above. At 680x425 one source shows at a time with `Other source`.
- Zoo fact page: made by "Maple Ridge Zoo, panda keepers" (tag with a zoo badge). It has a heading "Giant Panda", a photo of a panda eating bamboo, a caption "A panda eats bamboo at our zoo", and a short "What pandas eat" section.
- Toy shop poster: made by "Toy Barn" (tag with a shopping bag). It has big sale letters, a photo of a stuffed panda, and stars.
- Both are made for this tool; the zoo and shop names are invented.
- Pockets asks: "Which should we read first to learn what real pandas eat?" The child taps one and `Read this first`. Zoo page: "Good thinking. Panda keepers work with real pandas." Poster: "Hmm, a toy shop sells toy pandas. Let's peek, but which one knows about real pandas?" The poster then opens second either way; the order only changes Pockets' line. Pockets also points to the parts: "See the heading? And the caption under the photo? Fact pages often have those."

**Fact or Opinion (focus: the open source's lines).** Each source has four lines. Pockets reads one at a time; the child taps `Fact` or `Opinion`. Then `How do you know?` shows; tapping it plays Pockets' check.
- Zoo page lines:
  1. "Giant pandas eat mostly bamboo." Fact. Check: "We could check this. Keepers watch what pandas eat every day."
  2. "Pandas spend many hours a day eating." Fact. Check: "We could watch a panda and count the hours."
  3. "Wild pandas live in the mountains of China." Fact. Check: "We could look at a map of where pandas live."
  4. "Pandas are a wonderful animal to visit!" Opinion. Check: "That's how the zoo feels. Someone else might feel differently." (So the fact page has an opinion too.)
- Poster lines:
  1. "Pandas are the cuddliest animal ever!" Opinion. Check: "We can't check cuddliest. It's a feeling."
  2. "Our panda is the best toy in town!" Opinion. Check: "Best is a feeling, not something we can measure."
  3. "Pandas are black and white." Fact. Check: "We can check: look at a photo of a real panda."
  4. "Sale: only 9 dollars!" Fact. Check: "We could check the price at the store." (A poster can have facts too.)
- A wrong call: "Could we check that, or is it a feeling?" and the line plays again.

**Ask and answer (focus: question cards).** Pockets: "The poster says, 'Buy our panda because pandas are the cuddliest!' What could we ask about that?" Four question cards; the child picks two good ones:
- "How do you know pandas are the cuddliest?" (good)
- "Who made this poster, and why?" (good: Pockets: "To sell toys!")
- "What's my favorite color?" (not about the argument)
- "Is it Tuesday?" (not about the argument)
Then Pockets asks: "The zoo page says pandas eat mostly bamboo. How does the zoo know?" Three answers: "Keepers feed and watch pandas every day" (right), "Because it's in big letters" (no: "Big letters don't make it true"), "Because pandas are cute" (no).

**Answer card (focus: the answer card).** The child drags fact lines that answer "What do pandas eat?" onto the card. Only zoo line 1 answers it; zoo line 2 is allowed as a helper ("Yes, that's about eating!"); opinions bounce off: "That's an opinion. Our answer needs facts." The card reads: "Pandas eat mostly bamboo. We know because the panda keepers at the zoo watch them every day. Source: Maple Ridge Zoo fact page." `Print` prints it.

**Leaves and Firefighters cases.** Same four steps with new sources (both invented):
- Leaves: "Why do leaves fall in fall?" Sources: a nature center tree guide and a garden store rake ad. Facts: "In fall, many trees stop making food in their leaves." "Trees drop their leaves to save water in winter." "Leaves change color before they fall." Opinions: "Fall is the prettiest season!" (guide), "Our rake makes raking fun!" (ad). Ad fact: "This rake is 4 feet long."
- Firefighters: "What do firefighters do?" Sources: the town fire department's page and a toy fire truck box. Facts: "Firefighters put out fires." "Firefighters help people who are hurt or stuck." "Firefighters teach fire safety at schools." Opinions: "Our firefighters are the bravest!" (page), "The coolest truck you'll ever own!" (box). Box fact: "Batteries included."

## Content
- Three cases, each: one question, two sources with "who made it" tags, eight lines (fact or opinion with a check line each), four question cards (two good), one "how does it know" question with three answers, and an answer card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `How do you know?` shows only after a Fact or Opinion tap on the current line. `Read this first` shows only after a source is tapped. Leaves and Firefighters are open from the start.
- With Motion off sources open without sliding and stamps appear without bouncing.

## Look
- Accent `--brand` #7a5a0c backpack mustard (header, the question card frame, stamps); gold #f4c542 (the lit line, the answer card edge, Pockets' zipper); paper #fbf7ec; ink #261c02; muted #5e5644. Sources keep their own looks (the zoo page calm and white with headings; the poster loud) inside the frame.
- Contrast (WCAG 2.1, computed): white on brand 6.37:1; brand on paper 5.95:1; ink on paper 15.70:1; muted on paper 6.79:1; ink on gold 10.33:1. The poster's own colors are art; every poster line is also read and shown in a plain line strip in ink on paper.
- Never color alone: Fact carries a check list icon and the word; Opinion carries a heart icon and the word.
- Different from this batch (timeline terracotta, kite sky blue, council green, changemaker purple).

## Art
- Local FLUX (`scripts/localart.py`): a panda eating bamboo (4:3); a stuffed toy panda (1:1); a tree in fall and a rake (2); a fire truck toy and firefighters at work seen from a distance (2, 4:3; the firefighters are small in the scene, no faces in focus).
- Pockets is drawn in code as a character (a rounded backpack with button eyes, a zipper mouth that moves while talking, 5 expressions).
- Drawn in code: both source layouts (headings, captions, poster letters, stars), stamps, question cards, the answer card.
About 6 images. No people art.

## Voice
Bank voice `friendly-dad` as Pockets (unique in this batch), style: cheerful and curious. `Curio.voice` with `scope: () => state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: "Hi, I'm Pockets! I have a question: what do pandas eat? We have two things to read. Tap one to see who made it."
- event `who`: the source's tag read aloud.
- how `pick`: "Which should we read first to learn what real pandas eat? Tap it, then Read this first."
- event, whole, `first`: the zoo or poster line, then the headings and caption line.
- event, whole, each source line.
- how `call` (once): "Is it a fact or an opinion? Tap Fact or Opinion."
- event `call-no`: "Could we check that, or is it a feeling?"
- how `check` (once): "Tap How do you know?"
- event, whole, each check line.
- event, whole, `argument`: the poster argument and "What could we ask about that?"
- event, whole, `how-zoo`: "The zoo page says pandas eat mostly bamboo. How does the zoo know?"
- how `card`: "Drag the facts that answer our question onto the answer card."
- event `bounce`: "That's an opinion. Our answer needs facts."
- event, whole, `answer`: the answer card read aloud.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). The fact-check family (`kit/fact-check.js`) is a grades 6-12 mock web and does not fit a two-source K-2 table. Tool-only code: two source layouts, line-by-line Fact/Opinion with checks, question cards, and the answer card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fact or Opinion | Call every zoo line Fact and every poster line Opinion | Each source has one of the other kind (zoo line 4 is an opinion; poster lines 3 and 4 are facts). |
| Fact or Opinion | Tap both buttons | The first wrong call plays the hint; Pockets' check plays only after a call. |
| Ask | Tap all four questions | Off-topic ones say "Is that about the poster's argument?" and don't count. |
| Answer card | Drag every line | Opinions bounce off; only lines about eating stay. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a source: `who`; then `pick`.
2. `Read this first`: `first` (whole).
3. Each line: the line (whole), waits; `call` (once); a call: stamp or `call-no`; `check` (once); `How do you know?`: its check (whole).
4. `argument` (whole), waits; question picks; `how-zoo` (whole), waits; answer pick.
5. `card`; drags: chime or `bounce`; done: `answer` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D3.1.K-2, D3.2.K-2 and D4.4.K-2 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Giant pandas' diet is almost all bamboo (about 99 percent), they eat for many hours a day, and wild pandas live in mountain forests of central China | Wikipedia, Giant panda (checked 2026-11-09) | Smithsonian's National Zoo, "Giant panda" | yes |
| Pandas are black and white | Wikipedia, Giant panda | WWF, "Giant panda" | yes |
| In fall many trees stop making food (chlorophyll breaks down), leaves change color, and trees drop leaves to save water in winter | USDA Forest Service, "Why leaves change color" | SUNY College of Environmental Science and Forestry, "Why leaves change color" | yes |
| Firefighters put out fires, help people who are hurt or trapped, and teach fire safety | U.S. Fire Administration, "Fire safety education" and firefighter roles | National Fire Protection Association (NFPA), "Firefighters" and Sparky school program | yes |
| A fact can be checked; an opinion tells what someone thinks or feels | Reading Rockets, "Fact and opinion" | ReadWriteThink, "Fact and opinion" lesson | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-09): each case has eight lines with at least one opinion on the fact source and at least one fact on the ad, so no source is all one kind; exactly two good questions in each set of four; each answer card uses only lines marked Fact; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 both sources, Pockets and the question fit; at 680x425 one source shows with `Other source`.
2. Each source shows who made it, and picking the first one plays its line. (D3.1.K-2)
3. Every line takes only its right call. (D3.2.K-2)
4. `How do you know?` plays a check line for every line. (D3.2.K-2)
5. Two good questions are needed about the argument, and the "how does the zoo know" answer is checked. (D4.4.K-2)
6. The answer card takes only facts that answer the question and names the source. (D3.1.K-2)
7. `How do you know?` and `Read this first` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no slides or bounces; no network requests.

## Open questions
- None for Cory.
