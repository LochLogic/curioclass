OPEN (round 1 merged 2026-11-04, polish not started; sensitivity FAIL)
Counts: blockers 1 (general 1, family 0), should fix 14 (general 10, family 4), polish accepted 18

# Refine: music-history-radio (round 2026-11-04)

Lenses: refine/teaching.md, refine/play.md, refine/craft.md, refine/sensitivity.md (rule 5 applies: FAIL). Shared
audit: 4 leads. Measure-first run: no lens read codex-report.md, codex-review.md or sensitivity-pre-refine.md (the
earlier sensitivity note, kept in the tool folder). The re-check needs the sensitivity agent's PASS.

## Blocker

1. **Mystery scores Javanese gamelan against 1889**, and the ident and result say "1889. Javanese gamelan." / "It was
   1889.", dating a centuries-old living tradition from the year Europeans heard it, against the tool's own
   "encounter, not an origin". Leave gamelan out of scored Mystery sets (or a no-year bonus round), and voice it as
   "Javanese gamelan. A living tradition, heard in Paris in 1889." on the dial, strip and result heading.
   (Sensitivity 1, Teaching S3, Play 7, Craft 3) general

## Should fix

2. **No how line is spoken once Power is on** (the main path): compareHow, flipHow, dialReady, deskHow and
   mysteryHow never play; Power first leaves the tuning how-to unspoken. Speak each mode's how line once over the
   ducked music, as the idents do, keeping its `valid`. (Play 1, Craft 1) general
3. **Power-state lines are wrong for the mode**: powerHow names "the controls below the radio" in Mystery (the pin is
   above) and is used up by whichever mode comes first; flipHow plays with the radio off ("at the next bar"). Each
   mode its own Power line (deskPower and mysteryPower hints exist); flipHow only once playing. (Play 2, Play 9,
   Craft 2) general
4. **Spinning the dial uses up every ident** (each starts and is cut after about 300 ms, then marked heard). Queue an
   ident only after the lock has held about 400 to 500 ms. (Play 3, Craft 7) general
5. **Wobbling at the lock edge restarts the tune at bar 1 over and over** (20 restarts in under a second). Restart only
   on a new station or after the signal was lost a while. (Play 4) family:music-studio
6. **Stations differ by up to 14 dB, and the static is louder than eight of them**: per-station trims to within about
   3 dB, static a few dB under the average station. (Play 5) family:music-studio
7. **The "changed" tag is on all five rows of every station**, including organum's unchanged Voices, and makes Ragtime
   "changed from" Gamelan. Explicit per-row change lists (or drop the tag) and no comparison into or out of gamelan.
   (Teaching S1, Play 6, Sensitivity 3 part) general
8. **Organum's Harmony row "Open fifths and octaves"** vs the arrangement: 8 of 14 stressed notes are thirds or sixths,
   bar 7 holds a ninth. Re-voice so stressed notes land on fifths and octaves, or reword to "phrases begin and end on
   open fifths and octaves". (Teaching S2) general
9. **"How it might be written" shows the same plain rhythm for every staff station**: ragtime's syncopation and
   organum's long-short 3/4 pairs and held voice are not drawn; add a treble clef. (Teaching S4) general
10. **Key skills claims a revise step the tool lacks**: "then check it against the revealed evidence". (Teaching S5)
    general
11. **Mixing desk knobs are unusable with a mouse** (12 eras in 54 px): the tuning knob's drag (32 px per step) or
    small arrow buttons beside each era, and say arrow keys work. (Play 8) general
12. **The 1889 Paris colonial setting is unnamed**: say the musicians were shown at a Dutch colonial exhibit at the
    world's fair (row and one notes sentence, with Debussy). (Sensitivity 2) general
13. **Gamelan's "How it traveled" row is only about Europe** and the dial seats it in the European-American line: give
    it its own transmission (by ear, court and village ensembles; check any notation date) and mark it a side
    station. (Sensitivity 3) family:music-history-radio
14. **Swing headlines Goodman; Fletcher Henderson is not named as a Black bandleader** and no Black swing band
    appears: name Henderson's, Basie's and Ellington's bands and the Savoy. (Sensitivity 4) general
15. **The hip hop postcard is the only image with people** beside eleven empty rooms: match the set (empty Bronx block
    party gear at dusk, as the spec said) or keep people deliberately, credit Cindy Campbell, and say so in notes.
    (Sensitivity 5) family:music-history-radio

## Polish accepted

16. Baroque: a light continuo right hand, or "Harmony implied by the bass line". (Teaching P1)
17. Bar 2's E over F in Classical and Ragtime: use C (I) there. (Teaching P2)
18. Renaissance suspension: hold G and D only, add B when C falls. (Teaching P3)
19. Gamelan timing: gong on the cycle's final beat, elaboration on half-beats. (Teaching P4)
20. Desk rows that contradict the sound (Chant texture with drums; Chant beat under a pulsing bass). (Teaching P6)
21. "Within 50 years" can be farmed with a fixed 1930 guess: score by nearest station or half the neighbor gap.
    (Teaching P7, Play polish 2)
22. Chant Rhythm: "Free, unmeasured; each phrase stretches at its end." (Teaching P8)
23. Mystery reveal keeps the student's pin (dimmed) and draws the gap. (Play polish 1)
24. Dial labels scale with the radio at 1920x1080. (Play polish 3)
25. Hip hop pad grid cut off at 1366x768. (Play polish 4, Craft 5)
26. 760x900 reveal: scroll the clues into view or name them in the result line. (Play polish 5)
27. The needle covers the locked year and end years clip: lift the label, pad the scale. (Craft 4)
28. One-key shortcuts act anywhere (WCAG 2.1.4): stage focus only, or Shift. (Craft 6)
29. Organum: "was probably sung at Christmas 1198". (Sensitivity 6, Teaching N1)
30. Rock and roll: "Black gospel and rhythm and blues roots"; full names once (Sister Rosetta Tharpe, Chuck Berry).
    (Sensitivity 7)
31. Ragtime "Black composer Scott Joplin"; hip hop "Jamaican-born DJ Kool Herc" or "Black, Latino and Caribbean
    youth". (Sensitivity 8)
32. Gamelan postcard: a Central Javanese pendopo, not Balinese gates and shrines. (Sensitivity 9)
33. Swing and rock and roll postcards: where the makers played (Harlem ballroom bandstand; a juke joint or DJ booth).
    (Sensitivity 10)

## To the spec's open questions (not for the builder)

- Mystery: let the student tick one choice in two rows before Tune in, then show which matched? (Teaching P5)

## Nits (optional)

- Classical's "Balanced four-bar phrases" is true of every station (Teaching N2)
- Hip hop's loop harmony differs from the Classical bars it claims to sample (Teaching N3)
- Ragtime passing chords, swing stab placement, walking bass approach (Teaching N4)
- Needle on the tuned year (Play nit 1); Tune in works before Power (Play nit 2); 680x425 Power covers the dial edge
  (Play nit 3); a one-sample cut can click, use a 20 ms ramp (Play nit 4); Reset looks live at the start mix (Play
  nit 5)
- The dial window is a second Tab stop (Craft 8); idents differ from the spec's wording (Craft 9); dead `maker` code
  and overridden 7 to 9 px rules (Craft 10); flipHow "next bar" while paused (Craft 11); volume knob hidden in a
  covered round (Craft 12)
- Guido "fixed the pitches" (Sensitivity 11); unclear notes line "not scored identities" (Sensitivity 12)

## Settled calls

- Art: 15 tokens, all drawn by Codex, one people image marked. Words and contract clean. Every loop under 30 s.
