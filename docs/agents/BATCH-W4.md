# Batch note: spec wave 4, 9-12 ELA, library and ELD (2026-10-27)

Cory asked for a small wave 4 of about 40 tools after waves 2 and 3. This wave is every remaining 9-12 ELA tool, the
two 9-12 library tools and the six 6-12 ELD tools: 42 in five groups, grouped by family and strand rather than by
grade, so each family's tools are designed together. 9-12 social studies waits for Cory's answer on hard history
(gap fill Q3, `docs/agents/gapfill/REPORT.md`); world languages wait for signers and a Spanish voice.

The overlap pass is done and Cory decided every cluster (`docs/agents/overlap/choices.json`); accepted fixes are
already in `data/concepts/*.txt`. Fixes left for the spec are in the per-tool notes below. Tools added by the gap fill
point to their staging notes (`docs/agents/gapfill/<domain>/notes.md`).

## How this wave runs

Spec agents each take one group below and write every spec in it. At most three run at once. Then the integrating
session runs the spec check (`python scripts/spec_sheet.py docs/agents/BATCH-W4.md`) and a review like waves 2 and 3.

## Rules for this wave (on top of SPEC.md and STANDARDS.md)

The wave 1 rules apply unchanged (`docs/agents/BATCH-W1.md`, "Rules for this wave"), and so do the wave 2 additions
on standards, real numbers, families and look and voice across 9-12 (`docs/agents/BATCH-W2.md`). Read both first.
On top of them:

- **Texts.** Full passages only from public-domain works (published in the US before 1930, or US government
  documents), each with its source edition in "Sources". Modern works appear only as title, author and a one-line
  summary, never quoted beyond a short phrase. Original passages written for the tool are fine and say so.
- **Writing stays private.** Anything a student writes stays in the page (localStorage with Clear at most). No
  prompts that ask for trauma, health, family conflict or other private matters; personal essays offer neutral
  topics and say students choose what to share.
- **Speaking.** Microphone only if the tool can't work without it, kept in memory, never saved, with a no-mic path
  (wave 1 rule). A speaking tool works fully with the student reading aloud to a partner instead.
- **Families.** None of this wave's families has a family doc, and their lower-grade siblings are not specced. The
  sibling in this wave with the highest grade describes the shared engine in full in "Family engine" (research,
  rhetoric, founding-docs, shakespeare, evidence, word-lab, fallacies), written so the lower grades can reuse it, and
  names them. fact-check: read the wave 1 spec tools/fake-or-fact-lab/spec.md and match it. eld-talk: read the live
  classroom-phrases-game.
- **Hard history and founding documents** are taught plainly at grade level, including who the documents left out;
  anything a parent might want to see first goes in "Open questions".
- **Style guides and grammar** name their source (MLA Handbook 9th ed., APA 7th ed., Chicago 18th ed., or a named
  usage guide); where guides differ, the tool says so.
- **ELD** follows WIDA 2020 (language uses Narrate, Inform, Explain, Argue) with proficiency levels as settings;
  supports (frames, word banks, visuals) fade as the level rises. No home-language translation unless sourced and
  reviewed; leave that as an open question.

## Groups and per-tool notes

### ELA and library: research and sources (`ela-research`, 6)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| research-notebook | Research Notebook | 9 | explorer | research |
| portrait-in-four-media | Portrait in Four Media | 10 | explorer | research |
| source-mixer | Source Mixer | 11 | data | research |
| question-sharpener | Question Sharpener | 12 | tycoon | research |
| source-portfolio | Source Portfolio | 9-12 | builder | research |
| enduring-questions | Enduring Questions | 9-12 | explorer | - |

- **portrait-in-four-media:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **question-sharpener:** Topic line under the title on the tool page: "writing a research question". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: A business tycoon beside ad-agency and startup-tycoon, and a second research planner beside research-notebook. Family: stays in research.

- **source-portfolio:** New in the gap fill (docs/agents/gapfill/social/notes.md).

- **enduring-questions:** New in the gap fill (docs/agents/gapfill/social/notes.md).

### ELA: rhetoric, argument and founding documents (`ela-argument`, 11)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| rhetoric-spotter | Rhetoric Spotter | 9 | sort | rhetoric |
| rhetorical-situation-simulator | Rhetorical Situation Simulator | 11 | simulator | rhetoric |
| argument-map | Argument Map | 12 | builder | rhetoric |
| argument-builder-pro | Argument Builder Pro | 9 | builder | evidence |
| theme-ledger | Theme Ledger | 9-12 | data | evidence |
| fallacy-field-guide | Fallacy Field Guide | 10 | cards | fallacies |
| thesis-workshop | Thesis Workshop | 10 | builder | - |
| audience-shift-briefing | Audience Shift Briefing | 9 | simulator | - |
| ad-agency | Ad Agency | 12 | tycoon | fact-check |
| founding-words-explorer | Founding Words Explorer | 9 | explorer | founding-docs |
| premise-inspector | Premise Inspector | 11 | explorer | founding-docs |

- **theme-ledger:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **audience-shift-briefing:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **founding-words-explorer:** Overlap note (left for you to settle in the spec): Cuts 'echoes in later speeches', which belongs to premise-inspector (RI.11-12.9). Suggested fix (reshape): keep the title: Read founding documents with plain-English layers and historical context; trace how each document's central ideas develop across its sections. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in founding-docs.

- **premise-inspector:** Overlap note (left for you to settle in the spec): Reads founding documents beside later speeches, the same texts and move as founding-words-explorer. Suggested fix (reshape): keep the title: Lay out the Declaration's argument as premises and a conclusion, then test later responses (Seneca Falls, Douglass's Fifth of July speech, the Gettysburg Address) by which premise each accepts, stretches or rejects. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in founding-docs.

### ELA: literature (`ela-lit`, 10)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| character-web | Character Web | 9 | explorer | - |
| tension-meter | Tension Meter | 9 | data | - |
| world-lit-atlas | World Lit Atlas | 10 | map | - |
| american-lit-timeline | American Lit Timeline | 11 | timeline | lit-timeline |
| shakespeare-remix | Shakespeare Remix | 9 | studio | shakespeare |
| globe-theatre-stage | Globe Theatre Stage | 12 | explorer | shakespeare |
| page-to-screen | Page to Screen | 10 | explorer | - |
| ambiguity-lab | Ambiguity Lab | 12 | lab | - |
| idea-threads | Idea Threads | 9-12 | explorer | - |
| tone-dial | Tone Dial | 10 | simulator | - |

- **idea-threads:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

### ELA: writing, language and speaking (`ela-craft`, 9)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| parallel-parking | Parallel Parking | 9 | puzzle | - |
| punctuation-power-ups | Punctuation Power-Ups | 10 | race | - |
| personal-essay-studio | Personal Essay Studio | 11 | studio | - |
| editors-in-the-margin | Editors in the Margin | 9-12 | studio | - |
| pacing-strip | Pacing Strip | 9-12 | lab | - |
| word-family-tree | Word Family Tree | 12 | explorer | word-lab |
| key-term-tracker | Key Term Tracker | 9-12 | explorer | word-lab |
| socratic-seminar-board | Socratic Seminar Board | 10 | showdown | - |
| speech-coach | Speech Coach | 12 | lab | - |

- **editors-in-the-margin:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **pacing-strip:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **key-term-tracker:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

### ELD 6-12 (`eld-hs`, 6)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| then-what-happened | Then What Happened? | 6-12 | builder | - |
| definition-duel | Definition Duel | 9-12 | cards | - |
| chart-narrator | Chart Narrator | 9-12 | data | - |
| historian-s-toolkit | Historian's Toolkit | 9-12 | mystery | - |
| inbox-simulator | Inbox Simulator | 9-12 | simulator | - |
| argument-frames-pro | Argument Frames Pro | 9-12 | roleplay | eld-talk |

- **then-what-happened:** New in the gap fill (docs/agents/gapfill/ela/notes.md).

- **inbox-simulator:** Spec note from the overlap pass: stay on email and register; job interviews belong to interview-simulator.

- **argument-frames-pro:** Topic line under the title on the tool page: "academic argument language". Overlap note (left for you to settle in the spec): Title differs by one word from argument-builder-pro (9-12); the ELD scaffolds already make the tool different. Suggested fix (rename): "Counterpoint Frames". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in eld-talk.

