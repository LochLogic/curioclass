# Catalog review tables: pilot-ela-6

23 tools read (ela, grades 6, 6-8). Built by scripts/catalog_compute.py from docs/agents/catalog/rows/.

## 1. Coverage, standard by standard

A standard is covered when at least one tool teaches it (depth `taught`). `practiced` assumes it was taught elsewhere; `touched` can be skipped; `claimed` has no matching student action.

| Standard | Taught by | Practiced | Touched or claimed | Status |
|---|---|---|---|---|
| RL.6.1 | theme-evidence-ladder | - | - | ok |
| RL.6.2 | summary-squeeze, theme-evidence-ladder | - | - | ok |
| RL.6.3 | plot-rollercoaster | - | - | ok |
| RL.6.4 | word-thermometer | - | - | ok |
| RL.6.5 | plot-rollercoaster | - | - | ok |
| RL.6.6 | perspective-camera | - | - | ok |
| RL.6.7 | - | page-audio-screen | - | practice only |
| RL.6.9 | - | theme-evidence-ladder | - | practice only |
| RL.6.10 | - | climbing-reads | - | practice only |
| RI.6.1 | - | claim-quote-comment | - | practice only |
| RI.6.2 | summary-squeeze | - | - | ok |
| RI.6.3 | memoir-and-biography | - | - | ok |
| RI.6.4 | word-thermometer | - | - | ok |
| RI.6.5 | explainer-sections | - | - | ok |
| RI.6.6 | memoir-and-biography | - | - | ok |
| RI.6.7 | page-audio-screen | - | - | ok |
| RI.6.8 | argument-x-ray | - | - | ok |
| RI.6.9 | memoir-and-biography | - | - | ok |
| RI.6.10 | - | climbing-reads | - | practice only |
| W.6.1 | debate-prep-desk (a, b) | - | - | ok |
| W.6.2 | explainer-sections | - | - | ok |
| W.6.3 | - | blizzard-scenes | - | practice only |
| W.6.4 | draft-versus-draft | - | - | ok |
| W.6.5 | draft-versus-draft | - | - | ok |
| W.6.6 | - | linked-feature | - | practice only |
| W.6.7 | - | source-sorter | - | practice only |
| W.6.8 | source-sorter | - | - | ok |
| W.6.9 | claim-quote-comment | - | - | ok |
| W.6.10 | - | - | linked-feature (touched) | thin |
| SL.6.1 | book-group-table (a, b, c, d) | - | - | ok |
| SL.6.2 | podcast-listening-club | - | - | ok |
| SL.6.3 | podcast-listening-club | - | - | ok |
| SL.6.4 | docent-tour-talk | - | - | ok |
| SL.6.5 | docent-tour-talk | - | - | ok |
| SL.6.6 | docent-tour-talk | - | - | ok |
| L.6.1 | sentence-remixer (a, b, c, d, e) | - | - | ok |
| L.6.2 | pause-and-break (a), tricky-word-lab (b) | - | - | ok |
| L.6.3 | sentence-remixer (a, b) | - | - | ok |
| L.6.4 | context-roots-dictionary (a, c, d) | - | context-roots-dictionary (touched) | ok |
| L.6.5 | word-thermometer (a, c) | word-thermometer (b) | - | ok |
| L.6.6 | context-roots-dictionary | - | - | ok |

Count: ok 32, practice only 8, thin 1.

Codes named by these tools from outside the grade: D3.4.6-8 (1), D4.1.6-8 (1), L.7.2 (2), L.7.3 (1), L.7.4 (4), L.7.6 (1), L.8.2 (3), L.8.4 (4), L.8.6 (1), RI.7.1 (1), RI.7.10 (1), RI.7.3 (1), RI.7.5 (1), RI.7.7 (1), RI.8.1 (1), RI.8.10 (1), RI.8.3 (1), RI.8.6 (1), RI.8.7 (1), RL.7.1 (1), RL.7.10 (1), RL.7.2 (1), RL.7.6 (1), RL.7.7 (1), RL.8.1 (1), RL.8.10 (1), RL.8.2 (1), RL.8.5 (1), RL.8.7 (1), SL.7.1 (1), SL.7.2 (1), SL.7.3 (1), SL.7.4 (1), SL.7.5 (1), SL.7.6 (1), SL.8.1 (1), SL.8.3 (1), SL.8.6 (1), W.7.10 (1), W.7.2 (1), W.7.3 (1), W.7.4 (1), W.7.5 (1), W.7.6 (1), W.7.9 (1), W.8.10 (1), W.8.2 (1), W.8.3 (1), W.8.4 (1), W.8.5 (1), W.8.6 (1), W.8.9 (1).

## 2. Module codes its own tool does not teach

| Tool | Module codes | Not taught or practiced (from the row) | Claimed or only touched |
|---|---|---|---|
| debate-prep-desk | W.6.1, D3.4.6-8, D4.1.6-8 | W.6.1c, W.6.1d, W.6.1e | - |
| page-audio-screen | RL.6.7, RI.6.7, RL.7.7, RI.7.7, RL.8.7, RI.8.7 | - | RI.8.7 (touched) |
| context-roots-dictionary | L.6.6, L.7.4, L.7.6, L.8.4, L.8.6, L.6.4 | - | L.6.4b (touched), L.7.4b (touched), L.8.4b (touched) |
| pause-and-break | L.6.2, L.7.2, L.8.2 | L.6.2b, L.7.2b, L.8.2c | - |
| tricky-word-lab | L.6.2, L.7.2, L.8.2 | L.6.2a, L.7.2a, L.8.2a, L.8.2b | - |
| explainer-sections | W.6.2, RI.6.5, RI.7.5, W.7.2, W.8.2 | W.6.2d, W.6.2e, W.7.2d, W.7.2e, W.8.2d, W.8.2e | - |
| linked-feature | W.6.6, W.7.6, W.8.6, W.6.10, W.7.10, W.8.10 | - | W.6.10 (touched), W.7.10 (touched), W.8.10 (touched) |

## 3. Clash rule (two or more of skill key, action, setting group match, same band)

| Band | Tool A | Tool B | Matched | Shared standards |
|---|---|---|---|---|
| - | none | | | |

Rows with one match are listed only when the two tools also teach or practice the same standard.

## 4. Kinds of work

Each tool splits its time across understanding, fluency and application (0 to 3 each).

| Tool | Understanding | Fluency | Application | Use | Minutes |
|---|---|---|---|---|---|
| plot-rollercoaster | 2 | 0 | 1 | lesson | 30 |
| perspective-camera | 2 | 0 | 2 | lesson | 30 |
| summary-squeeze | 2 | 1 | 1 | lesson | 25 |
| argument-x-ray | 2 | 1 | 1 | lesson | 25 |
| debate-prep-desk | 2 | 0 | 3 | lesson | 30 |
| source-sorter | 1 | 1 | 2 | lesson | 30 |
| book-group-table | 1 | 0 | 2 | lesson | 30 |
| sentence-remixer | 1 | 2 | 1 | station | 25 |
| word-thermometer | 2 | 0 | 2 | lesson | 25 |
| draft-versus-draft | 2 | 1 | 2 | lesson | 32 |
| theme-evidence-ladder | 2 | 0 | 2 | lesson | 30 |
| claim-quote-comment | 1 | 1 | 2 | station | 25 |
| page-audio-screen | 2 | 0 | 2 | lesson | 35 |
| podcast-listening-club | 2 | 1 | 1 | lesson | 30 |
| docent-tour-talk | 1 | 2 | 2 | lesson | 38 |
| context-roots-dictionary | 2 | 1 | 2 | station | 20 |
| pause-and-break | 1 | 2 | 1 | station | 20 |
| tricky-word-lab | 2 | 2 | 0 | ongoing | 15 |
| explainer-sections | 2 | 0 | 2 | lesson | 38 |
| blizzard-scenes | 2 | 0 | 2 | lesson | 43 |
| memoir-and-biography | 3 | 0 | 1 | lesson | 35 |
| linked-feature | 1 | 1 | 2 | ongoing | 50 |
| climbing-reads | 1 | 2 | 1 | ongoing | 30 |

Share of all points: understanding 41%, fluency 19%, application 39%.

## 5. Value table

Depth = best depth on any code. Sole = standards only this tool teaches. Sorted so the weakest case for a tool comes first: little taught, paper could do it, costly to build. A sort order for the judge, not a verdict.

| Tool | Stage | Depth | Sole teacher of | Paper could do it | Screen adds | Cost |
|---|---|---|---|---|---|---|
| climbing-reads | spec | practiced | - | partial | Supports clip off one by one and a range map shows kinds read and clips used, with real texts read aloud on tap. | new-engine |
| pause-and-break | spec | taught | - | partial | The reading voice honors each mark and two waveforms show whether the pauses line up, which paper cannot play. | new-engine |
| linked-feature | spec | taught | W.7.6 | partial | Page counter, link picker, auto built sources list and rule based editor comments, none of which paper can do. | super |
| perspective-camera | spec | taught | RL.6.6 | partial | One scene rewrites live for each narrator while a can-know panel lights what each can reach, which would take four separate printed passages. | new-engine |
| summary-squeeze | spec | taught | RI.6.2 | partial | The gauge lights key details live as the student cuts words and flags opinion words as they type. | new-engine |
| book-group-table | spec | taught | SL.6.1 | partial | Classmates answer according to the move chosen and meters show the talk deepening or stalling, which a printed sheet cannot simulate. | new-engine |
| draft-versus-draft | spec | taught | L.7.3, W.6.4, W.6.5, W.7.4, W.7.5, W.8.4, W.8.5 | partial | The reader faces react live to the student's own cuts, adds, moves and rewords, which a sheet cannot show. | super |
| tricky-word-lab | spec | taught | - | partial | Lights the proving letters in two related words and brings missed words back on a 1, 3 and 7 day queue. | sibling |
| plot-rollercoaster | spec | taught | RL.6.3, RL.6.5 | partial | The track collapses where a pulled scene held something up, and the ride shows the character's face changing, which a sheet cannot animate. | new-engine |
| argument-x-ray | spec | taught | RI.6.8 | partial | The scan finds unsupported reasons and misfit links at once and shows them as cracks in a skeleton. | sibling |
| source-sorter | spec | taught | W.6.8 | partial | The copy meter finds borrowed four-word runs in a note as the student types, and the citation line builds from the card. | sibling |
| sentence-remixer | spec | taught | L.6.1, L.6.3 | partial | Each merge is built live so the glitch appears only when the merge causes it, and the rhythm strip shows sentence variety as a picture. | new-engine |
| word-thermometer | spec | taught | L.6.5, RI.6.4, RL.6.4 | partial | The tone gauge moves as words are swapped while the fact list stays fixed, so the effect of word choice shows at once. | new-engine |
| page-audio-screen | spec | taught | RI.6.7, RL.8.7 | partial | Plays two different audio readings with waveforms and a lens animation, which a printed sheet cannot. | new-engine |
| podcast-listening-club | spec | taught | SL.6.2, SL.6.3, SL.7.1, SL.7.3, SL.8.3 | partial | Timed claim cards pop up on an audio waveform with scrub back and a transcript toggle, which a worksheet or teacher reading aloud cannot match. | new-engine |
| docent-tour-talk | spec | taught | SL.6.4, SL.6.5, SL.6.6, SL.7.4, SL.7.5, SL.7.6, SL.8.6 | partial | Records takes, shows a live level meter and timer, fades the script each take and plays three openings side by side. | new-engine |
| explainer-sections | spec | taught | RI.6.5, W.6.2, W.7.2 | partial | A walking reader stops with question bubbles wherever the structure leaves a gap, which a worksheet cannot do. | new-engine |
| blizzard-scenes | spec | taught | RL.7.6, W.8.3 | partial | Facts only one narrator could know light up across side by side columns of the student's own versions. | new-engine |
| memoir-and-biography | spec | taught | RI.6.3, RI.6.6, RI.6.9, RI.8.3 | partial | Tags fill a three column table and light the timeline differences automatically. | new-engine |
| debate-prep-desk | spec | taught | D3.4.6-8, D4.1.6-8, W.6.1 | partial | The coach raises objections to the side the student built most, and a fairness meter blocks picking a side until both are fair, which a sheet cannot do. | sibling |
| theme-evidence-ladder | spec | taught | RL.6.1, RL.7.1, RL.8.1 | partial | Rungs wobble or snap as a keyed test against rival themes, which shows evidence strength more than a ranked list on paper. | sibling |
| claim-quote-comment | spec | taught | RI.7.1, RI.8.1, W.6.9, W.7.9 | partial | Dropped, unexplained and repeated quotes are flagged on the spot as dark lamps and the finished paragraph is read back with lamps lighting. | sibling |
| context-roots-dictionary | spec | taught | L.6.4, L.6.6, L.7.4, L.7.6, L.8.4, L.8.6 | partial | Locks open in order, the word splits on screen, and a strategy log counts which key cracked each word. | sibling |

## 6. Flags, beatable checks and unsure notes

- **plot-rollercoaster** [sensitive]
  - beatable: Ride: the first-to-last face 'What changed?' sentence frame has no stated check
  - beatable: Remove a scene: only three scenes have keyed jobs (flood, Karait, eggs); other pulls show nothing keyed
  - beatable: Heights: any peak among the three keyed late cards passes, so order of the first nine cards is not shown to be checked
  - unsure: flagged sensitive for the colonial household setting in Kipling; spec avoids drawing the family
  - unsure: cost_class guessed from track, ride and 6 face images
  - unsure: episode order check is not stated, only heights
- **perspective-camera**
  - beatable: Identify: choosing among four narrator types can be guessed; the 'how built' line is required and read back but its content is not stated as checked
  - beatable: Dial level has no check; a student can finish by turning the dial without reading
  - unsure: people art for four characters, 3 poses each, so cost may be nearer super
  - unsure: Tom Sawyer scene not detailed beyond 'same panel'
- **summary-squeeze**
  - beatable: Summary can be built by copying passage sentences word for word; no paraphrase or copy check is stated
  - beatable: Leak list has 60 entries so opinion in other words passes (spec accepts this)
  - beatable: Details light on keyword word families, so keyword lists pass at 50 and 25 words
  - unsure: cost_class guessed: no family engine but gauge, leaks, theme check and about 10 images
- **argument-x-ray**
  - beatable: Report: strongest and weakest reason are only required to be ribs; the spec does not say they are checked against the key
  - beatable: Cracks can be kept with 'the author left this unsupported' without explaining why
  - unsure: setting_group body-medical kept from old tag, fits the X-ray scene
  - unsure: one of three op-eds is based on real studies, two are made up and labeled
- **debate-prep-desk**
  - beatable: Sides: the spec does not say which side a card belongs on is keyed (only Doesn't help is keyed), so a card on the wrong side may not be caught
  - beatable: Pair prep and typed rebuttals 'that name a card' are checked only by naming, not by meaning
  - unsure: W.6.1 listed as a whole in the module; I split a and b as the spec does and listed c, d, e as untaught
  - unsure: D3 and D4 codes are C3 social studies, not ELA
- **source-sorter**
  - beatable: Refocus: any of three choices or own question, no stated key
  - beatable: Answer: each sentence needs a note tag, but tag relevance to the sentence is not stated as checked
  - beatable: Bibliographic details are built from the card, so the student never writes a citation
  - unsure: W.6.8 bibliographic part is automatic, so I rated W.6.8 on credibility and paraphrase alone
  - unsure: W.6.7 rated practiced: tag presence is the only check
- **book-group-table**
  - beatable: The script branches by move, not by the words typed, so frames can be filled with anything
  - beatable: Prep questions and pin are not checked for quality
  - beatable: 'Changed my mind' lines have no stated check
  - unsure: cost_class could be super: two branching scripts, three voices, about 15 images
  - unsure: SL.6.1d rated taught on the six-ideas pick; the mind-change part is self-report
- **sentence-remixer** [sensitive]
  - beatable: A student can choose only merges that do not glitch and still reach a varied rhythm without meeting the pronoun skills
  - beatable: Variety needs short, medium and long, but not that pronouns are used
  - beatable: Intensive pronoun glitch appears only for one keyed sentence
  - unsure: flagged sensitive for Grandpa Joe's rural dialect; spec protects his voice in his own words
  - unsure: untaught list empty: L.6.1 and L.6.3 are explicit codes
  - unsure: cost_class guessed from pairwise merge data and 8 people pictures
- **word-thermometer**
  - beatable: Relationship chip: the spec does not say the relationship named is checked
  - beatable: Passages: any word from a slot's set is allowed, so extreme words can be swapped at random and still read back
  - beatable: Class thermometer has no check
  - unsure: L.6.5b rated practiced because no response to a wrong relationship is stated
  - unsure: RL.6.4 and RI.6.4 are near-identical activities in two texts
- **draft-versus-draft**
  - beatable: Panel rules are narrow (Mr. Abbott smiles for a student count, Kenzie for a first sentence under 15 words), so one trivial edit can please a reader
  - beatable: Vote has no right answer; marks reveal the key's reading but nothing requires a good revision
  - beatable: Wordiness meter can be ignored and Done still holds
  - beatable: Flyer frame fit is not described as checked beyond the structure
  - unsure: cost_class super guessed: three grade levels, editor, panel rules, flyer, projector mode, saving, about 11 images
  - unsure: W.8.4 rated taught on the shared vote activity; grade 8 adds a letter text only
- **theme-evidence-ladder**
  - beatable: Wobble: the because line need only name a word from the student's own theme, so copying a theme word steadies the rung
  - beatable: Poem verdict (Holds, Holds partly, Differs) has no stated check
  - beatable: Grade 8 rung tags have no stated check
  - beatable: Timeline is a view only; the student does nothing that is checked
  - unsure: RL.7.2 and RL.8.2 rated practiced, not taught: the timeline is passive and the tags are unchecked
  - unsure: starter theme cards hand the theme to a student who does not write one
  - unsure: all three grade codes share the same activity across modes
- **claim-quote-comment**
  - beatable: RI.6.1: no check that the chosen quote actually supports the claim in grades 6 and 7, only repeats and the comment
  - beatable: Comment filler: 8 words with one claim word and one quote word passes
  - beatable: Lead-in: only presence is checked
  - beatable: Counter line has no stated check
  - unsure: spec names the module 'Citing and Explaining Evidence' while the packet says 'Analysis with Evidence from Nonfiction'
  - unsure: packet concept says the tool flags a quote that does not prove the claim, but the spec checks comment words, repeats and lead-ins, not quote fit
- **page-audio-screen** [spec-thin]
  - beatable: Pins only need an effect line, any sentence passes
  - beatable: Medium tag on explainer answers is the student's call and never checked
  - beatable: Recommendation needs two pins but not that the pins fit the request card
  - beatable: Pros and limits card has no stated check
  - beatable: Comparison line for the two readings has no stated check
  - unsure: RL.6.7 and RL.7.7 marked practiced because pins are unchecked beyond needing an effect line
  - unsure: RI.7.7 marked practiced: no check on the comparison line
  - unsure: RI.8.7 pros and limits card appears only in standards map and Done when, so touched and spec thin
  - unsure: Cost class new-engine from the 17 images and tool-only code; could be super
- **podcast-listening-club**
  - beatable: Club round: choose 'ask a question' or 'build on' every time, since only always changing your mind is closed
  - beatable: Summary reason only has to name a claim card, not a fitting one
  - beatable: Drag held cards to the three bins by trial
  - unsure: SL.7.2 practiced: chart check is keyed but main idea lines are not checked
  - unsure: SL.8.1 practiced: qualify frame is a sentence starter, unchecked
  - unsure: SL.7.1 taught because member replies depend on whether the tag was right
- **docent-tour-talk** [sensitive]
  - beatable: Record silence or noise: the meter shows a word but nothing blocks moving on
  - beatable: Grade 6 stop order is unchecked, any order passes
  - beatable: Audience openings pass on word counts and a question mark, not on fit to the audience
  - beatable: Rubric is self marked and never gates
  - unsure: SL.6.4 taught on the volume meter and timer response; grade 6 order itself is unchecked
  - unsure: SL.6.5 and SL.7.5 share one activity, spec maps both to the same step
- **context-roots-dictionary**
  - beatable: Tap every word in the passage so the keyed clue is always lit
  - beatable: Context guess text is never checked, so any word moves on
  - beatable: Clue type chip is a choice of four, open to trial
  - beatable: Verdict is self marked by the student; the tool only shows the key beside it
  - beatable: Skip to dictionary is allowed and only logged
  - unsure: L.x.4b marked touched: the tool does the split and the roots key can be skipped
  - unsure: Grades share activities, only the words change
  - unsure: Use set to station though it also teaches the strategy order
  - unsure: Packet module lists L.6.4 bare; spec names L.6.4a to d and I split them
- **pause-and-break**
  - beatable: Try slot and mark combinations until the waveforms line up, at most 9 slots and 6 marks
  - beatable: Whisper or shout and meaning questions are two-way picks
  - beatable: Final paragraph is punctuated and then simply played against the target, no stated check
  - beatable: Partner game has no stated check
  - unsure: Spec says the three spelling parts are not taught here, listed as untaught
  - unsure: Spec maps dash and ellipsis pause to L.8.2a and omission to L.8.2b
- **tricky-word-lab**
  - beatable: Family step: a wrong card names its own root, so tapping all three gets through
  - beatable: Rule reach line is a choice of three
  - beatable: Split step: tap splits until accepted
  - beatable: Review queue relies on the device clock
  - unsure: Packet family is none but the spec uses the word lab, so cost set to sibling
  - unsure: All three codes share one activity set; only the word trays differ by grade
  - unsure: Class list words without a family are plain spelling cards
- **explainer-sections**
  - beatable: Write placeholder headings: Pip only checks that a heading exists, not that it names the job
  - beatable: Section map and why-line are free text with no stated check
  - beatable: Comparison chart rows are student filled and unchecked
  - beatable: Own topic skips the definition-before-use check
  - beatable: Mix-up section is checked only for being there
  - unsure: Untaught list is my reading: precise language and formal style are not in the spec
  - unsure: W.7.2 taught because Pip checks definition order; chart itself unchecked
  - unsure: Packet module lists W.6.2 bare
- **blizzard-scenes**
  - beatable: My scene: write one line, prompt ticks are the student's own and nothing checks the scene
  - beatable: Rewrite: copy the first scene; the only-one facts are student tapped and unchecked
  - beatable: Side by side answers are free lines with no check
  - beatable: Reorder passes with any tray transition at each jump, fit not checked
  - unsure: W.6.3 and W.7.3 marked practiced: writing is unscored
  - unsure: RL.8.5 practiced: answers are free text, no key
  - unsure: W.8.3 reflective ending box is unchecked
- **memoir-and-biography** [sensitive]
  - beatable: Threads between highlights have no stated check
  - beatable: Point of view line is free text with no stated check
  - beatable: Conflict round accepts all four choices and any two sentences
  - beatable: Saying what a comparison connects is unchecked
  - unsure: RI.7.3 practiced: threads are not said to be keyed
  - unsure: RI.8.6 practiced: panel is shown whatever the choice
  - unsure: RI.8.3 taught on the span key; the connects line is unchecked
  - unsure: Sensitive for disability presentation
- **linked-feature**
  - beatable: Type filler words to pass the page counter, only typed words in the sitting count
  - beatable: Reply to a comment with any 8 words
  - beatable: Diagram labels come from a list and are not checked for fit
  - beatable: Quick-writes check only minutes, leave the timer running
  - beatable: Link claims only to paragraphs rated above 0, a few good ones cover many
  - unsure: No grade picker: all grade codes share the same path, so I split activities by the standards map
  - unsure: Editor comment collaboration sits under all three W.x.6 and is rule checked
  - unsure: W.x.10 touched because Quick-writes are a separate optional mode
  - unsure: Cost super is a guess from the many parts
- **climbing-reads** [sensitive]
  - beatable: Keep all four supports on: the hold still counts, only the badge differs
  - beatable: Chunks and guide questions work as answer hints for the checks
  - beatable: Read-aloud can replace reading and the hold still counts
  - beatable: Missed checks reveal the answering line and draw a new question from a pool of six, so repeat misses reveal answers
  - unsure: All six marked practiced: the tool teaches no reading strategy, the supports and answer line are the only help
  - unsure: Could be argued taught because of supports with feedback
  - unsure: Sensitive for the Douglass slavery chapter
