PASS

# Sensitivity agent: biased-bot (round 1)

Fresh read of REFINE.md (Sensitivity agent), BASELINE rules 5 to 8, spec.md, src.html (all on-screen strings, hints,
viewer text, aria labels), notes.md, voice/lines.json, art/prompts.json, tool.draft.json and refine/teaching.md.
Not bundled or driven: every line checked here is a static string in src.html or lines.json, and the teaching lens
already drove the states. Gender Shades checked against the PMLR listing and the authors' PDF.

Counts: blockers 0, should fix 1, polish 3, nit 2.

## What was checked and holds up

- **No real group is named or stereotyped on screen.** Rooms are numbers with a badge shape and color. Narration and
  hints never name a country, language or people (spec Voice: "Narration never names a real place or group of
  people"; confirmed in all 58 lines). The only real-world framing on screen is the Room 9 viewer line "Lots of
  people learn to write 1 with a long flag and 7 with a line through it.", which is accurate and normalizing.
- **No one way of writing is called wrong.** Mix-ups read "Room 9: wrote 1, got tacos", putting the error on Bitsy,
  not the writer. "Right lunch = Bitsy reads the written number correctly." defines correctness as the robot's job.
  The 0 / 15 / 0 run moves the harm onto Room 12 and Room 3 ("Now a different room is getting the wrong lunch."),
  which shows the symmetry: the plain style is not the "right" one either. Room 3 (big, wobbly writing) scores 10,
  and the notes use it to counter the "messy writing" explanation. Good.
- **No one is blamed.** Room 12 "built Bitsy ... with their own handwriting"; nothing calls that careless or mean.
  The fix is inclusion ("whose examples they are"), not punishment.
- **Numeral-style fact.** A long-upstroke 1 and a crossed 7 are common in much of continental Europe and Latin
  America (the cited Wikipedia section agrees). Stated only in the spec and linked in the notes; fine.
- **Gender Shades is accurate.** Buolamwini and Gebru, "Gender Shades: Intersectional Accuracy Disparities in
  Commercial Gender Classification", PMLR 81:77-91 (FAT* 2018). Three commercial gender classifiers (Microsoft, IBM,
  Face++) were tested on a new benchmark balanced by skin type and gender (Pilot Parliaments Benchmark, 1,270
  parliamentarians); darker-skinned women had the highest error, up to 34.7%, against at most 0.8% for
  lighter-skinned men. The notes' summary ("commercial gender classification systems ... highest error rates for
  darker-skinned women"; "the tested task was binary gender classification, not a test of every form of face
  recognition"; the lesson is to check results by group, not only an overall average) is correct and carefully
  scoped. It is marked teacher background only and is not in the scene or narration. Appropriate for grade 4
  teacher notes.
- **Rule 8.** Notes carry a "Sensitive context and sources" section. Rule 6: no unsafe language. Rule 7: privacy is
  stated on screen ("Your drawing stays on this device...") and in the notes.
- **People in art.** One asset, `cafeteria-counter`; the prompt has no people and the spec says "people no". Nothing
  is marked `people: true` and nothing needs to be.

## Findings

**SE1. should fix, general. The normalizing line is easy to miss, so a student's first and only view of Room 9's
style can be as the cause of wrong lunches.** (src.html `openViewer`, line 117; hint/voice `L.under`; notes "A
5-minute start" step 3.) The one on-screen statement that the flag 1 is a normal way to write ("Lots of people
learn...") shows only in the Room 9 jar viewer and only when that jar has cards. At the start it is empty, so the
post-run prompt "Tap a room's jar to see how its students write." leads to "This jar has no training cards yet."
(same root cause as teaching S1). A student who writes a flagged 1, often one who learned to write in another
country or from family, sees "Room 9: wrote 1, got tacos" four times and nothing that says their way is ordinary.
Better: when S1 is fixed, keep the framing line on whatever view shows Room 9's writing first (for example the empty
jar viewer showing Room 9's lunch cards: "Room 9's lunch cards. Lots of people learn to write 1 with a long flag
and 7 with a line through it. Bitsy has none of these in its jar."). Optionally add it once to the post-run Mix-ups
area when Room 9 has misses: "Room 9's 1s are written a common way Bitsy never saw."

**SE2. polish, general. Notes: tell the teacher who in the class may write like Room 9, and not to call them out.**
(notes "Sensitive context and sources", paragraph 1.) The notes say "Do not ask a child to represent an entire real
group" but don't say where the style comes from, so a teacher may not anticipate that newcomer or multilingual
students, or students taught by family from Europe or Latin America, write their 1s this way. Better, add: "The
long-flag 1 and crossed 7 are standard in much of Europe and Latin America, so some students in your class may write
them. In Try Your Writing, invite anyone who writes a different way to teach Bitsy, but don't ask who writes like
Room 9 or single a student out. Treat their style as a skill the robot lacked."

**SE3. polish, general. Notes: give the Gender Shades numbers and link so a teacher can check them.** (notes
"Sensitive context", paragraph 2, and the source bullet.) The summary is right but unquantified and unlinked.
Better: "...examined three commercial gender classification systems (2018) and found error rates up to 34.7% for
darker-skinned women, against at most 0.8% for lighter-skinned men." Source bullet: add "pages 77-91,
https://proceedings.mlr.press/v81/buolamwini18a.html".

**SE4. polish, general. Notes: state the symmetry as the respect point, not only the technical one.** (notes "Talk
about it", bullet 5.) The 0 / 15 / 0 run is the clearest evidence that neither style is wrong, but the bullet frames
it only as harm moving. Better, append: "Does that mean Room 12 writes wrong now? What does that tell you about
whose writing was ever 'wrong'?"

**SE5. nit, general. Spec Sources overstates what Gender Shades showed.** (spec.md "Sources", bullet 2.) It is cited
for "How unrepresentative training data makes a model fail for some groups". The paper measured accuracy gaps by
group and showed common benchmarks were skewed toward lighter-skinned faces; it could not see the vendors' training
data. The notes already scope it correctly. Better: "Buolamwini and Gebru ... for the teacher notes only: measured
accuracy gaps by skin type and gender in commercial classifiers."

**SE6. nit, general. Art prompt does not say "no people".** (art/prompts.json `cafeteria-counter`.) A cafeteria
scene can pull in lunch staff. Local models never draw people, so add "no people, empty counter" to the prompt and
`"people": false` to the entry so a regenerate can't slip one in. (The spec names Cloudflare FLUX.2 while the entry
says flux1-schnell local; the art lens should settle which.)

## Sources

- [PMLR 81: Gender Shades](https://proceedings.mlr.press/v81/buolamwini18a.html)
- [Authors' PDF copy](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS089/PDF_files/Gebru_18.pdf)
- [MIT Media Lab publication page](https://www.media.mit.edu/publications/gender-shades-intersectional-accuracy-disparities-in-commercial-gender-classification/)
- [University at Buffalo summary (vendors named)](https://www.buffalo.edu/catt/ai-resources/ai-in-practice/the-dataset-doesnt-lie.html)
