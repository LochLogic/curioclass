FAIL

# Sensitivity review: music-history-radio

Fresh, cold sensitivity agent (BASELINE rule 5: facts stay plain, with the human side). Read REFINE.md, STANDARDS.md,
BASELINE.md, spec.md, src.html (STATIONS data, L lines, ALTS, panel and Mystery code), notes.md, voice/lines.json,
art/prompts.json, and looked at all 12 shipped postcards plus the radio, knob and room art. Facts checked from what I
know of Britannica, Grove-level and Smithsonian accounts; where I am unsure I say so.

What holds up well: every American station names its Black (and for hip hop and disco, Latino; for disco, gay) origins
plainly in the student-facing row, not just in notes. Dates and names for chant, Guido, Petrucci (Odhecaton, Venice
1501), the Brandenburg dedication (1721), K. 545 (1788) with Alberti bass, Babcock's 1825 iron frame, Maple Leaf Rag
(1899), Goodman at Carnegie Hall (January 1938, Henderson arrangements, integrated band), RCA's 45 (1949) and Kool
Herc's 1973 Bronx party are correct. No slurs, no caricature sounds, no minstrel or "jungle" framing, no dialect. The
hip hop station correctly says it plays the beat only. Teacher notes say the path is selected, not a world history.

Counts: 1 blocker, 4 should fix, 5 polish, 2 nit.

## Blocker

1. **Gamelan is dated and scored as 1889 in Mystery and in the spoken ident.** family:music-history-radio
   - Where: src.html:474 (`"year": 1889`), src.html:1110-1111 (`ident-` and `result-` lines), src.html:1499-1511
     (newSet includes every station; reveal scores `gap = |guess - 1889|`), src.html:1320-1325 (result shows
     "Javanese gamelan · 1889"); voice/lines.json "1889. Javanese gamelan." and "It was 1889. Javanese gamelan."
   - What: the panel and notes say 1889 is "an encounter, not an origin", but Mystery treats 1889 as the answer. A
     student who hears bronze gongs and guesses 1500 (gamelan was played in Javanese courts long before) is told
     "389 years off", and the narrator says "It was 1889." The Dial ident also announces "1889. Javanese gamelan." the
     same way it announces "1900. Ragtime." as a style's date.
   - Why: this teaches the exact thing the notes warn against: that a living Indonesian tradition dates from the
     moment Europeans heard it. It erases its age and centers the colonial viewer. The tool contradicts itself.
   - How seen: read reveal() and newSet() code and the generated lines.
   - Better: leave gamelan out of Mystery rounds (or score it as "any year: a living tradition, centuries old" with
     no gap), and change the ident and result lines to something like "Javanese gamelan. A living tradition, heard in
     Paris in 1889."

## Should fix

2. **The 1889 Paris "encounter" is softened; the colonial setting is unnamed.** general
   - Where: src.html:481 (How it traveled row), src.html:1303 ("Paris encounter, 1889"), notes.md:221-230.
   - What: "Sundanese and Javanese artists performed in Paris in 1889; an encounter" leaves out that they were shown
     in a Dutch colonial exhibit (the "Javanese village" at the 1889 Exposition Universelle), Java then being a Dutch
     colony. Notes only touch it through a source title ("colonial encounters").
   - Why: rule 5 says facts stay plain. "Encounter" reads as an equal meeting; it was a colonial display of people.
     Naming it, with care, is the human side.
   - Better: row: "A living tradition, taught by ear in courts and villages. In 1889 Sundanese and Javanese musicians
     played in Paris at a Dutch colonial exhibit at the world's fair." Teacher notes: one plain sentence on the
     exhibit, and that Debussy heard them there.

3. **Gamelan's only "How it traveled" line is about Europe, and the dial seats it in the European-American sequence.**
   family:music-history-radio
   - Where: src.html:472-488 (station sits between Romantic and Ragtime in STATIONS), src.html:1307-1313 ("changed"
     tags compare each station with the previous one).
   - What: every other station's row says how the music moved among its own people (manuscripts, printing, sheet
     music, 45s, mixtapes). Gamelan's row spends its words on Paris. On the Dial, Ragtime's rows are tagged
     "changed" relative to gamelan, as if ragtime followed from it.
   - Why: notes.md:224 says gamelan is not "a stage between Romantic music and ragtime", but the dial order and the
     changed tags present it as one.
   - Better: give the row its own transmission (learned by ear and by playing together; court and village
     ensembles; a cipher notation, kepatihan, came into use around 1900 in Surakarta, though check that date before
     using it), and skip the "changed" comparison into and out of gamelan, or mark the station on the dial as a
     side station (a different mark style).

4. **Swing names only a white bandleader as the headline; Black creators of swing are unnamed.** general
   - Where: src.html:517, voice/lines.json (same line).
   - What: "African American jazz; ... Goodman's integrated 1938 concert used Henderson's arrangements." The only
     people named are Benny Goodman and "Henderson", and the row does not say Fletcher Henderson was a Black
     bandleader whose band and arrangements built the style Goodman made famous. No Black swing band (Ellington,
     Basie, Chick Webb) or Harlem's Savoy Ballroom appears.
   - Why: compare rock and roll, where Black artists are named directly. Here the line still reads, to a student,
     as "swing = Goodman", the "King of Swing" framing the tool means to avoid.
   - Better: "Built by Black bands such as Fletcher Henderson's, Count Basie's and Duke Ellington's; records, radio
     and dance halls like Harlem's Savoy. Goodman's integrated 1938 Carnegie Hall concert used Henderson's
     arrangements." (Trim to fit.)

5. **The hip hop postcard is the only image with people, and they are the Black and Latino youth of the one Black-
   created station shown at a party.** family:music-history-radio
   - Where: art/mhr-pc-hiphop.webp; art/prompts.json (mhr-pc-hiphop, `people: true`, redrawn); src.html:1136 (alt).
     spec.md:94 and :98 say no people, empty quiet places.
   - What: the picture itself is respectful (a woman DJ at work, neighbors of varied builds, a wheelchair user, no
     caricature). But ten European and American stations are elegant empty rooms and objects, and the one station
     whose people are drawn is the hip hop crowd dancing.
   - Why: the asymmetry (European music as refined spaces, Black music as bodies at a party) is a long-standing
     stereotype pattern, even when each image is fine on its own. A teacher could notice it.
   - Better: either match the set (turntables, sampler and speaker stack at an empty Bronx block party at dusk, as
     the spec had it), or keep people and make it deliberate and named: tie the woman DJ to the text by crediting
     Cindy Campbell, who organized the 1973 party with her brother Kool Herc. If people stay, say so in the notes.

## Polish

6. **Perotin's Viderunt omnes "was sung at Christmas 1198" is stated as certain.** general
   - Where: src.html:391, voice lines. Bishop Odo of Sully's 1198 decree allows organum triplum or quadruplum at
     Christmas; that Viderunt omnes was the piece is a strong scholarly inference, usually written "probably". Better:
     "was probably sung at Christmas 1198."

7. **Rock and roll lists Sister Rosetta Tharpe under "rhythm and blues roots".** general
   - Where: src.html:535. Tharpe came from gospel; she is usually credited as a gospel guitarist and a founding figure
     of rock and roll, not an R&B artist. Better: "Black gospel and rhythm and blues roots: Tharpe, Berry, Little
     Richard; ..." Also use first names once (Sister Rosetta Tharpe, Chuck Berry) so students can look them up.

8. **Ragtime and hip hop rows could name their people as fully as rock and roll does.** general
   - Where: src.html:499 and :571. "Joplin's Maple Leaf Rag" does not say who Joplin was; better "Black composer
     Scott Joplin's Maple Leaf Rag (1899)". Hip hop: Kool Herc was born in Jamaica and brought sound-system practice
     with him; "Black, Latino and Caribbean youth in the Bronx" or "Jamaican-born DJ Kool Herc" is more exact.

9. **The gamelan postcard leans on Balinese imagery for a "Javanese" station.** family:music-history-radio
   - Where: art/mhr-pc-gamelan.webp. Split candi bentar gates, shrine-like towers and a volcano beyond are the
     standard tourist picture of Bali. Split gates also exist in East Java, so this is not plainly wrong (I am not
     certain), but together they read as "generic Indonesia". Better: a Central Javanese pendopo with a joglo roof,
     plain tiled floor, no temple gates; or drop the background landscape.

10. **The rock and roll and swing postcards picture white-coded spaces.** general
    - Where: art/mhr-pc-rocknroll.webp (seaside diner with palm trees, the 1950s nostalgia look), art/mhr-pc-swing.webp
      (hotel ballroom with tablecloths). Neither is wrong, but both point at where the music was later sold rather than
      where its makers played it. Better: a jukebox in a neighborhood juke joint or a radio DJ booth; a Harlem
      ballroom bandstand (Savoy-style, long sprung floor). Low priority.

## Nit

11. **"Staff lines came about 1025" slightly overstates Guido.** general
    - Where: src.html:373. Scribes used one or two lines before Guido; his contribution (about 1025) was the
      systematic staff with lines and spaces in thirds and his teaching method. Better: "Guido of Arezzo's staff, about
      1025, fixed the pitches."

12. **Teacher-note phrasing "These are musical-history contexts, not scored identities" is unclear.** general
    - Where: notes.md:218. It seems to mean students are not graded on identities; say that plainly or cut it.
