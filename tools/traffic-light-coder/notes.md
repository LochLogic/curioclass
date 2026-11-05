## What it teaches

Students write if-then rules, test them against a goal, and use a report to debug their program.
They learn that the first matching rule wins when a program checks conditions from the top.

## Key skills

- Combine conditions with "and".
- Predict which matching rule will fire first.
- Break a crossing into car-light and walk-sign decisions.
- Test a program and trace an unsafe result to its rule.
- Change timing and rule order, then test again.

## Support at home

- Make an everyday if-then rule together: "If the plant's soil is dry, then water it."
- Invent two rules that could both fit. Discuss which one should come first and why.
- Describe a familiar routine with a missing condition. Ask your child to spot and repair it.

## A five-minute start

Open Watch the Street. Press a curb button and follow the glowing rule and firing ribbon.
Pause and use Step to see one half-second check. A program checks its rules again and again;
it does not perform every card as a sequence.

Open Street Jobs. Run the first job without changes and read the report. Add the missing
green-to-yellow rule, set its condition to button pressed, and test again.

## Modes

Watch the Street runs live with editable rules, curb calls and an ambulance. Reset street
keeps the program; Default rules restores the four starting rules. Pause offers Step.

Street Jobs has five separate programs for this page load. Start over restores the current
job. A test runs at four times street speed; Speed switches to normal speed. Stop or a rule
tap stops the test immediately. Skip to report completes the same simulation without waiting.
Unsafe report lines replay from three seconds before the moment and pause on the named rule.
The report strip shows the actual green, yellow and red intervals from your test.

## The five jobs

1. Press to Cross: add GREEN and button pressed, then turn YELLOW.
2. Don't Skip Yellow: change the first action to YELLOW, then add YELLOW and been 3 s, then RED.
3. Let Them Finish: change the return-to-green condition from been 10 s to walk is done.
4. Rush Hour: add been 30 s to the first rule. Add been 10 s to the walk-is-done return rule
   and move that return rule above start WALK. Both timing and priority matter.
5. Ambulance!: add GREEN and ambulance coming, then keep lights, above every other rule.

## Talk questions

- Why can a rule at the bottom never get a turn even when its condition fits?
- Which sensor tells us everyone has finished crossing?
- Which part of the report would change if you moved that rule?
- What should win when a walker presses while an ambulance approaches?

## Good to know

This is a classroom model. A real signal requires engineering, local rules and many additional
safety systems. The tool uses the cited MUTCD 2009 timing examples, not current design guidance.
WALK lasts 7 seconds; a flashing hand lasts 10 seconds for a 35-foot crossing at 3.5 feet per second.
Walkers take 10 seconds to cross. Repeated presses by the same waiting walker count once.

Every half second the first complete matching rule fires. A press or a walk-sign interval
ending at a check becomes available to rules on the next check. Ambulance detection in job 5
is true from checks 36.0 through 45.5. Incomplete rules are skipped. An active WALK cannot restart.
Green durations still open when a test ends are excluded from the shortest-green check.

The 60-second walker wait, 30-second green, 45-second red and 10-second empty-red thresholds
are this tool's own fairness limits. The last is report-only. Tests run at most 120 street seconds.
Rules and completed jobs are kept only for this page load. Only kit settings persist on the device; they never leave it.

Keyboard: Tab to a rule, Enter to edit; Left and Right switch chip slots in the picker.
Tab among choices and Enter to choose, Done or Escape to return. Alt plus Up or Down moves
the focused rule; Delete removes it. All controls also work with Tab and Enter.
Motion off removes gliding and blinking while keeping street time and rule checks unchanged.

The module's three standards are practiced directly: selecting conditions, constructing a
combined program, and using repeatable tests to find and repair bugs.

## Sources

- MUTCD 2009, 4D.26: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm
- MUTCD 2009, 4E.06 and 4E.08: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4e.htm
- Figure 4E-2: https://mutcd.fhwa.dot.gov/htm/2009/part4/fig4e_02_longdesc.htm
- CSTA 2017: https://csteachers.org/k12standards/
- Code.org glossary: https://code.org/curriculum/docs/k-5/glossary
