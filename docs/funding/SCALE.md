# The scale of Curio Class

Facts for later marketing and funding pieces: how large the project is and what it took to keep it in order. Every
number has a date and how it was counted. Numbers are added at milestones, never edited after the fact.

## Before the consolidation (2026-11-24)

Counted from the repository on main (`git ls-files`, `git rev-list --count HEAD`) and the consolidation census.

| What | Count |
|---|---|
| Files tracked in the repository | 35,364 |
| Commits | 1,358 |
| Files under courses/ | 4,865 |
| Course folders with work started | 19 |
| Day files written | 918 |
| Courses planned | 120 (118 active) |
| Tool folders | 821 (564 at Spec) |
| Topic modules in the older catalog | 815 |
| Standard-to-tool coverage rows | 2,400 |
| Python scripts that build and check the work | 115 |
| AI platforms that had worked on it | 3 (Claude, Codex, Antigravity), across hundreds of sessions |
| Files the Codex working folder (S:\CurioClass-codex) wrote or changed after 2026-11-01, outside git | 1,188,961 (scratch work, run logs and installed Python packages; `find -newer`, a few locked folders not counted) |

The consolidation (docs/CONSOLIDATION-PLAN.md) brings every platform's work back into one folder, one curriculum
model and permanent ids, built for the tens of thousands of files the finished curriculum will hold.

## Milestone: funding goes aggressive (2026-11-27)

Counted from the repository on main (`git ls-files`, `git rev-list --count HEAD`) and from the AI session logs still on
disk.

| What | Count |
|---|---|
| Files tracked in the repository | 38,453 |
| Commits | 1,978 (first commit 2026-10-22) |
| Day files written (lesson days) | 2,115 |
| Courses planned | 120 (118 active), every active course with a full-year scope and sequence |
| Courses finished and signed off | Kindergarten to grade 3 science (2026-11-23) |
| Interactive tools live | 92 |
| Tool folders | 823 |
| AI tokens processed, counted from logs still on disk | more than 4.2 billion (Codex 4.04 billion across 555 Curio Class sessions, 2026-11-20 to 2026-11-27; Claude Code 0.2 billion, 2026-11-27 only). Older logs were cleared by the tools, so the true total since 2026-10-22 is higher. Counts include cached input, the way the vendors bill and report usage. Script: the session scratch tok.py (sums `total_token_usage` per Codex session and `usage` per Claude message). |
| Development time | Five weeks of near-daily build since 2026-10-22, with AI runs going overnight |

## Outreach

One row per send, added when Cory reports it (an unreported draft is not sent). Plan and queue: OUTREACH-PLAN.md.

| Date | To | What | Reference | Status |
|---|---|---|---|---|
| 2026-11-27 | U.S. Department of Education (regulations.gov, docket ED-2026-OS-3169-0001) | Public comment | Comment Tracking Number mwz-y2ap-8ofp | Posted by Cory |
| 2026-11-27 | Colorado Nonprofit Development Center | Fiscal sponsorship inquiry (formsite) | Reached CNDC's "Application Submitted" page; CNDC says it replies within one week | Submitted by Cory |
| 2026-11-27 | GitHub Secure Open Source Fund | Application (Microsoft Form) | none shown | Submitted by Cory |
| 2026-11-27 | Anthropic, Claude for Open Source | Application (6 months of Claude Max/Ultra), text in applications/claude-for-oss.txt | Thank-you page shown: "If approved, you'll get a link to activate Claude Max" | Submitted (page went to thank-you right after Claude pressed "Use this repository" in Cory's session) |
| 2026-11-27 | CU Boulder iSAT (Tamara Sumner, AI Institute inbox) | IES Seedlings to Scale partner note | Gmail Sent | Sent by Cory (from his Gmail address) |
| 2026-11-27 | DU (Peter Organisciak) | IES Seedlings to Scale partner note | Gmail Sent | Sent by Cory (from his Gmail address) |
| 2026-11-27 | CU Boulder Research & Innovation Office | NSF TechAccess Colorado hub partner note | Gmail Sent | Sent by Cory (from his Gmail address) |
| 2026-11-27 | Kiwix | NLnet Restack partner idea | Gmail Sent | Sent by Cory (from cory@curioclass.org) |
| 2026-11-27 | Colorado Department of Education OER (Mallorie Klemm, OERColorado) | Open-library fit questions | Gmail Sent | Sent by Cory (from cory@curioclass.org) |
| 2026-11-27 | Oak National Academy (England) | Peer call request on AI quality checks | Gmail Sent | Sent by Cory (from cory@curioclass.org) |
| 2026-11-27 | Gates Family Foundation (Russell Ramsey, Ana Soler; info@ cc) | 20-minute introduction request | Gmail Sent | Sent by Cory |
| 2026-11-27 | The Denver Foundation (cgp@) | Meeting before Community Grants Cycle 1 (opens 2027-01-15) | Gmail Sent | Sent by Cory |
| 2026-11-27 | Rose Community Foundation (for VJ Brown, via info@) | Fit introduction | Gmail Sent | Sent by Cory |
| 2026-11-27 | Colorado Education Initiative (info@) | District partner introduction | Gmail Sent | Sent by Cory |
| 2026-11-27 | New America (An-Me Chung) | US answer to her Oak piece | Gmail Sent | Sent by Cory |

## After the consolidation

Filled at step 6 with the same counts, plus what moved, what was archived and what the new index links.
