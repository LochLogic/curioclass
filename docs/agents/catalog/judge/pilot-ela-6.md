# Judge report: pilot, grade 6 ELA (2026-11-10)

23 tools: 9 grade 6 tools and 14 from the grades 6-8 band. Inputs: docs/agents/catalog/tables/pilot-ela-6.md and the
two row files. Read and report only; nothing else was changed.

How much I read: four specs in full for the cold re-read (climbing-reads, book-group-table, source-sorter,
theme-evidence-ladder). Eleven more at section level (One idea, Who and how, Standards map, Screens, Content, Can it
be beaten): claim-quote-comment, blizzard-scenes, linked-feature, page-audio-screen, debate-prep-desk,
explainer-sections, pause-and-break, tricky-word-lab, context-roots-dictionary, sentence-remixer, plot-rollercoaster.
For the other eight I read Who and how and Content only, so calls on them lean on the rows and say so.
One caution on the cold re-read: I had seen the tables (not the row files) before reading the specs.

## A. Cold re-read: can the extract be trusted?

Depths are mine first, then the row's. "Taught" and "practiced" use the brief's own wording.

| Tool | Where I differ | Who is right |
|---|---|---|
| climbing-reads | Row: all six codes practiced ("teaches no reading strategy"). Mine: by the brief's words it is taught (keyed checks, a miss shows the answering line, supports come off one by one, which is the standard's own "scaffolding as needed"). Kinds: row 1/2/1, mine 2/1/2; nothing is timed or repeated, so fluency 2 is wrong. | Neither label fits. The row added a test the brief does not have. The real point both miss: 24 passages of 250 to 450 words is not a year of reading (see B). |
| book-group-table | Row: SL.6.1a, b, c, d all taught. Mine: a practiced (two questions and a pin, nothing checks them, they only light when used); b touched (the only rule the tool can catch is tapping while Priya's bubble plays; goals, deadlines and roles from the standard are absent); c taught; d taught for the key ideas (two of six keyed off the question), unchecked for "changed my mind". | Me on a and b. The row's own unsure note flagged d. |
| source-sorter | W.6.8 taught: agree, and both of us saw the citation is built by the tool. W.6.7: row practiced; mine is "done in full with a model, not checked" (the student runs a short project end to end and the pattern card models the refocus). Kinds 1/1/3 against 1/1/2. | The scale has no slot for this. "Practiced" undersells it; "taught" by the brief's words overstates it. |
| theme-evidence-ladder | Agree on all seven depths. I would put RL.7.2 one step lower (the timeline is only looked at). Kinds agree. | Row is right. |

Paper version: I also wrote "partial" for all four. The field cannot separate tools. Beatable lists: the rows found
everything I found; they are the best part of the extract. The `unsure` notes are honest and pointed at nearly every
depth I would change.

**Verdict.** Trust the rows as they are for: which codes, the activity, where it sits, beatable, unsure, cost.
Do not trust `depth`, `kinds` or `paper_version` as they are. Of 19 depth entries in four tools, 3 are wrong against
the brief and 7 more (climbing-reads, W.6.7) are cases the scale cannot express. The fault is the scale more than the
model: "taught" asks for a response that depends on a right answer, so free writing and talk can never reach it, and
each agent settled that its own way.

**Is taught / practiced / touched right for ELA? No.** It folds three separate facts into one word: what help the tool
gives, who can tell if the work was good, and whether the student can skip it. Proposed change to CATALOG-EXTRACT.md
(for every subject; ELA needs it most): replace `depth` with four short fields per code.

- `support`: `modeled` (a worked example or model text is shown first), `guided` (frames, prompts or a checklist while
  working), `none`.
- `check`: `tool-key` (compared with a keyed answer), `tool-rule` (a rule such as a word count or "uses a word from
  the claim"; write the rule), `self-guide` (the student compares with a key, model or rubric the tool shows),
  `teacher` (only on the printout), `none`. Add the sentence: "If you cannot name what the tool compares the student's
  work with, the check is not tool-key."
- `on_path`: `default`, `grade mode` (name it), `optional`.
- `share`: `all` of the standard's wording, or `part` (name the missing part, for example "citation is automatic").

Add one rule: "Free writing or talk is never marked down only because it has no answer key. Record support and check
as they are." The script then sets status: covered = default path, and either a tool check that needs the skill, or
modeled or guided work with a self-guide or teacher check. Practice only = no support and a right-or-wrong check.
Thin = no check and no guide, or optional.

Three more wording fixes:
1. `paper_version` becomes `screen_role`: `core` (the teaching move needs live response, audio or a simulation),
   `helper` (the screen speeds up or checks what paper could teach), `none`.
2. `kinds` is a math scale. For ELA use `work`: read closely, write, speak and listen, language skill (0 to 3 each).
3. Two new fields the bar needs: `texts` (title, source: public domain, adapted, or written for Curio Class; length;
   topic) and `grade_split` for band tools (`new text and new demand`, `same text, added step`, `same for all`).

## B. Against the adoption bar

### The eight "practice only" standards and W.6.10

| Standard | Tool | Call | Why |
|---|---|---|---|
| RL.6.7 | page-audio-screen | Fixable hole | Pins need only an effect line. The storyboard data already holds a key of what each frame adds, cuts or changes; the spec does not use it below grade 8. Also: the "film" is a 12-frame storyboard, not video. The two audio readings are real. |
| RL.6.9 | theme-evidence-ladder | Part real gap | One pairing (story and poem). The Holds, Partly, Differs pick is unchecked and nothing sends the student back into the poem. Spec note fixes the tool; comparing across genres also belongs in every unit that pairs texts. |
| RL.6.10, RI.6.10 | climbing-reads | Year standard | No single tool can teach "reads the range of the grade band by year's end". The tool is an honest support. The standard is met by the unit texts and the Reading Room. |
| RI.6.1 | claim-quote-comment | Real hole | At grades 6 and 7 nothing checks that the quote supports the claim, which is the standard. The spec already keys a point per paragraph. Cheap fix. |
| W.6.3 | blizzard-scenes | Real gap | Grade 6 mode is "write and retell": no model is read (models start at grade 7), nothing is checked, one line passes, and transitions and an ending (W.6.3c, e) appear only at grade 8. |
| W.6.6 | linked-feature | Extract artifact | The student does the whole standard: types three pages in a sitting, produces a web page, answers rule-checked editor comments. Guided with a tool rule. Count it as covered. |
| W.6.7 | source-sorter | Mostly artifact | A full short project with a modeled refocus. One small hole: the three refocus choices are not keyed. |
| W.6.10 | linked-feature | Year standard | "Write routinely" is a habit across a year. Quick-writes and the log help; they cannot be the proof. Met by the unit plan. |

Result: of nine flagged, two are artifacts, three are year standards, four need a spec note (RL.6.7, RL.6.9, RI.6.1,
W.6.3). None needs a new tool, but see "argument writing" just below.

### Sub-parts

- **W.6.1c, d, e** (linking words, formal style, concluding statement): a real gap. debate-prep-desk's spec claims
  only a and b, names its module "Both Sides of a Question", and centers on counterclaims (a grade 7 skill and a C3
  skill). The module in data/modules.csv is "Argument Writing". No grade 6 tool has a student write a whole argument
  with linked reasons and a close. The Draft step can carry c and e as real checks (a linking word between claim and
  reason, a closing line that restates the side). That is part of writing the argument, not a thin add-on.
- **W.6.2d, e** (precise and subject words, formal style): d is closer than the row says, since Pip already stops at a
  fact-pack word used before it is defined. Name it in the Standards map and require a set number of fact-pack terms.
  e is untaught.
- **Formal style (W.6.1d, W.6.2e)**: teach it once, well. draft-versus-draft (W.6.4, letter to the principal) is the
  natural home; the two writing tools then reuse its flag list in their draft checks.
- **L.6.2 split**: healthy. pause-and-break teaches L.6.2a, tricky-word-lab teaches L.6.2b, and each spec says so.
  Both modules list bare L.6.2, L.7.2, L.8.2. Fix the data, not the tools: put the lettered codes on each module and
  drop "spell correctly" from the commas module description.

### Band tools: do grades 6, 7 and 8 really differ?

| Kind | Tools | What the spec shows |
|---|---|---|
| New text and new demand per grade | podcast-listening-club, draft-versus-draft, pause-and-break | Three episodes with a new test each (enough evidence, true but irrelevant). Three letter pairs plus the wordiness meter and the flyer. Three different punctuation skills. |
| New content, same activity (right for these standards) | context-roots-dictionary, tricky-word-lab, climbing-reads | A passage and word set per grade; a word tray per grade; harder passages of the same six works. L.x.4 and "spell correctly" read almost the same in each grade, so this is honest. |
| Same text, a step added per grade | theme-evidence-ladder, claim-quote-comment, memoir-and-biography, page-audio-screen, explainer-sections, blizzard-scenes | One story, article or scene for all three years. Grade 7 and 8 add a tag, a link or a section. Several added steps are unchecked (RL.7.2 timeline, RL.8.2 tags, RI.7.3 threads, W.8.9 counter line, RI.8.7 card). |
| One path for all | linked-feature, docent-tour-talk | linked-feature has no grade picker; its one path holds all three grades' demands and three topics. docent-tour-talk maps SL.6.5 and SL.7.5, and SL.7.6 and SL.8.6, to the same step; four objects give fresh content. |

The six "same text" tools are the concern. A student who meets "After Twenty Years" in grade 6 meets it again in 7 and
8, so in practice each can serve one grade. Under BASELINE rule 1 a span is fine only when no grade loses anything;
here grades 7 and 8 lose a fresh text at their level.

### Texts, topics and the year spine

- **Public domain, read in the tool (9 tools):** "Rikki-Tikki-Tavi" (full text behind 12 cards), "The Gift of the
  Magi" (abridged, about 1,300 words), "After Twenty Years" (full) with "Auld Lang Syne", a 350-word Tom Sawyer
  excerpt, two Aesop fables, "The Open Boat" section III (adapted, about 600 words), Helen Keller's memoir with
  Sullivan's letter (exact text), six excerpt sets in climbing-reads (London, Frost, Shakespeare, Douglass, Faraday,
  the 1911 Boy Scouts Handbook), and Gettysburg Address quotations.
- **Written for Curio Class from sourced facts (14 tools):** every article, op-ed, podcast script, source card, model
  scene and practice passage. Lengths run 200 to 600 words.
- **Record of why each text sits there:** none in any spec. climbing-reads cut its Lexile claim and orders holds by a
  readability score that is not written down. Nothing here is longer than about 1,300 words.
- **Topic thread:** none by design; each tool is an island. There are echoes a unit could use:
  school rules (argument-x-ray, debate-prep-desk, podcast-listening-club, draft-versus-draft; phones appear twice);
  lighthouses (summary-squeeze, page-audio-screen); O. Henry's "The Four Million" (book-group-table,
  theme-evidence-ladder); animals and habitat (beavers, monarchs, moths under streetlights, Rikki, White Fang,
  homing animals); learning to read and to name the world (Keller, Douglass); lightning (source-sorter,
  explainer-sections).

What it means: the bar judges a course, and its three ELA asks are jobs for units and the Reading Room. The tools
should not be rebuilt around topics. Two things the tools do owe: a short text record for every text a student reads
(same shape as the Reading Room's `record`), and evidence checks that really send students back to the text (the
RI.6.1 and RL.6.9 fixes). Long texts, topic sets and knowledge that piles up come from the Reading Room.

### Overlap the tags missed

| Pair | Call | Note |
|---|---|---|
| theme-evidence-ladder and claim-quote-comment (citing evidence) | Healthy second angle | Ranking literary evidence against rival themes; then introducing and explaining a quote in writing. Same engine, different move, different kind of text. |
| perspective-camera and blizzard-scenes (point of view) | Healthy, close | Both light "what only this narrator can know". Reading first, writing second. perspective-camera's rewrite already checks reach; blizzard-scenes should borrow that check rather than leave grade 6 unchecked. |
| summary-squeeze and theme-evidence-ladder (RL.6.2) | Healthy ladder | Fable theme with two details, then story theme with ranked passages. The opinion-word summary flag is in both; fine as reuse. |
| argument-x-ray and podcast-listening-club (supported or not) | Healthy | The same skill on the page and by ear, as RI.6.8 and SL.6.3 intend. Order them in the spine. |
| book-group-table and the podcast club round (talk moves) | Healthy | The club round is short and a sibling in idea. No change. |
| source-sorter and linked-feature (citing) | Shared hole | Both build the citation for the student. Nowhere in grade 6 does a student put one together. |
| climbing-reads and the Reading Room (other shelf) | Duplicate in the making | A small second library with its own six excerpts, supports and checks, and no text record. |

### Beatable notes worth a spec edit before build

1. claim-quote-comment: quote fit is unchecked at grades 6 and 7 (RI.6.1).
2. debate-prep-desk: only "Doesn't help" is keyed; a card on the wrong side passes.
3. sentence-remixer: glitches appear only when a merge causes one, so a student can finish without meeting case,
   shift, vague or intensive pronouns. It is the sole teacher of L.6.1.
4. plot-rollercoaster: card order is not said to be checked, and only three of twelve scenes have keyed jobs for
   Remove a scene. It is the sole teacher of RL.6.5.
5. summary-squeeze: a summary can be copied sentence by sentence, and keyword lists pass at 25 words.
6. theme-evidence-ladder: the because line passes with any word from the student's own theme.
7. blizzard-scenes: one line passes; ticks are self-set; any transition fits any jump.
8. page-audio-screen: pins unchecked; the RI.8.7 card is in the Standards map but not in Screens.
9. source-sorter: refocus choices not keyed; note tags not matched to sentences.

Fine as they are (by design, or the fix would cost more than it gives): docent-tour-talk recording silence (no speech
recognition is a privacy choice; the rubric is a fair self-check), context-roots-dictionary's self-marked verdict
(the key is shown beside it), climbing-reads keeping supports on (the map shows it), linked-feature filler typing,
tricky-word-lab's device clock, draft-versus-draft's vote with no right answer.

## C. Proposals

### One line per tool

| Tool | Proposal | Note |
|---|---|---|
| plot-rollercoaster | Keep with a spec note | Check card order; key a job for all twelve scenes. |
| perspective-camera | Keep | Place before blizzard-scenes in the spine. |
| summary-squeeze | Keep with a spec note | Add the copy meter (four-word runs) to summaries; ask for sentences at 25 words. |
| argument-x-ray | Keep with a spec note | Check strongest and weakest reason against the key. (From the row; spec not read in full.) |
| debate-prep-desk | Reshape (small) | Key each card's side. Draft step checks a linking word and a closing line (W.6.1c, e). Settle the module name. |
| source-sorter | Keep with a spec note | Student builds one citation from the card's parts. Key the refocus choices (too big, off the notes, fits). |
| book-group-table | Keep; move a code | SL.6.1b is not taught here. Either the student sets a goal and a role before the talk and the closing checks it, or b moves to the unit's real discussion. Say on screen that the Class tracker is where real talk happens. |
| sentence-remixer | Keep with a spec note | Done needs one fix of each glitch type; steer the first remix into them. |
| word-thermometer | Keep with a spec note | Key the relationship chip (L.6.5b). (From the row.) |
| draft-versus-draft | Keep with a spec note | Own formal style: a flag list other writing tools reuse. |
| theme-evidence-ladder | Keep with a spec note | Because line needs a word from the passage as well. Poem verdict needs a pinned poem line, then shows a model comparison. Texts for grades 7 and 8 (question 2). |
| claim-quote-comment | Keep with a spec note | Check the quote's keyed point against the claim at every grade. Fix the module name in the spec. |
| page-audio-screen | Keep with a spec note | Check pin type against the storyboard key at grade 6. Write the RI.8.7 card into Screens. |
| podcast-listening-club | Keep | The best model of a band tool: a new text and a new demand per grade. |
| docent-tour-talk | Keep | Check grade 6 stop order as grades 7 and 8 do. |
| context-roots-dictionary | Keep with a spec note | Make the roots step count (a short keyed pick of the root's meaning) so L.x.4b is not skippable. |
| pause-and-break | Keep; fix module codes | L.6.2a, L.7.2a, L.8.2a, b on its module. |
| tricky-word-lab | Keep; fix module codes | L.6.2b, L.7.2b, L.8.2c on its module. |
| explainer-sections | Keep with a spec note | Name W.6.2d where fact-pack terms are required; add the formal style flag (e); check that a heading shares a word with its section. |
| blizzard-scenes | Reshape (small) | Grade 6 reads one model first. Replace self-ticks with "tap the line in your scene that does this". Reuse the can-know check on the rewrite. Bring the transition tray and an ending box down to grade 6. |
| memoir-and-biography | Keep with a spec note | Key the grade 7 threads. Keep the sensitivity review. (From the row.) |
| linked-feature | Keep; move a code | Count W.6.6 as covered. W.6.10, W.7.10, W.8.10 become year standards (question 1); the log stays as a helper. |
| climbing-reads | Hold, then reshape | See question 3. |

Nothing is cut. No code loses its teacher.

### Questions that need the owner (5)

1. **Year standards.** RL.6.10, RI.6.10 and W.6.10 cannot be taught by one tool. Record them as met by the year spine
   and the Reading Room, with tools listed as helpers? **Pick: yes.** Reason: it is the honest reading of the
   standard, and rule 2 forbids a thin activity added to make a code look taught.
2. **A text per grade for the six "same text" band tools.** **Pick: yes, as spec additions, in the order the spines
   need them; grade 6 uses today's text.** Reason: rule 1; no student should meet one story three years running, and
   grades 7 and 8 deserve a text at their level.
3. **climbing-reads and the Reading Room.** Build it as its own six-work library, or hold it and reshape it as a
   climbing view over Reading Room texts (supports, checks, range map) once those carry a text record?
   **Pick: hold and reshape after the ten-story pilot.** Reason: one library, one record, far more range.
4. **What counts as "taught" for writing and talk a tool cannot mark.** Accept "a model, a guide while working, and a
   self-check or teacher check against a shown guide" as taught? **Pick: yes, with the self-check on screen** so a
   solo student has it (rule 4). Reason: without this, narrative writing and discussion can never pass.
5. **Lettered sub-parts of W.6.1 to W.6.3.** Must each letter have a named, checked student action?
   **Pick: yes, inside the same tool's draft step.** Reason: reviews check coverage letter by letter, and these are
   real parts of writing the piece.

Everything else in the table above I would simply apply.

### What the grade 6 ELA year spine should take from this

- The tools cover skills; they do not make a year. The spine is built from units and Reading Room topic sets, and the
  tools are placed inside units as the skill lesson.
- Use the echoes as unit seeds: "Arguing about school" (argument-x-ray, debate-prep-desk, podcast-listening-club,
  draft-versus-draft), "Light at sea" (summary-squeeze, page-audio-screen), an O. Henry pair (book-group-table,
  theme-evidence-ladder), "Animals and their places" (summary-squeeze, source-sorter, plot-rollercoaster),
  "Learning to read the world" (memoir-and-biography, the Douglass route).
- Order by the ladders found here: summary-squeeze before theme-evidence-ladder; perspective-camera before
  blizzard-scenes; argument-x-ray before podcast-listening-club and debate-prep-desk; source-sorter before
  linked-feature; theme-evidence-ladder before claim-quote-comment.
- The spine must carry what no tool can: the year's reading range and volume (RL.6.10, RI.6.10), routine writing
  (W.6.10), real discussion with classmates (SL.6.1), at least one full narrative and one full argument taken through
  drafts with a rubric (W.6.3, W.6.1), and cross-genre comparison in each paired-text unit (RL.6.9).
- Every unit text, and every tool text used in a unit, needs the short text record. No tool has one today.
- Place each "same text" band tool in one grade only until it has a text per grade.
- Longer texts are missing. Nothing in the 23 tools is over about 1,300 words. The spine needs at least a few longer
  works from the Reading Room.
