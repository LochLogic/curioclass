# Editors in the Margin

## One idea
Three editors write in your margin (one for audience and purpose, one for the rhythm of your sentences, one for hyphens and spelling), and they don't always agree: you accept, reject or rewrite each note with a one-line reason, the page keeps tracked changes in each editor's mark, and a before-and-after read shows which of your decisions actually moved the audience fit, the sentence rhythm and the clean copy, including the ones where saying no was the right call.

## Not like
- draft-versus-draft (ela 6-8, showdown, not specced): the class votes between two finished revisions. Here one student makes every revision decision, note by note, and gives a reason for each.
- personal-essay-studio (ela 11, studio, this group): the student's own essay from a blank page, with questions and no suggested wording. Here the essay is given, the editors suggest wording, and the skill is judging suggestions.
- pacing-strip (ela 9-12, lab, this group): measures a narrative scene's pacing. Here the texts are a letter and an explainer, and sentence rhythm is one of three measures.
- punctuation-power-ups (ela 10, race, this group): fast right-or-wrong marks. Here the copy editor's notes come with a reason and a guide, and the other two editors' notes are judgment calls.
- usage-panel (ela 11, roleplay, spec): debates whether a usage is acceptable. Here the usage questions are settled by a named guide; the debate is about audience and rhythm.

## Who and how
- Grades 9 to 12 ELA. Module: Revising and Editing for Style (Writing).
- Topic line: "revising and editing".
- Driver: students on laptops, alone or in pairs. 25 to 40 minutes per essay.
- Standards: W.9-10.4 (clear and coherent writing suited to task, purpose and audience): the Audience editor's notes and the Audience fit gauge. W.9-10.5 and W.11-12.5 (develop and strengthen writing by revising and editing, focusing on purpose and audience): the whole accept, reject, rewrite loop with reasons, and Before and after. L.11-12.2 (2a hyphenation conventions, 2b spell correctly): the Copy editor and the Clean copy gauge. L.11-12.3 (3a vary syntax for effect, consulting references for guidance; apply an understanding of syntax to the study of complex texts when reading): the Rhythm editor, the Sentence rhythm gauge, and the Rhythm reference card, which the student consults from any Rhythm note and which runs the same gauge on four public-domain sentences.
- Grade setting in the panel: **9-10** opens Essay A first, **11-12** opens Essay B first; both essays are open at either setting.
- tool.json: driver "students", minutes "25-40", modes ["Edit", "Before and after", "Editor's letter"], grades_label "Grades 9-12". Kit starter.

## Screens and modes
Header: title "Editors in the Margin", small line "Three editors. Your call."; essay picker **A: Letter to the school board** / **B: Newsletter explainer**; mode buttons **Edit** (opens first), **Before and after**, **Editor's letter**; Motion, Sound, Read. Panel: `#hint`, the assignment card (task, audience, purpose: Content), a decisions count ("9 of 15 notes answered"), **Start this essay over** (asks Yes / No).

### Edit (opens first)
Focus: the essay page and the open note card beside its span; the page is the biggest, central thing, laid on the painted desk (Art).
- Center: the essay as a typeset page, paragraphs numbered. Right margin: note cards, each tied to its span by a thin leader line. Each editor has a mark and a glyph: Audience ◆ (solid underline), Rhythm ● (wavy underline), Copy ■ (double underline). Card header: the editor's painted emblem (Art), glyph, editor name, note number.
- A note card shows the editor's comment (one or two sentences) and, when the editor proposes wording, the proposal as a tracked change (insertion underlined, deletion struck).
- Buttons on every card: **Accept**, **Reject**, **Rewrite**. Rewrite turns the span into an editable box with the original words in it; **Done** keeps the student's version as a tracked change in the student's own mark (▲, dotted underline).
- A one-line **Why?** box follows every decision. Quick chips fill it and can be edited: "Fits my audience better", "Keeps my meaning", "Clearer", "Changes what I meant", "The guide says so", "I like the rhythm as it is". A decision with an empty Why? shows "Add a reason" on the card; it still counts, but Editor's letter lists it as missing a reason.
- Conflicts: when accepting one note removes or replaces another note's span, that card greys with "This text is gone after note A4" and an **Undo note A4** link.
- **Rhythm reference** (a card in the panel, and a "See the pattern" link on every ● card): four patterns, each with a public-domain example, its sentence-length bars drawn by the same gauge, and one line on its effect (Content). **Try it on a classic** runs the gauge on the example so the student reads a master's syntax the way they read their own.
- **Show changes** toggle: tracked marks on (default) or a clean read of the current text.
- Notes can be answered in any order; **Next note** jumps to the next unanswered card.

### Before and after
Focus: the three gauges over the two columns.
- Two columns, original and current, each with three gauges above it:
  - **Audience fit**: words or phrases from the essay's watch list still present (Content), as a count with each one listed ("Too casual for the board: 'So basically'"), plus the essay's purpose checks as yes/no lines with words.
  - **Sentence rhythm**: a bar for every sentence, its length in words, in order; under it shortest, longest, the spread (standard deviation, one decimal) and how many sentences start with the same word as the one before.
  - **Clean copy**: errors left from the Copy editor's list, by kind (hyphen, spelling).
- **Which edits mattered**: under each gauge, the decisions that moved it, with the change ("A1 accepted: Audience fit, 2 flags fewer"; "V2 rejected: no change"). Decisions that moved nothing are listed at the bottom as "Moved no gauge (that can be fine: some edits are about meaning)".
- **Read both** (button): shows the two versions one paragraph at a time, side by side, for a slow read; nothing is voiced.

### Editor's letter
Focus: the letter, centered on the painted desk.
- A short letter the tool assembles from the decisions: "Dear editors, I accepted 9 of your 15 notes..." then one line per note: the note number, the decision and the student's Why? text. Missing reasons are marked "(reason to add)". Below it, a box for the student's own closing paragraph: "What did you change most, and why?"
- **Copy letter** copies it as plain text. Nothing leaves the page otherwise.

## Content
All essays and notes are original, written for Curio Class. Sentence ids: paragraph.sentence.

### Essay A: Letter to the school board (grade setting 9-10)
- Assignment card: "Task: a letter asking the school board to install water bottle filling stations. Audience: the five members of the board. Purpose: get the request on the March meeting agenda."
- Text:
  P1: "Hey board members! So basically our school needs water bottle filling stations. Right now there are only two old fountains on the second floor. They are slow. They are warm. Students skip them. Most kids just buy bottled water from the vending machine, which is a total ripoff."
  P2: "Filling stations save money and plastic. A station counts every bottle it saves. Ours could show the board exactly how much plastic we keep out of the trash. The district recieved a grant for building upgrades in the goverment budget, so the money may already exist. A two hour install per station is all it takes."
  P3: "Some people say the fountains are fine. They are not. The well known problem with old fountains is that nobody uses them. A highly-rated station would get used."
  P4: "Please put this on the agenda for the March meeting. We would definately be willing to present. Thanks, and see you there!"
- Watch list (Audience fit): "Hey", "So basically", "total ripoff", "kids", "Thanks, and see you there!". Purpose checks: "Asks for a specific action" (yes while P4's first sentence or its rewrite contains "agenda"); "Answers the other side" (yes while P3's first two sentences remain in some form).
- Notes:
  - A1 ◆ on "Hey board members!": "This is a letter to elected officials. Open the way a formal letter does." Proposal: "Dear members of the school board,"
  - A2 ◆ on "So basically": "Cut the filler; start with the request." Proposal: delete "So basically" and capitalize "Our".
  - A3 ◆ on "Most kids just buy bottled water from the vending machine, which is a total ripoff.": "The board may agree, but slang costs you their trust." Proposal: "Most students buy bottled water from the vending machine, which costs them money every day."
  - A4 ◆ on all of P3: "Board members are busy. Cut this paragraph to keep the letter short." Proposal: delete P3. (Judgment call: accepting it turns "Answers the other side" to no; Before and after shows that line.)
  - A5 ◆ on "Thanks, and see you there!": "Close formally." Proposal: "Thank you for your time and consideration."
  - V1 ● on "They are slow. They are warm. Students skip them.": "Three short sentences in a row sound choppy here. Combine them." Proposal: "They are slow and warm, so students skip them."
  - V2 ● on P2.2 and P2.3: "Every sentence in this paragraph starts with its subject. Try opening one with a clause." Proposal: "Because a station counts every bottle it saves, it can show the board exactly how much plastic we keep out of the trash." (replaces P2.2 and P2.3)
  - V3 ● on "They are not.": "Keep this one short. After longer sentences, a three-word sentence lands hard." No proposal; Accept means keep it as is.
  - V4 ● on P4.1 and P4.2: "Join the request and the offer so they read as one move." Proposal: "Please put this on the agenda for the March meeting, where we would be glad to present."
  - C1 ■ "recieved" to "received". Reason line: "i before e, except after c: received."
  - C2 ■ "goverment" to "government".
  - C3 ■ "two hour install" to "two-hour install": "Hyphenate a compound modifier before a noun."
  - C4 ■ "well known problem" to "well-known problem": "Same rule: before the noun, hyphenate."
  - C5 ■ "highly-rated" to "highly rated": "No hyphen after an adverb ending in -ly."
  - C6 ■ "definately" to "definitely" (only while P4.2 is still in the text; if V4 was accepted the card greys).

### Essay B: Newsletter explainer (grade setting 11-12)
- Assignment card: "Task: an explainer for the town newsletter about the Main Street elms. Audience: residents of all ages, most without any tree training. Purpose: explain what is happening, when and why, and what residents can do."
- Text:
  P1: "The arboricultural assessment conducted by the municipal forestry division last spring determined that the eleven elms located along the Main Street corridor are exhibiting symptoms consistent with Dutch elm disease, a vascular wilt caused by a fungus that is transmitted by elm bark beetles, and the division has accordingly recommended removal."
  P2: "Some residents have asked why the trees can't simply be treated, and the answer is that fungicide injections can protect healthy elms but cannot cure trees in which the infection has already occured, which is the case for every tree on the list, according to the assessment."
  P3: "The removal will begin in April and will take about three weeks, and during that time parking on the north side of Main Street will be closed during work hours, and the 100 year old elm in front of the library, which stands on city owned land, will be the last to come down."
  P4: "The division will replant with a mix of drought tolerant species chosen to protect the enviroment, and a public meeting about the replanting will be held at the library in May, where residents can also sign up to water the new trees during their first summer."
- Watch list (Audience fit): "arboricultural", "assessment conducted by", "municipal forestry division", "corridor", "exhibiting symptoms consistent with", "vascular wilt", "accordingly". Purpose checks: "Says when" (yes while "April" remains); "Answers the residents' question" (yes while P2's fungicide sentence remains in some form); "Says what residents can do" (yes while "sign up" remains).
- Notes:
  - A1 ◆ on "The arboricultural assessment conducted by the municipal forestry division last spring determined that": "Most readers don't know these terms. Say who checked the trees, in plain words." Proposal: "Last spring, the town's tree crew found that"
  - A2 ◆ on "exhibiting symptoms consistent with": Proposal: "show signs of".
  - A3 ◆ on "a vascular wilt caused by a fungus that is transmitted by elm bark beetles": "Keep the fact; lose the jargon." Proposal: "a disease caused by a fungus that elm bark beetles carry from tree to tree"
  - A4 ◆ on all of P2: "Residents don't need the science of treatment. Cut it." Proposal: delete P2. (Judgment call: accepting it turns "Answers the residents' question" to no.)
  - A5 ◆ on "the division has accordingly recommended removal": "Lead with the news residents need: what and when." Proposal: move a new first sentence to the top, "The eleven elms on Main Street will come down this April." and change the end of P1 to "so they must be removed."
  - V1 ● on P1: "One 51-word sentence is a lot to hold. Split it." Proposal: end the sentence after "Dutch elm disease" and start "It is a disease caused by..." (works with or without A1 to A3: the proposal is rebuilt on the current text).
  - V2 ● on P2: "Turn the residents' question into a real question. A question gives the reader a breath." Proposal: "Why not treat the trees? Fungicide injections can protect healthy elms, but they cannot cure a tree that is already infected, and every tree on the list is."
  - V3 ● on P3: "Three 'and's chain this sentence. Break it, and give the library elm its own short sentence." Proposal: "The removal will begin in April and take about three weeks. Parking on the north side of Main Street will close during work hours. The 100 year old elm in front of the library goes last." (keeps C2's error if C2 hasn't been answered yet; the Copy note stays live on the new text. The proposal drops "which stands on city owned land", so accepting V3 greys C3 with the "text is gone" line)
  - V4 ● on P4: "Long sentences are fine when they gather steps. Keep this one long, but end the piece with something short." Proposal: add "Bring a watering can." as the last sentence.
  - C1 ■ "occured" to "occurred": "Double the r before -ed when the stress is on the last syllable."
  - C2 ■ "100 year old elm" to "100-year-old elm": "A compound modifier before a noun takes hyphens throughout."
  - C3 ■ "city owned land" to "city-owned land".
  - C4 ■ "drought tolerant species" to "drought-tolerant species".
  - C5 ■ "enviroment" to "environment".
  - C6 ■ on "sign up": "Correct as is: 'sign up' is the verb, 'sign-up' is the noun." No proposal; Accept keeps it.

### Hyphen and spelling notes (Copy editor's guide line, shown on each ■ card)
- "Guide: The Chicago Manual of Style, 18th ed., hyphenation guide; spelling: Merriam-Webster.com." Where guides differ the card says so; none of these notes differ between Chicago, APA and AP.

### Rhythm reference (public-domain examples, printed exactly from the editions in Sources)
- Short after long: "Both parties deprecated war; but one of them would make war rather than let the nation survive; and the other would accept war rather than let it perish. And the war came." Abraham Lincoln, Second Inaugural Address, 1865. Effect: "After a long, balanced sentence, four words land like a door closing."
- A question for a breath: "What, to the American slave, is your 4th of July?" Frederick Douglass, speech at Rochester, New York, July 5, 1852, asking what the holiday meant to people held in slavery. Effect: "A question turns the listener from receiving to answering."
- Hold the main point to the end: "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation." Declaration of Independence, 1776. Effect: "The reader waits through every condition before reaching what is required."
- Build by adding: "I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived." Henry David Thoreau, Walden, 1854. Effect: "Each added phrase pushes the purpose further, and the last one turns it around."
- Under the card: "For more, writers consult books on syntax and style, such as Virginia Tufte's Artful Sentences (named only)."

### Context card for Essay B (About the elms)
- With the painted elm (Art) at the top of the card.
- "Dutch elm disease is caused by a fungus spread by elm bark beetles and by connected roots. It has killed most of the American elms that once lined streets in the United States." (Sources.) The town, the trees and the dates in the essay are made up.

## Interactions in detail
- Spans are character ranges on the current text; every accepted or rewritten change is stored as an operation on the original, so Undo works per note in any order and the gauges recompute from scratch each time.
- A proposal whose span has changed (another note touched it) is rebuilt only where Content says so (B V1, B V3); otherwise the card greys with the "text is gone" line and Undo link.
- Gauges: sentences split on . ! ? followed by a space or the end of the paragraph; words split on spaces; hyphenated words count as one word; numerals count as words. Standard deviation is the population formula over sentence lengths.
- Watch-list matching is case-insensitive on whole words or phrases. Copy errors are counted by checking whether each erroneous string is still present.
- Storage per essay in localStorage `editors-in-the-margin:v1` (try/catch): decisions, rewrites, reasons, the closing paragraph. Start this essay over asks first.
- Nothing plays on its own. Leader lines and gauge bars ease over 200 ms (instant with Motion off); a tap during an ease acts at once and the gauges recompute on that tap.
- Keyboard: Tab moves through note cards in text order (panel controls first), A / R / W choose Accept, Reject, Rewrite on the focused card.
- Sizes: at 1000 px and up, page and margin side by side; at 760 and below, notes become numbered pins in the text that open a card as a bottom sheet. At 680x425 a note card and its span are visible together. At 375 Before and after shows one column at a time with a **Before / After** switch.

## Look
- Accent `--brand #b3261e` (editor's red pencil: header rule, active mode, unanswered-note dots). Own light `:root`, a manuscript on a desk (the painted desk shows only around the page; all text sits on `--paper` or `--panel`): `--paper #faf7f0`, `--panel #fffef8`, `--ink #1e1b18`, `--muted #5b554d`, `--line #e2dacb`, `--btn #b3261e`, `--head-ink #ffffff`, `--focus #1d5fa8`. Essay text in a serif stack at 18 px.
- Editor inks (marks also differ by glyph and underline style): Audience ◆ `#1d5fa8` solid, Rhythm ● `#7a4b9a` wavy, Copy ■ `#b3261e` double, student ▲ `#1e6b3a` dotted.
- Contrast (WCAG 2.1): brand on paper 6.11:1, on panel 6.47:1; white on brand 6.54:1; editor inks on panel (computed 2026-10-29): Audience 6.39:1, Rhythm 6.30:1, Copy 6.47:1, student 6.46:1; ink on paper above 15:1.
- Different from ELA 9-12 neighbors: research-notebook fountain-pen blue, theme-ledger ledger wine, interview-simulator (CTE) brick, usage-panel ink red on dark; this is a light page with a brighter red. Different from this group's accents.

## Art
Five painted images, all local FLUX (`scripts/localart.py`), people: false. The editors stay as emblems and role names, not faces: what they say is the point.
- `desk`: "Top-down view of a warm oak writing desk, a coffee mug, a few paper clips and a fountain pen near the edges, soft morning light, a wide empty middle". 16:9; cutout no; people: false. The backdrop around the essay page and the letter; cover-fit, the page card covers the empty middle.
- Editor emblem kit (3 cutouts). Shared prompt: "single object, three-quarter view, soft studio light, plain light backdrop, painted". Pieces: `ed-audience` a pair of reading glasses resting on a folded letter; `ed-rhythm` a wooden metronome; `ed-copy` a red pencil and a pink rubber eraser side by side. 1:1; cutout yes; people: false. Sizing rule: each fills about 80 percent of its square; 28 px in note card headers, 56 px on the Rhythm reference card and in the Editor's letter salutation line.
- `elm`: "A tall American elm with a wide vase-shaped canopy beside the stone steps of a small-town library, early spring, bare branches just budding, clear sky". 4:3; cutout no; people: false. Top of the About the elms card for Essay B (about 280 px wide). The library has no sign.
Drawn in code: the page, marks and leader lines, tracked changes, note cards, gauges and sentence-length bars.

## Voice
Bank voice `friendly-dad`, style "Say in a relaxed, friendly way, like a kind managing editor." Not used by this group, any neighbor or another spec in this batch; the other 9-12 ELA user, page-to-screen (grade 10 literature), is not a neighbor. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.essay`. Essays and notes are read on screen, not voiced.
- w-edit (how, Edit welcome; stale after the first decision): "Three editors left notes. Tap a note, then Accept, Reject or Rewrite, and say why."
- why (how, first decision; stale once the Why box has text): "Type a reason in the Why box, or tap a chip to start one."
- rhythm-ref (how, first Rhythm reference opened; stale when it closes): "Each pattern shows its sentence bars. Tap Try it on a classic to measure it."
- conflict (how, first greyed note; stale when that note is restored or the card closes): "That note's text is gone because of another change. Tap Undo if you want it back."
- judgment (how, first time a purpose check turns to no; stale when it turns back to yes): "One of your changes removed something your purpose needs. Tap Before and after to see which."
- w-before (how, Before and after welcome; stale on mode change): "Each gauge lists the decisions that moved it. Some good decisions move nothing. Tap Read both for a slow read."
- w-letter (how, Editor's letter welcome; stale once the closing box has text): "Here is every decision with your reason. Write a closing paragraph in the box at the bottom."
- done (event, each time all notes become answered; stale on Undo): "All notes answered. Tap Before and after."

## Family engine
None.

## Sources
- Standards: CCSS ELA W.9-10.4, W.9-10.5, https://www.thecorestandards.org/ELA-Literacy/W/9-10/; W.11-12.5, https://www.thecorestandards.org/ELA-Literacy/W/11-12/; L.11-12.2, L.11-12.3, https://www.thecorestandards.org/ELA-Literacy/L/11-12/.
- Hyphenation of compound modifiers before a noun, no hyphen after -ly adverbs, "sign up" (verb) and "sign-up" (noun): The Chicago Manual of Style, 18th ed. (2024), chapter 7, hyphenation guide; confirm section numbers at build. Merriam-Webster.com Dictionary entries "sign up" and "sign-up".
- Spellings received, government, definitely, occurred, environment: Merriam-Webster.com Dictionary.
- Varying syntax for effect: L.11-12.3a names Virginia Tufte, Artful Sentences: Syntax as Style (Graphics Press, 2006), as an example reference; named only, not quoted. The four pattern names and effect lines are original.
- Lincoln, Second Inaugural Address, March 4, 1865: Library of Congress or the Avalon Project, https://avalon.law.yale.edu/19th_century/lincoln2.asp (check the punctuation of the quoted lines against it at build).
- Frederick Douglass, "What to the Slave Is the Fourth of July?", delivered July 5, 1852, Rochester, New York: text in the 1852 pamphlet as reprinted by the Library of Congress or another public-domain edition; confirm the exact wording ("4th of July") at build.
- Declaration of Independence: National Archives transcription, https://www.archives.gov/founding-docs/declaration-transcript.
- Thoreau, Walden (1854), chapter 2, "Where I Lived, and What I Lived For": Project Gutenberg eBook #205, https://www.gutenberg.org/ebooks/205.
- Dutch elm disease: USDA Forest Service, "Dutch Elm Disease" (Forest Insect and Disease Leaflet or Pest Alert), https://www.fs.usda.gov/ (confirm the exact page at build); fungus spread by elm bark beetles and root grafts; losses of American elms in US cities.
- Essays, notes and the town: original, written for Curio Class.
- Checks run in Python (2026-10-29) with the stated split rules: original Essay A has 19 sentences, lengths 3, 9, 12, 3, 3, 3, 15, 6, 7, 15, 18, 10, 7, 3, 12, 6, 10, 7, 5 (shortest 3, longest 18, spread 4.5, one same-word start: "They are slow." then "They are warm."); Essay B has 4 sentences of 51, 47, 54 and 46 words (spread 3.2, one same-word start), so V1's "51-word sentence" holds and B P3 has three "and"s as V3 says. Clean copy on the originals: A 3 hyphen and 3 spelling errors, B 3 hyphen and 2 spelling. Rhythm reference: Lincoln 28 and 4 words, Douglass 10, Declaration 71, Thoreau 44. The split rule now names the end of a paragraph too, so each paragraph is split on its own.

## Done when
- Focus: at 1366x768 and 680x425 in Edit, the essay page is the largest thing on screen and an open note card is visible beside its span.
- Both essays load with every note tied to the right span; all 15 (A) and 15 (B) notes can be accepted, rejected or rewritten and undone in any order.
- Accepting A4 turns "Answers the other side" to no and lists A4 under Audience fit's purpose line; undoing it turns it back.
- Accepting A V4 greys C6 with the "text is gone" line.
- Gauges recompute exactly: on the original Essay A the Rhythm bars read 3, 9, 12, 3, 3, 3, 15, 6, 7, 15, 18, 10, 7, 3, 12, 6, 10, 7, 5 (spread 4.5), and Clean copy shows 3 hyphen errors (C3, C4, C5) and 3 spelling errors (C1, C2, C6) before any note is accepted; Essay B shows bars 51, 47, 54, 46 and 3 hyphen (C2, C3, C4) and 2 spelling (C1, C5).
- A tap on Accept while a leader line or gauge bar is easing acts at once; no voice line names a control that is hidden or disabled.
- Which edits mattered lists only decisions that changed a gauge value; others appear under "Moved no gauge".
- Editor's letter lists every decision with its reason and marks missing reasons.
- Accepting B V3 greys C3; the Rhythm reference shows four examples whose bars match their word counts (Lincoln: 28 and 4 words; a semicolon never ends a sentence).
- Each note card shows its editor's painted emblem; Essay B's About the elms card shows the painted elm.
- Work survives a reload; Start this essay over asks first.
- At 375 and 760 wide notes open as bottom sheets with no horizontal scroll; at 680x425 a card and its span are visible together.

## Open questions
None. Settled:
- Both deliberately poor notes (A A4, B A4) stay: judging an editor, including saying no, is the skill (BASELINE rule 2). The teacher notes name them.
- The Rhythm reference card was added, with four public-domain examples measured by the same gauge, so L.11-12.3a's "consulting references" and its reading half are taught, not only named (rule 2).
