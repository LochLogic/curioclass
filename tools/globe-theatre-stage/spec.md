# Globe Theatre Stage

## One idea
The words stay the same and the production changes: four scenes (three by Shakespeare, one by Susan Glaspell) each come in three made-up productions, and every choice a production makes (who sees whom, whether the dagger is real, how a line is pitched) is pinned to the lines that license it, so you can test which interpretation the text requires, which it only allows, and which the production adds on its own, then stage your own and defend it line by line.

## Not like
- shakespeare-remix (ela 9, this group, same family): compares a scene with the older source Shakespeare reworked. Here the text is fixed and the variable is performance; the question is interpretation, not adaptation.
- director-s-chair (arts, live): one scene in five theater traditions, each house with its own stage shape. Here the stage stays the same and the reading changes; nothing is about the building or tradition.
- stage-blocker (arts, live): blocking seen from sixteen seats, who hides whom. Here the positions are a small tableau that only matters for what it says about the text (does Hamlet see the watchers or not).
- character-voice-booth (arts, live): you say one line as different characters and see your voiceprint. Here a line has one speaker and three readings, drawn as a delivery score, and the point is which reading the words support.
- dramatic-irony-theater (ela 8, not specced): the audience knows what a character doesn't. Here that is only one of many choices, and it is the student who rules on it.
- ambiguity-lab (ela 12, this group): changes the structure of a story (ending, order). Here the script never changes; only the staging does.

## Who and how
- Grade 12 ELA, module British and World Literature: "Shakespeare and major works from British and world traditions".
- Standards: RL.11-12.7. The code asks for at least one play by Shakespeare and one by an American dramatist; the fourth scene (Glaspell's Trifles, 1916) is the American play.
- Driver: students on their own laptops or in pairs, or a teacher on a projector for one scene with the class voting. 30 to 45 minutes for two scenes.
- tool.json: driver "students", minutes "30-45", modes ["Compare", "Direct"], grades_label "Grade 12". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Globe Theatre Stage", small line with the scene name; Motion, Sound, Read. A scene picker (four cards) opens first; each card shows the play, act and scene, one line, and a "the question" sentence. A mode switch sits in the header: **Compare** and **Direct**.

**Stage.** The center of every scene is a drawn stage in code, a three-quarter view of an open-air thrust stage with two doors, a discovery space and the two pillars (the Trifles scene swaps to a plain kitchen box set, labeled "Guest company: a farmhouse kitchen, 1916"). Figures are simple silhouettes in costume color with a name tag; props are drawn icons. The stage shows a **tableau** for the line currently selected: positions, facing, who is visible to whom (a sight line drawn as a thin dashed ray), and props.

**Script panel** (left, or below on narrow screens): the scene text set by Bard.Script, verse lines numbered within the excerpt, speakers in small capitals, stage directions in italics. Glossed words carry a dotted underline. Tapping a line selects it: the stage jumps to that line's tableau, and the **delivery score** for that line appears under the stage.

**Delivery score**: the line's words in a row; stressed words in bold with a rising mark, pauses as gaps with a bar ("|" short, "||" long), pace as a band under the words (tight is fast, wide is slow), pitch as a thin contour line, and one word of direction ("cold", "teasing", "broken"). Every mark has a text equivalent read by screen readers ("Stress on lord. Long pause after sovereign. Slow.").

**Compare mode.** Three production tabs: **A**, **B**, **C**, each with a made-up title and a one-line director's note, and a banner on every tab: "Made up for Curio Class. Not a real production." Switching tabs keeps the selected line, so the stage, sight lines and score change while the words stay put. A **choice list** under the tabs names each production's 3 to 5 key choices (Content). For each choice the student sets a ruling with three buttons: **The text requires it**, **The text allows it**, **The production adds it**, and links it to the lines that support the ruling (tap lines in the script; each linked line gets a pin). **Check my ruling** shows ours, with the reason, and never scores. When every choice in a scene is ruled, a **license strip** appears for each production: a bar in three parts (requires, allows, adds) with counts.

**Direct mode.** The same scene with the decision points listed as switches (Content), each with two or three options taken from the three productions plus one option of the student's own written as a note. Choosing options builds **Your production**: the stage and scores follow, and each decision asks for at least one linked line before it counts. A short **Director's statement** box (up to 600 characters) asks: "What does your production say this scene means, and which lines make that fair?" **Read my production** shows the choices, linked lines and statement as one page, with **Copy**.

Panel (right): `#hint`, a **Gloss** card (the selected word's meaning and its source), a **Ruled** count (choices ruled, of total), the scene's question, and **Clear my work** (asks Yes / No).

## Content
Texts: Shakespeare from the Project Gutenberg Complete Works (eBook #100), cited by act and scene only, lines numbered within each excerpt; Glaspell from Plays (Project Gutenberg eBook #10623; Trifles first performed 8 August 1916). Where the source has an em dash, show two hyphens (--), never an em dash. The productions, their titles, notes and choices are written for Curio Class.

**Scene 1. Hamlet, 3.1** ("Soft you now, / The fair Ophelia!" through Hamlet's "Farewell."; about 45 lines). The question: "When does Hamlet know he is being watched, and does it matter?" Before the excerpt, a two-line setup card quotes the King: "Her father and myself, lawful espials, / Will so bestow ourselves that, seeing unseen," and the stage direction "Exeunt King and Polonius." (the text says they withdraw, not where). Key lines: "Ha, ha! Are you honest?", "I did love you once." / "I loved you not.", "Get thee to a nunnery.", "Where's your father?" / "At home, my lord."
- A "The Watched Prince": Hamlet glimpses the King's sleeve at "Ha, ha! Are you honest?"; from then his cruelty is played to the hidden listeners. Choices: sees the watchers early (allows: the sudden turn at "Ha, ha!"); "I loved you not" said toward the hiding place (adds); Ophelia's gifts thrown down (adds).
- B "The Wounded Lover": he never knows; the cruelty is hurt at Ophelia returning his gifts. Choices: no sight line to the watchers (allows); long pause before "I loved you not" (allows: "I did love you once" sits just before); "Get thee to a nunnery" said quietly, close to her (allows).
- C "The Late Turn": he realizes only when Ophelia glances off at "Where's your father?"; "At home, my lord" is a lie he hears as a lie. Choices: realization at "Where's your father?" (allows: the question and "Let the doors be shut upon him"); Ophelia looks toward the watchers (adds); exit fast on "Farewell" (allows).
- Requires (all three): Ophelia offers the remembrances back ("I pray you, now receive them."); the King and Polonius have withdrawn to watch.

**Scene 2. Macbeth, 2.1** ("Is this a dagger which I see before me," through "Thus to mine eyes."; 17 lines, then a cut mark and the last three lines, "I go, and it is done. The bell invites me. / Hear it not, Duncan, for it is a knell / That summons thee to heaven or to hell."). The question: "Should the audience see the dagger?" Key lines: "I have thee not, and yet I see thee still.", "A dagger of the mind, a false creation, / Proceeding from the heat-oppressed brain?", "I see thee yet, in form as palpable / As this which now I draw.", "There's no such thing."
- A "Empty Air": nothing is shown; Macbeth reaches at nothing. Choices: no dagger (allows: "There's no such thing"); he draws his real dagger at "As this which now I draw" (requires); the bell is a real sound (requires: "[A bell rings.]").
- B "Light on the Floor": a dagger of light appears on the boards, and blood spots bloom on it at "gouts of blood". Choices: projected dagger (allows); blood appears only at "Which was not so before" (allows); audience sees what he sees (adds a shared vision).
- C "The Wire": a real dagger hangs on a wire and swings away when he grabs. Choices: solid prop (adds: the text calls it "fatal vision" and "dagger of the mind"); it moves on "Thou marshall'st me the way" (allows); played as supernatural, not imagined (adds).

**Scene 3. The Taming of the Shrew, 5.2** (Katherina, "Thy husband is thy lord, thy life, thy keeper," through "Too little payment for so great a debt.", a cut mark, then "My mind hath been as big as one of yours," through "My hand is ready; may it do him ease.", then Petruchio's "Why, there's a wench! Come on, and kiss me, Kate." and, after a cut mark, Hortensio's "Now go thy ways; thou hast tam'd a curst shrew." and Lucentio's "'Tis a wonder, by your leave, she will be tam'd so."). The question: "Does Kate mean it?" A context card: the speech wins a bet; three husbands wagered on whose wife would come when called.
- A "Plain Words": sincere, warm, to the other wives. Choices: speech said straight (allows); Petruchio moved, not smug (allows); "may it do him ease" with her hand truly under his foot (allows: "place your hands below your husband's foot").
- B "The Long Con": Kate and Petruchio are a team winning the wager; she winks on "my reason haply more". Choices: ironic delivery (allows: "My mind hath been as big as one of yours, / My heart as great, my reason haply more"); shared look at the winnings (adds); Petruchio stops her hand before it reaches his foot (adds).
- C "Hollow": flat, exhausted, every word the same pitch; Petruchio grows uneasy. Choices: broken delivery (allows); Lucentio's last line played as a real doubt (allows: "'Tis a wonder... she will be tam'd so"); Kate exits alone (adds: the text sends them out together, "Exeunt Petruchio and Katherina", so this one contradicts a direction and the check says so).
- Requires: the speech is public, before the other couples; it ends the wager.

**Scene 4 (guest company). Susan Glaspell, Trifles, the ending** (from the stage direction "Their eyes meet. A look of growing comprehension, of horror." through "We call it--knot it, Mr Henderson." and CURTAIN, with a cut between the first "knot it" exchange and the final sequence; about 40 lines). A context card: two women in a farmhouse kitchen, while the men search for evidence that Minnie Wright killed her husband, find her canary dead in a sewing box; "Somebody--wrung--its--neck." Gloss card: to "quilt" a quilt is to stitch the layers; to "knot" it is to tie them with knots of yarn. The question: "When do the two women decide, and is it justice?" Key lines: "a sheriff's wife is married to the law. Ever think of it that way, Mrs Peters?" / "Not--just that way.", the long direction where Mrs Peters "goes to pieces" and Mrs Hale "snatches the box", "We call it--knot it, Mr Henderson."
- A "Quiet Pact": the women decide together at "Their eyes meet"; "knot it" is said flat and polite. Choices: decision at the first look (allows); flat last line (allows).
- B "Married to the Law": Mrs Peters is undecided until "Not--just that way"; the pause before "just" is the turn. Choices: decision late, at Mrs Peters's line (allows); long pause inside the line (allows: the dash).
- C "The Dare": Mrs Hale says "knot it" straight at Henderson, hand on her pocket, close to a challenge. Choices: defiant delivery (allows); hand on pocket (requires: "her hand against her pocket"); Henderson notices and lets it go (adds).
- Teaching note shown on this scene: Glaspell's stage directions are long and exact, so far more of a Trifles production is "required" than in the Shakespeare scenes, whose excerpts carry only two or three short directions each. The license strips make this visible.

Glosses (shown in the Gloss card, each with its source): orisons, prayers; honest, chaste and truthful (both senses are in play); nunnery, a convent (editors note a possible slang sense; the tool says "some editors read a second, ruder meaning" and no more); dudgeon, the handle of a dagger; gouts, drops; marshall'st, leads; meads, meadows; froward, stubborn; vail your stomachs, lower your pride; it is no boot, it is no use; quilt or knot (above); espials, spies. Source for all Shakespeare glosses: the Folger Shakespeare editions' notes (folger.edu).

Our rulings, for Check my ruling, are listed with each choice above; the license strips in the key are: Hamlet A 1 requires, 1 allows, 2 adds; B 1, 3, 0; C 1, 2, 1. Macbeth A 2, 1, 0; B 0, 2, 1; C 0, 1, 2. Shrew A 1, 3, 0; B 1, 1, 2; C 1, 2, 1 (one contradiction). Trifles A 0, 2, 0; B 0, 2, 0; C 1, 1, 1. The builder recounts these from the data so the strip and the key always agree.

## Interactions in detail
- Selecting a line updates the stage tableau in 300 ms (instant with Motion off) and the delivery score. Arrow keys move line by line; Home and End jump to the first and last line.
- Rulings: one ruling per choice; changing it is allowed until Check. Linked lines show a pin with the choice's number; a ruling with no linked line shows "Link a line first" and the Check button stays off for it.
- Check my ruling: ours appears beside the student's, with a reason. A different ruling is never marked wrong; the reason ends "Can you defend yours with a line?". For Shrew C's "Kate exits alone", the reason is fixed: "The text sends them out together. A production can do this, but it goes against a stage direction."
- Direct mode: switches are radio groups; the student's own option opens a text box (up to 140 characters). The stage follows the chosen options; a custom option draws a neutral figure pose with the note as a caption.
- Delivery score is drawn from the line data (stress, pauses, pace, pitch points, direction word). No audio of the scene lines (see Voice and Open questions); a **Read it aloud** tip suggests reading each version to a partner.
- Store: rulings, links, Direct choices and statements save to localStorage `globe-work` (try/catch), per scene. Clear my work (after Yes) empties them.
- Sizes: at 1366x768 and 1280x720 the script panel, stage and score fit side by side without page scroll. At 680x425 the script becomes a drawer over the stage. At 760 and 375 wide the stage sits on top, the score below it, the script below that with its own scroll, and the production tabs stay pinned under the header.

## Look
- `kit:theme-912` dark, accent `--brand #c0a080` (Globe oak: header rule, production tabs, buttons, pins), `--btn #c0a080`, brand text on brand `--brand-ink #1c1203`.
- The stage: oak boards `#6b4f36` with grain lines, pillars `#8a6a4a`, the "heavens" canopy `#2c3e6b` with drawn stars, the yard as `--paper`. Kitchen set for Trifles: grey-green walls `#3c4a44`, a table, a rocking chair, a stove, a birdcage.
- Production tabs carry a letter and a shape (A circle, B square, C triangle) as well as a tint: A `#7cc4ff`, B `#ffcf5c`, C `#ff8fb8`; sight lines take the production tint and a dash pattern.
- Ruling buttons: Requires solid, Allows outlined, Adds dashed, each with its word.
- Neighbors: shakespeare-remix violet `#9d8cff` (same family, dark), satire-decoder oxblood, director-s-chair orange `#ff9e5e`, stage-blocker rust (light). Nearest catalog colors: american-lit-timeline parchment (dE 21), `--warn` (dE 21).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 7.68:1, on panel 7.07:1, on sec-bg 6.70:1; brand-ink on brand 7.55:1. Production tints on sec-bg: A 8.75:1, B 11.19:1, C 7.71:1. Name tags `#e8edf3` on boards `#6b4f36` 6.38:1, on the kitchen wall `#3c4a44` 7.91:1. All pass AA.

## Art
None needed: the stage, kitchen set, figures, props and the delivery score are drawn in code. preview.svg shows the thrust stage with two figures, a sight line and a delivery score strip under it.

## Voice
Bank voice `lively-host` (Sadachbia), style "Say with lively energy, like a stage manager calling a rehearsal". The voice speaks only the tool's own lines, never the play text. `Curio.voice`, scope the scene.
- welcome (how, first open): "Pick a scene. The words never change, only the production does."
- tabs (how, first Compare view): "Switch A, B and C. Watch the stage and the score change while the words stay put."
- rule (how, first choice shown): "Rule on each choice. Does the text require it, allow it, or did the production add it? Then tap the lines that prove it."
- link (how, first ruling with no linked line): "Link a line before you check."
- check (event, each Check my ruling where ours differs; stale when the ruling changes): "Ours is different. Can you defend yours with a line?"
- strip (event, each license strip completed; stale when any ruling in that scene changes): "All ruled. Compare the strips: which production leans hardest on the text?"
- direct (how, first Direct mode): "Now it's your production. Choose at each switch, and link a line for every choice."
- guest (how, first open of Trifles): "Guest company tonight. Notice how much the stage directions already decide."

## Family engine
shakespeare (`kit/bard.js`), described in full here; Shakespeare Remix (ela 9) reuses it, and any later Shakespeare tool should too.
- **Bard.Text**: the scene data format. A scene is `{play, act, scene, source, lines: [{n, speaker, text, verse: true|false, dir: false|true, gloss: [{word, meaning, source}]}]}`, where `n` is the line number within the excerpt, `dir` marks a stage direction, and cut marks are lines `{cut: true}` rendered as "[...]". Dashes are stored as "--".
- **Bard.Script(el, scene, opts)**: renders a script: speakers in small capitals, verse with hanging indent and line numbers every five lines, prose wrapped, directions in italics, dotted underlines on glossed words. `onLine(fn)`, `select(n)`, `pin(n, label)`, `highlight(ranges, style)`. Keyboard: arrows move by line, Enter selects. Screen readers hear speaker, then line.
- **Bard.Gloss**: shared popup or card for glossed words, always with the source line ("Folger notes"). Same words get the same gloss across tools (a shared gloss list in `kit/bard-gloss.json`).
- **Bard.Align(el, columns, links)**: two or three texts side by side with links between segments; each link has a kind (kept, cut, added, changed, flipped for the remix; requires, allows, adds for this tool) drawn with its word and a line style, never color alone. Scroll is synced by segment.
- **Bard.Stage(svg, opts)**: the drawn thrust stage (doors, discovery space, pillars, canopy) with `place(figures)`, `props(list)`, `sight(from, to, style)` and `swapSet('kitchen' | 'thrust')`. Figures are silhouettes with a name tag. Motion respects the kit setting.
- **Bard.Score(el, line, marks)**: the delivery score (stress, pause bars, pace band, pitch contour, one direction word) with its text equivalent.
- **Bard.Store(key)**: localStorage wrapper with try/catch and a Clear.
Fixed by the engine: script typography, line numbering rules, the dash rule, gloss sourcing, link styles and their words, the stage drawing. Each tool brings its own scenes, its own question and its own mode.

## Sources
- Hamlet 3.1, Macbeth 2.1, The Taming of the Shrew 5.2: The Complete Works of William Shakespeare, Project Gutenberg eBook #100, https://www.gutenberg.org/ebooks/100 . Every quoted line above was checked against that file on 2026-10-27.
- Trifles: Susan Glaspell, Plays, Project Gutenberg eBook #10623, https://www.gutenberg.org/ebooks/10623 , with "First performed by the Provincetown Players at the Wharf Theatre, Provincetown, Mass., August 8, 1916." Lines checked against that file on 2026-10-27. The source prints "It's neck!" in Mrs Hale's line; keep it as printed (it is outside the excerpt).
- Glosses: Folger Shakespeare Library, Folger Shakespeare editions online (Hamlet, Macbeth, The Taming of the Shrew), https://www.folger.edu/explore/shakespeares-works/ ; quilt versus knot: Britannica, "quilting," https://www.britannica.com/art/quilting
- The count of stage directions in each excerpt is read from the excerpts themselves (Gutenberg #100 and #10623).
- Standards: CCSS ELA RL.11-12.7, https://www.thecorestandards.org/ELA-Literacy/RL/11-12/

## Done when
1. All four scenes render from Bard.Text data with excerpt line numbers, cut marks as "[...]", and no em dash anywhere (dashes show as --).
2. Selecting Hamlet's "Where's your father?" and switching A, B, C changes the tableau: sight line to the watchers present in A, absent in B, appearing in C, while the script line stays selected.
3. Every choice in the content has a ruling key; the license strips computed from data match the counts in Content (for example Macbeth A shows 2 requires, 1 allows, 0 adds).
4. Ruling Shrew C's "Kate exits alone" as Allows and checking shows the fixed contradiction reason.
5. A ruling with no linked line cannot be checked and the hint says "Link a line first".
6. In Direct mode, choosing options and linking lines produces Read my production with choices, linked lines and the statement; Copy gives plain text.
7. Every delivery score has a text equivalent a screen reader can reach; glossed words open the Gloss card with its source.
8. Reload keeps rulings and Direct work per scene; Clear my work (after Yes) empties it; no network; console clean.
9. At every size in STANDARDS.md the production tabs and mode switch are visible without page scroll; 375 wide works in `drive.py --host`.

## Open questions
- [globe-theatre-stage] The concept says "hear how delivery changes meaning". voice.py records one style per tool and keys clips by a hash of the text, so the same line in three deliveries would collide. Add a style-aware key (text plus style) so each production's key lines can be recorded? Until then the tool shows a visual delivery score only.
- [globe-theatre-stage] RL.11-12.7 asks for one American dramatist; this spec adds Trifles (1916) as a "guest company" scene on a kitchen set. Keep it here, or move the American play to a separate tool?
- [globe-theatre-stage] Parent preview: Trifles centers on a suspected murder (a husband strangled; a dead bird with a wrung neck), and the Shrew speech states a husband's rule over a wife. Both are standard grade 12 texts; the tool frames the Shrew speech as a question of interpretation.
