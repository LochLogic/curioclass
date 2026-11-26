# Fixes: scope and sequence of library-and-research-skills-kindergarten, 2026-11-26

Applied 14, not applied 0. By source: expert read 12 applied (findings 1 to 7, finding 6's five parts each counted,
plus the source note); lead calls 1 applied (call 1, with call 4 carrying the frame wording); band items 0 (no other
library sequence read exists yet; no "Across" item touches kindergarten); own 1. No Codex read yet (after
2026-11-30, its own pass). Every finding is logged in the defect ledger (`plan.py defect --status=fixed
--made-at=scope`).

## Applied

- **Expert 1** (days.csv days 1, 4, 15, 16, 17, 18, 19, 27; .md units 1 and 3; frame.md units 1 and 3): unit 1's seeds
  stay whole on day 1 and the teacher cuts one open on day 4 as a find source beside the read-aloud. Unit 3's day 15
  opens on the rabbit question as the hook, then models the held-question move on a tortoise passage ("What does a
  tortoise eat?"); the rabbit read-aloud is first read on day 17. Day 16's three passages and the unseen passages on
  days 18, 19 and 27 are other plant eaters.
- **Expert 2** (days.csv days 4, 5; .md unit 1; frame.md unit 1 evidence): the day 4 drawing (one found fact, labeled
  or dictated) is k-class-inquiry's observed performance for the find and use steps, marked on the checklist on day 4,
  beside day 5's picture-order item.
- **Expert 3** (days.csv day 20; .md unit 4; frame.md unit 4 skill card): the card is "eyes look, wait my turn, what
  did Sam add, who made it", opening with SEL's talk turn card in SEL's words; taught here where a school does not run
  SEL.
- **Expert 4** (days.csv day 7; .md one page and unit 2; frame.md unit 2 Days): day 7 opens with the hook and the
  compelling question; its k-wonder retrieval dropped.
- **Expert 5** (days.csv days 10, 17, 23 `retrieves` cleared; .md one-page and retrieval lines): show-me and practice
  days open with retrieval, inquiry days with the cycle card.
- **Expert 6a** (days.csv days 11, 28; .md unit 2 and check 2; frame.md unit 2 evidence and check 2 cell): "Which one
  would help us find out about ___?" for a named question, asking the ~AASL.IV.A.2 slice.
- **Expert 6b** (days.csv days 20, 23; .md unit 4, Unsure): the ELA trees host is in step (ELA days 80 to 118, weeks 16
  to 24); the Unsure line dropped; ssk-talk-together named for weeks 3 to 4 and week 23.
- **Expert 6c** (days.csv day 10; .md unit 2; frame.md unit 2): the partner share sits on day 12 only; day 10 ends at
  the drawing.
- **Expert 6d** (days.csv day 2; .md unit 1): the teacher shows one cover guess first; it stays about 3 minutes.
- **Expert 6e** (.md unit 3 passage list; frame.md unit 3 Tools): rabbit read-aloud, tortoise model passage, three
  practice passages, a fresh-try passage, two unseen passages and day 20's two-sentence retrieval passage, all plant
  eaters.
- **Expert 7** (.md Shorter path): day 24's circle share and the 3-minute feedback candidate fold into day 26's opening
  10 minutes, not into day 23; day 30 into day 29 stays; day 22 into days 21 and 23 stays third.
- **Expert source note** (frame.md Sensitivity reads, call 4): the frame no longer claims the online-safety
  presentation's rule matches the stop rule; the listing shows only the title, so the match is a browser check at
  grade close.
- **Lead call 1** (frame.md Placement paragraph and For the lead 4; .md For the lead): the weeks 27 and 28 after-core
  clash is settled by CALENDAR.md rule 1 (library is a special in K to 5); the scope's For the lead item dropped.
- **Own 1** (days.csv day 6; .md unit 1): unit 1's class counts (the day 4 find and draw, the day 5 items) go on the
  mid-year sheet before the checklist is thrown away, so day 13's cycle item stands with a record of the cycle done
  (collect once, call 9).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A show-me day models on a parallel case; the unit's own answer is first met on the inquiry day | The inquiry keeps something to find |
| A K inquiry-day product can stand as the observed performance for the cycle's find and use steps | Sequence-write rule 2; scoring stays off show-me days |
| Library's turn card opens with SEL's talk turn words, then adds library's steps | One card across courses, though library is not bound |
| Inquiry days carry no `retrieves` when the cycle card is the day's own skill | Not a retrieval task |
| A shorter-path fold-in keeps the year's last product shared with the whole class | Bar part 11 item 6, a real audience |

## For the structure pass

- docs/agents/lenses/library.md: "catalogues" to "catalogs", "licences" to "licenses", "judgement" to "judgment"
  (call 13, the lead's).
- data/plans/calendar.csv: no change from this pass (no school_day moved).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-kindergarten`: 0 failures.
- `python -X utf8 scripts/frame.py check library-and-research-skills-kindergarten`: 0 failures (4 units, 30 days, 24 in
  units, 6 for checks and respond days).
- No unit moved, no day count or owned row changed; no school_day changed, so the calendar is unaffected (library is a
  special and does not count in the K to 5 stagger).
