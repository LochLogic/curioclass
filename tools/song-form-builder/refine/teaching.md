# song-form-builder: Teaching lens (round 1, 2026-10-28)

Cold read of spec.md, src.html, notes.md, tool.draft.json, voice/lines.json and kit/music-studio.js (parse, semi,
rowSemi). Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py song-form-builder` (100 KB). Driven with
`scripts/drive.py`, held clicks, 1366x768, 1280x720, 680x425. Frames and scripts in the lens scratch folder
(lens-sfb-teaching/out: dw1_play, dw2_edit, dw2_linked, dw4_twin, dw67, listen0 to listen5, listenwrong, listen_mid,
preview680, w1280). No console errors in any shot.

Counts: blockers 0, should fix 1, polish 2, nits 4.

## Musical facts checked

- **Listen songs, note by note.** I wrote my own reference transcription of each song (in C, as sung in US classrooms)
  and parsed the tool's strings with a Python copy of `MS.parse` (lengths `e .5, dq 1.5, h 2, w 4`, numbers as beats,
  `scale .5` for 6/8). Every bar sums to its meter (4 beats; Row Row Row 3 quarter beats = one 6/8 bar), and every
  pitch and rhythm matches: Hot Cross Buns (E D C | x2 | C C C C D D D D | E D C), Mary (E D C D E E E, D D D, E G G /
  E D C D E E E E D D E D C), Twinkle (A: C C G G A A G F F E E D D C; B: G G F F E E D twice), Ode to Joy (both
  endings E. D D and D. C C; B phrase D D E C | D EF E C | D EF E D | C D G3), Row Row Row (C. C. | C D E. | E D E F |
  G.. | C5 x3 G x3 E x3 C x3 | G F E D | C..), Frere Jacques (C D E C | E F G | GAGF E C | C G3 C).
- **Engine pitches.** `semi()` gives C 0, D 2, E 4, F 5, G 7, A 9, G3 -5, C5 12 above middle C (261.63 Hz); the
  pentatonic rows are 0 2 4 7 9 12 (do re mi sol la high do). Right.
- **Forms.** A vs A′ compared bar by bar: Mary's A′ shares bar 1 and the start of bar 2, then a new ending; Ode to
  Joy's A′ differs only in bar 4. Hot Cross Buns AABA, Mary A A′, Twinkle ABA, Ode A A′ B A′ (AABA), Row Row Row
  ABCD, Frere Jacques AABBCCDD are the usual classroom analyses at the phrase lengths the spec chose.
- **Public domain.** All six are: Hot Cross Buns (English street cry, 18th century), Frere Jacques (French, 18th
  century), "Ah! vous dirai-je, maman" (published 1761), Mary Had a Little Lamb (words 1830, traditional tune), Row
  Row Row Your Boat (tune published 1881), Beethoven's Ninth (1824). Starter songs are original.
- **Form card rules.** Ran `analyze()` on 24 strips: AAA strophic; A A′ and A A′ A A′ twin; ABC, ABCD through-composed;
  AB binary; AABB binary repeated; ABA, B A B (with "Your B plays the A part. Your A plays the B part.") ternary;
  AABA and A A′ B A′ AABA; ABACA, ABABA, ABACABA rondo; ABBA, AAB, ABCA no special name; single block asks for more.
  All match the spec's order and wording. The ending check (`row % 5 == 0`) is do or high do: right.
- **Starter songs** match the spec (Sunny Day ABA ends on do; Rondo for Recess ABACA ends on do).

## Standards (rule 2)

Module arts-3-5-form-and-composition: MU:Cr2, MU:Cr3, MU:Re7. This is the only tool on the module.
- **MU:Cr2 (organize and develop):** taught. Students write 8-beat sections on a solfege grid and arrange them into
  forms (Cr2.1a), documented as iconic notation: lettered, shaped blocks and the grid, saved (Cr2.1b).
- **MU:Cr3 (refine and complete):** taught for Cr3.1. The Form card gives criteria and feedback the student acts on
  ("A and B have the same notes", "A′ is still the same as A", "Ends away from do"), and the linked edit makes
  revising one section revise the whole song. Cr3.2 (present and describe expressive intent) lives only in the
  teacher's Talk about it questions.
- **MU:Re7 (perceive and analyze):** taught for Re7.2's structure half: Listen has students identify same, almost
  and new by ear. The "how structure shapes a response" half is thin in Listen (see polish 1). Re7.1 (choosing music
  for a purpose) is not touched; fine at anchor level, but worth naming in notes.

## Done when

1. PASS. Held clicks A, B, A then Play song: playhead walked slots 0, 1, 2; card "A B A / Ternary form: away and
   back home."; spoken "A B A. You went away and came back home." after the music (dw1_play).
2. PASS. One cell in A's editor: both A slots changed (dataset keys and sketches), "2 copies changed"; the linked
   line spoken once over three edits (dw2_edit, dw2_linked).
3. PASS. All rules, including B A B as ABA, A A′ B A′ as AABA, ABACA as rondo (analyze run above).
4. PASS. A's beat 1 change reached A′; A's beat 7 change did not; A′'s beat 1 is locked with the chain tip; A′'s
   beat 8 is its own (dw4_twin).
5. PASS. All six songs labeled to their spec forms and end lines (listen0 to listen5); a wrong label replays the
   compared phrase (part 1) and then part 2 (listenwrong: phrase 0 at 4.7 s, phrase 1 at 7.5 s); two misses reveal
   "It's A again: exactly the same music."
6. PASS. playHow spoken once in the run, form line on each of three Plays (dw67).
7. PASS. Lines come after onEnd; Read during play stopped it (playing true, then false) and read the hint (dw67).
8. PASS. Strip, Play song and Form card on screen at 1366x768, 1280x720 and 680x425 (dw1_play, w1280, preview680).

## Findings

### Should fix

1. **Listen, Ode to Joy part 4 (src.html:829-838, 893-906): a correct ear gets "Not quite".** Part 4 is exactly
   A′ again (the same as part 2), but the buttons are only per base letter: Same as A, Almost A, New. A student who
   hears "that's part 2 again" and taps Same as A is marked wrong, and the replay compares part 4 with part 1, never
   with part 2, so the tool never confirms what the student actually heard. Better: once A′ is labeled, show a
   "Same as A′" button (and a ▶ A′ hear button) and accept it for a repeat of A′; or at least make the reveal and
   lAnswer say "A′ again counts as Almost A". Seen in listen3 and listen_mid; checked against the code paths.
   family:music-studio (Listen labeling format).

### Polish

1. **Listen end lines name letters only (src.html:334-341); Re7.2's response half is left to the teacher.** Build's
   form lines already tie form to feeling ("You went away and came back home", "Ends on do: sounds finished"); Listen's
   end lines mostly just spell the letters. A solo student never hears how the form shapes the listening. Better: one
   clause per song on the card and in the end line, for example "Twinkle Twinkle is A B A. The tune comes home at the
   end, so it feels finished." and "Ode to Joy is A A′ B A′. B is the trip away; A′ brings you back." This is real
   teaching, not a thin add-on. family:music-studio.
2. **A′ is taught only as "same start, new ending" (spec, H.editTwin, L.reveal.twin, notes.md).** That is one kind of
   variation; real A′ sections can change rhythm or the middle too (Mary's A′ already changes the rhythm in bar 2).
   Better: one line in notes.md's Good to know: "In real music A′ can be any small change; this tool shows the most
   common one, a new ending." general.

### Nits

1. **Sources, Mary Had a Little Lamb (tool.draft.json sources, src.html:18):** "Mary Had a Little Lamb (Sarah
   Josepha Hale, 1830)" sits in a list of public domain *melodies*; Hale wrote the words. The spec says "poem by". Say
   "words by Sarah Josepha Hale, 1830; traditional tune". general.
2. **Ode to Joy is the classroom version (spec, notes.md):** transposed to C and without Beethoven's tied
   anticipation into the last phrase. Fine for the grade; one phrase in notes ("the classroom version of Beethoven's
   tune, in C") keeps a music teacher from flagging it. general.
3. **ABABA is called a rondo (src.html:405, spec rule 7).** Inside the spec, and some texts accept it, but most
   grade 3-5 material defines rondo as A between *different* parts (ABACA); the spoken line "between new parts" is not
   quite true for ABABA, where B repeats. Optional: have ABABA's card add "Most rondos bring a new part each time
   (A B A C A)." family:music-studio.
4. **notes.md, A 5-minute start, step 2:** "listen to the Form card: 'Ternary form: away and back home.'" The card
   shows that text, but the voice says "A B A. You went away and came back home." Say "read the Form card" or quote
   the spoken line. Also the Two modes list of card names leaves out "A and its twin". general.

## Guardrails and sensitivity

Grades 3-5, students or teacher: no K-2 rule. No hard history, no health topic, no scoring or timer (Listen keeps no
score). No cultural, Native or living-tradition music: all six songs are European or American public domain children's
and concert tunes; no sensitivity agent needed (rule 5). Teacher notes: no sensitive topics in these standards (rule 8).
Nothing in Listen gives the answer away: the current part shows only "?", its sketch and playhead dot stay hidden until
it is labeled, and the aria-label says "listening now".
