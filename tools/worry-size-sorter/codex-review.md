# Codex review: worry-size-sorter

## Played
Cold grade 3-5 solo play preceded the builder report, handoff, notes and source: all 13 cards, five clues, all four tool sequences (including both full timed runs) and a week reflection. Also considered classroom projection. Warm, specific and reassuring; the shrinking cloud is the best moment.
Root: `S:\CurioClass-codex`. One review pass, no commits. Evidence stays in this tool's Scratch folder.

## Findings fixed
- **Blocker, general, Tools:** immediate Start/Stop plus 5-to-1 claimed the tool caused calm. Results now report the child's rating; early Stop is explicitly unfinished, with its own spoken response. No score or mastery reward was added.
- **Blocker, general, My week:** Finish on day one said the week got away and spoke that it was done. Early reflection now says "so far", uses an appropriate event line and makes all chips explicitly optional.
- **Blocker, general, Talk back:** swimming reassurance guaranteed shallow water and an instructor's position. Replaced it with asking the swim teacher for help learning safely.
- **Should fix, general, Sort/Talk back:** "Many kids say" and a claim about classmates' thoughts lacked evidence. Removed the implied survey and mind-reading claim; kept flexible worry sizing and realistic self-talk.
- **Should fix, general, Tools:** selecting a different worry left the old heading above the new bubble. Re-render the current tool with focus retained; heading and reply now agree.
- **Should fix, general, voice:** breathing completion still named Start; squeeze transitions gave no specific next-part instruction. Added state-matched Done/round-cap lines, next-part how lines and short fists/shoulders/toes event cues. The premise also remains in compact Read after a skipped welcome.
- **Should fix, general, focus/Read:** timed completion lost keyboard focus; automatic squeeze completion could hush Read. Focus follows Done/Next part; automatic transitions preserve Read.
- **Should fix, general, My week:** old reflection chips carried into a new goal. Reset both chip groups when a goal is set.
- **Should fix, general, notes:** a blanket US school-staff reporting statement could hide role/state differences and direct-report duties. Notes now distinguish applicable law from school procedure.
- **Should fix, general, art:** toe pose had exposed toes despite the specified socks and did not clearly teach curling. Redrew the same child with closed socks and curled fabric; kept rich painted style and people metadata.
- **Should fix, general, compact result:** extra early-stop explanation pushed the result low. Two result buttons now share a row; 680, phone and 1280x720 results remain visible. Phone square/check-in typography now stays inside its painting.
- **Polish, general, flat result:** the breathing scene reset to the same generic square after rating. It now shows this student's before-to-after check-in, with neutral wording and no success color.
- **Polish, general:** fixed the live countdown's "1 seconds" wording and added a comfortable, pain-free squeeze instruction.

## Findings left
- **Polish, general:** the week builder is the quietest interaction. Its complete choices, painted time tiles and personal goal are retained; no extra topic or game was added.
- Recorded friendly-dad clips remain a later media step under the build brief's no-recording rule. Browser fallback and queue behavior were tested; a specific recorded performance was not heard.

## Break it
- Empty-basket tapping: no progress. Five duplicate placements: still one card. Real jittered outside drag: returns after 300 ms, no ghost, zero progress. Real basket drag: one placement.
- All Small, all Medium and all Big were actually driven. The first two retain five Big cards; all Big accepts 13 and explains the eight optional adult-help choices. No scored "pass" can be farmed.
- Five identical talk-back taps: one distinct reply and only the middle cloud. A second distinct reply gives the small cloud. All three replies are intentionally helpful practice, not a hidden-answer quiz.
- Meter sweep and immediate Stop: only the chosen self-rating changes. Early Stop no longer claims successful practice or causation. Helpers remain the child's own preferences, not certified skill.
- Independently checked all 25 pairs: 10 lower, 10 higher, four unchanged, one calm start. The four extremes and actual rating paths agree.
- Incomplete goal: refused. Bedtime selected before/after Worry box: cleared or blocked. Today checks/unchecks; future mouse and keyboard attempts refuse. Zero/seven and day-eight reflection fixtures are correct.
- New-goal reflection chips reset. Blocked saving updates the privacy line. The goal and checked day survive reload. A local diary can trust a child's check mark; it is not tamper-proof attendance.
- 500 generated decks: 13 unique cards, Small then Medium first, no consecutive Big cards. Calendar arithmetic independently covers both DST changes, leap day and year end.
- Four three-count rounds stop at the cap; focus is on Done. Motion off keeps the 24-second initial run. Four-count initial run is 32 seconds; squeeze remains three 15-second parts.

## Voice walk
Held clicks at about two-second spacing, default tool settings, Sound on and Motion on. Initial card pickup correctly skips the welcome without consuming it; the premise stays in the hint and Read.
Final main path: Sort pickup, Small, Try a tool, before 4, full breathing, Done, after 3; Body clues; Talk back with two replies; all three squeeze parts; fold/post the worry; My week goal, today check and early reflection. See `final-voice-retry/results.json`.
Final timed cues: fists/shoulders/toes once each, let-go three times, inhale twice, hold four times and exhale twice; no timed cue was cut.
Side paths checked Read during breathing and the automatic squeeze transition, Sound-off Read, fast mode changes and day-eight entry. No automatic squeeze transition cut the Read log.

| Line/kind | Expected | Observed |
|---|---:|---:|
| Big safety event across five cards | 5 | 5 |
| Same reply event at two-second pace | 5 | 5 |
| howAfter across four tools, per page | 1 | 1, then silent |
| goalSet / early reflection, two new goals | 2 each | 2 each |
106 runtime strings exactly match `voice/lines.json`; no stale mode speech or console exception in successful interaction batches.

## Facts checked
Checked live on 2026-11-06; named guidance below supports the teaching, not a diagnosis or promised treatment outcome.
- Readiness/fight-or-flight, fast shallow breathing and gentle equal breath phases: [Cleveland Clinic](https://health.clevelandclinic.org/box-breathing-benefits).
- Fast heartbeat, sweating/shaking, stomachaches and sleep trouble: [CDC, Anxiety and Depression in Children](https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html).
- Worry lasting weeks or disrupting school/home/friends, and seeking help: [NIMH, Children and Mental Health](https://www.nimh.nih.gov/health/publications/children-and-mental-health).
- Stress/muscle-tension cycle, clench hands/shrug shoulders/curl toes, 4-10 seconds tense and 10-20 relaxed: [HealthLink BC](https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation). Tool uses 5/10, never into pain.
- Four equal four-count phases and comfort: Cleveland Clinic above. It suggests three to four rounds; the brief starts with two and offers a third/fourth. Three-count timing is a shorter implementation option, not a claimed clinical dose.
- Helpful, realistic self-talk and thoughts not being facts: [Anxiety Canada via HereToHelp](https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf). The eight situations/reply sets are fictional examples; removed unsupported guarantees and population claims.
- Asking a qualified swim instructor for help at a comfortable learning pace: [American Red Cross](https://www.redcross.org/take-a-class/swimming/swim-lessons/kids-swim-lessons).
- Paper worries, a box and adult conversation: [Just One Norfolk NHS](https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf). Avoid use just before bedtime: [YoungMinds](https://www.youngminds.org.uk/parent/blog/how-to-make-a-worry-box-a-guide-for-parents/).
- About ten minutes is an example within the 10-15-minute worry-time suggestion: [NHS Every Mind Matters](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/tackling-your-worries/), not a prescribed pediatric dose.
- Unsafe secrets, photo secrecy, trusted adults and continued telling: [Childhelp](https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/); online photo requests: [NCMEC NetSmartz](https://www.missingkids.org/content/dam/netsmartz/itc/downloadable/ITC%20Poster%20Kit.pdf). Doctors/help with persistent worries: NIMH above.
- Immediate US danger: [National 911 Program](https://www.911.gov/calling-911/). Teacher reporting cautions: [Michigan Department of Education](https://www.michigan.gov/mde/services/ed-serv/educator-conduct/abuse-neglect); state law and role govern the particular duty.
- S1 help/body information, S6 goal/track/reflect and S7 practice: [SHAPE America NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/), checked against the spec's student-action map.
- Source-independent arithmetic: `review-numbers.json` and browser checks reproduce 32/24-second breathing, 45-second squeeze, all meter branches and date differences. Recomputed contrasts agree: brand/white 6.23, brand/paper 5.85, ink/paper 14.81; basket white-text 6.09/5.93/8.01.

## Sensitivity
Abuse, being hurt, online exploitation, family illness and bodies warrant the next sensitivity lens. Check all five Big cards, m3/m4 replies, and the no-trouble reassurance as supportive wording rather than a guarantee about every adult's response.
The class is never asked for disclosures; one trusted adult and continued telling remain prominent. Parent/caregiver is one option among six; an unsafe family adult is not made mandatory. Notes name reporting duties. US 911 scope is explicit in notes.
All five people assets show the same specified child, naturally and fully clothed; all are marked people true. Check identity continuity and avoid reading one child's appearance as representative of who experiences worry. This review does not claim a separate cultural-review sign-off.

## Flattest moment left
Picking the week plan is slower than changing the cloud or folding the slip. The earned personal goal and seven-day chart give it purpose. Kept the strong art, motion and calm tone.

## Graphics
All 27 named assets checked in the contact sheet and scenes, including all five body poses, 13 vignettes, baskets/clouds/box and time tiles. One style; no missing art token. The spec's "26" heading actually lists 27.
Toe redraw uses the built-in OpenAI image tool; prompt is in `art/prompts.json`, raw PNG in `art/raw/ws-kid-toes.png`, accepted 600-pixel WebP keyed through `art.py --rekey`. No new scene or feature.
All four modes inspected at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe. Changed compact states re-shot at 680 and phone; grayscale, Motion off and keyboard frames inspected.
Bundle: 1249.4 KB. Art: about 861 KB; no recorded audio. Evidence folders include `cold-frames`, `layout`, `targeted`, `compact-recheck`, `phone-square`, cheat/input traces and `sheets`.

## Audit
Completed once, within the 40-minute limit, on Chrome 9961 and host 8765. Inspected all 87 audit PNGs in contact sheets and confirmed the affected 1280 frame at full size. Four mechanical leads concern the card/empty-basket first-tap welcome skips. These are specified behavior under the on-load rules and BASELINE 16; compact Read now retains the premise. The audit frame also exposed slight 1280x720 button clipping that its geometry did not flag. A scoped result-row repair and two targeted 1280 captures confirm it is fixed. No second audit.
Wave checks: hints/Read, focus, required sizes/targets, honest meters, no giveaways, actual standards actions, Motion off, complete choice sets, resize during activity, timely welcomes, unknown ratings, single-meaning labels, true badges, restored hints and no answer-copy shortcut.

## Left open
The specified browser fallback remains until the later recording pass. No clinical effectiveness, real-world practice verification or student usability study is claimed.
Two initial read commands and a few short inspections lacked explicit outer timeouts; subsequent long commands used the required bounds. A background read job initially used its default folder and was corrected before any write. Existing shared Python bytecode was unchanged; later Python runs disabled bytecode writes.
A host favicon 404 and harness startup/key/reload mistakes were isolated and corrected; successful replacement checks are named in the evidence. No unanswered questions were sent. Source guidance and the brief settled the narrow choices. All owned Chrome and host ports are closed; no temporary tool host remains. No known blocker or should-fix remains from this pass.
