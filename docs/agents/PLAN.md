# Plan agent brief

You write the lesson plan for ONE Curio Class tool that has passed verify. A teacher should be able to print it and
run tomorrow's class from it, and a substitute who has never seen the tool should manage too.

## Read first

0. `docs/agents/STANDARDS.md`: standing rules. They apply to plans.
1. `docs/LESSON-PLANS.md`: the format, the arcs and the rules. Follow it exactly.
2. `tools/<tool-id>/spec.md`, `notes.md` and `src.html` (the content lists, button labels and modes).
3. The module's row in `data/modules.csv` for its standards, and `tools/melt-or-not/plan.md`,
   `tools/contraction-crusher/plan.md` and `tools/hamburger-paragraph/plan.md` as the quality bar.

## Play it before you write

`python scripts/bundle_tool.py <tool-id>` (add `CURIO_DRAFT=1` for a draft), then `python scripts/shoot.py` frames of
the default screen and each mode. You are writing about what is on the screen, so look at it.

## Write `tools/<tool-id>/plan.md`

1. **Pick the arc** from what the tool does: explore tools explore first, practice tools come after a short teach,
   builders model and then students make. Say why in your report.
2. **Pick the focus standard**: the one or two module codes the tool really teaches, not all of them.
3. **The hook** is a question or a small surprise from the students' world that opens the standard. Not "today we
   will learn".
4. **The tool part** names the tool's own buttons, items and modes in bold, in the order to use them, and the moments
   to stop and ask. Use the tool's real content (which item first, which one is the surprise).
5. **Questions** go in quotes with the answers we expect in parentheses. Ask about thinking, not just answers.
6. **Apply, Make or Share** moves the idea off the screen: talk, draw, sort real things, write.
7. **The exit check** is one quick task that shows who got it. K-2: oral or physical.
8. **Support and stretch** and **Short on time** as the format says.

## Check before you report

`python scripts/check_plans.py <tool-id>` passes. Read the plan once as the teacher: is every step something you
could do with only this page and the tool? Report: the arc and why, the focus standard, anything in the tool that
made the plan awkward (that is a finding for the tool), and the check result. Do not commit.
