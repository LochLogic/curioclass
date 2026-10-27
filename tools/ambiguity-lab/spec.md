# Ambiguity Lab

## One idea
An open ending is built, not an accident: take two famous stories that refuse to answer their own question ("The Lady, or the Tiger?" and "Young Goodman Brown"), flip one structural switch per trial (where the story stops, whether the narrator's hedges stay, which clue survives, what order you meet things), and record what each trial does to the clue balance and to your own verdict, until your lab notebook can show which single choice of the author's holds the ambiguity open.

## Not like
- page-to-screen (ela 10, this group): the words stay and the medium changes. Here the medium stays and the structure changes.
- tension-meter (ela 9, this group): measures tension in the author's order against story order. Here the measure is how open a question stays, and the variables are cuts and endings.
- satire-decoder (ela 11, wave 4): proves one hidden meaning. Here the point is that two readings both stand, and how the text keeps them standing.
- theme-ledger (ela 9-12, spec): logs evidence for themes across a story. Here evidence is weighed for two rival readings, and the text itself is switched.
- character-web (ela 9, this group): a character's pulls. Here the princess's pulls appear only as clues for the reader's verdict.

## Who and how
- Grade 12 ELA, module Complex Structure and Ambiguity: "How structure choices contribute to meaning and aesthetic impact".
- Standards: RL.11-12.5, RL.11-12.3.
- Driver: students on laptops, alone or in pairs, after reading at least one story (Stockton about 12 minutes, Hawthorne about 22). 30 to 45 minutes for four to six trials. A teacher can project a trial and poll the room for verdicts.
- tool.json: driver "students", minutes "30-45", modes ["Read", "Tag", "Trials"], grades_label "Grade 12". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Ambiguity Lab", small line with the story; Motion, Sound, Read. A story picker: **The Lady, or the Tiger?** (Frank R. Stockton, 1882; "Which door did she point to?") and **Young Goodman Brown** (Nathaniel Hawthorne, 1835; "Was it real, or a dream?").

**Read.** The story as the current switches make it, paragraph by paragraph. Removed text shows struck through and dimmed (never hidden), so the student always sees what the trial cut; moved paragraphs carry a small "moved" tag. The question bar at the top names the two readings: **Lady | Tiger** or **Real | Dream**.

**Tag.** The clues (8 in Stockton, 9 in Hawthorne) glow in the text. Tap one: a card asks **Which reading does this support?** (Reading A, Reading B, Both, Neither) and **How strongly?** (1 or 2). Students can also tag any other sentence as a clue (up to 6 extra). **Compare with ours** shows our tags beside theirs, with one line of reasoning each.

**Trials.** The bench: four switches on the left, the text preview in the middle, the meters on the right.
- Switches, Stockton: **Ending**: Original (p25, the narrator's question) | Stop at p17 ("and opened it.") | Closed: Lady | Closed: Tiger (two-sentence endings written for Curio Class, marked "not Stockton"). **Princess's reflections** (p19 to p24): Keep | Remove. **Narrator's asides** (p18 and p25's first sentence): Keep | Remove. **Order**: From the king (p0) | Start in the arena (p10 to p17 first, then p0 to p9 as "how it came to this", then the rest).
- Switches, Hawthorne: **Ending**: Original (p69 to p72) | Stop at p68 ("look up to heaven, and resist the wicked one.") | Stop at the question (p71, without p72). **Narrator's hedges** (p12's "This, of course, must have been an ocular deception, assisted by the uncertain light." and p35's ", perhaps,"): Keep | Remove. **The forest ribbon** (p48's last sentence): Keep | Remove. **The morning ribbons** (p70's "with the pink ribbons,"): Keep | Remove.
- Meters, recomputed from the student's own tags as switches change: **Balance** (a horizontal bar, A points against B points, counting only clues still in the text); **Last clue** (which reading the last clue in reading order supports); **Asked?** (does the text still pose the question in words: Yes or No); **Answered?** (Yes only for the closed endings).
- **Run trial** saves a row to the notebook. Before saving, the student gives a **Verdict** (A, B, or Can't tell) and **Confidence** (1 to 5), and one line, "What did this change do to the meaning?" (up to 160 characters). Only one switch may differ from the original per trial unless **Two-switch trial** is ticked (marked in the row).

**Notebook** (a tab under the bench): the trial table, columns Trial, Story, Change, A points, B points, Last clue, Asked?, Answered?, Verdict, Confidence, Note. Trial 0 for each story is the original text and is added automatically on first Tag. Under it the **Conclusion card**: "Which single choice of the author's does the most to keep the question open? Name the trial that shows it." and "Why might an author build a story that will not answer its own question?" (up to 400 characters each).

Panel (right): `#hint`, **Trials** count, a two-color legend with icons, and **Clear my work** (asks Yes / No).

## Content
Texts quoted whole, exactly; paragraphs numbered from 0 as split on blank lines in the Gutenberg files (counts by script on 2026-10-27, every space-separated token with a letter or digit):
- Frank R. Stockton, "The Lady, or the Tiger?" (The Century Magazine, November 1882), Project Gutenberg eBook #396: 26 paragraphs, 2,699 words. p25 ends "Which came out of the opened door,--the lady, or the tiger?" (the source's own double hyphen).
- Nathaniel Hawthorne, "Young Goodman Brown" (New-England Magazine, 1835; collected in Mosses from an Old Manse, 1846), Project Gutenberg eBook #512: 73 paragraphs, 5,229 words. Em dashes show as two hyphens (--).

**Stockton clues and our tags** (Reading A Lady, B Tiger):
1. p8 "with a soul as fervent and imperious as his own" (Tiger 1: she is her father's daughter).
2. p11 "No wonder the princess loved him!" (Lady 1).
3. p13 "and the princess hated her." (Tiger 2).
4. p19 "She had lost him, but who should have him?" (Tiger 1).
5. p20 "had she started in wild horror, and covered her face with her hands" (Lady 2).
6. p21 "But how much oftener had she seen him at the other door!" (Tiger 2).
7. p22 "Would it not be better for him to die at once" (Tiger 1).
8. p23 "And yet, that awful tiger, those shrieks, that blood!" (Lady 2).
With our tags: Original, Lady 5, Tiger 7, Last clue Lady, Asked? Yes. Reflections removed: Lady 1, Tiger 3, Last clue Tiger (p13), Asked? Yes. Stop at p17: Lady 1, Tiger 3, Last clue Tiger, Asked? No. These are the Done when values.

**Hawthorne clues and our tags** (Reading A Real, B Dream):
1. p6 "She talks of dreams, too." (Dream 1).
2. p12 "This, of course, must have been an ocular deception, assisted by the uncertain light." (Dream 1: the narrator explains the snake staff away).
3. p25 "in whom Goodman Brown recognized a very pious and exemplary dame, who had taught him his catechism in youth" (Real 1: he knows her).
4. p35 "where, perhaps, it assumed life" (Dream 1: "perhaps").
5. p48 "The young man seized it, and beheld a pink ribbon." (Real 2: a thing he can hold).
6. p69 "he found himself amid calm night and solitude" (Dream 2).
7. p69 "a hanging twig, that had been all on fire, besprinkled his cheek with the coldest dew" (Both 1: it was on fire, and it is wet).
8. p70 "he spied the head of Faith, with the pink ribbons" (Dream 2, our reading: her ribbons seem to be on her cap the next morning).
9. p71 "Had Goodman Brown fallen asleep in the forest and only dreamed a wild dream of a witch-meeting?" (Dream 1, as a question). p72's "Be it so if you will" is shown as a note, not a clue: the narrator refuses to choose and says the effect on Brown was the same.
With our tags: Original, Real 4, Dream 9, Last clue Dream, Asked? Yes. Hedges removed: Real 4, Dream 7. Forest ribbon removed: Real 2, Dream 9. Stop at p68: Real 3, Dream 3, Last clue Real (p48), Asked? No. These are the Done when values.

**Teacher notes** (a collapsible "For teachers" strip, shown with the story):
- Hawthorne sets the story in Puritan Salem village, the town of the witch trials of 1692; his great-great-grandfather John Hathorne was a judge in those trials (Britannica). Twenty people were executed in 1692 (Britannica, "Salem witch trials"). The tool states this plainly.
- p8 "There may be a devilish Indian behind every tree": Brown's fear shows how Puritan settlers saw Native people, whose land the colony had taken; the line shows Brown's prejudice, and Hawthorne does not endorse it. p32 names a witch-lore recipe ("the fat of a new-born babe"); it is a rumor from the witch tales, not an event.
- Stockton blames the princess's jealousy on "the savage blood transmitted to her through long lines of wholly barbaric ancestors" (p13); the idea that a people's character is passed down in the blood is an old prejudice, and the story's "semi-barbaric" kingdom is a joke built on it.

## Interactions in detail
- Switches are radio groups; changing one updates Read, the meters and the preview in under 100 ms. With Motion off, moved paragraphs jump; with Motion on they slide.
- The Balance bar shows numbers and icons on both sides (door with a flower for Lady, a claw for Tiger, a sun for Real, a moon for Dream); screen readers hear "Lady 5, Tiger 7, last clue Lady, asked yes".
- Run trial is disabled until Verdict and Confidence are set; a sixth trial per story asks "Keep going?" once.
- Clue cards and extra tags are keyboard reachable (Tab through glowing clues, Enter opens).
- Closed endings are clearly boxed and labeled "Written for Curio Class, not by Stockton".
- Store: localStorage `amb-lab` (tags, trials, Conclusion card per story), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 the bench shows switches, text and meters in three columns; at 680x425 the text sits under the switches and the meters stay pinned at the top; at 760 and 375 wide the three stack, meters first. The notebook table scrolls sideways inside its box.

## Look
- `kit:theme-912` dark, accent `--brand #b9c4ff` (dusk periwinkle: switches, glowing clues, header rule, buttons), `--btn #b9c4ff`, brand text on brand `--brand-ink #1c1203`.
- Reading colors with icons, never color alone: Lady and Real `#5fd39a`, Tiger and Dream `#ffb35c`, Both striped in the two.
- Struck text in `--muted` with a line through; moved tags in the accent.
- Neighbors: page-to-screen non-photo blue (this group, dE 17), theme-ledger wine, satire-decoder. Nearest catalog colors: `--muted` (dE 24).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 11.10:1, on panel 10.22:1, on sec-bg 9.69:1; brand-ink on brand 10.91:1; `#5fd39a` on sec-bg 8.80:1; `#ffb35c` on sec-bg 9.26:1. All pass AA.

## Art
None needed: the bench, switches, meters, icons and preview.svg (two doors under a periwinkle question mark, a balance bar beneath) are drawn in code.

## Voice
Bank voice `curious-librarian` (Aoede), style "Say curiously and warmly, like a librarian who loves a story that keeps its secret". Not used by any 9-12 ELA tool or this group. `Curio.voice`, scope the mode and story. The stories are never voiced; Read speaks the hint.
- welcome (how, first open): "Two stories that won't answer their own question. Let's find out how they do it."
- tag (how, first Tag): "Tap a glowing clue. Which reading does it support, and how strongly?"
- trials (how, first Trials): "Flip one switch, give your verdict, then run the trial."
- cut (event, a trial makes Asked? turn No; stale on the next switch change): "Now the story doesn't ask the question at all. Do you still wonder?"
- closed (event, first closed ending; stale on the next switch change): "That ending isn't Stockton's. Does knowing the answer make it a better story or a smaller one?"
- conclude (how, third trial saved): "Three trials in. Which one kept the question most open? Write it in the conclusion."

## Family engine
none

## Sources
- Frank R. Stockton, "The Lady, or the Tiger?", Project Gutenberg eBook #396, https://www.gutenberg.org/ebooks/396 ; first publication in The Century Magazine, November 1882: Britannica, "The Lady, or the Tiger?" and "Frank R. Stockton".
- Nathaniel Hawthorne, "Young Goodman Brown," in Mosses from an Old Manse, Project Gutenberg eBook #512, https://www.gutenberg.org/ebooks/512 ; first publication (New-England Magazine, 1835) and John Hathorne's role: Britannica, "Young Goodman Brown" and "Nathaniel Hawthorne".
- Salem witch trials of 1692 (twenty executed): Britannica, "Salem witch trials," https://www.britannica.com/event/Salem-witch-trials
- Paragraph and word counts: computed from the Gutenberg files on 2026-10-27.
- Standards: CCSS ELA RL.11-12.3 and RL.11-12.5, https://www.thecorestandards.org/ELA-Literacy/RL/11-12/
- Clue choices, our tags, closed endings and teacher notes: written for Curio Class.

## Done when
1. Both stories show word for word from their Gutenberg files (2,699 and 5,229 words by the stated rule), paragraphs numbered as in Content.
2. With our tags, Stockton reads: Original Lady 5, Tiger 7, Last clue Lady; Reflections removed Lady 1, Tiger 3, Last clue Tiger; Stop at p17 Lady 1, Tiger 3, Asked? No.
3. With our tags, Hawthorne reads: Original Real 4, Dream 9; Hedges removed Real 4, Dream 7; Forest ribbon removed Real 2, Dream 9; Stop at p68 Real 3, Dream 3, Last clue Real, Asked? No.
4. Removed text is struck through, never hidden; closed endings carry the "not Stockton" label.
5. Run trial needs Verdict and Confidence; rows land in the notebook with every column filled; one switch per trial unless Two-switch trial is ticked.
6. Student tags replace ours in the meters; Compare with ours shows both.
7. Reload keeps tags, trials and the Conclusion card; Clear my work (after Yes) empties them; no network; console clean.
8. At every size in STANDARDS.md the switches and meters are reachable without page scroll; 375 wide works in `drive.py --host`.

## Open questions
- [ambiguity-lab] "Young Goodman Brown" has a witch meeting, the devil as a traveler, a "devilish Indian" line (p8) and a witch-lore recipe with "the fat of a new-born babe" (p32). Teacher notes handle them plainly; anything a parent might want to see first?
- [ambiguity-lab] Stockton's "savage blood" and "semi-barbaric" framing gets a teacher note naming it as an old prejudice. Enough, or should the note be on screen for students by default?
- [ambiguity-lab] The two closed endings are original text written for Curio Class and clearly labeled. OK to put invented endings beside Stockton's?
