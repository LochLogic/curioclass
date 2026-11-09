# Lunch Survey Cleanup handoff

## Structure
`src.html` starts from the kit starter. Its CSS lays out a cafeteria workbench, a painted menu, cleaning cards and a letter.
The script holds the exact raw survey, kit voice lines, cleaning transforms, outcome summaries, chart annotations,
the engine row table, draft checks, replies and persistent control wiring. `survey.json` is loaded at bundle time.
`window.__tool` exposes the spec's inspection API. Its report pick indices refer to shuffled visible positions.
`DataTable`, `t.replace`, `t.count`, `t.crosstab`, `renderTable`, `Chart`, `barRects` and `scales` come from data-desk 1.1.
No kit or family file was changed. All counts and report truth come from rows, never a verdict lookup table.

## Decisions and contradictions
- Accepted the recommended fictional-data exception to the family's public-data rule. Real private student rows are not used.
  The fictional school and survey are labeled on screen and in teacher notes. Any shared-family exception note is for the integrator.
- Kept the recommended sixth-grade paper-form premise. Did not restore the earlier English-learners premise.
- Followed the user's image request and CODEX-BUILD's generated-art instructions where BUILD says not to draw.
- The brief says to start codex-report.md early and also stop when it is written. The user's explicit stop condition wins:
  evidence stays in Scratch, and the completed report is created last.
- Three 140-pixel buttons cannot fit a 36-percent panel at 680 pixels. At widths up to 1100 or heights up to 740,
  problem tabs show one complete fix group. At 1366x768 and larger laptop layouts all three cards stay visible.
- Compact Report uses Part tabs, with Fix 1 to Fix 3 subtabs inside Part 1. All three reasons for the current fix are visible.
  The seven limits use two columns. These layout choices prevent short choice sets from disappearing into a scroll panel.
- After a check, Report uses the same tabs at every size so the explanatory feedback fits beside the selected statements.
  Before checking, the full two-column letter appears only when its measured content fits, including at 1366x768.
- At short preview heights the opening manager note uses its rule summary and opens fully over the stage on tap.
  The cafeteria header and Marcus fold. The Who's in evidence uses two columns of textual rows at these heights.
- On phones the controls come before the scene, and the page scrolls vertically. The tool remains a solo student tool.
  Report's compact evidence moves into Part 2 on phones, keeping the statement and its evidence together.
- The bundler only accepts json tokens with a basename. The requested data/survey.json is stored as the actually loaded
  survey.json at the tool root; the exact generated row recipe is unchanged.
- Cold review found that a longest/middle/longest length strategy still selected all three process reasons.
  Reason alternatives now have equal 76-character lengths, preserving their meanings. Counting alternatives likewise
  have equal lengths within each state, using equivalent grade and copies clauses, equal V/T and shuffled placement.
- The planned voice is casual-peer, Zubenelgenubi. No recording was authorized. Kit browser speech is the build fallback.
- STANDARDS forbids naming disabled controls. The Report welcome names Parts 1 to 3, followed by a Check instruction
  only when Check is enabled. After corrections, the Part 4 instruction names Part 4, followed by Send only when enabled.
- The menu item list folds at compact sizes; all menu names remain in the chart. On wide screens the menu, trays and
  badge have separate space. The chart remains the largest single central component, though below the spec's approximate
  half-stage-height aspiration while the opening note, verdict and all evidence are visible together.
- Effect comparisons list up to two removed grade groups, plus extra copies. The write-in subgroup remains in Who's in.
  This follows the spec's own Drop blanks effect example and prevents a fourth evidence clause overflowing short cards.
- Send to Ms. Reyes is a fictional local exchange. It draws a report and reply and makes no external transmission.

## Tricky parts
- Cold review: unchanged assisted reason selections carry their supplied flag and explanation into later drafts.
  The first-check count excludes those carried answers; they remain visibly marked Marcus fixed.
- Cold review: the longest-limit shortcut is blocked by a natural, longer false statement about grades 7 and 8.
  Keep these alternatives meaningfully mixed in length when changing their wording.
- Cold review: Days captions count retained blanks/filled guesses, not a constant 118 when another fix removes rows.
- Cold review: a check opens the first mismatching Part/Fix and adds result marks to the tabs.
  Check and Send take over obsolete speech with the kit's now option, which preserves Read priority.
- Cold review: the letter measures its available height before using the wide layout. Trying all three alternatives
  can add enough comparison text to hide the recommendation, so overflow uses the existing Part/Fix tabs instead.
  Resize remeasures from the full layout; control elements and keyboard focus are preserved.
- The short preview lays out prop, title and Show rows above full-width details. Comparison clauses keep every number,
  use concise grade labels and separate Veg/Tacos lines, and retain the complete text for assistive reading and hover.
  This clears the confirmed Report-button overlap without shrinking targets or removing evidence/art.
- Repeating the same view or mode preserves its live how-to/welcome; a genuine change still drops obsolete speech.
- Compact Part 1 hints name the first unanswered Fix tab. These three instructions are in the 28-line voice manifest.
- Cold review: shortened the short-preview cause note so it clears the Report button in Rows view at 680x425.
- Cold review: painted paper has code-drawn survey marks, and the spelling detail uses readable sticky-note labels.
- A null fix keeps raw rows but does not count as tried. Each fix rebuilds from raw rows, so order does not destroy evidence.
- Who's in distinguishes unique students, removed students and extra submissions. It preserves raw write-in identity after Merge.
- Filled and merged tags use raw metadata. The Row column is the original 1 to 412, never a new index.
- All selected limits must be true and at least two must be selected. Check still permits one so students see that it is insufficient.
- First-check credit freezes per draft. Marcus repairs are separately marked and never improve that first score.
- Any report-statement edit invalidates Send. A changed cleaning fix creates one new draft after a check; later changes
  before the next check join that draft. Unchanged reason rows and the recommendation survive; coverage and limits clear.
- Buttons are not replaced on selection or checking. Send moves focus deliberately to its earned report with preventScroll.
- Flip voice waits 600 ms and is capped at four per page. It checks the revision and scope before speaking.
- Stale grade-six teaching stops if sixth graders are restored. Queued speech is dropped on mode or state changes.
- The existing engine pager is moved outside the scrolling table host, preserving its controller and keyboard buttons.
- Opening locked Report focuses its Back to Clean button. Phone mode switches scroll to the start of the new mode.

## Sensitivity
No cultural, health, body or personal-data curriculum. Food preferences are not attributed to an ethnic or language group.
The manager and student are fictional. All three people assets have people: true. Their contact sheet is in Scratch.
A fresh-agent representation check passed: respectful, age-appropriate, consistent Marcus identity, plausible hands,
no stereotypes or mocking details. Small key fringes were subsequently despilled through the permitted rekey pipeline.
The owner's people contact sheet is retained for the later shipping review.

## Engine changes wanted
None required in data-desk. Optional bundler improvement, outside this build's write scope:
`scripts/bundle_tool.py`, the json token substitution: allow safe relative subpaths such as json:data/survey,
resolve inside the tool root and reject traversal. This would let the source use the spec's data subfolder directly.

## Evidence
All scripts, independent calculations, captured frames, voice logs and audit output live in `_scratch/lunch-survey-cleanup/`.
`model-check.json` records 27 states, 81 reply paths, 729 reason combinations and 3456 limit sets.
`browser-check-result.json` records actual engine-table and report-state assertions, including the first-score and Send cheats.
`numeric-details.json` records independently computed contrast, text lengths and shortest/longest strategy checks.
The report gives final frame, voice, audit and process-cleanup outcomes. No commit or polish round was performed.

### Build audit (before cold review)
The build audit completed with 113 mechanical leads. All 58 frames were opened (51 unique; seven exact duplicates).
Focused repairs afterwards corrected menu/badge overlap, compact cause overflow, pager overlap, the 28px All target,
disabled-control voice wording and locked-report focus. Seven repair frames and 76 browser assertions passed.
SVG tspan ownership and 17px checkbox glyphs were false positives: labels remain visible and the clickable labels are 44px tall.
The audit's phone iframe lookup failed; separate hosted 375px Clean, Report and evidence frames were inspected successfully.
The audit was not rerun. Its snapshot and the later focused checks are intentionally retained separately in Scratch.

### Cold review
The separate cold-review audit ran once and completed in 26.4 minutes: 71 leads, 76 individually viewed frames.
Scoped repairs fixed retained-fill comparison/cause overlap and repeated-tap speech cancellation.
Final checks covered equal-length reason/counting alternatives in all 27 states, keyboard submission, focused
1920-to-1366 resizing, score/Send gates and a fresh held-click voice path through Send. No second audit was run.
The compact comparison clears Report at 680x425 and 800x500; the worst compound cause clears it by 4px.
Final bundle: 471837 bytes; art: 150152 bytes. All owned review ports are closed and host.html is absent.
See codex-review.md for the findings, named sources, voice qualifications and retained spec decisions.
