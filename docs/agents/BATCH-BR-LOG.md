# Log: Build and Refine waves BR1 to BR4

Batch note: `docs/agents/BATCH-BR.md`. Counts come from each tool's refine.md counts line (round 1 blockers and
should-fixes; polish not counted).

## BR1 (started 2026-10-27)

Builds started three at a time: teach-the-robot, internet-journey, data-defenders first; then levels-and-pathways,
city-skyline-studio, snowy-mail-route, simulation-studio as slots free up.

### BR1 closed 2026-10-28: all 7 PASS

| Tool | Grade | Family | Round 1 blockers | Round 1 should fix | Exit checks to PASS |
|---|---|---|---|---|---|
| teach-the-robot | 2 | ml-lab (new) | 2 | 8 | 2 |
| internet-journey | 3 | network (new) | 1 | 13 | 2 |
| data-defenders | 5 | security (new) | 2 | 10 | 2 |
| levels-and-pathways | K-2 | dance (new) | 2 | 10 | 2 |
| city-skyline-studio | 9-12 | perspective (new) | 0 | 14 | 2 |
| snowy-mail-route | 1 | robot (new) | 0 | 10 | 2 |
| simulation-studio | 9-12 | data-desk (returning, engine created) | 1 | 15 | 2 |
| **Average** | | | **1.1** | **11.4** | **2.0** |

Every tool needed a second exit check; three of the last items were narrow integrator fixes (data-defenders hint,
snowy-mail-route badge and footprint size, simulation-studio text alternatives). The repeat findings became the
wave lessons in BUILD.md, STANDARDS.md (Voice) and REFINE.md (Rounds). BR2 is the first wave built with them.

Cost (from agent reports, approximate): build 125k to 235k tokens, each lens about 150k, each exit check 90k to
170k, a scoped re-check about 100k; roughly 0.7M to 1M tokens a tool.

Known gap: levels-and-pathways misreads about 1 in 11 drawn 3- or 4-hump waves at 375 and 680x425 (stage too small).

## BR2 (started 2026-10-28)

song-form-builder and capture-the-flag built first. Teaching lens round 1: song-form-builder 0 blockers, 1 should
fix; capture-the-flag 2 blockers (strength meter rewards patterns, tradeoff codes untaught), 5 should fix.

### BR2 closed 2026-10-28: all 7 PASS, deployed

| Tool | Grade | Family | Round 1 blockers | Round 1 should fix | Exit checks to PASS |
|---|---|---|---|---|---|
| song-form-builder | 3-5 | music-studio (new) | 1 | 10 | 1 |
| capture-the-flag | 9-12 | security (returning) | 2 | 9 | 2 + integrator fixes |
| stage-blocker | 6-8 | stage (new) | 2 | 16 | 2 |
| fake-or-fact-lab | 6-8 | fact-check (new) | 1 | 17 | 1 + integrator fix |
| biased-bot (Codex builder) | 2 | ml-lab (returning) | 0 | 9 | 2 + integrator fix |
| target-toss | 1 | none (PE) | 1 | 14 | 2 + integrator fix |
| career-cluster-explorer | 6-8 | careers (new) | 3 | 12 | 1 |
| **Average** | | | **1.4** | **12.4** | **1.6** |

Against BR1 (1.1, 11.4, 2.0): round 1 findings about the same, exit checks down. Three tools passed on the first exit
check (none did in BR1); four needed a narrow integrator fix after their last exit check (BR1: three).

Codex builder pilot (biased-bot): built and polished by Codex in S:/CurioClass-codex, branch codex/biased-bot,
reviewed blind by the usual lenses. Round 1 was the best of the wave (0 blockers, 9 should fix), but exit round 2
failed and one of its round 2 fixes caused a regression (story welcome cut by cutHow), closed by an integrator fix.
Codex tokens: build 14.0M in (13.8M cached), 73k out, 37 minutes; polish 62.3M in (60.9M cached), 0.30M out over
two rounds (a Claude build is 125k to 235k tokens, mostly uncached). The pilot flow (Codex builds, the audit, then the
usual blind lenses, exit checks and integrator) worked, but Codex's polish needed the same integrator close as ours:
it is a builder option, not a replacement for any later step. Not adopted as the default; Cory decides. It also changed kit/ml-lab.js (zero-size host skip,
groupBars empty and size options) and left scratch files in the tool folder that its sandbox could not delete.

Audit pilot (scripts/audit_tool.py) on BR2: its clean rows held, but its overlap and focus-lost leads were false where
markers are clipped by a stage or scroll panel, it missed anything past one click, and its 44 px target rule conflicted
with K-2's 60 px.

### Audit tuned after BR2 (2026-10-28)

Two passes, merged together:
- **States** (codex-pilot session): every header mode at every size, builder-written `audit-states.json` (real clicks,
  keys, drags; keep regions), voice-cut checks from a log-only `cut` field in kit/curio.js (`V.log`; test_voice 42/42),
  the hint or last line naming a disabled control. On Codex's first biased-bot build (72734765) it catches 5 of the 8
  mechanical findings (old audit: 0 of 11). Best case: that states file was written by someone who knew the findings.
- **BR2 lens notes** (this session), each a class of wrong lead seen in two or more tools, nothing tool-specific: every
  box clipped by its overflow ancestors first (no overlap or fold lead for what a stage or scroll panel hides); controls
  inside a scroll panel not "below the fold"; designed ellipses with a title or aria-label and screen-reader-only text
  not "clipped"; the walk skips a control when something else is drawn at its centre, flags a click that changes
  nothing, checks focus once the narration settles and after Enter twice, and walks every mode, not just the first;
  SVG shapes with a pointer cursor count as targets; K-2 targets 60 px at every size (BUILD.md), with an optional
  `target` in audit-states.json for a spec that allows less.

Re-run on three BR2 tools: career-cluster-explorer 93 leads to 24 (the ~60 clipped-marker overlaps and 4 false focus
losses gone; left: the marker under Pan right, Where? and Trails below the fold at 760 and 375, the Clusters hint out of
view at 375, all real); biased-bot 11 false 375 overlaps to 0, plus a real one no lens caught (the card stack over the
menu's first line at 760x900) and the Fewer/More double-tap cutting "Pick the cards, then press Train Bitsy";
target-toss clean at 60 px, and its per-mode walk (Test it, Free throw) adds no false leads once a re-tap on the option already chosen is not called a dead click. A run is about 15 minutes. Still blind to: whether a hint or line is the right one,
timing (a line waiting behind another), teaching, feel, and any state no one listed. BR3 lenses keep the
`## Audit pilot` notes so its cold catch rate can be measured before it gates anything.

Open for Cory: the audit flags "welcome not heard whole after a first tap" (biased-bot 7 controls, target-toss 10,
teach-the-robot 4). The kit allows it unless a tool sets `welcomeAfter`; biased-bot's lenses called it a should fix.
Make it a rule (every tool sets `welcomeAfter` or equivalent), or tell the audit to stop flagging it?

Left behind: `S:\CurioClass-audit` (no longer a worktree; delete by hand), `S:\CurioClass-codex-scratch` (Codex's
evidence), worktree `S:\CurioClass-codex` (merged, can be removed).

Left open (in each refine.md): target-toss P5 to P7 and N4; career-cluster-explorer Hospitality, Management and
Marketing at 2 of 5 levels, trail header wrap at 1366; biased-bot Run then Skip within 4 s, headless speech stall.
Found by the tuned audit after close (not fixed): biased-bot card stack over the menu at 760x900, Fewer/More double tap
cuts the how line, `#viewer-cards` focusable at 32 px; career-cluster-explorer Trails buttons below the fold at 760x900
and the Clusters hint out of view at 375.
Board items: career-match-quiz onto kit/careers.js; scripts/careers_data.py default --out.

## Single-tool tests: network-help-desk and half-life-dice (2026-10-28 to 10-29)

Two tools through the whole Refine process alone, Codex as builder (Build and Polish), blind Claude lenses, fresh
Claude exit checks, the integrator closing. Both merged to main as drafts (58a1b956, f16fb21c); not deployed: art,
voice, Final look and Plan come after Cory's review (a draft never deploys).

| Tool | Grade | Family | Round 1 blockers | Round 1 should fix | Exit checks to PASS |
|---|---|---|---|---|---|
| network-help-desk | 4 | network (second tool, engine reused) | 0 | 15 | 2 + integrator fix |
| half-life-dice | 9-12 | new (dice decay, nucleus cards, dating ruler) | 2 | 14 | 1 + integrator fixes |

Against BR1 (1.1, 11.4, 2.0) and BR2 (1.4, 12.4, 1.6): round 1 about the same, a little more should-fix; exit rounds
the same. Every last item was narrow and geometric, closed by the integrator and checked by driving the bundle, not
by a fresh exit round:
- network-help-desk: exit 1 left three items (clue cards in a scroll panel, lines through labels, badge overlaps);
  Codex round 2 fixed all three but timed out before its own checks; exit 2 held two and failed one (router links
  sharing the Internet cable's run at 680x425 and 800x500); the integrator gave each routed link its own lane.
- half-life-dice: exit 1 failed two (fission arrow over Ba at 375 and 760x900; repeated ruler minor labels, a
  regression from its own fix); the integrator moved the arrow to the title row and dropped repeated labels.
- Spec, not build: network-help-desk's three biggest findings came from the spec (Cory changed it, giveaway "All
  three"); half-life-dice's spec gained Counter clicks, Count again, the Mark rule and two OpenStax sources.

Codex cost and time (usage lines are cumulative per session; a failed or timed-out turn writes none):

| Run | Wall time | Input (cached) | Output |
|---|---|---|---|
| network-help-desk build + report resume | 19:12 to 21:22 (2 h timeout + 10 min) | 34.5M (33.8M) | 209k |
| network-help-desk polish | 21:59 to 23:40 (stopped and resumed once) | 34.3M | 127k |
| network-help-desk round 2 | 01:19 to 02:49 (90 min timeout) | not recorded | not recorded |
| half-life-dice build | 23:02 to 00:22 (80 min) | 25.9M (25.2M) | 152k |
| half-life-dice polish | 01:05 to 01:24, then 01:24 to 02:24 (capacity failure, 60 min timeout) | not recorded | not recorded |

Cory: about 3% of the weekly Codex budget for the network-help-desk build alone, and 42% of the weekly budget for
the whole night (both tools, every Codex round; Cory, 2026-10-29). At that rate a week covers about four or five
tools, so Codex as the default builder for a 797-tool catalog is a budget question, not only a quality one. Both polish rounds ran out their
timebox in their own final checks (re-shooting six sizes, a full audit), after the fixes were in: the integrator ran
those checks instead. Lessons, in CODEX.md: reconnects fall back to HTTPS (the integrator stopped a polish there by
mistake); `resume` needs `writable_roots` for the scratch folder; "Selected model is at capacity" is the server, resume
at once; when only the closing audit is left, the integrator runs it.

Audit pilot, cold catch rate:
- half-life-dice round 1 (34 leads): one real catch that matters (Sound started off, the root of 19 "not heard"
  rows); false: Age estimate hit-area overlap, curve "across" the half-life line, Clear "nothing changed" (designed);
  missed: tray readability, ladder text overlap at 375 (SVG line over text), welcome/hint mismatch, color-only
  nucleons, aria-disabled styling, the 500 mark rule, the Geiger rate. Mechanical, not teaching.
- network-help-desk exit round 1 (118 leads): mostly "line drawn across" noise where links meet walls; one real
  (claim clue cards hidden in a scroll panel, which the exit check also found); "welcome not heard" is settled
  behavior there.
- A run now takes 23 to 73 minutes (more states), not 15. Both final audits (exit rounds) did not finish: one hit
  my 25 minute cap, the network-help-desk one lost its Chrome connection, and the half-life-dice re-run was stopped
  in cleanup. Neither verdict rests on them.

Left open for Cory: half-life-dice spec questions (an energy-ladder student action, rule 2; 5,730 vs 5,700 years),
Polish 9 partly held (card buttons show no short names at 375), dice tray reads as texture at 680x425 and 375;
network-help-desk polish notes (Wi-Fi arcs through the "On" badge at 800x500 call 4, two badges near the right wall at
680). Worktrees S:/CurioClass-codex-network-help-desk and S:/CurioClass-codex-half-life-dice (merged) and
S:/CurioClass-codex-scratch (evidence) can be deleted.

## Final look run: five clean tools (2026-10-29, local media only)

Cory picked five of the ten clean drafts (code-drawn art, voice recorded locally with Qwen3-TTS bank voices) for the
Final look while at work. Claude agents only; no Codex, no Gemini. Pushed as 0daba9a3.

| Tool | Final look | Fix round | Plan | Notes for Cory's review |
|---|---|---|---|---|
| career-cluster-explorer | PASS, plus the sensitivity re-check PASS | none | explore-first, 45 min | welcome talks ~3 s after a cluster opens; trail stop header wraps at 1366; two try lines assume a house or a car |
| song-form-builder | PASS | none | model-then-make, 45 min | listen to line 4 ("You changed A...") for a swallowed "A"; while-playing hints 46, 47, 52 can never be heard; Safari/Firefox first Play unchecked |
| teach-the-robot | ROUND 2, then PASS | Read plays each part's clip; welcome never late; look-alike line off the names; chart counts | explore-first, 40 min | a Cat card's line still crosses Dog pictures; first Mystery pet is ~10 s of narration |
| snowy-mail-route | ROUND 2, then PASS | welcomeAfter removed, event lines cut the welcome and intros, Go cuts the level intro; Pip off the Fish symbol; welcome take re-recorded | teach-then-practice, 40 min | arrow names drop while the welcome plays; level 8 hBuild can play after cards are down |
| stage-blocker | ROUND 2 (1 blocker), then PASS | a focus note needs the actor lit (kit/stage.js, stage.md, spec); results scroll into view; same-mode tap keeps its welcome; dark actors dimmed | model-then-make, 45 min | at 1366 the results scroll hides Run again (`nearest` was tried and broke 680x425, so `start` stays); The Note run is ~40 s |

Kit changes, both opt-in and backward compatible: `hold` on Curio.voice say (docs/KIT.md; 42 of 42 voice tests pass)
and the stage family's "Lit for the eye" rule. Every plan passes check_plans; the integrator read each plan as a
sub would and checked its paths, numbers and button names against the tool. Every Sub Day packet builds, with the
module's six Word Wall words on the backup sheet.

Deploy: built and checked (5261 pages, 81 built tools, 0 broken links). The first `npx wrangler deploy` was blocked by
the session's permission check; Cory said go and it deployed (version 6f87e8bf). Review Desk items 55 to 59 set to
ready, stats board refreshed (live 81, voice 11 drafts left).

## Cory's review notes, round 1 (2026-10-29)

Cory reviewed three on the Review Desk. song-form-builder: approved (status ok). The other two came back with notes,
fixed with local FLUX art on the 5080 (Cory's pick over code redraws):

| Tool | Note | Fix | Final look |
|---|---|---|---|
| teach-the-robot | "the dogs and cats look weird, its mostly the face" | 26 painted FLUX pets replace the code-drawn ones; Shadow, Noodle, Pebble redrawn after the first look (cartoon faces, collar); look-alike line starts on the forehead; card crops keep ear tips; truth badge moves beside the pet | FIX then PASS (final-art.md) |
| career-cluster-explorer | "the background graphics are not good and need upgraded" | 34 painted FLUX sprites on a painted land strip, signs kept as code text; art row redrawn after its easel painting showed people; 9 HOT markers moved | FIX then PASS (final-art.md, sensitivity clean) |
| career-cluster-explorer | "jobs and descriptions over the map" in Trails | each stop's card drawn at its dot, earlier stops labelled, end line pinned on the town; 121 layouts measured clean | same |

Lessons for local art: FLUX schnell takes "no X" as "draw X". The first town run ("festival at night", "no other
buildings, no people") painted busy street scenes with crowds; positive wording ("a single ..., shown as one
isolated game asset") gave clean sprites. Key-color tint in leg gaps: neutralize the tint, do not cut it (cutting
speckled white fur). Waffles kept: every redraw gave bat ears, which would contradict its floppy-ears clue.

Commit ba87ba5b. Site built and checked (5261 pages, 0 broken links); deployed (version 69c28008) once Cory lifted the permission block; desk items back to ready, the three comments answered and marked done.

## Cory's review notes, round 2 (2026-10-29 night)

Approved: teach-the-robot, career-cluster-explorer, and snowy-mail-route (approve-when-fixed). Snowy Mail Route: the
'Left!' take itself was clipped (0.56 s, ended mid-word); re-recorded with 5 takes (localvoice.py --redo 28), new take
1.04 s with a clean fade. Stage Blocker: in Run, a seat tap only showed at the next cue's crossfade (holds are 2.2 s or
more); setSeat now redraws the current run moment from the new seat at once (runSnap, runFit), measured about 4 ms
mid-hold, no console errors. Commit 3c1be2e9, deployed (version de7f192f). Stage Blocker back on the desk as ready.
