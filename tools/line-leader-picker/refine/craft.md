# Craft lens: line-leader-picker (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/line-leader-picker/line-leader-picker.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/line-leader-picker/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/line-leader-picker/craft/frames/` (shots in `craft/shots.json`, Chrome port 9883, held
clicks 0.12 s, Sound on).

Counts: blocker 0, should fix 3, polish 3, nit 4.

## Findings

1. **Is It Fair?, check answers: the feedback for an answer plays after the next question, so it reads as the
   answer to the wrong question.** `src.html:1334-1340`: on the first answer to each chip, `V.how(next, {now: true})`
   speaks the next question ("Was any friend left out? Tap thumbs up for yes, or thumbs down for no.") first, and
   only then the feedback for the question just answered ("The chart agrees." + evidence line). A pre-reader hears
   "Was any friend left out? ... The chart agrees." and takes "agrees" as the verdict on Q2. With a 6 s tap pace the
   first answer's evidence line was then dropped (`q1C ... dropped, newer`). Seen: `craft/frames/v4-checkx5` log
   (16114 q1 how spoken, 21497 agree, 22249 q1C dropped). Better: feedback first (event, now), then the next
   question queued behind it. **should fix**, general.

2. **Is It Fair?, Q2 evidence line names "that friend" when several friends are left out and none is selected.**
   `src.html:1329`: Q2 with any zero uses the `left` line, "That friend waited all month and never led. Being left
   out feels sad." It is the classmate-tap line; after a Q2 answer no friend is picked, and in rule C usually 5 to 10
   friends are at 0 (my seeded run: 9 left out, `craft/frames/f1-fair-full`, evidence "Yes: 9 left out"). The spoken
   line does not match the screen. Better: a Q2 line built from the count ("n friends never got a turn", which
   already exists as `zeroN`/`zeroOne`), and keep `left` for the classmate tap. **should fix**, general.

3. **Compact layouts: the gold stars, the focus of the tool, shrink to 7 to 8 px specks.** `src.html:229` (`.star
   {width:8px}` at short heights), `src.html:348` (7 px at under 600 wide), stack columns 15 to 17 px wide. At
   680x425, 800x500 and 375 wide the sticker chart reads as faces plus numbers; a 2-star column is two dots in the
   corner of the cell (zoomed: `craft/zoom-fairc-680.png`, from `audit-r1/state-fair-c-680x425.png`;
   `craft/zoom-changed-375.png`, Ant's 20 Before outlines are a hatched bar). The preview must be readable and
   inviting (STANDARDS, Sizes); here the "chart shows at a glance" idea is lost in the 16:10 preview. Better: in the
   5x4 and 10x2 banks, give the stack the width the count number does not use (or stars as a short row of 12 px
   stars), so each sticker is visible. **should fix**, general.

4. **Q3 has three different wordings.** On the chip: "Extra turns while a friend got none?" (`src.html:846`); spoken
   and in the hint: "Did someone lead more than once while a friend got none?" (`L.q2`); in Our chart: "Extra /
   none?" (`src.html:527`). The spec's wording is the spoken one. Anything shown twice should match (POLISH);
   "Extra turns" is also vaguer for grade 2. Better: the chip heading uses the spoken question (or a shortened form
   with the same words), the summary column "Led twice, one none?" or the picture only. **polish**, general.

5. **Make a Rule / Change a Step: the tile's own name plays after "Tap Run".** `src.html:1074-1076`: when step 2 is
   chosen and `runReady`/`chRun` is not yet heard, the how line is spoken now and the tile's name is queued behind
   it, so the student hears "Tap Run to play our month." then "The leader stays at the front." about 2 s after the
   tap (`craft/frames/v2-step2x5` log: tap at about 3.8 s, runReady 4012, tile2 6093). If they tap Run straight
   away, the tile name starts after the month is already playing. Order should follow the action: tile name first,
   then the how line. **polish**, general.

6. **Is It Fair?, the hint names the Turn Machine while it is hidden.** `src.html:1285`: `fairRule` sets
   `hint('machine')` ("The Turn Machine does just what our card says.") for the 1.5 s month, but the machine art and
   rule card are hidden in this mode. Better: a fair-mode line ("Rule C is playing its month.") or keep the previous
   hint. **polish**, general.

7. **Lines that can never play are in `voice/lines.json`.** `tie11` to `tie20` (two friends with 11 or more turns
   need 22 or more days), `most1` (`resultParts` returns "everyone" first when the top count is 1) and `zero20`
   (someone always leads): 12 clips the voice step would record for nothing. Checked by reading `resultParts`
   (`src.html:1203-1211`). **nit**, general.

8. **Short layouts: Fair, Not fair, Our chart and New month are icon-only with no tooltip.** At 680x425 to 1000x625
   (`src.html:249-251`) the text is set to `font-size:0`; the accessible names survive, but there is no `title`, and
   the spec asked for labels as tooltips. The icons themselves render (`audit-r1/state-fair-c-680x425.png`).
   **nit**, general.

9. **Our chart: the voice says "Tap Close" but the control is a bare "×".** `L.fSummary` (`src.html:617`). A
   pre-reader hears a word that is not on screen. Better: "Tap the X to go back to the rule cards." **nit**, general.

10. **Run button text contrast at the top of its gradient is 4.40:1** (white on `#33884f`, 15 px bold, not large
    text); 6.53:1 at the bottom. `src.html:124`. Average passes; a flat `#1d6b3a` or a darker top stop removes the
    doubt. **nit**, general.

## Contract and access (clean)

- One file, 1,271,577 bytes (under the 2 MB goal). No `http` URL, `fetch` or XHR in the bundle; Resource Timing
  listed 0 entries after a full Make month and a Fair month (`p2-fairframes`, `f1-fair-full`). No console errors or
  exceptions in any of my 14 shots or in the audit. Kit used (`Curio.voice`, `Curio.tone`, motion, header buttons).
- Frame times at 1366x768 (headless, GPU off): a Make run, 300 frames, median 16.7 ms, max 16.8 ms, none over 33 ms;
  a Fair month's sticker pops, 150 frames, max 16.7 ms.
- Keyboard: Tab order is mode buttons, Motion, Sound, Read, step tiles, run buttons, then the 20 classmates (panel
  before the long list). Enter on a step-1 tile then Tab and Enter on a step-2 tile builds the rule; focus stays on
  the tile through the step-2 rebuild; focus ring 4 px solid (`k1-tab`). Escape closes both overlays. Who overlay
  takes focus on its first button; Our chart makes the chart inert and focuses Close.
- Targets: 60 px on tiles, run buttons, classmates, thumbs and verdicts; kit header buttons 44 px (audit clean).
- Color never alone: zero columns have a dashed ring and the waiting pose; Not fair has thumb plus cross; Before is
  dashed and has its count.
- Motion off: no fly-star, arrive or pop classes ever applied; day 1 about 1220 ms, then 454 to 469 ms per day, same
  as Motion on (`m1-calm-run`). Lamps' breathing loop stops under `.calm`.
- Lines: every value in the line table (including the 19 generated `monthZeroN` hints) is in `voice/lines.json`
  word for word and the reverse; no duplicates.
- Art: all 47 `art:` tokens have a prompts.json entry, none unused; all are animals or objects, `people:false` is
  correct.
- Words: no em dashes in src, notes, spec or lines; "Curio Class" only in full. Nothing is stored; notes say so.

## Standard voice check

Sound on, Motion on, held clicks. Logs in each shot's output (`craft/frames/*.png` named as below).

| Line | Kind | Expected | Spoken | Run |
|---|---|---|---|---|
| tile0 / tile1 (step 1 tiles) | event | 5 | 5 | v1, tiles 2.5 s apart |
| step2 | how | 1 | 1 (then dropped 1, silent 3) | v1 |
| tile2 / tile3 (step 2 tiles) | event | 5 | 5 (first one late, finding 5) | v2 |
| runReady | how | 1 | 1 (then dropped 1, silent 3) | v2 |
| friend name + "led one time." | event | 5 | 5 and 5 | v3, 4 s apart |
| agree (Q1 re-answered) | event | 5 | 5 | v4, 6 s apart |
| q1C evidence | event | 5 | 4 (first dropped behind the next question, finding 1) | v4 |
| q1 (next question) | how | 1 | 1, then silent | v4 |

- Stale lines (v5, taps 0.2 s apart through tile, tile, Run, classmate, Change mode, Make mode, New month): every
  older line dropped or cut by hush; the last spoken line ("The Turn Machine does just what our card says.") fits the
  running month; final hint "Tap Pause, One day, or To the end." Clean.
- First tap: stage tap gets the welcome at once (v7); a key (Tab) gets the welcome (v8); tiles, classmates, mode
  buttons, Read and Sound as in the audit table. Tile and classmate first taps skip the welcome (BASELINE 16); the
  premise stays in the hint and Read and returns in the Who answer lines. Not reported.
- Read (v6): Read during a tile line cuts it and speaks the hint; Read with Sound off still reads; a mode change 0.5 s
  after Read starts the Change welcome at once. Clean.
- Order (v9): lines followed the taps; classmate taps 0.6 s apart drop the older classmate's unstarted count (as the
  spec asks); the only order fault is the tile name behind its how line (finding 5) and check feedback behind the
  next question (finding 1).
- Done when 8 (no per-day line during a run) and 9 (five tile taps 2 s apart, step2 and runReady once) hold.

## Audit pilot

- Leads confirmed: none of the audit's leads became a finding.
- Leads wrong: "text under 10 px" on Motion, Sound, Read and on Fair, Not fair, Our chart, New month at short sizes
  (the icons render through `::first-letter`; names are intact; only the missing tooltip is a nit, finding 8). The
  375 "overlap" rows (count over classmate button) are by design: the classmate button fills the cell and the count
  sits in its padding, readable on the frame. "Welcome not heard" after tile and classmate first taps and the mode
  welcome cut by a second quick tap are BASELINE 16 cases, not reportable. The classmate "has not led yet" lost 1 of 5
  at a 2 s pace is the newer tap of the same friend replacing it (spec: newer drops older); at 4 s all 5 played.
- Missed by the audit: the stars shrinking to specks in the compact charts (finding 3; it checks text, not drawn
  marks), the check feedback playing after the next question (finding 1; its walk taps each control once, not an
  answer sequence), the Q2 line's wording against the state (finding 2), the three Q3 wordings (finding 4) and the
  unreachable recorded lines (finding 7).

Nothing here is cultural, Native or hard history; no sensitivity review needed from this lens.
