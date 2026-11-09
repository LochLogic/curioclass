# Pitch Deck Studio

## One idea
The student builds a three-minute, five-slide pitch to the student council (start a repair café at school), and before any borrowed chart, photo or ad goes on a slide, a media-motive lens makes them say who made it and what that maker wants (to sell, to inform, to win a vote), then they rehearse and record each slide against a timer and a council member reacts, so they learn to present a claim with sound evidence and media that strengthen it, and to name the motives behind the media they borrow.

## Not like
- docent-tour-talk (6-8, spec): an informative tour adapted to listeners. Here a persuasive pitch with borrowed media, grade 8.
- ad-agency (12, concept): running and auditing ad campaigns. Here judging one item's motive before using it.
- explainer-studio (7, spec): a written magazine page. Here slides and spoken delivery.
- source-sorter (6, spec): sorting sources by reliability. Here the maker's motive and what it means for using the item.
- dramatic-irony-theater (8, spec, this batch): directing a play. Here presenting yourself.

## Who and how
- Grade 8, ELA, module "Presentations and Media" (Speaking and Listening). Standards: SL.8.2, SL.8.4, SL.8.5.
- Driver: one student; class mode is "Council day", where students pitch live and the class votes (tool.json `driver: "student"`). Every library item and council line is read on tap.
- One main pitch (Repair café) and a practice pitch (Longer library hours), each with its own media library. tool.json `modes: ["Repair café", "Library hours", "Rehearse", "Council day"]`, `minutes: "35-45"`, `grades_label: "Grade 8"`.
- Records with the microphone in Rehearse; the privacy line always shows: "Your recordings stay on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the deck, the lens notes and the self-check.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.8.2 (motives: social, commercial, political) | Run every library item through the lens: maker, what they want, what that means for using it | the lens card with the motive named | 2 |
| SL.8.5 | Choose charts, photos and stills that clarify the claim; a chart that doesn't match its claim is flagged | the slide with its media and the checklist | 3 |
| SL.8.4 (claims, evidence, reasoning) | Write the claim slide and reason slides with evidence; the checklist flags slides with no evidence or too many words | the deck and the checklist | 3 |
| SL.8.4 (eye contact, volume, pronunciation) | Record each slide's talk with a timer and volume meter; mark own delivery | the rehearsal strip and self-check | 4 |
| SL.8.2, SL.8.4 | The council member reacts: evidence wins votes, an unnamed motive loses one | the vote card | 5 |

## Screens and modes
Header (kit): title "Pitch Deck Studio"; `Deck`, `Library`, `Rehearse`, `Council`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small studio with a laptop showing five blank slides, a pitch card pinned above it ("Council has three minutes and $500. Make your case.") and a drawer labeled Library; council president Isabel Ferreira waits at a long table. First hint: "Tap the pitch card to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Deck.** Five slides: Claim, Reason 1, Reason 2, Plan and cost, Ask. The student writes the claim ("Our school should hold a monthly repair café") and each reason, then drags in evidence and media. A checklist runs on every slide: no evidence on a reason slide; a chart whose title or numbers don't match the slide's claim; more than 30 words on a slide; a cost that is more than $500.

**Library.** About twelve items, each labeled "practice item, made up" unless real:
- Real: a short history card, "The first Repair Café was held in Amsterdam on October 18, 2009, organized by Martine Postma", with its source.
- Practice: a chart from a made-up school survey ("62% would bring something to fix"); a photo of a broken toaster and a phone with a cracked screen; a made-up electronics store ad ("Why repair? Our new phones start at $199!"); a made-up city waste report page; a made-up news story about a library tool-lending shelf; a made-up candidate flyer ("Vote Lee: Fix-It Fridays!").
When the student drags an item to a slide, the lens opens: Who made it? (choices plus own words) What do they want? (Sell, Inform, Win a vote, Win support for a cause) What does that mean for using it? (Drop it; Use it and say who made it; Use it as is). The store ad keyed Sell can be used only with "say who made it", and the student types the attribution the slide will show. The candidate flyer is keyed Win a vote.

**Rehearse.** For each slide the student taps `Record`, talks, and stops. A per-slide timer and a volume meter (loud enough, too quiet) run while recording; the whole pitch must fit in three minutes. Playback is local. Then a self-check: for each slide, the student marks eye contact (looked up at least twice), volume and pronunciation of hard words (they list any).

**Council.** Isabel reads the deck and votes slide by slide on a five-member board: an evidence slide that matches its claim wins a vote; a slide with an item whose motive was not named loses one ("Wait, isn't that from a store that sells phones?"); a slide over the word limit gets "I couldn't read all that." The pitch passes with three votes.

**Council day.** Live pitches; the class votes with cards.

At 1366x768 the slide and library fit side by side; at 680x425 the library is a drawer.

## Content
Written for Curio Class: both pitches, the libraries with keyed makers, motives and uses, the checklist rules and the council's reactions. Every practice item is labeled made up on screen. The repair café history card is the only real fact in the library.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Items can be removed from slides at any time; the lens note stays with the item.
- Recordings can be redone per slide; leaving the page erases them.
- With Motion off slides don't transition and the volume meter shows a level word instead of bouncing.

## Look
- Accent `--brand` #4b3a8c council violet (header, slide frames, lens); gold #f4c542 (votes won, the timer's last ten seconds); paper #f5f3fb; ink #17112e; muted #58546c. Scene: a sunny student studio with a long council table.
- Contrast (WCAG 2.1, computed): white on brand 9.20:1; brand on paper 8.36:1; ink on paper 16.52:1; muted on paper 6.59:1; ink on gold 11.17:1.
- Never color alone: checklist flags and votes have words and icons.
- Different from this batch (curtain red, slate blue, bronze, surgical green).

## Art
- People art goes to Gemini: Isabel Ferreira (a Brazilian American eighth grader with braids), 4 poses; four other council members (mixed teens, one in a wheelchair), 1 pose each; "illustrated student council member <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): studio with a laptop (1); a table of broken things (toaster, lamp, bike wheel) (1); a library tool shelf (1).
About 11 images. Drawn in code: slides, charts, the ad and flyer (made up, no real brands), lens, timer, meter.

## Voice
Bank voice `bright-teacher` as the hint voice and library reader (unique in this batch); Isabel and the council are read by `firm-captain` (unique in this batch). `Curio.voice` with `scope: () => state.pitch + ':' + state.view + ':' + state.slide`, `welcomeAfter: true`.
- how `welcome`: "You've got three minutes and five slides. Before you borrow anything, ask who made it and what they want."
- event `item`: the library item.
- event `lens`: "Who made this, and what do they want?"
- event `flag`: the checklist flag ("This chart's about lunch, but your slide's about repairs.").
- event `vote`: the council member's reaction.
- event `privacy`: "Your recordings stay on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: slide model, library with keyed motives, the lens, the checklist, recording with timer and volume meter (no speech recognition), council votes.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Lens | Pick Inform for everything | Each item's motive is keyed; a wrong motive reopens the lens. |
| Ad use | Use the store ad as is | "Use it as is" is not accepted for keyed Sell or Win a vote items. |
| Evidence | Put a photo on every slide | Reason slides need a chart, report or history card that matches the claim. |
| Rehearse | Skip recording | Council needs one take per slide within three minutes. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the pitch card: pitch card, `welcome` (queued, first time).
2. Library: `item` on tap; `lens` when dragged to a slide.
3. Deck: `flag` as it fires.
4. Rehearse: `privacy` the first time `Record` is tapped.
5. Council: `vote` per slide in order (each waits).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.8.2, SL.8.4 and SL.8.5 wording | thecorestandards.org, Speaking and Listening Grade 8 | CCSS ELA 2010 PDF | yes |
| The first Repair Café was organized by Martine Postma in Amsterdam on October 18, 2009 | repaircafe.org, About (checked 2026-11-09) | Wikipedia, Repair Café | yes |
| Media literacy asks who made a message and why it was made (purpose and motive) | Center for Media Literacy, Five Key Questions | National Association for Media Literacy Education, key questions | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): every chart, ad, flyer, report and news item in the libraries is made up and labeled; no real store or candidate is named.

Checks run (Python, scratchpad b23, 2026-11-09): the saved repaircafe.org page contains "the very first Repair Café in Amsterdam, on October 18, 2009"; each library has at least one item keyed to each motive; the sample deck fits three minutes at 130 words a minute; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 slide and library fit; at 680x425 the library is a drawer.
2. Every dragged item opens the lens; keyed motives and uses check. (SL.8.2)
3. The checklist flags missing evidence, mismatched charts, long slides and costs over $500. (SL.8.4, SL.8.5)
4. Rehearse records per slide with timer and volume meter, shows the privacy line, and takes the self-check. (SL.8.4)
5. The council votes by slide with keyed reactions. (SL.8.2, SL.8.4)
6. Council day works with a class vote.
7. Print shows the deck, lens notes and self-check.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no slide transitions and the meter shows words; no network requests.

## Open questions
- None for Cory.
