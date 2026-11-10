# Cold War Crisis Room

## One idea
On a table lie the reconnaissance photographs of Soviet missile sites in Cuba and a calendar open to October 16, 1962, and the student advises the White House day by day through the thirteen days of the Cuban Missile Crisis, choosing among the real options of each day (an air strike, an invasion, a naval blockade, quiet talks) after advisers argue their cases; after each choice a record card shows what was really chosen and why; then the student replays the same days from Moscow (U.S. missiles in Turkey, a nuclear gap, the Bay of Pigs as proof the U.S. would invade Cuba) and from Havana (the 1961 invasion, fear of another, Cuban sovereignty), including the night of October 27 when a Soviet submarine officer, Vasili Arkhipov, refused to approve firing a nuclear torpedo; at the end a three-column view shows one event from three capitals and the student writes what about 1962 made the crisis unique and how each side's past shaped what it could see, then and in how each country remembers it now, so a tenth grader learns how unique circumstances and the wider Cold War shaped events and how history shaped perspectives.

## Not like
- two-space-races (11, spec): the space race told by two sides. Here thirteen days decided by three.
- alliance-web (9, spec): a chain of causes in 1914. Here day-by-day choices in 1962.
- supreme-court-simulator (12, concept): a courtroom roleplay. Here a crisis room.
- claim-repair-shop (10, spec): explaining 1989. Here deciding 1962.

## Who and how
- Grade 10, Social Studies (World and U.S. History), module "The Cold War". Standards: D2.His.1.9-12 (evaluate how historical events and developments were shaped by unique circumstances of time and place as well as broader historical contexts), D2.His.5.9-12 (analyze how historical contexts shaped and continue to shape people's perspectives).
- Format: roleplay. Driver: one student alone, or the class in three delegations (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Three runs (Washington, Moscow, Havana) of about eight decision days each, record cards, the three-column view, the write-up. Extra: Three delegations (the class splits into Washington, Moscow and Havana, each team choosing for its capital on the same days). tool.json `modes: ["Crisis room", "Three delegations"]`, `minutes: "35-45"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.1.9-12 | Read each day's context, choose an option, and compare with the record card | the day's intelligence; the options with costs; the record card naming the circumstances that shaped the real choice | 2 |
| D2.His.5.9-12 | Replay from Moscow and Havana, then fill the three-column view and say how each country remembers the crisis now | the three runs; the three-column view; the memory cards | 3, 4 |

## Screens and modes
Header (kit): title "Cold War Crisis Room"; `Crisis room`, `Three delegations`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A dim conference room. On the table, the U-2 photographs of San Cristobal, Cuba, from October 14, 1962, with labels marking launch sites. A wall calendar at Tuesday, October 16. The welcome is queued (`welcomeAfter: true`): "These photos were taken over Cuba two days ago. The President has just seen them. He wants your advice. Tap the photographs." First hint: "Tap the photographs."

**Washington run (focus: the day and the options).** At 1366x768 the table and photographs fill the left with the day card and options right; at 680x425 the options are a sheet. Each day: new intelligence, two or three advisers' positions (in plain words, credited to real ExComm members from the meeting records), and three or four real options with what each risked.
- October 16 to 21: air strike, invasion, blockade or quiet talks. Record: the President chose a naval "quarantine," avoiding the word blockade, which is an act of war.
- October 22: the President's television address.
- October 24: the quarantine begins; Soviet ships stop short of the line.
- October 26: Khrushchev's first letter offers to remove the missiles if the U.S. promises not to invade Cuba.
- October 27, "Black Saturday": a second letter adds U.S. missiles in Turkey; a U-2 is shot down over Cuba and its pilot, Major Rudolf Anderson, is killed; the U.S. Navy drops practice depth charges to force Soviet submarines up.
- October 28: Khrushchev agrees to remove the missiles; in secret, the U.S. agrees to remove its Jupiter missiles from Turkey, which it did in April 1963.
- After each choice, the record card: what was chosen, what the advisers feared, and the circumstances that shaped it (the Bay of Pigs eighteen months earlier, the 1962 congressional elections, Berlin, the arsenals).

**Moscow run.** The same days through the Soviet leadership's eyes: why send missiles at all (U.S. Jupiters in Turkey and Italy; the U.S. had many more nuclear weapons able to reach the other side; protecting Cuba after the Bay of Pigs); what Khrushchev could and couldn't see of Washington's plans. The submarine B-59 on October 27: out of contact, hot, under depth charges; two officers favor firing a nuclear torpedo; Vasili Arkhipov, whose agreement was needed, refuses. The student reads the moment; there is no choice to fire.

**Havana run.** The same days in Cuba: the Bay of Pigs invasion (April 1961) and later U.S. plots against Castro; fear of a new invasion; Castro's October 26 letter urging Khrushchev to strike first if the U.S. invaded; Cuba's anger at a deal made without it. The student chooses among Cuba's real options (mobilize, demand guarantees, refuse inspections) and sees the record.

**The three-column view (the aha).** One event (October 27) across Washington, Moscow and Havana: what each knew, feared and chose. Memory cards: in the U.S. it is the "Cuban Missile Crisis," in Russia the "Caribbean Crisis," in Cuba the "October Crisis," each name pointing to a different center. The write-up: "What made 1962 unique was ___. Each side's past shaped what it could see: Washington ___, Moscow ___, Havana ___." Narrator: "Each capital was looking at the same days. None of them saw the same crisis."

**The end.** The three runs, the view and the write-up. `Print` prints them.

**Three delegations (extra).** The class splits into three teams that choose for their capital on the same days; the board compares choices with the record.

## Content
- Three runs with about eight days each, intelligence cards, advisers' positions from meeting records, real options with risks, record cards, the B-59 moment, the three-column view, memory cards, the write-up.
- All events, dates, people, positions and figures are real and sourced; quotes are under 15 words; choices that differ from the record play forward a short "what might have followed" labeled as a historians' argument.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each day waits for a choice; the record card follows every choice.
- The Moscow and Havana runs open after the Washington run.
- Keyboard: Tab to the photographs, the day card, options, record cards and the view; Enter to choose.
- With Motion off the calendar turns without flipping.

## Look
- Accent `--brand` #22364d night navy (header, the day card, the view); gold #f4c542 (the option in hand, the day marker); paper #f1f3f6; ink #0b1421; muted #50565f.
- Contrast (WCAG 2.1, computed): white on brand 12.33:1; brand on paper 11.09:1; ink on paper 16.63:1; muted on paper 6.66:1; ink on gold 11.36:1.
- Never color alone: each capital carries its name and a flag; options carry words.
- Different from this batch (archive gray, podcast plum, campaign green, orbit indigo).

## Art
- Public domain (John F. Kennedy Presidential Library, National Archives, ids checked at build): the U-2 photographs of October 14, 1962; low-level reconnaissance photographs; ExComm meeting photographs by Cecil Stoughton; the President's October 22 address. Each with credit.
- Photographs of Khrushchev and Castro from public domain U.S. government sources where available, checked at build.
- Local FLUX (`scripts/localart.py`): the Kremlin room at night (1, 16:9); a Havana street with anti-aircraft guns (1, 16:9); a submarine interior (1, 16:9).
About 10 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the intelligence briefer for each day; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.run + ':' + state.day + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each day's intelligence.
- event, whole, each adviser's position.
- how `choose`: "Pick one option for today."
- event, whole, each record card.
- event, whole, the B-59 moment.
- how `view`: "Fill the three columns for October 27."
- how `write`: "Write what made 1962 unique."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the day stepper, options and record cards, three runs, the three-column view, the write-up.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Days | Click through without reading | Each record card asks one question about the circumstance that shaped the real choice before the next day. |
| View | Copy one capital's column into all three | Each column checks against what that capital knew. |
| Write-up | Name only the arsenals | It must name one circumstance per capital. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Intelligence (whole), waits; advisers (whole); `choose`; record card (whole).
2. Moscow run, then Havana run; the B-59 moment (whole).
3. `view`.
4. `write`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.9-12 and D2.His.5.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The U-2 photographs (October 14), the briefing (October 16), the quarantine and the address (October 22, 24) | John F. Kennedy Presidential Library, "The Cuban Missile Crisis" | U.S. Department of State, Office of the Historian, "The Cuban Missile Crisis" | yes |
| Khrushchev's two letters (October 26, 27) and the agreement of October 28 | Office of the Historian, Foreign Relations of the United States, 1961-63, vol. VI | National Security Archive (George Washington University), "The Cuban Missile Crisis, 1962" | yes |
| The secret Jupiter deal; the missiles left Turkey in April 1963 | National Security Archive | Fursenko and Naftali, "One Hell of a Gamble" (Norton, 1997) | yes |
| Major Rudolf Anderson killed October 27 | National Museum of the U.S. Air Force | Dobbs, "One Minute to Midnight" (Knopf, 2008) | yes |
| B-59 and Vasili Arkhipov's refusal | National Security Archive, Briefing Book on Soviet submarines (Savranskaya, 2002) | Dobbs (2008) | yes |
| Castro's October 26 letter urging a first strike if invaded | Wilson Center Digital Archive | National Security Archive | yes |
| The U.S. held a large lead in weapons able to reach the other side | Office of the Historian | Fursenko and Naftali (1997) | yes |
| The crisis's names in Russia ("Caribbean") and Cuba ("October") | Wilson Center, "The Caribbean Crisis" | Blight, Allyn and Welch, "Cuba on the Brink" (Pantheon, 1993) | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r19, 2026-11-09): October 16 to 28 is thirteen days counting both; the Bay of Pigs (April 1961) came 18 months before; days in order; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and day card; at 680x425 sheet.
2. Each Washington day gives real options and a record card naming its circumstances. (D2.His.1.9-12)
3. The Moscow and Havana runs replay the days from those capitals. (D2.His.5.9-12)
4. The three-column view and memory cards compare perspectives then and now. (D2.His.5.9-12)
5. The B-59 moment is read, never chosen.
6. Three delegations compares team choices with the record.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flipping; no network requests.

## Open questions
None.
