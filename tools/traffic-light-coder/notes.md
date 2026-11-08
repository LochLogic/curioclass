## What it teaches

Students explore first-match if-then rules through a working traffic signal model.
They edit conditions, actions and priority, then see the consequences on the street and its time record.
This is a Curiosity: freely chosen setups, no score, progression, quiz or finish.

## Key skills

- Combine conditions with "and".
- Predict which matching rule fires first.
- Connect car-light and walk-sign decisions.
- Trace an unsafe moment to its firing rule.
- Compare timing and rule order on repeatable traffic.

## Support at home

- Make an everyday if-then rule together: "If the plant's soil is dry, then water it."
- Invent two rules that could both fit. Discuss which one comes first and why.
- Describe a familiar routine with a missing condition and imagine what happens.

## A five-minute start

Press a curb button on Live street and follow the lit rule and firing tape. Pause and Step
to see one half-second pass round the loop. Edit any chip; the next check uses your change.
Setups offers repeatable traffic, in any order. Run script watches it; Read record advances
the same simulation to its observation endpoint. There is no prescribed path through the setups.

## Modes

Live street runs with editable rules, curb calls and an ambulance. Reset street keeps rules;
Defaults restores the four starting rules. Pause offers Step.

Setups keeps five independent programs for this page load. Reset setup restores that setup's
program. Speed switches between normal and four times street time. Stop or a rule tap halts
a script immediately. Unsafe record lines replay the three seconds before that moment.
The record reports what happened; no thresholds confer a grade or unlock anything.

## Setup observations

- Press to Cross begins with no rule taking GREEN to YELLOW. A condition and action can connect
  that transition to the button event, building the GREEN, YELLOW, RED, WALK sequence from rules.
- Don't Skip Yellow begins with a direct GREEN to RED action. Adding the yellow transition
  constructs the same signal sequence through conditions, rather than a fixed list of steps.
- Let Them Finish begins with a timed return to green. The record now observes whether cars
  get green back after each red, including unfinished reds and reds that end in yellow.
  The numeric check uses the existing 45 s tool reference, with no pass badge.
- Rush Hour preserves the original walker spacing and two-part timing/priority interaction.
  The record names the dominant rule during the longest red. Repeated WALK requests and
  actual new walks are counted separately, because an active WALK request does nothing.
- Ambulance reads the vehicle's stopped flag on every beat until it clears the crossing,
  including queues continuing beyond the detector's active interval. A long yellow cannot
  produce "Never stopped" when the vehicle actually stopped.

## Talk questions

- Why can a rule lower down lose its turn even when its condition fits?
- Which sensor tells us everyone has finished crossing?
- Which observation changes if you move that rule?
- What happens when a walker presses while an ambulance approaches?

## Good to know

This is a simplified programming model, not current signal engineering guidance.
Historical MUTCD 2009 examples inform a 7 s WALK and a 10 s flashing clearance for
35 feet divided by 3.5 feet per second. Walkers take 10 s to cross. The fixed-speed driver,
two-second yellow decision, traffic scripts and half-second rule loop are original model choices.
An active WALK request cannot restart the walk. Repeated curb presses count once per waiting walker.

The 60 s walker wait, 30 s green, 45 s red and 10 s empty-red references are the tool's own.
A script observes at most 120 street seconds; the live street continues freely. Rules stay
only in page memory. Only Motion persists on this device; Sound and rules last for this page. Nothing leaves it.

Keyboard: Tab to a rule, Enter to edit; Left and Right switch chip slots. Tab among choices,
Enter chooses, and Done or Escape returns. Alt plus Up or Down moves a rule; Delete removes it.
Motion off removes gliding and blinking while preserving timing.

## Standards coverage

The legacy module references E3-ALG-PS-01, E3-PRO-PD-04 and E3-PRO-TR-08
(2017 crosswalk 1B-AP-10, 1B-AP-15, 1B-AP-11). Here students author selection through conditions,
use button and detector events, and test and trace rules. They build signal sequences indirectly
through state transitions. Iteration is the engine's fixed half-second loop, named beside Step
and in the Manual; students inspect it but do not author that loop. These are partial contributions
to the combined standards, not direct practice of every part. Module reassignment remains an owner
decision outside these permitted folders. No standards wording is reproduced.

## Sources

- FHWA MUTCD 2009, 4D.26 and 4D.27: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm
- FHWA MUTCD 2009, 4E.06 and 4E.08: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4e.htm
- Licence: public domain, explicitly confirmed in FHWA's General FAQ:
  https://mutcd-dr.fhwa.dot.gov/knowledge/faqs/faq_general.htm
- Independent timing cross-check: Minnesota DOT Traffic Signals 101 Course Manual,
  https://www.dot.mn.gov/trafficeng/signals/docs/signals-101-manual.pdf.
  Reference only; no Minnesota text, figures or dataset incorporated.
- Original scripts, thresholds, driver model and explanatory writing: Curio Class, content CC BY 4.0, code MIT.
- Existing illustrations generated with OpenAI gpt-image and edited for Curio Class, retained unchanged.
- CSTA codes are reference identifiers only: https://csteachers.org/k12standards/. No licensed standard text copied.
