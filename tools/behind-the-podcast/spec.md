# Behind the Podcast

## One idea
The student plays "Episode 12: Who caused the Great Depression?", an original ten-minute history podcast written for this tool with a full transcript and show notes; as it plays, claims light up in the transcript, and for each one the student opens the source it cites (a 1932 newspaper, a 1938 Federal Writers' Project interview, a Federal Reserve chart, a memoir written decades later, a famous quote) and marks whether the source supports the claim, partly supports it, or doesn't fit, naming why (wrong date, wrong place, a quote out of context or misattributed, a source that couldn't know); faults are planted on purpose and labeled so in the teacher key; then the episode's central argument sits beside a short historian's article on the same question, and the student checks both against the evidence and marks which claims hold; at the end the student writes a corrections note for the episode (what it got right, what it overstated, and which source would fix it), so an eleventh grader learns how secondary works are built from sources, whether a work's sources fit its claims, and how to critique a central argument across media for accuracy.

## Not like
- missing-voices-archive (11, concept): gaps in an archive. Here a finished work and its citations.
- claim-repair-shop (10, spec): repairing short explanations. Here auditing a whole episode.
- stock-market-1929 (11, spec): living through the crash. Here checking a story told about it.
- historians-disagree (7, spec): two historians compared. Here a podcast against a historian.

## Who and how
- Grade 11, Social Studies (U.S. History), module "Behind the Documentary". Standards: D2.His.9.9-12 (analyze the relationship between historical sources and the secondary interpretations made from them), D2.His.13.9-12 (critique the appropriateness of the historical sources used in a secondary interpretation), D2.His.17.9-12 (critique the central arguments in secondary works of history on related topics in multiple media in terms of their historical accuracy).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- One ten-minute episode with twelve cited claims, twelve sources, the argument step, the corrections note. Extra: Correction segment (the student scripts a 60-second correction to record or read aloud; printed with the transcript lines it fixes). tool.json `modes: ["Episode", "Correction segment"]`, `minutes: "35-45"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.9.9-12 | Open each lit claim's cited source and link the claim to what the source actually says | the transcript with lit claims; the source beside it | 2 |
| D2.His.13.9-12 | Mark each source supports, partly supports or doesn't fit, and name the fault | the support rating; the fault tag | 3 |
| D2.His.17.9-12 | Check the episode's argument and the historian's article against the evidence, then write the corrections note | the argument step side by side; the corrections note | 4, 5 |

## Screens and modes
Header (kit): title "Behind the Podcast"; `Episode`, `Correction segment`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A podcast player: a waveform, a play button, a transcript panel and a show-notes panel listing twelve sources. The episode title: "Episode 12: Who caused the Great Depression?" The welcome is queued (`welcomeAfter: true`): "This episode sounds sure of itself. Is it right? Press play, and when a claim lights up, check its source." First hint: "Press Play."

**The episode (focus: the transcript and the source).** At 1366x768 the player and transcript fill the left with the source panel right; at 680x425 the source is a sheet. The episode is an original script in the voice of a made-up host (labeled "an original podcast written for Curio Class"). The audio pauses when a claim lights up and the student opens its source. Twelve claims, about half sound and half with a planted fault:
- Sound: the crash of October 1929 (Black Thursday, October 24; Black Tuesday, October 29), cited to a 1929 newspaper; about 9,000 banks failed from 1930 to 1933, cited to FDIC history; unemployment near 25 percent in 1933, cited to Bureau of Labor Statistics history; the money supply fell by about a third from 1929 to 1933, cited to a Federal Reserve chart; the Smoot-Hawley Tariff (1930) and other countries' retaliation; the bank holiday of March 1933.
- Planted faults: a "prosperity is just around the corner" quote pinned on President Hoover as his exact words (a misattribution); a 1938 interview used as proof of what people felt in 1929 (a source written years later, about a different year); a Dust Bowl photograph from 1936 used for "the day after the crash" (wrong date and place); a claim that the crash alone caused the Depression, cited to a source that says the opposite; a memoir from the 1970s quoted as if it were a 1932 record; a chart cropped to hide the years before 1929.
- For each, the student marks supports, partly supports or doesn't fit, and tags the fault (wrong date, wrong place, out of context or misattributed, couldn't know, doesn't say that).

**The argument step (D2.His.17.9-12).** The episode's central argument ("the stock market crash caused the Great Depression") beside a short historian's article written for this tool, summarizing the main lines historians argue (bank failures and a shrinking money supply, the gold standard spreading the slump between countries, falling demand, policy mistakes), with its own citations to published work. The student checks both against the twelve sources and marks which claims hold.

**The corrections note (the aha).** "The episode got right ___. It overstated ___. The source that would fix it is ___, because ___." Narrator: "A confident voice isn't evidence. The sources are."

**The end.** The marked transcript, the ratings and the corrections note. `Print` prints them.

**Correction segment (extra).** The student scripts a 60-second correction to read aloud; it prints beside the lines it fixes.

## Content
- An original ten-minute script with full transcript and show notes; twelve real sources with credits; six planted faults, labeled in the teacher key; the historian's article written for this tool with citations to published historians; the corrections note template.
- The host and podcast are made up and labeled; every source, date and figure is real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The episode pauses at each lit claim until a rating is placed; the student can scrub back.
- The transcript is complete, so a student who can't listen can read every word.
- Keyboard: Tab to play, the transcript, claims, the source panel, ratings and tags; Space plays and pauses; Enter rates.
- With Motion off the waveform stays still.

## Look
- Accent `--brand` #8b2f55 podcast plum (header, the player, ratings); gold #f4c542 (the lit claim, a fault tag); paper #fbf1f5; ink #2a0d19; muted #61505a.
- Contrast (WCAG 2.1, computed): white on brand 7.97:1; brand on paper 7.21:1; ink on paper 16.24:1; muted on paper 6.78:1; ink on gold 11.04:1.
- Never color alone: ratings carry words and icons; faults carry labels.
- Different from this batch (night navy, archive gray, campaign green, orbit indigo).

## Art
- Public domain (Library of Congress FSA collection, National Archives, Federal Reserve, ids checked at build): a crowd outside the New York Stock Exchange (1929); a 1936 Dust Bowl photograph; a bank run photograph (1930s); a breadline photograph; the Federal Reserve money supply chart redrawn in code from published data. Each with credit.
- Local FLUX (`scripts/localart.py`): the podcast studio (1, 16:9).
- Drawn in code: the player, waveform, transcript, charts.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the made-up podcast host who reads the whole episode; `curious-librarian` as the hints and source notes. `Curio.voice` with `scope: () => state.mode + ':' + state.claim + ':' + state.line`, `welcomeAfter: true`. The episode's audio is generated from the script in `lively-host`.
- how `welcome`: as on load.
- event, whole, each episode segment.
- event, whole, each source note.
- how `rate`: "Mark whether this source supports the claim, and why."
- how `argue`: "Check each argument against the sources."
- how `correct`: "Write the corrections note."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the player with transcript sync, claim pauses, the source panel, ratings and fault tags, the argument step, the corrections note.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Ratings | Mark everything "supports" | Each rating checks against the key; a planted fault marked "supports" plays a pointer to the clue. |
| Fault tags | Pick any fault | Each tag checks against the planted fault. |
| Corrections | Write one vague line | The note needs one right claim, one overstated claim and a named source. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Episode segment (whole), waits; source note (whole).
2. `rate`, at each claim.
3. `argue`.
4. `correct`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.9.9-12, D2.His.13.9-12 and D2.His.17.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Black Thursday (October 24) and Black Tuesday (October 29, 1929) | Federal Reserve History, "Stock Market Crash of 1929" | Britannica, "Stock market crash of 1929" | yes |
| About 9,000 banks failed 1930 to 1933 | FDIC, "A Brief History of Deposit Insurance" | Federal Reserve History, "Banking Panics of 1930-31" | yes |
| Unemployment near 25 percent in 1933 | Bureau of Labor Statistics, "Unemployment in the 1930s" | Federal Reserve History, "The Great Depression" | yes |
| The money supply fell about a third, 1929 to 1933 | Friedman and Schwartz, "A Monetary History of the United States" (Princeton, 1963) | Federal Reserve History, "The Great Depression" | yes |
| The gold standard spread the slump | Eichengreen, "Golden Fetters" (Oxford, 1992) | Bernanke, "Nonmonetary Effects of the Financial Crisis," American Economic Review (1983) | yes |
| "Prosperity is just around the corner" is not a verified Hoover quote | Herbert Hoover Presidential Library, FAQ on attributed quotes | Keyes, "The Quote Verifier" (St. Martin's, 2006) | yes |
| Federal Writers' Project interviews date from 1936 to 1939 | Library of Congress, "American Life Histories" collection | National Archives, WPA records | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r19, 2026-11-09): twelve claims with six sound and six planted; every planted fault has one key answer; the 1938 interview is 9 years after 1929; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 player and source; at 680x425 sheet.
2. Each lit claim links to its cited source. (D2.His.9.9-12)
3. Each source is rated with a named fault where it doesn't fit. (D2.His.13.9-12)
4. The argument step checks the episode and the historian's article against the sources. (D2.His.17.9-12)
5. The corrections note names a right claim, an overstatement and a fixing source. (D2.His.17.9-12)
6. The full transcript matches the audio word for word.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still waveform; no network requests.

## Open questions
- The module is still titled "Behind the Documentary" while the tool is a podcast (default used: the podcast as the idea card says; module name left for the orchestrator to align).
