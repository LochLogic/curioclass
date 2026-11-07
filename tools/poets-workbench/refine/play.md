# Play lens: poets-workbench (Curiosity No. 10), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and the VISION "Curiosities: the second shape" section, not lesson norms.
Played twice: as a grade 7 student alone at home, and as a teacher projecting at 1920x1080. Frames are in
`S:/CurioClass-codex-scratch/poets-workbench/play/` (p*, q*, r*) unless they name the shared audit folder
`S:/CurioClass-codex-scratch/poets-workbench/audit-r1/`. Driven with `scripts/drive.py` (port 9451), real held clicks.

## Short test

- **Would a kid open it unassigned?** Yes, a word-loving one: a typewriter that marks the beat of whatever you type
  and finds rhymes on a tap is a real pull. The friction below (Play silent on open, rhymes buried under surnames,
  here/near not rhyming) is what would make a kid close it in the first two minutes.
- **Would an adult play for fun?** Yes. The whole CMU dictionary, live scansion, pronunciation variants and 16 real
  poems make it a desk a working poet could use. Stepping "record" and watching the marks move is a good moment.
- **Is the real thing the interface?** Yes. The page, the proof marks and the margins are the instrument; there is
  no wrapper (audit-r1/size-1366x768.png, p19-1920-raven.png).
- **No score, no finish line?** Passes. No goal, score, level, quiz or finish screen; a lesson-creep grep of src.html
  for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done finds nothing.

The short test passes. The findings are about the first two minutes and about readouts that look broken.

## Findings

1. **should fix · general · default screen, Play.** On open the caret sits on the empty line below the Frost line,
   so the big red Play key (the most inviting control on the desk) does nothing visible: it only sends "This line is
   silent. Type a word to tap its beats." to the screen-reader live region. Seen: q05-play-mid.png, page unchanged
   1.7 s after a held click, `playing:false`. With the caret on line 1 it works well (r01-play-line1.png). Better:
   on an empty line, Play taps the nearest line above (or the poem), so the first press always makes sound and light.

2. **should fix · family:curiosity · paper guides (Haiku, Limerick, Common, Sonnet).** The faint guide number or
   letter is drawn on top of the syllable count in the left margin, so the one comparison the paper exists for (your
   5 against the guide's 5, your 8 against a 6) is an unreadable smudge. Seen: q06-zoom-margin.png (haiku),
   q07-zoom-margin.png (limerick letters over counts), r05-sonnet-paper.png. The audit's overlap check missed it.
   Better: put the guide beside the count ("5 / 5") or in its own column.

3. **should fix · family:curiosity · paper guides count blank lines.** `guideFor(li)` (src.html:430) uses the raw
   line index, so a stanza break takes a guide slot. Sonnet 18 on sonnet paper puts the guide "C" on the blank line
   after the first quatrain and every later letter is off by one (r05-sonnet-paper.png, the lone "C" at y 662).
   Common meter on Dickinson's stanzas would shift 8, 6, 8, 6 to 6, 8, 6, 8 after the first break. Better: count
   only lines with words (and for haiku and limerick, restart at each stanza).

4. **should fix · family:curiosity · rhyme letters, "here" and "near".** CMU writes here as IY R and near, year,
   clear, fear, dear, queer as IH R, so the most common rhyme sound in English songwriting is split. A student's own
   couplet "standing here / have you near / sky is clear / another year" reads ABBB (q09, scheme readout); Frost, the
   opening poem, reads AABA CCDC DDED EEEE instead of its famous chain. The Manual is honest about Frost, but a kid
   writing their own poem sees the margin say their rhyme is not one. Only 31 CMU words end IY1 R against 192 for
   IH1 R (checked in `_scratch/poets-workbench/cmudict.dict`). Better: fold IY R into IH R for rhyme keys (a stated
   normalisation, like primary and secondary stress), and say so in the Manual. Teaching may rate this higher under
   REFINE's "a readout that misleads when its assumption doesn't hold".

5. **should fix · family:curiosity · words with two one-syllable pronunciations.** For a one-syllable word, Stress
   and Alt F only flip the stress; they never step to the word's other pronunciation (src.html:613-614). So tears
   (T EH1 R Z and T IH1 R Z), wind, read, lead, live, bow and close can never be corrected, and the rhyme letter
   uses whichever variant fit the meter first. Invictus, chosen because it "reads cleanly", reads ABAB CDCE FGHG IBIB
   (tears/years split, and unbowed takes B OW1 D, not aloud's AW). Flipping "tears" left the scheme unchanged
   (q04-invictus-tears). Better: step one-syllable words with several pronunciations through them too, and let the
   end-word variant prefer one that rhymes with a nearby line end.

6. **should fix · general · rhyme drawer, Replace word on by default.** The spec's first reaction is "tap hot ... tap
   spot and it can be dropped into the page". With Replace on, tapping spot turns "I like to eat my pizza hot" into
   "I like to eat my pizza spot" (q03-insert-spot). A rhyming dictionary is opened to find a word for another line;
   replacing the word you rhymed against is rarely wanted. Better: default to inserting at the caret as it was before
   the tap (or at the end of the next line), with Replace as the option.

7. **should fix · family:curiosity · rhyme drawer order.** Groups sort by syllable count first, so the one-syllable
   group of "hot" holds 154 entries and turns to surnames by the fifth row: baht, bhatt, bott, brott, clott, cott
   (q02-click-hot.png); "think" reaches cinq, cinque, finck, fincke, hinck within five rows (p13-midline-click.png).
   "forgot" and "apricot" from the spec's first two minutes sit below about 150 names. Better: show the SCOWL tier
   across all syllable groups first, then a single "Names and rare words" fold.

8. **should fix · general · meter names with fractional feet.** The line-end readout says "anapestic 2.7 feet" for
   every classic limerick line, "trochaic 2.5 feet" on haiku, "iambic 3.5 feet" for "I will record a record", and
   "trochaic 39.0 feet" for a long line (p08, q07-limerick-frame.png, p04, p15). It looks like a bug to a student and
   is not how a poet names a line ("anapestic trimeter, missing its first syllable", or "catalectic"). Even with the
   Anapest lens on, the limerick stays "2.7 feet". Better: round to whole feet and name the missing or extra
   syllables.

9. **should fix · general · Read key.** Read makes no sound and changes nothing on screen; it only puts "Type a line.
   The recorded hint is not supplied in this build." in the live region and the button title (p17-read-press,
   `vlog: []`, hint stays hidden). The Manual also says "The smooth-narrator hint recording has not been supplied in
   this build". That is maker talk on a student's desk. The clip waiting for the Forge is fine (BASELINE rule 18);
   until then Read should at least show the hint again on the page, and the build note belongs in notes.md, not in
   the Manual or a tooltip.

10. **polish · family:curiosity · Sounds key.** Assonance shades every word whose stressed vowel repeats anywhere in
    the line in one plum, over the whole 78 px word box including its marks. On The Raven 408 words are shaded and the
    page becomes a wall of purple (p06-raven-sounds.png); on "Peter Piper" you cannot tell the IH pair from the EH pair
    (q08-sounds-simple.png). Function words alliterate ("The ... the"). The alliteration underline sits low enough to
    strike through the meter note below. Better: one ink per repeated vowel (dreary/weary share one, napping/tapping/
    rapping another), skip function words, and keep shading to the text height. That would also make the spec's
    "find the rhymes hiding inside The Raven's lines" possible to see.

11. **polish · general · tap to place the caret opens the drawer.** Any click inside a word opens the rhyme drawer and
    narrows the page 50 px (848 to 798, p13-midline-click.png), so lines re-wrap; the first keystroke closes it and
    they re-wrap back. Revising mid-line by mouse makes the page jump twice each time. At 680x425 the tapped word
    "hot" wraps under the drawer to a row that is cut off (p20-680-drawer.png). Better: keep the page width when the
    drawer opens (it is already a fixed overlay at 1366), or open rhymes on a tap of the end word / double-click.

12. **polish · general · secondary stress always strong.** Names a student types for "Type your name" read oddly:
    Cory (K AO1 R IY2) marks "/ /", Aaliyah "/ / /" (p05). "midnight" in The Raven's first line costs a match
    (15 of 16). Better: treat secondary stress as flexible, like the free function words, so it follows the meter.

13. **polish · general · empty page.** Clear the page and nothing says what to do: the "Type a line." hint never
    returns, and Play and Rhymes only answer in the live region (p14-empty). Better: bring the hint back whenever the
    page is empty.

14. **nit · general · the shelf at 1366x768.** Six of sixteen books (Sympathy onward, including Jabberwocky and
    Invictus) are below the fold of a thin-scrollbar list, with only a sliver of the seventh showing
    (audit-r1/size-1366x768.png; books scrollHeight 899 vs 557). The "THE SHELF / 16" label helps. Smaller spines would
    fit all sixteen.

15. **nit · general · provenance wording.** After typing, the source line reads "YOUR PAGE / stays on this device only
    when saved", which reads as if the page leaves the device otherwise. "YOUR PAGE / not saved" or "YOUR PAGE / save
    in Drafts" says it plainly.

Checked and fine: the opening Frost line reads 8 and iambic tetrameter; typing "I like to eat my pizza hot" scans
x / x / x / x / and iambic tetrameter 8 of 8 (q01); "I will record a record" gives verb then noun stress (p04), and
stepping record moves the marks (r03); orange shows 0 perfect rhymes and slant lists (p03); Dickinson reads
8, 6, 8, 6 (p10); Jabberwocky's invented words carry the dotted underline (p09); The Raven's internal-rhyme lines
scan trochaic octameter 15 of 16 (p06); Play highlights each beat and Stop works (r01); drafts save with the
on-device note (r04); Motion off removes the drawer animation (q13); the dictionary is ready in about 0.3 s, and
re-scanning The Raven on a keystroke takes about 24 ms here (r02); the 680x425 preview is readable and inviting
(audit-r1/size-680x425.png); the 375 iframe and 1920 frames hold. No em dashes in src.html. Nothing cultural,
Native or hard-history needs a sensitivity flag from this lens beyond what notes.md already lists for the shelf.

## Counts

blocker 0 · should fix 9 · polish 4 · nit 2

## Audit pilot

- **Leads confirmed:** shelf books "off screen at load" at 1366x768 (finding 14; it is a scroll list, so not broken);
  Sympathy "covered at its centre" is the same scroll edge.
- **Leads wrong:** #editor / #hint overlap at every size (the hint is drawn on the page on purpose); "hint out of view"
  in the states (the hint hides after the first action by design); Manual and Drafts covering the editor (they are
  modal dialogs); Print "nothing changed" (headless print); tempo knob "nothing changed" (a click without a drag does
  not turn it, which is right; the arrow keys and drag work); "focus taken on load" (the editor taking focus is the
  right first state for a typewriter).
- **What it missed:** the guide-over-count overlap in the margins (finding 2), Play silent on the default screen
  (finding 1, the audit clicked Play with no check of sound or light), Read changing nothing visible (it scored "ok"),
  the guide shift on stanza breaks, and every readout question (here/near, tears, fractional feet), which it cannot
  see by design.
