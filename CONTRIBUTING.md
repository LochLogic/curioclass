# Helping with Curio Class

Thank you for wanting to help. Curio Class is a free K-12 classroom toolkit: interactive tools, printables and
lessons for every standard, with no logins, no ads and no tracking. Please read this page before you start, so your
time goes into work that can actually ship.

## How decisions are made

Curio Class has one editor: Cory (GitHub: LochLogic). Cory sets the direction, approves every change and is the only
person who merges or deploys. That is not a judgment on anyone's skill; it is how a site for children stays
consistent and safe.

- **Direction lives in three files:** [docs/VISION.md](docs/VISION.md) (why Curio Class exists),
  [docs/ROADMAP.md](docs/ROADMAP.md) (what comes next, in order) and
  [docs/agents/decisions/BASELINE.md](docs/agents/decisions/BASELINE.md) (the standing rules for every call).
  Suggestions about them are welcome as an issue. Changes to them are Cory's alone.
- **Every tool goes through the same path,** whoever made it: Spec, Build, Self-check, Refine, Fix, Exit check, Art
  and voice, Finish check, then Cory's Sign-off. Nothing skips a step, including work by Cory's own helpers. We say
  the step's name, never just "review", so everyone knows which moment is meant.
- **"Not now" is common** and usually means "not yet in the roadmap's order", not "bad idea".

## Rules every contribution follows

1. **Kid safe.** No ads, no accounts, no tracking, no analytics, no chat between users, nothing that collects data
   about a child. Anything a tool saves stays on the device.
2. **Offline, single file.** Each tool is one HTML file that works with no internet. No outside scripts, fonts,
   images or servers. The safety scan (below) fails anything that reaches outside.
3. **Teaches well.** A tool exists to teach its standard well, and it has to be accurate. Cool comes second.
4. **Plain, honest words.** Say what a thing is. Practice tools are not diagnoses or grades.
5. **Original work.** No characters, names, art or levels taken from existing games, shows or brands.
6. **Respectful.** Cultures, languages and people are shown accurately and with permission where it matters.
   Sacred or community-owned material never goes in without that community's say.

## Ways to help (most wanted first)

- **Teachers and homeschool parents:** try tools with a lesson in mind and tell us what you would change. This is
  the most valuable help there is.
- **Playtesting with real kids:** watch a child use a tool and note where they got stuck or bored. Never send
  photos, names or recordings of children.
- **Subject experts:** check a tool's facts in your field (science, math, music, history, languages).
- **Art:** original illustration, or finding public domain pictures with a clear source.
- **Code:** fixes and scoped builds that Cory has agreed to first. Please open an issue and wait for a yes before
  building something new.

## Building a tool from a spec

This is where AI-assisted builders help most. Curio Class writes the spec and does the final check; you do
everything in between, with your own tools and our guides.

1. **Ask for a spec.** Open an issue saying you would like to build one. Cory assigns a tool whose spec is ready
   (`tools/<id>/spec.md`), so two people never build the same thing.
2. **Build it** to the spec, following [docs/TOOL-CONTRACT.md](docs/TOOL-CONTRACT.md) and the build brief in
   [docs/agents/CODEX-BUILD.md](docs/agents/CODEX-BUILD.md). Any AI assistant is fine.
3. **Self-check and fix it** using [docs/agents/CODEX-REVIEW.md](docs/agents/CODEX-REVIEW.md) and
   [docs/agents/CODEX-FIX.md](docs/agents/CODEX-FIX.md), until your Self-check finds nothing that blocks.
4. **Run the checks:** `python scripts/check_safety.py` and `python scripts/check_tools.py` must pass for your tool.
5. **Open a pull request** with the tool folder, your Self-check notes and the name of the AI tools you used. Curio
   Class then runs Refine and the Exit check. A tool that needs work comes back to you with notes for a Fix.

## How to send something

1. **Open an issue first** for anything bigger than a typo: an idea, a bug, a review of a tool. Say which tool
   (its folder name under `tools/`) and what you saw.
2. **For code or content:** fork the repository, make the change on a branch and open a pull request. Keep one
   change per pull request.
3. **Checks run on every pull request.** `python scripts/check_safety.py` must pass. If a tool truly needs a risky
   browser feature (for example a bundled library that contains network code it never calls), its `notes.md` needs
   a line starting `Safety:` that says why, and Cory reads every one.
4. **Cory reviews and merges** when it fits the roadmap. A pull request may wait, or be closed with a reason.

## Licensing and credit

- By sending a contribution you agree it is released under the Curio Class licenses: code under MIT
  ([LICENSE](LICENSE)), content (text, art, audio, lessons) under CC BY 4.0 ([LICENSE-CONTENT.md](LICENSE-CONTENT.md)).
- Send only work you have the right to give: your own, or public domain, or openly licensed with the source named.
- If you used an AI tool to make art, audio or text, say which one in the pull request. Do not imitate a living
  artist's style or a real brand.
- Contributors are thanked by name (or handle) in the credits if they want to be.

## Speaking for Curio Class

Please do not speak for Curio Class in public, contact schools or partners on its behalf, or describe yourself as
staff. "I helped with Curio Class" is welcome; anything beyond that, ask Cory first.

## Be kind

Be patient and generous with each other. Reviews are about the work, never the person. Harassment of any kind ends
your involvement.
