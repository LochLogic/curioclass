# Evidence Corkboard

## One idea
On the board of a canal office in Albany, the child answers one question, "Why did the Erie Canal change New York?", by pinning evidence from a box (a booster's letter, canal maps, toll records, freight prices before and after 1825, a table of New York City's population by census, a traveler's account, a worker's pay record) under reasons, then stringing each pin to the claim; each pin gets a limits tag for what it can't show (a toll record counts boats, not who profited; a booster's letter is one-sided), and weak strings sag until a second piece of evidence supports them; the finished board reads off as an argument card, and the gaps become a "next sources" list (whose story is missing: the canal's workers, many of them Irish immigrants, and the Haudenosaunee nations whose lands the canal crossed), so an eighth grader learns to organize evidence into a coherent argument, back each claim with several sources while noting limits, and use questions about sources to find what to look for next.

## Not like
- why-the-pony-express-ended (5, spec): a claim from two sources each, no limits. Here limits tagged and gaps named.
- resource-detective (2, spec): finding resources in a picture. Here building an argument.
- unlabeled-archive (7, spec): identifying sources. Here using them together.
- historians-disagree (7, spec): judging others' arguments. Here building one.

## Who and how
- Grade 8, Social Studies (History and Inquiry), module "Evidence Corkboard". Standards: D2.His.16.6-8 (organize applicable evidence into a coherent argument about the past), D3.3.6-8 (identify evidence that draws information from multiple sources to support claims, noting evidentiary limitations), D2.His.12.6-8 (use questions generated about multiple historical sources to identify further areas of inquiry and additional sources).
- Format: mystery. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Nine evidence pieces, three reasons, the argument card, the next-sources list. Extra: Poster (prints the board as a large poster across four pages). tool.json `modes: ["The board", "Poster"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D3.3.6-8 | Pin each piece under a reason, string it to the claim, and tag its limit; add a second piece where a string sags | the strings tightening with two sources; the limits tags | 2, 3 |
| D2.His.16.6-8 | Read off the argument card in order (claim, three reasons, evidence, a counterpoint) | the argument card built from the board | 4 |
| D2.His.12.6-8 | Write questions about the gaps and pick sources to look for next | the "next sources" list with a question for each | 5 |

## Screens and modes
Header (kit): title "Evidence Corkboard"; `The board`, `Poster`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A canal company office in Albany, 1830s: a tall corkboard on the wall with the question card pinned in the middle, three blank reason cards around it, a spool of red string, a box of evidence on the desk, and a window showing a canal boat pulled by mules. The welcome is queued (`welcomeAfter: true`): "The Erie Canal opened in 1825. People say it changed New York. Can you prove why? Open the evidence box." First hint: "Tap the evidence box."

**Evidence (focus: the piece and the board).** At 1366x768 the board fills the right with the open piece on the left; at 680x425 the piece is a sheet. Nine pieces, each a real document or real figures (picked at build), with a short plain summary:
1. A canal map from Albany to Buffalo, 363 miles, with locks marked.
2. Freight prices: shipping a ton of goods from Buffalo to New York City cost about $100 and took about two weeks by road before the canal, and about $10 and about a week or less after.
3. Toll records: boats and tons passing through each year, rising fast after 1825.
4. A census table: New York City's population in 1820, 1830, 1840 and 1850 (about 124,000; 202,000; 313,000; 516,000).
5. A letter by Governor DeWitt Clinton promoting the canal (a booster).
6. A traveler's account of busy canal towns (Rochester, Syracuse, Buffalo) growing.
7. A map of the Great Lakes region showing farms and settlers moving west by canal.
8. A worker's pay record from the building years (laborers paid by the day, many Irish immigrants later in construction).
9. A note on Haudenosaunee lands: the canal crossed lands taken from the Haudenosaunee nations through treaties and sales in the years before.
- The child pins each piece under a reason (the child names the reasons from tiles: cheaper shipping, trade through New York City's port, growing towns and settlement), strings it to the claim, and picks a limits tag ("counts boats, not profits"; "one person's view"; "a booster wanted support"; "shows numbers, not why"; "doesn't say who did the work").
- One string sags until a second piece supports the same reason; a reason with only one piece stays slack.

**The argument card (D2.His.16.6-8).** Built from the board in order: the claim, three reasons, two pieces of evidence for each with their limits, and one counterpoint the child picks (New York City was already growing; railroads soon competed). The child reorders sentences if the logic jumps.

**Next sources (the aha, D2.His.12.6-8).** The board shows gaps: no workers' own words, no Haudenosaunee voices, no farmers' accounts. The child writes a question for each gap from tiles plus a free line ("What did the workers say about their pay and danger?") and picks a kind of source to look for (letters, newspaper ads, nation records, oral histories). Narrator: "An argument is only as strong as its evidence, and the gaps tell you where to look next."

**The end.** The board, the argument card and the next-sources list. `Print` prints them.

**Poster (extra).** The board printed large across four pages.

## Content
- Nine evidence pieces with summaries and real figures, five limits tags, reason tiles, the argument card builder, two counterpoints, gap questions and source kinds.
- Every piece and figure is real and sourced; figures are rounded and labeled "about".
- The Haudenosaunee land note is plain and sourced.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A piece can be pinned under only one reason at a time; moving it moves its string.
- The argument card opens when every reason has two pins.
- Keyboard: Tab to the box, pieces, reasons, strings and tags; Enter to pin, string and tag.
- With Motion off strings don't sag and swing; slack strings show as dashed.

## Look
- Accent `--brand` #1b5e7a canal blue (header, reason cards, the office trim); gold #f4c542 (a tight string, the piece in hand); paper #eff5f8; ink #06202a; muted #4b5960.
- Contrast (WCAG 2.1, computed): white on brand 7.17:1; brand on paper 6.52:1; ink on paper 15.30:1; muted on paper 6.59:1; ink on gold 10.35:1.
- Never color alone: tight strings are solid and slack strings dashed with a "needs a second source" label; tags carry words.
- Different from this batch (printer's sepia, archive green, Philadelphia navy, signal orange). A canal office, not a detective's den.

## Art
- Public domain (Library of Congress and the New York State Archives, checked at build): an Erie Canal map; a print of a canal lock at Lockport; DeWitt Clinton's portrait; a canal boat print. Each with credit.
- Local FLUX (`scripts/localart.py`): the canal office with the corkboard (1, 16:9).
- Drawn in code: the board, pins, strings, tags, the population chart, the freight price bars, the argument card.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as the canal office clerk and narrator; `news-reader` as the evidence summaries. `Curio.voice` with `scope: () => state.mode + ':' + state.piece + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each evidence summary.
- how `pin`: "Pin this piece under a reason."
- how `string`: "String the pin to the claim."
- how `limit`: "Tag what this piece can't show."
- how `argue`: "Put the argument card in order."
- how `next`: "Write a question for each gap and pick a source to look for."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the corkboard with pins and strings, limits tags, the argument card builder, the gaps list.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pins | Pin everything under one reason | The other reasons stay slack and the argument card won't open. |
| Limits | Tag every piece "one person's view" | Each tag checks; on the census table it plays "Is a census one person's view?" |
| Argument | Accept the default order | The card starts shuffled; each sentence checks its place. |
| Next sources | Leave the questions blank | Print waits for them. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Evidence summary (whole), waits.
2. `pin`; `string`; `limit`.
3. `argue`.
4. `next`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.16.6-8, D3.3.6-8 and D2.His.12.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Erie Canal opened in 1825, about 363 miles from Albany to Buffalo | New York State Canal Corporation, "History of the Canal System" | Encyclopaedia Britannica, "Erie Canal" | yes |
| Freight cost from Buffalo to New York City fell from about $100 a ton to about $10, and time from about two weeks to about a week or less | Britannica, "Erie Canal" | Smithsonian National Museum of American History, "On the Water: The Erie Canal" | yes, as rounded figures |
| New York City's population: about 124,000 (1820), 202,000 (1830), 313,000 (1840), 516,000 (1850) | U.S. Census Bureau, "Population of the 100 Largest Cities, 1790 to 1990" (Gibson, 1998) | New York State Library, census summaries | yes |
| DeWitt Clinton promoted the canal | Britannica, "DeWitt Clinton" | New York State Museum, "Erie Canal" | yes |
| Many laborers were Irish immigrants, especially in later construction | Smithsonian National Museum of American History, "On the Water" | Sheriff, "The Artificial River" (Hill and Wang, 1996) | yes |
| The canal crossed lands taken from the Haudenosaunee nations through earlier treaties and sales | National Museum of the American Indian, "Nation to Nation" treaty materials | Onondaga Nation and Oneida Indian Nation histories of land loss in New York | yes |
| Canal towns like Rochester and Syracuse grew quickly | Britannica, "Rochester (New York)" and "Syracuse" | Sheriff (1996) | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the taking of Haudenosaunee lands is named plainly as a gap in the board and a source to seek, with sources from the nations themselves. A fresh-agent read of that piece is needed before build.

Checks run (Python, scratchpad r14, 2026-11-09): freight $100 to $10 is a 90 percent drop; population rises each census (124,000 to 516,000 is about 4.2 times); three reasons with two pins each need six of the nine pieces; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and piece; at 680x425 sheet.
2. Pins string to reasons; slack strings need a second source. (D3.3.6-8)
3. Each pin has a limits tag that checks. (D3.3.6-8)
4. The argument card orders claim, reasons, evidence and a counterpoint. (D2.His.16.6-8)
5. The next-sources list names questions and source kinds. (D2.His.12.6-8)
6. Poster prints across four pages.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no swinging strings; no network requests.

## Open questions
- Sensitivity flag: Haudenosaunee land loss (default used: named plainly with sources from the nations, framed as a gap to research, fresh-agent read before build).
