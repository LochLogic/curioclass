# Play lens: letter-lanterns (round 1)

Played twice: as a kindergartner alone at home (sound on, no reading) and as a teacher projecting it at 1366x768.
Frames are in `S:/CurioClass-codex-scratch/letter-lanterns/play/` (f1 = the first lantern walked by real held clicks
and real drags, f2 = every event kind, f3 = Village, f4 = misses and free writing), plus the shared audit frames in
`S:/CurioClass-codex-scratch/letter-lanterns/audit-r1/`. Voice was read from `__tool.vlog` after each shot.

What works: the first screen is clear (one gold button, the hint names it), the Find, Say, Trace and Sign loop is
calm and big on a projector, wrong answers teach ("That one says sss."), the second miss beckons the right lantern,
three trace misses finish the stroke with "Let's do it together", tracing backward or scribbling never passes, and
Read the street is a good class finale. The lit string filling the sky is a real reward. Counts below.

## Findings

1. **Say step: the next action is never spoken.** Wake, Say step (`src.html` answerLetter, the `say`/`seeSay`
   branch: `hint('next'); speak('sound.'+letter)`). After the child taps the awake lantern they hear only "mmm"; the
   hint switches to "Tap Next." but that line is never voiced (the log shows `Tap Next.` only as `dropped`, the
   invalid line `interruptNarration` uses). A non-reader alone at home hears the sound and then silence with a gold
   button they cannot read. Same in a Lantern check's See and say. Other done-moments already end with "Tap Next."
   ("Yes! You found it. Tap Next.", "Map! The map shop is open. Tap Next."), so this is the one gap. Better: say
   "Tap Next." once as a how line after the sound the first time, then hint only. Seen: f1/p05-say-tap.png, log
   `[["spoken","mmm"]]`; f2/c02 log. **should fix**, general.

2. **Say step speaks the instruction before the model.** Wake, right Find (`speak([['say',{kind:'how'}],'intro.'+letter])`).
   On the first lantern the child hears "Say its sound. Tap the lantern to check." and then "Mmm. M says mmm, like
   moth." The last thing heard before the waiting moment is the teacher's model, not the child's turn, and the
   right-answer moment opens with an instruction instead of the payoff. The spec has the intro on the right Find,
   then Say ("Your turn..."). Better: intro first, then the say line. Seen: f1/p04-right-m.png, log order
   `spoken Say its sound...` then `spoken Mmm. M says mmm, like moth.` **should fix**, family:letter-pals.

3. **Twins: the shop windows give the answer away.** Wake, Twins (e.g. pan/pin after lantern 7). Both twin shops are
   already open, so each shows its goods in the window: a pincushion under "pin", a frying pan under "pan". "Which
   sign says pin? Tap it." can be answered from the pictures the child just matched in the Sign events, without
   reading the letter that differs, which is the whole point of RF.K.3d (POLISH, Games and quizzes). Better: twins
   shops show closed windows or no goods until the sign is picked, then light up. Seen: f2/e03-twin-diff.png.
   **should fix**, family:letter-pals.

4. **Banners: capital I looks exactly like small l, and "a" turns double-story.** Village street 1 and Lantern check
   banner finds (`.banner-card` font: `'Century Gothic','Trebuchet MS',sans-serif`). The banner "I" is a bare
   vertical bar, the same shape as the l on the ladybug lantern hanging above it. On this machine the font falls back
   and the "a" banner draws a double-story a, while every lantern and sign teaches the single-story ball-and-stick a
   (spec Look). School Chromebooks have neither listed font, so most classrooms see the fallback. Better: draw banner
   words with the tool's own `glyph()` paths (capital I with its top and bottom bars, as STROKES defines it).
   Seen: play/zoom-banner.png (from f3/v04-readstreet.png), f2/f02-banner-find.png ("I my the"). **should fix**,
   general.

5. **Glow levels do not read at a glance on the string.** Village and the Wake string at 1366x768 (`.string .stars
   { font-size:10px }`, halo via `::before` opacity). With 26 lit and mixed glow, one star and two stars are 10 px
   marks under 50 px lanterns; the halo difference is not visible, and the creatures differ in drawn size (the moth m
   and the inchworm i are half the size of the ladybug l), so size reads as glow more than glow does. From the back of
   a room the four outcome states (Done when 7) cannot be told apart. Better: one shared lantern box size on the
   string, stars about 16 px, and a halo that steps visibly per level. Seen: play/zoom-string.png, f3/v04, f3/v09.
   **should fix**, family:letter-pals.

6. **Below 800 px wide the Village hides every lantern, but the welcome says "Tap a lantern".** Village at 680x425
   and 760x900. The string is replaced by the "26 lit" chip in Village too, so the glowing village (the tool's own
   outcome picture) is gone, and at 760x900 the top half of the stage is empty sky. The Village welcome still says
   "Tap a lantern, a shop or a banner." Better: hang the string (even scrolled or two rows) in the empty sky at
   760x900; at 680x425 at least drop "a lantern" from the line when none is shown. Seen: f3/v11-680.png,
   f3/v13-760.png, audit state-demo-village-680x425.png. **should fix**, general.

7. **Village before any lantern is lit points at things that are not there.** Village with 0 lit. The welcome says
   "Tap a lantern, a shop or a banner. Or tap Read the street." and the hint "Tap a shop or Read the street." There
   are no lanterns or banners, every shop is asleep, and Read the street only answers "This street is still asleep."
   A child who taps Village first gets three dead ends before learning to go to Wake. Better: at 0 lit, the Village
   line and hint say the street is asleep and to tap Wake. Seen: f3/v00-fresh-village (log), f3/v00b. Audit lead
   "#read-street ... still asleep" is this. **should fix**, general.

8. **760x900: the lantern being learned is smaller than the cart and floats above it.** Wake, Say and Find at 760x900.
   The backdrop scales to the tall stage but the lantern does not: the moth hangs mid-air about 150 px wide over a
   cart twice its size. The step's focus is not the biggest thing on stage. Better: size the solo and cart lanterns
   from the stage height there, and seat them on the cart. Seen: audit state-say-760x900.png. **polish**, general.

9. **Tracing shows one stroke, never the letter.** Wake, Trace. Stroke 1 of M is a lone vertical bar; the child
   does not see the M they are making until it is done, and the "Look at the model over your ink" after a free-write
   miss shows only that one stroke, not the letter. Better: draw the whole letter faintly under the current stroke
   (current stroke brighter, done strokes gold), and show the full model after a free-write miss. Seen:
   audit state-trace-1366x768.png, f4/x07-free-miss.png. **polish**, family:letter-pals.

10. **Sign and Twins say "lantern" for plain letter tiles.** Wake, Sign and Twins. The hint says "Tap each lantern to
    hear it" and "Tap the different lantern", but above the sign are cream rounded tiles, not lanterns (the spec has
    the lit lanterns hanging over the letters). A child looking for a lantern finds none. Better: hang small awake
    creature lanterns over the letters, or say "letter". Seen: f2/d01-sign-map.png, f2/e01-twins.png.
    **polish**, family:letter-pals.

11. **Long/short flames are loose blobs, off the vowel.** Wake, Long/short (no/not). The tall and small "flames" are a
    cream teardrop and an orange dot centered on each cloth, not over the o, and look unrelated to the flame buttons
    of the vowel step. Better: the o lantern over the o of each word with its tall or small flame, as the spec says.
    Seen: f2/f01-long.png. **polish**, family:letter-pals.

12. **The end card is three lanterns on a cart.** Wake, end. "The whole village glows!" sits over m, s and a on the
    cart, the same picture as the first screen. The moment the whole year built to is flat. Better: every lantern
    swings in, shops light down the street, then Go to Village. Seen: f2/g01-end.png. **polish**, general.

13. **The new lantern flies to the top-left corner, not to its place on the string.** Wake, trace done (`@keyframes fly
    { to { top:6px; left:20px } }`). The string is centered, so the lantern lands in an empty corner, vanishes and
    pops in elsewhere; frozen mid-flight it also covers the "5 lit" chip. Better: fly to the slot it will hang in.
    Seen: audit state-independent-writing-1366x768.png and state-first-shop-sign-680x425.png / 375x812 (creature in
    the corner). **polish**, general.

14. **Write it yourself has no way out before you draw.** Wake, Write it yourself. The panel shows only Teacher; Next
    appears only after a miss or a pass. The spec says it never blocks. A child who tapped it by accident has to
    scribble a failure to leave. Better: keep Next visible. Seen: audit state-independent-writing-1366x768.png.
    **polish**, general.

15. **Say step shows a glow star before the lantern is lit.** Wake, Say: one star under the moth while the chip reads
    "0 lit". Seen: f1/p05-say-tap.png. **nit**, family:letter-pals.

Cheap passes tried: tapping every lantern in Find (wrong taps just repeat, first meetings never score; checks reset
the streak), every picture in Sign (each wrong one names itself, which teaches), every lantern in Twins ("same"
line), scribbling, tapping and tracing backward on the slate (all fail, three fails auto-finish without a free pass).
Only Twins (finding 3) can be passed without reading. Nothing cultural, Native or hard-history to flag.

Counts: blocker 0, should fix 7, polish 7, nit 1.

## Audit pilot

- Leads confirmed: Read the street on an asleep street says "still asleep" (finding 7, with the welcome and hint
  around it).
- Leads not reported (BASELINE rule 16): welcome not heard after a first tap on Teacher, a cart lantern or a quick
  double tap on Wake or Village. The premise is not needed later, and the Find question is in Read.
- Clean rows I relied on: every size and state clean for targets, fold and overlaps; Motion off clean; resize
  mid-action clean.
- Missed by the audit: the unspoken "Tap Next." in Say (it logs the dropped placeholder, not a missing line), the
  intro/say order, the twins window giveaway, the I/l and double-story a on banners, glow levels unreadable at a
  glance, the Village string vanishing below 800 px, the 760x900 floating lantern, and the end card.
