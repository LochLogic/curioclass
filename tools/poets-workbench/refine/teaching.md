# Teaching lens: poets-workbench (Curiosity No. 10), round 1

Cold lens. I read the spec, src.html, notes.md, art/prompts.json, voice/lines.json, audit-states.json, the
CODEX-CURIOSITY brief, VISION "Curiosities: the second shape" and the shared audit (audit-r1). I did not read
the codex reports. I drove the bundle myself (drive.py, port 9441). My frames and data are in
`S:/CurioClass-codex-scratch/poets-workbench/teaching/`: `frames/t-*.png`, `facts-out.json` (Done-when checks,
rhyme lists, sample scansions) and `meters-out.json` (meter names and unknown words for all 16 shelf poems,
529 lines).

Counts: blockers 3, should fix 7, polish 3, nit 1.

## Blockers

**B1. "here" and "hear" do not rhyme with "near", "year", "fear": the Frost rhyme scheme and the rhyme drawer are
wrong.** (rhyme index, `pronunciation()` src.html:322; Frost on the shelf; Done when 5)
CMU lists `here`, `hear`, `ear`, `tier`, `we're` as `IY1 R` but `near`, `year`, `fear`, `dear`, `clear`, `queer`
as `IH1 R` (checked in `_scratch/poets-workbench/cmudict.dict`: 31 entries end `IY1 R`, 192 end `IH1 R`). In
American English these are the same sound before R. That is an inconsistency in the dictionary, not a real
difference. The tool treats it as real:
- Stopping by Woods, the default poem, shows `AABA CCDC DDED EEEE`, not the AABA BBCB CCDC DDDD in Done when 5
  (frame `t-frost.png`; "here" gets B, "queer/near/year" get C).
- The drawer for "hear" lists 34 perfect rhymes. Most are surnames (baehr, grier, keir, speare, teare, keneer,
  manteer) and fear, near, dear, year, clear are missing (frame `t-hear.png`).
- The Manual explains the split as "strict" dictionary hearing (src.html:840). That tells students two words they
  say the same way sound different.
It is a readout that lies, on the first poem and on some of the most common rhyme words in English.
Fix: treat `IY R` as `IH R` when building the rhyme keys, and check the other pre-R vowel pairs CMU mixes the same
way. Then Frost reads AABA BBCB CCDC DDDD, Done when 5 passes and the Manual note can go.
Tag family:curiosity.

**B2. Meter names with fractions of a foot: 227 of 529 shelf lines read "3.5 feet", "2.7 feet", "3.3 feet".**
(`scanLine` src.html:405-407)
`lengthName` divides syllables by foot size, so any line that doesn't divide evenly gets a decimal. 85 lines get
thirds ("anapestic 3.3 feet", "dactylic 2.7 feet"), which isn't a measure anyone uses. The textbook examples are hit
hardest:
- The Tiger: 12 of 24 lines say "trochaic 3.5 feet". It's the standard example of trochaic tetrameter with the last
  syllable dropped.
- The Raven: 42 lines "trochaic 7.5 feet" and 17 refrains "3.5 feet". Poe himself called these octameter and
  tetrameter with a missing syllable.
- Invictus, chosen because it "reads cleanly": "anapestic 2.7 feet" and "dactylic 2.7 feet" (`meters-out.json`).
A grade 7 student learns that meter comes in fractions. Under the brief that is a meter that misleads when its
assumption doesn't hold.
Fix: name the length from the number of stressed beats or whole feet. Say what's left over in words, such as
"trochaic tetrameter, last syllable dropped" or "iambic tetrameter + 1 extra". Never print a decimal.
Tag family:curiosity.

**B3. The rhyme-scheme strip runs two-letter labels together, so long poems show a false scheme.**
(`render()` src.html:469, letters from src.html:424)
After Z the letters become AA, AB, and so on, but the strip joins them with no gap. The Raven's last stanzas read
`AABABBBB AABACBBB ADBJBBB AEBAFBBB`. That looks like 8- and 7-line stanzas in a poem whose stanzas are all 6 lines.
Paul Revere's Ride has the same problem. Confirmed on `t-raven-end.png` (labels AD, AE, AF in the margin, from
`meters-out.json`).
Fix: separate the letters in each stanza group (A·B·AB) or start the letters again where the reader needs them.
Show the margin letter and the strip the same way. This is a narrow fix, but the readout is false as it stands.
Tag family:curiosity.

## Should fix

**S1. In Auto, a poem's meter name changes from line to line.** (`scanLine` per line, src.html:361)
Every line takes its own closest foot. The Road Not Taken, an iambic tetrameter poem, names 9 different meters in
20 lines, and "dactylic trimeter" (6 lines) beats "iambic tetrameter" (4) (`t-road.png`, `meters-out.json`).
Ozymandias puts 4 of 14 lines in "dactylic 3.3 feet". The Meter lens dial fixes this, but a student never learns
that from the screen. When a poem is loaded or has 3 or more lines, judge each line against the poem's best foot
by default and show the line's own closest foot only where it really differs. "Poets vary meter on purpose" is
then something the student can see.
Tag family:curiosity.

**S2. Common words outside the dictionary get stress on the first syllable, which breaks shelf lines.**
(`variants()` src.html:339-347)
The guess always stresses syllable 1. "unconquerable" (Invictus) comes out /xxxx, and the line falls to
"anapestic 2.7 feet". Many of the shelf's unknown words are made of known parts: hyphenated compounds (pea-green,
five-pound, high-born, hoof-beats, to-night, farm-yard, belfry-tower), possessives (bosom's, demon's, cushion's,
sentinel's, belfry's) and old -'d endings (mock'd, stamp'd, dimm'd, untrimm'd). Paul Revere's Ride has 21. Look up
the hyphenated parts separately, drop the 's, and read -'d as the -ed word minus a syllable. Real coinages like
brillig can stay as guesses.
Tag family:curiosity.

**S3. Names come out stressed on both syllables, which hurts Things to do item 1, "type your name".**
CMU gives many names a secondary stress on the final vowel (`cory K AO1 R IY2`, `kylie ... IY2`,
`aiden EY2 D EH1 N`, `jeremy ... IY2`; 552 entries end in `IY2`). The tool counts secondary stress as strong, so
"Cory", "Kylie" and "Aiden" each show `/ /` (`t-name.png`). A student testing the tool's first suggestion gets a
wrong answer about their own name. Count a word-final `IY2` in a two-syllable word as weak, or draw secondary
stress as a half mark.
Tag family:curiosity.

**S4. The pronunciation readout has no key.** (drawer head `#phones`, src.html:603; Manual)
The drawer shows "HH IY1 R" and "R EH1 K ER0 D · / x · 2/3". The Manual never says what the letters stand for,
what the digits 0, 1 and 2 mean, or what "2/3" counts (I grepped the Manual for any key to these symbols). The
Manual's own facts lean on the symbols too ("tea has IY, obey has EY"). Add a short key: digits mean stress
(1 main, 2 second, 0 none), a small table of the vowel symbols with example words, and "2/3 = pronunciation 2 of
3". Label the "2/3" on screen.
Tag family:curiosity.

**S5. The Sounds key shades nearly every word, so the Raven's inner rhymes can't be found.** (src.html:474-485;
Things to do 8)
The assonance shading counts the stressed vowels of free function words too, and uses one colour for every
repeated vowel. In the Raven's first lines almost every word is shaded, and dreary/weary or napping/tapping look the
same as "upon", "of" and "volume" (`t-sounds-raven.png`). RL.7.4's sound work ("analyze the impact of rhymes and
other repetitions of sounds") needs the student to see which sounds repeat. Leave free syllables out, give each
repeated vowel its own ink, and mark rhymes inside a line (same perfect-rhyme key) separately. The spec's "find
the rhymes hiding inside its lines" then becomes something the tool can show.
Tag family:curiosity.

**S6. RL.7.5's "form contributes to meaning" is shown but not linked to meaning, and RL.7.4's word-meaning half
isn't exercised.** (module ela-7-sound-and-form-in-poetry: RL.7.4, RL.7.5)
The student can see form: rhyme scheme, stanza breaks, line lengths, sonnet paper. Nothing on the desk or in the
Manual connects a form to what the poem means. "Its final two lines repeat" (src.html:839) stops short of saying
why. The cheapest fix inside the Curiosity shape is a few "Things people have found" entries that join the two,
plus one form question in notes "Talk together":
- Frost's repeated last line;
- the short "In Flanders fields." refrain line;
- Sonnet 18's closing couplet turning to "So long lives this";
- "Nevermore" ending every Raven stanza.
RL.7.4's figurative and connotative word-meaning half isn't touched anywhere. That suits a second card, but
Poetry Soundboard, the module's lesson card, is still only a concept. The integrator should make sure notes.md
"What it teaches" says "the sound half of RL.7.4", and should log that the module's word-meaning half has no
built tool yet (rule 2).
Tag general.

**S7. The source texts have stray marks left from the dash clean-up.** (material.json poems)
- The Raven, line 26: "here I opened wide the door:," (the original has a semicolon and a dash).
- Annabel Lee, line 37: "Of the beautiful ANNABEL LEE:,".
Turning a dash into a comma after a colon left ":," in a public-domain text the Manual calls checked. Use one mark.
Tag family:curiosity.

## Polish

**P1. The "N of M" match count counts free syllables as matches.** (src.html:408)
Free one-syllable function words always take the expected mark, so they always "match". "I hear the rain" reads
4 of 4, and a line of nothing but function words would score full marks. Better: "6 of 6 fixed · 2 free", or count
only fixed syllables.

**P2. The Manual's wording is above grade 7.** Examples: "The lens compares a foot at each starting offset",
"Primary and secondary stresses both count as strong", "rather than a universal account of speech",
"free one-syllable words follow the nearest pattern" (src.html:804-836). Better is plain sentences with an example
word each, such as "Small words like *the* and *of* can go either way, so they're grey and take whatever beat
fits."

**P3. Content notes sit under a builder-style heading.** notes.md lists the shelf's sensitive content (death, grief,
war, religious imagery, Hughes) under "Review care points", mixed in with layout notes ("44-pixel Stress key"). Rule
8 is met, but a teacher would look for a "Content notes" line in Good to know (BASELINE, parent-preview call). Move
it there and drop the build notes.

## Nit

**N1. Unlabelled pronunciation index, and rhymes that only match an unstressed form.** The "1/1" at the end of the
drawer readout has no label (see S4). Also, "the" (`DH IY0`) appears high in "tea"'s perfect rhymes and "a" in
"obey"'s, because a word with no stressed vowel falls back to its first vowel. Leave unstressed-only forms out of
perfect rhymes.

## Done when (teaching view)

1. Frost scanned on open, scans as you type: PASS (`t-frost.png`, `t-name.png`).
2. 8 syllables, iambic tetrameter: PASS (`facts-out.json`: 8, "iambic tetrameter", 8 of 8).
3. "orange" 0 perfect plus slant lists; "hot" shows lot, not, spot: PASS (orange: 0 perfect, Same vowel and Same
   ending filled; hot: 154 perfect including lot, not, spot, forgot).
4. "record" steps through 3 pronunciations: PASS (3 variants; "I will record a record" scans x/ then /x,
   `t-record.png`).
5. Dickinson 8, 6, 8, 6: PASS. Frost AABA BBCB CCDC DDDD: **FAIL** (shows AABA CCDC DDED EEEE; see B1).
6. Jabberwocky's invented words are dotted, with guessed counts: PASS (25 unknown words, all coinages).
7 to 10: Play and Craft lenses. 11: no score, goal, level or finish in the code or on screen: PASS from this lens.

## Facts spot-checked against a second source

1. The Rape of the Lock pairs obey/Tea (Canto III) and away/Tea (Canto I): confirmed in the Gutenberg 9800 text.
2. Gutenberg 1568 is Henley's *Poems* (holds Invictus): confirmed on gutenberg.org.
3. Gutenberg 74745 is Hughes, *The Weary Blues*, Knopf 1926 (so public domain in the US): confirmed.
4. Gutenberg 29345 is Frost, *Mountain Interval* (The Road Not Taken): confirmed.
5. Record has 3 CMU pronunciations, 2 with the beat second and 1 with it first: confirmed in cmudict.dict.
6. "ourselves" has 2- and 3-syllable forms: confirmed (`AA0 R S EH1 L V Z`, `AW0 ER0 S EH1 L V Z`).
7. Orange and month have 0 perfect rhymes: confirmed in the tool, and no `AO1 R AH0 N JH` or `AH1 N TH` match was
   found.
8. Stopping by Woods text, and its conventional AABA BBCB CCDC DDDD with a repeated last line: matches the 1923
   text.
9. Invictus text matches the standard text word for word ("Finds, and shall find, me unafraid"; "how strait the
   gate").
10. In Flanders Fields and Sympathy texts match the standard texts. Dickinson's 1890 text has 5 stanzas without
    "Or rather, he passed us", as the Manual says ("differs from modern editions").
11. Poe on The Raven: trochaic, octameter lines with a syllable dropped, ending on a shorter line. The Manual's
    summary is accurate.
Errors found: only B1's explanation and S7's two stray marks.

## Sensitivity

The shelf has death, grief, war (In Flanders Fields), Hughes's "Dream Variations" (Black identity) and Dunbar's
"Sympathy". Cory settled on 2026-11-05 that no poem on the shelf needs a sensitivity review (spec, Open
questions). I flag them as the brief asks but don't judge them. One thing for whoever looks: the function-word rule
marks "me" weak in Hughes's closing "Dark like me" / "Black like me", the poem's key word. The student can flip it,
but the default reading undersells it.

## Audit pilot

- Leads confirmed: the shelf's last books (Paul Revere, Flanders, Jabberwocky, Invictus) are below the fold at
  1366x768 (`t-frost.png`). That's a layout matter for Play and Craft.
- Leads that are wrong or expected: the #editor / #hint overlap and focus on load are intended (the hint sits on
  the page and the caret waits on the empty line). "Beat tempo knob: nothing changed" is expected, because a plain
  click doesn't turn it (keys and drag do). "Print: nothing changed" is the print dialog in headless Chrome.
- Missed (outside what it can see): B1 to B3, S1 to S7. All are about what the readouts teach. Its clean rows
  ("nothing runs forever", no exceptions on resize) hold for the frames I took.
