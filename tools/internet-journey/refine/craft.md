# internet-journey: Craft lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, kit/network.js and
docs/families/network.md, against REFINE.md (Craft lens), STANDARDS.md and BASELINE.md. Bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py internet-journey` (194 KB). Driven in muted headless Chrome on my own
profile and ports 9461-9466 (a small CDP harness on top of scripts/drive.py, held clicks of 120 ms, real keys).
Browser voice only (no clips yet), so a "spoken" line in headless lasts until the kit's cap; timings below are relative.

Counts: blockers 0, should fix 8 (general 5, family 3), polish 4, nits 5 (general 3, family 2)

## Contract (passes)

- One file, 194 KB. No network requests (Network domain and `performance.getEntriesByType('resource')` both empty
  in every run). No fetch, XHR, storage or WebSocket in src.html or kit/network.js.
- No console errors, warnings or exceptions in any run (13 page loads, both modes, Motion on and off, two full Story
  runs, Trip map tests, fast-tap runs, sizes 680x425 to 1920x1080).
- Kit used: header buttons, `Curio.voice`, `Curio.tone/yes/wait/reduce`, and the new `kit/network.js` (graph, draw,
  token, send with bounce, split, join, path). Nothing in the kit is re-implemented.
- Engine pure part runs in Node (path with a down node reroutes, reach, split by words, join with "___", step with
  ttl). The engine matches the spec's "Family engine" description except the items under S5, S6, N2, N3.
- `allLines()` (29) equals voice/lines.json (29), word for word and in the same order.
- Words: no em dashes in src.html, notes.md, lines.json, tool.draft.json, prompts.json, network.js or network.md;
  "Curio Class" never "Curio" alone; classroom-safe; nothing stored, and notes say so.
- Art: both `art:` tokens (ij-dusk-town, ij-server-hall) have prompts.json entries; no people in either.
- Targets: every button and focusable stop is at least 44 x 44 px at 680x425, 800x500, 1000x625, 1280x720,
  1920x1080 and 760x900 (measured in Story chapter 1, chapter 2 and Trip map). Map labels 13 px at 680x425.
- Motion off: pieces jump hop to hop, the "bounced" tag shows at Router A (frame kb-calm-ch4-bounce), no pan.
  Sound off hushes and drops queued lines unmarked; Read works with Sound off.
- Keyboard only with Motion off, all B in chapter 1 then A: reaches the ending, then See the trip map, every stop
  by Tab. The focus ring (4 px `--focus`) shows on cards, Send, Next, Try other choices, the header and every map
  stop.

## Standard voice check

Two full Story runs at real speed (all A, then Try other choices, all B, then Try other choices again), then Trip map:
Send a test five times, Close a road toggled five times, Send a test, five stops tapped.

| line | kind | expected | spoken |
|---|---|---|---|
| w-story "Welcome to Internet Journey..." | welcome | 1 | 1 |
| ch1 "You are inviting your friend Juno..." (3 chapter-1 openings) | event | 3 | **2** (first load: silent "early", never re-queued; see S1) |
| ch2 to ch6 chapter texts (2 runs) | event | 2 each | 2 each |
| result 1 "Your tablet cut the invite..." | event | 2 | 2 |
| results 2A..6A (run 1), 2B..6B (run 2) | event | 1 each | 1 each |
| next "Press Next to send the pieces on..." (12 triggers) | how | 1 | 1 (then silent x11) |
| E1 (run 1), E2 (run 2) | event | 1 each | 1 each |
| again "Press Try other choices..." (2 triggers) | how | 1 | 1 (then silent x1) |
| w-map "This is the whole trip..." | welcome | 1 | 1 |
| landed "All 8 pieces arrived..." (6 tests) | event | 6 | 6 |
| closed "Router A is closed..." (3 times on) | how | 1 | 1 (then silent x2) |
| hints send / choose / watch | hint only | 0 (Read) | 0 (but see S1: the Send step is never spoken) |

First tap, one fresh page each (time after the tap):

| first tap | expected | got |
|---|---|---|
| the stage | welcome within ~0.5 s | w-story at 133 ms |
| a chapter 1 card (no line of its own) | welcome | w-story at 146 ms |
| Trip map | its welcome only | w-map at 135 ms |
| Read | the Read text only | read at 137 ms, nothing else |
| Tab key | welcome | w-story at 3 ms |
| Motion | welcome | w-story at 136 ms |
| Sound off | nothing; Sound on brings the welcome once | nothing; w-story on Sound on; a second off/on adds nothing |

Stale lines and order: fast taps (gap 0.2 s) through the three chapter 1 cards, Send, Trip map, Send a test, Close a
road, Story: the result, the closed line and Next's line were dropped (`hush`, `newer`); nothing played after its
moment and nothing from an older action played after a newer one. With the time scale at 0.2 through chapters 1 to 3,
each chapter text and result was dropped `newer` when the next action came. Read during the welcome stopped it; lines
queued during Read waited for it; Read with Sound off spoke; Trip map right after Read started its welcome 141 ms
later. Every spoken line was checked against the frame at its time (frames r1-*, r2-*): they match, except S7 and P3.

## Findings

### Should fix

**S1. Chapter 1's story line is never spoken on a first visit, and the Send step is never spoken at all.**
general. src.html:886 (`V.say(L.ch[n]...)` in `openChapter(1)` runs at load), 1160. How seen: every first-tap log
starts `event silent early "You are inviting your friend Juno..."`; nothing re-queues it, so a pre-reader's first
visit hears only the welcome ("tap a card to choose"). The chapter 1 how-to "Pick a card for Place, Extra and Photo.
Then press Send." (L.h.send) is hint only, so after picking three cards nothing spoken names Send. Done when 6 says
"chapter and result lines play each time". Better: queue the chapter 1 text after the welcome on the first tap
(welcome list `[wStory, ch1]` or `welcomeAfter`), and speak L.h.send once as a `V.how` (needs '#send').

**S2. The Story welcome overwrites the panel hint.** general. src.html:395-400 (welcome uses the kit default
`hint: true`). How seen (s9): after the first tap the Story hint reads "Welcome to Internet Journey..." instead of
"Pick a card for Place, Extra and Photo. Then press Send."; Read then says the chapter text plus the welcome, never the
Send step. Better: give the welcome `hint: false` (a `[key, {hint: false}]` welcome entry), so the panel hint and Read
keep naming the next action.

**S3. Trip map pieces leak into Story's stacks.** general. src.html:1077 (`state.flying.add` in `sendTest`), 1127
(leaving Trip map does not clear `state.flying`), 617. How seen (s8 stale1, s9): Send, Trip map, Send a test, back to
Story within 1 s: `state.flying` is `[1, 2, 3, 4, 5]`, the stack at Your Wi-Fi router shows "3" (frame stale-end shows
"5" in another run) while the story says 8 pieces; it stays wrong until the next chapter's pieces fly (returning at
chapter 5 keeps it through chapter 5). Better: clear `state.flying` when leaving Trip map, or keep a separate set per
mode.

**S4. Tapping a moving envelope almost never works, and the envelope is not reachable by keyboard.** family:network
(engine tokens, kit/network.js:451-466, and src.html:1046-1050). How seen (s5): a token is 34 x 24 px and moves; the
tool listens for `click`, which needs press and release on the token. Four tries each: Quick with a 120 ms hold 0 of 4,
Quick 30 ms 0 of 4, Slow 120 ms 0 of 4, Slow 30 ms 4 of 4. A grade 3 tap is about 120 ms, so the envelope view (To,
From, "Piece n of 8", the lock: the spec's way of showing what a router reads) is out of reach, and tokens have no
tabindex. Better: in the engine, an invisible hit circle of at least 44 px on tokens and a `pointerdown` pick (or a
token `onPick` option); in the tool, pause the test while an envelope is open, and a keyboard route (for example the
stop card of the stop a piece is at offers "Look at piece n").

**S5. `view.badge()` changes the map's tab order.** family:network. kit/network.js:356-359 and 416 (`drawNode`
removes the node and appends the new one at the end of the nodes layer). How seen (s6, Trip map Tab order): you, ispA,
rA, rB, rC, rD, ispB, home2, juno, then home, srv (the two nodes that Trip map un-badges on entry). The family rule says
node tab order follows `nodes`. Better: replace the old element in place (`old.replaceWith(gEl)`) in drawNode.

**S6. The family doc promises `view.labelBox(id)`, which the engine does not have.** family:network.
docs/families/network.md:37 and the handoff list `labelBox`; the view object (kit/network.js:408-429) has no
`labelBox`, so a sibling calling it throws. Better: add it (the label's bounding box in px) or remove it from the doc.

**S7. Ending E3 says details went along when none did.** general (needs a spec change, so it may belong in the spec's
open questions). src.html:450-453, spec chapter 7. How seen (`ending()` with every A except 6B): no private chips, the
invite on 15 devices including 12 strangers' phones, and the spoken and shown line is "Some private details went
along, but only to people you know." Both halves are false on that screen. The build handoff flagged it. Better: a
fourth line for "no private details, but shared with people you don't know", or send 6B to E2 with wording that fits.

**S8. Focus jumps to the first card on page load.** general. src.html:910 with 913 (`lostFocus()` is true at load,
since nothing has focus yet) and 1160. How seen (s6): the first Tab lands on the second card (at my house) and the
header (Story, Trip map, Motion, Sound, Read) comes only after the cards, Start over, the map and Body. In the site's
16:10 preview iframe this focus() also pulls keyboard focus out of the host page on load. Better: only move focus when
a control inside the panel had it and went away (remember that before re-rendering), never on the first render.

### Polish

**P1. Event lines write over the hint and leave no next action.** general. src.html:903 and 1094 (`V.say` with the
default `hint: true`). Seen (s12): after a Trip map test the hint (and Read) says "All 8 pieces arrived, and the numbers
put them back in order."; during the ending line the panel shows the ending text twice (story text and hint) instead
of "Press Try other choices...". Better: `hint: false` on both, and a Trip map hint after a test that names a next step
("Close a road, then press Send a test again.").

**P2. Coming back to Story does not retell the chapter cut off by the mode switch.** general. src.html:1118-1139.
Seen (s8 stale2): chapter 3's text was hushed by the switch to Trip map; back in Story at chapter 3 "choose" nothing was
spoken. Better: on return, re-queue the current chapter text when it was not heard in this visit.

**P3. The 4A result is spoken before the bounce happens.** general. src.html:921-933. Seen (frame kb-calm-ch4-bounce
and r1-ch4 frames): "The pieces bounced back from the closed router and went around. They got there, just later." plays
at the tap, while pieces 5 to 8 are still at the internet provider for about 7 s. Better: speak and show the result
after `moveAll` for chapter 4 (the same holds, more mildly, for 2A/2B "Your pieces made it").

**P4. Low contrast placeholders.** general. src.html:143 and 155. The invite's blank "place / extra / photo" is
#8a7fa0 on cream, 3.51:1 at 15 px; the pop-up's field text 3.73:1 at 12 px (AA needs 4.5). Better: `--muted` #5e5470
(7.05:1 on white).

### Nits

- **N1** general: the stage `<svg id="sv">` is an empty Tab stop in both modes (s6 Tab order shows `sv` after Start
  over and after Quick). Give it `tabindex="-1"` or `focusable="false"`.
- **N2** family:network: `Net.stop()` keeps tokens marked `__keep` (kit/network.js:548), but nothing sets `__keep`;
  `send({keep})` is never honored by `stop()`, unlike the doc ("removes tokens not marked keep").
- **N3** family:network: `colors.ring` is used by the engine and passed by the tool but missing from the documented
  skin colors; the spec says path ties go "to the lower node index" while the engine and network.md say "fewer hops,
  then lower node index". Align the two docs.
- **N4** general: the ending board (1366x768, frame r2-ch7) lets the map's "Juno sees" bubble and slot numbers ghost
  through behind the rows; a fully opaque board background reads cleaner.
- **N5** general: the soccer group row's "phones" icon (three tall rectangles) reads as a folded map at 30 px
  (frame r2-ch7); a small phone with a "12" badge would read at once.

## Frames looked at

s1-default-1366, r1-ch1-next, r1/r2 ch2 to ch6 choose and next, r1-ch7, r2-ch7, r2-ch3-next, map-landed,
map-envelope, map-env2, map-stop, kb-focus-ch1, kb-calm-ch4-choose, kb-calm-ch4-bounce, kb-calm-ch7, kb-map-focus,
next-focus, stale-end, flying-leak-ch2, end-line-hint, size-{680x425, 800x500, 1000x625, 1280x720, 1920x1080,
760x900}-{ch2, map}, 375-ch1, 375-map (in the lens scratch folder, not committed).
