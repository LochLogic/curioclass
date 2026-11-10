# Supreme Court Simulator

## One idea
Five case folders sit on the bench, each opening with the ordinary person who brought it: the Brown family of Topeka, whose daughter Linda had to cross railroad tracks to a segregated school (Brown v. Board of Education, 1954); Clarence Earl Gideon, who wrote his own petition in pencil from a Florida prison because he couldn't afford a lawyer (Gideon v. Wainwright, 1963); Mary Beth and John Tinker and Christopher Eckhardt, sent home for wearing black armbands against the Vietnam War (Tinker v. Des Moines, 1969); a fourteen-year-old whose purse was searched by a vice principal (New Jersey v. T.L.O., 1985); and Brandi Levy, a cheerleader suspended for an angry weekend Snapchat (Mahanoy Area School District v. B.L., 2021); for each the student reads the facts and the law, builds an argument for each side (claim, precedent, counterclaim), answers illustrated justices who probe the weak points, rules, and writes a short opinion; then the real decision appears with short passages from the majority and the dissent and what changed afterward; a "whose interest" panel shows how each party's interests and the justices' views of rights shaped the outcome, and the student marks where their own view tilted their ruling, so a twelfth grader learns how people use and challenge the law on public issues, how personal interests and perspectives shape how rights are applied, and how to refine claims and counterclaims with their strengths and limits.

## Not like
- checks-and-balances (12, spec): the three branches as a card game. Here the Court on rights cases.
- jury-room (12, spec): a jury weighing facts. Here justices weighing law.
- empire-debate (11, spec): a Senate debate. Here a courtroom argument.
- who-decides (12, spec): local civic action. Here constitutional cases.

## Who and how
- Grade 12, Social Studies (Government), module "Civil Rights and Liberties". Standards: D2.Civ.12.9-12 (analyze how people use and challenge local, state, national, and international laws to address a variety of public issues), D2.Civ.10.9-12 (analyze the impact and the appropriate roles of personal interests and perspectives on the application of civic virtues, democratic principles, constitutional rights, and human rights), D3.4.9-12 (refine claims and counterclaims attending to precision, significance, and knowledge conveyed through the claim while pointing out the strengths and limitations of both).
- Format: roleplay. Driver: one student alone, or two teams arguing while the class rules (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Five cases, each with facts, law, two arguments, justices' questions, a ruling and opinion, the real decision and the whose-interest panel. Extra: Two teams (the class splits into sides and argues; the class votes as the Court). tool.json `modes: ["The bench", "Two teams"]`, `minutes: "40-50"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.12.9-12 | Read how each person used or challenged the law, then what changed after the ruling | the person card; the "what changed" card | 2 |
| D3.4.9-12 | Build both arguments and refine each after the justices' questions, naming a strength and a limit | the argument builder; the justices' questions; the refine step | 3 |
| D2.Civ.10.9-12 | Fill the whose-interest panel and mark where the student's own view tilted the ruling | the panel with each party's interest and each side's view of the right | 4 |

## Screens and modes
Header (kit): title "Supreme Court Simulator"; `The bench`, `Two teams`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Supreme Court bench from the lawyer's lectern. Five folders, each with a photo or portrait of the person who brought the case. The welcome is queued (`welcomeAfter: true`): "Every one of these cases started with one person who thought a rule was wrong. You'll hear both sides and decide. Tap a folder." First hint: "Tap a case folder."

**A case (focus: the argument).** At 1366x768 the bench fills the left with the case panel right; at 680x425 the panel is a sheet. Steps:
1. The person: who they were and how they used or challenged the law.
2. The facts and the question, in one sentence each.
3. The law: the constitutional text and two earlier cases (for Brown, the Fourteenth Amendment and Plessy v. Ferguson, 1896; for Gideon, the Sixth Amendment and Betts v. Brady, 1942; for Tinker, the First Amendment; for T.L.O., the Fourth Amendment; for Mahanoy, Tinker itself).
4. Arguments: the student builds a claim, a precedent and a counterclaim for each side.
5. Questions: two illustrated justices (composites, labeled) ask about a weak point in each; the student refines the claim and names its strength and limit.
6. Ruling and opinion: the student rules and writes three sentences.

**The real decision.** The vote and a passage under 15 words from the majority and from a dissent:
- Brown (May 17, 1954): 9 to 0, Chief Justice Warren; with no dissent, Justice Harlan's lone dissent in Plessy (1896) is shown instead. What changed: Brown II (1955) and the slow, fought-over path to desegregation.
- Gideon (March 18, 1963): 9 to 0; states must provide lawyers to poor defendants in felony cases. What changed: Gideon was retried with a lawyer and acquitted; public defender systems grew.
- Tinker (February 24, 1969): 7 to 2; students don't "shed their constitutional rights" at the schoolhouse gate; Justice Black dissented.
- T.L.O. (January 15, 1985): 6 to 3 on the search question; schools need "reasonable suspicion", not probable cause; Justices Brennan, Marshall and Stevens dissented in part.
- Mahanoy (June 23, 2021): 8 to 1; the school went too far punishing off-campus speech, though schools keep some power off campus; Justice Thomas dissented.

**Whose interest (the aha, D2.Civ.10.9-12).** For each case the panel lists each party's interest (a family's, a school's, a state's, a student's) and how each side saw the right. The student marks where their own view (as a student, a future parent, a voter) pulled their ruling and whether that was appropriate. Narrator: "Justices bring their views to the bench too. The question is whether the reasons hold without them."

**The end.** The five rulings beside the Court's, the refined claims and the panel. `Print` prints them.

**Two teams (extra).** The class splits into sides for one case, argues, and votes as the Court; then the real decision.

## Content
- Five cases with facts, law, precedents, prompts, composite justices' questions, real votes and short quotes (credited), what-changed cards, the panel.
- Court opinions are public domain; no oral-argument audio is used.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The ruling waits until both arguments are refined; the real decision waits for the student's opinion.
- Keyboard: Tab to folders, steps, the builder, questions, the ruling and the panel; Enter to choose.
- With Motion off folders open without sliding.

## Look
- Accent `--brand` #3d2b56 court purple (header, folders, the builder); gold #f4c542 (the step in hand, the ruling); paper #f4f1f8; ink #120a1c; muted #57525e.
- Contrast (WCAG 2.1, computed): white on brand 12.51:1; brand on paper 11.19:1; ink on paper 17.30:1; muted on paper 6.77:1; ink on gold 11.89:1.
- Never color alone: sides carry names; votes carry numbers.
- Different from this batch (branch amber, campaign blue, charter green, jury brown).

## Art
- Public domain or licensed photographs, checked at build (Library of Congress, National Archives, Kansas Historical Society): Linda Brown's family; Gideon's handwritten petition (National Archives); Mary Beth and John Tinker with armbands (permission checked); the Court building. Each with credit.
- People (illustrated) for T.L.O. (a minor, never shown) as a silhouette only; Brandi Levy only from a licensed photograph or not at all; composite justices labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the bench from the lectern (1, 16:9).
About 9 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the narrator, the composite justices' questions and hints; `knowing-guide` as the case reader and the reader of opinions, introduced each time as "from" the opinion. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each person card.
- how `argue`: "Build a claim, a precedent and a counterclaim for this side."
- event, whole, each justice's question.
- how `refine`: "Sharpen your claim and name its limit."
- how `rule`: "Rule, and write three sentences."
- event, whole, each real decision.
- how `interest`: "Mark where your own view pulled your ruling."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: case folders, the argument builder, question and refine steps, the ruling, the decision reveal, the panel.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Arguments | Build only one side | The ruling stays closed until both sides have a claim, precedent and counterclaim. |
| Refine | Resubmit the same claim | The refine step needs a named strength and limit. |
| Panel | Mark "no tilt" every time | The panel asks for one interest per party first. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Person card (whole), waits; `argue`.
2. Justice's question (whole); `refine`.
3. `rule`; real decision (whole).
4. `interest`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.12.9-12, D2.Civ.10.9-12 and D3.4.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Brown v. Board of Education, 347 U.S. 483 (May 17, 1954), 9 to 0 | National Archives, "Brown v. Board of Education" | U.S. Courts, "History: Brown v. Board of Education Re-enactment" | yes |
| Gideon v. Wainwright, 372 U.S. 335 (March 18, 1963), 9 to 0; his handwritten petition; acquittal on retrial | National Archives, Gideon's petition | U.S. Courts, "Facts and Case Summary: Gideon v. Wainwright" | yes |
| Tinker v. Des Moines, 393 U.S. 503 (February 24, 1969), 7 to 2 | U.S. Courts, "Facts and Case Summary: Tinker v. Des Moines" | Oyez, "Tinker v. Des Moines" | yes |
| New Jersey v. T.L.O., 469 U.S. 325 (January 15, 1985), reasonable suspicion | U.S. Courts, "New Jersey v. T.L.O." | Oyez, "New Jersey v. T.L.O." | yes |
| Mahanoy Area School District v. B.L., 594 U.S. 180 (June 23, 2021), 8 to 1 | Supreme Court of the United States, opinion 20-255 | U.S. Courts, "Mahanoy Area School District v. B.L." | yes |
| Plessy v. Ferguson (1896) and Harlan's dissent | Library of Congress, "Plessy v. Ferguson" | National Archives | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r22, 2026-11-09): five cases in date order from 1954 to 2021; every vote sums to 9; Mahanoy came 52 years after Tinker; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and panel; at 680x425 sheet.
2. Each case shows how the person used or challenged the law and what changed. (D2.Civ.12.9-12)
3. Both sides are argued and refined with a named strength and limit. (D3.4.9-12)
4. The whose-interest panel is filled and the student's tilt is marked. (D2.Civ.10.9-12)
5. The real vote and short majority and dissent passages show for every case.
6. No minor's face is generated; no oral-argument audio.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
