# API Playground

## One idea
A made-up town's open-data APIs answer inside the page like real ones (status codes, headers, JSON, a 404 for a stop that doesn't exist, a 429 when you call too fast), and every response you poke in the console can be snapped, as the same call written as a module function, into a working phone app whose pipeline shows the value at every step from response to screen.

## Not like
- sorting-showdown, data-policy-council (9-12, same group): measuring fixed algorithms, and a policy roleplay. Here you build, freely, with no right answer.
- network-architect (9-12 CS): designs the network the data travels on. Here the network is invisible; you work at the level of requests, responses and functions.
- capture-the-flag (9-12 CS): breaks into made-up systems on purpose. Here every call is an ordinary, polite request, and the only "attack" is calling too fast, which the server answers with 429.
- game-remix (grade 5): changes values in a finished game. Here you assemble a small app from library calls and see data flow through it.
- code-kitchen (6-8): writes procedures. Here the procedures already exist in modules with documentation; the skill is reading docs and composing calls.

## Who and how
- Grades 9 to 12, computer science. Module: Modular Programs and APIs (Algorithms and Programming), "Procedures, objects, libraries and documentation". Topic line: "calling APIs and building with modules".
- Driver: students on laptops, alone or in pairs.
- 20 to 40 minutes: Console with the docs (10 min), App with one idea card (15 min), own app (open).
- Standards (CSTA 2026, as listed): HS-PRO-PD-12, HS-PRO-PD-13, HS-PRO-RD-17. CSTA 2017 crosswalk (matched by topic): 3B-AP-16 (demonstrate code reuse by creating programming solutions using libraries and APIs), 3A-AP-17 (decompose problems into smaller components using procedures, modules and/or objects), 3A-AP-18 (create artifacts by using procedures within a program, combinations of data and procedures, or independent but interrelated programs).
- tool.json: driver "students", minutes "20-40", modes ["Console", "App"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`.

## Screens and modes
Header (kit): "API Playground", small line "Millbrook Open Data". Mode buttons: **Console** (opens first), **App**. Motion, Sound, Read.

Panel (both modes): `#hint`; **Morning** picker: **Sunny Monday** (default), **Rainy Tuesday**, **Windy Friday** (the data changes; the clock reads 7:20 am); the rate meter "Calls this minute: 4 of 30"; then the **Docs** drawer (Console: endpoints; App: modules), each entry with a **Try it** button.

### Mode 1: Console
Stage, top to bottom:
- **Request bar**: "GET" tag, the URL field (`https://api.millbrook.example/v1/...`, typed with autocomplete of paths and parameter names), **Send** (big). Under it the parameter form for the chosen endpoint (one field per parameter, required ones marked), kept in sync with the URL both ways. **Show as code** toggle: the same request as one line of JavaScript `fetch(...)` and of Python `requests.get(...)`, display only.
- **Response**: status line ("200 OK", "404 Not Found", with a ✓ or ✗ glyph), time ("180 ms"), **Headers** (collapsed: `Content-Type`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `Retry-After` on 429), and the body as a **Tree** (collapsible objects and lists, keys, typed values in color with quotes on strings) or **Raw** (pretty-printed JSON). Tapping a value shows its path ("arrivals[0].minutes") with **Use in app**.
- **History** (side strip): the last 20 requests (status and path); tap one to load it again.

### Mode 2: App
Stage: a **phone** (9:16, light screen) on the left showing up to four tiles, and the **pipeline editor** on the right for the selected tile.
- A tile = title, then a pipeline of cards, top to bottom. Each card's output feeds the next, and its value shows under it ("→ 6", "→ [3 items]", "→ {object}", tap to expand). The last card is **Show** ("Next bus in {} min", where {} is the value) or **Decide** ("if value > 40 show "Take the bus" else "Bike today"").
- **Add card** menu: a module call (Content), `get`, `first`, `count`, `where`, `min_of`, `max_of`, `round`, Show, Decide. Cards can be reordered (**Up**, **Down**) and removed (**Remove**).
- Buttons: **New tile**, **Delete tile**, **Refresh app** (re-runs every tile, which calls the APIs again and counts toward the rate limit), **Clear app**.
- **Ideas** cards in the panel (optional): each names a goal and the modules it needs; **Start it** adds an empty tile with that title.

## Content

Base URL `https://api.millbrook.example/v1` (`.example` is reserved and never resolves; the tool makes no network request). Every endpoint is GET.

Endpoints (docs text says what each does, its parameters, an example response and its errors):
- `/weather/now?zone=` zone required: north, south, river. Returns `{zone, time, temp_f, rain_chance, wind_mph, sky}`.
- `/weather/hourly?zone=&hours=` hours optional, 1 to 12, default 3. Returns `{zone, hours: [{time, temp_f, rain_chance, wind_mph}]}` from 08:00.
- `/transit/stops?near=` near optional: school, library, park (none lists all). Returns `{stops: [{id, name, walk_min}]}`.
- `/transit/arrivals?stop=` stop required. Returns `{stop, name, arrivals: [{route, to, minutes, crowding}]}`, crowding one of "seats", "standing", "full".
- `/bikes/stations?near=` near optional. Returns `{stations: [{id, name, bikes, docks}]}`.
- `/library/search?q=&limit=` q required (matches title or author, any case); limit optional 1 to 10, default 5. Returns `{count, results: [{title, author, year, copies, available}]}`.

Errors (JSON body `{error, message}`): 400 `missing_param` ("zone is required."); 400 `bad_value` ("hours must be 1 to 12.", "zone must be north, south or river."); 404 `not_found` for an unknown stop ("No stop with id S99.") or path ("No endpoint /weather/today. See the docs."); 429 `rate_limited` after 30 requests in any 60 seconds (this tool's own limit), with `Retry-After` in seconds and "Slow down. Try again in 12 seconds." Unknown parameters are ignored with a grey note under the status ("Unknown parameter zon was ignored."). Response times: 120 ms plus 20 ms per item returned, shown with a short spinner.

Data by morning (Monday / Tuesday / Friday):
- Weather now, `temp_f, rain_chance, wind_mph, sky`: north 54, 10, 6, clear / 48, 80, 12, rain / 58, 20, 24, cloudy. south 56, 5, 4, clear / 49, 75, 11, rain / 60, 15, 22, cloudy. river 51, 10, 9, clear / 46, 85, 14, rain / 55, 20, 31, cloudy.
- Hourly, hour k = 1 to 12 (08:00 to 19:00): temp_f = now + 2k (Monday) or now + k (Tuesday, Friday); wind as now. rain_chance: Monday 10 every hour; Tuesday 80, 80, 70, 60, 50, 40, 30, 30, 20, 20, 20, 20; Friday 20, 30, 30, 20, then 10.
- Stops: S12 "Oak and 5th" (near school, walk 4; near library, walk 7), S14 "Millbrook High Front" (near school, walk 1), S3 "Library Square" (near library, walk 2), S8 "River Park" (near park, walk 3).
- Arrivals at S12 (`route, to, minutes, crowding`): Monday 7 Millbrook High 6 seats, 2 Library Square 9 seats, 7 Millbrook High 21 seats. Tuesday 7 Millbrook High 11 standing, 2 Library Square 4 seats, 7 Millbrook High 19 full. Friday 7 Millbrook High 3 seats, 2 Library Square 14 seats, 7 Millbrook High 18 seats. S3 and S8 list the same three with minutes plus 5 and plus 8. S14 lists route 7 "Depot" at the route 7 minutes plus 4.
- Bike stations `bikes / docks`: B1 "School Gate" (near school) 6/12, 1/12, 3/12; B3 "Library Steps" (near library) 4/8, 7/8, 0/8; B5 "River Park" (near park) 9/10, 10/10, 2/10.
- Library (public-domain books; copies, available): Frankenstein, Mary Shelley, 1818 (2; Monday 1, Tuesday 0, Friday 2); Pride and Prejudice, Jane Austen, 1813 (3, 2); The Time Machine, H. G. Wells, 1895 (1, 1); The War of the Worlds, H. G. Wells, 1898 (2, 0); Treasure Island, Robert Louis Stevenson, 1883 (1, 1); Little Women, Louisa May Alcott, 1868 (2, 2); The Adventures of Tom Sawyer, Mark Twain, 1876 (2, 1); A Christmas Carol, Charles Dickens, 1843 (1, 0); Dracula, Bram Stoker, 1897 (2, 2); The Call of the Wild, Jack London, 1903 (1, 1); Narrative of the Life of Frederick Douglass, Frederick Douglass, 1845 (2, 2); The Secret Garden, Frances Hodgson Burnett, 1911 (1, 1).

Modules (the same data as functions; docs list each with parameters and return value): `weather.now(zone)`, `weather.hourly(zone, hours=3)`, `transit.stops(near)`, `transit.arrivals(stop)`, `bikes.stations(near)`, `library.search(q, limit=5)`. A module call returns the response body; an error stops the pipeline at that card with the status and message. `util`: `get(path)` (a field or path like `arrivals[0].minutes`), `first`, `count`, `where(field, op, value)` (op =, !=, >, <, >=, <=), `min_of(field)` and `max_of(field)` (the item with the smallest or largest field), `round`.

Ideas: "Next bus to school" (transit, util), "Bike or bus?" (weather), "Is my book in?" (library), "Bikes near the library" (bikes), "Rain later?" (weather.hourly, max_of). Example pipeline, Next bus: `transit.arrivals("S12")` → `get("arrivals")` → `where("to", "=", "Millbrook High")` → `min_of("minutes")` → `get("minutes")` → Show "Next bus in {} min" (Monday 6, Tuesday 11, Friday 3).

## Interactions in detail
- Opens on Console with `/weather/now?zone=north` in the bar, not sent. The Docs drawer is open at Weather.
- Send with a missing required parameter still sends (the server answers 400), so students meet real errors; the form marks the field after.
- Rate limit: requests in the last 60 seconds of real time; Refresh app counts one call per tile. While limited, Send stays enabled and every call returns 429 with the seconds left; the meter turns warn-colored and counts down.
- A get with a missing field stops at that card: "No field minute. Fields here: route, to, minutes, crowding."; a get on a list: "This is a list. Use first, or where." Values over 200 characters truncate with "more".
- Changing Morning re-runs the app's tiles (counted calls) but not the console.
- Use in app (from the console) adds a tile with that call and a `get` of that path.
- The app (tiles and pipelines) is saved on this device in localStorage `curio-api-playground` (try/catch); Clear app asks first. History is for the page load only.
- Extremes: 4 tiles, 8 cards per tile; URL field 300 characters.
- Motion off: no spinner rotation (a "Waiting..." label instead) and no card slide.
- Sizes: at 1366x768 the request bar, Send and the status line are on screen with the body scrolling in its own box; in App the phone and the selected pipeline both show. At 760 wide the panel goes below; at 375 wide App shows the phone or the pipeline with a **Phone / Pipeline** switch, and the docs open as a sheet.
- Keyboard: Enter in the URL field sends; Up and Down walk History when the field is empty; tree nodes expand with Right and Left.
- `window.__tool = {state, setMode, setMorning(id), request(url), runApp(), app(), setApp(json)}` for tests.

## Look
- Accent `--brand #ffd75e` (lemon: Send, the header rule, the selected tile) with `--brand-ink #1c1203`, on `kit:theme-912`.
- Console body on `#0b1017` in the readout font: keys `#9ecbff`, strings `#a5e3a1` (with quotes), numbers `#ffb38a`, true, false and null `#d2a8ff`. Status: 2xx `--ok` with ✓, 4xx `--warn` with ✗ and the code number.
- Phone: dark bezel, screen `#f7f7f2`, tile text `#1c2330`, tiles with a lemon top edge.
- Contrast (computed): brand on `--panel` 12.47:1, on `--sec-bg` 11.82:1; brand-ink on brand 13.31:1; keys 11.30:1, strings 12.81:1, numbers 10.96:1, booleans 9.80:1 on `#0b1017`; ok 11.32:1, warn 11.51:1 there; phone ink on screen 14.67:1. All pass AA. Type is never shown by color alone (quotes, words, glyphs).
- Neighbors: sorting-showdown violet, data-policy-council light navy paper, network-architect sky blue, capture-the-flag pink.

## Art
none: drawn in code (phone, tiles, weather and bus icons, preview.svg).

## Voice
Bank voice `casual-peer` (Zubenelgenubi), "Say casually and naturally, like a friendly teenager explaining something", here a classmate who builds apps. Not used by any group sibling or 9-12 CS neighbor. JSON, docs and messages are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-console (how, Console welcome): "This is the town's data. Press Send and see what comes back."
- tree (how, first 200 response): "Tap any value to see its path. That's how you'll grab it in your app."
- e400 (how, first 400): "A 400 means the request was missing something. The docs list what each call needs."
- e404 (how, first 404): "A 404 means that thing doesn't exist. Check the id or the path."
- e429 (event, each new 429 streak; stale when the limit clears): "Too many calls. The server says wait, so wait."
- w-app (how, App welcome): "Pick an idea, or press New tile. Each card's answer feeds the next one."
- stopped (event, a pipeline stops on a card; stale on the next edit): "The pipeline stopped. Read the note on that card."
- morning (how, first Morning change in App): "Same app, new morning. The data changed, your code didn't."

## Family engine
none

## Sources
- CSTA 2026 ids HS-PRO-PD-12, HS-PRO-PD-13, HS-PRO-RD-17 (`data/standards/csta-2026-ids.txt`); CSTA K-12 CS Standards (2017) 3A-AP-17, 3A-AP-18, 3B-AP-16: https://csteachers.org/k12standards/
- What an API is, requests and responses: MDN Web Docs, "Introduction to web APIs", https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction
- Status codes 200, 400 and 404, GET: RFC 9110, HTTP Semantics, https://www.rfc-editor.org/rfc/rfc9110
- 429 Too Many Requests and Retry-After: RFC 6585, section 4, https://www.rfc-editor.org/rfc/rfc6585#section-4
- Rate limit headers are a convention, not yet a standard: IETF draft "RateLimit header fields for HTTP", https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
- JSON format: RFC 8259, https://www.rfc-editor.org/rfc/rfc8259
- `.example` is reserved for documentation: RFC 2606, https://www.rfc-editor.org/rfc/rfc2606
- `fetch` and Python `requests.get` forms: MDN "Using the Fetch API", https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch ; Requests quickstart, https://requests.readthedocs.io/en/latest/user/quickstart/
- Book titles, authors and first publication years: each title's entry at Project Gutenberg, https://www.gutenberg.org (all public domain in the US).
- Millbrook, its weather, stops, buses, bikes, copies and the 30-per-minute limit are original to Curio Class.

## Done when
1. `/weather/now?zone=north` on Sunny Monday returns 200 with temp_f 54, rain_chance 10; Rainy Tuesday 48, 80.
2. Missing zone returns 400 missing_param; zone=east 400 bad_value; stop=S99 404; `/weather/today` 404; each with the message in Content.
3. The 31st request inside 60 seconds returns 429 with Retry-After, the meter counts down, and calls succeed again after it.
4. URL and form stay in sync both ways; Show as code prints matching fetch and requests lines.
5. Tapping `minutes` in an arrivals response shows `arrivals[0].minutes`; Use in app makes a tile that shows that value.
6. The Next bus pipeline shows 6, 11 and 3 across the three mornings; a misspelled field stops at its card with the field list.
7. Bike or bus (`weather.now("north")` → `get("rain_chance")` → Decide > 40) shows "Bike today" Monday and "Take the bus" Tuesday.
8. The app survives a reload; Clear app (after Yes) empties it; nothing goes over the network (no requests in DevTools).
9. Every size in STANDARDS.md: Send and the status line (Console) and the phone or pipeline (App) visible without page scrolling.
10. Voice: welcome once per mode, how lines once then hint only, e429 each new streak; Read speaks the hint; console clean; the name only as "Curio Class".
