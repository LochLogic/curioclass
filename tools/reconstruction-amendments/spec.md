# Reconstruction Amendments

## One idea
Three amendment cards lie on a desk above a timeline from 1865 to 1965: the 13th (ending slavery), the 14th (citizenship and equal protection) and the 15th (the vote regardless of race); the child opens each, reads its words in plain English beside short phrases of the real text, and steps through three panels (what it promised, how it was carried out, how it was undermined), tagging who acted at each step and at what level (Congress, presidents, the courts, states, and Black citizens themselves, who voted, organized and held office, like Senator Hiram Revels); then a chart shows Black voter registration in Louisiana falling from about 130,000 in 1896 to about 1,300 in 1904 after a new state constitution, and a change and continuity board ends with Brown v. Board of Education and the Voting Rights Act using the same amendments a century later, so an eighth grader learns the powers and limits of each branch and level, how amendments work as policy with purposes, carrying-out and consequences, how people changed society then and later, and what changed and what lasted.

## Not like
- voices-of-freedom (8, concept): voices before the war. Here the amendments after it.
- premise-inspector (11, spec): reasoning inside founding documents. Here what happened to three amendments.
- rights-match (5, spec): matching the Bill of Rights. Here amendments as promises kept and broken.
- constitutional-convention (8, spec): writing the Constitution. Here changing it.

## Who and how
- Grade 8, Social Studies (Civics and History), module "Reconstruction". Standards: D2.Civ.4.6-8 (explain the powers and limits of the three branches of government, public officials, and bureaucracies at different levels in the United States and in other countries), D2.Civ.14.6-8 (compare historical and contemporary means of changing societies, and promoting the common good), D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.Civ.13.6-8 (analyze the purposes, implementation, and consequences of public policies in multiple settings).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three amendments with three panels each, the registration chart, the board. Extra: Pick the state (the teacher switches the chart to Mississippi, where Black registration was about 7 percent in 1964 and about 60 percent by 1967). tool.json `modes: ["Louisiana chart", "Mississippi chart"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.13.6-8 | Step through each amendment's three panels: purpose, carried out, undermined | the panel strip with the policy's purpose and consequences | 2 |
| D2.Civ.4.6-8 | Tag each event with who acted (Congress, president, courts, states, citizens) and the level | branch and level tags on the timeline; a tally of who acted | 3 |
| D2.His.2.6-8 | Read the chart, then sort events into Changed or Continued on the 1865 to 1965 board | the chart; the board | 4 |
| D2.Civ.14.6-8 | Compare how people sought change in the 1860s and 1870s (voting, office, petitions, conventions) with the 1950s and 1960s (lawsuits, marches, voter drives) | the two-column means-of-change card | 5 |

## Screens and modes
Header (kit): title "Reconstruction Amendments"; `Louisiana chart`, `Mississippi chart`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A desk with three cards stamped XIII, XIV and XV, and a long timeline beneath from 1865 to 1965 with empty slots. The welcome is queued (`welcomeAfter: true`): "After the Civil War, three amendments changed the Constitution. Each made a promise. Open one to see what happened to it." First hint: "Tap the XIII card."

**Each amendment (focus: the panels, D2.Civ.13.6-8).** At 1366x768 the card opens with three panels across and the timeline below; at 680x425 panels are a carousel.
- 13th (ratified December 1865): promised the end of slavery, except as punishment for a crime. Carried out: four million people freed; the Freedmen's Bureau (1865) set up schools and helped with labor contracts. Undermined: Black Codes in Southern states (1865 to 1866) limited Black people's work and movement; convict leasing used the amendment's exception.
- 14th (ratified 1868): citizenship for all born here; equal protection of the laws; due process. Carried out: the Civil Rights Act of 1866, Black men elected to state and national office (Hiram Revels to the U.S. Senate in 1870), about 2,000 Black officeholders across the South during Reconstruction. Undermined: United States v. Cruikshank (1876) limited federal protection after the Colfax massacre; Plessy v. Ferguson (1896) allowed "separate but equal."
- 15th (ratified 1870): the vote could not be denied because of race. Carried out: Enforcement Acts (1870 to 1871) against the Ku Klux Klan; Black men voted in large numbers. Undermined: violence and fraud; the end of federal enforcement after 1877; poll taxes, literacy tests and new state constitutions (Mississippi 1890, Louisiana 1898).
- Each panel names events plainly; violence is named without images.

**Who acted (D2.Civ.4.6-8).** Each event gets a tag from tiles: Congress (passed and enforced), President (Grant sent troops; Hayes withdrew them in 1877), Courts (narrowed the amendments), States (Black Codes, new constitutions), Citizens (voters, officeholders, conventions, newspapers). A tally shows how often each acted to carry out or to undermine.

**The chart (the aha).** Louisiana's registered Black voters by year: about 130,000 in 1896; about 5,300 in 1900; about 1,300 in 1904, after the 1898 constitution added a poll tax, a literacy or property test and a "grandfather clause." Narrator: "The 15th Amendment stayed in the Constitution the whole time. What changed was whether anyone enforced it."

**The board (D2.His.2.6-8).** Events sorted from 1865 to 1965: Changed (slavery ended; citizenship for Black Americans; Black officeholders, then their removal; Brown v. Board of Education in 1954 used the 14th; the Voting Rights Act of 1965 enforced the 15th) or Continued (the amendments' words; resistance by some states; Black citizens organizing throughout).

**Means of change (D2.Civ.14.6-8).** A two-column card: then (voting, holding office, state conventions, petitions, newspapers, schools) and later (lawsuits like Brown, marches, voter drives, the Voting Rights Act). The child picks one way that carried over and one that was new.

**The end.** The three amendment strips, the tally, the chart, the board and the means card. `Print` prints them.

**Mississippi chart (extra).** Black registration about 7 percent in 1964 and about 60 percent in 1967, after the Voting Rights Act.

## Content
- Three amendments with plain words, short real phrases and three panels each, about 25 timeline events with who-acted keys, two state charts, the board, the means card.
- Every event, figure and quote is real and sourced; figures are rounded and labeled "about".
- Racial violence and Jim Crow are told plainly with care, without images of violence.
- Founding-docs data (amendment, section, plain words, real text, principle) sits in one marked block for the family engine.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Amendments open in any order; each panel must be read before its tags.
- The chart reads each point aloud on focus.
- Keyboard: Tab to cards, panels, tags, chart points and board cards; Enter to open and place.
- With Motion off panels change without sliding.

## Look
- Accent `--brand` #3a4470 amendment indigo (header, amendment cards, the timeline); gold #f4c542 (the open card, a placed tag); paper #f3f4f8; ink #10142a; muted #545766.
- Contrast (WCAG 2.1, computed): white on brand 9.37:1; brand on paper 8.53:1; ink on paper 16.54:1; muted on paper 6.52:1; ink on gold 11.17:1.
- Never color alone: carried-out and undermined panels carry headings and icons; chart points carry values.
- Different from this batch (committee green, mill brick, colonial leather, transit teal).

## Art
- Public domain (Library of Congress and National Archives, ids checked at build): the 13th Amendment as passed; "The First Vote" (Harper's Weekly, 1867); Hiram Revels's portrait; the first Black members of Congress print (Currier and Ives, 1872); a Freedmen's Bureau school photograph; the Brown v. Board decision page; the Voting Rights Act signing photograph (1965). Each with credit.
- Drawn in code: the panels, timeline, tags, tally, chart, board.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `calm-professor` as the panel reader. `Curio.voice` with `scope: () => state.mode + ':' + state.amendment + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each amendment's plain words.
- event, whole, each panel.
- how `tag`: "Tag who acted and at what level."
- event, whole, the chart line.
- how `board`: "Drag each event to Changed or Continued."
- how `means`: "Pick one way that carried over and one that was new."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
founding-docs (no engine on main yet; `kit/founding-docs.js` is planned for premise-inspector and founding-words-explorer). This tool keeps its amendment data (number, section, plain words, short real text, principle) as plain data in one marked block, `/* FOUNDING-DOCS DATA: begin */ ... /* end */`, so the family engine can take it later. Tool-only code: the panels, timeline tags and tally, the charts, the board, the means card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everything Congress | Each tag checks; Plessy tagged Congress plays "Who decided Plessy?" |
| Board | Put everything in Changed | Each event checks; "the amendments' words" in Changed plays a reason line. |
| Means | Pick the same for both | The card needs one carried-over and one new way. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Plain words (whole), waits; panels (whole), each waits.
2. `tag`.
3. Chart line (whole); `board`.
4. `means`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.4.6-8, D2.Civ.14.6-8, D2.His.2.6-8 and D2.Civ.13.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Text and ratification of the 13th (1865), 14th (1868) and 15th (1870) Amendments | National Archives, Constitution amendments transcripts | National Constitution Center, Interactive Constitution | yes |
| Freedmen's Bureau (1865); Black Codes (1865 to 1866) | National Archives, "Freedmen's Bureau" | Foner, "Reconstruction: America's Unfinished Revolution" (Harper and Row, 1988) | yes |
| Hiram Revels to the Senate in 1870; about 2,000 Black officeholders | U.S. Senate, "Hiram Revels" | Foner, "Freedom's Lawmakers" (Oxford, 1993) | yes |
| Enforcement Acts (1870 to 1871); end of federal enforcement after 1877 | Britannica, "Enforcement Acts" | Foner (1988) | yes |
| United States v. Cruikshank (1876) and Plessy v. Ferguson (1896) | Oyez, case pages | National Archives, "Plessy v. Ferguson" | yes |
| Louisiana Black registered voters about 130,000 (1896), 5,300 (1900), 1,300 (1904) | Kousser, "The Shaping of Southern Politics" (Yale, 1974) | Woodward, "The Strange Career of Jim Crow" (Oxford, 1955 and later eds.) | yes |
| Mississippi Black registration about 7 percent (1964) and about 60 percent (1967) | U.S. Commission on Civil Rights, "Political Participation" (1968) | U.S. Department of Justice, "Introduction to Federal Voting Rights Laws" | yes |
| Brown v. Board (1954) used the 14th; the Voting Rights Act (1965) enforced the 15th | National Archives, "Brown v. Board of Education" | National Archives, "Voting Rights Act (1965)" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: racial violence (the Colfax massacre, the Klan) and Jim Crow laws are named plainly with sources and no images of violence; Black Americans are shown acting throughout, not only as victims. A fresh-agent read of the undermined panels is needed before build.

Checks run (Python, scratchpad r15, 2026-11-09): ratification years in order (1865, 1868, 1870); Louisiana figures fall each step (130,000 to 1,300 is a 99 percent drop); Mississippi rises from 7 to 60 percent; 1965 minus 1865 is 100 years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 panels and timeline; at 680x425 carousel.
2. Each amendment's three panels open with purpose, carrying-out and undermining. (D2.Civ.13.6-8)
3. Events carry who-acted tags and the tally fills. (D2.Civ.4.6-8)
4. The chart and the board check. (D2.His.2.6-8)
5. The means card compares then and later. (D2.Civ.14.6-8)
6. Mississippi chart loads.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
- Sensitivity flag: racial violence and Jim Crow (default used: named plainly with sources, no images of violence, Black Americans shown acting throughout, fresh-agent read before build).
