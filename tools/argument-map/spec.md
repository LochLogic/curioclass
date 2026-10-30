# Argument Map

## One idea
An essay is printed in one order and holds itself up in another: you rebuild it as a tree of what supports what, then pull any claim out and watch which conclusions fall, so you can say which lines carry the weight and whether the author's order makes that weight easy to see.

## Not like
- rhetoric-spotter (ela 9, family sibling): sorts single speech lines by appeal and device. Here no line is judged alone; the subject is how lines lean on each other.
- rhetorical-situation-simulator (ela 11, family sibling): keeps a speech fixed and changes the situation around it. Here the situation is fixed and the structure inside the text is taken apart.
- premise-inspector (ela 11, founding-docs): lays out one document's premises so later speakers can be compared against them. Here there is no comparison between texts; the tree is built by the student, then stress-tested by pulling, and the reading order is the second subject.
- satire-decoder (ela 11): proves what a text really means beneath what it says. Here meaning is plain; the question is which parts hold the rest up.
- argument-builder-pro (ela 9, evidence family): builds the student's own outline. Here the argument belongs to Madison or Thoreau and is analyzed, not written.
- argument-x-ray (ela 6, evidence family, not built): colors claims, reasons and evidence in an op-ed. Here roles are not colored by the tool; the student draws the links and the pull test checks them.

## Who and how
- Grade 12 ELA. Module: Analyzing Complex Explanations (Reading Informational Text), "Evaluate structure and effectiveness of an author's argument".
- Driver: students on laptops, alone or in pairs. A teacher can project Build for the first essay and take suggestions. 30 to 45 minutes (one essay is a full period's work; the second is for a later day or a fast pair).
- Standards: RI.11-12.5 (analyze and evaluate the effectiveness of the structure an author uses in an argument, including whether it makes points clear and convincing): Build, Pull and Reorder. RI.11-12.6 (point of view and purpose in a text whose rhetoric is particularly effective; how style and content add to its power): the Quotable lines layer in Pull asks whether the most famous lines carry weight or decorate.
- tool.json: driver "students", minutes "30-45", modes ["Build", "Pull", "Reorder"], grades_label "Grade 12". Kit starter plus `kit:rhetoric` and `kit:theme-912` (overridden by the own `:root` below).

## Screens and modes
Header: title "Argument Map", small line "What holds up what."; essay picker **Federalist No. 51** / **Civil Disobedience**; mode buttons **Build** (opens first), **Pull**, **Reorder**; Motion, Sound, Read. Layout: reader column on the left (about 38 percent), map canvas in the middle, panel on the right with `#hint`. At 760 wide and below the reader becomes a drawer opened by **Text** (book icon) and the panel drops under the map.

### Build (opens first)
- Focus: the map canvas, center and the largest thing on screen; the reader column is narrower beside it and the tray runs along the map's bottom edge.
- Reader: the essay's paragraphs, numbered (¶1 to ¶9 for Federalist No. 51; the edition's own numbers for the Thoreau excerpt). The twelve unit sentences from Content are boxed with their ids (F1, T4) in a margin tab; everything else is plain text to read.
- Map: the root card sits at the top (its text in Content). Unit cards wait in a tray along the bottom of the map in reading order.
- The student drags a card onto a card already on the map (or taps a card, then taps the target; keyboard: Enter on a card, arrows to a target, Enter). A link-type chooser opens at the drop: **Supports**, **Assumes** (an unstated or stated premise the claim needs), **Answers an objection** and **Concedes** (a limit the author admits). The link is drawn with its type's line style and its word label.
- Each placed card has **Move**, **Change link** and **Back to tray**. A card can have only one parent.
- **Compare with one reading** (enabled once every card is placed, or by a second press of **Show it now**): the tool's own map fades in behind the student's as a ghost. Each card where the two differ shows a small "Another reading" tag; tapping it shows the tool's parent, link type and a one-sentence reason from Content. Cards whose parent is on the "also fair" list in Content show "Also fair" instead. No score is shown; the panel counts "Same as one reading: 9 of 12, also fair: 2, different: 1".
- **Use my map** / **Use the reading's map** decides which map Pull and Reorder use (default: the student's, once complete).

### Pull
- Focus: the map at full size; the panel readout sits beside it, so a pull and what falls are seen together.
- The chosen map, full size. Tap any card, then **Pull** (or press P). The card lifts off; links from it go grey.
- What responds (engine Map rules): a card stays up if all its Assumes children stand and, if it has any Supports children, at least one of them stands (a card no one ever argued for is a stated premise and stands on its own). Cards that fall turn to a dashed outline with the word "Falls" and drop 12 px (no drop with Motion off). An Answers-an-objection link pulled leaves its parent standing but flags it "Objection open". Concedes links never hold anything up; pulling one flags "Limit removed: the claim now says more than the author did".
- Panel readout: "Falls with it: F4, F1" and "Root: still standing / falls"; the card is tagged **Load-bearing** when anything else falls, else **Not load-bearing**.
- **Put back** restores the last pull; **Put all back** restores everything. Only one card is pulled at a time.
- **Quotable lines** toggle: the essay's four most quoted lines (Content) get a quotation-mark badge. For each, the panel asks "Weight or decoration?" with buttons **Carries weight** / **Decoration** / **Not sure yet**; after the student answers, a pull of that card shows its real effect beside the answer. The student's one-line note per quotable line goes in a private box ("Why put this line here?").
- **Map notes**: a private text box per essay (localStorage, **Clear notes** button).

### Reorder
- Focus: the tile stack, center, with the two meters right beside it at the same height.
- The essay's paragraphs as a vertical stack of tiles (paragraph number plus the first eight words plus the unit ids it holds). The student drags tiles into any order (keyboard: select, then Up and Down).
- Two meters update on every move, computed from the chosen map: **Leaps ahead** (links where a claim appears before the card that supports it: the reader must trust and wait) and **Build-ups** (support appears before its claim). Beside each, the author's real order's count in grey for comparison. Links inside one paragraph count in neither meter (the panel lists them as "same paragraph"), and Federalist No. 51's printed heading is a title that always comes first, so links to it are left out too.
- **Logic first** button: reorders tiles so as few links as possible leap ahead (every support before its claim wherever the paragraphs allow; ties keep the author's order). **Author's order** puts them back. In Federalist No. 51, ¶6 and ¶8 lean on each other (F11 in ¶6 sits under F12 in ¶8, which supports F10 in ¶6), so one leap always stays; the panel says "One leap stays: ¶6 and ¶8 lean on each other." (shown under the meters).
- A **Why this order?** note box (private) and three prompts on screen, one at a time with **Next prompt**: "Where does the main claim first appear, and what has the reader been given by then?", "Which objection is answered earliest, and why there?", "Read your logic-first order aloud. Is it clearer, or flatter?"

## Content
Exact texts from the named editions (Sources). Source em dashes are shown as "--" (see Open questions). Each unit: id, paragraph, text, the reading's parent and link, and the reason shown under "Another reading".

### Federalist No. 51 (Avalon Project text, from the New York Packet, February 8, 1788; signed Publius; Avalon names the author as "Hamilton or Madison")
Root R: the essay's printed heading, "The Structure of the Government Must Furnish the Proper Checks and Balances Between the Different Departments" (labelled "Heading").
- F1 ¶1 "the defect must be supplied, by so contriving the interior structure of the government as that its several constituent parts may, by their mutual relations, be the means of keeping each other in their proper places." Supports R. Reason: the first paragraph restates the heading as a design rule; everything after explains how.
- F2 ¶2 "each department should have a will of its own" Supports F1. Also fair: supports R. Reason: separate wills are the first condition for parts that can check each other.
- F3 ¶2 "Some deviations, therefore, from the principle must be admitted." Concedes, on F2. Reason: judges are not chosen by the people; Madison admits his rule bends.
- F4 ¶3 "the great security against a gradual concentration of the several powers in the same department, consists in giving to those who administer each department the necessary constitutional means and personal motives to resist encroachments of the others." Supports F1. Reason: this is the "how" of keeping parts in place.
- F5 ¶3 "Ambition must be made to counteract ambition." Supports F4. Also fair: supports F1. Reason: it compresses F4 into a rule about motives.
- F6 ¶3 "If men were angels, no government would be necessary." Assumes, under F7. Reason: F7 only follows if people, rulers included, are not angels; Madison states the premise as a conditional and never argues for it.
- F7 ¶3 "you must first enable the government to control the governed; and in the next place oblige it to control itself." Supports F1. Reason: a government that must control itself needs the inner checks F1 describes.
- F8 ¶4 "A dependence on the people is, no doubt, the primary control on the government; but experience has taught mankind the necessity of auxiliary precautions." Answers an objection, on F1. Reason: it meets "elections are enough" before a reader can raise it.
- F9 ¶4 "In republican government, the legislative authority necessarily predominates. The remedy for this inconveniency is to divide the legislature into different branches" Supports F4. Reason: one application of the rule, to the strongest branch.
- F10 ¶6 "Hence a double security arises to the rights of the people." Supports R. Reason: a second, separate branch: power split between state and national governments as well as among departments.
- F11 ¶6 "If a majority be united by a common interest, the rights of the minority will be insecure." Assumes, under F12. Reason: the extended-republic argument only matters if majorities can be a danger.
- F12 ¶8 "It consists in the one case in the multiplicity of interests, and in the other in the multiplicity of sects." Supports F10. Also fair: supports R. Reason: a large republic with many interests protects minorities.
- Quotable lines: F5, F6, F7, F10.
- Reading's pull results to check: pull F6, then F7 falls (F1 still stands on F2 and F4); pull F4, then F5 and F9 lose their parent and go back unattached ("Floating") while F1 stands on F2 and F7; pull F11, then F12 falls, F10 falls, R stands on F1. Pull F8: F1 stands, "Objection open".
- Context card (shown once, from the reader's **Context** button): "Who is 'the people' here? The Constitution let each state decide who could vote (Article I, Section 2), and it counted enslaved people as three fifths of a person for representation while giving them none of the rights this essay protects (Article I, Section 2). Keep that in mind when Madison writes 'the rights of the people.'"

### Civil Disobedience (Thoreau; Project Gutenberg #71, "On the Duty of Civil Disobedience", the text of the 1866 collection; first printed 1849 as "Resistance to Civil Government")
Root R: T7b below. The reader shows eight of the essay's 51 paragraphs in full, keeping the edition's numbers (¶1, ¶3, ¶4, ¶9, ¶20, ¶22, ¶23, ¶26); each gap is marked "[paragraphs skipped]" with a line naming the full edition. Reading order of the units: T1, T2, T3, T4, T12, T5, T6, T8, T9, T7, T7b, T10, T11.
- T1 ¶1 "I heartily accept the motto,--'That government is best which governs least;'" Concedes, on R. Also fair: supports T11. Reason: an opening agreement that he then narrows.
- T2 ¶3 "But, to speak practically and as a citizen, unlike those who call themselves no-government men, I ask for, not at once no government, but at once a better government." Answers an objection, on R. Reason: it heads off "so you want no government at all".
- T3 ¶4 "After all, the practical reason why, when the power is once in the hands of the people, a majority are permitted, and for a long period continue, to rule, is not because they are most likely to be in the right, nor because this seems fairest to the minority, but because they are physically the strongest." Answers an objection, on T5. Reason: it meets "the majority decides what is right".
- T4 ¶4 "Must the citizen ever for a moment, or in the least degree, resign his conscience to the legislator?" Supports T5. Reason: a question that expects the answer "no".
- T5 ¶4 "The only obligation which I have a right to assume, is to do at any time what I think right." Supports R. Reason: the core premise: conscience, not law, sets duty.
- T6 ¶4 "Law never made men a whit more just; and, by means of their respect for it, even the well-disposed are daily made the agents of injustice." Supports R. Reason: obeying unjust law makes good people into agents of injustice.
- T7 ¶22 "If the injustice is part of the necessary friction of the machine of government, let it go, let it go" Concedes, on R. Reason: not every injustice calls for breaking the law.
- T7b (root) ¶22 "but if it is of such a nature that it requires you to be the agent of injustice to another, then, I say, break the law."
- T8 ¶9 "I cannot for an instant recognize that political organization as my government which is the slave's government also." Supports T6. Reason: slavery is his case of law that makes citizens agents of injustice.
- T9 ¶20 "Unjust laws exist: shall we be content to obey them, or shall we endeavor to amend them, and obey them until we have succeeded, or shall we transgress them at once?" Supports R. Also fair: concedes on R. Reason: it sets out the three choices the root answers.
- T10 ¶23 "As for adopting the ways which the State has provided for remedying the evil, I know not of such ways. They take too much time, and a man's life will be gone." Answers an objection, on R. Reason: it meets "use the legal ways to change the law".
- T11 ¶26 "Under a government which imprisons any unjustly, the true place for a just man is also a prison." Supports R. Also fair: supports T6. Reason: where breaking the law leads, and why he accepts it.
- T12 ¶4 "I think that we should be men first, and subjects afterward." Supports T5. Reason: the same premise as a slogan.
- Quotable lines: T7b, T11, T12, T1.
- Reading's pull results to check: pull T5, then T3, T4 and T12 float, R still stands on T6, T9 and T11; pull T8, then T6 falls (its only support is gone) and R stands on T5, T9 and T11; pull T10, R stands, "Objection open".
- Context card: "Thoreau spent one night in the Concord jail in 1846 for refusing to pay his poll tax, in protest against slavery and the Mexican-American War. He says in the essay he had paid no poll tax for six years."

## Interactions in detail
- Moving a card that has children moves its whole branch. **Back to tray** returns the branch's cards to the tray too, with a one-line note "3 cards went back with it".
- Loops are refused: dropping a card on its own descendant shakes the target (no shake with Motion off) and says "That would make the claim hold itself up."
- The root cannot be pulled or moved. A floating card (parent pulled) is drawn at the map's edge with "Floating" until **Put back**.
- Pull uses the engine's `rh.map.pull(id)` only; a branch that falls is recomputed from scratch each time, so the order of pulls never matters.
- Compare is a view: it never changes the student's map. Swapping essays keeps each essay's map, notes and answers (saved per essay in localStorage `argument-map:v1`, in try/catch; **Start over** per essay clears the map, **Clear notes** clears notes).
- Reorder meters: a link counts once; Concedes and Answers links count by where the objection or limit sits against its parent. The author's counts are computed from the map in use, never hard-coded. With the reading's map: Federalist No. 51 in the author's order has 6 leaps ahead, 1 build-up and 3 same-paragraph links (it states its design rule in ¶1); Logic first brings it to 1 leap, 6 build-ups. Civil Disobedience in the author's order has 3 leaps, 5 build-ups and 4 same-paragraph links (its root arrives in ¶22 after most of its support); Logic first gives 0 leaps, 8 build-ups.
- Nothing waits on an animation: a tap during a card's 12 px drop, a shake or a tile slide acts at once.
- Sizes: map canvas scales with `Curio.fit`; at 375 wide the map shows one branch at a time with **Branch** arrows, and drag becomes tap-to-place. No horizontal page scroll at any listed size.

## Look
- Own `:root`, a drafting blueprint: `--paper #0b2238` with a faint 24 px grid, `--panel #0f2a45`, `--ink #e6f6ff`, `--muted #9fc0d8`, `--line #23476a`, accent `--brand #19ffff` (cyan draft line: header rule, selected card ring, Pull, link lines in the reading's ghost), `--btn #133658`, `--btn-line #4f86b5`, `--head-ink #e6f6ff`, `--focus #ffd166`. Brand text on brand: `#04222e`.
- Link styles, always with their word: Supports solid 3 px with an arrowhead; Assumes double line with the word "assumes"; Answers an objection dashed with a "?" turned to "!" end mark; Concedes dotted with a small bracket. Falls: dashed card outline plus the word "Falls" in `--warn #ffb8a8`.
- Cards: white-on-blueprint drafting style, the unit id in a corner tab, monospace ids.
- Neighbors: satire-decoder oxblood (dark), premise-inspector citron (dark), rhetorical-situation-simulator split-flap cream (dark), rhetoric-spotter electric blue (light). Nearest catalog accent is dice-in-the-chatbot (dE 19.1).
- Contrast (WCAG 2.1): ink on paper 14.61:1, on panel 13.21:1; muted 8.46:1 and 7.66:1; brand on paper 12.91:1, on panel 11.68:1; brand-ink on brand 13.18:1; focus on paper 11.20:1, on panel 10.13:1; warn on panel 8.82:1. All pass AA.

## Art
none: drawn in code. The whole tool is a diagram: the map's cards, link lines, grid, tiles, meters and preview.svg (three cards on a blueprint grid, one dashed "Falls") are drafting marks, and the texts are read as text. No people, no photos.

## Voice
Bank voice `clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient debate coach at a whiteboard." Used by no family sibling, no neighbor `neighbors.py` lists, and no other spec in batch R10. `Curio.voice`, `scope: () => state.mode + state.essay`. Essay text is never read aloud by the voice (Read speaks the hint); the student reads.
- w-build (how, Build entered; stale once a card is placed): "Drag a card onto the claim it holds up, or tap the card and then the claim. Then choose how it holds it up."
- type (how, first link chooser; stale once a type is picked): "Supports means it gives a reason. Assumes means the claim needs it to be true. Tap one."
- compare (how, first time Compare is enabled; stale once Compare is tapped): "Every card is placed. Tap Compare with one reading to see another map."
- w-pull (how, Pull entered; stale after the first pull): "Tap a card, then tap Pull. Watch what falls with it."
- falls (event, each pull that drops something; stale on Put back or mode change): "That card was load-bearing."
- stands (event, each pull that drops nothing; stale on Put back or mode change): "Everything else still stands."
- quotable (how, first time Quotable lines is on; stale once an answer is tapped): "Before you pull a famous line, guess. Tap Carries weight, Decoration or Not sure yet."
- w-reorder (how, Reorder entered; stale after the first move): "Drag a paragraph tile up or down. Watch the two meters."
- logic (how, first time Leaps ahead reaches its lowest possible count for the essay; stale on the next move): "Every reason now comes as early as it can. Read it. Is it better?"
- loop (event, each refused drop; stale on the next drop): "That would make the claim hold itself up."

## Family engine
`kit/rhetoric.js` (the rhetoric family: rhetoric-spotter, grade 9; rhetorical-situation-simulator, grade 11; argument-map, grade 12). No family doc exists; this spec holds the full description and the siblings say what they feed it. Pure parts in one marked block, exposed as `__tool.rh`.
- **Passage**: `{id, title, speaker, date, place, edition, paras:[{n, units:[{id, text, start, end}]}], context:[{id, title, text}]}`. Text is stored exactly as in the edition; units are character ranges inside paragraphs, so the plain reading text and the marked units never drift. `rh.check(passage)` confirms each unit's text equals its range (console error otherwise).
- **Marks**: highlight layers drawn over units or word spans: `rh.mark(target, layer)`, where a layer has `{id, label, glyph, style: 'box'|'underline'|'bracket'|'tint'}`. Every layer shows a glyph or word as well as color.
- **Tagger**: `rh.tagger({bins, multi, key})` sorts units into bins (a unit may take up to `multi` bins). The key gives one reading per unit `{bins, also:[...], reason, cue:[[start,end]]}`. `rh.compare(answer, key)` returns `same | also | different` per unit with the reason; it never returns "wrong". `rh.cueOverlap(picked, cue)` scores the words a student tapped as "doing the work" against the cue spans (share of cue words picked).
- **Player**: `rh.play(passage, {from, rate, onUnit})` steps through units, lighting each and handing its text to `Curio.say` (a recorded clip if present, else the browser voice); Pause, Step and Stop; with Sound off it paces by `est`. Resolves on the last unit.
- **Map**: nodes `{id, unit|text}` and links `{from, to, type}` with types `supports`, `assumes`, `answers`, `concedes`. `rh.map.attach(from, to, type)` refuses loops; `rh.map.pull(id)` returns `{falls:[ids], floating:[ids], open:[ids], limits:[ids], root: 'stands'|'falls'}` by the rule: a node stands if every `assumes` child stands and (it has no `supports` children, or any `supports` child stands); `answers` and `concedes` never hold anything up. `rh.map.loadBearing()` lists nodes whose pull drops anything.
- **Order**: `rh.order(map, paragraphOrder)` returns `{leaps, buildUps, links:[{from,to,kind}]}`; `rh.order.logicFirst(map)` returns a topological paragraph order (ties keep the author's order).
- **Situation tags** (used by rhetorical-situation-simulator): a unit may carry `depends:[tag]`; the engine only stores and returns them.
This tool uses: Passage (two essays above), Marks (unit boxes, Quotable layer), Map, Order. Not Tagger or Player.

## Sources
- Federalist No. 51, text and heading: Avalon Project, Yale Law School, https://avalon.law.yale.edu/18th_century/fed51.asp (from the New York Packet, February 8, 1788; "Hamilton or Madison").
- Thoreau, "On the Duty of Civil Disobedience", Project Gutenberg eBook #71, https://www.gutenberg.org/ebooks/71 (jail for one night and six years without paying the poll tax: from the essay itself).
- First printing 1849 as "Resistance to Civil Government" in Elizabeth Peabody's Aesthetic Papers; retitled "Civil Disobedience" in the 1866 collection; protest against slavery and the Mexican-American War (1846 to 1848): Wikipedia, "Civil Disobedience (Thoreau)", checked 2026-10-27; confirm against the Walden Woods Project or the Thoreau Society at build.
- Voting left to the states and the three-fifths clause: Constitution of the United States, Article I, Section 2, National Archives transcript, https://www.archives.gov/founding-docs/constitution-transcript.
- Checks run 2026-10-29 (Python, the engine's pull rule and the meter rule on the reading's maps): pull F6 drops F7 only; pull F4 floats F5 and F9, F1 stands; pull F11 drops F12 and F10, root stands; pull F8 drops nothing, "Objection open" on F1; pull T5 floats T3, T4 and T12 (Content had left out T3), root stands; pull T8 drops T6; pull T10 drops nothing, "Objection open" on the root. Load-bearing cards: F6, F11, F12 and T8. Reorder: author's order Federalist 6 leaps, 1 build-up, 3 same-paragraph; Thoreau 3, 5, 4. Every paragraph order was tried: Federalist's best is 1 leap (the ¶6 and ¶8 links point both ways, so the old "Logic first gives 0" was impossible there); Thoreau's best is 0.
- Argument-map link types (supports, linked premise, objection, rebuttal): the standard argument-mapping vocabulary; the tool's own wording.

## Done when
- Every unit's text matches its edition exactly (`rh.check` logs nothing), with em dashes shown as decided.
- A full Federalist map built to match the reading gives "Same as one reading: 12 of 12"; moving F5 under F1 shows "Also fair", moving F11 under F1 shows "Another reading" with its reason.
- Pulling F6 in the reading's map drops F7 and only F7; pulling F11 drops F12 and F10, the root stands; pulling F8 flags "Objection open" and drops nothing.
- Dropping F1 onto F5 when F5 sits under F1 is refused with the loop line.
- Reorder: Logic first gives Leaps ahead 0 on Civil Disobedience and 1 on Federalist No. 51 with the "One leap stays" note; Author's order restores 6 and 3; same-paragraph links count in neither meter.
- Focus: at 1366x768 and 680x425 the map is the largest thing on screen in Build and Pull, and the tile stack with its meters in Reorder.
- A tap on another card while a falling card drops, or a tile drag during a slide, acts at once; Pull T5 shows T3, T4 and T12 floating.
- Notes and answers survive a reload and are gone after Clear notes; nothing leaves the page.
- Quotable lines: answering before a pull, then pulling, shows the answer and the effect side by side.
- At 375 wide the map works by tap with branch arrows and there is no horizontal page scroll; Build's main controls are visible without scrolling at 680x425.

## Open questions
- Federalist No. 51's author: the tool says "Publius (Avalon lists Hamilton or Madison)". Name Madison, as most textbooks do, or keep the source's wording?
- The Thoreau excerpt skips most of the essay. Is an eight-paragraph excerpt with "[paragraphs skipped]" markers fine, or should the full essay be readable in the drawer? (The question said twelve paragraphs; Content lists eight.)
