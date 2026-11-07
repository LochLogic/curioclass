# Teaching lens: puppet-show-feelings (round 1)

Cold lens, 2026-11-05. Read spec.md, src.html, notes.md, art/prompts.json, audit-states.json, the shared audit
(S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1) and the NCAS Theatre at a Glance PDF (K to 2 rows of
TH:Re7.1, TH:Re8.1, TH:Cn10.1). Own runs: drive.py on port 9881, shots in
S:/CurioClass-codex-scratch/puppet-show-feelings/teaching/ (shots.json, shots2.json, out/, vlog.json, show5.json,
likeme.json, read.json).

Not a Curiosity. Nothing cultural, Native or hard-history: no sensitivity review needed (the Like me memory prompt is
a disclosure question, covered below as a notes item, not a sensitivity item).

## Standards against the NCAS wording

- **TH:Re7.1** (K: express an emotional response to characters; 1: recall choices made; 2: recognize when artistic
  choices are made). Taught well. Show asks "How does Pom feel?" every scene; Backstage has the student make one
  choice at a time and watch the reading change; the "what changed" row names the choice. Pass.
- **TH:Re8.1a** (K: identify preferences; 1: explain preferences and emotions; 2: explain how personal preferences
  and emotions affect an observer's response). K is taught (ending choice, ending vote). Grades 1 and 2 are thin: see
  finding 2.
- **TH:Cn10.1** (K: similarities between characters and oneself; 1: identify character emotions and relate them to
  personal experience; 2: relate character experiences to personal experiences). Like me never connects to Pom or
  the story: see finding 1.

## Findings

1. **should fix** (general). Like me, src.html:732 and :423 (`life` lines). The card prompt is "When did you feel
   worried? Tell Pom, or pass." with no link to Pom. Cn10.1.1 asks the child to identify a *character's* emotion and
   relate it to their own; Cn10.1.2 to relate the character's *experience*. As built it is a generic feelings chat.
   Every feeling already has a story moment, so the fix is cheap: "Pom felt worried when the kite got stuck. When did
   you feel worried?" (happy scene 1, excited scene 2, worried scene 3, sad scene 4, proud A new kite, calm Wait for
   the wind). Seen: likeme.json (spoken lines), frame audit-r1/state-like-feeling-1366x768.png.

2. **should fix** (general). Like me ending vote, src.html:738-747 and :855. Tapping an ending at once replaces the
   prompt "Tap the ending you like. Tell Pom why." with the narrator's own reason ("Some people like it when a friend
   helps."), spoken about 4 s later (likeme.json: 13.8 s then 18.0 s). The child is handed the why instead of giving
   it, so Re8.1.1 (explain preferences and emotions) and Re8.1.2 (how your own preferences and emotions shape your
   response as an observer) are only mentioned. Better: on a vote, first "Why do you like that ending? How did it make
   you feel?" and keep "Some people like..." as the follow-up (or behind a second tap), so the class's own reasons
   come first. Seen: likeme.json, frame audit-r1/state-like-vote-1366x768.png.

3. **should fix** (general). notes.md, Like me and Good to know (rule 8). The prompt asks five-year-olds in front of
   a class when they felt sad or worried. Notes rightly say a child may pass, but they do not name that this can
   surface a serious disclosure (home, loss, fear) or what to do: model a small example first, keep it light, and
   follow the school's procedure and talk privately if a child shares something worrying. One or two sentences.

4. **should fix** (general). src.html:423 and :655 (`praise`), :422 (`audience`). "Yes! That's sad!" reads to a
   child as cheering that something is sad (or the idiom "that's too bad"), and "Yes! That's worried!" and "That's
   calm!" are not natural English. "The audience sees worried." / "sees sad." has the same problem. Plainer for K-2:
   "Yes! Pom looks sad!" and "The audience sees a worried Pom." (or "The audience thinks Pom feels worried."). Seen:
   vlog.json (42.9 s "Yes! That's sad!"). The spec wrote these lines, so the change touches voice/lines.json too.

5. **polish** (general). Show, Show me, src.html:584 and :813. The reveal gives only the word ("Pom feels worried.").
   The story text already carries most feelings ("Oh no! The kite is stuck"), so a child can answer from the words and
   never look at the puppet, which is the whole idea of the tool. Better: the reveal names the clues too, on the card
   and in the line: "Pom feels worried. Head down, fast voice." That makes the default mode teach Re7 the way
   Backstage does.

6. **polish** (general). Backstage first change, src.html:690. "Only one thing changed, and the feeling changed!"
   plays after the babble, before Audience says (vlog.json: 9.4 s, card at 26.3 s). It tells the class the reading
   flipped before they have said what they see. Better: speak it once right after the first Audience says that
   follows a flip, where it confirms instead of tips.

7. **polish** (general). Feeling faces, src.html:460-468. At the small sizes the sad and worried faces are nearly the
   same frown (frame audit-r1/state-like-feeling-375x812.png, the worried card beside sad). Pre-readers lean on the
   face, not the word. Better: give worried a wavy mouth and raised inner brows so it differs from sad at 27 px.

8. **nit** (general). src.html:406. "all by herself" is the only pronoun for Pom; everywhere else Pom is just "Pom".
   "all on Pom's own" keeps it consistent.

## Done when (spec)

| # | check | result | how |
|---|---|---|---|
| 1 | Pom largest, nine controls visible, 1366x768 and 680x425 | pass | audit frames size-1366x768, state-backstage-audience-1366x768 and -680x425 |
| 2 | 27 settings and every scene read as the table | pass | logic shot: `feeling()` against the spec table, 0 mismatches; all 8 scenes/endings and 6 presets match |
| 3 | ease from where it is; babble Slow 260, Middle 150, Fast 95 ms | pass | ease shot: tilt -18 to 28 over about 160 ms (4, 17.8, 23.2, 27.1, 28); babbleLog ms 150/260/95, pitch 1/0.85/1.15 |
| 4 | a tap during babble acts at once and hides the card | pass (code and audit) | change() bumps serial, stopBabble, hides #audience-card; audit held clicks clean |
| 5 | three endings; Next disabled only on scene 5; no line names Next there | pass | showwalk: Next disabled only at index 4; ending how line names the three endings only; show5.json plays A new kite and Dot helps, audit state-ending-2 the third |
| 6 | Try it praises every met target, cycles all six | pass | try shot: all six met in order and wrapped to sad; praise spoken with real input (vlog.json 42.9 s) |
| 7 | how lines once; scene lines and the question every scene | pass | vlog.json: change how once, flip once then silent x4; show5.json: question after every scene, ending how silent the second time |
| 8 | 60 px controls with icon and word; face plus word | pass | audit size rows clean; frames |
| 9 | Motion off: no bounce or ease, babble timing the same | pass | motionoff shot: tilt jumps to 28, translateY(0px) throughout, babble 150 ms |
| 10 | no network, nothing saved | not my lens | no storage calls in src.html beyond the kit Motion preference |

Facts: the table recomputed (sad 4, worried 7, calm 3, proud 3, happy 5, excited 5; 27 cells), tilt angles, bounce
sizes and syllable timings all match the spec. Citations check out (Dael, Mortillaro and Scherer 2012, Emotion 12(5)
1085-1101; Wallbott 1998, EJSP 28, 879-896; Juslin and Laukka 2003, Psych Bull 129(5) 770-814: slow rate for sadness,
fast for fear and happiness). Notes describe this tool truly; Read in Backstage gives only the settings while the card
is hidden (read.json), so no giveaway. Support at home ideas are doable tonight.

Cheap pass: Try it can be met by sweeping H, V and B (notes say so honestly; there is no score, so it is not a
blocker). Like me shows each feeling's preset pose, which is a demonstration, not a quiz answer.

## Audit pilot

- Leads confirmed: none that bear on teaching. The "welcome not heard" lead (first tap on Show me, Back, Next or
  Again) is real in code (the Show welcome only plays from a stage tap or mode entry), but its teaching cost is small:
  the welcome only says "Watch Pom. Then tap Next." Left to Play.
- Leads wrong: none seen.
- Missed (by design): findings 1 to 4 (standards depth, disclosure note, praise wording), the clue-free reveal, the
  early flip line, and the sad/worried face likeness.
