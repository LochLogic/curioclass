# Teaching lens: music-history-radio (round 1)

Counts: blockers 0, should fix 5, polish 8, nit 4

Fresh, cold read of spec.md, src.html, notes.md, handoff.md, tool.draft.json, audit-states.json, and the shared
audit (audit-r1/audit.md plus its frames). I did not read codex-report.md, codex-review.md,
sensitivity-pre-refine.md or refine/sensitivity.md. Music checks were made from the event logs, not by ear: I pulled
`compileBar` out of src.html into Node (scratch `teaching/cb.js`, `check.js`, `check2.js`, `check3.js`) and listed
every station's events, intervals and timings. All audio in the audit was muted, so nothing here is certified by
ear.

## Standards (rule 2)

Module arts-9-12-music-history lists MU:Cn11 and MU:Re7 (anchor codes; data/modules.csv line 225).

- **MU:Re7 (perceive and analyze; how structure and context shape a response): taught.** Dial plus Compare/Flip
  holds the melody fixed and switches one era for another at the bar line, and Mystery asks for an estimate from
  sound alone, then points at the two rows that should have given it away. That is analysis by doing. It covers the
  7.2 (analyze) side; nothing asks the student to select music for a purpose (7.1), which is fine for an anchor
  code but the teacher note could say "analysis" rather than the whole anchor.
- **MU:Cn11 (relate music to its history and context): taught, but thinner.** The student places each sound in
  time on the true-time strip, which is a real context act. The "How it traveled" row, though, is read-only: the
  masked prompt "What setting might carry this music?" asks a question the student has no way to answer (see
  polish P5). Not a should fix: placing a sound in history by ear does the job.

## Done when

| # | Check | Result |
|---|---|---|
| 1 | All stations play the whole tune recognizably, rules as written | Pass by event log: every one of the 12 stations plays all 24 melody notes in order; chant and organum map the degrees onto D Dorian, contour kept. Not checked by ear. Arrangement details mostly match the spec; mismatches are S2, P1 to P4. |
| 2 | Static by signal strength; eye closes only when locked | Pass by code: strength = 1 minus distance / 0.5, lock at 0.15 of the gap (strength 0.70). |
| 3 | Compare flips at the bar line; Flip off until B | Pass by code: Flip is disabled while `state.b` is null; the swap is queued and committed on the bar boundary. |
| 4 | Every desk mix compiles; panel names each row's era | Pass: 12 x 12 x 12 = 1728 mixes, 232,380 events, all finite (my run). The spec's "1331" is stale since the twelfth station; notes.md says 1,728 correctly. Rows name their era, but see P6. |
| 5 | Mystery: six rounds, gap, two giveaways, correct count, New set, nothing stored | Pass: shuffle then slice gives six different stations; frame state-complete-set-1366x768 shows six gaps (538, 200, 450, 500, 100, 556), all over 50, and "Within 50 years: 0 of 6" is right; no storage calls in src.html. See S3 and P7. |
| 6, 9, 10 | Focus, sizes, images | Play and Craft lenses; the audit's size rows are clean and the 1366x768 frames show the radio largest. |
| 7 | A tap changes the sound in the same frame | Pass by code: `tune()` restarts the station inside the same handler. |
| 8 | Idents once each over ducked music; no line names Flip while it is off | Pass by code (`V.how` per station; flipHow needs `#flip` and only queues once B exists). The audit's double-tap lead on Power (ident cut, never heard whole) is for Craft. |

## Findings

### Should fix

**S1. The "changed" tag is on every row of every station, including rows that did not change.**
Where: src.html:1313 (`renderPanel`), Dial mode. What: the tag compares the feature strings with the station
before, and no two consecutive stations share a string, so all 5 rows read CHANGED on all 11 stations after the
first (my check2.js). Organum's Instruments row ("Voices.") is tagged changed from Chant ("Voices only."), which is
false. The tag carries no information and sometimes says something untrue. How seen: frame
state-locked-second-1366x768 (five CHANGED tags on Notre Dame organum) and the string comparison. BUILD.md wave
lesson "The badge says what is true", so at least a should fix. Better: give each station an explicit
"changed from the previous station" list per row (organum: Texture, Rhythm, Harmony, How it traveled; not
Instruments), or drop the tag. Note the "previous" of Ragtime is now Gamelan (see S3). Tag: general.

**S2. Organum's Harmony row ("Open fifths and octaves") is not what the arrangement sounds like, and it is the
station's first Mystery giveaway.**
Where: src.html:390 (feature), 624 to 680 (`compileBar` organum timing and drone). What: interval of each long
(stressed) melody note above the held voice, from the event log: bar 1 D (octave), F (third); bar 2 B (sixth),
F (third, held a full 3/4 bar); bar 3 F, F (thirds); bar 4 E over A (fifth); bar 5 D, F; bar 6 B, B (sixths);
bar 7 A (fifth), then E over D held a full bar (a ninth, a held dissonance); bar 8 D (octave). Of 14 stressed notes,
5 are octaves or fifths, 8 are thirds or sixths and 1 is a held ninth. A student told to "listen for open fifths
and octaves" hears mostly thirds. The good news: every phrase starts and ends on an octave or fifth (bars 1, 4, 5,
8), which is the real Notre Dame habit. How seen: check.js output. Better: either re-voice the held note per bar
so stressed notes land on fifths and octaves (and fix bar 7's held ninth), or reword the row to what is there:
"Held low note; phrases begin and end on open fifths and octaves." Tag: general.

**S3. Mystery scores a guessed year for Javanese gamelan against 1889, which the tool itself says is not
gamelan's date.**
Where: src.html:1498 to 1517 (`newSet` draws from all 12 stations; `reveal` scores `|guess - 1889|`), lines
`result-gamelan` ("It was 1889. Javanese gamelan.") and the reveal heading "Javanese gamelan · 1889". What: the
Dial panel and notes say 1889 is "an encounter, not an origin", and a talk question asks why an encounter date
says little about a tradition's age. Mystery then asks the student to hear a year in the gamelan station and marks
them wrong by the distance from 1889; there is no audible evidence for that year, and the spoken reveal drops the
"encounter" qualifier. The task teaches the opposite of the note. How seen: code; the Dial frame
state-gamelan-context-1366x768 shows the careful wording that Mystery loses. Better: leave gamelan out of the
scored set (play it as a bonus round with no year, or reveal it as "Javanese gamelan, a living tradition; heard
in Paris in 1889" with no gap and not counted). Flag for the sensitivity agent too; I have not judged the
cultural side. Tag: general.

**S4. "How it might be written" shows the same plain rhythm for ragtime and organum that the rows say are
different.**
Where: src.html:1254 to 1280 (`notation`). What: every staff station draws the tune's four bars as straight
quarter and half notes in 4/4. Ragtime's Rhythm row and giveaway is "Syncopated", and the station plays the notes
on eighth positions 1, 2, 4 and 6, but the lead sheet shows no syncopation; ragtime's printed sheet music is
exactly where its syncopation was written. Organum plays long-short pairs in 3/4 (14 bars) over a held voice, but
its notation shows 4/4 bars of equal notes and no held voice. Spec: "the first four bars of the tune as written
for that era". How seen: frames state-complete-set-1366x768 (rock and roll lead sheet, same rhythm as baroque in
state-mystery-reveal-1366x768) and state-locked-second-1366x768 (organum). Better: draw ragtime with eighth-note
ties across the beat, organum as long-short pairs with the held note on a second line; swing written straight is
correct (that is the convention) and can stay. A treble clef on the five-line staves would also help, since the
notes sit at treble positions. Tag: general.

**S5. Key skills claims a step the tool does not have.**
Where: notes.md "Key skills": "Make a historical estimate, then revise it using revealed evidence." What: after
Tune in the guess is locked; there is no revise step. Rule: Key skills are true of this tool. Better: "Make a
historical estimate, then check it against the revealed evidence." Tag: general.

### Polish

**P1. Baroque's Harmony row says "Chords built on the bass", but no chords sound.**
Where: src.html:684 to 688. The continuo is the root in octaves (harpsichord) plus cello, under the tune: a
two-part texture. Accurate for Texture ("Tune over a busy bass line"), not for Harmony. Better: add a light
right-hand realization (the chord on beats 1 and 3) so the continuo really fills in chords, or reword to
"Harmony implied by the bass line". Tag: general.

**P2. Bar 2 holds E against an F major chord in Classical, Ragtime and Rock and roll.**
Where: src.html:664 to 666 (the C F C G C F G C progression replaces the tune's Am in bar 2). The tune's E is a
half note on beat 3, so a major seventh sounds for half a bar (event log: Classical bar 2 melody A G E over
F, C, A). For rock and roll it is the spec's progression; for Classical "Simple I, IV, V" it is not idiomatic.
Better: use C (I) in bar 2 for Classical and Ragtime (A and G become passing notes, E a chord tone). Tag: general.

**P3. The Renaissance 4-3 suspension sounds against its own resolution note.**
Where: src.html:715 and 721 to 724. The G chord (G3, B3, D4) is held all of bar 7 while the C5 suspension plays,
so B3 clashes with C5 (a minor ninth) before the resolution. "Careful dissonance" is the row's claim. Better: hold
G and D only for the first half of bar 7, add the B when the C falls. Tag: general.

**P4. Gamelan timing details.** The two gong strokes in every bar land at 2.32 s and 2.38 s of a 2.5 s bar,
0.12 to 0.18 s before the beat, so they sit off the beat grid; the upper elaborating layer starts 80 ms after
each tune note (a flam), not on a subdivision; the layer sketch draws the gongs at the start of each bar. Better:
put the gong on the cycle's final beat and the elaboration on half-beats. For the sensitivity agent as well; I
have not judged the cultural side. Tag: general.

**P5. The sealed Mystery panel asks five questions the student cannot answer.** "One line or several?",
"Free, steady, or syncopated?" and so on read like a form, but there is nothing to pick. Better: let the student
tick one choice in two rows (Rhythm and How it traveled, say) before Tune in, then show which matched; that turns
the "listen for evidence" frame into a justified estimate (Re7) and gives Cn11 an action. This adds to Mystery, so
it may belong in the spec's open questions. Tag: general.

**P6. Desk rows can contradict the sound.** Harmony on Chant with a drum Beat (disco, rock) reads "Texture. Chant:
one melody without accompaniment" while the kick and hats play (check3.js: layers melody plus drums). Beat on
Chant with Rock and roll Harmony reads "Follows the words, no beat" while the boogie bass pulses in even eighths.
Better: when Beat has drums, the solo texture line says "one melody with drums"; when Beat is Chant, an
accompaniment that pulses is labeled as such. Tag: general.

**P7. "Within 50 years" rewards modern guesses more than listening.** A fixed guess of 1930, without listening,
is within 50 years of 5 of the 12 stations (1889, 1900, 1938, 1956, 1978): 2.5 of 6 expected. Chant, organum and
Renaissance each need a guess inside a 100-year window in 1200 years. Better: show a second line in the recap,
"nearest station: right / wrong" (or count a guess on the nearest pin as right), so the score measures hearing the
era, not the crowding of the 1900s. Tag: general.

**P8. Chant's Rhythm row says "Follows the words", but no words are sung (the choir sings "ah").** Better:
"Free, unmeasured; each phrase stretches at its end." Tag: general.

### Nit

**N1.** Organum, How it traveled: "Perotin's four-voice Viderunt omnes was sung at Christmas 1198." The date comes
from inference from the Paris bishop's 1198 and 1199 decrees; "is thought to have been sung" is safer.

**N2.** Classical: "Balanced four-bar phrases" is true of every station (same tune), so it is not a Classical
clue; the Alberti bass note sits in the How it traveled row rather than Texture or Harmony.

**N3.** Hip hop's sample loop uses C and Am under bars 1 and 2, while the Classical station's bar 2 is on F; the
spec says the loop is "Bars 1 and 2 of the Classical station". Either match them or say "a Classical-style loop".

**N4.** Small arranging details: ragtime's "passing chords" are one chromatic note a half step under the current
root; swing's brass stabs sit on the straight "and" (1.5 beats) rather than the swung one (1.67); the walking bass's
fourth note approaches the current root, not the next bar's.

## Other checks

- **Facts:** dates and names on screen match the spec's Sources (Guido about 1025, Odhecaton 1501, Brandenburgs
  1721, K. 545 1788, Babcock 1825, Maple Leaf Rag 1899, Carnegie Hall 1938, 45 rpm 1949, Kool Herc 1973). Numbers
  recomputed: loop lengths swing 13.600 s, disco 17.000 s, hip hop 22.174 s, organum 24.444 s (14 bars of 3/4),
  chant 17.46 s; all under 30 s. Ragtime detune 1.004632 = 8.0 cents. Swing chords C6, Am7, Em7, G7, C6, F6, G7,
  C6 and disco Cmaj7, Am7, Em7, G7, Cmaj7, Fmaj7, G7, Cmaj7 match the lead-sheet labels. Romantic Am7, A7, D7 to G7
  and the 0.75 / 1.1 tempo scales match the spec. Hip hop kick on 1 and the "and" of 2, snare 2 and 4, and the
  pad grid match. Time strip end labels 800 / 1200 / 1600 / 2000 sit at true thirds.
- **Giveaways in Mystery:** cover, postcard, panel, notation, needle, knob, tuner, idents and Read are all sealed
  (`identify` returns in Mystery; Read gives the hint only). The strip shows ticks at all 12 station years, so the
  student is picking among 12 known years; that is fair, not a leak.
- **Language and notes:** plain and right for grades 9-12; "monophony" is glossed. Support at home ideas are
  doable tonight. No topics in these standards need a rule 8 teacher note. Guardrails: no hard-history scoring
  issues apart from S3.
- **For the sensitivity agent (not judged here):** gamelan sits between Romantic and Ragtime on the dial as
  "Station 07 / 12", and the changed tags (S1) compare Ragtime with Gamelan, which reads as a sequence the notes say
  is not intended; the hip hop postcard is people art; S3 and P4.

## Audit pilot

- **Leads confirmed:** none of the four leads is a teaching fault. "Welcome not heard after the first tap on
  Power": confirmed by code, and expected (the welcome is valid only while the radio is off; Power speaks the
  station ident instead). "Welcome not heard after the first tap on Compare": confirmed by code, expected (Compare
  before Power speaks the Power instruction). "Reset: nothing changed": confirmed, expected (Reset at the starting
  Baroque mix has nothing to undo). "Power double tap cuts the ident and it is never heard whole": plausible from
  code (the ident counts as heard once it starts); it is a voice item for Craft, and the name stays on screen.
- **Leads that were wrong:** none outright; the three above are expected behavior rather than faults.
- **What it missed (by design, it cannot see these):** the changed tag on every row (S1), the organum harmony
  claim against its intervals (S2), gamelan scored against an encounter year (S3), notation rhythm that
  contradicts the rows (S4), Key skills wording (S5), and the arranging and desk-row mismatches (P1 to P4, P6).
  None are visible in a frame without reading the music. The size, state, Motion-off and resize rows were clean
  and I cited them rather than re-shooting; I looked at state-locked-second, state-mystery-covered,
  state-mystery-reveal, state-complete-set, state-desk-extreme and state-gamelan-context at 1366x768.
