# Draft: the Refine step (not in use yet)

Cory's idea (2026-10-27): split "build" into **Build**, the first solid draft, and **Refine**, a multi-agent review
that looks the tool over and polishes it. This draft replaces docs/agents/VERIFY.md with docs/agents/REFINE.md and
rewrites the pipeline rows in RUNBOOK.md. Nothing changes until Cory approves it.

## What changes, in short

| | Today (Verify) | Draft (Refine) |
|---|---|---|
| Who looks | one cold verify agent | three cold lens agents at once (Teaching, Play, Craft), plus a sensitivity agent when rule 5 applies |
| What they look for | what is wrong | what is wrong **and** what would make it better (a new "polish" level) |
| Who fixes | the same build agent | the same build agent, now also taking the polish items the merge accepts |
| How it ends | a re-verify | one fresh exit check against a fixed gate, at most two rounds |
| File | tools/<id>/verify.md | tools/<id>/refine/ (one file per lens) and tools/<id>/refine.md (the merged list and the verdict) |
| Cost | about 2 agent runs a tool | about 5 to 6 agent runs a tool (3 lenses, 1 exit check, often a second round) |

Why three lenses and not one bigger agent: one reviewer with a long checklist skims. A narrow brief finds more, and
three run in parallel, so the step takes about as long as one verify. Three lenses and a build agent fit inside the
3 to 4 agent limit.

---

## Part 1: the new brief, docs/agents/REFINE.md

> # Refine brief
>
> Refine takes ONE Curio Class tool from a first solid draft (Build) to something ready for Cory's review. It has
> three parts: **look** (three cold lens agents), **polish** (the build agent fixes), **exit check** (one cold agent
> confirms the gate). Read `docs/agents/STANDARDS.md` and `docs/agents/decisions/BASELINE.md` first; they win over
> this brief.
>
> ## Look: three lenses, run at once
>
> Each lens agent is fresh and cold: you did not build the tool and you owe it nothing. Do not fix anything. Each lens
> reads `tools/<id>/spec.md`, then `src.html`, `notes.md`, `art/prompts.json` and `voice/lines.json`, bundles with
> `CURIO_DRAFT=1 python scripts/bundle_tool.py <id>`, and works in its own scratch folder with its own Chrome profile
> and port (RUNBOOK, Agent Chrome hygiene). Write `tools/<id>/refine/<lens>.md` only.
>
> **Teaching lens: does it teach what it claims, to this grade?**
> 1. Every standard code on the tool's module is really taught by something the student does (BASELINE rule 2). A
>    code that is only mentioned is a finding: name the activity that would teach it, or say the code should move.
> 2. Every "Done when" in the spec, tested.
> 3. Facts: every number, date and claim on screen or in notes matches the spec's Sources. Recompute numbers yourself.
> 4. Nothing gives an answer away in a predict, quiz or hidden-information mode (POLISH, Games and quizzes).
> 5. Language is plain and right for the grade; teacher notes name sensitive topics the standards cover (rule 8).
> 6. Guardrails: K-2 teacher-led; hard history has no points, timers or win states; health topics neutral.
> 7. Flag anything cultural, Native or hard-history for the sensitivity agent (rule 5). Don't judge it yourself.
>
> **Play lens: what is it like to use?** Play it twice: once as a student of that grade alone at home with no teacher
> (rule 4), once as a teacher projecting it to a class.
> 1. Frames (`scripts/shoot.py` or `scripts/drive.py`) of the default screen, every mode, the extremes (smallest and
>    largest values, empty states, the end of a round), a narrow window and 1366x768. Look at every frame: overlaps,
>    clipping, text over art, unreadable sizes, placeholder art in odd spots.
> 2. The defaults work for a solo student: the first screen says what to do, every waiting moment names the next
>    action and the control (spoken once, then hint only).
> 3. POLISH.md, all of it: pacing for reading aloud, calm mode keeps time, anything shown twice matches, words match
>    the state.
> 4. Feel: where did you get bored, lost or unsure? Where is a moment flat that could land? These are polish items.
>
> **Craft lens: is it built right?**
> 1. Contract: one file, no network requests, under 2 MB, kit used (not re-implemented), no console errors.
> 2. Access: keyboard, visible focus, 44 px targets (60 px for K-2), color never the only signal; Motion, Sound and
>    Read work.
> 3. Lines: every spoken line is in `voice/lines.json` and `allLines()`, word for word; each line matches the state.
> 4. The standard voice check (kept word for word from today's VERIFY.md), with its counts table.
> 5. Art: every `art:` token has a prompts.json entry; people are marked `people: true`; local models never draw people.
> 6. Words: no em dashes, "Curio Class" never "Curio" alone, classroom-safe language (rule 6), privacy stated where
>    anything is stored (rule 7).
>
> **Sensitivity agent (only when rule 5 applies):** a fresh agent checks accuracy and respect for the cultural,
> Native or hard-history content and writes `refine/sensitivity.md`. Its PASS is part of the gate.
>
> **Every lens reports the same way:** each finding as where (file:line or mode), what, how you saw it (the frame or
> the check), and a level:
> - **blocker**: wrong, broken or unsafe; cannot go to Cory;
> - **should fix**: a real flaw a teacher or student would notice;
> - **polish**: not wrong, but a clear step up (a flat moment, a confusing word, a tighter layout). Say what better
>   looks like;
> - **nit**: small and optional.
> Don't pad a short list. A lens with nothing to say writes "Nothing found" and the frames it looked at.
>
> ## Merge (the integrator)
>
> Read the three lens files. Merge duplicates, settle any lens disagreement with BASELINE, and write
> `tools/<id>/refine.md`: one ranked list (blockers, should fix, then the polish items you accept). Accept a polish
> item when it improves what the student sees or hears and stays inside the spec. A polish item that would change the
> spec (what the tool teaches, a new mode) goes to the spec's open questions, not to the builder.
>
> ## Polish (the same build agent)
>
> SendMessage the merged list to the build agent that built the tool, blockers first. It fixes every blocker and
> should-fix and the accepted polish items, re-shoots its own frames, and reports what it changed.
>
> ## Exit check (one fresh cold agent)
>
> Re-check each item on the merged list yourself and look for regressions (re-shoot the default screen, every mode
> and the frames tied to each fix). Then check the gate. **All must hold:**
> 1. every "Done when" passes;
> 2. every code on the module is taught, or its move is written down (rule 2);
> 3. the defaults work for a solo student (rule 4);
> 4. the sensitivity agent passed, where rule 5 applies;
> 5. no blocker or should-fix is open;
> 6. the bundle is clean, under 2 MB, no console errors, no network requests;
> 7. the voice check counts are right.
> Write the verdict as the first line of `refine.md`, `PASS` or `ROUND 2` with the open items, and append the
> check below the merged list.
>
> ## Rounds
>
> At most two rounds (look, polish, exit check). Round 2 runs only the lenses that had open items. If round 2 still
> fails the gate, the tool does not go on: the integrator either fixes one narrow item itself (with an "Integrator
> fix" note, as today) or brings it to Cory with the open list. Polish items left over never block; they go in the
> Review Desk "changed" note as "known, not done".

---

## Part 2: RUNBOOK.md changes

**The pipeline table:** the Verify, Fix and Re-verify rows become:

| Step | Agent | Prompt (fill in the id) |
|---|---|---|
| Look | 3 fresh, cold, at once (+1 sensitivity when rule 5 applies) | "You are the `<lens>` lens for ONE Curio Class tool: `<id>`. Repo: S:\CurioClass. Follow the `<lens>` section of docs/agents/REFINE.md exactly, cold, plus STANDARDS.md and BASELINE.md. Write only tools/<id>/refine/`<lens>`.md. Do not fix anything, do not commit." |
| Merge | you | Merge the lens files into tools/<id>/refine.md (REFINE.md, Merge). |
| Polish | the SAME build agent (SendMessage to it) | Paste refine.md's list, blockers first. "Fix every blocker and should-fix and the accepted polish items. Re-shoot your frames. Report what changed." |
| Exit check | fresh, cold | "Follow the Exit check in docs/agents/REFINE.md for `<id>`. Re-check every item in tools/<id>/refine.md and the gate. Write the verdict as refine.md's first line." |
| Plan | fresh, after PASS | (unchanged) |

**Under the table:** "At most 2 fix rounds..." becomes "At most two Refine rounds (REFINE.md, Rounds)."

**Agent count:** three lenses plus one build agent is four, the top of the limit. While a tool is in Look, don't start
another build; start it when Look ends.

**Going live, step 4:** the Review Desk "changed" note adds one line: what Refine polished, and any "known, not done"
items.

**Open items:** add "Refine replaced Verify on <date>. Tools verified before it keep their verify.md; the board counts
either file."

## Part 3: the board

`scripts/board.py` counts a tool at the Refine stage when `refine.md` starts with PASS, or, for tools built before
the change, `verify.md` does. The internal stage key stays `verified`, so docs/BUILD-BOARD.md and the desk keep
working; only the label reads Refine. VERIFY.md moves to `docs/agents/archive/` with a pointer to REFINE.md.

## Choices in this draft (say if any should change)

1. **Three lenses, not more.** A fourth (say, a separate Words lens) would break the agent limit while a build runs.
2. **Polish goes back to the original builder,** not to a separate polish agent. The builder knows the code; a new
   agent would spend most of its run learning it.
3. **The integrator filters polish items.** Lens agents tend to suggest more than a tool needs; the merge keeps only
   what improves the student's experience within the spec.
4. **About 2.5 times the agent cost per tool.** On a batch of 10 tools that is about 30 more agent runs. The payoff is
   fewer rounds on the Review Desk.
