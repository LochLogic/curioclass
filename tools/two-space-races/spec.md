# Two Space Races

## One idea
Two timelines run side by side from Sputnik's beep on October 4, 1957 to Apollo 11 on July 20, 1969, one written by Soviet sources and one by American sources at the time; the student places each milestone (Sputnik, Explorer 1, Gagarin, Shepard, Tereshkova, the first spacewalk, Apollo 1, Soyuz 1, Apollo 11) on both, reads each side's period account, and flags what each stressed or hid (Gagarin's parachute landing kept quiet, the Chief Designer Sergei Korolev's name kept secret until his death in 1966, rocket disasters on both sides, the Soviet moon program denied until 1989, and the Black women mathematicians and the women pilots left out of American accounts for decades); a context strip links each milestone to Cold War politics of its moment (the "missile gap," Kennedy's 1961 challenge, the budget pressures of Vietnam); at the end a third timeline, "historians later," shows how opened archives and new research filled the gaps, and the student writes how each side's writers shaped the story and what about those years made space a battlefield, so an eleventh grader learns how unique times shaped events and how the perspectives of those writing history shaped what they produced.

## Not like
- cold-war-crisis-room (10, spec): decisions in 1962. Here two histories of twelve years.
- decades-explorer (11, concept): America since 1980. Here 1957 to 1969.
- colonial-newsroom (8, spec): two slanted papers made by the student. Here two real national accounts.
- historians-disagree (7, spec): two historians. Here two governments' writers, then historians.

## Who and how
- Grade 11, Social Studies (U.S. and World History), module "Cold War America". Standards: D2.His.1.9-12 (evaluate how historical events and developments were shaped by unique circumstances of time and place as well as broader historical contexts), D2.His.6.9-12 (analyze the ways in which the perspectives of those writing history shaped the history that they produced).
- Format: timeline (changed from the card's "race", because D2.His.6.9-12 needs comparing how each side wrote the events, not beating a clock). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Twelve milestones, two period accounts each, flags, the context strip, the historians-later timeline, the write-up. Extra: Review round (a quick milestone-order quiz for review, side mode only). tool.json `modes: ["Two timelines", "Review round"]`, `minutes: "30-40"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.6.9-12 | Read both sides' accounts of each milestone and flag what each stresses, hides or leaves out | the two timelines with accounts; the flags | 2 |
| D2.His.6.9-12 (later) | Open the historians-later timeline and match each gap to the record that filled it | the third timeline with dated revelations | 3 |
| D2.His.1.9-12 | Link each milestone to its Cold War moment on the context strip, then write the write-up | the context strip; the write-up | 4 |

## Screens and modes
Header (kit): title "Two Space Races"; `Two timelines`, `Review round`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two timelines side by side, labeled Moscow and Washington, at October 4, 1957, with Sputnik's radio beep (a recording from NASA, public domain). The welcome is queued (`welcomeAfter: true`): "Both countries told the story of the space race as it happened. They didn't tell the same story. Tap Sputnik." First hint: "Tap Sputnik."

**Milestones (focus: the two accounts).** At 1366x768 the two timelines run left and right with the account panel between; at 680x425 the timelines are tabs. Twelve milestones, each with a short period account from each side (under 15 words quoted, credited):
1. Sputnik (October 4, 1957).
2. Sputnik 2 with the dog Laika (November 3, 1957); the Soviet press said she lived for days; she died within hours, revealed in 2002.
3. Vanguard explodes on the launch pad (December 6, 1957), on live television; American papers call it "Flopnik."
4. Explorer 1 (January 31, 1958); NASA founded (October 1958).
5. The Nedelin disaster (October 24, 1960): a rocket explodes at Baikonur, killing dozens; denied until 1989.
6. Gagarin (April 12, 1961): the first human in orbit; he ejected and landed by parachute, which Soviet accounts hid because record rules required landing in the craft.
7. Shepard (May 5, 1961), and Kennedy's challenge to Congress (May 25, 1961).
8. Tereshkova (June 16, 1963), the first woman in space; the U.S. barred women from astronaut training; the women pilots tested privately (later called the "Mercury 13") left out.
9. Leonov's spacewalk (March 18, 1965), with a ballooning suit and a hard landing, kept quiet at the time.
10. Korolev dies (January 14, 1966), named publicly only after his death.
11. Apollo 1 fire (January 27, 1967) and Soyuz 1 (April 24, 1967), losses on both sides.
12. Apollo 11 (July 20, 1969); Soviet moon rocket failures (1969 to 1972) and a moon program denied until 1989.
- Also on the American side: Katherine Johnson, Dorothy Vaughan and Mary Jackson at NASA Langley, whose work became widely known with the 2016 book "Hidden Figures"; Ed Dwight, the first Black astronaut candidate, not selected in 1963.
- For each account the student flags what it stresses (firsts, heroes, national pride), hides (failures, deaths, names) and leaves out (people).

**The historians-later timeline (D2.His.6.9-12).** A third timeline shows when each gap was filled and how: glasnost-era releases (late 1980s), Russian archives (1990s and 2000s), NASA oral histories, new research and books. The student matches each flag to the record that filled it.

**The context strip (D2.His.1.9-12).** Each milestone links to its moment: the shock of Sputnik and the 1958 National Defense Education Act; the "missile gap" in the 1960 election; the Bay of Pigs a week after Gagarin; Kennedy's 1961 challenge; NASA's budget peaking in the mid-1960s while Vietnam costs rose.

**The write-up (the aha).** "Soviet writers shaped the story by ___. American writers shaped it by ___. What made these years a battlefield in space was ___." Narrator: "Every account was true in parts. Each side chose which parts."

**The end.** Both timelines with flags, the historians-later timeline and the write-up. `Print` prints them.

**Review round (extra).** A quick order-the-milestones quiz for review, separate from the main work.

## Content
- Twelve milestones, two period accounts each, flag tiles, the historians-later timeline with dated revelations, the context strip, the write-up.
- All events, dates, people and quotes are real and sourced; period Soviet press excerpts are short and credited.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Milestones open in order; any opened milestone can be reopened.
- The historians-later timeline opens after eight milestones are flagged.
- Keyboard: Tab to milestones, accounts, flags, the strip and the third timeline; Enter to open and flag.
- With Motion off rockets don't launch on the timeline; markers appear in place.

## Look
- Accent `--brand` #3b3f8f orbit indigo (header, timelines, the strip); gold #f4c542 (the open milestone, a flag); paper #f2f2fb; ink #10122e; muted #555770.
- Contrast (WCAG 2.1, computed): white on brand 9.16:1; brand on paper 8.23:1; ink on paper 16.44:1; muted on paper 6.32:1; ink on gold 11.25:1.
- Never color alone: each timeline carries its city name and a label on every account; flags carry words.
- Different from this batch (night navy, archive gray, podcast plum, campaign green).

## Art
- Public domain NASA photographs (ids checked at build): Explorer 1's team, Shepard's launch, Apollo 1's crew, Apollo 11 on the moon, Katherine Johnson at Langley. Each with credit.
- Soviet-era photographs only where free to use, checked at build; otherwise local FLUX (`scripts/localart.py`) scenes without people: the Baikonur launch pad (1, 16:9), a Moscow newsstand in 1961 (1, 16:9).
- People art goes to Gemini with `people: true` only for figures without a free photograph (Korolev, Tereshkova, Leonov), each labeled "illustration" (3; cutout yes).
About 10 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator and hints; `bright-teacher` as the reader of period accounts from both sides, introduced each time as "from" the newspaper or agency. `Curio.voice` with `scope: () => state.mode + ':' + state.milestone + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each milestone's plain note.
- event, whole, each period account.
- how `flag`: "Flag what this account stresses, hides or leaves out."
- how `later`: "Match each flag to the record that filled the gap."
- how `strip`: "Link this milestone to its moment in the Cold War."
- how `write`: "Write how each side shaped the story."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: two linked timelines, accounts, flags, the historians-later timeline, the context strip, the write-up, the review quiz.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Flags | Flag "hides" everywhere | Each flag checks against the record and needs a named detail. |
| Later timeline | Match at random | Each match checks the date and record. |
| Write-up | Name only one side | It needs a line for each side and one circumstance of the times. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Plain note (whole), waits; both accounts (whole).
2. `flag`, for each milestone; `strip`.
3. `later`.
4. `write`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.9-12 and D2.His.6.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Sputnik, Sputnik 2, Explorer 1, Vanguard's failure, NASA's founding | NASA History Office, "Sputnik and the Origins of the Space Age" | Smithsonian National Air and Space Museum | yes |
| Gagarin's parachute landing hidden; Korolev unnamed until his death | Siddiqi, "Challenge to Apollo" (NASA SP-2000-4408, 2000) | Smithsonian National Air and Space Museum, "Gagarin" | yes |
| The Nedelin disaster (1960), denied until 1989 | Siddiqi (2000) | Russian Space Web / Zak, "Nedelin disaster" | yes |
| Laika died within hours, revealed in 2002 | Malashenkov, World Space Congress paper (2002) | NASA History Office | yes |
| Leonov's spacewalk problems; Soyuz 1; the N1 failures and the denied moon program | Siddiqi (2000) | Smithsonian National Air and Space Museum | yes |
| Katherine Johnson, Dorothy Vaughan and Mary Jackson at Langley | NASA, "Katherine Johnson biography" | Shetterly, "Hidden Figures" (Morrow, 2016) | yes |
| The women pilots tested in 1960-61 ("Mercury 13"); Ed Dwight not selected | Smithsonian National Air and Space Museum | NASA History Office | yes |
| Kennedy's challenge (May 25, 1961); NASA budget peak in the mid-1960s | John F. Kennedy Presidential Library | NASA, budget history tables | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r19, 2026-11-09): milestones in date order from October 4, 1957 to July 20, 1969; Gagarin flew 23 days before Shepard; Korolev's name was revealed about 8 years after Sputnik; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 two timelines and accounts; at 680x425 tabs.
2. Each milestone's two accounts are flagged for what they stress, hide or leave out. (D2.His.6.9-12)
3. The historians-later timeline matches gaps to records. (D2.His.6.9-12)
4. The context strip and write-up name the circumstances of the times. (D2.His.1.9-12)
5. Format is timeline; the race quiz is only in Review round.
6. Illustrations of real people without free photos are labeled.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no launches; no network requests.

## Open questions
- The idea card proposes changing the format from race to timeline (default used: timeline, with the race quiz kept as the side mode Review round).
