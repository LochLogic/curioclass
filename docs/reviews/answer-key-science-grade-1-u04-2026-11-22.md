# Answer-key read: science-grade-1 unit 4 checks (2026-11-22)

Kind: answer-key. Target: science-grade-1-u04, the check, mid and end items (not exit, not practice). Course finish, COURSE-RUN stage 7. Read-only: this report is the only file written.

## What I studied

- The items themselves, solved cold. Scope from data/plans/science-grade-1/items.csv, stretch 4, check not exit and not practice: two items, s04-E33a and s04-E33b (both end, day 33, 1-PS4-1). There are no mid or check rows in unit 4.
- Honesty note: my filter script printed each row whole, so the key column came up on screen in the same read as the stem. I wrote my own answers below from the stem and the unit plan's goal before comparing, but they were not fully blind.
- docs/courses/science-grade-1/s04.md: the 1-PS4-1 goal (vibrating things make sound, and sound makes things vibrate), the day 33 assessment row, the collection plan and the supplies and safety list.
- courses/science-grade-1/u04-2/d033.md, cards-day33.md (the held-back records), sheet-two-panel.md, and cards-motion-sequence.md (how the day 32 record cards show motion, for comparison).
- data/plans/science-grade-1/wrongs.csv rows for s04-E33a and s04-E33b.

## My cold answers

- **s04-E33a (ruler beside a paper drum, which part sounds?).** Flick the ruler with the drum away, and tap the drum alone. Then flick the ruler and still its free end (or still the drum with a hand while flicking). If the sound stops when the ruler is stilled and goes on when the drum is stilled, the ruler is the source. This keeps the arrow "it shakes, so it sounds."
- **s04-E33b (ribbon near a playing speaker, why might it move?).** Other causes: the table shaking it, a draft or a breath, a hand. Put the ribbon on its own support apart from the table, keep hands and breath away, and compare sound off with sound on. Only if it moves with sound on and not off do we add "it sounds, so it makes things shake." A trial with no motion is still a result.

Both match the key in substance. No key errors in the science.

## Verdict

Pass with fixes. Both keys are sound science, fit 1-PS4-1 and the plan's day 33 goal, and the wrong answers carry the right A, B and C letters; but the item 1 held-back record cards, as written, cannot show sound, so the waiting groups cannot get from the picture what the key asks them to observe.

## Findings

### 1. Item 1 records cannot show the observation the key needs (item ambiguous; worst)

cards-day33.md, item 1: "plain black line drawings on white, thick lines, no shading ... no result written on any card", with cards "ruler flicked alone", "drum tapped alone", "equal ruler flicks with the free end free" and "... gently held". The key for s04-E33a rests on hearing: "sounds when free and is much quieter when held, and the drum makes no sound unless it is tapped." A still line drawing of a ruler shows no sound. Groups 2, 4 and 6 do item 1 from these cards only, and it is scored from their panel. The day 32 motion cards solve this for motion with dated frames; nothing solves it for sound.

Fix (cards-day33.md, item 1 paragraph): add "Each item 1 card is a three-frame record like the motion sequence cards: before, during and after, each frame dated. The during frame shows what the adult observed: the ruler's free end drawn blurred when it moved, and a heard mark (three short curved lines by the ear of a drawn listener) when a sound was heard, a small heard mark when it was quieter, and no mark when nothing was heard. The mark records what was heard; it names no cause." If a heard mark is judged to give away the result, the fallback is a short audio recording played at classroom level, which the room-with-nothing path would then need too.

### 2. "Flicks with the free end gently held" reads as flicking a held end (item ambiguous)

s04-E33a answer: "equal ruler flicks with its free end free and then gently held"; steps: "equal flicks free and gently held"; cards-day33.md: "equal ruler flicks with the free end gently held". A child or teacher can read this as pressing the end down and then trying to flick it, which is not the stopping test of day 31 (flick, then still the vibrating end). Fix, in the answer, steps, card and d033.md at-home line: "equal flicks, one left to ring and one gently stilled by a fingertip on the free end right after the flick."

### 3. A fair alternative comparison is not named (item ambiguous)

s04-E33a steps: "chooses a comparison with a stated observation: ruler alone and drum alone, or equal flicks free and gently held". A child who asks for the drum to be gently stilled with a hand while the ruler is flicked has a sound plan for "which part is sounding", the same stopping logic applied to the other part. As written a strict marker could leave that step at "not yet seen". Fix, append to that step: ", or the drum gently stilled while the ruler is flicked". (Live groups can do this; the record set has no card for it, which is fine, since the card set need not hold every plan.)

### 4. The key's last sentence is garbled (key wording)

s04-E33a answer: "Say only what the records show; if the ruler pair agrees with the band and the drum, the arrow it shakes, so it sounds, is kept." Fix: "Say only what the records show. If the ruler's free and stilled trials agree with the band and drum records from days 29 to 31, keep the arrow \"it shakes, so it sounds.\""

### 5. The drum claim in the key is stronger than the evidence (key wording, small)

s04-E33a answer: "the drum makes no sound unless it is tapped." A paper drum beside a sounding ruler can buzz a little from the ruler's sound, which is the very second arrow of this unit. A child who says "the drum shook a bit too" from a real observation should not be marked down. Fix: "the drum alone, untapped, makes no sound of its own (a faint buzz while the ruler sounds is the other arrow, and is a fair observation)."

### 6. Missing common wrong answer (wrongs.csv, small)

s04-E33a has no row for the likeliest wrong idea, that the drum makes the sound because drums make sound. Add a row: item_id s04-E33a, shown "The drum makes the sound, because it is a drum.", error x, note "a reason about what a thing is, not what was seen; shown with help" (matching the s04-X28b wall row).

### 7. Double-naming in the key (key wording, small)

s04-E33a answer: "Ask for the ruler alone and the drum alone, a separate gentle drum tap as a comparison". The record set has one drum card, "drum tapped alone"; "the drum alone" and "a separate gentle drum tap" read as two trials. Fix: "Ask for the ruler flicked alone and the drum tapped gently alone".

### s04-E33b: no changes needed

Stem, key, steps and records agree. The records include the shared-table trial, the separate-support off and on trials and the hand-pressing trial, so the confounds the key names can be chosen or rejected from the cards. The key's "A trial with no clear motion is a result" correctly guards against inventing success. Wrongs rows B, C and the unclassified shared-table answer match the plan's day 33 row. It tests the second half of 1-PS4-1 (sound makes things vibrate) and the planning practice, as the plan says.

## Gate

Filtered plan.py check: science-grade-1, 240 items and 369 wrong answers checked, 13 failures, all of the form "section N.N (science-grade-1-uNN-N) is not in data/units.csv" (one per section, including 4.1 and 4.2). None is an item or key failure; they are outside this read.

## Could not settle

- Whether a drawn heard mark on the item 1 cards counts as "a result written on the card". It records an observation, not a cause, so I think it is allowed; the lead decides, and if not, item 1's record path needs audio.

## Fixes applied (2026-11-22)

1. Item 1 records: applied. cards-day33.md: each item 1 card is a dated three-frame record with a printed heard mark and a key strip; item 2 cards are dated three-frame records with sound on or off labels; a hand-drawn paper fallback from real trials the adult runs before day 33. d028 and d033 Before class name it. Could not settle: taken as allowed, since the heard mark records an observation and names no cause.
2. "gently held": applied. Answer, step, card and d033 At home say one flick left to ring and one gently stilled by a fingertip right after the flick.
3. Drum stilled: applied. Added to the comparison step.
4. Garbled key sentence: applied.
5. Drum claim: applied. The untapped drum makes no sound of its own; a faint buzz is a fair observation.
6. Drum wrongs row: applied. New s04-E33a row, error x.
7. Double-naming: applied. "the ruler flicked alone and the drum tapped gently alone".
