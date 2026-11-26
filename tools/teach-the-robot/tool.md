# Teach the Robot: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 2 (general 1, family 1), should fix 8 (general 8, family 0), polish accepted 10

### teach-the-robot: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

#### Blockers
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

#### Should fix
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

#### Polish accepted
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

#### Exit check (round 1, 2026-10-28, fresh cold agent)

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

#### Exit check (round 2, 2026-10-28, same cold agent)

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

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json, art/prompts.json, kit/ml-lab.js and
docs/families/ml-lab.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` (117,020 bytes).
Driven in muted headless Chrome (own profile, ports 9520 to 9524) with `scripts/drive.py` and a scratch CDP runner
with held clicks (120 ms). Headless Chrome has no speech voices, so the runner stood in a fake `speechSynthesis`
(about 70 ms per character at rate .95) to get real-length lines and their start and end times against the state.

Counts: blockers 0, should fix 6 (general 6, family 0), polish 3 (general 3), nits 4 (general 2, family 2).

#### Should fix

1. **Pet Parade with an empty wall names a hidden control.** src.html:855 (`startParade`), :673, :683, :932.
   Seen in run rep-parade-empty: opening Pet Parade first (a solo student's likely first tap) speaks the welcome
   ("Count how many Kip gets right") and "Tap Start parade.", then Start parade plays line 11 "Kip doesn't remember
   any pets yet. Tap Next pet first!" 5 of 5 times, and the hint keeps it, while Next pet is not on screen in this
   mode (the handoff lists it as a known gap). A line naming a hidden control must not play. Better: a Parade-mode
   line such as "Kip doesn't remember any pets yet. Tap Teach first!" (added to voice/lines.json), and with an empty
   wall the Parade how-to and hint name Teach instead of Start parade. Tag: general.
2. **Selecting a wall card from the keyboard loses focus, so Delete, Escape and the arrow keys do nothing.**
   src.html:823-826 (`selectCard`). `drawShelves()` rebuilds every card, so by the time the guard checks
   `document.activeElement.closest('.card')` the focused card is gone and focus is on `body`; the refocus never runs.
   Seen in run kb: Tab to Inky, Enter selects it (frame kb-cardsel: thick outline, Forget shown, no focus ring),
   active element = BODY; ArrowRight and Delete then left all 4 cards on the wall. notes.md ("On a selected wall
   card, Delete forgets it and Escape lets go. Arrow keys move between wall cards") promises what does not work.
   Better: note whether a card had focus before `drawShelves()`, then focus the new node by `data-key`. Tag: general.
3. **Focus drops to the page after every panel action.** src.html:688-695 (`updateButtons`). Next pet, Cat, Dog
   and Mystery pet disable themselves while busy, so the focused button loses focus and no focus ring shows (run kb2:
   Enter on Next pet, active = BODY; Tab, Enter on Cat, active = BODY). A teacher on a keyboard or clicker loses
   their place each step. Better: when the waiting control enables, move focus to it with
   `focus({preventScroll: true})` if focus was in the panel (Cat when a pet sits waiting, Next pet after a card
   lands, Mystery pet after the truth). Tag: general.
4. **Header buttons are 48 to 52 px, under the K-2 60 px target.** Measured: Teach, Pet Parade, Motion, Sound, Read
   are 52 px tall at 1280x720, 1366x768, 1920x1080 and 760x900, 48 px at 680x425, 800x500 and 1000x625 (compact).
   The handoff left them at kit size to avoid changing `kit/curio.css`, but the K-2 neighbors robot-dance and
   computer-builder set `.seg button` and `.icon-btn` to `min-height: 60px` in their own CSS, so no kit change is
   needed. Panel buttons are 60 px everywhere (passes). Tag: general.
5. **Line 6 ("Kip looks for the pet it remembers that looks the most alike.") is a teaching line spoken on every
   Mystery pet.** src.html:802. Voice check: 5 of 5 Mystery pets spoke it; the standard says teaching lines are
   spoken once, then hint only. It also holds the guess back: the line runs about 4.9 s against a 1.2 s think, so
   the guess shows on Kip's screen about 3 s before "Kip thinks it's a cat!" is heard (that line waits in the queue),
   and a Mystery pet takes about 9 s with Sound on against 3.6 s with Sound off. The spec marks line 6 an event, so
   this is a lens and spec disagreement for the integrator. Better: `V.how` (once per load; the hint keeps it for
   Read), or keep it an event but cut it down so the guess line lands with the guess. Tag: general.
6. **Line 32 ("Tap Teach and show Kip more pets. Then run the parade again.") plays when there are no more pets to
   show.** src.html:891 and :683. Its `valid` checks only `!state.running`. After all 16 cards are taught (the Done
   when 3 path, a common class flow) the first parade speaks it and the hint keeps it; Teach then answers Next pet
   with "That's every example card!". Better: speak it only while `state.deck.length > 0`; with an empty deck name
   what still works (relabel with Forget, or Start over). Tag: general.

#### Polish

1. **Wall cards are smaller than 60 px at the main sizes.** Card size measured: 40 px at 680x425 and 800x500, 51 at
   1000x625, 49 at 1280x720, 55 at 1366x768, 41 at 760x900, 88 at 1920x1080. The spec allows 40 px in the small
   embed, but cards are the only way to reach Forget. Better: an invisible hit rect over the whole cell (card, name
   and gap: about 55 x 76 px at 1366x768) inside each `.card` group. Tag: general.
2. **The hint is stale during a Mystery pet and names no next step after it.** src.html:789-818. Lines set the hint
   only when they start, so while a Mystery pet walks and Kip thinks, the hint still reads the previous line (frame
   calm-walk: "This is Kip... Tap Next pet to show Kip a pet." with Next pet disabled); Read during the think (run
   read-myst) spoke that welcome. After the truth the hint is "Yes! Kip got it right!" with no next action. Better:
   set the hint when the pet walks in (for example the line 6 text) and, after the truth, show the next step with the
   result ("Tap Mystery pet again, or Next pet to teach Kip more."). Tag: general.
3. **Line 13 tells the teacher to tap a card that is already selected.** src.html:827. It plays when a card is
   selected: "Tap a card on the wall, then the trash can, to make Kip forget it." Better at that moment: "Tap Forget
   to make Kip forget it. Tap the card again to keep it." (or keep line 13 for an idle hint and add this one).
   Tag: general.

#### Nits

1. The stage `<svg id="sv" role="img">` holds the focusable wall-card buttons; `role="img"` hides its children from
   screen readers. `role="group"` with the same label keeps the cards reachable. src.html:149. Tag: general.
2. A line already playing runs past its moment: in run stale-label "Kip remembers: that one is a cat!" (Inky) kept
   playing as the next Mystery pet walked in, and line 6 for that pet was then dropped as stale. Only with fast taps;
   the kit does not cut a playing line on `dropQueued`. Tag: general.
3. Engine: `view.confusion` without `onCell` removes the cells' `role` but leaves `tabindex="0"`, so Tab stops on
   cells that do nothing. kit/ml-lab.js:300-314. Tag: family:ml-lab.
4. Doc: docs/families/ml-lab.md does not list `MLLab.version` (exported, kit/ml-lab.js:388). Tag: family:ml-lab.

#### Checks that passed

**Contract.** One file, 117,020 bytes. `kit:curio` (CSS and JS) and `kit:ml-lab` inlined, nothing re-implemented
(the tool calls `MLLab.knn` through `guessFor`). No network requests: across about 30 page loads the Network log held
only the tool file; `performance.getEntriesByType('resource')` was empty. The only absolute URL in the bundle is the
SVG namespace. No console errors, warnings or exceptions in any run (drive.py sizes run: "errors in 0 shots").

**Engine against the family spec and doc.** `rng` is the spec's mulberry32 character for character (seed 1 gives
0.6270739405881613); `uni`, `r2` (0.285 to 0.29, -0.285 to -0.29), `item`, `dist`, `knn` (distance, then position;
vote by count; ties to the label whose nearest member comes first; `score`), `train('knn' | 'tree' | 'linear')`,
`evaluate` (cm, cells, byGroup, results, mistakes, tp to precision, threshold with `positive`) and the three views
(`confusion` with `onCell`, `scatter` with `query` and `onPick`, `groupBars`; glyph or letter as well as color;
ResizeObserver; aria-label with the numbers) match spec.md "Family engine" and the API block in ml-lab.md. No
stylesheet; colors from the documented CSS variables. No closing script tag in the file. Rechecked in Node with
the engine: parade scores after N correct cards, N = 1 to 16: 4, 4, 5, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10;
misses at N = 2 Rusty, Luna, Noodle, Pippin, Waffles, Bramble; at N = 11 Pippin; Marmalade as dog with 2 cards: 6.
All match the spec and notes. In the page the parade runs gave 4, 4, 10, 4, 4 (rep-parade), 9 then 10 at 11 and 12
cards, 5 at 3 cards.

**Access.** Tab order as the spec says: Teach, Pet Parade, Motion, Sound, Read, Next pet, Mystery pet, Start over,
then the wall cards (Pet Parade: the cards are out of the tab order). Focus ring visible on buttons and on a
focused wall card (frames kb-tab4, kb-tab5, kb-tab8, kb-680-card). Every panel button is 60 px tall and has an
icon; Cat and Dog, the shelf headers, the truth badge, Kip's right or wrong badge and the parade slots all carry a
glyph or word as well as color. Motion off: pets appear in place, the spin and glow stop, timing and scores hold
(frames calm-walk, calm-p-end). Sound off hushes and still updates the hint; Read works with Sound off.

**Lines.** `__tool.allLines()` returns 33 lines, word for word and in order the same as voice/lines.json; every
quoted line in the spec's Voice section is among them.

**Art.** No `art:` tokens; art/prompts.json has no assets (everything drawn in code). No people.

**Words.** No em dashes in src.html, notes.md, lines.json, kit/ml-lab.js or docs/families/ml-lab.md. "Curio Class"
only, never "Curio" alone in text. Classroom-safe. The tool stores nothing (notes say so; the kit's own Motion
preference is the only stored value).

#### Standard voice check

Held clicks, Sound on, Motion on, 1366x768. Gaps longer than the lines unless noted.

**1. Repeats (five of each action).**

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| 1 Teach welcome | welcome | 1 | 1 |
| 2 Is it a cat or a dog? | how | 1 | 1 (then 4 silent) |
| 3, 4 Kip remembers: cat / dog | event | 3 / 2 | 3 / 2 |
| 5 Now tap Mystery pet | how | 1 | 1 (then 3 silent) |
| 6 Kip looks for the pet... | event in spec, teaching line by the standard | 1 by the standard | 5 (should fix 5) |
| 7, 8 Kip thinks it's a cat / dog | event | 3 / 2 | 3 / 2 |
| 9 Yes! Kip got it right! | event | 5 | 5 |
| 10 Oops! Kip guessed wrong | event | not reached (5 cards: Maple to Ghost all right) | n/a |
| 11 Kip doesn't remember any pets (Teach) | event | 5 | 5 |
| 11 same, in Pet Parade | event | must not name hidden Next pet | 5 (should fix 1) |
| 12 That's every example card! | event | 5 | 5 |
| 13 Tap a card on the wall... | how | 1 | 1 (then 6 silent) |
| 14 Kip forgot that one. | event | 2 | 2 |
| 15 Starting over! | event | 1 | 1 |
| 16 Pet Parade welcome | welcome | 1 | 1 |
| 17 Tap Start parade. | how | 1 | 1 |
| 18 to 28 Kip got N out of ten right | event | 5 | 5 (four, four, ten, four, four) |
| 29 / 30 / 31 more / same / fewer | event | 1 / 2 / 1 | 1 / 2 / 1 |
| 32 Tap Teach and show Kip more pets | how | 1 | 1 (then 4 silent) |
| 33 The more examples Kip saw... | event, once per load | 1 | 1 (with the first 10 after a lower run) |

**2. Stale lines.** Fast taps (0.2 to 0.9 s): Next pet, Cat, Next pet, Dog, Mystery pet, Pet Parade, Teach, Start
over. Queued lines whose moment passed were dropped (newer), the mode switches and Start over hushed what was
playing, and every line that started matched the frame state at its start (logged per line: mode, pet, phase).
Mystery then Pet Parade then Start, Stop, Teach: the think and guess lines were hushed, nothing played late. One line
already playing ran into the next Mystery pet (nit 2). No line named a hidden control except line 11 in Parade
(should fix 1).

**3. First tap (fresh page each; nothing spoke before the tap in any).** Stage: the welcome at once. Key (Tab): the
welcome at once. Motion: the welcome. Next pet: the welcome was dropped unmarked (stage busy), line 2 came at the end
of the walk-in (0.8 s), and the welcome came once after the first card landed. Mystery pet (empty wall): only line 11.
Pet Parade: only the Parade welcome. Read: the hint only. Sound: nothing; Sound on again: the welcome, once (a second
off and on did not repeat it).

**4. Read.** Read during the welcome cut it and spoke the hint; Read with Sound off spoke the hint; nothing cut Read
off, and a line queued during Read (line 7 in run read-myst) waited until Read ended; Pet Parade right after Read
started the Parade welcome at once.

**5. Order.** In every run spoken lines followed the order of the actions; no line from an older action played after
a newer one started.

#### Frames and runs looked at

drive.py sizes run (Teach with 16 cards at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900; Pet
Parade at 680x425 and 1366x768; no horizontal scroll at any size); kb-tab4, kb-tab5, kb-tab8, kb-cardsel, kb-afterdel,
kb2-cat-focus, kb-680-card; calm-walk, calm-think, calm-truth, calm-p-walk, calm-p-end; rep-teach after5 and
after-myst; rep-parade run1 to run5; rep-empty end; rep-parade-empty end; the ft-* first-tap frames.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json; bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
teach-the-robot` (112 KB). Driven with `scripts/drive.py` (held clicks, muted Chrome, own profile, ports 9510-9515),
frames in the lens scratch folder (f1 to f5). Played twice: as a grade 2 student alone (real clicks only, hint and
voice log polled every 200 ms) and as a teacher projecting at 1366x768.

Frames looked at: default, Next pet wait, labelled, Mystery think, guess and truth (2 cards and 16 cards), card
selected with Forget, deck used up, Parade default, mid parade, parade end (4 runs and 9 runs, chart at 8 bars),
empty-wall Start parade and Mystery, Start over, Forget; each of 680x425, 800x500, 1000x625, 1280x720, 1920x1080,
760x900 (default, wait, 16-card truth, selected, parade end) and 375 wide in the iframe host; Motion off; every one
of the 16 deck pets and 10 parade pets in the spotlight. No console errors (one favicon 404 from the test host only).

Counts: blockers 0, should fix 6, polish 7, nit 2.

#### Should fix

1. **Several dogs are drawn as cats, so the class labels them wrong in good faith.** (stage drawing, `drawHead` /
   `drawPet`, src.html:324-409) Seen in the per-pet frames (f4/g06, g12, p07, p10 and the dogs.png crop): Rocket,
   Ziggy, Pippin and Juniper are pointy-eared, whiskered, upright-tailed animals any 7-year-old calls a cat. The snout
   clue, which is the strongest cat/dog difference in the data (cats .15-.30, dogs .50-.75), is drawn as a small
   muzzle oval that barely changes; on dark coats the ears vanish (Bear's .50 ears sit behind the ruff, Moose's
   floppy ears are coat-dark on coat-dark), and every pet has the same upright cat tail. Teach never checks labels, so
   a class that says "cat" for Ziggy breaks the tool's own talk point (Ziggy is the only card that fixes Pippin), and
   in Parade a big "Dog" badge lands on a cat-looking picture, which reads as the tool being wrong. Better: make the
   snout read as a real dog snout at high values (longer, deeper muzzle, visible nose at the tip), show floppy and
   half ears in a lighter or outlined shade on dark coats, and let the tail follow a clue (or be neutral) so it does
   not say "cat" on every pet. Keep Pippin and Juniper honestly tricky, but tricky to Kip, not to the class. general.
2. **Start parade with an empty wall: nothing for about 5 s, then a line naming a hidden button.** (Parade,
   `startParade`, src.html:855) Real clicks Pet Parade then Start parade (f2/21): the welcome keeps playing, the
   "empty" line only starts at 4.7 s and says "Tap Next pet first!", but Next pet is hidden in Parade. The Teach pulse
   that should point the way is invisible: `.pulse` is on `#m-teach` (class and box-shadow confirmed, f3/c-pulse) but
   the `.seg` has `overflow: hidden`, which clips the ring. Better: the tap's own line cuts the welcome (hush first), a
   Parade version of the line names Teach ("Kip doesn't remember any pets yet. Tap Teach first!"), and the pulse shows.
   general.
3. **Event lines replace the hint and leave no next step.** (Teach: after a Mystery result, Forget, Start over) Polled
   hints (f2/22, 27, 28): the hint ends on "Yes! Kip got it right!", "Oops! Kip guessed wrong. Kip needs more
   examples.", "Kip forgot that one." or "Starting over! Kip's memory is empty." and stays there. A solo student
   pressing Read hears only the result, not what to tap next (rule 4, "say how to act"). Better: after the event line,
   the hint falls back to the current how-to (teachHow(): Next pet / Mystery pet), silently. general.
4. **The "Kip looks..." teaching line plays on every Mystery pet and runs about 2 s behind the screen.**
   (`mystery`, src.html:802-812) Five Mysteries in a row (f2/24): the 4 s line is spoken 4 times (once dropped). Kip
   thinks only 1.2 s, so the look-alike line and Kip's guess are on screen while the voice is still on "looks the
   most alike"; "Kip thinks it's a cat!" comes at 4.5 s, two seconds after the cat face appeared, and the truth waits
   for it. By the third pet it is the slow part of every round. Better: treat it as a teaching line (spoken the first
   time, hint after), and hold the thinking swirl until it ends that first time, so the guess lands right after the
   words. general.
5. **Shelf counters say "8 of 16" when the deck is finished.** (stage, `drawShelves`, src.html:538) Frames f1/09, f1/12
   and every 16-card frame: each shelf shows 16 slots and "8 of 16" while the panel says "That's every example card!".
   A class reads that as eight more cats to find. Better: show only the count with the icon (or "8 cats") and let
   empty slots grow with the wall rather than promising 16 per shelf. general.
6. **"Show Kip more pets" when there are none.** (Parade end, `againHow`) Frames f1/12, f1/13: after all 16 cards and a
   10 of 10 run, the hint (and the first-run voice) still says "Tap Teach and show Kip more pets." Words don't match the
   state. Better: when the deck is empty, a different how-to (for example try a wrong label, or Start over), or no
   prompt to teach more. general.

#### Polish

1. **Kip's guess is on screen for only about 0.6 s in the parade.** (`startParade`, src.html:867-873) Think 0.4 s,
   line 0.3 s, then 0.3 s before the truth badge. The class is meant to call out Kip's guess, but the cat or dog face
   barely shows before the check or X covers the moment. Better: hold the guess about 1 s before the truth (the
   2.6 s per pet can come from a shorter truth hold or walk). general.
2. **The end of the parade is flat on the stage.** (f1/12) Kip shows its idle face at "10 of 10", the same as at "4 of
   10". Better: Kip's screen reacts to the score (a big smile and blinking antenna for a high score, a thinking face
   for a low one), which is the moment the class has been counting toward. general.
3. **In the preview size the pet is tiny.** (680x425 and 800x500, f3/s680x425-wait) Two rows of empty dashed slots per
   shelf take over half the stage; Marmalade is about 55 px wide and Kip about 60 px tall. Better: lay out only the rows
   the wall needs now so the pet and Kip get the floor. general.
4. **The glow on a top-left matched card covers the shelf chip, and the line's end dot sits on the card's name.**
   (f1/05, f1/06: Marmalade; f3/s1920 truth: "Zig.."). Better: end the line at the card's lower edge beside the name,
   and keep the glow inside the shelf. general.
5. **Chart and score text are small for a projector.** (Kip's Chart: axis 11 px, bar values and memory counts 12 px;
   slot numbers 12 px.) The class counts bars together. Better: about 16 px values and memory counts at 1366x768. general.
6. **Teach panel at 1366x768 is half empty.** (f1/01 to f1/09) Below "Kip remembers" there are ~350 px of blank panel
   while the paws are 16 px. Better: a bigger memory counter (larger paws, maybe split by cat and dog icons), which is
   the number the parade chart talks about. general.
7. **Deck used up, Next pet still looks like the main move.** (f1/09) The hint says tap Pet Parade, but the big blue
   button is Next pet; tapping it just repeats the line. Better: pulse Pet Parade when Next pet is tapped with an empty
   deck (and fix the clipped pulse, should fix 2). general.

#### Nits

1. After a label, the hint keeps "Then tap Cat or Dog." for about a second after Cat and Dog are dimmed (until "Kip
   remembers" starts) (f2/20). general.
2. At 680x425 with a card selected, the paws row is cut at the bottom of the panel (f3/s680x425-select). general.

#### Checked and fine

- First screen says what to do (welcome names Next pet); first tap on the stage or Next pet behaves (welcome on a
  stage tap, Next pet's own line otherwise); Sound off then on brings the welcome once; Read during a line reads the
  hint.
- How-to lines once: "Cat or Dog" and "Now tap Mystery pet" each spoken once in five label rounds; "Kip remembers"
  every time; results every time.
- Next pet, Cat, Dog, Mystery pet and Start parade visible and 60 px tall at every size checked, including 375 wide.
- Motion off: no walking, same timing (Mystery 4449 ms off vs 4438 ms on), same scores.
- Parade scores match the spec at 1, 2, 3, 4, 5, 10, 12 and 16 cards; the chart keeps 8 bars and stacks equal runs;
  "10 of 10" on the stage and in the panel match.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, tool.draft.json; bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` (112 KB). Numbers recomputed in Python (independent
k = 1 nearest neighbor over the six features, exact-fraction tie check). Frames and voice runs with
`scripts/drive.py` (held clicks), own profile, ports 9500-9507. Scratch: lens-ttr-teaching (calc.py, calc2.py,
frames f1 to f6).

Counts: blockers 2 (general 1, family 1), should fix 1 (general 1), polish 4, nit 2.

#### Standards (rule 2)

- **E2-ALG-ML-02** (module: "How data trains a machine learning model"): taught by doing. The class labels examples,
  Kip guesses from them, and the parade score and chart show what the data did. Taught, but B1 and B2 both damage
  what the data appears to teach.
- CSTA 1A-DA-07 (crosswalk only) and AI4K12 Big Idea 3 (reference): see P1 and N1.

#### Done when

| # | Result | How checked |
|---|---|---|
| 1 | pass | held clicks stage, Next pet, Cat (8 s gaps): teachWelcome, catOrDog, remCat all spoken; wall `Marmalade:cat` (f4 v-dw1) |
| 2 | pass | 2 cards: 4 of 10; misses Rusty, Luna, Noodle, Pippin, Waffles, Bramble (Python and tool agree) |
| 3 | pass | 16 cards: 10 of 10; chart bars carry their paw counts (2, 11, 12, 16, 2 in f2 parade-runs) |
| 4 | pass | 11 cards: 9, Pippin missed; plus Ziggy: 10, line 29 "more" then line 33 "better" spoken (f4 v-better2) |
| 5 | pass as written | Marmalade as dog: 6 vs 4; Forget puts Marmalade at the deck front; relabeled cat: 4 again (f5 d5). But see B2 |
| 6 | pass | 10 truth frames (f2 ptruth01-10): one line, ending on the card Python picks; truth matches the table; no distance ties at any minimum |
| 7 | pass | five Next/label rounds: catOrDog spoken 1, silent 4; tryMystery spoken 1, silent 3; startHow spoken 1; score line every run (3 of 3); "same" 2 of 2; againHow spoken 1, then silent |
| 8 | pass | Next pet, Cat, Dog, Mystery pet, Start parade on screen and 60 px tall at 680x425, 1366x768 and 375x812 (host iframe, no horizontal scroll) |
| 9 | pass | Motion off: slots 2.64 s apart (1842 to 25642 ms), score 4 |

Facts: the parade score table for N = 1 to 16 (4, 4, 5, 7, 8, 8, 8, 8, 8, 9, 9, then 10), the six 2-card misses and
their look-alikes (Marmalade for Rusty, Noodle, Pippin, Waffles; Bear for Luna, Bramble), Pippin fixed by Ziggy and
Waffles by Pudding all match the spec and notes. Sources and attribution are as stated.

#### Findings

**B1. blocker, family:ml-lab. The dogs are drawn as cats, so the class's labels and the "truth" disagree with what
the class sees.** (src.html `drawHead`/`drawPet`; frames f1 deck06 Rocket, deck10 Pudding, deck12 Ziggy,
f1 pippin-truth, f2 ptruth07 Pippin, ptruth10 Juniper.) Every pet has the same cat body: long whiskers, an upright
curled tail, a small round muzzle. The snout value (.15 to .75) barely changes the muzzle, so it is not the visible
clue the spec says it is. Rocket and Ziggy look like cats; Juniper (dog) and Bramble (cat) look almost the same;
Pippin, the talk-point pet, reads as an orange cat. The core action is "Say it out loud. Then tap Cat or Dog" and
labels are never checked, so a grade 2 class will call Ziggy and Rocket "cat". Then the score table, Done-when 4 and
the Ziggy-fixes-Pippin lesson stop happening. When the truth badge says "Dog" over Pippin, children will decide
Kip was right and the tool was wrong; the notes' question "Why did Kip think Pippin was a cat?" gets the answer
"because it is one". Better: every dog reads as a dog at a glance, including the pointy-eared and short-nosed ones.
Let the snout value drive a clearly longer muzzle with a dog nose pad, draw low whisker values as short stubs or
dots, and give dogs a dog tail. If a cue Kip does not use is needed, that is fine (and a talk point: people use more
clues than Kip). The ear and snout data may need retuning with the drawing; judge it by frames, not numbers.

**B2. blocker, general. The wrong-label experiment the notes suggest makes Kip score higher.** (notes.md "Talk
about it" item 4 and "Good to know" item 3; tool.draft.json outcome "wrong labels make them worse"; calc2.py.)
Labeling Marmalade as a dog raises the parade score at every memory size from 1 to 9 cards (2 cards: 6 vs 4;
5 cards: 9 vs 8; 9 cards: 9 vs 8), and the tool then says "That's more than last time!", the opposite of line 31's
lesson. Root cause: 6 of the 10 parade pets are dogs, so with 1 or 2 right cards Kip (4 of 10) does worse than a
robot that always says dog (6). A Marmalade-as-dog card catches Pippin and Waffles: right answers for the wrong
reason. Other cards behave (at 5 cards, mislabeling any other card drops the score to 6 or 7). Better: data in
which an early wrong label lowers the score (for example a 5 and 5 parade, or retuned Marmalade, Pippin and Waffles),
and notes that name a mislabel that clearly hurts. Rerun the full mislabel table (calc2.py) after any data change.
This changes spec numbers, so it is a spec fix.

**S1. should fix, general. "Show Kip more pets" when no pets are left.** (src.html `paradeHow`, and `startParade`
queuing `againHow`.) After all 16 cards, every parade ends with "Tap Teach and show Kip more pets. Then run the
parade again." In Teach, Next pet then answers "That's every example card! Tap Pet Parade", a loop. Seen in f2
parade-runs and by reading the code (no deck check). Better: once the deck is empty, the parade hint says something
true, such as "Kip has seen every pet. Try Forget, or Start over to teach Kip again."

**P1. polish, general. Nothing on screen invites the class to predict Kip's guess.** (Mystery think phase, 1.2 s;
spec "Who and how" says the class predicts Kip's guesses; CSTA 1A-DA-07 crosswalk.) The prediction lives only in
the notes ("Ask first: What will Kip say?"). Better: during Mystery's think, the hint and line say "What will Kip
guess? Say it out loud!" and the think holds a beat longer, so the class predicts before the look-alike line draws.

**P2. polish, general. Line 10 blames missing examples even when a wrong label caused the miss.** ("Oops! Kip
guessed wrong. Kip needs more examples.") During the wrong-label experiment this points the class at the wrong cause.
Better: when the deciding card's label differs from that pet's real label (the deciding card is known), use a line
like "Oops! Kip remembered that pet wrong."

**P3. polish, general. Line 33 teaches "more" when the data teaches "different".** ("The more examples Kip saw, the
better Kip guessed!") Cards 5 to 9 add nothing (8 stays 8); Ziggy alone fixes Pippin; the notes say "Kip needs an
example like the new pet, not just more of the same." Better: "The more different pets Kip saw, the better Kip
guessed!"

**P4. polish, family:ml-lab. In the parade, Kip's guess shows only 0.6 s before the truth badge.** (`startParade`:
line 0.3 s, hold 0.3 s.) The spec says guesses are shown, not spoken, "so the class can call them out"; in 0.6 s a
class can only react to the check or X. Better: hold the guess about 1 s before the truth and keep 2.6 s per pet by
shortening the walk or the truth hold.

**N1. nit, general.** The spec and code paraphrase 1A-DA-07 as "identify and describe patterns in data to make
predictions"; the standard says patterns "in data visualizations, such as charts or graphs". Kip's Chart is one: a
notes prompt such as "Look at Kip's Chart. What will happen if we teach four more pets?" would use it.

**N2. nit, general.** Notes and spec say Waffles is fixed "only by Pudding". Scout (card 16) also fixes it (distance
.534 vs Marmalade .545), which shows if Pudding is forgotten after all 16 cards. Say "Pudding fixes it first".

#### Guardrails and sensitivity

K-2 teacher led; no hard history, health or cultural content; the only score is the parade tally, which is the
measurement. Language is plain and short for grade 2. Rule 8: no sensitive topics in scope. Nothing to flag for a
sensitivity agent.

<!-- end part -->

## Fix

<!-- part: review-fix.md -->

### Review fix: painted pets (2026-10-29)

#### Cory's note

"the dogs and cats look weird, its mostly the face. otherwise its a good tool."

#### What changed

- All 26 pets are now the painted FLUX portraits in `art/pet-<name>.webp` (360 px tall, cut out, side view). The code
  drawing of the pets (`drawHead`, the parametric body, legs, tail) is gone, along with two color helpers only it used.
- `src.html`, `ART` table: one row per pet with its `art:pet-<name>` picture, width/height ratio, head centre and head
  radius (read off each painting by eye), and a flip flag. Four paintings came back facing left (Marmalade, Inky,
  Pepper, Luna); they are mirrored with `scale(-1 1)` so every pet faces Kip and the way it walks. No pet walks left.
- `petGeom` now describes the painting, so the look-alike line still starts on the head, the Cat/Dog badge still sits
  above the pet (or beside or over the body when there is no room), and the fly to the shelf still works.
- Size trait: picture height is 150 + 100 x size stage units (Pebble and Marmalade about 170, Moose and Bear about
  240), so big pets stand taller. Width follows each painting's own ratio, so nothing is stretched.
- Walking: the leg steps became a gentle 2.5 degree rock on the feet, on top of the existing bob. Both are off when
  Motion is off (`Curio.reduce`: callers pass step 0 and bob 0). Opacity (`o.opacity`, the leaving fade and the fly)
  is unchanged.
- Shelf cards: a head-and-shoulders crop of the same painting, centred just under the head, ear tips in. Bigger pets
  fill a little more of the card (the old size scaling). The fly to the shelf now lands the head exactly where the
  card shows it.
- Accessibility: unchanged. Cards keep their `aria-label` ("Marmalade, on the Cat shelf"), the stage keeps its group
  label, and each pet's group is `aria-hidden` (the SVG equivalent of empty alt, since the card or the spoken line
  already names the pet).
- Pet data rows (ears, snout, whiskers, size, dark, fluffy, plus coat and pattern) are untouched. Kip's guesses are
  identical (checked: Maple still matches Marmalade; Pippin is "cat" with 11 cards, "dog" with 12; Luna is "dog" with
  2 cards; full deck parade 10 of 10).
- `tool.json` sources: the "drawn in code" line now says Kip, the lobby and the chart; added "Illustrations drawn with
  FLUX.1-schnell (Apache 2.0) on a local computer, edited for Curio Class". Same fix in the src.html header comment
  and notes.md ("Everything is drawn in code" was no longer true).
- `preview.svg` regenerated with `scripts/preview.py` (a mystery-pet moment: Maple, Kip thinking, 6 cards on the wall).

#### Sizes

- Paintings: 26 files, 12 to 23 KB each, about 440 KB in all.
- Bundle `teach-the-robot.html`: 1207 KB (was 640 KB), under the 2 MB limit.
- `preview.svg`: 22 KB.

#### Checks

- `python scripts/check_tools.py`: teach-the-robot ok.
- Test hook (`window.__tool`): `drawPet`, `drawPortrait` and `previewSVG` still exported and working; every one of the
  26 pets resolves to an inlined WebP; step adds the rock, opacity carries through, Luna's portrait is mirrored.
- Browser (scripts/drive.py, ports 9311/9312, host 8831), no console errors (one favicon 404 from the narrow host page
  only).

#### Screenshots

`S:/CurioClass-codex-scratch/review/teach-pets/`:
- `shelf-wide-1280.png` all 16 cards, `shelf-names-1024.png` cards with names
- `parade-luna-wide.png` (Luna, the miss with 2 cards), `parade-shadow-wide.png` (dark dog, truth badge on its body)
- `pippin-11-cards-cat.png`, `pippin-12-cards-dog.png`, `luna-mystery-wide.png`, `moose-1024.png`, `fly-to-shelf.png`
- `narrow-380-shelf.png`, `narrow-380-parade.png`
- `preview.png` (the new card art); every frame is in `drive/`

Dark pets (Inky, Luna, Moose, Shadow, Pepper) read clearly against the cream wall, the wood floor and the cream
cards, so no halo was added.

#### Unsure / for Cory

- The paintings no longer change with the clue numbers the way the code drawing did (it drew ear angle, snout length
  and whisker length straight from the data). They were prompted to match each pet's clues, but a few are loose:
  Pebble and Noodle read as fluffy white dogs with floppy ears (fine); Bear's ears are half-floppy; Coco is a short
  coat. Worth a glance that each painting still shows the clue the lesson points at (Pippin's pointy ears and
  Waffles' short nose do).
- Head centres were set by eye. The line and crops looked right in every frame checked; Noodle has the oddest pose
  (face toward the viewer).
- At 380 px wide the pets are small (the layout's minimum scale); faces are still readable but small. That is the
  existing layout, not the art.
- Mid-fly, the shrinking full-body pet briefly overlaps its neighbour card before the card appears (as before with
  the drawn pets).
- `art/prompts.json` still marks every pet `"review": "pending"`; left for the reviewer.

#### Round 2 (after the Final look, final-art.md)

Art (done before this round, not redrawn here): Shadow, Noodle and Pebble are new paintings with natural faces,
side view facing right; Bear, Biscuit, Bramble, Pepper, Pippin, Noodle and Pebble had the leg-gap tint cleaned.

- **ART rows re-fitted:** Shadow 433/360 (head .82, .18, r .15), Noodle 311/360 (.72, .23, .20), Pebble 328/360
  (.78, .24, .20); none flipped. Re-checked every head on a zoomed sheet of all 26 and nudged ten head centres a
  little toward the face (Coco, Smoky, Rocket, Duchess, Ghost, Nutmeg, Pippin, Juniper, Tiger, Bramble, Ziggy) or up
  (Biscuit, Moose), so the line start never lands on an ear or an eye.
- **Look-alike line:** it now starts on the forehead (`petFace`: half a head radius above the head centre, below the
  ears) and the line runs *under* the pet, so a line coming from a card never crosses an ear. The start dot scales with
  the pet (7 px wide screens, 3.5 px at 380 px), so it no longer covers Luna's ear on a phone.
- **Card crops:** `portraitFrame` keeps the head-and-shoulders crop but moves it up when needed so its top edge sits
  just above the top of the painting: every ear tip stays in. Checked all 26 offline and on the wall at 1920, 1280,
  680 and 380; Rocket, Inky, Ziggy and Duchess are whole. The fly to the shelf uses the same frame.
- **Truth badge:** when it cannot go above the pet it now goes beside the pet, left gap first, then the gap between
  the pet and Kip, shrinking to fit (down to 34 px); only if neither fits does a small 34 px badge go over the pet's
  back end. At 680x425 Shadow and Waffles are fully visible (badge to their right); at 380 px it sits left of Shadow.
- **prompts.json:** `"review": "ok"` on all 26 pets.
- Bundle 1207 KB; `check_tools.py` ok; test hook unchanged and working (Maple still matches Marmalade; Pippin cat with
  11 cards, dog with 12; Luna dog with 2). preview.svg regenerated. No console errors (favicon 404 on the host page
  only).

Frames: `S:/CurioClass-codex-scratch/review/teach-pets/round2/` (zooms: z-shelf-1920.png, z-shelf-680.png,
z-pippin-1920.png, z380-luna.png, z-shadow-1366.png, z-quad-1366.png; full frames parade-shadow-680.png,
waffles-10-680.png, parade-luna-680.png, n380-parade-shadow.png, n380-shelf16.png, shelf16-1920.png and the rest;
offline sheets _dots.png and _check.png for all 26).

Still open: nothing blocking. The new Pebble painting has no collar tag (final-art.md polish item 6 is gone with it).
Moose's start dot sits just above the eye on the forehead; fine at every size looked at.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: teach-the-robot

Built 2026-10-27 (build stage, grade 2, ml-lab family, first tool of the family). Status: `tool.draft.json` (no
painted art is planned, but voice clips are not recorded yet, so it bundles only with `CURIO_DRAFT=1`).

#### What was built

- `src.html`: the tool. Teach mode (Next pet, Cat, Dog, Mystery pet, Forget, Start over, the memory wall) and Pet
  Parade (10 pets at 3.5 s each, 10 score slots, Kip's Chart). Everything is drawn in code: lobby, door, shelves,
  Kip, one parametric pet drawing for all 26 pets, icons.
- `kit/ml-lab.js`: the family engine, built to the full family description so the four siblings can use it.
  Reference: `docs/families/ml-lab.md`.
- `voice/lines.json` (41 lines since refine round 1, bank playful-friend), `art/prompts.json` (no assets), `notes.md`, `preview.svg`
  (800 x 500: Maple in the spotlight, the look-alike line to Marmalade, Kip showing "cat"), `tool.draft.json`.
- No existing kit file was changed.

#### How src.html is laid out

In file order: CSS (three page layouts: wide, compact, stack; the panel comes before the stage in the DOM so Tab
reaches panel buttons before wall cards, and the grid puts the stage first on screen), then the script.
- Data: `F` (the six features), `DECK` (16) and `PARADE` (10), each `{id, name, label, coat, pat, v}`; `L` (the
  line table) and `NUM`.
- `state`: mode, wall `[{key, pet, idx, label, arriving}]`, deck (indexes still to show), `mi` (next Mystery pet),
  busy, sel, arrivals (a counter that makes stale lines drop), `teach.spot` / `parade.spot` (the pet in the
  spotlight and its phase: walk, wait, fly, think, guess, truth), running, slots, runs `[{right, mem}]`, `tk`
  (a cancel token), `speed` (tests only).
- Drawing: `petGeom`, `drawHead` (ears blend floppy to pointy, muzzle by snout, whiskers by whiskers, scalloped
  ruff by fluffy), `drawPet`, `drawPortrait` (a wall card), `drawKip` (screen face idle, think, cat or dog; badge
  ok or bad), `ICON` (100 x 100 icons in currentColor, details in `var(--ib)`).
- `layoutFor(W, H)` computes everything in real pixels per stage size: card size (height-aware, 40 to 88 px),
  16 or 8 cards per row, names under cards only at 52 px or more, Kip scale `ks`, pet scale `ps`, door size.
  `build()` draws the static scene; `drawShelves()`, `paintKip()` and `paintDyn()` redraw the moving parts.
- Teach: `nextPet`, `teachLabel`, `finishFly`, `mystery`, `selectCard`, `forget`, `startOver`. Parade:
  `startParade`, `stopParade`. Modes: `settle`, `setMode`, `relayout`.
- `window.__tool` for tests: `teachNow(n, labels)` puts the first n deck cards on the wall at once, `guessFor`,
  `previewSVG(W, H)` (returns `{svg, match}`), `layout()`, `vlog` (the voice log), plus the actions.

#### Tricky parts

- The welcome is deferred while something is moving: its `valid` needs the stage idle and no pet waiting for a
  label, and `teachLabel` calls `V.welcome()` after each card lands.
- `settle()` on a mode change finishes a flying card (it lands), drops a walking or thinking pet and stops a
  parade (a part run adds no bar). Every async step checks `aliveFor(mode)` (the token `tk`) after each await.
- `anim(ms, step, alive)`: with Motion off it jumps to the end but still waits the full time, so the parade keeps
  its 3.5 s rhythm and the same scores. Calm mode places pets at once.
- The look-alike line runs from the pet's head top to the deciding card's lower corner that faces the pet
  (6 px in from the corner, end dot r 5), so it leaves between two names instead of across one. The truth badge goes above the pet when there is room, else to
  its left, else over the body, never over the face.
- Mystery (refine round 1): walk, then the prediction beat (at least 1.8 s), then on the first Mystery pet only
  the "looks the most alike" how line while Kip thinks, then the guess and the line together, held at least 2 s and
  until "Kip thinks" ends (each wait capped, so a missing voice never stalls it), then the truth.
- The hint is the kit's: event lines pass `hint: event + next how line` (helper `both`), and Read reads the hint, so
  both always name the next control. `teachHow()` and `paradeHow()` give the hint on a mode switch; `NEEDS` maps
  each how line to the control it names.
- `rowsFor(cols)`: at 8 cards per row a shelf gets its second row only when it needs one (fuller shelf, plus a free
  slot while cards are left). `drawShelves()` relayouts when that changes. It also keeps a focused card focused
  across redraws (`refocus`).
- Busy buttons use `aria-disabled` (still focusable, the kit's `needs` treats them as off); `steer(from, to)` moves
  focus to the next control when the one in use goes away.
- The bundler inlines `kit/ml-lab.js` between script tags: a literal closing script tag in that file (even in a
  comment) breaks the bundle. It happened once in this build.
- Bundle with `CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` while the tool has `tool.draft.json`;
  without it the bundler silently skips the tool and the old bundle stays.

#### Engine API (short; full reference in docs/families/ml-lab.md)

`MLLab.rng, uni, r2, item, dist, knn(train, item, {features, k}), train('knn' | 'tree' | 'linear', items, opts),
evaluate(model, items, {classes, groupBy, positive, threshold}), glyph, view.confusion, view.scatter,
view.groupBars, version`. This tool uses `knn` with k = 1 over all six features, through `guessFor`. Distance ties
go to the card taught first.

#### Checked at build (2026-10-27, before refine; the parade numbers here are the old parade's, see Refine round 1)

- Done when 1: first tap plays the welcome; Next pet brings Marmalade; Cat files it with line 3.
- Done when 2: 2 cards give 4 of 10, missing Rusty, Luna, Noodle, Pippin, Waffles and Bramble.
- Done when 3: 16 cards give 10 of 10; the chart shows bars with their memory counts.
- Done when 4: 11 cards give 9 (Pippin missed); adding Ziggy gives 10 and line 29 plays.
- Done when 5: Marmalade as dog gives 6 instead of 4; Forget puts the card back at the front of the deck, and
  relabeling it cat gives 4 again.
- Done when 6: 50 Mystery pets (wall sizes 1, 2, 5, 11, 16): each shows one line ending on the card an independent
  `knn` call picks, and the truth matches the table.
- Done when 7: lines 2, 5 and 17 spoken once in a run; result lines every time.
- Done when 8: Next pet, Cat, Dog, Mystery pet and Start parade on screen without scrolling at 680x425, 1280x720,
  1366x768, 760x900 and 375x812 (inside the host iframe; no horizontal scroll). Panel buttons are 60 px tall.
- Done when 9: parade slots about 2.63 s apart with Motion on and off; same score.
- Frames looked at: 1920, 1366x768 (default, Mystery truth, parade mid-run), 1280x720, 1000x625, 800x500,
  760x900, 680x425 (Mystery, parade end with 4 bars), 375x812 (Teach, parade end). No console errors.
- Keyboard: Tab order is mode buttons, Motion, Sound, Read, Next pet, Mystery pet, Start over, then the wall
  cards; Enter selects a card, Delete forgets it and focus goes to Next pet.
- Engine: the teach-the-robot score table and the whole ai-evaluator results table reproduced in Node
  (scratch scripts t1.js and t2.js, not in the repo; the family doc lists the numbers). The three views rendered
  in Chrome with made-up data.

#### Known gaps

- At 680x425 the stage is about 390 x 353, so wall cards are 43 px and their whole-cell hit area 47 px; 60 px
  hit areas are reached from about 1000 px wide.
- At 760x900 the header wraps to two rows (Read on the second); everything still fits.
- Scout ("white with dark spots #3a3a3a") is drawn as a white coat with #3a3a3a spots.
- Next pet and Mystery pet are disabled while a pet waits for its Cat or Dog label (the spec only says buttons are
  disabled while a pet walks or Kip thinks). This keeps one pet in the spotlight at a time.
- During the truth phase the look-alike line passes behind the big truth badge at some sizes. It still ends on
  the right card. When the badge has to sit over the pet (small stages), the pet's small name is hidden under it.
- The first Mystery pet takes about 8 s with voice (prediction, how Kip guesses, the guess); later ones about 5 s.
- Headless Chrome has no speech voice, so spoken timing was checked with the kit's caps, not real audio. Line 33
  ("The more examples Kip saw...") was confirmed queued, but the test switched modes too soon to hear it.
- Voice clips are not recorded yet (`scripts/voice.py teach-the-robot`); the browser voice speaks until then.

#### Refine round 1 (2026-10-28)

What changed, by refine.md item:
- B1: the pet drawing. Dogs: a snout reaching out by the snout value with a big nose pad, tongue and whisker dots,
  round brown eyes, a collar with a tag, ears in a contrasting shade (lighter on dark coats, with a light outline),
  floppy and half ears hang in front of the head, a thick low wagging tail. Cats: whisker pads, pink nose, w mouth,
  slit pupils, long whiskers, a curled S tail. All 26 pets checked in a contact sheet.
- B2: the parade is 5 cats and 5 dogs (Nutmeg, a cat, replaces Rusty; Noodle is retuned to a fluffy white dog).
  Engine unchanged. New table (also in spec.md under "Refine changes" and in notes.md):

  | Cards taught (N) | 1 | 2 | 3 | 4 | 5 to 9 | 10 and 11 | 12 to 16 |
  |---|---|---|---|---|---|---|---|
  | Right labels | 5 | 6 | 7 | 7 | 8 | 9 | 10 |
  | Marmalade labeled dog | 5 | 5 | 6 | 6 | 8 | 8 | 8 |

  Node check: for every N from 1 to 16, every single wrong label of any taught card lowers or holds the score.
  2-card misses: Luna, Bramble (like Bear), Pippin, Waffles (like Marmalade). Ziggy fixes Pippin (card 12), Pudding
  fixes Waffles first (card 10). Snowball as dog with 5 cards: 8 to 6.
- 3 and 20: once the deck is used up, Pet Parade replaces Next pet, empty slots go away, the hints name Mystery pet,
  Pet Parade, Teach or Start over.
- 4: Pet Parade with an empty wall says "Tap Teach first!", no welcome, and the Teach button pulse is drawn inside
  the button (the switcher clips outside shadows).
- 5: every event line carries its next step in the hint (after a Mystery result, Forget, Start over, a new card),
  and a matching how line is spoken once.
- 6 and 18: the prediction beat, then line 6 as a how line on the first Mystery pet; the guess line plays as the
  guess shows.
- 7 and 8: focus stays on the card after Enter; aria-disabled plus `steer` keep focus on a live control.
- 9: header buttons 60 px in this tool's CSS. 10: shelf counts say "3 pets". 11: guess holds 2 s (Mystery and
  parade; parade is 3.5 s per pet). 12: Kip smiles at 8 or more, looks puzzled at 4 or less. 13: only needed rows.
  14: glow stays on the shelf, the line ends on the card's corner. 15: chart axis 14 px, values and memory counts
  16 px, memory counter 34 px with 24 px paws. 16: a hit rect over the whole cell. 17: line 13 reworded.
  19: "Oops! Kip remembered that pet wrong." when the deciding card had a wrong label; line 33 says "different".
- Nits: hint changes at once when Cat or Dog is tapped; paws hidden at the compact layout; stage `role="group"`;
  Next pet and Mystery pet hush a playing line; confusion cells without onCell lose tabindex (engine);
  `MLLab.version` in the family doc; CSTA wording and a chart talk prompt in notes.md; "Pudding fixes it first".

Checked after refine (headless Chrome on ports 9410 and 9412, and Node):
- Scores in the page: 1 card 5, 2 cards 6 (misses Luna, Pippin, Waffles, Bramble), 5 cards 8, 11 cards 9 (Pippin),
  12 cards 10, 16 cards 10; Marmalade as dog: 5 (2 cards), 8 (12 cards); Snowball as dog at 5 cards: 6.
- 50 Mystery pets (wall sizes 1, 2, 5, 11, 16): one line, one end dot, the card an independent `knn` picks.
- Motion off: parade slots 3.52 to 3.56 s apart, 3 cards score 7 as in the table.
- Voice, real clicks: catOrDog, tryMystery, predict, looks, afterMystery, forgetHow, forgotHow, nextHow spoken once
  then silent (heard); events every time; empty-wall Pet Parade speaks only its own line.
- Keyboard: Next pet to Cat, Cat to Next pet (or Pet Parade when the deck is done), Mystery keeps focus, Enter on
  a card keeps it, arrows move, Escape lets go, Delete forgets and focus goes to Next pet, Start parade to Stop and
  back. Real keys: Enter, ArrowRight, Enter selects the second card with focus on it.
- Frames at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (host iframe), looked
  at. No console errors. host.html deleted, no listeners left on 9410 to 9419.
- Engine: t1 (new parade) and t2 (ai-evaluator) re-run in Node, numbers as in the family doc.

#### Refine round 2 (2026-10-28)

- Exit check item: at 680x425 the Pet Parade panel squeezed the hint to 41 px, so three-line hints ran under Start
  parade or Stop. Now the hint never shrinks (`flex: none`) and, at the compact layout, keeps room for three lines
  at 14 px (`min-height: 4.05em`, 57 px) in both modes. Kip's Chart takes what is left of the parade panel (at
  least 72 px; renderChart's floor is 72, and a chart under 56 px of plot keeps only the 0 and 10 labels). The
  compact layout hides the small "7 of 10" under the slots, since the stage shows the same tally large.
- Measured (hint height = its content, panel scrollHeight = clientHeight, so nothing hidden or scrolled):
  680x425 and 800x500 parade mid run, parade end (3 cards), parade end with the deck used up (the longest hint),
  and Teach with the deck used up: hint 57 px, Start parade or Stop at 144 to 204 px. Kip's Chart 104 to 108 px at
  680x425, 179 to 183 px at 800x500. 760x900 and 375x812 (stack) unchanged: the hint grows to its lines and Start
  parade stays on screen.
- Frames looked at: 680x425 parade mid run, parade end with the deck used up, Teach with the deck used up;
  800x500 parade end; 375x812 parade end.
- Wall card hit area at 680x425 not lifted: the stage there is about 390 px wide, so 8 cards per row leave 47 px
  cells, and a bigger hit rect would overlap the next card. It reaches 60 px from about 1000 px wide.

#### Engine changes made after first writing it

- `view.confusion`: the row labels column now fits the longest name, the two titles drop to two lines when
  narrow, and column headers center the glyph and name together.
- `view.scatter`: points at 0 and 1 sit inside the frame.
- Refine round 1: `view.confusion` cells without `onCell` drop their tabindex (view code only; tables unchanged).

#### Next steps

- Record voice clips (41 lines, 10 new or changed in refine round 1), then rename `tool.draft.json` to `tool.json`.
- Siblings: read `docs/families/ml-lab.md` first and check their spec tables in Node before building.

#### For Cory

Nothing needs a decision.

<!-- end part -->

## Art and voice

<!-- part: final-art.md -->

PASS (round 2 re-check, 2026-10-29: should fix 1 and polish 2, 3, 6, 7 fixed; 4 fixed except a small Pebble leftover; 5 Waffles kept by choice, accepted)

#### Round 2 re-check (same agent, 2026-10-29)

Read review-fix.md "Round 2". Bundle rebuilt with `CURIO_DRAFT=1`: 1207 KB, no console errors in 35 shots (favicon
404 on the host page only). Re-shot every frame tied to a finding with the same shot lists; frames in
`S:/CurioClass-codex-scratch/review/teach-final-art/r2/` (frames/, frames-narrow/, art/, work/). Host.html deleted,
nothing listening on 9321, 9322 or 8841. Voice not re-run: no clip or line changed.

1. **Shadow and Noodle: fixed.** Both are new paintings in the set's style: Shadow a natural black Labrador (calm
   brown eye, no blush, no grin; r2/art/c-shadow-face.png), Noodle a white fluffy dog with long floppy ears in side
   view facing Kip (r2/art/c-noodle-dark.png). Both read as dogs at once, on stage and on cards
   (r2/frames/myst5-16-1366.png, myst3-16-1366.png, parade-shadow-1366.png, r2/frames-narrow/n380-shadow-16.png,
   n380-noodle-16.png). Shadow (dark, floppy, long snout, smooth) and Noodle (fluffy, floppy, white) now show their
   clues. The new Pebble is also natural and has no collar.
2. **Line dot on an ear: fixed.** The dot sits on the forehead below the ears and the line runs under the pet: Pippin's
   two pointy ears are both clear (r2/work/z-pippin-1366.png, r2/frames/pippin-11-1920.png), Luna's at 380 px too
   (r2/work/z380-luna.png).
3. **Card crops: fixed.** Rocket, Inky, Ziggy and Duchess keep their ear tips at 1920, 680 and 380
   (r2/work/z-shelf-1920.png, r2/work/z380-shelf.png, r2/frames/shelf16-680.png).
4. **Leg-gap tint: fixed on Bear, Biscuit, Bramble, Pepper, Pippin, Noodle** (0 green or magenta pixels now).
   **Pebble keeps a small leftover:** the gap between its hind legs shows a thin yellow-tan rim
   (r2/art/c-pebble-dark.png; on stage r2/work/z-pebble-legs.png, about 4 x 12 px at 1366x768). Only seen when
   zoomed; polish, known, not done.
5. **Waffles kept:** accepted. A slightly long muzzle for snout .20 is a smaller miss than bat ears against ears .30;
   Kip's guesses do not change.
6. **Pebble's collar tag: gone** with the new painting.
7. **Truth badge at 680: fixed.** It sits beside the pet now; Shadow and Waffles are fully visible
   (r2/frames/parade-shadow-680.png, r2/frames/waffles-10-680.png; at 1366 it sits between Shadow and Kip,
   r2/frames/myst5-16-1366.png).

Lessons still hold: Luna is Dog with 2 cards (line to Bear; r2/frames/luna-2-1366.png, luna-2-680.png), Pippin Cat
with 11 and Dog with 12 (r2/frames/pippin-11-*.png, pippin-12-1366.png), the full deck parade is 10 of 10
(r2/frames/parade-done-1366.png). `art/prompts.json`: all 26 pets "review": "ok".

### Round 1 (FIX: 1 should fix: redraw Shadow and Noodle with natural faces; 6 polish; nothing blocks)

### teach-the-robot: Final look on the painted pets (2026-10-29, fresh cold agent)

Read refine.md, handoff.md, final.md (PASS, round 2) and review-fix.md first. Cory's note: "the dogs and cats look
weird, its mostly the face. otherwise its a good tool." All 26 pets are now painted FLUX portraits.

Tools: `scripts/audit_tool.py` (port 9321, host 8841), then `scripts/drive.py` on 9321 (wide frames) and 9322 (380 px
iframe host on 8841, host.html deleted after). Scratch: `S:/CurioClass-codex-scratch/review/teach-final-art/`
(audit/, frames/, frames-narrow/, art/, work/). Every Chrome and server I started is closed; nothing listens on 9321,
9322 or 8841. Bundle rebuilt with `CURIO_DRAFT=1`: byte-identical to the one on disk (md5 925dfd39...), 1207 KB, under
2 MB; no http(s) src/href, no leftover `art:` tokens; `check_tools.py`: ok. No console errors in 60 shots (one favicon
404 from the host page only). Audit: every size, Motion off, resize, five-click and quick-tap rows clean; the same 4
"welcome not heard" leads final.md already settled (nothing new).

#### Should fix

1. **Shadow and Noodle have cartoon faces, unlike the other 24** (should fix, art). Both have a big white-ringed eye,
   a pink cheek blush and a drawn grin (art/c-shadow-130.png, art/c-noodle-0.png; on stage:
   frames/myst5-16-1366.png, frames/myst3-16-1366.png, frames/parade-shadow-1366.png). The house style asks for
   "natural eyes ... not a cartoon mascot", and the rest of the set (Moose, Bear, Biscuit, every cat) follows it, so
   these two read as from a different book. This is the part Cory flagged (the faces). Noodle is also the oddest
   pose: the body points away with the head turned back over the shoulder, so it reads as walking toward the door
   while looking at Kip. Redraw both with the same prompt plus the house style (Shadow: a black Labrador-like dog,
   floppy ears, long snout, smooth coat; Noodle: a white fluffy dog with floppy ears and a medium-long snout, side
   view facing right), keep the clue values. Both are parade pets, so check the head centre in `ART` again after.

#### Polish

2. **The look-alike line's end dot sits on an ear** (polish). The dot is drawn at the head top, which on the paintings
   is often an ear: Pippin's near ear tip (frames/pippin-11-1366.png, pippin-11-1920.png, zoom
   work/z-pippin-1920-badge.png) and Luna's right ear at 380 px (frames-narrow/n380-luna-2.png, zoom
   work/z380-luna.png, the dot covers most of the ear). Pippin's pointy ears are the very clue the lesson points at.
   Better: end the line a few px above the head (above the ear tips) instead of on it.
3. **Card crops clip some ear tips** (polish). Rocket, Inky, Ziggy and Duchess touch or lose the tip of an ear at the
   card's top edge (work/z-shelf-1920.png, work/z-shelf-680.png, work/z380-shelf.png). The builder aimed for "ear
   tips in". Better: move the crop down a little for tall-eared pets (or per pet in `ART`).
4. **Two small key leftovers between the legs** (polish). Bear has a keyed hole with a thin green-yellow rim between
   the hind legs, Biscuit a faint green sliver between the front legs (art/c-bear-80.png, art/c-biscuit-220.png on a
   dark ground). On the cream stage at real size neither is visible (work/z-bear-legs-1366.png,
   work/z-biscuit-legs-1366.png). No magenta (key) fringe on any pet: 0 to 9 magenta-ish pixels per painting, and
   the greenish counts in cats are their green eyes. Optional cleanup.
5. **A few paintings show their clue loosely** (polish). Checked all 26 against the data rows (art/sheet-bg0.png,
   art/sheet-bg2.png, work/deckgrid0.png, work/deckgrid1.png). Ears, snout, fluffy and dark read right for every pet
   the lesson leans on. Loose: Waffles (snout .20) has a medium puppy muzzle, not a flat face like Pudding; Noodle
   (fluffy .78) looks mostly smooth; Scout (dark .60) is a white dalmatian; Bear's ears (.50) are floppy. Kip's
   guesses are unchanged, so nothing is wrong on screen; only a teacher asking "why did Kip match these?" would see
   the gap. Fold Noodle into item 1; the rest can stay.
6. **Pebble wears a collar with a gold tag** (polish). The house style says no collar tags. The tag is blank (no
   lettering), so it is harmless; visible on its card at every size.
7. **At 680x425 the truth badge covers most of a pet's body** (polish, known from refine for the name). With the
   paintings, Shadow is nearly hidden behind the Dog badge (frames/parade-shadow-680.png) and so is the back half of
   Waffles (frames/waffles-10-680.png). Faces stay clear. Better: a smaller badge at that size, or beside the pet.

Also for whoever closes this: `art/prompts.json` still marks every pet `"review": "pending"`.

#### The pets (extra attention)

- **Faces:** 24 of 26 read as friendly, natural cats and dogs with calm eyes and a small nose, one artist feel (soft
  gouache, dark outline). Every cat reads as a cat and every dog as a dog at a glance, on stage and on the cards,
  including at 380 px (frames-narrow/n380-shelf16.png). Exceptions: item 1.
- **Key surprises still fair and visible:**
  - Luna (black fluffy cat): with Marmalade and Bear on the wall Kip says Dog and draws the line to Bear
    (frames/luna-2-1366.png, luna-2-1920.png, luna-2-680.png, frames-narrow/n380-luna-2.png). Luna is clearly a cat
    (tall pointy ears, cat face) and clearly dark and fluffy like Bear, so the mistake is visible and fair. With 16
    cards she matches Smoky and is right (frames/myst2-16-1366.png).
  - Pippin (clearly a dog, pointy ears): 11 cards, Kip says Cat via Marmalade (frames/pippin-11-1366.png, -1920,
    -680); 12 cards, Ziggy is on the wall and Kip says Dog (frames/pippin-12-*.png). Pippin and Ziggy are painted as
    the same kind of fox-like dog, Pippin's ears are upright and pointy like a cat's: the lesson reads.
  - Maple matches Marmalade, Waffles matches Pudding (frames/myst0-16-1366.png, waffles-10-*.png); full deck parade
    10 of 10 (frames/parade-done-1366.png).
- **Dark pets:** Inky, Luna, Pepper, Moose, Shadow, Coco and Bear all read against the cream wall, the wood floor and
  the cream cards (frames/deck02-1366.png, deck13-1366.png, deck14-1366.png, motionoff-moose-1366.png,
  frames-narrow/n380-deck13.png).
- **Size, stretch, blur:** heights follow the size clue (Pepper and Marmalade small, Moose and Bear tall); width
  follows each painting's ratio, nothing stretched; 360 px sources stay sharp at 1920x1080 (frames/shelf16-1920.png,
  pippin-11-1920.png). No pet is cut off on stage at any size checked.

#### Frames looked at

audit/: size-* at all 8 sizes, state-mode-pet-parade-* at all 8, calm-1366x768. frames/: deck00 to deck15 at
1366x768 (every deck pet arrived), myst0 to myst9 with 16 cards (every parade pet at the truth), luna-2, pippin-11,
pippin-12, waffles-10 at 1366, 1920 and 680; shelf16 at 1366, 1920, 680, 1280, 760; parade-shadow at 1366, 1920,
680; parade-done, motionoff-moose, fly, walk-mid at 1366. frames-narrow/ (380 wide host): Bear, Inky, Moose, Pepper
arriving; Luna 2 cards, Pippin 11, Shadow and Noodle with 16; full shelf; parade at Luna. art/: contact sheets of all
26 paintings on cream, white and dark grounds, and zooms.

Known and left (from final.md, still true): the look-alike line can cross a neighbouring card or name (frames/myst4-16-1366.png
crosses Biscuit and Pudding); at 1920 the line passes behind the truth badge (work/z-pippin-1920-badge.png); voice
was not re-run because no clip or line changed.

<!-- end part -->

## Finish check

<!-- part: final.md -->

PASS (round 2 re-check, 2026-10-29: the 3 should fix items and polish item 6 are fixed; polish 4, 5 and the line over dog pictures are known, not done)

### teach-the-robot: Final look (round 1, 2026-10-29, fresh cold agent)

Read handoff.md and refine.md (Refine PASS, round 2) first. Bundle rebuilt with `CURIO_DRAFT=1` (634 KB on disk 652 KB,
byte-identical to the committed bundle). 41 lines in voice/lines.json, 41 clips; every line's `clip_name()` file exists,
and every clip is under the kit's hold cap (2.5 s + 80 ms per character; the longest, the Teach welcome, is 7.34 s
against 9.38 s). Drawn in code, no `art:` tokens, no people.

Tools: `scripts/audit_tool.py` on ports 9231/9232 with host port 8814 (audit.md: 4 leads, all "welcome not heard" after
a first tap on Pet Parade, Next pet, Mystery pet or Start over; every size, state, Motion off, resize, five-click and
quick-tap row clean). Then `scripts/drive.py` on 9231 (voice) and 9232 (frames), host on 8814 for 375 wide (host.html
deleted after). Voice runs wrapped `window.Audio` to log each clip's start, end or cut, and matched each played clip's
data back to its mp3 file, so every played clip is identified by its content, not by the log's text. Scratch:
`S:/CurioClass-codex-scratch/final/teach-the-robot/` (audit/, frames/, vframes/, work/). Every Chrome and server
closed; nothing left listening on 9231, 9232 or 8814.

#### Should fix

1. **Read on a two-part hint plays the browser voice, not a clip** (should fix, general; K-2 rule "every fixed line has
   its clip"). Most hints are two lines joined (`both()`: "Kip remembers: that one is a cat! Now tap Mystery pet. Kip
   will guess!", every Mystery result, Forget, Start over, every parade end). Read speaks `#hint` as one string, which
   has no clip, so the kit falls back to speechSynthesis: a different, robotic voice in a tool that otherwise speaks
   only Laomedeia. Seen: v-read-pend (Read after a parade end: no clip started, `speechSynthesis.speak` called with
   "Kip got six out of ten right. Tap Teach and show Kip more pets. Then run the parade again."). Single-line hints
   (v-first-read, v-read-off, v-read-mid) play their clip. Fix: pass `read: () => [...]` to `Curio.voice` returning
   the hint's lines as a list (the kit plays a list part by part, each with its clip); keep the hint text as is.
2. **The skipped Teach welcome arrives late and is cut, so the premise is lost** (should fix, general; audit lead
   confirmed). The natural first tap is Next pet (the screen says "Tap Next pet"). Its own line plays, the welcome is
   skipped, and it is queued again when the first card lands, after "Kip remembers" (about 8 s into the lesson). The
   recorded welcome is 7.3 s, so the next Next pet hushes it: v-teach5 (6 s pace) played 3.05 of 7.34 s; v-read-combined
   1.04 s (cut by Read). It is marked said when it starts, so "Kip is a robot that learns from examples" is never heard
   whole, and it plays after the class has already started, the late-welcome case the audit warns about. With the
   browser voice this passed; the real clip's length is what breaks it. Fix: on a first tap of Next pet, play the
   premise first (a short welcome line before "Is it a cat or a dog?", recorded), or drop the late welcome after a
   landing and leave it for Read; either way, no welcome after the class has begun.
3. **The look-alike line crosses the next card's name** (should fix, general; BUILD "Labels and badges never
   overlap"). When the deciding card is first on its shelf and the pet is down and to the right, the line leaves the
   card's lower right corner and runs straight through the name of the card beside it: "Bear" reads "?ear" in
   mtruth-1366x768, mtruth-800x500, mtruth-1000x625, mtruth-760x900 (zoom: work/z1.png). Not seen at 680x425 or 375
   (no names). Fix: end the line at the card's bottom edge centre when a name sits to the side, or route the last
   segment below the name row.

#### Polish

4. **First Mystery pet: 10 s of back-to-back talk before the truth** (polish, general). Tap at 1.4 s, prediction
   2.2 to 4.9 s, "Kip looks for..." 5.0 to 9.3 s, guess 9.4 s, truth 11.4 s, then "Yes!" and the how line to 17.9 s
   (v-mystery5). It works and is spoken once, but it is the slowest moment in the tool; a class sits through 9 s of
   narration after its own guess. Better: let the prediction beat end when its clip ends (it already waits), and start
   "Kip looks..." while the line draws instead of after, so the guess lands about 2 s sooner.
5. **How lines cut at a teacher's pace and never heard whole** (polish, general). "Now tap Mystery pet. Kip will
   guess!" starts about 3 s after Cat (after "Kip remembers" ends) and needs 3.5 s; the next Next pet cut it at 3.15 s
   (v-teach5). "Tap Mystery pet again, or Next pet to teach Kip more." starts 2.3 s after the truth and was cut at
   0.79 s by the next Mystery pet (v-mystery5). Both stay in the hint, so nothing is lost for Read, but the spoken
   once-only instruction is usually clipped. Better: start the how line right after the event line with no extra gap,
   or let a cut how line come back once on the next idle moment.
6. **Kip's Chart memory counts collide at two digits** (polish, general). Under the bars, "12" runs into the next paw
   icon (the "12" touches the paw before "16") at 1366x768 (work/z3.png), 1280x720 and 1920x1080. Better: center the paw and number as one group
   under each bar, and shrink or drop the paw when the slot is narrow.
7. **The late welcome replaces the two-part hint** (polish, general). After the first card lands, the welcome sets the
   hint to "This is Kip... Tap Next pet to show Kip a pet." while one card is on the wall (v-read-combined frame). It
   still names Next pet, so it is not wrong; fixing item 2 removes it.

Known and left (from refine, still true): truth badge over the pet's small name at 680x425; wall card hit area 47 px at
680x425; Teach panel scrolls 24 px with a card selected at 680x425; Forget sits at the bottom edge at 760x900 (the
page scrolls).

#### 1. Frames (all looked at)

audit/: size-* at all 8 sizes, state-mode-pet-parade-* at all 8, calm-1366x768. frames/: default, waiting, mguess,
mtruth (wrong label), selected, deckdone, pmid, pend (three runs 6, 10, 8), pempty at 1366x768, 680x425 and 375x812
(host); default, mtruth, pend, deckdone, selected at 800x500, 1000x625, 1280x720, 1920x1080, 760x900; default, mtruth,
pmid at 1366x768 with Motion off. vframes/: the end frame of each voice run. No horizontal scroll at any size, main
controls on screen, every hint whole, no placeholders. Pets: every dog reads as a dog (snout, nose pad, collar) and
every cat as a cat (whiskers, slit eyes); Marmalade on the Dog shelf in the wrong-label state is the intended lesson.
Text is drawn on flat scene color, not on pictures: no contrast issue on art. Only item 3 and item 6 seen.

#### 2. Art against the spec

No `art:` tokens and no art files (art/prompts.json has none); everything is drawn in code, one consistent flat style.
Nothing to check against an art spec; no people.

#### 3. Voice with the real clips

Every played clip matched its line (by content); played length = file length + 50 to 100 ms in every uncut case, so
nothing is truncated in the files. No clip ran into another line: the kit stops one before the next starts, and the
only cuts are hushes from a newer tap or Read (items 2 and 5). The browser voice was never used except Read on a
two-part hint (item 1). Clips never played in these runs (wrongLabel, afterMysteryAll, empty, allCards, the other
score lines, more, fewer, better, againAllHow) exist, match their text by hash and fit their cap.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| catOrDog (Next pet x5) | how | 1 | 1 |
| remCat (Cat x5) | event | 5 | 5 |
| tryMystery | how | 1 | 1 (cut at 3.15 of 3.53 s) |
| teachWelcome (after first-tap Next pet) | welcome | 1 whole | 1, cut at 3.05 of 7.34 s (item 2) |
| predict (Mystery x5) | how | 1 | 1 |
| looks | how | 1 | 1 |
| thinkCat / thinkDog | event | 5 | 5 (3 + 2) |
| right / wrong | event | 5 | 5 (4 + 1) |
| afterMystery | how | 1 | 1 (cut at 0.79 s) |
| forgetHow (select x5) | how | 1 | 1 |
| forgot (Forget x5) | event | 5 | 5 |
| forgotHow | how | 1 | 1 |
| paradeWelcome, startHow | welcome, how | 1, 1 | 1, 1 |
| score line (parade x5) | event | 5 | 5 |
| same as last time | event | 4 | 4 |
| againHow | how | 1 | 1 |

First taps (fresh page each): stage tap, welcome clip at 1341 ms right after the tap; Tab key, welcome; Pet Parade
with an empty wall, only "Tap Teach first!"; Read, the hint (welcome text) by clip; Sound, nothing, then Sound on
brings the welcome once; Next pet, only its own line (then item 2). Stale (0.2 s taps through Next pet, Cat, Next pet,
Mystery pet, Pet Parade, Teach, Start over): each line cut at its moment, only "Starting over!" and "Tap Next pet"
play to the end, in order. Read cuts a playing line and plays the hint, works with Sound off; after Read a mode change
speaks at once. Liveliness: no take flagged flat by the reading; timing gives no take a reason to redo.

#### 4. Full run, solo student and teacher projecting

Solo student: the first screen and the welcome say Tap Next pet; Cat or Dog is asked out loud; every waiting moment
names its control in the hint and once by voice. A student who starts with Next pet never hears what Kip is (item 2).
Teacher projecting at 1366x768 and 1920x1080: cards, names, slots and the score box read from the back; the chart
numbers are readable apart from item 6; the parade's 3.5 s per pet gives time to call out each guess. The flattest
spot is the first Mystery pet (item 4). Scores in the page: 2 cards 6 of 10 (five runs), 12 cards 10, 16 cards with
Marmalade as dog 8: as the spec table.

#### 5. Contract

One file, 634 KB with all 41 clips (under 2 MB). No console errors or exceptions in any audit or drive run (the only
log line is the host page's favicon 404). The only http string in the bundle is the SVG namespace; clips are data URIs;
no network requests.

#### Re-check (round 2, 2026-10-29, same agent)

I treated final-fix.md as claims and checked each one. Rebundled with `CURIO_DRAFT=1` (638 KB; the working kit/curio.js
now has a `hold` option this tool does not use). drive.py on 9231 (voice, 18 runs) and 9232 (frames), host on 8814
for 375 wide (host.html deleted after). No console errors or exceptions in any run (the only log line is the host
favicon 404). Nothing left listening; every Chrome closed. Frames: frames2/ (r2-mguess, r2-mtruth, r2-mguess10 with 10
cards, r2-pend at 1366x768, 680x425, 800x500, 1000x625, 1280x720, 1920x1080, 760x900 and 375x812, r2-pend1 at
1366x768 and 1920x1080) and vframes2/ (the end frame of each voice run), all looked at.

1. **Read on two-part hints: fixed.** Read after Cat, a right and a wrong-label Mystery result, Forget, Start over,
   a parade end and a parade end with the deck used up (v-read-cat, -myst, -wrong, -forget, -over, -pend, -pendall):
   each plays two clips, the event line, then the how line, matched by audio content. `speechSynthesis.speak` was
   never called in any of the 18 runs. Read with a single-line hint and with Sound off still plays its one clip.
2. **Teach welcome: fixed.** It no longer plays after a card lands: a first tap on Next pet, then five Next pet and
   Cat pairs at a 6 s pace, never brings it (v-first-next, v-teach5). A plain first tap plays it whole at 1.34 s
   (v-first-stage). Cut at 2.63 s by Next pet, it plays again whole (7.42 s) at the next Teach entry (v-cut-mode). Cut
   by Sound off, it plays whole when Sound comes back on (v-cut-sound). Cut by Read at 1.63 s, it plays whole at the
   next Teach entry (v-cut-read). The cut Pet Parade welcome gets the same treatment. One trade-off, which I accept: a
   class that starts with Next pet now hears the premise only by Read or on its first return to Teach, never cut
   mid-sentence. The hint and the first how line still say what to do.
3. **Look-alike line over a name: fixed.** With names shown, the line now ends just under the deciding card's own
   name, and any name it still crosses is redrawn whole on top: "Bear" (mtruth) and "Pebble" and "Rocket" (mguess,
   mguess10) read whole at every size; at 680x425 and 375 there are no names and the line ends on the card corner.
   **Cat card line over Dog card pictures (polish, general, known, not done).** From a Cat card the line crosses the
   Dog shelf, through Pebble's face (mguess, every size) or Pebble and Rocket (mguess10). I judge this acceptable: the
   gold glow and the end dot sit on the deciding card, so the line reads as ending there, and no name or label is
   hidden. Still, a child could take the dog it passes over as the match. Better: draw the line under the cards (or
   fade it where it crosses a card) so only the deciding card has it on top.
4. **Chart memory counts (polish item 6): fixed.** Counts are centered under each bar. When two-digit counts leave no
   room, one paw sits at the left of the row (1366x768, 1280x720, 1920x1080, 760x900); otherwise each bar gets its own
   paw (680x425, 800x500, 1000x625, 375). No count touches a paw or another count. With one paw at the row's left, the
   link between paw and pets remembered is a little weaker, but still readable.

**Regressions (voice counts, real clips):** Next pet x5: catOrDog 1, remCat 5, tryMystery 1. Mystery x5: predict 1,
looks 1, guess 5, result 5, afterMystery 1. Select and Forget x5: forgetHow 1, forgot 5, forgotHow 1. Parade x3: score 3,
same 2, againHow 1, paradeWelcome and startHow 1 each. Stale 0.2 s taps: each line cut at its moment, the order follows
the actions. No played clip ran past its moment; every uncut clip played its full length. Scores: 6 (2 cards), 10
(12), 8 (16 with Marmalade as dog), 10 (16), as the spec. No horizontal scroll and no hint clipped in any re-shot frame.

Still open as polish (known, not done): item 4 (the first Mystery pet's 10 s of narration) and item 5 (how lines cut at
a teacher's pace; tryMystery cut at 3.15 of 3.53 s and afterMystery at 0.8 s, as in round 1). Item 7 is gone with
item 2: the hint after Cat now stays "Kip remembers... Tap Next pet to show Kip a pet."

<!-- end part -->

<!-- part: final-fix.md -->

### teach-the-robot: Final look fix (round 2, 2026-10-29)

Scratch: `S:/CurioClass-codex-scratch/final/teach-the-robot-fix/` (frames/, voice/, work/). drive.py on Chrome 9261 (voice) and 9262 (frames), host on 8817 for 375 wide; all closed, host.html deleted. Bundle 638 KB (under 2 MB), 0 console errors (only the host page's favicon 404). voice/lines.json unchanged and equal to `allLines()` (41 lines, 41 clips, every line has its clip).

1. Read on two-part hints: `Curio.voice` now gets `read: readParts`, which splits the hint into its own lines (longest match from `allLines()`, the whole text if it does not split), so the kit plays each part's clip in order. Verified with Read after Cat, a Mystery result, Forget, Start over and a parade end (voice/v-read-*.json): two clips each, in order, `speechSynthesis.speak` never called.
2. Teach welcome: dropped the `V.welcome()` after a card lands (the late one); a welcome skipped by a first tap now waits for its kit moment (next mode entry, Sound on). Added `unsayCut()`: a welcome whose log entry is `cut` is taken out of `V.said` before the next `V.welcome()` and before a Sound click, so a cut welcome is not counted as said. Verified: first-tap Next pet and 5x Next pet/Cat at 6 s pace, the welcome never plays (v-first-next, v-teach5); stage tap plays it whole at 1.3 s (v-first-stage); cut at 2.6 s by Next pet, it plays again whole (7.4 s) at the next Teach entry (v-cut-mode); cut by Sound off, whole again on Sound on (v-cut-sound); stale taps clean (v-stale).
3. Look-alike line: with names under the cards it now ends on the plank just under the deciding card's own name (centred), so it never enters its shelf's name row; without names (small sizes) it keeps the corner. A name the line still crosses (a Dog-shelf name under a Cat card's line) is redrawn on top on a shelf-colored patch, so it stays whole. Looked at mguess, mtruth (Marmalade first on the Dog shelf) and mtruth8 (Inky, 10 cards) at 1366x768, 1000x625, 800x500, 760x900, 1280x720, 1920x1080, 680x425 and 375x812: "Bear", "Inky" and every other name read whole.
4. Chart counts: each count is centred under its bar; the paw goes beside it only when every count has room for paw plus number, else one paw sits at the left of the count row. Looked at pend (counts 2, 12, 16, 10 to 14) at all 7 sizes plus 375x812, and one-digit runs at 1366x768 and 1920x1080: no count touches a paw or another count; the 4-bar embed keeps per-bar paws.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: review-fix.md folded in (last changed 2026-10-29)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
- 2026-11-25: final-art.md folded in (last changed 2026-10-29)
- 2026-11-25: final.md folded in (last changed 2026-10-29)
- 2026-11-25: final-fix.md folded in (last changed 2026-10-29)
