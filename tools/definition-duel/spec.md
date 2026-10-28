# Definition Duel

## One idea
A definition is a gate, and the other player holds a deck of counterexamples: you build a math definition from condition cards, the deck throws every figure it has at your gate, and you see at once which non-examples slip in (the definition is too loose) and which true examples get shut out (it is too tight, like "two long sides and two short sides" shutting out the square), until your gate lets in exactly the right figures and you can say why each one outside fails.

## Not like
- shape-talk (eld K-2, built): describe a hidden shape with frames so a partner can guess it. Here the student writes the rule that decides membership for every case, including tricky ones (a tilted square, a square as a rectangle, 2 as a prime).
- word-problem-decoder (eld 6-8, not built): maps math words like per and each to operations. Here the words are conditions and quantifiers (all, exactly, at least, never) and the job is defining, not computing.
- math-explainer (eld 3-5, not built): explains a solution with sequence words. Here the language is the language of definitions and justification ("is not a ___ because it does not ___").
- chart-narrator, historian-s-toolkit, inbox-simulator, argument-frames-pro (eld 9-12, this group): data, history, email and debate language. This is the group's only math-language tool and its only card duel.

## Who and how
- ELD grades 9 to 12. Module: Precise Mathematical Language (Language for Mathematics).
- Driver: a student alone on a laptop, or two students sharing one (one builds, one predicts which figures slip in before Test). 20 to 35 minutes.
- Standards: WIDA.ELD-3 (Language for Mathematics) through the eight geometry, algebra and number terms; WIDA.Explain taught in full: define a term with a kind word and conditions, use precise quantifiers, and justify membership with a reason ("A ___ is not a ___ because it ___"). The math content follows CCSS (G-CO.A.1, F-IF.A.1, 4.OA.B.4, 3.G.A.1 and 5.G.B.3 for the square-rectangle relation), named in teacher notes, not on the module.
- Help setting: **Lots of help**, **Some help**, **Little help** (teacher notes map them to WIDA levels 1-2, 3-4, 5-6). Default Some help.
- Topic line: "precise definitions in math".
- tool.json: driver "students", minutes "20-35", modes ["Duel", "Precise words"], grades_label "Grades 9-12". Kit starter only.

## Screens and modes
Header: title "Definition Duel"; mode buttons **Duel** (opens first), **Precise words**; Motion, Sound, Read. Panel: Help setting, hint, tip.

### Duel (opens first)
- Term rail along the top: eight term cards in order (Square, Rectangle, Parallel lines, Perpendicular lines, Circle, Function, Prime number, Line segment). Each card shows a ✓ word when won. Any term can be opened in any order.
- Center: **Your gate**. A definition frame: "A [term] is [card] [card] [card]." The first slot is the starting definition's cards, already placed (each term starts with an imprecise definition from a classmate's notes, shown as a sticky note: "From the notes: A rectangle is a shape with two long sides and two short sides.").
- Below the gate: the hand, all condition cards for the term (5 or 6), each with its words; precise words (all, every, exactly, at least, only, never, same) are underlined. Tap a card to add it to the gate, tap a placed card to take it back. A **kind** card (what sort of thing it is) has a small "kind" tag.
- Right: **The deck**, six or seven figure cards face down, drawn in code.
- **Test the gate**: the deck's cards flip one by one (instant with Motion off) and walk to one of four trays, each with a word and an icon: **In, correct** (examples the gate lets in), **Out, correct** (non-examples kept out), **Slipped in** (non-examples let in), **Shut out** (examples kept out). Tapping a tray card shows the figure big with every condition card it meets or fails, ✓ or ✗ with words.
- The gate is won when Slipped in and Shut out are both empty. A card that does no work for this deck gets a quiet "extra" note (never for a kind card): "Every figure here passes or fails the same way without this card."
- After a win, **Explain** opens: pick one figure from Out, correct, then build "A [figure] is not a [term] because it [reason]." At Lots and Some help the reason is chosen from the failed conditions' "not" phrases; at Little help it is typed. Then one positive sentence for a tricky example ("A tilted square is a square because it has all sides equal and four right angles."). **Next term** moves on.
- The record (bottom of the panel): per term, the number of tests used. No timer, no points beyond that.

### Precise words
- Ten word cards: all, every, each, exactly, at least, at most, only, never, same, if and only if. Each card shows a plain meaning, a picture made of dots or shapes drawn in code, and two sentences from the duel terms, one where swapping the word changes the meaning ("exactly two factors" against "at least two factors": 12 has at least two factors, but not exactly two).
- A **Swap** button on each card replaces the word in the example with its partner and shows which deck figures would change trays.

## Content
Each term: conditions (letter, card words, "not" phrase), starting definition, figures with the conditions they meet, and whether each is an example. Every figure is drawn in code. The tables were checked by computing every combination of cards; the exact gates are listed.

Square. Cards: Q kind "is a quadrilateral (4 straight sides)" / "is not a quadrilateral"; E "with all sides equal" / "does not have all sides equal"; R "with four right angles" / "does not have four right angles"; P "with two pairs of parallel sides" / "does not have two pairs of parallel sides"; F "that sits flat on one side" / "does not sit flat"; R1 "with at least one right angle" / "has no right angle". Start: "A square is a shape with all sides equal." (E). Figures: upright square (Q E R P F R1, example); tilted square, 45 degrees (Q E R P R1, example); rhombus, 60 and 120 degree angles (Q E P F); long rectangle 2:1 (Q R P F R1); regular pentagon (E F); right trapezoid (Q F R1). Start lets in rhombus and pentagon. Exact gates: E with R; E with R1 (note shown: "This works here. Most books say four right angles; one right angle is enough only when all four sides are equal."). Adding F shuts out the tilted square: "A square is still a square when you turn it."

Rectangle. Cards: Q kind; R "with four right angles"; L "with two long sides and two short sides" / "does not have two long and two short sides"; P "with two pairs of parallel sides"; E "with all sides equal". Start: "A rectangle is a shape with two long sides and two short sides." (L). Figures: long rectangle (Q R L P, example); square (Q R P E, example); tilted rectangle (Q R L P, example); slanted parallelogram (Q L P); right trapezoid (Q); rhombus (Q P E). Start lets in the parallelogram and shuts out the square. Exact gate: R (with or without Q). Tip after the win: "A square is a rectangle: it has four right angles."

Parallel lines. Cards: Ln kind "are lines (they go on forever both ways)"; Pl "in the same plane" / "are not in the same plane"; Nm "that never meet, even when they go on" / "meet somewhere"; Nt "that do not touch on the page" / "touch on the page". Start: "Parallel lines are lines that don't touch." (Ln, Nt). Figures: rails (Ln Pl Nm Nt, example); tilted pair (Ln Pl Nm Nt, example); opposite edges of one face of a drawn cube (Ln Pl Nm Nt, example); nearly parallel, 3 degrees apart, an arrow showing where they meet off the page (Ln Pl Nt); skew edges of a drawn cube (Ln Nm Nt); crossing lines (Ln Pl). Start lets in nearly parallel and skew. Exact gate: Pl with Nm (Ln is the kind card).

Perpendicular lines. Cards: Ln kind; RA "that meet at a right angle" / "do not meet at a right angle"; Up "where one goes straight up and down" / "where neither goes straight up and down"; Cr "that cross each other" / "do not cross". Start: "Perpendicular lines are a line that goes up and a line that goes across." (Ln, Up). Figures: plus sign (Ln RA Up Cr, example); tilted cross with a right-angle box (Ln RA Cr, example); cross at 80 degrees, one line vertical (Ln Up Cr); two vertical parallel lines (Ln Up); two segments at right angles with a gap at the corner (Up). Start lets in the 80 degree cross and the parallel pair and shuts out the tilted cross. Exact gate: RA (with or without Ln).

Circle. Cards: Pl "lies flat in one plane" / "is not flat"; Al "is every point at one distance from a center, and only those points" / "leaves out points or adds points"; So "has some points at the same distance from a center" / "has no such points"; Rd "is round with no corners" / "has corners". Start: "A circle is a round shape." (Rd). Figures: circle (all, example); small circle (all, example); ellipse (Pl So Rd); sphere (Al So Rd); rounded square (Pl So Rd); half-circle arc (Pl So Rd). Start lets in four non-examples. Exact gate: Pl with Al. Al on the sphere: true in space, which is why Pl is needed; the tray card says so.

Function. Cards: K kind "is a rule that matches inputs to outputs"; Ev "that gives every input an output" / "leaves an input with no output"; Ex1 "that gives each input exactly one output" / "gives an input more than one output, or none"; Dif "that never gives two inputs the same output" / "gives two inputs the same output"; Num "that uses only numbers" / "does not use only numbers"; Ln "whose graph is a straight line" / "whose graph is not a straight line". Start: "A function is a rule with numbers that gives a different answer for each number." (Num, Dif). Figures as small tables: double it, inputs 1, 2, 3, 4 to 2, 4, 6, 8 (K Ev Ex1 Dif Num Ln, example); square it, inputs -2, -1, 0, 1, 2 to 4, 1, 0, 1, 4 (K Ev Ex1 Num, example); birthday months, Ana to March, Ben to July, Chen to March (K Ev Ex1, example); input 3 to both 5 and 7, with 1 to 4 and 2 to 6 (K Ev Dif Num); the circle x² + y² = 9 drawn, inputs -3 to 3 (K Ev Num); inputs 1, 2, 3, 4 with 1 to 10, 2 to 20, 3 to 30 and 4 to nothing (K Dif Num Ln). Start lets in the 3-to-5-and-7 table and the missing-output table, and shuts out square it and birthday months. Exact gate: Ex1 (with or without K and Ev).

Prime number. Cards: Wh kind "is a whole number" / "is not a whole number"; G1 "greater than 1" / "is not greater than 1"; T2 "with exactly two factors: 1 and itself" / "does not have exactly two factors"; Od "that is odd" / "is not odd"; Nf "with no factors other than 1 and itself" / "has another factor". Start: "A prime number is an odd number with no factors other than 1 and itself." (Od, Nf). Figures: 2 (Wh G1 T2 Nf, example); 7 (all, example); 13 (all, example); 1 (Wh Od Nf); 9 (Wh G1 Od); 15 (Wh G1 Od); 2.5 (G1). Start lets in 1 and shuts out 2. Exact gates: T2; G1 with Nf. Tray card for 1: "1 has only one factor: 1."

Line segment. Cards: Pt kind "is part of a line"; St "that is straight" / "is not straight"; Tw "with two endpoints" / "does not have two endpoints"; Sh "that is short" / "is not short". Start: "A line segment is a short, straight line." (St, Sh). Figures: short segment (Pt St Tw Sh, example); long segment across the card (Pt St Tw, example); tiny segment (Pt St Tw Sh, example); ray, one endpoint and an arrow (Pt St); line, arrows both ways (Pt St); curved path between two points (Tw Sh). Start shuts out the long segment. Removing Sh lets in the ray and the line. Exact gates: St with Tw; Tw with Pt.

Precise words examples: all ("all sides equal": a rhombus has all sides equal, a kite does not); every ("every point at one distance"); each ("each input exactly one output"); exactly ("exactly two factors": 7 yes, 12 no); at least ("at least one right angle": a right trapezoid has two, so yes); at most ("at most one output": the missing-output table passes, the 3-to-5-and-7 table fails); only ("only those points": the arc has only those points but not every one of them); never ("never meet": the nearly parallel lines meet off the page); same ("same plane": the skew cube edges are not); if and only if ("a number is prime if and only if it has exactly two factors": both directions hold).

## Interactions in detail
- A figure passes the gate when it meets every placed card. Trays come from the tables above; nothing is random.
- Test is always allowed, even with one card. Each Test counts once in the record. Changing a card after a Test returns the deck face down.
- "Extra" note: shown for a placed non-kind card when removing it leaves every figure in the same tray.
- Explain checks: at Lots and Some help the chosen "not" phrase must be one the chosen figure fails, else "That one is true for a ___. Pick a condition it fails." At Little help the typed reason must contain a negative (not, no, never, doesn't, isn't, n't) and at least one keyword of a failed condition (keywords per card: Q quadrilateral, four sides; E equal; R right angle(s); P parallel; F flat; R1 right angle; L long, short; Pl plane, flat; Nm meet, never; Nt touch; RA right angle; Up up and down, vertical; Cr cross; Al every point, distance, center; So some; Rd round, corner; Ev every input; Ex1 exactly one, one output; Dif same output, different; Num numbers; Ln straight line; Wh whole; G1 greater than 1; T2 exactly two, two factors; Od odd; Nf other factor; Pt part of a line; St straight; Tw two endpoints, endpoint; Sh short). The positive sentence needs the term and one keyword per condition in the winning gate.
- Little help also asks for the full definition in the student's own words after the win; checked for the term, a kind word (shape, quadrilateral, lines, rule, number, part of a line) and one keyword per gate card. A miss names the missing piece.
- Help levels: Lots of help adds a picture icon to every card, reads each card when tapped, and shows the frame "A ___ is a ___ that ___." under the gate; Some help drops the icons; Little help hides the starting frame and adds the own-words step.
- Two-player use: **Predict** (optional toggle) lets a second student tap figures they think will slip in before Test; their predictions show beside the trays.
- Mode change calls `V.hush()`. Storage `definition-duel:v1` (try/catch): help setting and the record; **Clear record** in the panel.
- Sizes: at 1366x768 the term rail, gate, hand, Test button and trays fit without scrolling; at 1000x625 the trays become a strip under the gate; at 760 the deck and trays go below the hand; at 375 the hand scrolls sideways inside its own box and Test stays pinned. Figure cards at least 72 px. No horizontal page scroll.

## Look
- Own light `:root`, a card table: `--paper #f4f1f7`, `--panel #ffffff`, `--ink #1d1626`, `--muted #5a5068`, `--line #ddd5e6`, accent `--brand #4a2c5e` (deep plum: card backs, active mode, Test), `--btn #4a2c5e`, `--head-ink #ffffff`, `--focus #b45309`. Slipped in uses `#b3261e` with ⚠ and words; Shut out uses `#1d4ed8` with ⊘ and words; correct trays use ink with ✓.
- Neighbors: shape-talk violet #4b3f9e; group accents magenta, cyan, rust, brick, coral; nearest catalog accent note-ninja #3b2d6b (dE 9.7).
- Contrast: ink on paper 15.71:1; muted on paper 6.75:1, on panel 7.55:1; brand on paper 10.35:1; white on brand 11.58:1; red 5.84:1 and blue 5.99:1 on paper; focus ring 4.49:1 on paper (non-text, needs 3:1). All pass AA.

## Art
None: drawn in code (figures, tables, mapping diagrams, cards). No people.

## Voice
Bank voice `calm-professor` (Schedar), style "Say evenly and clearly, like a calm, friendly college professor." No other ELD tool uses it. `Curio.voice`, `scope: () => state.mode`. Card words are read on tap only at Lots of help.
- w-duel (how): "Here's a definition from a classmate's notes. Add or remove cards, then press Test the gate."
- slipped (event, after a Test with slipped figures; stale on the next card change): "Some figures slipped in. Your gate is too loose."
- shut (event, after a Test with shut-out figures; stale on change): "A true example was shut out. Your gate is too tight."
- both (event, when both happen): "Too loose and too tight at once. Check each tray."
- won (event): "Exactly right. Now explain one figure that stays out."
- extra (how): "One card does no work here. You can keep it or take it out."
- explain (how): "Pick a figure outside the gate. Then say why it is not one."
- explain-miss (event; stale on edit): "That is true for this figure. Pick a condition it fails."
- w-words (how): "Tap a word. Then press Swap to see how one word changes the meaning."

## Family engine
None.

## Sources
- Common Core State Standards for Mathematics: G-CO.A.1 (precise definitions of angle, circle, perpendicular line, parallel line and line segment), https://www.thecorestandards.org/Math/Content/HSG/CO/; F-IF.A.1 (a function assigns to each element of the domain exactly one element of the range), https://www.thecorestandards.org/Math/Content/HSF/IF/; 4.OA.B.4 (prime and composite), https://www.thecorestandards.org/Math/Content/4/OA/; 3.G.A.1 and 5.G.B.3 (squares are rectangles; all rectangles have four right angles), https://www.thecorestandards.org/Math/Content/5/G/.
- WIDA ELD Standards Framework, 2020 Edition (Explain; Language for Mathematics; proficiency levels): https://wida.wisc.edu/teach/standards/eld.
- Every figure, table and starting definition is original to Curio Class; the truth tables were checked by computing all card combinations.

## Done when
- Each term's starting definition produces exactly the slipped and shut-out figures listed in Content.
- Every exact gate listed wins; Square with E and R1 wins and shows the note; F added to a winning Square gate shuts out the tilted square.
- Prime with Od and Nf lets in 1 and shuts out 2; T2 alone wins.
- Function with Ex1 alone wins; Num with Dif lets in two tables and shuts out two.
- "Extra" never shows for a kind card (Q in a winning Rectangle gate); it shows for P added to a winning Rectangle gate.
- Explain rejects a "not" phrase the figure meets; Little help accepts "A rhombus is not a square because it does not have four right angles" and rejects "because it is a shape".
- Precise words: Swap on "exactly" (to "at least two factors") moves 9 and 15 into the Prime gate, and 1 stays out.
- Record survives reload; Clear record empties it.
- How lines are spoken once in five actions; slipped and won repeat per event.
- No horizontal scroll at any listed size; the hand scrolls inside its box at 375.

## Open questions
- None beyond the group's home-language question (see then-what-happened).
