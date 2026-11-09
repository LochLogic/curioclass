# Story Building Blocks

## One idea
A short story, a short play and a short poem have each tumbled into scrambled blocks, and the child stacks every tower back in order, names each block (chapter, scene or stanza), and locks it only by tapping the earlier block it builds on (a clue in chapter 1 pays off in chapter 3); then one block is pulled out and the child sees which later block no longer makes sense, so they learn that every part of a story rests on the parts before it.

## Not like
- two-sides-theater (2, spec): beginning and ending scenes of one tale, then two points of view. Here three forms and the words chapter, scene and stanza, with links between parts.
- genre-remix (4, concept): features of poems, drama and prose. Here how parts build within each.
- story-map-treasure (1, spec): plot events on a map. Here parts and what each builds on.
- stay-in-character (3, spec): choices cause events. Here structure parts depend on earlier parts.
- side-by-side-reader (3-5, spec): comparing two texts. Here one text's parts.

## Who and how
- Grade 3, ELA, module "Chapters, Scenes and Stanzas" (Reading Literature). Standard: RL.3.5.
- Driver: one student or a pair (tool.json `driver: "student"`). Every block's text is read on tap.
- Three towers: Story (3 chapters), Play (3 scenes), Poem (4 stanzas). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grade 3"`.
- Nothing is saved; `Print` prints each rebuilt tower with its links.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.5 (terms) | Label each block chapter, scene or stanza | the label stamped on the block | 2 |
| RL.3.5 (order) | Stack the blocks in order; a wrong order makes the tower lean with a note | the tower straight or leaning | 3 |
| RL.3.5 (builds on) | Lock each block by tapping the earlier block it builds on and the clue line that links them | a glowing beam between the two | 4 |
| RL.3.5 (builds on) | Pull-out test: one block is removed; tap the later block that no longer makes sense and say why | the wobbling block and a why tile | 5 |

## Screens and modes
Header (kit): title "Story Building Blocks"; `Towers`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A building site with three tumbled towers labeled Story, Play and Poem, and Foreman Brix, a beaver in a hard hat. First hint: "Tap a tower to start rebuilding." The first tap opens it with its line; the welcome is queued after it (`welcomeAfter: true`).

**Build.** Focus: a build zone (base 360 wide) and the scattered blocks (each 340 x 120 with a small scene picture and its first line; tap to hear the whole part). Drag a block onto the stack. When the stack is complete, `Check` tests the order: a wrong order leans the tower, and the note names what's missing ("Scene 2 talks about the soup pot, but nobody has brought it yet.").

**Name.** Each block gets a label stamp: chapter, scene or stanza. A wrong stamp shows the clue ("This has character names and stage directions. It's part of a play.").

**Link.** For every block after the first, tap the earlier block it builds on, then tap the clue line in that earlier block (data: 1 or 2 accepted clue lines per link). The beam glows and the block locks.

**Pull-out.** Brix pulls one block from a finished tower (data picks which). The child taps the later block that now doesn't make sense and picks the why tile; then puts the block back.

At 1366x768 the build zone and blocks fit; at 680x425 the blocks are in a tray drawer.

## Content
- **Story: "The Note in the Library Book"** (original, 3 chapters). Ch. 1: Ada finds a note in a library book: "Look under the oldest tree." Ch. 2: she and her brother search the park and learn which tree is oldest from a plaque. Ch. 3: under the tree is a box from the town's 1950 time capsule club, with a note asking the finder to add something and return it. Links: ch. 2 builds on the note; ch. 3 builds on the plaque.
- **Play: "Stone Soup"** (original three-scene play adapted from the traditional folktale, which is told in many versions across Europe). Scene 1: a hungry traveler arrives in a village where everyone says they have no food; scene 2: he sets a pot of water and a stone to boil and villagers each add something "to make it even better"; scene 3: everyone shares the soup, and the traveler leaves the stone. Links: scene 2 builds on the pot and the villagers' "no food"; scene 3 on each added ingredient.
- **Poem: "My Shadow"** by Robert Louis Stevenson (A Child's Garden of Verses, 1885, public domain), 4 stanzas. Links: stanza 2 (how the shadow grows and shrinks) builds on stanza 1's shadow that goes in and out with the speaker; stanza 3 (the shadow sticks close and doesn't know how to play) builds on stanza 2's odd behavior; stanza 4 (one early morning the shadow stayed asleep in bed) builds on stanza 1's line about the shadow jumping into bed first.
- Pull-outs: story ch. 2 (ch. 3's tree makes no sense), play scene 1 (scene 2's "no food" joke is lost), poem stanza 1 (stanza 4's "my shadow" has no setup).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Blocks snap to the stack; dragging one off reopens the gap.
- Link taps: earlier block first, then clue line; a wrong clue line gets "That line is in the block, but does the later part need it?"
- Pull-out happens once per tower and can be replayed.

## Look
- Accent `--brand` #b04517 brick orange (header, labels, hard hats); gold #f4c542 (beams, the lock glow); paper #fdf7f2; ink #2a160b; muted #68564a. Scene: a sunny building site with cranes.
- Contrast (WCAG 2.1, computed): white on brand 5.66:1; brand on paper 5.33:1; ink on paper 16.23:1; muted on paper 6.55:1; ink on gold 10.60:1.
- Never color alone: labels are words; the lean is shown with a note; locked blocks show a lock icon.
- Different from this batch (game-show violet, trail green, fair red, clinic blue).

## Art
Local FLUX (`scripts/localart.py`); people in the scenes are small and story-book style (Ada and her brother, villagers, the traveler) and drawn locally at block-face size, with no close faces.
- site (1): "A sunny cartoon building site with three tumbled block towers and a crane, soft gouache, no text"; 16:9; cutout no.
- Brix (4, point, lift, think, cheer): "A friendly beaver construction foreman in a hard hat <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- block faces (10): "<a note in a library book / a park with an old oak and a plaque / a village square with a big pot / a child and its shadow at bedtime / ...>, soft gouache, small scene"; 17:6; cutout no.
About 15 images. Drawn in code: blocks, stack, beams, stamps.

## Voice
Bank voice `hero-coach` as Brix and the reader of the blocks (unique in this batch). `Curio.voice` with `scope: () => state.tower + ':' + state.step`, `welcomeAfter: true`.
- event `tower`: "The {Play} tower fell down!"
- how `welcome`: "Every tower here fell down. Rebuild each one in order, name every block, and show what each one builds on."
- event, whole, `block`: the block's text.
- how `stackHow`: "Drag the blocks onto the base, first part at the bottom. Then tap Check."
- event `lean`: the lean note.
- how `nameHow`: "Stamp each block: chapter, scene or stanza."
- how `linkHow`: "Tap the earlier block this one builds on, then tap the line that links them."
- event `locked`: "Locked in!"
- event `pullOut`: "I pulled one out. Which block doesn't make sense now?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Try orders until straight | 6 orders for 3 blocks, 24 for 4; each lean shows a note naming the missing setup, so the trying is reading. |
| Labels | Stamp all "chapter" | Each tower uses one label; three towers use all three, and wrong stamps show the form's clue. |
| Links | Tap any earlier block | Only the data block and 1 or 2 clue lines count; random clue lines fail. |
| Pull-out | Guess | One block of 2 or 3 later blocks, plus a why tile. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a tower: `tower`, `welcome` (queued, first time), `stackHow`.
2. Tap a block: `block` (whole). Check: `lean` if wrong.
3. Name: `nameHow`. Link: `linkHow`, `locked`.
4. Pull-out: `pullOut`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.5 wording | thecorestandards.org, Reading Literature Grade 3 | CCSS ELA 2010 PDF | yes |
| "My Shadow" by Robert Louis Stevenson, A Child's Garden of Verses (1885), 4 stanzas, public domain | Project Gutenberg, A Child's Garden of Verses | Poetry Foundation, "My Shadow" | yes |
| "Stone Soup" is a traditional European folktale told in many versions (tale type ATU 1548, The Soup Stone) | D. L. Ashliman, Folktexts (University of Pittsburgh), Stone Soup type 1548 | Uther, The Types of International Folktales (2004), type 1548 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b10, 2026-11-08): orders 3! = 6 and 4! = 24; each tower has a pull-out with one block that loses its setup; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the build zone and blocks fit; at 680x425 blocks are in a drawer.
2. Stamps accept chapter, scene or stanza with clues on wrong stamps. (RL.3.5)
3. Check leans a wrong order and names what's missing. (RL.3.5)
4. Links lock only with the right earlier block and a data clue line. (RL.3.5)
5. Pull-out asks which block breaks and why, then restores. (RL.3.5)
6. All three towers work, and Print shows each with links.
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the tower doesn't lean (an outline and the note show instead); no network requests.

## Open questions
- None for Cory.
