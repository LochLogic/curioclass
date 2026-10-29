PASS

# Final look sensitivity review: career-cluster-explorer

Fresh cold review, 2026-10-29, against BASELINE.md (rules 4, 5, 6), STANDARDS.md and REFINE.md (Sensitivity agent,
Final look). Read refine/sensitivity.md, spec.md, handoff.md, notes.md, src.html, careers.json (all 93 careers, every
does / path / try line), voice/lines.json and voice/local.json. Drove the bundle (career-cluster-explorer.html) with
scripts/drive.py on Chrome port 9251 at 1366x768 and 1920x1080: cards for braids, help, police, kids, clinic, food,
hardware and truck; sheets for doctor, chef, stylist, home-aide, childcare, police, retail, mover, cook and
social-worker; ladders for health, edu, hosp and public; the full town. Frames and text log in
S:/CurioClass-codex-scratch/final/career-cluster-explorer-sens/ (out/, run1.txt). No console errors in 23 shots. Chrome
closed after the run (no process left on the profile).

Counts: blockers 0, should fix 0, polish 0, nit 1.

## Earlier fixes: all still fixed

Checked in careers.json, src.html and the bundle text (old strings count 0, new strings count 1), and on screen:

1. People emoji: Family Doctor 🧑‍⚕️, Chef 🧑‍🍳, Hairstylist ✂️. The clinic and food truck cards (out/card-clinic.png,
   out/card-food.png) and the health ladder (out/ladder-health.png) draw the gender-neutral figures in default yellow.
   No 👩‍⚕️, 👨‍🍳 or 💇 anywhere in the bundle.
2. Police figure head is `#c9c3ea` (src.html line 693, and the bundle). It reads as a lavender silhouette like the rest
   of the town (out/card-police.png, out/scene-full.png).
3. Fashion Designer 🧵 (no 👗 in the bundle).
4. Musician "places of worship" (no "churches").
5. Hotel Manager "Plan a pretend weekend trip and compare three places to stay online." (no "family trip").

## New since that review: checked, fine

- **The 10 careers added in polish round 1** (Administrative Assistant, Retail Sales Worker, Computer Research
  Scientist, Childcare Worker, Teacher Assistant, Home Health Aide, Bookkeeper, Warehouse Worker, Drafter,
  Environmental Technician) were not in the first review. Each does line is plain and respectful ("Helps older adults
  and people with disabilities with daily care in their homes"; "Helps customers find what they need..."). Paths say
  what the Handbook says without ranking words ("no diploma is needed to start"). Emoji are all objects (📎 🛍️ 🧮 🧩 ✏️
  🏠 📒 🏷️ 📏 💧). Childcare's try line keeps a grown-up nearby.
- **Low-pay care and service jobs** (home aide, childcare, teacher assistant, hairstylist, cook, retail, warehouse) sit
  in the "No degree needed" or "Certificate or some college" columns at $35k to $37k. That is the BLS fact, shown on the
  same $0 to $250,000 scale as every job, with no "low" or "entry" label and the "many also have other ways in" key. The
  health ladder puts Home Health Aide beside Dental Hygienist ($98,100, associate's) and Paramedic, so a column is not a
  class marker. Rule 5: plain, with the human side. Fine.
- **Which jobs sit together:** Home Health Aide joined the community help booth (counselor, social worker,
  psychologist); it is human services, and the booth line stays non-clinical. Hairstylist moved to Healthcare and Human
  Services (Advance CTE 2024, Personal Care Services, per sources.md); the braids booth itself is unchanged and still
  ties the job to no group. The kids' corner (teacher, preschool, teacher assistant, childcare) and the clinic hold
  gender-neutral titles and object emoji, so no card casts a gender.
- **Words:** no gendered pronouns or nouns (he, she, his, her, man, woman, guy, girl, boy) in src.html or careers.json;
  no em dashes in src.html, careers.json, lines.json or the bundle. Rule 6 passes. No cultural, Native or hard-history
  content anywhere: Maple Bend and its harvest night are made up, and no line names a culture, faith or group.
- **Drawn people:** the town has one person, the crosswalk officer. The kids' corner circles are craft items on a table
  (src.html lines 659-660), the stage and field have no players drawn. No art files.
- **Voice, real clips.** All nine lines are neutral how-to and event lines; none comments on a job, a pay level or a
  choice, and "from no degree to grad school" names the ladder's columns without judging them. The Final look's Whisper
  pass matched every clip to its text. My own liveliness run (scripts/voice_liveliness.py) and a pitch contour of lines
  3, 6 and 8: deliveries are upbeat and moving (semitone SD 2.98 to 7.94). Line 3 ("All fourteen lanterns are lit...")
  has the widest range (29.6), from a celebratory rise on "One night" plus two 60 Hz breath frames that inflate the
  number; that fits a finish line. Line 4 is the flattest (2.98) and is a plain instruction. No take reads as sarcastic
  or dismissive from these readings. I judged delivery from transcript, pitch and rate, not by ear.

## Finding

1. **nit (general)**, careers.json via scripts/careers_data.py: two try lines assume a home or a car a student may not
   have: solar "Track how much sun your house gets in a day." and auto-tech "Learn to check a car's oil and tire
   pressure." How seen: reading all 93 try lines. Better: "Track how much sun one window or yard spot gets in a day."
   and "Learn how to check a car's oil and tire pressure (a video works too)." The same kind of fix as the first
   review's Hotel Manager line; optional.

Nothing else found. The finished tool keeps every fix the first review asked for, and the recorded voice adds nothing
that reads as mocking or dismissive.
