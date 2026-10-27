# Word Family Tree

## One idea
English is a family reunion of cousins who don't know they're related: grow a tree from one ancestor root and watch its words reach English by different roads (straight from Latin, through Old French, through Old English or Old Norse), then meet the doublets, pairs like frail and fragile or royal and regal that share one ancestor, took different roads, and came out meaning slightly different things.

## Not like
- context-roots-dictionary (ela 6-8, puzzle, word-lab family, not specced): cracks one academic word at a time by context, then root, then dictionary. Here the root is the starting point and the subject is how a family of words spread and drifted; the unknown-word strategy is one mode, not the whole tool.
- key-term-tracker (ela 9-12, explorer, this group and family): follows one word's meaning through one text. Here many words across centuries, and no single text.
- root-detective-cards (ela 4, cards, family, not specced): collects common roots to build words. Here the roots are a starting point for history: roads, borrowings, doublets and fossil metaphors.
- myth-museum (ela 4, explorer, not specced): words from Greek myths. Here Latin, Greek, Old English, Old Norse and French roads, and no myths.
- usage-panel (ela 11, roleplay, spec): the history of opinions about one usage. Here the history of the words themselves.

## Who and how
- Grade 12 ELA. Module: Advanced Vocabulary and Etymology (Language).
- Topic line: "etymology".
- Driver: students on laptops, alone or in pairs; a teacher can project one tree to open. 20 to 40 minutes.
- Standards: L.11-12.4 (determine or clarify unknown words: 4a context, 4b patterns of word changes such as conceive, conception, conceivable, 4c reference materials for pronunciation, part of speech, etymology, 4d verifying a guess): Unknown word mode and the Change the form strip. L.11-12.5 (figurative language, word relationships and nuances: 5a figures of speech, 5b nuances of words with similar denotations): Doublets (5b) and Figures (5a): fossil figures hidden inside words, and live figures (hyperbole, paradox, metaphor) read in context in public-domain passages, where the student names the figure and says what it does in that text.
- tool.json: driver "students or teacher", minutes "20-40", modes ["Grow", "Doublets", "Figures", "Unknown word"], grades_label "Grade 12". Kit starter plus `kit:theme-912` and `kit:wordlab`.

## Screens and modes
Header: title "Word Family Tree", small line "Same ancestor, different roads."; mode buttons **Grow** (opens first), **Doublets**, **Figures**, **Unknown word**; Motion, Sound, Read. Panel: `#hint`, the road key (each language's glyph and color), the word card for the selected word, **Found** count ("doublets found: 3 of 8").

### Grow (opens first)
- Root picker: 9 roots as seed buttons along the bottom (Content): capere, frangere, caput, hospes, graphein, Germanic ward, regere, dignus, sker- ("cut").
- Stage: the chosen root as a trunk at the bottom ("Latin capere, to take, seize"). **Grow** (or tap the trunk) sends out branches, one per road, each labeled with its language and glyph: ⬢ Latin, ✦ Greek, ◆ Old English, ▲ Old Norse, ● Old French and Anglo-Norman, ■ Frankish, ◇ Italian or Spanish, ★ modern French. Leaves are modern English words, each a rounded tag.
- Tap a leaf: the word card in the panel shows the word, part of speech, respelling, a one-line meaning, and its road as a chain of stops ("Latin concipere > Old French conceveir > English conceive"). **Show on tree** traces that road in brand color from trunk to leaf.
- **Change the form** strip (capere tree): rows of verb, noun, adjective (conceive, conception, conceivable; receive, reception, receivable; perceive, perception, perceptible; deceive, deception, deceptive), each with the stem lit: "ceive" (came through French) and "cept" (kept Latin's past-participle stem). A note: "Why conceive but conception? The -ceive verbs came through Old French; the -cept- words keep the stem of Latin's past participle."
- **False cousins**: on the hospes tree, a dashed ghost branch "host (an army), hostile" from a different root, Latin hostis, with the line "Looks like family. It isn't."
- **Doublet glints**: two leaves from one root that form a doublet get a small linked-rings mark; tapping it opens that pair in Doublets when the pair is in the gallery, or otherwise a pair card in the panel with both roads and the nuance line (Content).

### Doublets
- A gallery of 8 pairs (one triple). Each pair card shows the two words side by side, the shared ancestor above them, and both roads drawn as two branches from one trunk.
- **Which fits?**: two sentences per pair, each with a blank. The student drags or taps a word into each blank. Feedback names the nuance, not a score: "Fragile: easily broken, usually said of things. Frail: weak in body or health, usually said of living things." Mismatches show the same nuance line with "Try the other one."
- A pair counts as found when both blanks are right; Found rises. All pairs are open from the start.
- **Your own sentence**: one box per pair for the student's sentence using either word, kept on the device.

### Figures
Two shelves, **Fossil** (opens first) and **Live**.
- Fossil: 7 cards, each a word whose origin is a figure of speech that has gone stiff: the card shows the word, then **Crack it open** reveals the original picture ("muscle: Latin musculus, little mouse") and asks "Why would someone have called it that?" with a short box for the student's idea; **One explanation** then shows the usual account (Content).
- Fossil: one card is a myth: "sincere" with the popular story "without wax", and **Crack it open** shows "That story is not supported. Sincere comes from Latin sincerus, clean, pure." The card is labeled "Myth check".

- Live: 6 cards, each a short public-domain passage with the figure underlined (Content). The student taps a chip to name it (**Hyperbole**, **Paradox**, **Metaphor**); a wrong chip shows what that figure would need ("A paradox seems to contradict itself. Does this?") and stays open for another try. Then a box asks "What does it do in this passage?" and **One reading** shows a note, labeled "One reader's reading." A last line on each Live card links back to Fossil: "Metaphors that get used enough turn into fossils, like muscle."

### Unknown word
- 6 sentences, each with one hard word underlined (Content). Steps, each a button the student presses in order, and each unlocked by the one before:
  1. **Context**: the student types a guess at the meaning from the sentence alone.
  2. **Parts**: the word splits into its parts with meanings (engine Split), and the student may revise the guess.
  3. **Dictionary**: the entry card (respelling, part of speech, etymology line, meaning).
  4. **Verify**: the student ticks "My guess fits the sentence" or "My guess needed the dictionary" and the tool logs which step cracked it.
- **Strategy log** (panel): for each word, the step that cracked it, so a student sees whether context or parts did more of the work.

## Content
Roads and meanings follow Merriam-Webster and the Online Etymology Dictionary (Sources); "through" means the word passed through that language on its way to English.

### Trees (root, gloss; leaves with road)
1. Latin capere, "to take, seize" (participle captus; -cip-, -cept- in compounds). Latin: capture, captive, capable, accept, except, concept, reception, deception, perception, conception. Through Old French: conceive, receive, deceive, perceive. Through Anglo-Norman (Old North French cachier, from Latin captiare): catch. Through Old French (chacier, from captiare): chase, purchase. Doublet: catch and chase.
2. Latin frangere, "to break" (fractus). Latin: fragile, fraction, fracture, fragment, refract, infringe. Through Old French: frail. Doublet: fragile and frail.
3. Latin caput, "head" (capit-). Latin: capital, decapitate, precipice (from praeceps, "headlong"). Through Old French: captain, chief, chattel. Through Anglo-Norman: cattle (catel, "property", from Medieval Latin capitale). Modern French: chef. Doublets: chief and chef; cattle, chattel and capital.
4. Latin hospes, "guest, host" (hospit-). Latin: hospitality, hospital. Through Old French: host (one who receives guests), hostel. Modern French: hotel. Ghost branch: host (an army), hostile, from Latin hostis, "stranger, enemy". Triple: hospital, hostel, hotel.
5. Greek graphein, "to write". Through Latin: graphic, paragraph, biography, autograph. English coinings from Greek parts: graph, photograph. Greek gramma, "letter", from graphein, through Latin and Old French: grammar. Scots alteration of grammar: glamour (once meaning a magic spell, from the old sense of grammar as learning of any kind, including magic).
6. Germanic ward, "watch, guard" (Proto-Germanic *ward-, from the Indo-European root *wer-, "perceive, watch out for"). Old English: ward, wary, aware, beware, warn. Through Frankish and Old North French or Anglo-Norman, keeping the w-: warden, award, reward. Through Frankish and Old French, where Germanic w- became gu-: guard, guardian, regard. Doublets: ward and guard; warden and guardian; reward and regard. The tree's note: "French speakers said Germanic w- as gu-. Norman French kept the w-. English borrowed from both."
9. Indo-European *sker-, "to cut". Old English: shear, share, short, shirt (a short garment). Old Norse: skirt (skyrta), score (skor, "notch"). Latin: curt (curtus, "cut short"). Doublet: shirt and skirt. The tree's note: "Old English softened sk- to sh-; Old Norse kept sk-. Shirt and skirt are the same word, borrowed twice."
7. Latin regere, "to rule" (rex, regis, "king"; regula, "rule"; regnum, "reign"). Latin: regal, regular, region. Through Old French: royal, rule, reign. Doublet: regal and royal.
8. Latin dignus, "worthy". Latin: dignity, indignant. Through Old French: dainty (deintie, from dignitatem), deign, disdain. Doublet: dignity and dainty.
- Leaf data per word: part of speech, respelling, one-line meaning. The builder fills these from Merriam-Webster for every leaf above. If Merriam-Webster and the Online Etymology Dictionary disagree on a leaf's road, the leaf stays and its road shows "probably" with both sources named on the word card; a leaf neither source supports is cut.
- Pair cards for tree doublets not in the gallery (nuance lines, checked against Merriam-Webster at build): ward / guard ("ward: to fend off, or a person in someone's care; guard: to watch over, or the person who does"); warden / guardian ("warden: an official in charge of a place, like a prison or a park; guardian: someone who protects a person, often legally"); reward / regard ("reward: something given for what you did; regard: to look at or think of in a certain way"); shirt / skirt ("both a short garment; one covers the top, one hangs from the waist"); dignity / dainty ("dignity: being worthy of respect; dainty: small and delicate, once 'worthy, choice'"); chattel / cattle / capital ("chattel: movable property; cattle: livestock, once any property; capital: wealth, or the head city").

### Doublet pairs (Which fits?)
1. frail / fragile. "After the long illness, the old dog was ___." (frail) "The label said ___: handle with care." (fragile)
2. royal / regal. "The ___ family waved from the balcony." (royal: belonging to a king or queen) "She crossed the stage with a ___ calm." (regal: like a king or queen in manner)
3. loyal / legal. "A ___ friend keeps your secret." (loyal: faithful) "A ___ contract must be signed." (legal: allowed or set by law)
4. sure / secure. "I'm ___ the meeting is on Tuesday." (sure: certain in your mind) "Lock the bikes so they're ___." (secure: safe, firmly fixed)
5. catch / chase. "The dog leapt to ___ the ball in its mouth." (catch: seize) "The dog ran to ___ the ball across the yard." (chase: run after)
6. hospital / hostel / hotel. "We slept in a cheap ___ with bunk beds and a shared kitchen." (hostel) "The ___ had room service and a pool." (hotel) "The ___ admitted three patients overnight." (hospital)
7. chief / chef. "The fire ___ spoke at the assembly." (chief: leader) "The ___ tasted the soup and added salt." (chef: a cook in charge of a kitchen)
8. poison / potion. "The label warned that the cleaner was a ___ if swallowed." (poison) "In the story, the wizard brewed a sleeping ___." (potion) Shared ancestor: Latin potio, "a drink"; poison came through Old French poison.

### Figures: Fossil shelf
1. muscle: Latin musculus, "little mouse"; one explanation: a flexing muscle under the skin looked like a mouse moving.
2. disaster: Italian disastro, from dis- plus astro, "star"; an event blamed on an unlucky star.
3. companion: Late Latin companio, com- "with" plus panis "bread"; someone you share bread with.
4. pedigree: Anglo-French pe de grue, "crane's foot"; the branching mark used in family trees looked like a crane's foot.
5. window: Old Norse vindauga, "wind eye"; an eye-shaped opening the wind came through.
6. nightmare: Old English mare, an evil spirit believed to sit on sleepers' chests; the night spirit, later the bad dream.
7. Myth check, sincere: the story "sine cera, without wax" is popular but not supported; Latin sincerus, "clean, pure, whole".

### Figures: Live shelf (public-domain passages, printed exactly from the editions in Sources)
1. Paradox. Charles Dickens, A Tale of Two Cities (1859): "It was the best of times, it was the worst of times". One reading: "Both can't be true at once, unless the same years were wonderful for some people and terrible for others. The opening warns that the novel will be about a divided age."
2. Paradox. William Wordsworth, "My Heart Leaps Up" (1807): "The Child is father of the Man". One reading: "A child can't father an adult, but the adult grows out of the child. The poem wants the grown man to keep the child's wonder."
3. Paradox. John Donne, Holy Sonnet "Death, be not proud" (1633): "And death shall be no more; Death, thou shalt die." One reading: "Death dying sounds impossible. The speaker's faith in an afterlife turns death's own power against it."
4. Hyperbole. Ralph Waldo Emerson, "Concord Hymn" (1837): "And fired the shot heard round the world." One reading: "No one across the world heard a musket at Concord. The overstatement claims the first battle of the Revolution mattered to everyone."
5. Hyperbole. Shakespeare, Macbeth, 2.2: "Will all great Neptune's ocean wash this blood / Clean from my hand?" One reading: "A little blood can't outlast an ocean. The exaggeration measures Macbeth's guilt, not the stain."
6. Metaphor. Abraham Lincoln, speech at Springfield, Illinois, June 16, 1858: "A house divided against itself cannot stand." One reading: "The nation is a house, slavery the split in it. Lincoln borrowed the figure from the Bible, so his listeners already knew it."

### Unknown words (original sentences)
1. "The tide's inexorable rise swallowed the sandcastle no matter how high we built the wall." Parts: in- "not" + ex- "out" + orare "to plead" + -able. Entry: inexorable, ih-NEK-ser-uh-bul, adjective, "not able to be stopped or changed by pleading; relentless".
2. "After winning, she was magnanimous, thanking the other team and praising their goalie." Parts: magnus "great" + animus "spirit, mind". Entry: magnanimous, mag-NAN-uh-mus, adjective, "generous, especially toward a rival or someone less powerful".
3. "Be circumspect about what you post: look at it from every side first." Parts: circum "around" + specere "to look". Entry: circumspect, SER-kum-spekt, adjective, "careful to consider all circumstances before acting".
4. "The benevolent stranger paid for everyone's bus fare." Parts: bene "well" + volens "wishing". Entry: benevolent, buh-NEV-uh-lunt, adjective, "kind; wanting to do good".
5. "He was incredulous when the coach said practice was canceled for the whole week." Parts: in- "not" + credulus "believing" (from credere "to believe"). Entry: incredulous, in-KREJ-uh-lus, adjective, "unwilling or unable to believe something".
6. "The tenacious vine had climbed the whole fence by August." Parts: tenax "holding fast" (from tenere "to hold"). Entry: tenacious, tuh-NAY-shus, adjective, "holding firmly; persistent".
- Respellings and meanings are checked against Merriam-Webster at build and adjusted to its entry; the etymology line names its source.

## Interactions in detail
- Trees are laid out by the engine's Tree view at real pixel size: the trunk at the bottom center, one branch per road fanned evenly, leaves spaced so tags never overlap (they wrap to a second ring when needed). Pinch or wheel zoom and drag pan; **Fit tree** resets.
- Leaves are buttons in tab order after the panel controls; arrow keys move between leaves on a branch, Enter opens the card.
- Doublets: a blank accepts any of the pair's words; the nuance line shows on every drop; a found pair stays found. Your own sentence saves per pair.
- Figures: on Fossil cards the idea box is optional and One explanation is always available after Crack it open. On Live cards One reading appears after the figure is named and the box has any text; the chip is checked, the box is never graded.
- Unknown word: steps unlock in order; the guess boxes keep each version (context guess, parts guess). The Strategy log records the first step after which the student ticked "fits".
- Storage: localStorage `word-family-tree:v1` (try/catch): found pairs, own sentences, fossil ideas, live-figure notes, guesses, strategy log. **Clear my work** in the panel asks first.
- Sizes: at 680x425 the tree fits with leaf tags at 11 px or more (fewer, larger leaves shown, with "+4 more" on a crowded branch that expands on tap). At 760 and below the panel becomes a bottom sheet. At 375 the tree turns sideways (trunk at the left, branches to the right) and scrolls vertically. No horizontal page scroll.
- Motion off: branches appear at once instead of growing.

## Look
- Accent `--brand #a6d84a` (new-leaf green: header rule, the traced road, Grow, found marks) on the kit `theme-912` base. Trunk and branches drawn in bark `#8a6b4f`; leaf tags `#1c2532` with text in `--ink`. Road colors (always with glyph and language name): Latin `#5aa9ff` ⬢, Greek `#c9a0ff` ✦, Old English `#ffd166` ◆, Old Norse `#5fd39a` ▲, Old French and Anglo-Norman `#ff8a8a` ●, Frankish `#ffb86b` ■, Italian or Spanish `#7fe3ff` ◇, modern French `#f2c6ff` ★.
- Contrast (WCAG 2.1): brand on panel #141b25 10.34:1, on sec-bg 9.80:1; brand-ink #1c1203 on brand 11.03:1; leaf text #e8edf3 on #1c2532 about 13:1; each road color on panel above 6:1 (confirm at build).
- Different from ELA 9-12 neighbors and this group (key-term-tracker is a light page in dark amber; pacing-strip mint; speech-coach cue-light green #5ee07a, dE 31; ad-agency acid green #a3ff19 is brighter and yellower). world-lit-atlas #8ff05a (dE 18) is not a neighbor; virtual-gallery (arts 9-12) #b8e07a is close (dE 18.7) but in another subject.

## Art
None: drawn in code (tree, branches, tags, the crane's-foot mark on the pedigree card). No people.

## Voice
Bank voice `gravel-ranger`, style "Say warmly with a gravelly voice, like an old park ranger reading a tree's rings." Not used by this group or any neighbor (fallacy-field-guide, grade 10, is the other 9-12 ELA user). It moved off science-narrator, which neighbor premise-inspector uses. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.root`. Word cards are read on screen; Read speaks the hint.
- w-grow (how, welcome Grow): "Pick a root at the bottom, then tap Grow. Tap any leaf to see the road it took."
- road (how, first leaf opened): "Tap Show on tree to trace this word's road from the root."
- form (how, first Change the form strip): "The -ceive words came through French. The -cept- words kept the Latin stem."
- ghost (how, first ghost branch shown): "That dashed branch looks related, but comes from a different root."
- w-doublets (how, welcome Doublets): "Each pair shares one ancestor. Drag each word into the sentence it fits."
- found (event, a pair found; stale on the next pair): "Same family, different shades."
- w-fossil (how, welcome Figures): "Each word hides an old picture. Tap Crack it open, then guess why."
- live (how, first Live shelf): "Name the figure with a chip. Then write what it does in the passage."
- myth (event, the sincere card opened; stale on the next card): "A good story, but not a true one."
- w-unknown (how, welcome Unknown word): "Guess the word from the sentence first. Then tap Parts, then Dictionary."

## Family engine
`kit/wordlab.js`, the word-lab family engine. No family doc exists; this spec holds the full description, written so the lower grades can reuse it. Siblings: word-lab (2), root-detective-cards (4), glossary-makers (3-5), context-roots-dictionary (6-8), key-term-tracker (9-12), word-family-tree (12). Pure parts in one marked block, exposed as `__tool.wl`.
- **Morphemes**: `{id, forms:[...], kind:'prefix'|'root'|'suffix', meaning, lang, source}`. `wl.morph(id)`.
- **Word records**: `{word, pos, say, gloss, parts:[morphemeIds], road:[{lang, form, gloss}], root, notes, senses:[{text, source}], related:[{word, kind:'doublet'|'false'|'form'}]}`.
- **Split**: `wl.split(word)` returns `[{text, morph, from, to}]` for highlighting; unknown stretches come back as `{text, morph:null}`.
- **Build**: `wl.build(morphIds)` returns matching word records (beakers in word-lab, card combining in root-detective-cards); `wl.near(morphIds)` suggests one-part-away words.
- **Tree view**: `wl.tree(el, rootId, words, opts)` lays out trunk, road branches and leaves at real pixel size with collision-free tags, zoom, pan, `traceRoad(word)`, ghost branches (`related.kind === 'false'`) and the "+n more" fold; `opts.orient` 'up' or 'right'.
- **Card view**: `wl.card(el, record, layers)` draws a word card whose layers stack (senses, notes, student layers), so a card can grow during a session (key-term-tracker's meaning card).
- **Lookup**: `wl.entry(el, record)` draws a dictionary entry: respelling, part of speech, etymology line from the road, numbered senses, a source line.
- **Strategy log**: `wl.log(word, step)` with steps 'context', 'parts', 'dictionary'; `wl.cracked(word)` returns the first step marked as enough. Used by context-roots-dictionary, key-term-tracker and Unknown word here.
- **Guess and verify**: `wl.guess(word, step, text)` keeps each guess per step; verification is the student's own tick (the engine never grades a meaning).
- **Road key**: `wl.LANGS` with each language's glyph, name and color variable, so every sibling shows roads the same way.
This tool uses: Morphemes, Word records, Split, Tree view (with ghost branches and traceRoad), Card view, Lookup, Strategy log, Guess and verify, Road key. key-term-tracker feeds the engine its term's forms, unfamiliar words with parts and entries, and uses Card view for the growing meaning card and Lookup plus Strategy log for hard words.

## Sources
- Standards: CCSS ELA L.11-12.4 and L.11-12.5, https://www.thecorestandards.org/ELA-Literacy/L/11-12/.
- Live figures: Dickens, A Tale of Two Cities (1859), Project Gutenberg eBook #98; Wordsworth, "My Heart Leaps Up", Poems, in Two Volumes (1807), Project Gutenberg eBook #8905 or the Poetry Foundation's public-domain text; Donne, Holy Sonnet 10, Poems (1633), Project Gutenberg eBook #48688 or another pre-1930 edition; Emerson, "Concord Hymn" (1837), Poems (1847), Project Gutenberg eBook #12843; Shakespeare, Macbeth, Project Gutenberg eBook #1533; Lincoln, "House Divided" speech, June 16, 1858, Abraham Lincoln Online or the Collected Works of Abraham Lincoln (University of Michigan digital edition); the Bible source of the figure, Mark 3:25. Confirm each eBook number and the exact wording at build.
- Etymologies, roads and doublets: Merriam-Webster.com Dictionary, each word's etymology section, https://www.merriam-webster.com/; Online Etymology Dictionary (Douglas Harper), https://www.etymonline.com/ (entries for each leaf, doublet and fossil word, including catch, chase, cattle, chattel, glamour, ward, guard, reward, regard, wary, warn, shirt, skirt, score, curt, pedigree, window, nightmare, sincere). Check every road against both at build.
- Meanings in the Doublets nuance lines, the Unknown word entries and respellings: Merriam-Webster.com Dictionary.
- Context sentences: original, written for Curio Class.

## Done when
- All 9 trees grow with every leaf on the road listed in Content, each road labeled with its glyph and language.
- Show on tree traces the selected word's road from trunk to leaf; the hospes tree shows the dashed hostis ghost branch with its line.
- The Change the form strip lights "ceive" and "cept" in all four rows.
- Every doublet sentence accepts only its listed word and shows the nuance line on each drop; Found counts pairs with both blanks right (8 total).
- Figures: each Fossil card reveals its picture; sincere is labeled Myth check and says the story is not supported. Each Live card accepts only its listed chip and shows One reading after the box has text.
- Tapping the ward/guard glint (not in the gallery) opens the pair card with its nuance line.
- Unknown word steps unlock in order, keep both guesses, and the Strategy log records the step that cracked each word.
- Work survives a reload; Clear my work asks first.
- At 375 the tree turns sideways with readable tags and no horizontal scroll; at 680x425 leaf tags are 11 px or more.
- `__tool.wl` exposes the engine parts listed in Family engine.

## Open questions
None. Settled:
- L.11-12.5a is now taught in context (BASELINE rule 2): a Live shelf of six public-domain passages with hyperbole, paradox and metaphor, named and interpreted, beside the fossil figures.
- When the two references disagree on a road, the leaf stays with "probably" and both sources named; facts stay plain and checkable (rule 5).
- Tree 6 was a mix of unrelated Germanic roots; it is now one root (ward), and the Norse road moved to a new ninth tree (sker-, "cut") so every tree grows from one ancestor.
