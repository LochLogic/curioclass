# Desk Dock

## One idea
The small helpers a teacher keeps open on the projector all day, in one calm tool: a timer, a sound board, a noise
meter and a group maker. It is the first tool on the Supply Closet's Teacher Desk shelf (docs/ROADMAP.md, Track 2).
Bigger desk tools (a game-show quiz board, classroom music) are separate tools on the same shelf later; the rule is
that anything used in a corner while something else runs belongs here, and anything that takes over the screen gets
its own tool.

This is a teacher utility, not a lesson: it teaches no standard and has no module. It lives on the Teacher Desk shelf,
not in the tool catalog.

## Who and how
- Any grade, K to 12. Driver: the teacher, on a projector or a classroom screen, often left open for a whole day.
- tool.json: driver "teacher", minutes "all day", modes ["Timer", "Sounds", "Noise", "Groups"], grades_label
  "Grades K-12", hook and outcome written for teachers.
- No voice: a teacher runs it, and spoken lines would interrupt a class. Sounds are only the ones a teacher presses or
  a timer ending.

## Look
- Clean and readable from the back of a room: very large numbers and names, high contrast, a calm palette (a soft desk
  wood or chalkboard tone is fine, never busy). Works in a small window beside other content and full screen.
- Kit frame (`kit:curio`) with a header holding the four mode buttons plus Sound and Motion. A "Big" button (or
  double-click) makes the current panel fill the screen; Esc returns.
- Each mode remembers its settings in localStorage (wrapped in try/catch), so a teacher's presets survive a reload.

## Modes

### Timer (opens first)
- Countdown with presets (1, 2, 3, 5, 10, 15, 20 minutes) and a custom entry (minutes and seconds). Start, pause,
  reset, and plus or minus one minute while running.
- A large digital readout plus a shrinking ring or bar; the last 10 seconds change color calmly (no flashing).
- End: a gentle chime (choice of three: chime, bell, soft beeps; or none), and the readout pulses once (still if
  Motion is off). A stopwatch toggle counts up instead.
- Optional label above the time ("Clean up", "Silent reading"), typed by the teacher.

### Sounds
- A grid of big buttons: applause, cheer, drumroll, ta-da, buzzer (wrong), ding (right), chime (attention), whistle,
  countdown beeps, and a soft "shh" swell. Every sound is synthesized in code with Web Audio (no audio files, no
  recordings, no licensing). Each sound is short (under 3 seconds) and never harsh or startling at default volume.
- A volume slider, and keys 1 to 0 trigger the buttons in order.

### Noise
- A noise meter from the microphone, shown as a big friendly level gauge with three zones (quiet, talking, too loud)
  and a teacher-set limit. When the level stays over the limit for 3 seconds, the gauge shows it (and an optional
  soft chime).
- Microphone use starts only when the teacher presses Start, the browser asks permission, and the screen says plainly:
  "The sound level is measured on this device. Nothing is recorded or sent." (BASELINE rule 7.) Stop releases the
  microphone. If permission is refused or there is no microphone, explain kindly and offer nothing else broken.

### Groups
- The teacher types or pastes a class list (one name per line); it is kept on this device only, with a Clear list
  button and the same privacy line.
- Make groups by number of groups or by group size; shuffle again; show groups as big named cards (Group 1, 2, ... or
  fun names from a small built-in list such as animals or colors).
- A "Pick one" button chooses a random name, without repeats until everyone has been picked (a reset starts over).
- Students can be marked absent for today with one tap so they are left out.

## Art
None required. Drawn-in-code icons for the sound buttons and modes. One small tasteful flourish in the header is fine.
No people.

## Done when
- All four modes work as written, by mouse, touch and keyboard, at every STANDARDS size and full screen.
- The microphone is never opened before Start, and Stop releases it.
- No network requests; class names never leave localStorage.
- The bundle is well under the 2 MB goal.
