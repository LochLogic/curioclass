# Play lens: line-leader-picker (round 1)

Played twice: as a K-2 child alone at home (Sound on, nothing read), and as a teacher projecting at 1366x768 and
1920x1080. My frames and logs: `S:/CurioClass-codex-scratch/line-leader-picker/play/out1/` and `out2/` (drive.py,
held clicks, port 9880). Shared audit frames used: `audit-r1/size-1366x768.png`, `state-who-*`, `state-changed-*`,
`state-fair-c-*` (1366, 1920, 680), `state-bee-b-1366x768.png`, `state-summary-1366x768.png`, `state-changed-375x812.png`,
`state-who-680x425.png`.

Overall: the core loop lands. The droopy sitting pose on 19 friends after rule A is the strongest moment in the tool,
the Before outlines in Change a Step read at a glance, and a solo K child gets a clear first instruction. The
problems are in Is It Fair?, where the grade 2 feedback is mostly unheard and unseen, and one easy trap in Change a Step.

## Should fix

1. **Is It Fair?: the check feedback is dropped at a normal tapping pace** (src.html:1333-1340, `check()`).
   On the first rule, each thumb tap speaks the next question's how line first (`now:true`), then queues
   "The chart agrees." / "Look at the chart again." plus the evidence line. That question line takes about 3.5 s, so
   the next thumb tap (a child answering a question they just heard) drops the queued feedback. Rule A with taps
   3.5 s apart (`out2/fair-A-flow.png`, vlog): "Look at the chart again." + "Only the friend at the front can lead..."
   dropped, "The chart agrees." + "That friend waited all month and never led..." dropped, "Look at the chart again." +
   "One friend led more than once..." dropped by the verdict tap. Same in `fair-bee-C` (q1CSick never heard). The
   child hears three questions and no answers: the evidence lines are the teaching of E2, and the "left" feelings
   line is lost too. Better: speak the feedback first and let the next question wait for it (or speak the next question
   only after the feedback ends), and do not let a later thumb drop a feedback line that has not started on the first
   pass. Tag: general (event line lost behind a how line on rapid answer flows).

2. **Is It Fair?: a pre-reader cannot see that the chart disagreed, or which verdict they picked**
   (src.html:1313, 1318-1319, CSS .verdict). The tapped thumb gets the same blue pressed ring whether it matches the
   data or not; the only sign is 12 px text "× No" under it (hidden entirely at 680x425 and narrower, src.html:247).
   With the spoken "Look at the chart again." dropped (finding 1), a mismatch is invisible to a grade 2 non-reader
   (`out2/fair-A-flow.png`: thumb up on Q1 for rule A, evidence "× No"). Separately, Fair / Not fair have no pressed
   style at all: after tapping Not fair nothing on screen changes except the hint (same frame). Better: show the
   evidence as a picture next to the thumbs (a small check or look-again mark, not right/wrong scoring), and give the
   verdict buttons a pressed look. Tag: general. Level stays should fix since the spec
   promises "evidence on the chart for each check" to pre-readers.

3. **Change a Step: tapping the already chosen tile wipes last month and changes nothing** (src.html:1051-1069,
   `choose()`). The mode opens with "Stays at the front" pressed; a child who taps it (natural: to hear it, or because
   it glows green) turns Ant's 20 stars into Before outlines, clears the chart, and is told "Tap Run to play our
   month." with `changed: []`. Running replays the identical month, then no compare line and no "Which step" question
   arrive (`out1/change-same-tile.png`). The same tap in Make a Rule silently clears a finished month. Better: a tap on
   the tile that is already chosen only speaks its name (and in Change a Step, says "That step is the same. Tap the
   other picture to change it."), and never moves the month to Before. Tag: general.

4. **Our chart hint names a control that is not on screen** (src.html L.fSummary, overlay `.close`). The hint and voice
   say "Tap Close to return to the rule cards." but the button is a bare "×" (`audit-r1/state-summary-1366x768.png`).
   A child who cannot read cannot find "Close". Better: "Tap the X to go back to the rule cards." or a visible "Close"
   label on the button. Also: opened before any rule is tried, the summary asks "Which one would you pick for our
   class?" over a table of only "?" (same frame); ask that only once at least two rules have rows. Tag: general.

## Polish

5. **Step 2 tap: the instruction plays before the confirmation** (src.html:1074-1076). Tapping a step 2 tile speaks
   "Tap Run to play our month." first and the tile's own name after it (`out1/make-d-end` vlog: 2131 ms "Tap Run...",
   4276 ms "The name stays out of the jar."). The child hears the next action, then the echo of what they tapped,
   and the Run instruction is buried. Better: tile name, then "Tap Run...". Tag: general.

6. **The name slip pops up over Week 1, far from the jar** (src.html:57, `.slip {left:145px; top:30px}`). In jar rules
   the slip always lands on day squares 1-2, covering day 1's face for the whole month while the jar sits at the far
   right (`out1/make-d-day1.png`, `make-d-day8.png`). Better: place it beside the jar (or the Leader spot) so the
   draw reads as coming out of the jar, and never over a calendar day. Tag: general.

7. **The third question reads differently on screen and in the voice** (src.html:846 vs L.q2). Chip: "Extra turns while
   a friend got none?"; hint and voice: "Did someone lead more than once while a friend got none?"; summary column:
   "Extra / none?" (`audit-r1/state-fair-c-1366x768.png`, `state-summary-1366x768.png`). POLISH: anything shown twice
   matches. Use one wording (the spoken one is clearer for grade 2); "Extra / none?" is cryptic as a header. Tag: general.

8. **Our chart fills in the answers before the child checks** (src.html:1239, `recordSummary()` at finish). As soon as
   a month ends, its Q1-Q3 row shows ✓/× from the data, so opening Our chart answers the three checks, including Q1,
   which is not visible on the chart itself. Toggling Bee also records a row for a rule nobody looked at
   (`out2/fair-summary-after`: "A · Bee sick" filled with no checks answered). Better: fill a cell once the child has
   answered that check. Tag: general.

9. **Projector reading size** (`audit-r1/state-fair-c-1920x1080.png`). At 1920x1080 the rule card names stay 12 px,
   the check questions 14 px and the evidence 12 px while the chart grows huge; from the back of a room the rule cards
   are unreadable. The 1600 px media query scales the chart and hint but not `.rule-pick`, `.check h2`, `.evidence`
   or `.verdict button`. Tag: general.

## Nit

10. The first-in-line step icons (dots, ring, curl arrow, door bracket) are hard to tell apart at 680x425 rule cards
    (`audit-r1/state-fair-c-680x425.png`: A and B look the same). The voice covers it; a bigger difference in the
    arrow would help. Tag: general.

## Checked and fine

- First screen (solo K): hint says what to do, Run stays disabled until both steps, first tile tap speaks its name
  (welcome skip is rule 16, not reported). Who overlay appears once and both answers land on "people made the rule".
- Motion off keeps time: 20 days took 8.7 s after the Run tap (1200 ms + 19 x 450 ms expected 9.75 s from the tap)
  (`make-calm-run`).
- Month result lines play whole and say the right thing (rule C: "Some friends led three times each. Nine friends
  never got a turn."; rule D: "Everyone got one turn."). Bee sick rule B gives Ant 2, Bee 0 with the ring.
- Changing both steps in Change a Step says "Two steps changed" and accepts either tile (`out1/change-both`).
- No console errors in any of my shots. Depth: rules C and D give a new month each time; Change a Step chains
  (each run becomes the new Before). Enough for a K-2 tool used across a few sessions.

## Audit pilot

- Leads confirmed: none that matter for play. The 375x812 friend/count "overlaps" are by design (count sits in the
  button's corner, `state-changed-375x812.png` reads fine); the "text under 10 px" rows are icon-only buttons with
  font-size 0 (intended compact layout).
- Leads wrong: the "welcome not heard" rows for friend and tile first taps are BASELINE rule 16, the premise stays in
  the hint. The "has not led yet" 4 of 5 at a 2 s pace is the newer tap dropping the older one's tail, as the spec asks.
- Missed: finding 1 (feedback dropped behind the next question; its 2 s pace test only covered single controls, not a
  three-answer chain), finding 3 (re-tapping the chosen tile), findings 2 and 7 (visual and wording, out of its scope).
