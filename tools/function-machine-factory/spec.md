# Function Machine Factory

## One idea
On a factory floor where every machine takes an input and gives an output, the floor manager, Mr. Boateng (made up, labeled "illustration"), puts the child on quality control with one rule, "every input gets exactly one output", and the child feeds inputs down the conveyor and watches what comes out; each test drops an ordered pair on the machine's graph, and a faulty machine that answers 4 and then 7 for the same input shows two dots stacked on one input and gets the red reject tag; compare levels set two machines side by side described in different ways, a machine labeled y = 3x + 2 against one known only from its table (0, 5), (1, 7), (2, 9), and the child finds that the first grows faster (3 per step against 2) while the second starts higher (5 against 2), then picks the machine a customer's order needs; straight-or-curved levels let the child build machines from y = mx + b and watch every graph come out straight, then a square-area machine (side in, area out) gives 1, 4, 9, 16 with steps of 3, 5, 7, and its graph curves; the child sorts every machine into linear and nonlinear with a table reason (equal steps in give equal steps out, or not); at the end the child sees that a function is a rule with one output per input and that the same function can wear four disguises, a table, a graph, an equation and a sentence, so an eighth grader learns to define, evaluate and compare functions and tell linear functions from nonlinear ones.

## Not like
- rule-machine (4, spec): pattern rules, same family. Here the definition of a function.
- undo-machine (11, live): inverse functions, same family. Here functions and their forms.
- story-graphs (8, spec): sketching graphs from stories. Here testing and comparing rules.
- summer-stand (6, spec): dependent and independent variables. Here one output per input.

## Who and how
- Grade 8, Math, module "Defining Functions". Standards: 8.F.1 (understand that a function is a rule that assigns to each input exactly one output; the graph of a function is the set of ordered pairs consisting of an input and the corresponding output), 8.F.2 (compare properties of two functions each represented in a different way (algebraically, graphically, numerically in tables, or by verbal descriptions)), 8.F.3 (interpret the equation y = mx + b as defining a linear function, whose graph is a straight line; give examples of functions that are not linear).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve inspections, six compare orders, ten machines to sort, the four-disguises board. Extra: Mystery machine (a partner builds a hidden machine, the other classifies it, one device). tool.json `modes: ["Factory", "Mystery machine"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.F.1 | Feed inputs; pass or reject machines | two dots stacked on one input | 2 |
| 8.F.2 | Compare machines given in different forms | rate 3 against 2; start 2 against 5 | 3 |
| 8.F.3 | Build y = mx + b machines; sort linear and nonlinear | straight lines; the square curve | 4 |

## Screens and modes
Header (kit): title "Function Machine Factory"; `Factory`, `Mystery machine`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright factory floor, a conveyor, three machines with inspection tags, and Mr. Boateng with a clipboard. The welcome is queued (`welcomeAfter: true`): "Every input gets exactly one output. Test them. Type an input and tap Feed." First hint: "Type an input and tap Feed."

**Inspect (focus: the machine).** At 1366x768 the conveyor and machine fill the left with the graph and table right; at 680x425 the graph is a tab. Each feed adds a row to the table and a dot to the graph. The child stamps `Pass` or `Reject`; a reject must point to the two outputs for one input. Some machines are sentences ("gives your locker number for your name"), and the child tests them by thinking, not feeding.

**Compare.** Two machines on one bench, each in a different form (equation, table, graph, words). The child types each rate and start, says which grows faster and which starts higher, and fills a customer order ("we need more than 20 by input 6").

**Straight or curved.** The child sets m and b on a machine and feeds 0 to 4; the graph is straight. Then the square-area machine. A sorting bin takes ten machines; each sort needs a table reason: the differences row is shown after the child picks.

**Four disguises (the aha).** Mr. Boateng: "One rule, one output each time. Table, graph, equation or words, it's the same machine."

**The end.** The inspection log and the sorted bins. `Print` prints them.

**Mystery machine (extra).** One partner builds a hidden machine; the other feeds and classifies.

## Content
- Thirty machines in all four forms, all readable with `Read`.
- Non-function machines are clearly marked after the stamp, never before.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Stamps can be changed until `File it`; m and b can be changed any time.
- Keyboard: Tab to the input box, Feed, the table, the graph (arrows move between dots), stamps, compare boxes and bins; Enter feeds or files.
- With Motion off the conveyor does not move and outputs appear at once.

## Look
- Accent `--brand` #a03a1c factory red (header, machines, buttons); gold #f4c542 (the input in hand, the pass stamp); paper #fbf0ec; ink #2c0f05; muted #5f514b.
- Contrast (WCAG 2.1, computed): white on brand 6.74:1; brand on paper 6.02:1; ink on paper 15.95:1; muted on paper 6.79:1; ink on gold 10.96:1.
- Never color alone: stamps read "Pass" or "Reject"; bins read "linear" and "nonlinear".
- Different from this batch (blueprint blue, reef green, loop indigo, case-file brown).

## Art
- People (illustrated): Mr. Boateng and two workers, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the factory floor (1, 16:9), machine shells (4, 1:1).
- Drawn in code: the conveyor, tables, graphs, stamps and bins.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Boateng; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.machine + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `feed`: "Type an input and tap Feed."
- how `stamp`: "Tap Pass or Reject."
- how `compare`: "Type the rate and the start for each machine."
- how `build`: "Set m and b, then tap Feed."
- how `sort`: "Drag the machine to a bin."
- event, whole, four disguises.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
function-machine, the `/* ==== FUNCTION-MACHINE ENGINE ... */` block as described in undo-machine's spec: the part table, chain run and formula builder. Graphs use kit:graphing `Plane`, `g.fn` and `g.point`. Tool-only code: faulty machines (seeded two-output rules), the compare bench, the differences row, the sorting bins.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Inspection | Pass every machine | Faulty machines show stacked dots, and the stamp is checked. |
| Compare | Pick the bigger first number | Rate and start are typed and checked separately. |
| Sort | Call every rising graph linear | The square machine rises and curves; the reason must cite the differences. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `feed`; `stamp`.
2. `compare`.
3. `build`; `sort`.
4. Four disguises (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.F.1 to 8.F.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Moving among tables, graphs, equations and words builds the function idea | Common Core Standards Writing Team (2013), "Progressions for the CCSS, Grade 8 Functions" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 algebra | yes |
| Constant first differences mark linear functions | Common Core Standards Writing Team (2013), "Progressions for the CCSS, Grade 8 Functions" | Leinhardt, Zaslavsky and Stein (1990), "Functions, Graphs, and Graphing", Review of Educational Research | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s20, 2026-11-10): y = 3x + 2 has rate 3 and start 2; the table (0, 5), (1, 7), (2, 9) has rate 2 and start 5; 1, 4, 9, 16 have differences 3, 5, 7; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 conveyor, graph and table; at 680x425 graph as a tab.
2. Twelve machines are inspected and stamped, with rejects pointing to two outputs for one input. (8.F.1)
3. Six pairs in different forms are compared by rate and start. (8.F.2)
4. Ten machines are sorted linear or nonlinear with a table reason. (8.F.3)
5. Uses the FUNCTION-MACHINE ENGINE block unchanged.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: outputs appear at once; no network requests.

## Open questions
None.
