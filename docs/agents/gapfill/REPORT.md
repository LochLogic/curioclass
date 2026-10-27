# Gap fill report (2026-10-27)

Cory asked for the data-only code pass and then to fill the standards gaps "smartly and completely", open to new
tools. Both are done and merged into data/. The catalog grows from 586 to 762 planned tools. Every framework on an
official list is now fully claimed except 41 ELA codes left out by design. Nothing new is specced or built yet.

Per-domain detail and reasoning: `core/`, `cs/`, `ela/`, `social/` and `arts-health/notes.md` in this folder. The
staging files (codes.txt, modules.txt, concepts.txt, tags.csv) stay as the record of what was merged.

## Coverage, all planned tools

| Framework (official list) | Unit | Before (wave1-gaps.md) | After |
|---|---|---|---|
| NGSS performance expectations | 208 | 196 | **208** |
| CCSS math clusters | 147 | 143 | **147** |
| CCSS ELA grade-level standards | 455 | 169 | **414** (41 left out by design) |
| C3 social studies indicators (D1 to D4) | 283 | 116 | **283** |
| CSTA 2026 computer science | 196 | 85 | **196** |
| NCAS arts anchors x band | 220 cells | 65 | **220** |
| NHES health x band | 32 | 23 | **32** |
| SHAPE PE x band | 16 | 9 | **16** |
| AASL x band | 24 | 13 | **24** |
| CASEL x band | 20 | 8 | **20** |
| WIDA standards x band | 20 | 20 | 20 |
| WIDA language uses x band | 16 | 11 | **16** |
| NSPFE x benchmark band | 18 | 6 | **18** |

Rerun with `python scripts/overlap/coverage.py`. Before this pass, the C3 numbers counted only D2 codes, because the
validator rejected D1, D3 and D4. It now checks C3 and ELA against the official lists.

**Left out by design (ELA, 41 codes):**
- RL.10 and RI.10 in every grade (22): reading a range of texts over a year is a program, not a tool skill.
- W.10 in grades 3-12 (8): routine writing.
- W.6 in every grade (11): every writing tool on the site is digital, so claiming it would be empty.

## What changed

**Code adds:** 108 code lines changing 107 existing modules, added only where the tool already does the work.
- Every add was checked against the tool's concept, spec or plan.
- The `- Standards` lines of 30 specced (not live) tools were updated to match. All 75 wave 1 specs still claim
  exactly their module codes (`wave_standards.py`).
- Six planned science concepts were extended by a clause so their new NGSS codes are honest (core/notes.md).
- 11 live tools gained codes, each checked against its spec or plan: art-passport, beat-buddies, comeback-club,
  community-project-planner, concert-ticket-market, feelings-faces, mind-map, robot-dance, safety-street,
  walk-in-their-shoes and wonder-wall. No live tool's page or code changed; the new codes show on the site at the
  next deploy.

**New tools: 176, one new module each.**

| Subject | K-2 | 3-5 | 6-8 | 6-12 | 9-12 | Total |
|---|---|---|---|---|---|---|
| ELA | 10 | 12 | 12 | | 7 | 41 |
| Social studies | 7 | 14 | 12 | | 8 | 41 |
| Arts | 11 | 10 | 9 | | 7 | 37 |
| Computer science | 7 | 9 | 8 | | 8 | 32 |
| Health and PE | 2 | 4 | | 1 | 1 | 8 |
| CTE (6-8 finance and markets) | | | 5 | | | 5 |
| Library | 1 | 1 | 1 | | 2 | 5 |
| ELD, SEL, science, math | 2 | | 1 | 1 | 3 | 7 |

- **Band spans:** most new modules span a band (`3-5`, `6-8`, `k-2`) and carry each grade's code. The tool gets a
  grade switch; each domain's notes say what the switch changes.
- **Arts:** all five disciplines now cover every anchor in every band, including anchor 10 and theater responding.
  Media arts now opens at K (the course is k-12).
- **Health topic holes are filled:**
  - Weekend Substance Choices (9-12)
  - Recess Upstander (3-5)
  - Safety Sweep House (3-5: home, online and medicine safety)
  - Worry Size Sorter (3-5 mental health)

**Overlap:** checked three ways.
- Each folder ran the clash rule against the catalog and the other folders.
- After the merge, the whole catalog was rerun. It still finds 93 rule hits, the same pairs as before; none involves
  a new tool.
- A word scan caught same-picture repeats in a band, which the rule cannot see. Seven were re-worlded:

| Was | Now | Why |
|---|---|---|
| Attic Trunk | Capsule From 1965 | Attic Gadget Box is also a K-2 grandparent's attic box |
| Festival Folk Dances | Family Dance Night | Festival Parade is the K-2 world festival |
| Puppet Wants More | Owl Wants More | four K-2 puppets |
| How Do You Know? (puppet) | a talking backpack | four K-2 puppets |
| Behind the Documentary | Behind the Podcast | Mini Documentary Crew is also 9-12 |
| Bike Fund Chances | Skateboard Fund Chances | Learn and Earn is the other 3-5 bike |
| Snack Ad Questions | Cereal Ad Questions | four K-2 snack tools |

**Two crowding warnings are left, each judged fine:**
- Mini Documentary Crew is the sixth film-media tool in 9-12.
- Safety Sweep House is the sixth home tool in 3-5; home is its subject.

**Tooling:**
- **New scripts:**
  - `scripts/add_codes.py` writes code edits to data/modules/*.txt. modules.csv is generated, and wave 1's 14 code
    adds had gone only into modules.csv, so they would have been lost on the next build; they are restored.
  - `scripts/overlap/stage_check.py` validates a staging folder, runs the clash and crowding checks and projects
    coverage.
  - `scripts/overlap/stage_merge.py` merges a checked folder.
- **Fixed:**
  - `scripts/standards.py` validates ELA and C3 against the official lists, so L.K.3 is now rejected and was removed.
  - `wave_standards.py` reads ELA and C3 codes and applies through add_codes.py.
  - `coverage.py` accepts 9-10 and 11-12 spans.
- **Checks:** check_codes, check_concepts and check_words are clean. A local `build_site.py` run built 4048 pages with
  no errors; nothing was deployed.

## Questions for Cory

**Answered 2026-10-27:**
- Q1 sexual health past puberty: paused. Do not add a tool or plan one until Cory reopens it.
- Q2 Weekend Substance Choices: naming cannabis edibles and underage drinking is fine.
- Q4 tool count: keep all 176. A weak tool may be cut only if every code it carries stays covered by another
  tool. A check of all 176 found one new tool whose codes are all held elsewhere (Safety Sweep House), and it fills
  the home and medicine safety topic hole, so nothing was cut. The four named social studies candidates each hold
  two codes no other tool claims.
- Q3 and Q5 to Q11: still open. Cory will go through them on the evening of 2026-10-27; until then the defaults below
  are placeholders, not decisions.

None of these blocks the next spec wave. Each new tool's spec can settle its own, so the defaults below stand unless
you say otherwise.

**Content (needed before those specs are written):**
1. **Sexual health past puberty:** add a 6-12 tool on consent, contraception and STI prevention? Default: not added.
2. **Weekend Substance Choices (9-12):** it names cannabis edibles and underage drinking. Is that the right
   frankness, or should it stay with vaping and alcohol like Pressure Point?
3. **Four social studies tools touch hard history.** Default: include each topic plainly, at grade level.
   - Made for Whom? (a railroad poster selling land taken from Native nations)
   - Voices on the Vote (who was excluded from voting)
   - Missing Voices Archive (whose records were kept in 1918)
   - Cocoa Chain (mention child labor, or keep only the drought?)

**Scope:**

4. **176 new tools.** If that is too many, the agents named the cheapest cuts:
   - social studies: Barter Bay, Unlabeled Archive, The Shrinking Lake, Economy Checkup
   - media arts: fold the three K-2 media arts tools into two
   - Each cut reopens a few codes.
5. **Courses for 6-8:** middle school has no civics or economics course, so the 6-8 finance and market tools sit in
   cte-explore and the 6-8 civics tools in us-hist-8. Add a 6-8 civics and economics course instead?
6. **K-2 span modules:** the K-2 CS and other new modules use grade k-2 with one code per grade. Default: keep. The
   alternative is splitting into single grades, about 10 more tools.

**Codes:**

7. **Codes across subjects:** some codes sit on modules from other subjects where that tool does the work. Default:
   keep. Examples:
   - ELA codes on 5 ELD and library tools
   - C3 and NSPFE codes on grocery-run, lemonade-stand and climate-postcards
   - a CS code on the K math tool toy-box-sort
   - MA:Re8 on the ELA tool page-to-screen
   - SHAPE.S2 on a dance tool
8. **Busy modules:** some carry 5 to 8 codes across a band, and a few arts tools carry 4 or 5 anchors. Default: keep.
   Examples: Asking With Data (8 codes, K-2 CS), ai-evaluator (6), School Wall Mural.
9. **input-or-output (K-2 CS):** its spec says it does not teach E2-SYS-SE-12, but its module carries that code.
   Default: leave it until that tool is touched.
10. **Media arts Connecting anchors:** the 2021 NCAS handout swaps the MA:Cn10 and MA:Cn11 labels compared with the
    anchor definitions. We followed the definitions; the cell counts are unaffected either way.

**Recorded elsewhere:**

11. **fact-check-desk (ELA 8):** still clashes with misleading-charts. The ELA agent's reshape idea is almanac
    editors checking a town record book; see ela/notes.md. It is settled when fact-check-desk is specced.
