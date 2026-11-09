# Root Detective Cards

## One idea
The student collects Greek and Latin root and affix cards and plays them to crack unknown words in case sentences (transportable, telegraph, autograph), building each word's meaning from its parts, checking it against the sentence and then the dictionary card, and solved cases win new root cards, so they learn that a few roots unlock hundreds of words; the case wall ends with one root (port) linking a dozen words the student can now read.

## Not like
- word-lab (2, spec): word parts in beakers. Here Greek and Latin roots at grade 4.
- glossary-makers (3-5, spec): subject words in a passage. Here roots as the main tool across many words.
- word-family-tree (12, spec): word histories. Here meanings for reading.
- syllable-surgeon (3, spec): decoding by syllables. Here meaning by roots.
- context-roots-dictionary (6-8, concept): older readers. Same engine.

## Who and how
- Grade 4, ELA, module "Greek and Latin Roots" (Language). Standard: L.4.4 (a, b, c).
- Driver: one student, or two trading cards (tool.json `driver: "student"`). Every card, sentence and dictionary entry is read on tap.
- 24 cases over four case files; 20 root and affix cards to win. tool.json `modes: ["Solo", "Partners"]`, `minutes: "15-25"`, `grades_label: "Grade 4"`.
- Saving: the card collection and case wall are kept in this browser; footer: "Your cards stay on this device." `Clear my cards` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.4.4b | Play cards onto the word to split it and build a meaning from the parts (trans = across, port = carry, -able = can be) | the word split with a card on each part | 2 |
| L.4.4a | Check: does the built meaning fit the case sentence? Pick from three sentence readings | the sentence read with the meaning in place | 3 |
| L.4.4c | Open the dictionary card to confirm the meaning and hear the pronunciation | the entry with respelling and audio | 4 |
| L.4.4b | Build round: combine cards into real words; fake words get a "No such word" stamp | the build tray and stamps | 5 |
| L.4.4 (all) | The final case: a word never seen before, solved with all three tools | the case closed stamp and strategy log | 6 |

## Screens and modes
Header (kit): title "Root Detective Cards"; `Cases`, `My cards`, `Case wall`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A detective agency office with a card table and Inspector Quill, a fox in a trench coat with a magnifier. First hint: "Tap Case 1 to open it." The first tap reads the case sentence; the welcome is queued after it (`welcomeAfter: true`).

**Hand.** Starter hand of 7 cards: tele, graph, port, auto, -able, re-, trans-. Each card has the part, its meaning, its language (Greek or Latin) and a small picture (a far-off tower for tele, a pencil line for graph, a carried box for port, a mirror for auto).

**Case.** The case sentence with one word in a magnifier: "The museum's new exhibit was transportable." The student drags cards onto the word; a card snaps only onto a matching stretch (`wl.split`); helper chips fill the small leftover parts on their own. When every part is covered, the meanings line up ("across + carry + can be") and the student picks the best plain meaning from three ("can be carried from one place to another").

**Context check.** The sentence is read with the meaning swapped in; the student says whether it fits.

**Dictionary card.** Opens the entry: respelling, syllables, audio, part of speech, the meaning. The strategy log marks which tool cracked it (context, parts or dictionary).

**Rewards.** Solved cases win new cards (spect, dict, scrib, struct, bio, geo, phon, micro, therm, aud, vis, ject, rupt, tract, -logy, -ful, -less, pre-, sub-, inter-).

**Build round.** Combine cards into words (`wl.build`): real words go to the case wall with a check; non-words get "No such word" (`wl.build` returns nothing); near misses show `wl.near` ("Did you mean report?").

**Case wall.** A string board with each root in the middle and its words around it; port links export, import, report, portable, transport, transportation, support, passport, airport, porter, important (an "odd one" note: important's link to port is distant, so it is shown in gray as "related, not obvious").

**Final case.** A word not in any deck before, built from known parts ("The scientist used a microphone, then studied the phonograph." with phonograph new), solved with all three tools.

**Partners.** Two players hold separate hands and trade cards to solve a shared case.

At 1366x768 the hand, case and dictionary fit; at 680x425 the hand is a tray.

## Content
- 27 morphemes on cards with kid meanings and language (data, from the word-lab engine's Morphemes), plus helper chips: small free parts that are not cards (in-, con-, pro-, e-, -or, -ion, -ence, -ible, -ate, -ator, -ience, -y, -o-, -e, scope, meter, turn, view, care), each with its meaning, so every case word can be fully split while the card does the main work.
- 24 cases (6 per file), each sentence written for Curio Class with a target word whose parts are all in the deck: transportable, telegraph, autograph, return, transport, telephone, autobiography, spectator, dictate, inscribe, construction, biology, geography, portable, microscope, thermometer, audience, visible, project, erupt, tractor, careful, careless, preview.
- Dictionary entries for every word (respelling, part of speech, meaning).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Keyboard path: pick a card, then the word stretch.
- A wrong card bounces with its meaning read ("graph means write. Does this word have a graph part?").
- Collection and wall persist; the build round has no limit.

## Look
- Accent `--brand` #6a3d6e root plum (header, card backs, string); gold #f4c542 (snapped cards, closed stamps); paper #f9f4f9; ink #22122a; muted #625466. Scene: a warm detective agency.
- Contrast (WCAG 2.1, computed): white on brand 8.38:1; brand on paper 7.72:1; ink on paper 16.28:1; muted on paper 6.49:1; ink on gold 10.87:1.
- Never color alone: Greek and Latin cards show the word "Greek" or "Latin" and a glyph from the engine's Road key.
- Different from this batch (rover indigo, card red, chameleon green, glacier teal).

## Art
Local FLUX (`scripts/localart.py`).
- office (1); Inspector Quill (4 poses: magnify, point, think, stamp), "A friendly fox detective in a trench coat with a magnifying glass <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- card pictures (27), "<a small picture for the meaning: a far-off radio tower / a pencil drawing a line / a person carrying a box shown as a simple hand and box / a mirror>, flat sticker style, plain white background"; 1:1; cutout yes.
About 32 images. Drawn in code: cards, magnifier, string board, stamps.

## Voice
Bank voice `knowing-guide` as Inspector Quill (unique in this batch). `Curio.voice` with `scope: () => state.file + ':' + state.case + ':' + state.step`, `welcomeAfter: true`.
- event `case`: the case sentence.
- how `welcome`: "Long words are made of smaller parts. Play a card on each part, and the meanings will crack the case."
- how `playHow`: "Drag a card onto a part of the word in the magnifier."
- event `bounce`: "{graph} means {write}. Does this word have a {graph} part?"
- event `fits`: the sentence with the meaning swapped in.
- event `entry`: the dictionary pronunciation and meaning.
- event `won`: "Case closed! You won the {spect} card. It means {look}."
- event `noWord`: "No such word. Try another card."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
word-lab (`kit/wordlab.js`), described in full in tools/word-family-tree/spec.md, exposed as `__tool.wl`. This tool uses: Morphemes, Word records, Split (snapping cards onto stretches), Build (`wl.build`, `wl.near` for the build round), Lookup (the dictionary card), Strategy log (context, parts, dictionary), Guess and verify (the meaning pick), Road key (Greek and Latin glyphs). Not Tree view or Card view (the case wall is drawn in tool code).

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Splitting | Drag every card on | Cards snap only on matching stretches; bounces read the card's meaning. |
| Meaning pick | Guess | 3 choices; the context check reads the pick in the sentence, so a wrong one sounds wrong. |
| Build round | Try random pairs | Non-words get stamped; only real words count (from Word records). |
| Final case | Open the dictionary first | Allowed: the log records it; dictionary use is a real strategy, and the parts still show on the card. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a case: `case`, `welcome` (queued, first time), `playHow` (first time).
2. Cards: `bounce` on misses.
3. Meaning picked: `fits`. Dictionary: `entry`.
4. Solved: `won`. Build round: `noWord` on misses.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.4.4 wording | thecorestandards.org, Language Grade 4 | CCSS ELA 2010 PDF | yes |
| Meanings and languages of the 27 parts (tele far, Greek; graph write, Greek; port carry, Latin; auto self, Greek; trans across, Latin; spect look, Latin; dict say, Latin; scrib write, Latin; struct build, Latin; bio life, Greek; geo earth, Greek; phon sound, Greek; micro small, Greek; therm heat, Greek; aud hear, Latin; vis see, Latin; ject throw, Latin; rupt break, Latin; tract pull, Latin; and the affixes) | Merriam-Webster, etymologies | Online Etymology Dictionary | yes |
| Important comes from Latin importare (to bring in, to carry in), a distant link to port | Online Etymology Dictionary, important | Merriam-Webster, important (etymology) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b14, 2026-11-09): every case word splits fully into card parts and helper chips with at least one card; all 24 case words are distinct; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the hand, case and dictionary fit; at 680x425 the hand is a tray.
2. Cards snap onto matching parts and build a meaning. (L.4.4b)
3. The context check reads the meaning in the sentence. (L.4.4a)
4. The dictionary card gives respelling, audio and meaning. (L.4.4c)
5. The build round accepts real words and stamps fakes. (L.4.4b)
6. The final case logs the tools used.
7. The case wall links each root's words.
8. Cards survive a reload where storage works; `Clear my cards` removes them.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: cards place without flipping; no network requests.

## Open questions
- None for Cory.
