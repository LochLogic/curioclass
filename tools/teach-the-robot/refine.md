PASS
Counts: blockers 2 (general 1, family 1), should fix 8 (general 8, family 0), polish accepted 10

# teach-the-robot: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
1. **The dogs look like cats** (T-B1, P-S1; family:ml-lab, the shared pet drawing). Whiskers and the curled upright
   tail go on cats only; dogs get a clear snout scaled by the snout value, ears that show on dark coats (Bear, Moose:
   an outline or lighter inner ear), and a dog tail. Check every one of the 26 pets in a contact sheet: a grade 2
   child must call each dog a dog and each cat a cat at a glance. The look-alike pairs the lesson needs (Ziggy and
   Pippin, Marmalade) must still look alike in the feature the spec means, not in species.
2. **A wrong label makes the parade score go up** (T-B2; general). 6 of the 10 parade pets are dogs, so labeling
   Marmalade a dog raises the score at every wall size 1 to 9 and Kip says "That's more than last time!". The lesson
   is that wrong labels make guesses worse. Rebalance the parade (5 cats, 5 dogs, or pets chosen so that) and check in
   Node that the notes' wrong-label experiment lowers or holds the score at every wall size the class is likely to
   try (1 to 16), then update the spec's score table and notes under a "Refine changes" line. Keep the engine
   unchanged unless the data truly cannot do it.

## Should fix
3. **Loop after all 16 cards** (T-S1, P-S6, C-S6). Once the deck is used up, Parade and the hint point to Mystery pet
   or Start over, never "show Kip more pets"; the shelves stop showing empty slots as if more were coming (P-S5).
4. **Pet Parade with an empty wall** (P-S2, C-S1). Its own line names Teach (and the Teach button pulse is visible:
   the mode switcher's overflow clips it). Nothing waits 5 s behind the welcome.
5. **Every waiting moment names the next control** (P-S3, C-P2). After a Mystery result, Forget, Start over and during
   a Mystery pet, the hint and Read name the next action.
6. **Line 6 ("Kip looks for the pet it remembers...")** (P-S4, C-S5). Settled: it is a how line, spoken on the first
   Mystery pet only, then hint only (BASELINE, say how to act once). Kip's guess line plays when the guess shows.
   Update the spec's voice table under "Refine changes".
7. **Enter on a wall card loses focus** (C-S2). Refocus after drawShelves(); Delete, Escape and arrows work.
8. **Focus falls to the body after Next pet, Cat, Dog, Mystery pet** (C-S3). Keep focus on a live control (use
   aria-disabled while busy, or move focus to the next control).
9. **Header buttons under 60 px** (C-S4). Raise them to 60 px in this tool's CSS, as robot-dance and computer-builder
   do; no kit change.
10. **Shelf count** (P-S5): "8 of 16" with 16 slots after the deck is used up; show what is taught.

## Polish accepted
11. Kip's guess stays up long enough for the class to call it out before the truth badge (at least 2 s; T-P4, P).
12. Kip's face changes with the parade result (P).
13. 680x425: fewer empty slot rows, a bigger pet (P).
14. The matched-card glow and the line's end dot don't cover the shelf header or the pet's name (P).
15. Chart and score text at least 14 px on a projector; the memory counter larger at 1366x768 (P).
16. Wall cards get a hit area over the whole cell, at least 60 px (C-P1).
17. Line 13 doesn't ask to tap a card when one is selected (C-P3).
18. A "What will Kip guess?" beat before the Mystery reveal so the class predicts (T-P1).
19. Line 10 doesn't blame "more examples" when a wrong label caused the miss; line 33 says "different" examples
    (T-P2, T-P3). Keep allLines() and voice/lines.json matched.
20. Once the deck is used up, Pet Parade is the main button, not Next pet (P).

Nits are optional; fix the cheap ones (hint during the dimmed Cat and Dog second, paws row at 680x425, the stage's
role="img" hiding buttons, a line running into the next Mystery pet, confusion cells' tabindex, MLLab.version in the
doc, the CSTA paraphrase, "only Pudding").

## Exit check (round 1, 2026-10-28, fresh cold agent)

Bundled with `CURIO_DRAFT=1` (123 KB, one file, only http string is the SVG namespace). Driven with `scripts/drive.py`
(own profile and ports 9590 to 9594, iframe host on 9592 for 375 wide; host.html deleted, nothing left listening).
No console errors or exceptions from the tool in any run (the only log line was the host page's favicon 404).

**Open (blocks PASS):**
1. **Pet Parade hint cut off at 680x425** (should fix, general; regression of the round 1 hints, which are longer).
   In the compact layout the parade panel gives `#hint` 41 px (scrollHeight 57), so a three line hint runs under the
   Start parade or Stop button: "Welcome to the Pet Parade! ... Count how many Kip gets right." loses "right." during
   every run, and every end hint loses its last words ("...Then run the parade again.", "Kip has seen every pet! Tap
   Teach to try Mystery pets, or Start over to teach Kip again." loses a whole line). Teach at the same size gives the
   hint 57 px and fits. Fine at 800x500 and up, 760x900 and 375 wide. Frames: parade-mid-680x425, parade-end-680x425,
   paradeall-680x425. Fix: give the parade panel's hint the same room as Teach's (min-height for three lines at 14 px).

**Merged list, re-checked:**
- B1 dogs look like cats: fixed. Own contact sheet of all 26 pets (full body, and wall cards at 43 and 88 px). Every
  dog has a long snout with a black nose pad, tongue, round brown eyes and a red collar with a tag; every cat has long
  whiskers, slit green eyes, a pink nose and a curled S tail. A grade 2 child would sort all 26 right at a glance;
  the pointy eared dogs (Rocket, Ziggy, Pippin, Juniper) still read as dogs by snout, collar and tongue, and dark coats
  (Bear, Moose, Shadow) show a light ear outline. Ziggy and Pippin still share the pointy ears the lesson needs.
- B2 wrong label raises the score: fixed. Parade is 5 cats, 5 dogs. Recomputed in Python from the arrays in src.html
  (Euclidean, k = 1, ties to the first taught card): right labels 5, 6, 7, 7, 8 (N 5 to 9), 9 (10 and 11), 10 (12 to
  16); Marmalade as dog 5, 5, 6, 6, 8 ..., 8; for every N from 1 to 16, no single wrong label of any taught card raises
  the score; no distance ties. Snowball as dog with 5 cards: 6. All match spec and notes. The page gives the same
  numbers and the same misses (2 cards: Luna, Pippin, Waffles, Bramble).
- 3, 10, 20: deck used up: Pet Parade is the main button, Next pet gone, no empty slots, "8 pets"; parade hint names
  Teach and Start over. Fixed.
- 4: empty wall Pet Parade speaks only its own line ("Tap Teach first!"), the Teach button pulse shows. Fixed.
- 5: hints after Mystery result, Forget, Start over and the prediction beat name the next control. Fixed.
- 6, 18, 11: prediction beat about 3 s, line 6 on the first Mystery pet only, guess line with the guess, held 2 s.
  Fixed.
- 7, 8: real keys: Enter on Next pet moves focus to Cat; Cat to Next pet; Dog on the last card to Pet Parade; Mystery
  keeps focus through the run; Enter on a card keeps focus and selects it; ArrowRight then Enter selects the next
  card; Escape lets go; Delete forgets and focus goes to Next pet (card back at the front of the deck); Start parade to
  Stop. Fixed.
- 9: header and panel buttons 60 px tall at every size. Fixed.
- 12: Kip smiles at 10, looks puzzled at 4 (two wrong labels). 13, 14, 15 (chart axis 14 px, values and memory counts
  16 px at 1366x768), 17, 19 ("Oops! Kip remembered that pet wrong." when the deciding card was mislabeled): fixed.
- 16: whole cell hit area: 61x76 at 1366x768, 82x97 at 1000x625, but 47x47 at 680x425 (polish, known, not done; the
  handoff names it).

**Regressions:** frames of default, waiting for a label, Mystery guess, Mystery truth, card selected, deck used up,
parade mid run, parade end, empty wall parade at 680x425 and 1366x768; default, waiting, Mystery guess and parade end
at 800x500, 1000x625, 1280x720, 1920x1080 and 760x900; default, Mystery, parade end and deck used up at 375 wide.
Nothing off screen, no horizontal scroll, main controls visible at every size. Only the hint clip above. Known and
left: at 680x425 the truth badge covers the pet's small name.

**Gate:**
1. Done when 1 to 9: pass (2: 6, misses as listed; 3: 10 with bars 6 and 10 over paws 2 and 16; 4: 9 then 10 with
   "That's more than last time!"; 5: 5 vs 6 and 8 vs 10, Forget and relabel gives 6 again; 6: 50 Mystery pets at wall
   sizes 1, 2, 5, 11, 16, one line each, its end inside the card an independent nearest pet check picks, truth as the
   table; 7: counts below; 8: yes, 60 px buttons; 9: slots 3.53 to 3.55 s apart Motion on and calm, same score 7).
2. Standards: E2-ALG-ML-02 taught by labeling and testing; CSTA 1A-DA-07 through Kip's Chart: pass.
3. Solo student: first screen says tap Next pet, every waiting moment names the control: pass.
4. Sensitivity: not needed (rule 5 does not apply).
5. Open should fix: 1 (above): FAIL.
6. Bundle clean, 123 KB, no console errors, no network requests: pass.
7. Voice check (held clicks, 0.12 s): pass.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| catOrDog (Next pet x5) | how | 1 | 1 |
| remCat (Cat x5) / remDog (Dog x5) | event | 5 / 5 | 5 / 5 |
| tryMystery | how | 1 | 1 |
| predict (Mystery x5) | how | 1 | 1 |
| looks | how | 1 | 1 |
| thinkCat / thinkDog | event | 5 | 5 (4 + 1) |
| right | event | 5 | 5 |
| afterMystery | how | 1 | 1 |
| forgetHow (select x5) | how | 1 | 1 |
| forgot (Forget x5) | event | 5 | 5 |
| forgotHow | how | 1 | 1 |
| score line (parade x5) | event | 5 | 5 |
| same as last time | event | 4 | 4 |
| againHow | how | 1 | 1 |
| teachWelcome | welcome | 1 | 1 |

First tap: stage gets the welcome 132 ms after the press; Read speaks the hint only; Sound says nothing, Sound off and
on brings the welcome once; Pet Parade with an empty wall speaks only its own line; Next pet gets only its own line and
the skipped welcome comes on a later card landing or the next Teach entry, once. Stale: fast taps (0.2 s) through Next
pet, Cat, Mystery pet, Pet Parade, Teach, Start over: no line after its moment (no guess line after leaving mid
Mystery). Read cuts a playing line, works with Sound off, and a mode change right after Read speaks at once. Order
follows the actions. allLines() and voice/lines.json: 41 lines, word for word. No em dashes. Browser voice (clips not
recorded yet, expected).

## Exit check (round 2, 2026-10-28, same cold agent)

Rebundled with `CURIO_DRAFT=1` (124 KB). Driven on ports 9595 to 9597, iframe host on 9596 (host.html deleted,
nothing left listening). No console errors from the tool.
- Open item 1, closed. At 680x425 and 800x500, `#hint` is 57 px with scrollHeight = clientHeight (nothing hidden),
  and no panel control overlaps it, in all four cases: Pet Parade mid run, parade end, parade end with the deck used up
  (the longest hint) and Teach with the deck used up. Stop, Start parade and Pet Parade sit at 144 to 204 px, on screen.
  The panel does not scroll in Pet Parade.
- Kip's Chart: 104 to 108 px tall at 680x425 and 179 to 183 px at 800x500. Bars, values, the 10/5/0 axis and the
  paw counts are readable in the frames (3 bars at 680x425). The compact layout drops the small "7 of 10" under the
  slots, and the stage still shows the tally large.
- Regressions: default, Mystery result, wrong label result, card selected, deck used up, and parade mid run, end and
  end with the deck used up, at 680x425, 800x500, 1366x768 and 760x900, plus 375 wide (host): every hint whole, main
  controls on screen, no horizontal scroll. 760x900 and 375 look the same as in round 1.
- Nit (does not block): at 680x425 with a card selected, the Teach panel scrolls by 24 px, so "Kip remembers" sits
  below the fold under Forget. Forget and every main control stay visible.
- Polish left from round 1 (known, not done): wall card hit area 47 px at 680x425; the truth badge covers the pet's
  small name at 680x425.
Gate: all seven hold (items 1 to 4, 6 and 7 as in round 1; nothing that touches them changed, and no blocker or
should-fix is open).
