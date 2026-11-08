# Craft lens: worry-size-sorter (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/worry-size-sorter/worry-size-sorter.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/worry-size-sorter/craft/out/` (shots1.json, shots2.json beside it).

## Contract
- One file, 1.28 MB (under the 2 MB goal). No `fetch`, XHR or dynamic import in the bundle; the resource list after
  visiting all four modes is empty (`net` shot). Kit used (`Curio.voice`, `Curio.tone`, motion, theme). No console
  errors in any of my 20 shots or the audit.
- Frame times at 1366x768: Box breathing running 16.7 ms median, 16.8 ms p95 and max over 5 s; Sort idle with the
  daylight and cloud loops 16.7/16.8 ms (`fps-breath`, `fps-sort-drag`). Headless Chrome, GPU off, so a floor, not a
  laptop figure.
- Words: no em or en dashes in src, notes, data or lines; "Curio Class" never "Curio" alone. Classroom-safe.

## Lines
- `voice/lines.json` and `allLines()` match exactly: 106 and 106, none missing either way (`alllines.json`).
- Art: all 27 `art:` tokens have a prompts.json entry, none unused; the five kid poses carry `people: true`, and
  all art is gpt-image (no local model drew people).

## Standard voice check (Sound on, Motion on, held clicks 0.12 s)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| big (5 Big drops, into Small, Medium, Big, Small, Medium) | event | 5 | 5 |
| Head clue text (clue0 tapped 5 times) | how | 1 | 1, then 4 silent |
| bIn / bHold / bOut (two rounds at count 4) | event | every phase | 2 / 4 / 2 |
| breathDone | how | 1 | 1 |
| Talk-back replies (5 taps over three runs) | event | 5 | 5 |
| startTalk, howAfter (three runs) | how | 1 each | 1, then silent |
| meterDown (twice), meterOther (once) | event | 2, 1 | 2, 1 |
| goalSet | event | 1 | 1 |
| checked (day0 tapped 5 times) | event, once per day by spec | 1 | 1 |

- Stale: Tools, meter, Start, Stop, Sort at 0.2 s gaps: each line is cut by the next action, nothing plays after
  the switch to Sort except wSort (`stale`). Squeeze then My week mid-run: `sqz` stops, `letgo` never plays, the run
  stops (`squeezeSwitch`).
- Read: Read 0.4 s into the Tools welcome cuts it and reads; a mode switch right after lets wClues start at once
  (`readDuring`). First taps: the audit rows hold (I did not re-shoot them); the welcome skipped by a first tap on
  the card or a basket is fine under BASELINE 16, and the premise stays on screen and in Read.
- Order: in every log the spoken lines follow the actions.

## Findings

1. **Number keys change mode while using a tool.** src.html:1247-1250. Keys 1 to 4 switch modes from anywhere
   except a SELECT. With focus on Stop during Box breathing, pressing "1" jumped to Sort and stopped the run
   (`digit-in-meter`: mode "sort", running false). The meter steps are labeled 1 to 5, so a keyboard user rating
   "2" or "4" leaves the tool and loses the rating. Better: ignore the mode digits when focus is inside the stage or
   panel (or on a meter), or let the meter take 1 to 5 itself. **should fix**, general.
2. **Saving "My helpers" has no privacy line where it happens.** src.html:848-852 and 1006-1008. "This one helps me"
   writes `wss-week` to localStorage (`helps-privacy`: `{"week":null,"helpers":[3]}`), but the Tools panel says
   nothing about storage; the privacy line only shows in My week (frame `helps-privacy.png`). BASELINE rule 7.
   Better: one small line under the result buttons: "Saved on this device only." **should fix**, general.
3. **Read uses lines that cannot be recorded.** src.html:389-401. Read speaks the hint plus the panel's
   `innerText`. About 16 hint strings ("Tap a numbered ring to open a body clue.", "Tap Try a tool on it, or tap Next
   worry.", the My week builder hints and others) are not in `voice/lines.json`, so once the friendly-dad clips
   exist, Read will switch to the browser voice partway through. STANDARDS "Bands" says the panel hints go in the
   lines so Read can use recordings. Better: put the hint strings in `L` and have Read speak keyed lines.
   **should fix**, general.
4. **Body clue rings sit over the face and in odd places.** Body clues, src.html:94-95 and 232-233. Ring 1 (Head)
   covers the kid's nose and mouth at every size; at 680x425 ring 4 (Tummy) sits on the belt and crotch, and ring 5
   floats off the body with its leader line pointing at the thigh, not the hands (audit frames
   `state-body-clue-1366x768.png`, `state-body-clue-680x425.png`). Better: Head ring on the forehead or temple
   edge, Tummy on the hoodie pocket, ring 5 led to the hand. **should fix**, general.
5. **Tool tile icons mix text glyphs and color emoji.** src.html:320. Box breathing "□" and Worry box "▣" render as
   thin black text glyphs; Talk back "☁" and Squeeze "✊" render as color emoji (frames
   `state-talk-result-1366x768.png`, `helps-privacy.png`). The spec asks for code icons; the row looks unfinished.
   Better: four small inline SVG icons in the brand color, or four emoji. **polish**, general.
6. **Read in the Big panel runs the adult chips together.** readPanel, src.html:395. The 721-character Read says
   "Parent or caregiver Grandparent Teacher School counselor Coach Doctor" with no breaks, and "Tell one grown-up you
   trust" comes twice (start and end) (`read-big`). Better: join the chips as one sentence ("A parent or caregiver,
   a grandparent, a teacher..."), and drop the repeat. **polish**, general.
7. **Count toggle states its value twice.** src.html:772 and 820-824. The button's label flips to "Count of 3"
   and it also sets `aria-pressed=true`, so a screen reader hears "Count of 3, pressed" (`count-toggle`). Better:
   a fixed label ("Shorter count (3)") with aria-pressed, or a two-button group. **nit**, general.
8. **A sorted card keeps saying "Pick up worry card".** src.html:484. After a drop the card is `aria-disabled` but
   its label still ends "Pick up worry card". Better: "Sorted" in its label. **nit**, general.

Checked and fine: keyboard sort (focus on the card, Enter, Arrow, Enter places it; 4 px blue focus ring on the
basket, `kbd-sort.png`); tab order header, card, baskets; jittered real-mouse drag lands in Medium with no ghost
left (`drag-jitter`); Motion off keeps breathing timing, the dot jumps per side and no animation runs
(`calm-breath`); storage wrapped in try/catch with the "This browser won't save it." line; week index by
calendar date.

Counts: blocker 0, should fix 4, polish 2, nit 2.

## Audit pilot
- Leads confirmed: none to confirm; its only lead (welcome not heard after a first tap on the card or a basket) is
  allowed by BASELINE 16, and the premise stays on screen and in Read.
- Leads wrong: none.
- What it missed: the number keys pulling a keyboard user out of a running tool (finding 1), the missing privacy line
  where helpers save (2), hints outside lines.json for Read (3), and hotspot rings placed over the face and off the
  hand (4). Those are about meaning and placement, which it cannot judge.
