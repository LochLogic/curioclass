# Case Conference

## One idea
The student joins a clinic team's weekly case conference with four made-up case summaries (a college student with panic attacks, a retired teacher with depression, a cook with obsessive-compulsive symptoms, a young adult with attention problems at work); for each the team looks through three lenses in turn, biological (genes, brain, sleep, medicine), psychological (thoughts, learning, coping) and social (family, culture, money, stress), the student places each fact from the summary under its lens and sees how the three together explain more than any one; then the team checks the case against how disorders are classified (DSM-5-TR and ICD-11 criteria in plain words, and why a label needs distress or impairment) and compares treatments by their research evidence (cognitive behavioral therapy, exposure and response prevention, medication, combined care) on a strength-of-evidence chart; a stress and health round traces how a hard month moves through the body (the stress response, sleep, immune function, the evidence on colds and wound healing); support resources (988 by call or text, a trusted adult, the school counselor) stay on every screen; at the end the student writes the team's summary for one case, so a twelfth grader learns perspectives on psychological disorders, how they are classified, how treatments are compared, and how stress affects health.

## Not like
- mind-map (9-12, live): stigma and helping a friend. Here disorders, classification and treatment evidence.
- go-along (12, spec): social pressure. Here mental health.
- trait-lab (12, spec): typical variation. Here disorders.
- brain-explorer (12, spec): brain structures. Here three lenses on a whole person.

## Who and how
- Grade 12, Psychology, module "Psychological Disorders and Treatment". Standards: APA.Mental and Physical Health (APA National Standards for High School Psychology Curricula: perspectives on abnormal behavior, classification of disorders, treatment approaches and their evidence, and stress and health).
- Format: roleplay. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Four made-up cases, three lenses each, a classification check, a treatment evidence chart, a stress and health round, the team summary; a support bar on every screen. Extra: none. tool.json `modes: ["Case conference"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Mental and Physical Health (perspectives) | Sort each case's facts under the biological, psychological and social lenses | the three-lens board | 2 |
| APA.Mental and Physical Health (classification) | Check the case against plain-words criteria, including distress or impairment | the criteria card | 3 |
| APA.Mental and Physical Health (treatment) | Compare treatments on the evidence chart and pick a plan with reasons | the evidence chart | 4 |
| APA.Mental and Physical Health (stress and health) | Trace a hard month through the body | the stress pathway | 5 |

## Screens and modes
Header (kit): title "Case Conference"; `Case conference`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more. A support bar under the header on every screen: "If you or someone you know is struggling: call or text 988, or talk to a trusted adult or your school counselor."

**On load and first tap.** A clinic meeting room with a round table and four illustrated team members (a psychiatrist, a psychologist, a social worker, a nurse, all made up). A folder: "Case 1: Jordan, 20, college student (made up)". The welcome is queued (`welcomeAfter: true`): "You're on the team today. Every case is made up, but the science is real. Look at each person through three lenses before anyone names anything. Tap the folder." First hint: "Tap the folder to open the case."

**Three lenses (focus: the board).** At 1366x768 the case fills the left with the lens board right; at 680x425 the board is a sheet. Each case summary has about nine facts; the student drags each under Biological, Psychological or Social. Each team member then speaks for their lens. The board shows how the lenses connect (poor sleep worsens worry; worry worsens sleep). The biopsychosocial model is named (Engel, 1977).

**Classification.** A criteria card in plain words for the case's likely category, with the rule that symptoms must cause real distress or trouble in daily life. The team asks: "What else could explain this?" (a medical condition, a substance, a hard season of life). DSM-5-TR (2022) and ICD-11 are shown as the two systems clinicians use, and a card explains why labels can help (access to care, research) and harm (stigma).

**Treatment evidence.** A chart rates each treatment's evidence for the case: strong evidence for cognitive behavioral therapy for panic disorder; for depression, therapy and antidepressants each help and combined care often helps most; exposure and response prevention for obsessive-compulsive disorder; stimulant medication and skills coaching for adult ADHD. The student picks a plan and gives one reason from the chart.

**Stress and health.** A hard month (exams, a sick parent, a lost job) moves along a pathway: the stress response (Selye's general adaptation syndrome), sleep loss, immune changes; evidence cards: people under more stress caught colds more often after exposure (Cohen and colleagues, 1991); wounds healed more slowly during exam stress (Marucha and colleagues, 1998). Coping that helps: sleep, exercise, social support.

**The team summary (the aha).** "For ___, the biological lens shows ___, the psychological lens shows ___, the social lens shows ___. The team's plan is ___ because the evidence ___." Narrator: "No one lens sees a whole person. The team does."

**The end.** The four boards, the plans and the summary. `Print` prints them, with the support bar.

## Content
- Four made-up cases with about nine facts each (no self-harm, no suicide attempt, no eating disorder, no case under 18), four made-up team members, plain-words criteria, the evidence chart, the stress pathway, the summary template, the support bar.
- No self-screening quiz; the tool never asks about the student's own health. A teacher note: what the tool covers, what it leaves out, and how to point a student to help.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each case opens after the previous one's plan; any case can be reopened.
- The support bar is a real link list that works offline as text.
- Keyboard: Tab to the folder, facts, lenses, the chart and the summary; Enter places a fact.
- With Motion off facts jump to their lens.

## Look
- Accent `--brand` #1d5c63 clinic teal (header, the folder, lens labels); gold #f4c542 (the fact in hand, the chosen plan); paper #eef6f6; ink #072022; muted #4e5a5b.
- Contrast (WCAG 2.1, computed): white on brand 7.60:1; brand on paper 6.93:1; ink on paper 15.46:1; muted on paper 6.52:1; ink on gold 10.42:1.
- Never color alone: lenses carry names and icons (a cell, a thought bubble, a house); evidence bars carry words (strong, moderate, limited).
- Different from this batch (harvest ochre, clock blue, line crimson, map slate).

## Art
- People (illustrated) for the four team members and the four made-up clients, labeled "illustration", calm and ordinary, no distress poses (Gemini, `people: true`, 8; cutout yes).
- Local FLUX (`scripts/localart.py`): the clinic meeting room (1, 16:9).
- Drawn in code: the lens board, the evidence chart, the stress pathway.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the team lead and the evidence; `warm-teacher` as the guide, the support bar and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag each fact under a lens."
- event, whole, each team member's lens.
- how `criteria`: "Check the case against the criteria."
- how `plan`: "Pick a plan and say why."
- event, whole, the stress pathway.
- how `summary`: "Write the team's summary."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: case folders, the lens board, criteria cards, the evidence chart, the stress pathway, the support bar. Case text sits in a marked block `/* CASE-CONFERENCE DATA: begin */ ... /* end */` for a reviewer to read.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Lenses | Put every fact under Biological | Each fact checks against its lens, with the team member's reason. |
| Plan | Pick medication every time | The plan needs a reason from the chart, which differs by case. |
| Summary | Name a diagnosis only | It needs all three lenses and an evidence reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`.
2. Team lenses (whole), waits; `criteria`; `plan`.
3. Stress pathway (whole).
4. `summary`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Mental and Physical Health wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt | yes |
| The biopsychosocial model | Engel, Science (1977) | APA Dictionary of Psychology | yes |
| Distress or impairment required; DSM-5-TR and ICD-11 | American Psychiatric Association, "DSM-5-TR" (2022) | World Health Organization, "ICD-11" (in effect 2022) | yes |
| CBT for panic disorder; ERP for OCD | National Institute for Health and Care Excellence, guidelines CG113 and CG31 | APA Division 12, "Research-Supported Psychological Treatments" | yes |
| Therapy and antidepressants for depression; combined care | Cuijpers and colleagues, World Psychiatry (2014) | National Institute of Mental Health, "Depression" | yes |
| Adult ADHD: stimulants and skills coaching | National Institute of Mental Health, "ADHD" | NICE guideline NG87 (2018) | yes |
| Selye's general adaptation syndrome | Selye, Nature (1936) | APA Dictionary of Psychology | yes |
| Stress and colds; stress and wound healing | Cohen, Tyrrell and Smith, New England Journal of Medicine (1991) | Marucha, Kiecolt-Glaser and Favagehi, Psychosomatic Medicine (1998) | yes |
| 988 by call or text | SAMHSA, "988 Suicide and Crisis Lifeline" | Federal Communications Commission, "988" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: mental health content for teens; made-up adult cases only, no self-harm, suicide or eating disorder cases, no self-screening, the support bar on every screen and in print, a teacher note; a fresh agent reads the cases and cards before build.

Checks run (Python, scratchpad r24, 2026-11-09): four cases with three lenses each is 12 lens panels; DSM-5-TR (2022) came 9 years after DSM-5 (2013); the 988 line began July 16, 2022; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 case and board; at 680x425 sheet.
2. Each case's facts are sorted under three lenses with the team's reasons. (APA.Mental and Physical Health)
3. The criteria card includes distress or impairment and other explanations. (APA.Mental and Physical Health)
4. A plan is picked with a reason from the evidence chart. (APA.Mental and Physical Health)
5. The stress pathway shows two evidence cards and coping that helps. (APA.Mental and Physical Health)
6. The support bar shows on every screen and in print; no self-screening; all cases made up and adult.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
- Sensitivity flag: mental health disorders and treatment for teens (default used: four made-up adult cases with no self-harm, suicide or eating disorder content, no self-screening, 988 and trusted-adult support on every screen, a teacher note, fresh-agent read before build).
- The idea card flags overlap risk with mind-map (default used: mind-map keeps stigma and helping a friend; this tool teaches perspectives, classification, treatment evidence and stress and health, and links to mind-map).
