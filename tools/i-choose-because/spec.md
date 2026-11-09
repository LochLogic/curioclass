# I Choose Because

## One idea
The town can do only one thing (a new playground or a bigger library, a clean-up day or a book swap, a bus stop by the school or by the store), and the student taps a choice and builds "I choose ___ because ___" from picture-word tiles, then answers Pip the puppet's opposite choice with "I agree because..." or "I disagree because...", and a reason that is only "because I want it" gets Pip's gentle "But why is it good for the town?", so they learn to state a choice, give a real reason with because, and agree or disagree politely.

## Not like
- because-bridge (K-2, spec): reasons an author gives in a text, ELA. Here the student's own reasons about town choices, ELD.
- classroom-phrases-game (live): classroom requests. Here choices and reasons.
- talk-moves-trainer (3-5, spec later): group discussion moves. Here one frame, one reason, one reply.
- bedtime-retell (K-2, spec, this batch): retelling in order. Here giving reasons.
- el-restaurante (K-12, spec, this batch): likes and requests in Spanish. Here reasons in English.

## Who and how
- Grades K to 2, English Language Development, module "Choosing and Giving Reasons". Standards: WIDA ELD-SS (Standard 5, the language of social studies), Argue key language use (WIDA 2020).
- Driver: one student; class mode is a projector vote where the class says the frame together and pairs agree or disagree (tool.json `driver: "student"`). Every tile, frame and line is read on tap.
- Six town choices. Help setting: Lots (picture tiles and full frames read aloud), Some (word tiles with small pictures, frames), Little (frames fade to "I choose" and a blank; the student picks words from a bank). Teacher notes map the levels to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Town meeting", "Class vote"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.
- Nothing is saved; `Print` prints the student's sentences as a small "My reasons" page.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Argue (state a choice) | Tap a choice and build "I choose the playground" | the choice and the frame | 2 |
| WIDA Argue (give a reason with because) | Add a reason tile that says why it's good for the town | the full sentence read back | 2 |
| WIDA Argue (agree or disagree with a reason) | Answer Pip with I agree because... or I disagree because... | Pip's reply and the student's frame | 3 |
| WIDA ELD-SS (community places, helpers, choices) | Use town words (playground, library, bus stop, clean-up, neighbors) in reasons | the picture-word tiles | 2 |
| WIDA Argue (best reason, not loudest) | See the mayor pick by the best reason on the town tally | the tally board | 4 |

## Screens and modes
Header (kit): title "I Choose Because"; `Town meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more for small hands, icon plus word.

**On load and first tap.** A town hall with bunting, two big picture choices on easels, Mayor Grace Kim at a little podium and Pip, a puppet friend in a striped hat, on a chair. First hint: "Tap the mayor to hear her." She says: "Our town can do one thing. Which one? Why?" The welcome is queued after it (`welcomeAfter: true`).

**Choose and say why.** The student taps a choice. A frame appears: "I choose [ ] because [ ]." The first slot fills with the choice; the second takes a reason tile. Reason tiles (with pictures): because kids can play, because we can read more books, because it keeps the park clean, because people can get to work, because neighbors can meet. Each tile is keyed to the choices it fits. `Hear it` reads the whole sentence.

**Pip's turn.** Pip picks the other choice and says why ("I choose the library because we can read on rainy days."). The student answers with "I agree because..." or "I disagree because..." and a tile. If the student's reason is "because I want it" or "because it's fun" for a choice where fun isn't the point, Pip asks kindly, "But why is it good for the town?", and the student tries again.

**Town tally.** After all six neighbors (tile characters) and the student speak, a tally board shows everyone's reasons. Mayor Kim reads the reasons and picks the choice with the best reason, not the most hands ("Lots of people want the playground, but the library reason helps everyone on rainy days."). Sometimes the student's side wins and sometimes not, and the mayor thanks each person for a reason.

**The six choices.** Playground or library; clean-up day or book swap; bus stop by the school or by the store; a crosswalk or a bike rack; a garden or a splash pad; a mural or more benches.

**Class vote.** The projector shows the choice; the class says "I choose ___ because ___" together and pairs agree or disagree.

At 1366x768 the easels and tiles fit; at 680x425 the tiles are below.

## Content
Written for Curio Class: six choices, about 40 reason tiles with pictures and keyed fits, Pip's reasons, neighbors' reasons and the mayor's decisions. Reasons are about the common good (safety, reading, play, getting places), never cost or money.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tiles can be swapped any time; there is no score.
- With Motion off Pip doesn't bounce and the tally fills at once.

## Look
- Accent `--brand` #2c6a2a town green (header, easel frames, tiles); gold #f4c542 (the chosen easel, the winning reason); paper #f2f8f1; ink #0d230c; muted #4c5e4b. Scene: a friendly small-town hall.
- Contrast (WCAG 2.1, computed): white on brand 6.56:1; brand on paper 6.08:1; ink on paper 15.42:1; muted on paper 6.47:1; ink on gold 10.22:1.
- Never color alone: Agree and Disagree tiles have words and a thumbs icon.
- Different from this batch (terracotta, hallway blue, night indigo, rewind amber).

## Art
- People art goes to Gemini: Mayor Grace Kim (a Korean American woman in her forties), 3 poses; Pip (a felt puppet with a striped hat, not a person), 4 poses; six neighbors (a mix of ages and backgrounds, one with a cane, one in a wheelchair), 1 pose each; "illustrated friendly <role> <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): town hall interior (1); twelve choice pictures (playground, library, clean-up, book swap, two bus stops, crosswalk, bike rack, garden, splash pad, mural, benches) (12); about 40 small reason icons (40).
About 66 images. Drawn in code: frames, tally board.

## Voice
Bank voice `warm-teacher` as Mayor Kim and the hint voice (unique in this batch); Pip and the neighbors are read by `lively-host` (unique in this batch). `Curio.voice` with `scope: () => state.choice + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Pick one, and tell us why it's good for the town."
- event, whole, `sentence`: the student's sentence.
- event `pip`: Pip's choice and reason.
- event `why`: "But why is it good for the town?"
- event `mayor`: the mayor's decision.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: frames with tile slots, keyed reason fits, Pip's turn, the tally, help levels.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reason | Pick any tile | Each tile is keyed to the choices it fits; a mismatch reads back and Pip asks how it helps. |
| "Because I want it" | Use it every time | Pip asks why once per choice; the turn waits for a town reason. |
| Agree or disagree | Always agree | Fine, but the frame needs a reason tile; a bare "I agree" asks "Why?" |
Low stakes by design: there is no score, and every reason gets thanked.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the mayor: her question, `welcome` (queued, first time).
2. Choose: `sentence` (whole) on Hear it; `why` as it fires.
3. Pip: `pip` (waits), then the student's reply.
4. Tally: `mayor`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 5 is the language of social studies; Argue is a key language use with features like a claim, reasons and evidence, and responding to others | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Sentence frames and visuals support young English learners' academic talk, and supports fade as proficiency grows | WIDA ELD Standards Framework, 2020 Edition, proficiency level descriptors | Colorín Colorado, sentence frames for English learners | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b25, 2026-11-09): each choice has at least four keyed town-reason tiles and at least one "want it" tile that triggers Pip's question; every Pip reason has a keyed agree and disagree tile; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 easels and tiles fit; at 680x425 tiles are below; controls are 56 px or more.
2. Choices and reasons build and read back. (WIDA Argue, ELD-SS)
3. Pip's turn takes an agree or disagree reply with a reason. (WIDA Argue)
4. The tally and mayor decide by reason. (WIDA Argue)
5. Help levels fade the frames as in Who and how.
6. Class vote and Print work.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Motion off: Pip is still and the tally fills at once; no network requests.
9. Every tile and frame is read on tap so a child who can't read yet can play.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).
