# Word Wall picture review: does the picture show the word?

Review of every Curio Class Word Wall card that has a published picture (3,633 of 4,413 cards; the other 779 are 9-12
cards with no picture by design, plus one people card not drawn yet). Local models only, nothing downloaded, nothing in
the cards, prompts, pictures or specs changed. Made 2026-11-03 with `scripts/review_word_pictures.py`; the text checks
are in [wordwall-text-review.md](wordwall-text-review.md).

**Open the contact sheet:** [wordwall-picture-review/index.html](wordwall-picture-review/index.html) (flagged cards
grouped by subject: picture, word, definition, the model's "shows" and "problem", scores, flag kind, and a purple tag
when an earlier audit listed the card). Every card's scores are in
[wordwall-picture-review/flags.csv](wordwall-picture-review/flags.csv).

## Method

1. **Render.** Every diagram spec in `data/closet/words/diagrams.py` (2,072) was drawn fresh with `wordsvg.render()` and
   `wordsvg.rasterize()` (headless Chrome) to PNG in `closet/words/art/_raw/review/diagrams/` (gitignored). 0 render
   errors, and 0 renders differ from the published webp, so no diagram is stale. Diagrams were judged from these PNGs,
   paintings from `closet/words/art/<module_id>/<slug>.webp`.
2. **CLIP** (openai/clip-vit-large-patch14): cosine of each picture against "a picture of {word}: {definition}",
   turned into a percentile within its subject (0 = worst). Also recorded: where the card's own word ranks among its
   module's words for that picture (`mod_rank`), a useful tiebreak in the CSV.
3. **Qwen3-VL-4B-Instruct**: one look per card at 448 px, given word, definition, grade band and picture kind, asked
   for strict JSON `{"match": 1-5, "shows", "problem"}` (5 = a student would name or understand the word from the
   picture, 1 = wrong or misleading). Greedy decoding, batches of 16, resumable (`qwen.jsonl`). The full run took
   about 14 minutes (0.22 s a card) on the RTX 5080, so every card was rated, no sampling. All 3,633 replies parsed.
   Score spread: 5: 1,634, 4: 1,078, 3: 391, 2: 315, 1: 215.
4. **Flag rule.** `qwen-1-2`: Qwen 1 or 2. `qwen-3+clip`: Qwen 3 and bottom 10% CLIP in its subject.
   `diagram-text`: a diagram whose spec has text or labels (1,323 of them; small vision models misread these), flagged
   only at Qwen 1, or Qwen 2 with bottom-10% CLIP.

## Counts

**524 flagged of 3,633 (14%)**: 372 `qwen-1-2`, 56 `qwen-3+clip`, 96 `diagram-text`.

| Subject | Cards with pictures | qwen-1-2 | qwen-3+clip | diagram-text | Flagged | Share |
|---|---|---|---|---|---|---|
| arts | 312 | 31 | 6 | 12 | 49 | 16% |
| computer-science | 282 | 37 | 3 | 16 | 56 | 20% |
| cte | 43 | 8 | 1 | 0 | 9 | 21% |
| ela | 629 | 91 | 12 | 31 | 134 | 21% |
| eld | 100 | 9 | 0 | 3 | 12 | 12% |
| health-pe | 142 | 13 | 2 | 4 | 19 | 13% |
| library | 51 | 6 | 1 | 0 | 7 | 14% |
| math | 811 | 27 | 9 | 11 | 47 | 6% |
| science | 594 | 51 | 10 | 5 | 66 | 11% |
| sel | 41 | 6 | 1 | 1 | 8 | 20% |
| social-studies | 526 | 84 | 11 | 4 | 99 | 19% |
| world-languages | 102 | 9 | 0 | 9 | 18 | 18% |
| all | 3,633 | 372 | 56 | 96 | 524 | 14% |

By kind: 286 of 1,412 paintings (20%), 223 of 2,072 diagrams (11%), 14 of 129 people pictures, 1 of 20 gpt pictures.
By band: K-2 157, 3-5 135, 6-8 172, 9-12 60.

**Earlier audits.** 73 flagged cards were already listed in WORDWALL-PAINTINGS.md or WORDWALL-DIAGRAMS.md. 65 of them
still have the same picture as when those audits were written (46 REDO, 14 FIX, 4 CODE, 1 PAINT): known and not yet
fixed, so they need no new judgment. The other 8 were redrawn and are flagged again, so the redraw may have missed.

## How well the flagging works (my look at 60 cards)

I looked at 30 random flagged and 30 random unflagged cards (seed 7) on labeled sheets.

- **Precision about 55 to 60%.** Of 30 flagged: 16 are real problems (the picture does not show the word, or only a
  stretch of it), 2 borderline, 12 false alarms. By flag kind: `qwen-1-2` 12 of 21 real; `qwen-3+clip` 3 of 4 real,
  1 borderline; `diagram-text` 1 of 5 real, 1 borderline (as expected, the weak one).
- **False alarms** come from icons the model reads literally: a Bee-Bot for "program", a check mark for "answer", a
  mouse click for "event", a door and arrow for "log out", hearts for "beat", a box labeled "age" holding 7 for
  "variable", a HELLO tag for "my name is". A person skims these in seconds.
- **Misses: about 1 to 3 in 30 unflagged** (3 to 10%), so perhaps 100 to 300 weak pictures among the 3,109 unflagged.
  Clear miss: science-6 "axis" (a planet whose dashed line runs across, not from pole to pole as the red pole ticks
  suggest). Borderline: "demographic transition" (two unlabeled falling lines), "prey" (a mouse alone, no predator,
  Qwen 3 but CLIP was not low). The model is lenient: it gives 4 or 5 to most pictures that are merely related.
- Net: the sheet is worth Cory's time (about 290 to 310 real problems among the 524), but it is a review queue, not a
  verdict list, and it is not a complete list of weak pictures.

## Top problems

1. **Abstract and function words painted as an unrelated object.** The biggest group, mostly ELA, ELD and SEL:
   topic (a shark; a honeycomb), meaning (an elephant and mice), key detail (honey), benefit (bread rolls), synonym
   (two elephants), now and present (a school; vehicles), finally, since, pun, long vowel (a birthday cake). A
   painting of a thing rarely teaches these; a small code-drawn scene with a word or a sentence strip would.
2. **History terms drawn as generic scenery.** Social studies: French Revolution (a castle), Haitian Revolution (an
   island), Treaty of Versailles (a hallway), Fugitive Slave Act (a blank paper on a fence), Deaf President Now (a
   gate with lanterns), Mandate of Heaven (a dragon), civil service exam (a paintbrush), patrician (a robe on a stool),
   griot (an instrument, no person). These need an event scene, a document with a date, or a map.
3. **Science processes shown as one object.** irreversible (a fried egg), fermentation (a slice of bread), chemical
   reaction (a nail). They need a before and after.
4. **Feelings with no one feeling them.** scared (a lightning bolt), calm down (five numbered clouds).
5. **Word-part and notation diagrams the model cannot judge.** root, base word, syllable, gloss, genotype, identity:
   some are fine (false alarms), some are thin (identity shows only a number line). These are the `diagram-text` cards;
   skim them, do not trust the score.

The worst cards (Qwen 1 with the lowest CLIP in their subject) sort first within each subject on the sheet.

## Files

- `scripts/review_word_pictures.py`: render, clip, qwen, combine (rerun any step; qwen skips cards already in the JSONL).
- `docs/agents/audit/wordwall-picture-review/`: `index.html` (contact sheet), `flags.csv` (every card),
  `qwen.jsonl`, `clip.csv`, `render.json`.
- Diagram PNGs for the sheet: `closet/words/art/_raw/review/diagrams/` (gitignored; `python scripts/review_word_pictures.py render` remakes them).
