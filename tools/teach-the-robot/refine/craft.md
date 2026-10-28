# Craft lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json, art/prompts.json, kit/ml-lab.js and
docs/families/ml-lab.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` (117,020 bytes).
Driven in muted headless Chrome (own profile, ports 9520 to 9524) with `scripts/drive.py` and a scratch CDP runner
with held clicks (120 ms). Headless Chrome has no speech voices, so the runner stood in a fake `speechSynthesis`
(about 70 ms per character at rate .95) to get real-length lines and their start and end times against the state.

Counts: blockers 0, should fix 6 (general 6, family 0), polish 3 (general 3), nits 4 (general 2, family 2).

## Should fix

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

## Polish

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

## Nits

1. The stage `<svg id="sv" role="img">` holds the focusable wall-card buttons; `role="img"` hides its children from
   screen readers. `role="group"` with the same label keeps the cards reachable. src.html:149. Tag: general.
2. A line already playing runs past its moment: in run stale-label "Kip remembers: that one is a cat!" (Inky) kept
   playing as the next Mystery pet walked in, and line 6 for that pet was then dropped as stale. Only with fast taps;
   the kit does not cut a playing line on `dropQueued`. Tag: general.
3. Engine: `view.confusion` without `onCell` removes the cells' `role` but leaves `tabindex="0"`, so Tab stops on
   cells that do nothing. kit/ml-lab.js:300-314. Tag: family:ml-lab.
4. Doc: docs/families/ml-lab.md does not list `MLLab.version` (exported, kit/ml-lab.js:388). Tag: family:ml-lab.

## Checks that passed

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

## Standard voice check

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

## Frames and runs looked at

drive.py sizes run (Teach with 16 cards at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900; Pet
Parade at 680x425 and 1366x768; no horizontal scroll at any size); kb-tab4, kb-tab5, kb-tab8, kb-cardsel, kb-afterdel,
kb2-cat-focus, kb-680-card; calm-walk, calm-think, calm-truth, calm-p-walk, calm-p-end; rep-teach after5 and
after-myst; rep-parade run1 to run5; rep-empty end; rep-parade-empty end; the ft-* first-tap frames.
