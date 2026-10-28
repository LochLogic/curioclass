# The Word Wall diagrams, drawn by scripts/wordsvg.py: one "<module_id>/<slug> = <spec>" line per card,
# under a comment with the card's word and picture prompt. paint(...) hands the card to scripts/wordart.py.

# lines: a script page with lines highlighted
arts-3-5-characters-and-scenes/lines = page(240, lines=8, hl=(1, 2, 5))
# projection: sound waves reaching rows of seats
# gesture: a waving hand outline
arts-3-5-characters-and-scenes/gesture = wave_hand(220)
# color wheel: a twelve-part color wheel
arts-3-5-color-theory-and-mixing/color-wheel = pie(parts=[1] * 12, colors=['#e04848', '#f0582a', '#f08a24', '#f5a623', '#f5c33b', '#a8c83a', '#2f9e5b', '#1d9a9a', '#3a7bd5', '#5b4fc4', '#8e5bc4', '#c4479a'], size=280)
# tint: a red swatch and a pink swatch
arts-3-5-color-theory-and-mixing/tint = row(box(w=150, h=150, color=DARK, fill='#e04848', rx=20), arrow(70), box(w=150, h=150, color=DARK, fill='#f7a8b8', rx=20))
# shade: a blue swatch and a navy swatch
arts-3-5-color-theory-and-mixing/shade = row(box(w=150, h=150, color=DARK, fill='#3a7bd5', rx=20), arrow(70), box(w=150, h=150, color=DARK, fill='#1b2a5c', rx=20))
# complementary colors: a color wheel with red and green joined by a line
arts-3-5-color-theory-and-mixing/complementary-colors = over(pie(parts=[1] * 12, colors=['#e04848', '#f0582a', '#f08a24', '#f5a623', '#f5c33b', '#a8c83a', '#2f9e5b', '#1d9a9a', '#3a7bd5', '#5b4fc4', '#8e5bc4', '#c4479a'], size=280), raw(280, 280, '<line x1="140" y1="22" x2="140" y2="258" stroke="#1f2430" stroke-width="7"/><circle cx="140" cy="22" r="14" fill="#e04848" stroke="#1f2430" stroke-width="4"/><circle cx="140" cy="258" r="14" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/>'))
# abstract: overlapping colored circles
arts-3-5-famous-artists-and-movements/abstract = raw(300, 260, '<circle cx="110" cy="110" r="90" fill="#3a7bd5" opacity="0.75"/><circle cx="190" cy="120" r="80" fill="#f5c33b" opacity="0.75"/><circle cx="150" cy="180" r="70" fill="#e04848" opacity="0.75"/><circle cx="70" cy="200" r="45" fill="#2f9e5b" opacity="0.8"/>')
# form: three blocks labeled A, B, A
arts-3-5-form-and-composition/form = boxes('A', 'B', 'A', colors=[BLUE, ORANGE, BLUE], size=64, w=120, h=120)
# AB form: two blocks, blue then orange
arts-3-5-form-and-composition/ab-form = boxes('A', 'B', colors=[BLUE, ORANGE], size=64, w=140, h=140)
# ABA form: three blocks, blue, orange, blue
arts-3-5-form-and-composition/aba-form = boxes('A', 'B', 'A', colors=[BLUE, ORANGE, BLUE], size=64, w=120, h=120)
# compose: a pencil writing notes on a staff
arts-3-5-form-and-composition/compose = over(staff([2, 4, 3, 6], size=420), pencil(150), dx=150, dy=-30)
# repetition: the same pattern block repeated
arts-3-5-form-and-composition/repetition = row(*[row(shape('circle', 60, BLUE), shape('square', 60, ORANGE), shape('triangle', 60, GREEN), gap=6) for _ in range(3)], gap=20)
# contrast: a blue block next to an orange block
arts-3-5-form-and-composition/contrast = row(box(w=170, h=170, color=DARK, fill=BLUE, rx=20), box(w=170, h=170, color=DARK, fill=ORANGE, rx=20), gap=0)
# melody: notes climbing up a staff
arts-3-5-melody-and-scales/melody = staff([0, 2, 1, 4, 3, 6, 5, 8], size=440)
# scale: eight notes climbing like stairs
arts-3-5-melody-and-scales/scale = staff([-2, -1, 0, 1, 2, 3, 4, 5], size=440)
# solfege: stairs labeled do to ti
arts-3-5-melody-and-scales/solfege = stairs(7, 380, labels=['do', 're', 'mi', 'fa', 'sol', 'la', 'ti'], color=PURPLE)
# major scale: eight notes on a staff going up
arts-3-5-melody-and-scales/major-scale = staff([-2, -1, 0, 1, 2, 3, 4, 5], size=440)
# step: two notes side by side on a staff
arts-3-5-melody-and-scales/step = staff([2, 3], size=360, colors=[BLUE, ORANGE])
# leap: two notes far apart on a staff
arts-3-5-melody-and-scales/leap = staff([-1, 7], size=360, colors=[BLUE, ORANGE])
# sequence: eight numbered footprints
arts-3-5-patterns-in-dance/sequence = footprints(8, 60, numbered=True)
# formation: dots arranged in a circle
arts-3-5-patterns-in-dance/formation = raw(300, 300, ''.join(f'<circle cx="{150 + 110 * math.cos(k * math.pi / 4):.1f}" cy="{150 + 110 * math.sin(k * math.pi / 4):.1f}" r="22" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/>' for k in range(8)))
# count: numbers 1 to 8 in a row
arts-3-5-patterns-in-dance/count = col(row(*[T(n, 64, BLUE if n % 2 else ORANGE) for n in range(1, 5)], gap=30), row(*[T(n, 64, BLUE if n % 2 else ORANGE) for n in range(5, 9)], gap=30), gap=10)
# choreography: a page of footprints and arrows
arts-3-5-patterns-in-dance/choreography = box(col(row(footprint(50), arrow(60), footprint(50, angle=20)), row(arrow(60, dir='down'), footprints(2, 45)), row(footprint(50, angle=-30), curve_arrow(30), footprint(50)), gap=14, align='l'), color=DARK, fill='#fff')
# horizon line: a flat line between sky and ground
arts-3-5-perspective-and-space/horizon-line = raw(400, 260, '<rect x="0" y="0" width="400" height="140" fill="#d6e6fb"/><rect x="0" y="140" width="400" height="120" fill="#d3f0de"/><line x1="0" y1="140" x2="400" y2="140" stroke="#e04848" stroke-width="8"/><circle cx="320" cy="60" r="30" fill="#f5c33b" stroke="#1f2430" stroke-width="4"/>')
# overlap: three overlapping tree shapes
arts-3-5-perspective-and-space/overlap = raw(300, 220, f'{g(tree(150, "#1b6b3a"), 10, 40)}{g(tree(170, GREEN), 70, 30)}{g(tree(190, "#8fd18f"), 140, 20)}')
# staff: a five-line music staff
arts-3-5-reading-music/staff = staff([], size=440, clef=False)
# quarter note: a single quarter note
arts-3-5-reading-music/quarter-note = note('q', 240)
# half note: a single half note
arts-3-5-reading-music/half-note = note('h', 240)
# rest: a quarter rest symbol
arts-3-5-reading-music/rest = quarter_rest(240)
# time signature: a 4 over 4 on a staff
arts-3-5-reading-music/time-signature = staff([], size=440, time=(4, 4), w=300)
# measure: a staff divided by bar lines, one measure shaded
arts-3-5-reading-music/measure = staff([2, 4, 3, 4, 5, 2, 4, 1], size=440, bars_=(2, 4, 6), shade=(2, 4))
# frame: a filmstrip with a ball in each box
arts-6-8-animation-basics/frame = row(*[box(ball(50, RED), w=100, h=100, color=DARK, fill='#fff', rx=4) for _ in range(3)], gap=0)
# frame rate: a stopwatch beside a filmstrip
arts-6-8-animation-basics/frame-rate = row(clock(130, 12, 10, numbers=False), row(*[box(dot(30, RED), w=70, h=70, color=DARK, fill='#fff', rx=2) for _ in range(3)], gap=0), gap=20)
# timing: a ball bouncing: dots at equal time steps, close together at the top of each bounce
arts-6-8-animation-basics/timing = raw(420, 240, '<line x1="10" y1="222" x2="410" y2="222" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{30 + i * 19:.0f}" cy="{208 - h * (1 - (2 * u - 1) ** 2):.0f}" r="8" fill="#e04848" stroke="#1f2430" stroke-width="3"/>' for i, (h, u) in enumerate([(h, j / 7) for h in (180, 110, 60) for j in range(7)])))
# storyboard: six empty panels in a grid
arts-6-8-animation-basics/storyboard = grid([box(w=140, h=100, color=DARK, fill='#fff', rx=6) for _ in range(6)], 3, gap=14)
# squash and stretch: a ball flattening and stretching
arts-6-8-animation-basics/squash-and-stretch = row(shape('circle', 110, RED), raw(170, 70, '<ellipse cx="85" cy="40" rx="80" ry="30" fill="#e04848" stroke="#1f2430" stroke-width="5"/>'), raw(70, 170, '<ellipse cx="35" cy="85" rx="28" ry="78" fill="#e04848" stroke="#1f2430" stroke-width="5"/>'), gap=24)
# Cubism: a guitar made of overlapping angular shapes
arts-6-8-art-history-timeline/cubism = paint('a guitar made of overlapping flat angular shapes in brown and tan, in the style of cubist art')
# context: a framed artwork with its time, place and events around it
arts-6-8-art-history-timeline/context = col(row(col(clock(80), T('time', 26), gap=2), col(globe(80), T('place', 26), gap=2), col(calendar(80), T('events', 26), gap=2), gap=26), arrow(40, ORANGE, dir='down'), box(box(star(70), w=150, h=110, color=BROWN, fill=YELLOW, rx=2, sw=4), color=BROWN, fill=BROWN, rx=4, p=12), gap=8)
# movement phrase: a sequence of arrows in a line
arts-6-8-choreography/movement-phrase = row(*[arrow(70, color=c, dir=d) for c, d in ((BLUE, 'right'), (ORANGE, 'ur'), (GREEN, 'right'), (PURPLE, 'dr'), (RED, 'right'))], gap=4)
# motif: a spiral, a bigger spiral, then a turned and recolored spiral: one idea repeated and changed
arts-6-8-choreography/motif = row(*[raw(150, 150, f'<g transform="translate(75 75) rotate({r}) scale({k})"><path d="M0 0 a6 6 0 0 1 12 0 a12 12 0 0 1 -24 0 a18 18 0 0 1 36 0 a24 24 0 0 1 -48 0 a30 30 0 0 1 60 0" fill="none" stroke="{c}" stroke-width="{7 / k:.1f}" stroke-linecap="round"/></g>') for r, k, c in ((0, 1.2, BLUE), (0, 1.9, BLUE), (120, 1.2, ORANGE))], gap=18)
# canon: three staggered rows of the same shapes
arts-6-8-choreography/canon = col(*[row(Item(i * 60, 10, ''), shape('circle', 46, BLUE), shape('square', 46, ORANGE), shape('triangle', 46, GREEN), gap=8) for i in range(3)], gap=14, align='l')
# unison: identical shapes in a row
arts-6-8-choreography/unison = row(*[shape('star', 80, PURPLE) for _ in range(5)], gap=14)
# revise: a pencil and a circular arrow
arts-6-8-choreography/revise = row(pencil(150), curve_arrow(60, ORANGE), gap=20)
# one-point perspective: a hallway with lines meeting at a center dot
arts-6-8-drawing-and-one-point-perspective/one-point-perspective = raw(320, 260, '<rect x="5" y="5" width="310" height="250" fill="#eef0f4" stroke="#1f2430" stroke-width="5"/><rect x="110" y="90" width="100" height="80" fill="#fff" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#3a7bd5" stroke-width="4"/>' for a, b, c, d in ((5, 5, 110, 90), (315, 5, 210, 90), (5, 255, 110, 170), (315, 255, 210, 170))) + ''.join(f'<line x1="{a}" y1="{b}" x2="160" y2="130" stroke="#e04848" stroke-width="2" stroke-dasharray="6 5"/>' for a, b in ((110, 90), (210, 90), (110, 170), (210, 170))) + '<circle cx="160" cy="130" r="9" fill="#e04848"/>')
# orthogonal lines: lines converging on one dot
arts-6-8-drawing-and-one-point-perspective/orthogonal-lines = raw(320, 220, '<line x1="0" y1="110" x2="320" y2="110" stroke="#8a8f9c" stroke-width="3"/>' + ''.join(f'<line x1="{x}" y1="{y}" x2="160" y2="110" stroke="#3a7bd5" stroke-width="5" stroke-linecap="round"/>' for x, y in ((10, 10), (90, 0), (230, 0), (310, 10), (10, 210), (90, 220), (230, 220), (310, 210))) + '<circle cx="160" cy="110" r="12" fill="#e04848" stroke="#1f2430" stroke-width="3"/>')
# value: a five-step gray scale
arts-6-8-drawing-and-one-point-perspective/value = row(*[box(w=80, h=110, color=DARK, fill=c, rx=0, sw=4) for c in ('#ffffff', '#c8cad0', '#8f939c', '#555a64', '#1f2430')], gap=0)
# shading: a shaded sphere with a cast shadow
arts-6-8-drawing-and-one-point-perspective/shading = raw(300, 240, '<defs><radialGradient id="sh" cx="0.35" cy="0.35" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="0.6" stop-color="#9aa0aa"/><stop offset="1" stop-color="#3b404a"/></radialGradient></defs><ellipse cx="190" cy="210" rx="110" ry="24" fill="#c8cad0"/><circle cx="130" cy="120" r="95" fill="url(#sh)" stroke="#1f2430" stroke-width="4"/>')
# cross-hatching: a square filled with crossing lines
arts-6-8-drawing-and-one-point-perspective/cross-hatching = raw(240, 240, '<clipPath id="ch"><rect x="5" y="5" width="230" height="230"/></clipPath><g clip-path="url(#ch)">' + ''.join(f'<line x1="{-240 + i * 20}" y1="0" x2="{i * 20}" y2="240" stroke="#1f2430" stroke-width="3"/><line x1="{i * 20}" y1="0" x2="{-240 + i * 20}" y2="240" stroke="#1f2430" stroke-width="3"/>' for i in range(25)) + '</g><rect x="5" y="5" width="230" height="230" fill="none" stroke="#1f2430" stroke-width="5"/>')
# blend: several sound waves merging
arts-6-8-ensemble-skills/blend = raw(420, 220, ''.join(f'<path d="M10 {40 + i * 40} ' + ' '.join(f'L{10 + t * 4:.0f} {40 + i * 40 + (110 - 40 - i * 40) * min(1, t / 60) + 22 * math.sin(t / 7 + i) * (1 - min(1, t / 60)):.1f}' for t in range(101)) + f'" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>' for i, c in enumerate((BLUE, ORANGE, GREEN, PURPLE))))
# balance: a level scale
arts-6-8-ensemble-skills/balance = scale_icon(300, ball(50, BLUE), ball(50, BLUE))
# cue: a raised baton
arts-6-8-ensemble-skills/cue = paint('a conductor baton raised in a hand, simple')
# harmony: stacked notes on a staff
arts-6-8-harmony-and-chords/harmony = staff([(0, 2, 4), (1, 3, 5), (2, 4, 6)], size=420)
# interval: two notes on a staff with a bracket
arts-6-8-harmony-and-chords/interval = staff([0, 4], size=360, bracket=(0, 1))
# triad: three stacked notes C, E, G
arts-6-8-harmony-and-chords/triad = staff([(-2, 0, 2)], size=320, labels=['C E G'], w=300)
# chord progression: four chord symbols with arrows
arts-6-8-harmony-and-chords/chord-progression = row(T('C', 64, BLUE), arrow(46), T('F', 64, ORANGE), arrow(46), T('G', 64, GREEN), arrow(46), T('C', 64, BLUE), gap=8)
# minor: an A minor chord stacked on a staff: A C E
arts-6-8-harmony-and-chords/minor = staff([(3, 5, 7)], size=320, labels=['A C E'], w=300)
# call and response: two speech bubbles taking turns
arts-6-8-music-around-the-world/call-and-response = col(bubble(dots(3, size=26, color=BLUE), color=BLUE, w=220, h=100), row(Item(80, 10, ''), bubble(dots(3, size=26, color=ORANGE), color=ORANGE, tail='right', w=220, h=100)), gap=0, align='l')
# composition: a frame with a winding path
arts-6-8-photography-and-framing/composition = raw(320, 240, '<rect x="5" y="5" width="310" height="230" rx="6" fill="#d3f0de" stroke="#1f2430" stroke-width="5"/><path d="M40 235 C80 170 250 180 210 120 C170 60 120 90 150 30" fill="none" stroke="#a0673a" stroke-width="16" stroke-linecap="round"/>' + g(tree(70), 230, 30))
# rule of thirds: a frame split by a 3 by 3 grid
arts-6-8-photography-and-framing/rule-of-thirds = raw(330, 250, '<rect x="5" y="5" width="320" height="240" rx="4" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="5" y="150" width="320" height="95" fill="#d3f0de"/><line x1="111.7" y1="5" x2="111.7" y2="245" stroke="#e04848" stroke-width="4"/><line x1="218.3" y1="5" x2="218.3" y2="245" stroke="#e04848" stroke-width="4"/><line x1="5" y1="85" x2="325" y2="85" stroke="#e04848" stroke-width="4"/><line x1="5" y1="165" x2="325" y2="165" stroke="#e04848" stroke-width="4"/><circle cx="218" cy="85" r="22" fill="#f5c33b" stroke="#1f2430" stroke-width="4"/><rect x="5" y="5" width="320" height="240" rx="4" fill="none" stroke="#1f2430" stroke-width="5"/>')
# balance: a seesaw with equal shapes on each side
arts-6-8-principles-of-design/balance = seesaw(320, shape('square', 60, BLUE), shape('square', 60, BLUE))
# contrast: a white shape on a black field
arts-6-8-principles-of-design/contrast = box(shape('star', 170, '#fff', fill='#fff'), w=300, h=260, color=DARK, fill=DARK, rx=4)
# unity: shapes sharing one color family
arts-6-8-principles-of-design/unity = grid([shape(k, 90, c) for k, c in (('circle', BLUE), ('square', '#1d5fa8'), ('triangle', '#7ab0ef'), ('star', '#3a7bd5'), ('rhombus', '#5d93db'), ('hexagon', '#2a5d9e'))], 3)
# blocking: a stage map with arrows
arts-6-8-scripts-and-staging/blocking = raw(320, 240, '<path d="M5 5 H315 L295 235 H25 Z" fill="#efdccb" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><circle cx="80" cy="180" r="16" fill="#3a7bd5"/><circle cx="240" cy="70" r="16" fill="#f08a24"/>' + '<path d="M96 172 Q160 120 220 80" fill="none" stroke="#e04848" stroke-width="6"/><path d="M226 76 l-20 2 l8 16 z" fill="#e04848"/><path d="M240 86 Q250 140 200 190" fill="none" stroke="#2f9e5b" stroke-width="6"/><path d="M194 196 l4 -20 l14 12 z" fill="#2f9e5b"/>')
# upstage: a stage seen from above; the part farthest from the audience is shaded
arts-6-8-scripts-and-staging/upstage = raw(320, 340, '<path d="M5 5 H315 L295 235 H25 Z" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M5 5 H315 L305 120 H15 Z" fill="#f08a24" opacity="0.65"/><path d="M5 5 H315 L295 235 H25 Z" fill="none" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="40" y="235" width="240" height="20" fill="#a0673a"/>' + ''.join(f'<circle cx="{40 + i * 30}" cy="{276 + r * 22}" r="9" fill="#8a8f9c"/>' for i in range(9) for r in range(2)) + '<text x="160" y="336" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#5a5f6c">audience</text>')
# downstage: a stage seen from above; the part nearest the audience is shaded
arts-6-8-scripts-and-staging/downstage = raw(320, 340, '<path d="M5 5 H315 L295 235 H25 Z" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M15 120 H305 L295 235 H25 Z" fill="#f08a24" opacity="0.65"/><path d="M5 5 H315 L295 235 H25 Z" fill="none" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="40" y="235" width="240" height="20" fill="#a0673a"/>' + ''.join(f'<circle cx="{40 + i * 30}" cy="{276 + r * 22}" r="9" fill="#8a8f9c"/>' for i in range(9) for r in range(2)) + '<text x="160" y="336" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#5a5f6c">audience</text>')
# key signature: a staff with two sharp signs
arts-9-12-music-theory/key-signature = staff([], size=440, sharps=2, w=300)
# modulation: a key signature of one sharp, then an arrow to a key of two sharps
arts-9-12-music-theory/modulation = col(staff([], size=300, sharps=1, w=220), arrow(50, ORANGE, dir='down'), staff([], size=300, sharps=2, w=220), gap=6)
# cadence: two chord symbols V → I
arts-9-12-music-theory/cadence = row(T('V', 100, ORANGE, font=MATHF), arrow(90), T('I', 100, BLUE, font=MATHF), gap=20)
# scale degree: a scale with numbered notes
arts-9-12-music-theory/scale-degree = staff([-2, -1, 0, 1, 2, 3, 4, 5], size=440, labels=list('12345678'))
# Roman numeral analysis: I IV V under a staff
arts-9-12-music-theory/roman-numeral-analysis = staff([(-2, 0, 2), (1, 3, 5), (2, 4, 6)], size=420, labels=['I', 'IV', 'V'])
# counterpoint: two melodic lines weaving
arts-9-12-music-theory/counterpoint = raw(420, 200, '<path d="M10 60 C80 10 120 150 200 90 S330 20 410 110" fill="none" stroke="#3a7bd5" stroke-width="8" stroke-linecap="round"/><path d="M10 140 C70 180 130 40 210 110 S340 190 410 70" fill="none" stroke="#f08a24" stroke-width="8" stroke-linecap="round"/>')
# two-point perspective: a box drawn with lines to two dots
arts-9-12-two-point-perspective-and-composition/two-point-perspective = raw(400, 260, '<line x1="0" y1="80" x2="400" y2="80" stroke="#8a8f9c" stroke-width="3"/><circle cx="12" cy="80" r="9" fill="#e04848"/><circle cx="388" cy="80" r="9" fill="#e04848"/>' + ''.join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="80" stroke="#e04848" stroke-width="2" stroke-dasharray="6 5"/>' for a, b, c in ((150, 120, 12), (150, 230, 12), (250, 120, 388), (250, 230, 388), (200, 130, 12), (200, 130, 388))) + '<path d="M150 120 L200 130 L250 120 L250 230 L200 245 L150 230 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M200 130 V245" stroke="#1f2430" stroke-width="5"/><path d="M150 120 L200 130 L250 120" fill="#3a7bd5"/>')
# horizon line: a horizontal line across a frame
arts-9-12-two-point-perspective-and-composition/horizon-line = raw(360, 240, '<rect x="5" y="5" width="350" height="230" rx="4" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="5" y="130" width="350" height="105" fill="#efdccb"/><line x1="5" y1="130" x2="355" y2="130" stroke="#e04848" stroke-width="8"/><rect x="5" y="5" width="350" height="230" rx="4" fill="none" stroke="#1f2430" stroke-width="5"/>')
# foreshortening: a cylinder pointing toward the viewer
arts-9-12-two-point-perspective-and-composition/foreshortening = raw(300, 260, '<path d="M30 110 L200 40 L200 220 L30 150 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><ellipse cx="30" cy="130" rx="12" ry="20" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><ellipse cx="200" cy="130" rx="60" ry="90" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>')
# focal point: a frame with one bright square
arts-9-12-two-point-perspective-and-composition/focal-point = raw(330, 250, '<rect x="5" y="5" width="320" height="240" rx="4" fill="#d9dbe2" stroke="#1f2430" stroke-width="5"/><rect x="30" y="160" width="40" height="40" fill="#8a8f9c"/><rect x="250" y="40" width="40" height="40" fill="#8a8f9c"/><rect x="60" y="40" width="34" height="34" fill="#8a8f9c"/><rect x="250" y="170" width="30" height="30" fill="#8a8f9c"/><rect x="190" y="110" width="56" height="56" fill="#f5c33b" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<line x1="{218 + 40 * math.cos(a):.1f}" y1="{138 + 40 * math.sin(a):.1f}" x2="{218 + 56 * math.cos(a):.1f}" y2="{138 + 56 * math.sin(a):.1f}" stroke="#f08a24" stroke-width="5" stroke-linecap="round"/>' for a in [k * math.pi / 4 for k in range(8)]))
# negative space: a vase outline that also shows two profiles
arts-9-12-two-point-perspective-and-composition/negative-space = raw(300, 280, '<rect x="5" y="5" width="290" height="270" fill="#1f2430"/><path d="M110 20 C70 20 120 70 90 90 C60 110 130 130 100 150 C70 170 60 230 110 262 H190 C240 230 230 170 200 150 C170 130 240 110 210 90 C180 70 230 20 190 20 Z" fill="#fff"/>')
# high: a music note at the top of a staff
arts-k-2-high-and-low-loud-and-soft/high = staff([8], size=380, w=300)
# dynamics: a hairpin growing from p (soft) to f (loud)
arts-k-2-high-and-low-loud-and-soft/dynamics = raw(460, 250, '<path d="M70 100 L390 30 M70 100 L390 170" fill="none" stroke="#1f2430" stroke-width="12" stroke-linecap="round"/><text x="10" y="122" font-family="Georgia, serif" font-size="70" font-style="italic" font-weight="700" fill="#3a7bd5">p</text><text x="404" y="122" font-family="Georgia, serif" font-size="70" font-style="italic" font-weight="700" fill="#e04848">f</text><text x="30" y="236" font-family="Segoe UI, Arial, sans-serif" font-size="36" font-weight="700" text-anchor="middle" fill="#3a7bd5">soft</text><text x="420" y="236" font-family="Segoe UI, Arial, sans-serif" font-size="36" font-weight="700" text-anchor="middle" fill="#e04848">loud</text>')
# line: a straight, a wavy and a zigzag line
arts-k-2-lines-shapes-and-colors/line = col(raw(360, 20, '<line x1="10" y1="10" x2="350" y2="10" stroke="#3a7bd5" stroke-width="10" stroke-linecap="round"/>'), raw(360, 50, '<path d="M10 25 ' + ' '.join(f'Q{10 + i * 85 + 42} {(-5 if i % 2 == 0 else 55)} {10 + (i + 1) * 85} 25' for i in range(4)) + '" fill="none" stroke="#f08a24" stroke-width="10" stroke-linecap="round"/>'), raw(360, 60, '<path d="M10 55 ' + ' '.join(f'L{10 + (i + 1) * 42.5} {5 if i % 2 == 0 else 55}' for i in range(8)) + '" fill="none" stroke="#2f9e5b" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>'), gap=40)
# shape: a heart, a star and a circle
arts-k-2-lines-shapes-and-colors/shape = row(heart(110), star(110), shape('circle', 110, BLUE), gap=20)
# primary colors: three paint blobs, red, yellow and blue
arts-k-2-lines-shapes-and-colors/primary-colors = row(*[raw(100, 90, f'<path d="M50 6 C78 4 96 26 92 50 C88 76 66 88 44 84 C20 80 4 62 8 40 C12 18 26 8 50 6 Z" fill="{c}" stroke="#1f2430" stroke-width="5"/>') for c in (RED, YELLOW, BLUE)], gap=20)
# secondary colors: three paint blobs, orange, green and purple
arts-k-2-lines-shapes-and-colors/secondary-colors = row(*[raw(100, 90, f'<path d="M50 6 C78 4 96 26 92 50 C88 76 66 88 44 84 C20 80 4 62 8 40 C12 18 26 8 50 6 Z" fill="{c}" stroke="#1f2430" stroke-width="5"/>') for c in (ORANGE, GREEN, PURPLE)], gap=20)
# pattern: a row of dots and lines repeating
arts-k-2-lines-shapes-and-colors/pattern = row(*[(dot(40, BLUE) if i % 2 == 0 else raw(14, 70, '<line x1="7" y1="5" x2="7" y2="65" stroke="#f08a24" stroke-width="10" stroke-linecap="round"/>')) for i in range(9)], gap=18)
# beat: a row of evenly spaced hearts
arts-k-2-steady-beat-and-rhythm/beat = row(*[heart(70) for _ in range(5)], gap=22)
# rhythm: long and short bars in a pattern
arts-k-2-steady-beat-and-rhythm/rhythm = row(*[raw(w, 50, f'<rect x="2" y="5" width="{w - 4}" height="40" rx="10" fill="{c}" stroke="#1f2430" stroke-width="4"/>') for w, c in ((140, BLUE), (60, ORANGE), (60, ORANGE), (140, BLUE), (60, ORANGE))], gap=10)
# short sound: a long bar above a short bar; the short one is circled
arts-k-2-steady-beat-and-rhythm/short-sound = col(raw(320, 60, '<rect x="5" y="5" width="310" height="50" rx="12" fill="#c9ced8" stroke="#1f2430" stroke-width="5"/>'), mark(raw(80, 60, '<rect x="5" y="5" width="70" height="50" rx="12" fill="#f08a24" stroke="#1f2430" stroke-width="5"/>')), gap=20, align='l')
# rest: a quarter rest music symbol
arts-k-2-steady-beat-and-rhythm/rest = quarter_rest(240)
# arrow: four direction arrows
computer-science-1-code-a-path/arrow = grid([arrow(90, BLUE, 'up'), arrow(90, ORANGE, 'right'), arrow(90, GREEN, 'down'), arrow(90, PURPLE, 'left')], 2, gap=40)
# path: a dotted path weaving around rocks on a grid
computer-science-1-code-a-path/path = raw(300, 300, ''.join(f'<rect x="{10 + c * 56}" y="{10 + r * 56}" width="56" height="56" fill="#fff" stroke="#c4c8d0" stroke-width="2"/>' for r in range(5) for c in range(5)) + ''.join(f'<path d="M{10 + c * 56 + 8} {10 + r * 56 + 48} L{10 + c * 56 + 20} {10 + r * 56 + 14} L{10 + c * 56 + 36} {10 + r * 56 + 10} L{10 + c * 56 + 50} {10 + r * 56 + 44} Z" fill="#9aa5b8" stroke="#1f2430" stroke-width="3"/>' for r, c in ((0, 2), (1, 0), (2, 2), (3, 4), (4, 1))) + '<path d="M38 38 H94 V150 H150 V94 H262 V206 H206 V262 H262" fill="none" stroke="#f08a24" stroke-width="8" stroke-dasharray="4 12" stroke-linecap="round"/><circle cx="38" cy="38" r="14" fill="#2f9e5b"/>' + g(star(36), 244, 244))
# debug: code with a red bug line found by a magnifier, then the fixed code with a check
computer-science-1-code-a-path/debug = row(over(code_lines(4, 200, hl=1, hl_color=RED), magnifier(80, inner=bug(40)), dx=130, dy=60), arrow(50), code_lines(4, 200, hl=1, hl_color=GREEN), check(60), gap=10)
# turn: a curved arrow turning left
computer-science-1-code-a-path/turn = curve_arrow(90, BLUE, start=40, end=-180, cw=False)
# log in: a login box with a key
computer-science-1-parts-of-a-computer/log-in = box(col(T('log in', 40), raw(220, 40, '<rect x="2" y="2" width="216" height="36" rx="8" fill="#fff" stroke="#1f2430" stroke-width="4"/>'), raw(220, 40, '<rect x="2" y="2" width="216" height="36" rx="8" fill="#fff" stroke="#1f2430" stroke-width="4"/><text x="16" y="30" font-size="30" font-family="Segoe UI" fill="#1f2430">• • • • •</text>'), key(100), gap=14), color=BLUE, fill='#fff')
# log out: a door with an arrow going out
computer-science-1-parts-of-a-computer/log-out = row(door(220), arrow(110, ORANGE, sw=12), gap=6)
# AI: a computer chip with a lightbulb
computer-science-1-what-is-ai/ai = chip(240, inner=lightbulb_on(100))
# pattern: a row of shapes that repeats
computer-science-1-what-is-ai/pattern = row(*[shape(k, 70, c) for k, c in (('circle', BLUE), ('square', ORANGE), ('triangle', GREEN)) * 2], gap=12)
# data: a stack of small picture cards
computer-science-1-what-is-ai/data = raw(260, 220, ''.join(f'<g transform="translate({20 + i * 14} {10 + i * 18}) rotate({-8 + i * 5} 80 60)"><rect x="0" y="0" width="160" height="120" rx="10" fill="#fff" stroke="#1f2430" stroke-width="5"/><rect x="14" y="14" width="132" height="70" rx="5" fill="{c}"/><circle cx="50" cy="44" r="14" fill="#fff" opacity="0.8"/></g>' for i, c in enumerate(('#d6e6fb', '#fde3c8', '#d3f0de', '#e8dcf5'))))
# guess: a computer screen with a question mark
computer-science-1-what-is-ai/guess = screen(260, inner=T('?', 120, BLUE))
# mistake: a red X on a picture card
computer-science-1-what-is-ai/mistake = over(card(sized(cat_icon(100), 110), 180, 220), cross(80), dx=55, dy=-70)
# digital footprint: a footprint made of tiny dots
computer-science-2-input-and-output/digital-footprint = raw(170, 260, ''.join(f'<circle cx="{x}" cy="{y}" r="6.5" fill="#3a7bd5"/>' for x in range(8, 170, 16) for y in range(8, 260, 16) if ((x - 85) / 56) ** 2 + ((y - 170) / 86) ** 2 < 1 or (x - 40) ** 2 + (y - 40) ** 2 < 400 or (x - 82) ** 2 + (y - 26) ** 2 < 230 or (x - 118) ** 2 + (y - 36) ** 2 < 180 or (x - 146) ** 2 + (y - 62) ** 2 < 130))
# loop: a circular arrow around a jump icon
computer-science-2-loops-and-events/loop = curve_arrow(100, BLUE, start=-70, end=230, inner=raw(100, 100, '<path d="M20 80 Q50 -10 80 80" fill="none" stroke="#f08a24" stroke-width="9" stroke-linecap="round"/><path d="M70 72 l12 12 l2 -18 z" fill="#f08a24"/>'))
# repeat: a circular arrow with the number 3
computer-science-2-loops-and-events/repeat = curve_arrow(100, BLUE, start=-70, end=230, text='3')
# event: a green flag with a pointer
computer-science-2-loops-and-events/event = row(flag(170, GREEN), pencil(0) if False else raw(80, 110, '<path d="M10 10 L10 90 L30 72 L44 104 L58 98 L44 66 L70 66 Z" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), gap=0, align='b')
# sequence: two code blocks stacked in order
computer-science-2-loops-and-events/sequence = col(T('1', 40), code_blocks(1, 260, colors=(BLUE,)), T('2', 40), code_blocks(1, 260, colors=(ORANGE,)), gap=6)
# code: stacked colorful code blocks
computer-science-2-loops-and-events/code = code_blocks(4, 300)
# train: a stack of cat picture cards going into a computer
computer-science-2-teach-the-machine/train = row(col(*[card(cat_icon(70), 130, 100, ORANGE) for _ in range(3)], gap=-60), arrow(80), screen(190), gap=10)
# label: picture cards with name tags
computer-science-2-teach-the-machine/label = row(*[col(card(ic(80), 130, 130, c), box(T(w, 28), color=c, p=8)) for ic, w, c in ((cat_icon, 'cat', ORANGE), (dog_icon, 'dog', BROWN), (bird, 'bird', BLUE))], gap=18)
# model: a computer screen with a cat outline and a check
computer-science-2-teach-the-machine/model = screen(260, inner=row(cat_icon(100, '#fff'), check(80), gap=10))
# data: a big stack of picture cards
computer-science-2-teach-the-machine/data = col(*[card(sized(ic(60), 60), 200, 80, c) for ic, c in ((cat_icon, ORANGE), (dog_icon, BROWN), (bird, BLUE), (fish, ORANGE), (cat_icon, PURPLE))], gap=-40)
# fair: a level balance scale
computer-science-2-teach-the-machine/fair = scale_icon(300)
# search engine: a screen with a search box and a magnifying glass
computer-science-3-how-we-use-the-internet/search-engine = browser(300, search=True)
# loop: a circular arrow around a step-forward arrow
computer-science-3-if-this-then-that/loop = curve_arrow(100, BLUE, start=-70, end=230, inner=arrow(90, ORANGE, sw=12))
# variable: a box labeled score holding the number 7
computer-science-3-variables-in-programs/variable = col(box(T('7', 110, BLUE), w=170, h=150, color=ORANGE, fill='#fff'), T('score', 50, ORANGE), gap=8)
# value: the number 10 dropping into a box
computer-science-3-variables-in-programs/value = col(T('10', 90, BLUE), arrow(60, DARK, 'down'), box(w=170, h=120, color=ORANGE, fill='#fff', dashed=True), gap=6)
# table: a simple grid table
computer-science-4-tables-and-visualizations/table = table(4, 3, size=320)
# row: a table with one row highlighted
computer-science-4-tables-and-visualizations/row = table(4, 3, size=320, hl_row=2)
# column: a table with one column highlighted
computer-science-4-tables-and-visualizations/column = table(4, 3, size=320, hl_col=1)
# visualization: a bar chart
computer-science-4-tables-and-visualizations/visualization = bars([3, 5, 2, 4], size=320, colors=[BLUE, ORANGE, GREEN, PURPLE], axis=True)
# chart: a line chart with sun icons
computer-science-4-tables-and-visualizations/chart = over(plot(lambda x: 1.5 + 0.9 * x - 0.06 * x * x, size=320, xr=(0, 10), yr=(0, 7), axes=True, points=[(x, 1.5 + 0.9 * x - 0.06 * x * x, ORANGE) for x in (1, 3, 5, 7, 9)]), sun(70), dx=100, dy=-110)
# sort: bars out of order, then the same bars sorted shortest to tallest
computer-science-4-tables-and-visualizations/sort = col(bars([4, 2, 5, 1, 3], size=300, color=GRAY), arrow(50, dir='down'), bars([1, 2, 3, 4, 5], size=300, color=BLUE), gap=6)
# trace: an arrow moving down lines of code
computer-science-4-trace-the-code/trace = code_lines(6, 300, arrow_at=3)
# variable: a box labeled score holding 0
computer-science-4-trace-the-code/variable = col(box(T('0', 110, BLUE), w=170, h=150, color=ORANGE, fill='#fff'), T('score', 50, ORANGE), gap=8)
# value: a box with the number 5
computer-science-4-trace-the-code/value = box(T('5', 130, BLUE), w=190, h=170, color=ORANGE, fill='#fff')
# update: a box with 4 crossed out and 5 written
computer-science-4-trace-the-code/update = box(row(T('4', 110, GRAY, strike='4'), T('5', 110, BLUE), gap=30), w=280, h=170, color=ORANGE, fill='#fff')
# comment: code with a gray # comment line that the computer skips
computer-science-4-trace-the-code/comment = code_lines(5, 300, comment=2, skip=True)
# output: a screen showing a star
computer-science-4-trace-the-code/output = screen(280, inner=star(120))
# bias: a tilted balance scale
computer-science-4-training-data-matters/bias = scale_icon(300, ball(50, BLUE), ball(50, ORANGE), tilt=18)
# prediction: a computer screen with a cat icon and a question mark
computer-science-4-training-data-matters/prediction = screen(280, inner=row(cat_icon(100), T('?', 110, BLUE), gap=10))
# accuracy: ten circles, nine checked
computer-science-4-training-data-matters/accuracy = grid([over(shape('circle', 70, GREEN if i < 9 else RED), check(46, '#fff') if i < 9 else cross(40, '#fff')) for i in range(10)], 5)
# pattern: repeated shapes with one circled
computer-science-4-training-data-matters/pattern = row(shape('circle', 70, BLUE), shape('square', 70, ORANGE), shape('circle', 70, BLUE), shape('square', 70, ORANGE), mark(shape('circle', 70, BLUE)), gap=10)
# network: computers joined by lines
computer-science-4-wired-wireless-and-login/network = network(320, 5)
# authentication: a key going into a screen lock
computer-science-4-wired-wireless-and-login/authentication = row(key(130), arrow(50), screen(200, inner=lock(80)), gap=6)
# authorization: a door with a green check
computer-science-4-wired-wireless-and-login/authorization = door(240, sign=check(100))
# empathy: two hearts linked
computer-science-5-human-centered-design/empathy = row(heart(130), chain(1, 60), heart(130, PINK), gap=-14)
# feedback: speech bubbles with stars
computer-science-5-human-centered-design/feedback = row(bubble(row(star(36), star(36), star(36), gap=4), color=BLUE), bubble(row(star(36), star(36), gap=4), color=ORANGE, tail='right'), gap=14)
# iterate: a circular arrow with a pencil
computer-science-5-human-centered-design/iterate = over(curve_arrow(110, ORANGE), pencil(130))
# remix: two code blocks mixing into a new one
computer-science-5-remix-a-program/remix = row(col(code_blocks(1, 120, colors=(BLUE,)), code_blocks(1, 120, colors=(ORANGE,)), gap=30), arrow(70), code_blocks(2, 160, colors=(BLUE, ORANGE)), gap=14)
# modify: a slider being moved
computer-science-5-remix-a-program/modify = col(slider(320, 0.7), arrow(80, BLUE, 'right'), gap=6)
# debug: a magnifying glass over a ladybug
computer-science-5-remix-a-program/debug = magnifier(260, inner=raw(80, 80, '<ellipse cx="40" cy="46" rx="30" ry="28" fill="#e04848" stroke="#1f2430" stroke-width="4"/><circle cx="40" cy="20" r="12" fill="#1f2430"/><line x1="40" y1="20" x2="40" y2="74" stroke="#1f2430" stroke-width="3"/><circle cx="28" cy="40" r="5" fill="#1f2430"/><circle cx="52" cy="40" r="5" fill="#1f2430"/><circle cx="30" cy="60" r="5" fill="#1f2430"/><circle cx="50" cy="60" r="5" fill="#1f2430"/>'))
# test: a play button with a check
computer-science-5-remix-a-program/test = row(raw(150, 150, '<circle cx="75" cy="75" r="70" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><path d="M58 44 L112 75 L58 106 Z" fill="#fff"/>'), check(130), gap=20)
# attribution: a block program, a remix of it, and a credit tag pointing back to the first coder
computer-science-5-remix-a-program/attribution = row(col(code_blocks(3, 140), T('Ana', 30, BLUE), gap=6), arrow(60, ORANGE, 'left'), col(code_blocks(4, 160, colors=(BLUE, ORANGE, GREEN, RED)), tile('by Ana', ORANGE, 46), gap=6), gap=10)
# integrity: a document with a seal
computer-science-5-the-cia-triad/integrity = row(page(220, lines=7), raw(110, 110, '<circle cx="55" cy="55" r="44" fill="#e04848" stroke="#1f2430" stroke-width="5"/><circle cx="55" cy="55" r="30" fill="none" stroke="#fff" stroke-width="4"/><path d="M35 96 L28 120 L44 112 L55 124 L55 98 Z M75 96 L82 120 L66 112 L55 124 L55 98 Z" fill="#e04848" stroke="#1f2430" stroke-width="3"/>'), gap=-50, align='b')
# availability: a server with a green light
computer-science-5-the-cia-triad/availability = server(260, GREEN)
# cybersecurity: a shield over a laptop
computer-science-5-the-cia-triad/cybersecurity = col(shield(130, BLUE, inner=check(70, '#fff')), screen(230, laptop=True), gap=-20)
# encryption: letters turning into scrambled symbols with a key
computer-science-5-the-cia-triad/encryption = col(tiles('C', 'A', 'T', color=BLUE), row(arrow(60, dir='down'), key(90), gap=10), tiles('#', '&', '%', color=PURPLE), gap=10)
# label: a photo card with a tag
computer-science-5-train-a-classifier/label = row(card(sun(80), 150, 180), raw(130, 70, '<path d="M4 35 L30 6 H124 V64 H30 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><circle cx="30" cy="35" r="7" fill="#fff" stroke="#1f2430" stroke-width="3"/>'), gap=-10)
# confidence: a meter at 90 percent
computer-science-5-train-a-classifier/confidence = meter(320, 0.9, '90%')
# algorithm: a flowchart
computer-science-6-8-algorithms-and-fairness/algorithm = flowchart(330, ('Start', '?', 'Yes', 'No'))
# algorithmic bias: a computer flowchart feeding a scale that comes out uneven
computer-science-6-8-algorithms-and-fairness/algorithmic-bias = row(flowchart(200), arrow(50), scale_icon(230, dots(3, 3, 22, ORANGE, gap=4), dot(22, BLUE), tilt=18), gap=10)
# ethics: a balance with a question mark
computer-science-6-8-algorithms-and-fairness/ethics = scale_icon(300, qmark(60), qmark(60, ORANGE))
# transparency: a glass box with gears inside
computer-science-6-8-algorithms-and-fairness/transparency = box(row(gear(90), gear(70, YELLOW), gap=-6), w=260, h=200, color=BLUE, fill='#eaf4ff')
# recommendation: a phone with a star-marked music tile
computer-science-6-8-algorithms-and-fairness/recommendation = phone(280, inner=col(box(col(raw(50, 50, '<circle cx="18" cy="38" r="10" fill="#1f2430"/><line x1="27" y1="38" x2="27" y2="6" stroke="#1f2430" stroke-width="5"/><line x1="27" y1="6" x2="44" y2="12" stroke="#1f2430" stroke-width="5"/>'), star(40), gap=4), color=PURPLE, p=10), page(50, lines=2, w_ratio=1.5), gap=8))
# phishing: an envelope on a fishing hook
computer-science-6-8-cyber-attacks-and-defense/phishing = raw(260, 300, '<line x1="160" y1="0" x2="160" y2="80" stroke="#8a8f9c" stroke-width="5"/><path d="M160 80 V200 C160 260 80 260 80 210 L96 196" fill="none" stroke="#8a8f9c" stroke-width="10" stroke-linecap="round"/>' + g(envelope(150), 80, 110))
# malware: a bug inside a download arrow
computer-science-6-8-cyber-attacks-and-defense/malware = over(arrow(200, BLUE, 'down', sw=34), raw(80, 80, '<ellipse cx="40" cy="46" rx="28" ry="26" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><circle cx="40" cy="20" r="12" fill="#1f2430"/>' + ''.join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1f2430" stroke-width="4"/>' for x1, y1, x2, y2 in ((14, 36, 2, 28), (66, 36, 78, 28), (12, 56, 0, 62), (68, 56, 80, 62)))), dy=-20)
# firewall: a brick wall between a cloud and a laptop
computer-science-6-8-cyber-attacks-and-defense/firewall = row(cloud(130), raw(80, 200, ''.join(f'<rect x="{2 + (r % 2) * 20 - 20 * (r % 2 and 1)}" y="{2 + r * 28}" width="40" height="26" fill="#e04848" stroke="#1f2430" stroke-width="3"/><rect x="{42 + (r % 2) * 20 - 20 * (r % 2 and 1)}" y="{2 + r * 28}" width="36" height="26" fill="#e04848" stroke="#1f2430" stroke-width="3"/>' for r in range(7))), screen(150, laptop=True), gap=14)
# encryption: a message turning into symbols with a key
computer-science-6-8-cyber-attacks-and-defense/encryption = row(bubble(T('hi!', 50), size=130, color=BLUE), arrow(50), key(70), arrow(50), bubble(T('#&%', 44, PURPLE), size=130, color=PURPLE), gap=6)
# CIA triad: a triangle with C, I and A at the corners
computer-science-6-8-cyber-attacks-and-defense/cia-triad = raw(320, 290, '<path d="M160 40 L295 260 H25 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="34" fill="{c}" stroke="#1f2430" stroke-width="5"/><text x="{x}" y="{y + 16}" font-family="Segoe UI" font-size="46" font-weight="700" text-anchor="middle" fill="#fff">{t}</text>' for x, y, t, c in ((160, 40, 'C', BLUE), (36, 252, 'I', ORANGE), (284, 252, 'A', GREEN))))
# filter: a funnel over table rows
computer-science-6-8-data-detectives/filter = col(funnel(130), table(4, 3, size=240), gap=-8)
# sort: bars out of order, then the same bars sorted tallest to shortest
computer-science-6-8-data-detectives/sort = col(bars([4, 2, 5, 1, 3], size=300, color=GRAY), arrow(50, dir='down'), bars([5, 4, 3, 2, 1], size=300, color=BLUE), gap=6)
# misleading: a bar chart with a cut-off axis
computer-science-6-8-data-detectives/misleading = bars([92, 95, 98, 100], size=320, colors=[BLUE, BLUE, BLUE, ORANGE], cut=True, maxv=100)
# outlier: a scatter plot with one far dot
computer-science-6-8-data-detectives/outlier = plot(size=320, xr=(0, 10), yr=(0, 10), scatter=[(1, 2), (2, 2.6), (3, 3.4), (4, 3.6), (5, 4.8), (6, 5.1), (7, 6.2), (8, 6.4)], points=[(8.6, 9.2, RED)], axes=False, box_=True)
# dataset: a spreadsheet grid
computer-science-6-8-data-detectives/dataset = table(cells=[['', 'A', 'B', 'C'], ['1', '', '', ''], ['2', '', '', ''], ['3', '', '', ''], ['4', '', '', '']], size=320, hl_col=0)
# axis: a chart with bold axes
computer-science-6-8-data-detectives/axis = over(plot(lambda x: 0.6 * x + 1, size=320, xr=(-0.3, 8), yr=(-0.3, 8)), raw(320, 320, '<line x1="12" y1="306" x2="310" y2="306" stroke="#e04848" stroke-width="10"/><line x1="14" y1="10" x2="14" y2="308" stroke="#e04848" stroke-width="10"/>'))
# flowchart: boxes and a diamond joined by arrows
computer-science-6-8-flowcharts-and-pseudocode/flowchart = col(box(T('Start', 30), color=BLUE, rx=30, p=12), arrow(36, dir='down'), diamond(140, '?'), arrow(36, dir='down'), box(T('Do it', 30), color=GREEN, p=12), gap=4)
# pseudocode: a page of indented plain lines
computer-science-6-8-flowcharts-and-pseudocode/pseudocode = page(240, lines=9, indent=(1, 2, 4, 5, 6))
# conditional: a diamond with yes and no arrows
computer-science-6-8-flowcharts-and-pseudocode/conditional = diamond(320, '?', yes_no=True)
# loop: a circular arrow around a box
computer-science-6-8-flowcharts-and-pseudocode/loop = curve_arrow(110, BLUE, inner=box(w=90, h=90, color=ORANGE))
# procedure: a labeled box with a reuse arrow
computer-science-6-8-flowcharts-and-pseudocode/procedure = row(box(T('draw()', 44), color=PURPLE, p=20), curve_arrow(50, ORANGE), gap=10)
# decision: an arrow into a decision diamond that splits into yes and no
computer-science-6-8-flowcharts-and-pseudocode/decision = col(arrow(50, dir='down'), diamond(300, '?', yes_no=True), gap=0)
# feature: a bird outline with the wing highlighted
computer-science-6-8-machine-learning-models/feature = raw(300, 220, '<ellipse cx="150" cy="130" rx="100" ry="60" fill="#fff" stroke="#1f2430" stroke-width="6"/><circle cx="240" cy="80" r="40" fill="#fff" stroke="#1f2430" stroke-width="6"/><path d="M278 76 L300 84 L278 92" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><circle cx="250" cy="72" r="5" fill="#1f2430"/><path d="M80 120 C120 40 190 50 200 110 C170 140 120 150 80 120 Z" fill="#f08a24" stroke="#1f2430" stroke-width="6"/><path d="M50 130 L10 110 L20 150 Z" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>')
# accuracy: ten answers: nine checks and one X, 9 of 10 right
computer-science-6-8-machine-learning-models/accuracy = col(grid([check(52) for _ in range(9)] + [cross(52)], 5, gap=10), T('9 of 10 right', 40, GREEN), gap=16)
# bias: a tilted scale
computer-science-6-8-machine-learning-models/bias = scale_icon(300, None, None, tilt=18)
# training set: a stack of photo cards
computer-science-6-8-machine-learning-models/training-set = col(*[card(sized(ic(70), 70), 220, 100, c) for ic, c in ((sun, ORANGE), (tree, GREEN), (cat_icon, BLUE), (car, RED))], gap=-60)
# packet: an image splitting into small envelopes
computer-science-6-8-packets-and-the-internet/packet = row(card(sun(90), 130, 130), arrow(50), grid([envelope(56) for _ in range(6)], 2, gap=8), gap=10)
# IP address: a laptop with a number tag
computer-science-6-8-packets-and-the-internet/ip-address = row(screen(220, laptop=True), raw(160, 60, '<path d="M4 30 L24 4 H156 V56 H24 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><circle cx="24" cy="30" r="6" fill="#fff" stroke="#1f2430" stroke-width="3"/><text x="90" y="40" font-family="Consolas" font-size="22" font-weight="700" text-anchor="middle" fill="#1f2430">10.0.0.7</text>'), gap=-10)
# protocol: two computers with a rulebook between them
computer-science-6-8-packets-and-the-internet/protocol = row(screen(140), book(110, PURPLE, open_=False), screen(140), gap=14)
# redundancy: a network with two paths around a broken line
computer-science-6-8-packets-and-the-internet/redundancy = network(320, 5, broken=0)
# bandwidth: a wide pipe next to a narrow pipe
computer-science-6-8-packets-and-the-internet/bandwidth = col(raw(320, 80, '<rect x="5" y="5" width="310" height="70" rx="10" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{40 + i * 60}" cy="{25 + (i % 2) * 30}" r="10" fill="#3a7bd5"/>' for i in range(5))), raw(320, 40, '<rect x="5" y="10" width="310" height="22" rx="8" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><circle cx="60" cy="21" r="6" fill="#3a7bd5"/>'), gap=30)
# variable: a labeled box holding a value
computer-science-6-8-variables-data-types-and-procedures/variable = col(box(T('7', 110, BLUE), w=170, h=150, color=ORANGE, fill='#fff'), T('age', 50, ORANGE), gap=8)
# data type: three tiles: 42, "hi", true
computer-science-6-8-variables-data-types-and-procedures/data-type = row(tile('42', BLUE, 100), tile('"hi"', ORANGE, 100), tile('true', GREEN, 100), gap=14)
# string: text characters on a string of beads
computer-science-6-8-variables-data-types-and-procedures/string = raw(420, 160, '<path d="M0 60 Q210 140 420 60" fill="none" stroke="#8a8f9c" stroke-width="5"/>' + ''.join(f'<circle cx="{40 + i * 68}" cy="{60 + 80 * (1 - ((40 + i * 68 - 210) / 210) ** 2) * 0.5:.0f}" r="30" fill="{c}" stroke="#1f2430" stroke-width="4"/><text x="{40 + i * 68}" y="{74 + 80 * (1 - ((40 + i * 68 - 210) / 210) ** 2) * 0.5:.0f}" font-family="Segoe UI" font-size="38" font-weight="700" text-anchor="middle" fill="#fff">{ch}</text>' for i, (ch, c) in enumerate(zip('HELLO', (BLUE, ORANGE, GREEN, PURPLE, RED)))))
# Boolean: a switch labeled true and false
computer-science-6-8-variables-data-types-and-procedures/boolean = col(toggle(True, 170, 'true'), toggle(False, 170, 'false'), gap=20, align='l')
# parameter: a box with an input arrow labeled size
computer-science-6-8-variables-data-types-and-procedures/parameter = row(col(T('size', 40, ORANGE), arrow(80, ORANGE), gap=0), box(T('draw', 44), color=PURPLE, p=24), gap=6)
# function: a machine with input and output arrows
computer-science-6-8-variables-data-types-and-procedures/function = machine(380, 'x', 'y')
# data: a tally chart with three rows
computer-science-k-count-and-decide/data = table(cells=[['cat', 'IIII'], ['dog', 'II'], ['bird', 'III']], size=320, header=False)
# tally mark: tally marks in a group of five
computer-science-k-count-and-decide/tally-mark = tally(5, 200)
# chart: a picture graph: apples and bananas, one picture per box
computer-science-k-count-and-decide/chart = col(row(T('apples', 30, RED), *[box(apple(42), w=60, h=60, color=GRAY, fill='#fff', rx=2, sw=3) for _ in range(4)], gap=0), row(T('bananas', 30, ORANGE), *[box(banana(42), w=60, h=60, color=GRAY, fill='#fff', rx=2, sw=3) for _ in range(2)], *[box(w=60, h=60, color=GRAY, fill='#fff', rx=2, sw=3) for _ in range(2)], gap=0), gap=0, align='r')
# most: three stacks of blocks with the tallest one starred
computer-science-k-count-and-decide/most = blocks_stack((3, 5, 2), 300, star_=1, colors=[BLUE, ORANGE, GREEN])
# least: three stacks of blocks with the shortest one starred
computer-science-k-count-and-decide/least = blocks_stack((3, 5, 2), 300, star_=2, colors=[BLUE, ORANGE, GREEN])
# public: an open web page with eyes all around it and an open lock
computer-science-k-public-or-private/public = row(col(eye(70), eye(70), gap=20), browser(220, inner=globe(90)), col(eye(70), lock(64, open_=True), gap=20), gap=14)
# share: two tablets with an arrow between them
computer-science-k-public-or-private/share = row(phone(180, inner=star(50)), harrows(BLUE, 90), phone(180), gap=14)
# trusted adult: a shield with a heart
computer-science-k-public-or-private/trusted-adult = shield(240, BLUE, inner=heart(100))
# safe: a tablet inside a shield
computer-science-k-public-or-private/safe = shield(280, BLUE, inner=phone(110))
# sequence: three boxes joined by arrows, numbered 1 2 3
computer-science-k-step-by-step/sequence = flow(*[col(T(i, 36), box(w=90, h=80, color=c)) for i, c in ((1, BLUE), (2, ORANGE), (3, GREEN))], length=40)
# order: three picture cards labeled 1, 2, 3
computer-science-k-step-by-step/order = row(*[col(card(ic(70), 120, 140, c), T(i + 1, 40)) for i, (ic, c) in enumerate(((egg, BLUE), (duck, ORANGE), (bird, GREEN)))], gap=14)
# career pathway: a winding path with milestones
cte-6-8-career-clusters/career-pathway = raw(380, 280, '<path d="M30 260 C120 260 60 170 160 170 C270 170 170 70 280 60 C320 56 340 40 350 20" fill="none" stroke="#a0673a" stroke-width="14" stroke-linecap="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="{c}" stroke="#1f2430" stroke-width="4"/>' for x, y, c in ((30, 260, BLUE), (160, 170, ORANGE), (280, 60, GREEN))) + g(flag(70, RED), 330, -10))
# values: a heart inside a briefcase
cte-6-8-interests-and-skills/values = raw(260, 220, '<rect x="10" y="50" width="240" height="160" rx="16" fill="#a0673a" stroke="#1f2430" stroke-width="6"/><path d="M90 50 V22 C90 12 170 12 170 22 V50" fill="none" stroke="#1f2430" stroke-width="8"/><rect x="10" y="100" width="240" height="14" fill="#7a4d2a"/>' + g(heart(90), 85, 100))
# inventory: a checklist with stars
cte-6-8-interests-and-skills/inventory = clipboard(260, inner=col(*[row(star(30), raw(80, 10, '<rect x="0" y="0" width="80" height="10" rx="5" fill="#8a8f9c"/>'), gap=8) for _ in range(4)], gap=10))
# transferable skill: a key fitting several locks
cte-6-8-interests-and-skills/transferable-skill = row(key(130), col(lock(70, BLUE), lock(70, ORANGE), lock(70, GREEN), gap=8), gap=20)
# communication: two speech bubbles
cte-6-8-workplace-skills/communication = row(bubble(dots(3, size=26), color=BLUE), bubble(dots(3, size=26, color=ORANGE), color=ORANGE, tail='right'), gap=14)
# teamwork: puzzle pieces fitting together
cte-6-8-workplace-skills/teamwork = puzzle(320, BLUE, ORANGE)
# initiative: an arrow starting forward on its own
cte-6-8-workplace-skills/initiative = row(raw(60, 60, '<circle cx="30" cy="30" r="22" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/>'), arrow(240, GREEN, sw=14), gap=0)
# feedback: a speech bubble with a star
cte-6-8-workplace-skills/feedback = bubble(star(110), size=240, color=BLUE)
# conjunction: two word blocks joined by a plus
ela-1-grammar-basics/conjunction = row(tile('salt', BLUE, 100), T('+', 80, ORANGE), tile('pepper', GREEN, 100), gap=14)
# question mark: a big question mark
ela-1-grammar-basics/question-mark = T('?', 340, BLUE)
# exclamation point: a big exclamation point
ela-1-grammar-basics/exclamation-point = T('!', 340, ORANGE)
# silent e: the word cap plus an e making cape
ela-1-phonics-blends-and-digraphs/silent-e = col(row(tiles('c', 'a', 'p', color=BLUE, size=90), T('+', 70, DARK), tile('e', ORANGE, 90), gap=10), arrow(60, dir='down'), tiles('c', 'a', 'p', 'e', colors=[BLUE, BLUE, BLUE, ORANGE], size=90), gap=8)
# decode: a word broken into sound boxes
ela-1-phonics-blends-and-digraphs/decode = col(T('ship', 90), tiles('sh', 'i', 'p', size=100, colors=[BLUE, ORANGE, GREEN]), gap=14)
# expression: a speech bubble with an exclamation mark
ela-1-reading-fluency/expression = bubble(T('!', 120, ORANGE), size=220, color=ORANGE)
# reread: a book with a circular arrow
ela-1-reading-fluency/reread = over(curve_arrow(130, ORANGE), book(160))
# pause: a pause symbol of two bars
ela-1-reading-fluency/pause = raw(220, 220, '<rect x="40" y="20" width="50" height="180" rx="10" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><rect x="130" y="20" width="50" height="180" rx="10" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>')
# accuracy: a book with a check mark
ela-1-reading-fluency/accuracy = row(book(220), check(110), gap=-30)
# phrase: three words under one swoop line
ela-1-reading-fluency/phrase = col(raw(400, 60, '<path d="M10 50 Q200 -20 390 50" fill="none" stroke="#f08a24" stroke-width="8" stroke-linecap="round"/>'), T('in the park', 70), gap=0)
# lesson: a lightbulb over an open book
ela-1-story-elements-and-lessons/lesson = col(lightbulb_on(140), book(240), gap=4)
# feeling: a smiling face with a small star
ela-1-story-elements-and-lessons/feeling = row(face(200, 'happy'), star(70), gap=0, align='t')
# retell: three story cards with arrows
ela-1-story-elements-and-lessons/retell = flow(card(sun(70), 110, 130), card(tree(70), 110, 130, ORANGE), card(moon(70), 110, 130, PURPLE), length=40)
# heading: a page with a bold heading bar
ela-1-text-features/heading = para_page(240, paras=(3, 3), title=True)
# table of contents: a list of chapter lines with page numbers
ela-1-text-features/table-of-contents = box(col(raw(160, 16, '<rect x="0" y="0" width="160" height="16" rx="6" fill="#3a7bd5"/>'), *[row(raw(140, 10, '<rect x="0" y="0" width="140" height="10" rx="5" fill="#8a8f9c"/>'), T(n, 30), gap=16) for n in (1, 5, 12, 20)], gap=14, align='l'), color=DARK, fill='#fff')
# glossary: an open book at its last page with a word list
ela-1-text-features/glossary = book(280, hl=[1])
# caption: a photo frame with a line of text under it
ela-1-text-features/caption = col(box(row(sun(60), mountain(120), gap=-10), w=240, h=170, color=BROWN, fill='#e9f3fb', sw=10), raw(220, 12, '<rect x="0" y="0" width="220" height="12" rx="6" fill="#8a8f9c"/>'), gap=12)
# icon: a toolbar of small pictures: home, trash, search
ela-1-text-features/icon = box(row(house(66, BLUE), raw(60, 70, '<path d="M8 16 H52 M24 16 V6 H36 V16" fill="none" stroke="#1f2430" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M13 22 L17 66 H43 L47 22 Z" fill="#8a8f9c" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), magnifier(66), gap=30), color=GRAY, fill='#f2f3f6', p=18)
# bold: a line of text with one word in thick letters
ela-1-text-features/bold = row(T('a', 60, GRAY, bold=False), T('big', 80, DARK), T('dog', 60, GRAY, bold=False), gap=18)
# I and me: a speech bubble with the words I and me
ela-1-who-is-telling-the-story/i-and-me = bubble(row(T('I', 80, BLUE), T('me', 80, ORANGE), gap=30), size=260, color=BLUE)
# speaker: a speech bubble pointing to a parrot
ela-1-who-is-telling-the-story/speaker = row(bubble(T('Hello!', 50), color=GREEN, tail='right'), bird(130, GREEN), gap=-10, align='b')
# context clue: a magnifying glass over a sentence
ela-1-word-meanings/context-clue = col(T('The sly fox hid.', 60, bold=False, hl={'sly': ORANGE}), magnifier(150), gap=6)
# root word: the word jumping with jump highlighted
ela-1-word-meanings/root-word = T('jumping', 110, hl={'jump': ORANGE})
# sort: two baskets with word cards
ela-1-word-meanings/sort = row(basket(170, inner=row(tile('cat', BLUE, 60), tile('hat', BLUE, 60), gap=4)), basket(170, inner=row(tile('dog', ORANGE, 60), tile('log', ORANGE, 60), gap=4)), gap=20)
# ending: the word jump with an -ed tile added
ela-1-word-meanings/ending = row(tile('jump', BLUE, 100), T('+', 70), tile('-ed', ORANGE, 100), gap=12)
# first: a big number 1 on a step
ela-1-writing-sentences-and-stories/first = stairs(3, 300, labels=['1', '2', '3'], hl=0)
# purpose: a target with an arrow in the center
ela-2-author-s-purpose/purpose = target(260)
# explain: rain, then a puddle, with a why? bubble over the arrow between them
ela-2-author-s-purpose/explain = col(bubble(T('why?', 40), 140, color=ORANGE, tail='left'), row(raincloud(140), arrow(70, ORANGE), raw(140, 60, '<ellipse cx="70" cy="34" rx="64" ry="22" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>'), gap=10), gap=6)
# moral: a lightbulb over a tortoise
ela-2-fables-and-folktales/moral = col(lightbulb_on(110), raw(240, 140, '<ellipse cx="110" cy="80" rx="80" ry="50" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<path d="M{70 + i * 26} 54 l18 0 l9 14 l-9 14 l-18 0 l-9 -14 z" fill="none" stroke="#1d6b3c" stroke-width="3"/>' for i in range(3)) + '<circle cx="210" cy="78" r="22" fill="#a8c83a" stroke="#1f2430" stroke-width="5"/><circle cx="216" cy="72" r="4" fill="#1f2430"/>' + ''.join(f'<rect x="{x}" y="118" width="20" height="20" rx="6" fill="#a8c83a" stroke="#1f2430" stroke-width="4"/>' for x in (50, 150))), gap=4)
# lesson: an open book with a star
ela-2-fables-and-folktales/lesson = row(book(240), star(90), gap=-40, align='t')
# recount: four story cards with arrows
ela-2-fables-and-folktales/recount = flow(*[card(T(n, 50), 80, 100, c) for n, c in ((1, BLUE), (2, ORANGE), (3, GREEN), (4, PURPLE))], length=30)
# irregular verb: the word go with an arrow to went
ela-2-grammar-and-spelling/irregular-verb = row(T('go', 100, BLUE), arrow(90), T('went', 100, ORANGE), gap=16)
# contraction: can + not squeezing into can't
ela-2-grammar-and-spelling/contraction = col(row(tile('can', BLUE, 90), T('+', 60), tile('not', ORANGE, 90), gap=10), arrow(50, dir='down'), T("can't", 110, hl={"'": RED}), gap=6)
# apostrophe: two words with a red apostrophe: can't and Sam's
ela-2-grammar-and-spelling/apostrophe = col(T("can't", 100, hl={"'": RED}), T("Sam's", 100, hl={"'": RED}), gap=6)
# past tense: a timeline with an arrow pointing back
ela-2-grammar-and-spelling/past-tense = timeline(4, 420, now=3, back=True, labels=['', '', '', 'now'])
# pronoun: a name tile, Mia, with an arrow to the pronoun she; below, he, she and they
ela-2-grammar-and-spelling/pronoun = col(row(tile('Mia', ORANGE, 90), arrow(60), tile('she', BLUE, 90, fill='#fde97a'), gap=10), tiles('he', 'she', 'they', color=BLUE, size=64), gap=26)
# prefix: a re- tile joining the word play
ela-2-long-vowels-and-two-syllable-words/prefix = row(tile('re-', ORANGE, 110), T('+', 70), tile('play', BLUE, 110), gap=12)
# suffix: the word care joining a -ful tile
ela-2-long-vowels-and-two-syllable-words/suffix = row(tile('care', BLUE, 110), T('+', 70), tile('-ful', ORANGE, 110), gap=12)
# spell: the letters r, a, i, n on tiles
ela-2-long-vowels-and-two-syllable-words/spell = tiles('r', 'a', 'i', 'n', size=110, colors=[BLUE, ORANGE, GREEN, PURPLE])
# paragraph: a page with three blocks of text
ela-2-main-idea-and-connections/paragraph = para_page(260, paras=(4, 4, 4))
# steps: three numbered panels of planting
ela-2-main-idea-and-connections/steps = flow(*[card(raw(90, 90, s), 100, 120, GREEN) for s in ('<rect x="10" y="60" width="70" height="26" fill="#a0673a"/><circle cx="45" cy="50" r="6" fill="#7a4d2a"/><path d="M45 10 v24 m-8 -8 l8 8 l8 -8" fill="none" stroke="#1f2430" stroke-width="4"/>', '<rect x="10" y="60" width="70" height="26" fill="#a0673a"/><path d="M60 20 l-10 30 M70 20 l-8 30 M80 22 l-6 28" stroke="#3a7bd5" stroke-width="4"/><rect x="40" y="6" width="44" height="16" rx="4" fill="#8a8f9c" transform="rotate(20 60 14)"/>', '<rect x="10" y="60" width="70" height="26" fill="#a0673a"/><path d="M45 60 V24" stroke="#2f9e5b" stroke-width="6"/><path d="M45 36 C30 30 24 18 30 14 C40 16 46 26 45 36 Z M45 30 C60 24 66 12 60 8 C50 10 44 20 45 30 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="2"/>')], length=30)
# connection: two circles joined by a line
ela-2-main-idea-and-connections/connection = row(shape('circle', 100, BLUE), raw(120, 10, '<line x1="0" y1="5" x2="120" y2="5" stroke="#1f2430" stroke-width="8"/>'), shape('circle', 100, ORANGE), gap=0)
# closing sentence: a paragraph with its last line highlighted
ela-2-paragraph-writing/closing-sentence = page(240, lines=7, hl=(6,))
# indent: a paragraph with its first line moved in
ela-2-paragraph-writing/indent = page(240, lines=7, indent=(0,), hl=(0,))
# problem: a kite with a question mark
ela-2-story-structure-and-point-of-view/problem = paint('a red kite tangled high in the bare branches of a tall tree, string dangling')
# prefix: an un- tile joining the word happy
ela-2-word-building/prefix = row(tile('un-', ORANGE, 110), T('+', 70), tile('happy', BLUE, 110), gap=12)
# root word: the word kindness with kind highlighted
ela-2-word-building/root-word = T('kindness', 100, hl={'kind': ORANGE})
# shades of meaning: warm, hot, boiling: tiles shaded from light to dark
ela-2-word-building/shades-of-meaning = col(row(tile('warm', ORANGE, 76, fill='#fde3c8'), tile('hot', ORANGE, 76, fill='#f5a65b'), tile('boiling', RED, 76, fill=RED, text='#fff'), gap=10), arrow(380, RED, sw=10), gap=10)
# synonym: two equal word tiles with an equal sign
ela-2-word-building/synonym = row(tile('big', BLUE, 110), T('=', 80), tile('large', ORANGE, 110), gap=14)
# stanza: a poem shape made of three blocks of four lines
ela-3-chapters-scenes-and-stanzas/stanza = raw(200, 280, ''.join(f'<rect x="30" y="{10 + b * 92 + i * 18}" width="{140 - (i % 2) * 30}" height="10" rx="5" fill="{c}"/>' for b, c in enumerate((BLUE, ORANGE, GREEN)) for i in range(4)))
# sequence: three panels in a row joined by arrows, sunrise, sun and moon
ela-3-chapters-scenes-and-stanzas/sequence = flow(card(raw(80, 60, '<line x1="0" y1="50" x2="80" y2="50" stroke="#1f2430" stroke-width="4"/><path d="M14 50 A26 26 0 0 1 66 50 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="4"/>'), 110, 130, ORANGE), card(sun(80), 110, 130, YELLOW), card(moon(70), 110, 130, PURPLE), length=34)
# feeling: three simple faces in a row, scared, calm and proud
ela-3-characters-and-their-choices/feeling = faces('scared', 'calm', 'proud', size=120)
# dialogue: two speech bubbles facing each other
ela-3-characters-and-their-choices/dialogue = row(bubble(dots(3, size=24, color=BLUE), color=BLUE), bubble(dots(3, size=24, color=ORANGE), color=ORANGE, tail='right'), gap=10)
# root word: the word comfortable with comfort highlighted
ela-3-literal-and-figurative-language/root-word = T('comfortable', 84, hl={'comfort': ORANGE})
# syllable: the word basket split into two colored blocks, bas and ket
ela-3-multisyllable-decoding/syllable = row(tile('bas', BLUE, 130), tile('ket', ORANGE, 130), gap=8)
# vowel: the letters a e i o u on bright tiles
ela-3-multisyllable-decoding/vowel = tiles('a', 'e', 'i', 'o', 'u', size=100, colors=[RED, ORANGE, GREEN, BLUE, PURPLE])
# prefix: a block un- joining the word happy to make unhappy
ela-3-multisyllable-decoding/prefix = col(row(tile('un-', ORANGE, 90), T('+', 60), tile('happy', BLUE, 90), gap=10), arrow(50, dir='down'), T('unhappy', 90, hl={'un': ORANGE, 'happy': BLUE}), gap=6)
# suffix: the word help joining a block -ful to make helpful
ela-3-multisyllable-decoding/suffix = col(row(tile('help', BLUE, 90), T('+', 60), tile('-ful', ORANGE, 90), gap=10), arrow(50, dir='down'), T('helpful', 90, hl={'help': BLUE, 'ful': ORANGE}), gap=6)
# base word: the word replaying with play highlighted in the middle
ela-3-multisyllable-decoding/base-word = T('replaying', 96, hl={'play': ORANGE})
# irregular spelling: the word said with a question mark over the letters ai
ela-3-multisyllable-decoding/irregular-spelling = col(row(Item(64, 10, ''), T('?', 70, RED), gap=0, align='l'), T('said', 130, hl={'ai': ORANGE}), gap=-20, align='l')
# plot: a story mountain line with dots for the beginning, middle and end
ela-3-narrative-writing/plot = raw(380, 240, '<path d="M10 220 L150 220 L240 50 L330 220 L370 220" fill="none" stroke="#1f2430" stroke-width="8" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}" stroke="#1f2430" stroke-width="4"/>' for x, y, c in ((60, 220, BLUE), (240, 50, ORANGE), (350, 220, GREEN))))
# linking word: two sentence parts joined by the linking word because
ela-3-opinion-and-informative-writing/linking-word = col(tile('We stayed in', BLUE, 70), tile('because', ORANGE, 70, fill='#fde97a'), tile('it rained.', BLUE, 70), gap=8)
# pronoun: the name Maria with an arrow pointing to the word she
ela-3-parts-of-speech/pronoun = row(T('Maria', 80, BLUE), arrow(80), T('she', 80, ORANGE), gap=12)
# verb tense: a timeline marked yesterday, today and tomorrow
ela-3-parts-of-speech/verb-tense = timeline(3, 440, labels=['yesterday', 'today', 'tomorrow'], hl=1)
# keyword: a search box with the keyword volcano typed in
ela-3-text-structure-and-search-tools/keyword = browser(300, search=True, query='volcano')
# heading: a page with bold heading bars above blocks of text
ela-3-text-structure-and-search-tools/heading = para_page(240, paras=(3, 3), title=True)
# focus: a spotlight on a heart
ela-4-firsthand-and-secondhand-accounts/focus = raw(320, 300, '<path d="M120 10 L200 10 L290 280 L30 280 Z" fill="#fdf0c4" opacity="0.9"/><ellipse cx="160" cy="280" rx="130" ry="16" fill="#fde97a"/><rect x="120" y="0" width="80" height="22" rx="4" fill="#1f2430"/>' + g(heart(130), 95, 140))
# perspective: two eyes looking at the same star from different sides
ela-4-firsthand-and-secondhand-accounts/perspective = raw(360, 240, g(star(100), 130, 70) + g(eye(110, look=12), 0, 90) + f'<g transform="translate(360 90) scale(-1 1)">{eye(110, look=12).svg}</g>' + '<path d="M110 120 L135 120 M250 120 L225 120" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="6 6"/>')
# relative pronoun: the word who linking two word blocks
ela-4-grammar-in-use/relative-pronoun = row(tile('the girl', BLUE, 90), tile('who', ORANGE, 90), tile('sings', GREEN, 90), gap=8)
# progressive tense: an arrow that keeps going on a timeline
ela-4-grammar-in-use/progressive-tense = timeline(4, 440, keep_going=1, labels=['', 'now', '', ''])
# modal verb: three word tiles: can, may, must
ela-4-grammar-in-use/modal-verb = col(tile('can', BLUE, 90), tile('may', ORANGE, 90), tile('must', GREEN, 90), gap=14)
# fragment: a sentence strip torn in half
ela-4-grammar-in-use/fragment = raw(400, 140, '<path d="M10 30 H200 L188 54 L204 78 L190 102 L200 120 H10 Z" fill="#fdf0c4" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M230 30 H390 V120 H226 L216 102 L232 78 L214 54 Z" fill="#fdf0c4" stroke="#1f2430" stroke-width="5" stroke-linejoin="round" transform="rotate(6 300 75)"/><rect x="30" y="66" width="140" height="14" rx="7" fill="#8a8f9c"/><rect x="250" y="70" width="110" height="14" rx="7" fill="#8a8f9c" transform="rotate(6 300 75)"/>')
# root: a word with its middle part highlighted
ela-4-greek-and-latin-roots/root = T('unkindly', 110, hl={'kind': ORANGE})
# affix: two tiles attached to a root
ela-4-greek-and-latin-roots/affix = row(tile('re-', ORANGE, 100), tile('read', BLUE, 100), tile('-ing', GREEN, 100), gap=4)
# context clues: a magnifying glass over a sentence
ela-4-greek-and-latin-roots/context-clues = col(T('The sly fox hid.', 60, bold=False, hl={'sly': ORANGE}), magnifier(150), gap=6)
# stanza: four blocks of short lines
ela-4-poetry-drama-and-prose/stanza = raw(220, 300, ''.join(f'<rect x="20" y="{10 + b * 74 + i * 14}" width="{110 - (i % 2) * 30}" height="8" rx="4" fill="{c}"/>' for b, c in enumerate((BLUE, ORANGE, GREEN, PURPLE)) for i in range(4)))
# verse: short lines with a rhythm pattern beside them
ela-4-poetry-drama-and-prose/verse = row(raw(170, 200, ''.join(f'<rect x="0" y="{10 + i * 26}" width="{150 - (i % 2) * 40}" height="10" rx="5" fill="#8a8f9c"/>' for i in range(7))), raw(110, 200, ''.join(f'<circle cx="{14 + k * 26}" cy="{16 + i * 26}" r="{10 if k % 2 else 5}" fill="#f08a24"/>' for i in range(7) for k in range(4))), gap=10)
# stage directions: a script with words in parentheses highlighted
ela-4-poetry-drama-and-prose/stage-directions = box(col(row(raw(70, 10, '<rect width="70" height="10" rx="5" fill="#1f2430"/>'), raw(120, 10, '<rect width="120" height="10" rx="5" fill="#8a8f9c"/>'), gap=10), hlbg(T('(she waves)', 34, PURPLE, italic=True)), row(raw(70, 10, '<rect width="70" height="10" rx="5" fill="#1f2430"/>'), raw(140, 10, '<rect width="140" height="10" rx="5" fill="#8a8f9c"/>'), gap=10), hlbg(T('(he sits)', 34, PURPLE, italic=True)), gap=16, align='l'), color=DARK, fill='#fff')
# prose: a page of paragraphs
ela-4-poetry-drama-and-prose/prose = para_page(240, paras=(4, 5, 4))
# organize: index cards sorted into three piles
ela-4-short-research-projects/organize = row(*[col(*[card(None, 80, 60, c) for _ in range(3)], gap=-44) for c in (BLUE, ORANGE, GREEN)], gap=20)
# text structure: four small diagrams of different structures
ela-4-text-structures/text-structure = grid([box(timeline(3, 120), color=BLUE, fill='#fff', p=8), box(row(box(w=40, h=30, color=ORANGE), arrow(30), box(w=40, h=30, color=ORANGE), gap=2), color=ORANGE, fill='#fff', p=8), box(sized(venn(2), 130), color=GREEN, fill='#fff', p=8), box(row(T('?', 44, RED), arrow(30), check(36), gap=4), color=PURPLE, fill='#fff', p=8)], 2)
# chronology: a timeline with dots
ela-4-text-structures/chronology = timeline(5, 440)
# cause and effect: an arrow from a raincloud to a flooded house
ela-4-text-structures/cause-and-effect = row(raincloud(150), arrow(70), raw(150, 150, g(house(130), 10, 0) + '<path d="M0 120 Q40 108 75 120 T150 120 V150 H0 Z" fill="#3a7bd5" opacity="0.85"/>'), gap=10)
# signal words: a road sign with an arrow
ela-4-text-structures/signal-words = raw(220, 300, '<rect x="100" y="120" width="20" height="176" fill="#8a8f9c" stroke="#1f2430" stroke-width="4"/><rect x="10" y="10" width="200" height="120" rx="14" fill="#2f9e5b" stroke="#1f2430" stroke-width="6"/><rect x="20" y="20" width="180" height="100" rx="8" fill="none" stroke="#fff" stroke-width="4"/><path d="M40 70 H150 M120 40 L160 70 L120 100" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>')
# summary: a long page shrinking into a short card
ela-4-theme-and-summary/summary = row(page(220, lines=10), arrow(80), card(raw(80, 30, '<rect x="0" y="0" width="80" height="10" rx="5" fill="#8a8f9c"/><rect x="0" y="20" width="56" height="10" rx="5" fill="#8a8f9c"/>'), 120, 90, ORANGE), gap=10)
# key details: a list with three items starred
ela-4-theme-and-summary/key-details = box(col(*[row(star(40) if i != 1 else Item(40, 40, ''), raw(180, 12, '<rect x="0" y="0" width="180" height="12" rx="6" fill="#8a8f9c"/>'), gap=14) for i in range(4)], gap=20), color=DARK, fill='#fff')
# infer: a magnifying glass over a page with a lightbulb
ela-4-theme-and-summary/infer = over(page(240, lines=7), magnifier(170, inner=lightbulb_on(70)), dx=40, dy=30)
# character trait: a name tag with a star
ela-4-theme-and-summary/character-trait = raw(300, 220, '<rect x="10" y="10" width="280" height="200" rx="20" fill="#e04848" stroke="#1f2430" stroke-width="6"/><rect x="24" y="70" width="252" height="124" rx="10" fill="#fff"/><text x="150" y="54" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#fff">HELLO</text>' + g(star(90), 105, 88))
# evidence: a page with two highlighted lines
ela-4-writing-with-evidence/evidence = page(240, lines=8, hl=(2, 5))
# quotation: large quotation marks
ela-4-writing-with-evidence/quotation = T('“ ”', 300, BLUE)
# linking words: It rained, so we got wet: so links the two parts
ela-4-writing-with-evidence/linking-words = col(tile('It rained', BLUE, 70), tile('so', ORANGE, 70, fill='#fde97a'), tile('we got wet.', BLUE, 70), gap=8)
# conclusion: a page with its last paragraph boxed
ela-4-writing-with-evidence/conclusion = para_page(240, paras=(3, 3, 3), box_para=(2,))
# compare: a Venn diagram
ela-5-comparing-characters-and-themes/compare = venn(2, labels=['A', 'B'])
# contrast: two different boxes with arrows apart
ela-5-comparing-characters-and-themes/contrast = row(arrow(80, BLUE, 'left', sw=10), box(w=150, h=150, color=BLUE), Item(40, 10, ''), shape('circle', 150, ORANGE), arrow(80, ORANGE, sw=10), gap=8)
# theme: two books with a shared star
ela-5-comparing-characters-and-themes/theme = col(star(90), row(book(130, BLUE, open_=False), book(130, ORANGE, open_=False), gap=30), gap=10)
# Venn diagram: two overlapping circles
ela-5-comparing-characters-and-themes/venn-diagram = venn(2)
# conjunction: two word blocks joined by a plus sign
ela-5-conjunctions-tense-and-commas/conjunction = row(tile('salt', BLUE, 100), T('+', 80, ORANGE), tile('pepper', GREEN, 100), gap=14)
# correlative conjunctions: two linked word tiles
ela-5-conjunctions-tense-and-commas/correlative-conjunctions = row(tile('either', BLUE, 100), chain(1, 60), tile('or', ORANGE, 100), gap=-4)
# perfect tense: a timeline with a completed check mark
ela-5-conjunctions-tense-and-commas/perfect-tense = timeline(4, 440, now=3, segment=(0, 2), check_at=2, labels=['', '', '', 'now'])
# comma: a large comma mark
ela-5-conjunctions-tense-and-commas/comma = raw(120, 230, '<circle cx="60" cy="60" r="50" fill="#3a7bd5"/><path d="M106 70 C108 130 80 180 30 220 L20 206 C50 176 62 140 62 108 Z" fill="#3a7bd5"/>')
# introductory phrase: a sentence strip with its first part highlighted
ela-5-conjunctions-tense-and-commas/introductory-phrase = raw(440, 110, '<rect x="5" y="5" width="430" height="100" rx="12" fill="#fff" stroke="#1f2430" stroke-width="5"/><rect x="18" y="22" width="212" height="66" rx="8" fill="#fde97a"/><text x="124" y="68" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="middle" fill="#1f2430">After lunch,</text><text x="330" y="68" font-family="Segoe UI" font-size="34" text-anchor="middle" fill="#1f2430">we played.</text>')
# interjection: a burst shape with an exclamation mark
ela-5-conjunctions-tense-and-commas/interjection = raw(280, 280, '<polygon points="' + ' '.join(f'{140 + (130 if i % 2 == 0 else 80) * math.cos(math.pi * i / 8):.1f},{140 + (130 if i % 2 == 0 else 80) * math.sin(math.pi * i / 8):.1f}' for i in range(16)) + '" fill="#f5c33b" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><text x="140" y="180" font-family="Segoe UI" font-size="120" font-weight="700" text-anchor="middle" fill="#e04848">!</text>')
# integrate: three arrows merging into one
ela-5-multiple-sources/integrate = raw(380, 240, ''.join(f'<path d="M10 {y} C120 {y} 140 120 220 120" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"/>' for y, c in ((30, BLUE), (120, ORANGE), (210, GREEN))) + '<path d="M220 120 H330" stroke="#8e5bc4" stroke-width="16"/><path d="M370 120 l-40 -24 v48 z" fill="#8e5bc4"/>')
# point of view: two eyes looking at one object
ela-5-multiple-sources/point-of-view = raw(360, 240, g(ball(100, ORANGE), 130, 70) + g(eye(110, look=12), 0, 90) + f'<g transform="translate(360 90) scale(-1 1)">{eye(110, look=12).svg}</g>')
# synthesize: puzzle pieces fitting into a whole
ela-5-multiple-sources/synthesize = row(puzzle(200, BLUE, ORANGE, apart=True), arrow(60), puzzle(200, BLUE, ORANGE), gap=10)
# dialogue: two speech bubbles
ela-5-narrative-craft/dialogue = row(bubble(dots(3, size=26), color=BLUE), bubble(dots(3, size=26, color=ORANGE), color=ORANGE, tail='right'), gap=14)
# sensory details: five icons for the senses
ela-5-narrative-craft/sensory-details = row(eye(80), ear(70, waves=False), raw(60, 70, '<path d="M30 6 C14 30 10 46 18 60 C24 70 36 70 42 60 C50 46 46 30 30 6 Z" fill="#f6d6bd" stroke="#1f2430" stroke-width="5"/><path d="M22 58 C26 62 34 62 38 58" fill="none" stroke="#1f2430" stroke-width="4"/>'), raw(80, 50, '<path d="M6 26 Q40 -10 74 26 Q40 50 6 26 Z" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M14 26 H66" stroke="#1f2430" stroke-width="3"/>'), hand(80), gap=16)
# introduction: a page with its first paragraph boxed
ela-5-organized-essays/introduction = para_page(240, paras=(3, 3, 3), box_para=(0,))
# body paragraph: a page with three middle paragraphs boxed
ela-5-organized-essays/body-paragraph = para_page(260, paras=(2, 3, 3, 3, 2), box_para=(1, 2, 3))
# transition: a bridge between two blocks
ela-5-organized-essays/transition = raw(420, 220, '<rect x="5" y="60" width="120" height="150" rx="14" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><rect x="295" y="60" width="120" height="150" rx="14" fill="#fde3c8" stroke="#f08a24" stroke-width="6"/><path d="M125 120 Q210 30 295 120" fill="none" stroke="#a0673a" stroke-width="10"/><path d="M125 120 H295" stroke="#a0673a" stroke-width="12"/>' + ''.join(f'<line x1="{x}" y1="120" x2="{x}" y2="{120 - (60 - abs(x - 210) * 0.7):.0f}" stroke="#a0673a" stroke-width="6"/>' for x in range(150, 280, 20)))
# logical order: three numbered boxes in a row
ela-5-organized-essays/logical-order = flow(*[box(T(i, 60), w=100, h=100, color=c) for i, c in ((1, BLUE), (2, ORANGE), (3, GREEN))], length=40)
# quote: quotation marks around a highlighted line
ela-5-quoting-and-inferring/quote = row(T('“', 140, BLUE), hlbg(raw(200, 30, '<rect x="0" y="9" width="200" height="12" rx="6" fill="#1f2430" opacity="0.6"/>')), T('”', 140, BLUE), gap=4)
# explicit: a page with one bold line
ela-5-quoting-and-inferring/explicit = page(240, lines=8, bold=(3,))
# text evidence: a page with a paragraph highlighted
ela-5-quoting-and-inferring/text-evidence = para_page(240, paras=(3, 3, 3), hl_para=(1,))
# accurate: a target with an arrow in the center
ela-5-quoting-and-inferring/accurate = target(260)
# support: a roof held up by three pillars
ela-5-reasons-and-evidence/support = pillars(3, 320)
# statistic: a pie with one third shaded: 1 in 3
ela-5-reasons-and-evidence/statistic = row(pie(1 / 3, 230, ORANGE), M('1 in 3', 70, color=ORANGE), gap=20)
# convincing: a balance tipped far to one side
ela-5-reasons-and-evidence/convincing = scale_icon(300, ball(50, BLUE), None, tilt=26)
# thesis statement: a paragraph with its last line highlighted
ela-6-argument-writing/thesis-statement = page(240, lines=7, hl=(6,))
# transition: a bridge between two blocks
ela-6-argument-writing/transition = raw(420, 220, '<rect x="5" y="60" width="120" height="150" rx="14" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><rect x="295" y="60" width="120" height="150" rx="14" fill="#fde3c8" stroke="#f08a24" stroke-width="6"/><path d="M125 120 Q210 30 295 120" fill="none" stroke="#a0673a" stroke-width="10"/><path d="M125 120 H295" stroke="#a0673a" stroke-width="12"/>' + ''.join(f'<line x1="{x}" y1="120" x2="{x}" y2="{120 - (60 - abs(x - 210) * 0.7):.0f}" stroke="#a0673a" stroke-width="6"/>' for x in range(150, 280, 20)))
# concluding statement: a page with a boxed final line
ela-6-argument-writing/concluding-statement = page(240, lines=7, boxed=(6,))
# supporting detail: a box held up by three pillars
ela-6-central-idea-and-summary/supporting-detail = pillars(3, 320, inner=None) if 0 else raw(300, 260, '<rect x="40" y="10" width="220" height="70" rx="10" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/>' + ''.join(f'<rect x="{x}" y="80" width="34" height="150" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/>' for x in (60, 133, 206)) + '<rect x="20" y="230" width="260" height="20" fill="#8a8f9c" stroke="#1f2430" stroke-width="5"/>')
# objective summary: a level scale next to a short page
ela-6-central-idea-and-summary/objective-summary = row(scale_icon(220), card(raw(80, 30, '<rect x="0" y="0" width="80" height="10" rx="5" fill="#8a8f9c"/><rect x="0" y="20" width="56" height="10" rx="5" fill="#8a8f9c"/>'), 120, 90, ORANGE), gap=20)
# develop: a staircase of blocks
ela-6-central-idea-and-summary/develop = stairs(5, 320, color=GREEN)
# key idea: a highlighter over a line
ela-6-central-idea-and-summary/key-idea = raw(380, 160, '<rect x="10" y="20" width="360" height="14" rx="7" fill="#8a8f9c"/><rect x="0" y="62" width="300" height="36" fill="#fde97a"/><rect x="10" y="73" width="330" height="14" rx="7" fill="#1f2430"/><rect x="10" y="126" width="300" height="14" rx="7" fill="#8a8f9c"/><g transform="rotate(-30 300 70)"><rect x="290" y="40" width="90" height="34" rx="6" fill="#f5c33b" stroke="#1f2430" stroke-width="5"/><path d="M290 46 L266 57 L290 68 Z" fill="#fde97a" stroke="#1f2430" stroke-width="4"/></g>')
# conclude: a magnifying glass and a check
ela-6-central-idea-and-summary/conclude = row(magnifier(170), check(120), gap=20)
# norms: a checklist poster
ela-6-collaborative-discussions/norms = clipboard(280, inner=col(*[row(check(30), raw(80, 10, '<rect x="0" y="0" width="80" height="10" rx="5" fill="#8a8f9c"/>'), gap=8) for _ in range(4)], gap=12))
# pose a question: a large question mark
ela-6-collaborative-discussions/pose-a-question = T('?', 340, BLUE)
# elaborate: a small box growing into a bigger one
ela-6-collaborative-discussions/elaborate = row(box(w=70, h=70, color=BLUE), arrow(70), box(w=170, h=170, color=BLUE), gap=10)
# paraphrase: two matching speech bubbles
ela-6-collaborative-discussions/paraphrase = row(bubble(star(60), color=BLUE), T('=', 60), bubble(star(60), color=ORANGE, tail='right'), gap=10)
# connotation: a frowning face beside a word tile
ela-6-connotation-and-context/connotation = row(face(140, 'sad'), tile('cheap', ORANGE, 100), gap=20)
# nuance: slim, thin, skinny: close words in lighter and darker shades
ela-6-connotation-and-context/nuance = row(tile('slim', BLUE, 76, fill='#d6e6fb'), tile('thin', BLUE, 76, fill='#8fb6ea'), tile('skinny', BLUE, 76, fill=BLUE, text='#fff'), gap=10)
# dynamic character: a seed growing into a flower
ela-6-plot-and-character-development/dynamic-character = row(raw(80, 80, '<ellipse cx="40" cy="50" rx="20" ry="28" fill="#a0673a" stroke="#1f2430" stroke-width="5"/>'), arrow(60), raw(100, 160, '<path d="M50 160 V60" stroke="#2f9e5b" stroke-width="8"/><path d="M50 110 C30 100 20 80 30 76 C44 80 52 96 50 110 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/>'), arrow(60), raw(140, 220, '<path d="M70 220 V90" stroke="#2f9e5b" stroke-width="9"/><path d="M70 170 C46 160 34 136 44 130 C60 134 72 154 70 170 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/>' + ''.join(f'<ellipse cx="{70 + 30 * math.cos(a):.1f}" cy="{60 + 30 * math.sin(a):.1f}" rx="22" ry="14" transform="rotate({math.degrees(a):.0f} {70 + 30 * math.cos(a):.1f} {60 + 30 * math.sin(a):.1f})" fill="#f28bb3" stroke="#1f2430" stroke-width="4"/>' for a in [k * 2 * math.pi / 6 for k in range(6)]) + '<circle cx="70" cy="60" r="18" fill="#f5c33b" stroke="#1f2430" stroke-width="4"/>'), gap=6, align='b')
# first person: a speech bubble with the word I
ela-6-point-of-view/first-person = bubble(T('I', 160, BLUE), size=240, color=BLUE)
# third person limited: a spotlight on one figure of three
ela-6-point-of-view/third-person-limited = raw(380, 280, '<path d="M150 0 H230 L330 260 H50 Z" fill="#fdf0c4"/>' + ''.join(f'<circle cx="{x}" cy="160" r="32" fill="{c}" stroke="#1f2430" stroke-width="5"/><path d="M{x - 40} 260 C{x - 40} 210 {x + 40} 210 {x + 40} 260 Z" fill="{c}" stroke="#1f2430" stroke-width="5"/>' for x, c in ((60, '#c4c8d0'), (190, '#f08a24'), (320, '#c4c8d0'))))
# third person omniscient: an eye above several thought bubbles
ela-6-point-of-view/third-person-omniscient = col(eye(140), row(bubble(None, 110, BLUE, think=True), bubble(None, 110, ORANGE, think=True), bubble(None, 110, GREEN, think=True), gap=10), gap=20)
# unreliable narrator: a speech bubble with a crack
ela-6-point-of-view/unreliable-narrator = bubble(dots(3, size=28), size=240, color=BLUE, crack=True)
# pronoun case: two tiles, she and her
ela-6-pronouns-and-sentence-variety/pronoun-case = row(tile('she', BLUE, 110), tile('her', ORANGE, 110), gap=24)
# vague pronoun: a pronoun tile with a question mark
ela-6-pronouns-and-sentence-variety/vague-pronoun = col(T('?', 100, RED), tile('it', BLUE, 120), gap=0)
# sentence variety: bars of different lengths
ela-6-pronouns-and-sentence-variety/sentence-variety = col(*[raw(w, 30, f'<rect x="0" y="0" width="{w}" height="30" rx="15" fill="{c}"/>') for w, c in ((300, BLUE), (140, ORANGE), (380, GREEN), (220, PURPLE))], gap=20, align='l')
# intensive pronoun: the word myself in bold
ela-6-pronouns-and-sentence-variety/intensive-pronoun = T('myself', 110, PURPLE)
# citation: a sentence with a small source tag
ela-6-research-and-citing-sources/citation = row(raw(260, 20, '<rect x="0" y="5" width="260" height="14" rx="7" fill="#8a8f9c"/>'), raw(110, 60, '<path d="M4 30 L22 6 H106 V54 H22 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><text x="62" y="40" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">(1)</text>'), gap=10)
# quote: quotation marks
ela-6-research-and-citing-sources/quote = T('“ ”', 300, BLUE)
# paraphrase: two different speech bubbles with the same star
ela-6-research-and-citing-sources/paraphrase = row(bubble(row(star(50), T('A', 40), gap=6), color=BLUE), bubble(row(star(50), T('B', 40), gap=6), color=ORANGE, tail='right'), gap=12)
# plagiarism: a copy icon with a red X
ela-6-research-and-citing-sources/plagiarism = over(raw(200, 220, '<rect x="60" y="10" width="130" height="160" rx="10" fill="#fff" stroke="#1f2430" stroke-width="6"/><rect x="10" y="50" width="130" height="160" rx="10" fill="#fff" stroke="#1f2430" stroke-width="6"/>'), cross(160))
# bibliography: an alphabetized list
ela-6-research-and-citing-sources/bibliography = box(col(*[row(T(c, 40, BLUE), raw(170, 12, '<rect x="0" y="0" width="170" height="12" rx="6" fill="#8a8f9c"/>'), gap=12) for c in 'ABCD'], gap=14, align='l'), color=DARK, fill='#fff')
# claim: a flag on a hill
ela-6-tracing-an-argument/claim = raw(340, 240, '<path d="M0 240 C80 120 260 120 340 240 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/>' + g(flag(130, RED), 150, 30))
# unsupported: a roof with no pillars
ela-6-tracing-an-argument/unsupported = raw(320, 240, '<path d="M20 90 L160 20 L300 90 Z" fill="#e04848" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><rect x="10" y="210" width="300" height="20" fill="#8a8f9c" stroke="#1f2430" stroke-width="5"/><text x="160" y="180" font-family="Segoe UI" font-size="70" font-weight="700" text-anchor="middle" fill="#e04848">?</text>')
# relevant: a puzzle piece that fits
ela-6-tracing-an-argument/relevant = puzzle(300, BLUE, ORANGE)
# trace: a dotted path through three boxes
ela-6-tracing-an-argument/trace = raw(400, 160, ''.join(f'<rect x="{10 + i * 140}" y="40" width="100" height="80" rx="12" fill="{soft(c)}" stroke="{c}" stroke-width="5"/>' for i, c in enumerate((BLUE, ORANGE, GREEN))) + '<path d="M60 80 H340" stroke="#e04848" stroke-width="6" stroke-dasharray="4 12" stroke-linecap="round"/>')
# acknowledge: a nod of two arrows meeting
ela-7-argument-with-counterclaims/acknowledge = row(arrow(120, BLUE), arrow(120, ORANGE, 'left'), gap=0)
# rebuttal: an arrow bouncing back
ela-7-argument-with-counterclaims/rebuttal = raw(320, 220, '<rect x="270" y="20" width="30" height="190" rx="6" fill="#8a8f9c" stroke="#1f2430" stroke-width="5"/><path d="M20 60 L240 110" stroke="#3a7bd5" stroke-width="9" stroke-linecap="round"/><path d="M240 120 L40 180" stroke="#f08a24" stroke-width="9" stroke-linecap="round"/><path d="M24 186 l26 -20 l6 22 z" fill="#f08a24"/>')
# logical: three steps in a row
ela-7-argument-with-counterclaims/logical = stairs(3, 300, labels=['1', '2', '3'], color=BLUE)
# however: a fork in a path
ela-7-argument-with-counterclaims/however = fork(300)
# emphasis: a bold, underlined word
ela-7-comparing-authors/emphasis = T('really', 120, under='really')
# interpretation: two different arrows from one dot
ela-7-comparing-authors/interpretation = raw(340, 260, '<circle cx="40" cy="130" r="20" fill="#1f2430"/><path d="M60 120 L280 40" stroke="#3a7bd5" stroke-width="10" stroke-linecap="round"/><path d="M300 33 l-30 -6 l10 28 z" fill="#3a7bd5"/><path d="M60 140 L280 220" stroke="#f08a24" stroke-width="10" stroke-linecap="round"/><path d="M300 227 l-30 6 l10 -28 z" fill="#f08a24"/>')
# purpose: a light bulb, a megaphone and a smiling face: inform, persuade, entertain
ela-7-comparing-authors/purpose = row(col(bulb(90), T('inform', 28), gap=4), col(raw(100, 80, '<path d="M10 28 H32 L84 6 V74 L32 52 H10 Z" fill="#f08a24" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M20 52 L28 74 H40 L36 54" fill="#f08a24" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>'), T('persuade', 28), gap=10), col(face(90), T('entertain', 28), gap=4), gap=34, align='b')
# shape: clay being formed by an arrow
ela-7-comparing-authors/shape = row(arrow(90, ORANGE, sw=10), raw(200, 160, '<path d="M20 150 C10 100 40 60 60 70 C80 40 120 30 140 60 C170 50 190 90 180 150 Z" fill="#c98b4f" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>'), arrow(90, ORANGE, 'left', sw=10), gap=0)
# omit: a list with one line crossed out
ela-7-comparing-authors/omit = box(col(*[raw(220, 14, f'<rect x="0" y="0" width="220" height="14" rx="7" fill="#8a8f9c"/>' + ('<line x1="-10" y1="7" x2="230" y2="7" stroke="#e04848" stroke-width="7"/>' if i == 2 else '')) for i in range(5)], gap=22), color=DARK, fill='#fff')
# evaluate: a balance scale
ela-7-evaluating-arguments/evaluate = scale_icon(300, ball(50, BLUE), ball(50, ORANGE))
# sound reasoning: a chain with all links closed
ela-7-evaluating-arguments/sound-reasoning = chain(4, 340)
# sufficient: a dashed line for what is needed; a short bar falls short (X), a tall bar reaches it (check)
ela-7-evaluating-arguments/sufficient = raw(300, 290, '<rect x="40" y="190" width="80" height="80" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><rect x="170" y="70" width="80" height="200" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><line x1="10" y1="90" x2="290" y2="90" stroke="#e04848" stroke-width="5" stroke-dasharray="12 8"/><text x="60" y="80" font-family="Segoe UI, Arial, sans-serif" font-size="24" font-weight="700" text-anchor="middle" fill="#e04848">needed</text><line x1="10" y1="270" x2="290" y2="270" stroke="#1f2430" stroke-width="5"/>' + g(cross(46), 57, 132) + g(check(56), 182, 6))
# fallacy: a cracked chain link
ela-7-evaluating-arguments/fallacy = chain(3, 340, broken=1)
# irrelevant: a puzzle piece that does not fit
ela-7-evaluating-arguments/irrelevant = puzzle(300, BLUE, ORANGE, fits=False)
# delineate: an outline with numbered parts
ela-7-evaluating-arguments/delineate = box(col(*[row(T(i, 40, BLUE), raw(200 - (i % 2) * 40, 14, '<rect width="200" height="14" rx="7" fill="#8a8f9c"/>'), gap=12) for i in (1, 2, 3)], row(Item(40, 10, ''), raw(160, 14, '<rect width="160" height="14" rx="7" fill="#c4c8d0"/>'), gap=12), gap=16, align='l'), color=DARK, fill='#fff')
# accuracy: a target with an arrow
ela-7-fiction-vs-history/accuracy = target(260)
# alter: a square, then the same square changed: new color, rounded corners
ela-7-fiction-vs-history/alter = row(box(w=130, h=130, color=BLUE, rx=4), arrow(70, ORANGE), box(w=130, h=130, color=PURPLE, rx=44), gap=12)
# classification: three labeled bins
ela-7-informative-writing/classification = row(*[col(T(w, 30, c), raw(120, 120, f'<path d="M6 10 H114 L102 116 H18 Z" fill="{soft(c)}" stroke="{c}" stroke-width="6" stroke-linejoin="round"/>'), gap=6) for w, c in (('A', BLUE), ('B', ORANGE), ('C', GREEN))], gap=16)
# heading: a page with bold section titles
ela-7-informative-writing/heading = para_page(240, paras=(2, 3, 3), bold_first=True, title=True)
# precise: a target with an arrow dead center
ela-7-informative-writing/precise = row(tile('nice', GRAY, 100, dashed=True, fill='#f4f5f7'), arrow(70, sw=10), tile('brave', BLUE, 120), gap=12)
# compound sentence: two blocks joined by a plus
ela-7-phrases-clauses-and-sentence-types/compound-sentence = row(box(w=120, h=90, color=BLUE), T('+', 80), box(w=120, h=90, color=ORANGE), gap=12)
# complex sentence: a big block with a smaller block attached
ela-7-phrases-clauses-and-sentence-types/complex-sentence = row(box(w=200, h=140, color=BLUE), box(w=90, h=70, color=ORANGE), gap=0)
# interplay: two gears turning together
ela-7-setting-plot-and-character-interplay/interplay = row(gear(170, BLUE), gear(130, ORANGE), gap=-16)
# rhyme scheme: four lines labeled A B A B
ela-7-sound-and-form-in-poetry/rhyme-scheme = col(*[row(raw(220, 14, f'<rect width="{220 - (i % 2) * 40}" height="14" rx="7" fill="#8a8f9c"/>'), T(c, 50, BLUE if c == 'A' else ORANGE), gap=14) for i, c in enumerate('ABAB')], gap=18, align='l')
# meter: a pattern of short and long marks
ela-7-sound-and-form-in-poetry/meter = row(*[raw(w, 40, f'<rect x="0" y="0" width="{w}" height="40" rx="20" fill="{c}"/>') for w, c in ((40, BLUE), (110, ORANGE), (40, BLUE), (110, ORANGE), (40, BLUE), (110, ORANGE))], gap=10)
# free verse: uneven lines of text
ela-7-sound-and-form-in-poetry/free-verse = col(*[raw(320, 16, f'<rect x="{x}" y="0" width="{w}" height="16" rx="8" fill="#8a8f9c"/>') for x, w in ((0, 300), (40, 140), (0, 220), (60, 260), (20, 90))], gap=22, align='l')
# structure: stacked building blocks
ela-8-analyzing-structure-and-paragraphs/structure = col(row(cube_icon(80, BLUE), gap=0), row(cube_icon(80, ORANGE), cube_icon(80, GREEN), gap=0), row(cube_icon(80, PURPLE), cube_icon(80, RED), cube_icon(80, YELLOW), gap=0), gap=0)
# refine: a rough stone becoming a gem
ela-8-analyzing-structure-and-paragraphs/refine = row(raw(140, 120, '<path d="M20 100 L10 60 L40 20 L90 10 L130 40 L120 90 L80 110 Z" fill="#9aa5b8" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>'), arrow(70), raw(140, 130, '<path d="M30 10 H110 L134 44 L70 124 L6 44 Z" fill="#7fd0f0" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M6 44 H134 M30 10 L50 44 L70 124 L90 44 L110 10" fill="none" stroke="#1f2430" stroke-width="3"/>'), gap=10)
# key sentence: a paragraph with one sentence boxed
ela-8-analyzing-structure-and-paragraphs/key-sentence = page(240, lines=7, boxed=(3,))
# topic sentence: a paragraph with the first line bold
ela-8-analyzing-structure-and-paragraphs/topic-sentence = page(240, lines=7, bold=(0,))
# function: a gear inside a page
ela-8-analyzing-structure-and-paragraphs/function = over(page(240, lines=7), gear(120, ORANGE))
# coherence: links of a smooth chain
ela-8-analyzing-structure-and-paragraphs/coherence = chain(4, 340, color=BLUE)
# opposing claim: two arrows pointing at each other
ela-8-argument-and-rebuttal/opposing-claim = row(arrow(140, BLUE, sw=10), arrow(140, ORANGE, 'left', sw=10), gap=10)
# rebuttal: an arrow bouncing back
ela-8-argument-and-rebuttal/rebuttal = raw(320, 220, '<rect x="270" y="20" width="30" height="190" rx="6" fill="#8a8f9c" stroke="#1f2430" stroke-width="5"/><path d="M20 60 L240 110" stroke="#3a7bd5" stroke-width="9" stroke-linecap="round"/><path d="M240 120 L40 180" stroke="#f08a24" stroke-width="9" stroke-linecap="round"/><path d="M24 186 l26 -20 l6 22 z" fill="#f08a24"/>')
# concede: a white flag
ela-8-argument-and-rebuttal/concede = flag(260, white=True)
# logical fallacy: a broken chain link
ela-8-argument-and-rebuttal/logical-fallacy = chain(3, 340, broken=1)
# persuasive: a balance tipped to one side
ela-8-argument-and-rebuttal/persuasive = scale_icon(300, ball(50, BLUE), None, tilt=26)
# corroborate: two documents with matching checks
ela-8-conflicting-information/corroborate = row(*[col(page(150, lines=5), check(60), gap=-30) for _ in range(2)], gap=30)
# dialogue: two speech bubbles
ela-8-dialogue-and-dramatic-irony/dialogue = row(bubble(dots(3, size=26), color=BLUE), bubble(dots(3, size=26, color=ORANGE), color=ORANGE, tail='right'), gap=14)
# hero's journey: a circle path with stops
ela-8-modern-takes-on-classic-stories/hero-s-journey = cycle([star(70), house(70), mountain(80), trophy(70), house(70, BLUE)], r=140)
# point of view: two eyes facing each other
ela-8-narrative-techniques/point-of-view = row(eye(130, look=14), Item(80, 10, ''), raw(130, 76, f'<g transform="translate(130 0) scale(-1 1)">{eye(130, look=14).svg}</g>'), gap=0)
# eye contact: two eyes with a line to rows of seats
ela-8-presentations-and-media/eye-contact = raw(400, 260, g(eye(110), 10, 20) + '<path d="M130 56 L380 150" stroke="#f08a24" stroke-width="5" stroke-dasharray="12 8"/>' + ''.join(f'<rect x="{200 + c * 40 + r * 10}" y="{150 + r * 34}" width="30" height="24" rx="6" fill="{BLUE}" stroke="#1f2430" stroke-width="3"/>' for r in range(3) for c in range(4)))
# multimedia: icons for text, image, sound and video
ela-8-presentations-and-media/multimedia = grid([card(page(60, lines=3), 110, 110, BLUE), card(row(sun(40), mountain(60), gap=-10), 110, 110, ORANGE), card(raw(60, 60, '<circle cx="18" cy="46" r="12" fill="#1f2430"/><line x1="29" y1="46" x2="29" y2="6" stroke="#1f2430" stroke-width="6"/><path d="M29 6 C40 14 54 14 54 28" fill="none" stroke="#1f2430" stroke-width="6"/>'), 110, 110, GREEN), card(raw(70, 60, '<rect x="2" y="6" width="66" height="48" rx="8" fill="#1f2430"/><path d="M28 18 L50 30 L28 42 Z" fill="#fff"/>'), 110, 110, PURPLE)], 2)
# title: a book cover with a bold title bar
ela-k-all-about-books/title = raw(220, 290, '<rect x="10" y="10" width="200" height="270" rx="10" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><rect x="10" y="10" width="26" height="270" fill="#1f2430" opacity="0.25"/><rect x="50" y="50" width="140" height="34" rx="6" fill="#fff"/><rect x="70" y="100" width="100" height="14" rx="6" fill="#fff" opacity="0.7"/>' + g(star(80), 80, 160))
# label: a drawing of a tree with an arrow pointing to a word tag
ela-k-draw-tell-and-write/label = row(tree(170), arrow(70, dir='left'), box(T('tree', 44), color=ORANGE, p=12), gap=8)
# sight word: the word the on a flash card with a star
ela-k-letter-sounds-and-sight-words/sight-word = over(card(T('the', 90), 260, 190, BLUE), star(70), dx=110, dy=-80)
# vowel: the letters a e i o u on bright tiles
ela-k-letter-sounds-and-sight-words/vowel = tiles('a', 'e', 'i', 'o', 'u', size=100, colors=[RED, ORANGE, GREEN, BLUE, PURPLE])
# consonant: the letters b, t and m on tiles
ela-k-letter-sounds-and-sight-words/consonant = tiles('b', 't', 'm', size=120, colors=[BLUE, ORANGE, GREEN])
# sound out: three sound dots joined by a swoosh arrow
ela-k-letter-sounds-and-sight-words/sound-out = col(row(*[col(dot(50, c), T(s, 40)) for s, c in (('c', BLUE), ('a', ORANGE), ('t', GREEN))], gap=40), raw(320, 40, '<path d="M10 10 Q160 50 300 10" fill="none" stroke="#e04848" stroke-width="7"/><path d="M314 4 l-22 -4 l6 20 z" fill="#e04848"/>'), gap=0)
# blend: three letter tiles sliding together
ela-k-letter-sounds-and-sight-words/blend = col(row(tile('s', BLUE, 100), arrow(40), tile('u', ORANGE, 100), arrow(40, dir='left'), tile('n', GREEN, 100), gap=4), arrow(40, dir='down'), tiles('s', 'u', 'n', colors=[BLUE, ORANGE, GREEN], size=100, gap=0), gap=10)
# letter: a big letter A on a tile
ela-k-print-concepts-and-the-alphabet/letter = tile('A', RED, 260)
# alphabet: letter blocks A B C in a row
ela-k-print-concepts-and-the-alphabet/alphabet = tiles('A', 'B', 'C', size=130, colors=[RED, BLUE, GREEN])
# word: the letters c, a, t joined into one word
ela-k-print-concepts-and-the-alphabet/word = col(tiles('c', 'a', 't', size=100, colors=[BLUE, ORANGE, GREEN], gap=20), arrow(50, dir='down'), T('cat', 110), gap=8)
# space: two words with a finger-wide gap between them
ela-k-print-concepts-and-the-alphabet/space = row(T('I', 110), raw(80, 110, '<rect x="10" y="10" width="60" height="90" rx="14" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="10 7"/>'), T('ran', 110), gap=6)
# uppercase: a big B next to a small b with the big one highlighted
ela-k-print-concepts-and-the-alphabet/uppercase = row(mark(T('B', 200, BLUE), 'box', ORANGE), T('b', 100, GRAY), gap=20, align='b')
# lowercase: a big B next to a small b with the small one highlighted
ela-k-print-concepts-and-the-alphabet/lowercase = row(T('B', 200, GRAY), mark(T('b', 100, BLUE), 'box', ORANGE), gap=20, align='b')
# left to right: an arrow going across lines of text from left to right
ela-k-print-concepts-and-the-alphabet/left-to-right = col(*[raw(320, 14, '<rect width="320" height="14" rx="7" fill="#8a8f9c"/>') for _ in range(3)], arrow(320, ORANGE, sw=10), gap=18)
# syllable: an apple with two clap marks above it
ela-k-rhymes-and-sounds/syllable = col(row(raw(60, 50, '<path d="M8 40 L30 6 L52 40" fill="none" stroke="#f08a24" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'), raw(60, 50, '<path d="M8 40 L30 6 L52 40" fill="none" stroke="#f08a24" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'), gap=30), apple(200), T('ap · ple', 60), gap=10)
# clap: two hands meeting with small motion lines
ela-k-rhymes-and-sounds/clap = row(hand(130, 'flat'), raw(70, 120, '<path d="M10 20 l20 14 M6 60 h26 M10 100 l20 -14 M60 20 l-20 14 M64 60 h-26 M60 100 l-20 -14" stroke="#3a7bd5" stroke-width="6" stroke-linecap="round"/>'), raw(90, 114, f'<g transform="translate(90 0) scale(-1 1)">{hand(130, "flat").svg}</g>'), gap=0)
# retell: a speech bubble with a small book inside
ela-k-story-time-characters-and-setting/retell = bubble(book(120), size=240, color=BLUE)
# beginning: a book with its first page highlighted
ela-k-story-time-characters-and-setting/beginning = book(280, hl=[0])
# listen: a big ear with sound waves
ela-k-talk-it-over/listen = ear(240)
# question: a big question mark in a speech bubble
ela-k-talk-it-over/question = bubble(T('?', 130, BLUE), size=240, color=BLUE)
# answer: a speech bubble with a check mark
ela-k-talk-it-over/answer = bubble(check(120), size=240, color=GREEN)
# take turns: two speech bubbles with arrows going back and forth
ela-k-talk-it-over/take-turns = col(row(bubble(dots(3, size=22), 150, BLUE), bubble(dots(3, size=22, color=ORANGE), 150, ORANGE, tail='right'), gap=10), harrows(DARK, 120), gap=0)
# speak: a speech bubble coming out of a microphone
ela-k-talk-it-over/speak = row(raw(90, 200, '<rect x="20" y="10" width="50" height="90" rx="25" fill="#8a8f9c" stroke="#1f2430" stroke-width="6"/><path d="M10 80 C10 130 80 130 80 80" fill="none" stroke="#1f2430" stroke-width="6"/><line x1="45" y1="122" x2="45" y2="170" stroke="#1f2430" stroke-width="7"/><rect x="20" y="168" width="50" height="10" rx="4" fill="#1f2430"/>'), bubble(dots(3, size=26), 180, BLUE), gap=0, align='t')
# sentence: a row of word blocks ending with a period
ela-k-words-and-sentences/sentence = row(tile('I', BLUE, 90), tile('see', ORANGE, 90), tile('a', GREEN, 90), tile('dog', PURPLE, 90), dot(34, RED), gap=8, align='b')
# capital: The cat ran. with a red capital T
ela-k-words-and-sentences/capital = T('The cat ran.', 90, hl={'T': RED})
# period: a big dot at the end of a line of words
ela-k-words-and-sentences/period = row(raw(260, 20, '<rect x="0" y="4" width="260" height="14" rx="7" fill="#8a8f9c"/>'), raw(60, 60, '<circle cx="30" cy="38" r="20" fill="#e04848"/>'), gap=6, align='b')
# agree: two speech bubbles with matching check marks
eld-3-5-academic-conversations/agree = row(bubble(check(70), color=BLUE), bubble(check(70), color=ORANGE, tail='right'), gap=14)
# disagree: two speech bubbles, one with a check and one with an X
eld-3-5-academic-conversations/disagree = row(bubble(check(70), color=BLUE), bubble(cross(60), color=ORANGE, tail='right'), gap=14)
# build on: one block stacked on top of another
eld-3-5-academic-conversations/build-on = col(box(w=150, h=90, color=ORANGE), box(w=210, h=90, color=BLUE), gap=0)
# clarify: a blurry circle becoming a sharp circle
eld-3-5-academic-conversations/clarify = row(raw(120, 120, '<defs><filter id="bl"><feGaussianBlur stdDeviation="7"/></filter></defs><circle cx="60" cy="60" r="44" fill="#3a7bd5" filter="url(#bl)"/>'), arrow(70), shape('circle', 110, BLUE), gap=10)
# respond: two speech bubbles with an arrow between them
eld-3-5-academic-conversations/respond = row(bubble(dots(3, size=24), 150, BLUE), arrow(60), bubble(dots(3, size=24, color=ORANGE), 150, ORANGE, tail='right'), gap=6)
# strategy: a question mark, then a plan card with three numbered checked steps
eld-3-5-explaining-my-solution/strategy = row(qmark(110), arrow(50), box(col(*[row(tile(str(i), BLUE, 44), raw(90, 14, '<rect width="90" height="14" rx="7" fill="#c9ced8"/>'), check(36), gap=8) for i in (1, 2, 3)], gap=10), color=GRAY, fill='#fff', p=14), gap=10)
# first: a numbered step 1
eld-3-5-explaining-my-solution/first = box(T('1', 160, BLUE), w=220, h=220, color=BLUE)
# next: an arrow from step 1 to step 2
eld-3-5-explaining-my-solution/next = row(box(T('1', 90, BLUE), w=130, h=130, color=BLUE), arrow(80), box(T('2', 90, ORANGE), w=130, h=130, color=ORANGE), gap=10)
# finally: a last step with a check mark
eld-3-5-explaining-my-solution/finally = row(box(T('3', 110, GREEN), w=160, h=160, color=GREEN), check(120), gap=10)
# solution: 8 + 5 = 13 with the answer boxed
eld-3-5-explaining-my-solution/solution = row(M('8 + 5 =', 90), mark(M('13', 90), 'box', RED), gap=10)
# explain: a speech bubble with a question mark and an arrow
eld-3-5-explaining-my-solution/explain = row(bubble(T('?', 90, BLUE), 170, BLUE), arrow(80), lightbulb_on(120), gap=10)
# reason: a lightbulb next to a "because" arrow
eld-3-5-opinions-with-reasons/reason = row(lightbulb_on(130), col(T('because', 44, ORANGE), arrow(160, ORANGE, sw=8), gap=0), gap=10)
# in conclusion: a page with its last paragraph highlighted
eld-3-5-opinions-with-reasons/in-conclusion = para_page(240, paras=(3, 3, 3), hl_para=(2,))
# change over time: an old rotary phone next to a smartphone
eld-3-5-then-and-now-language/change-over-time = row(raw(170, 140, '<path d="M10 120 L30 60 H140 L160 120 Z" fill="#e04848" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><circle cx="85" cy="90" r="26" fill="#fff" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<circle cx="{85 + 17 * math.cos(a):.1f}" cy="{90 + 17 * math.sin(a):.1f}" r="4" fill="#1f2430"/>' for a in [k * math.pi / 5 for k in range(10)]) + '<path d="M10 40 C10 10 160 10 160 40 L140 50 L120 36 H50 L30 50 Z" fill="#e04848" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>'), arrow(70), phone(170, inner=grid([box(w=20, h=20, color=c, rx=4, sw=0, fill=c) for c in (BLUE, ORANGE, GREEN, PURPLE, RED, YELLOW)], 2, gap=5)), gap=10)
# similarly: two matching arrows
eld-6-8-comparing-perspectives/similarly = col(arrow(220, BLUE, sw=10), arrow(220, BLUE, sw=10), gap=30)
# in contrast: two arrows pointing opposite ways
eld-6-8-comparing-perspectives/in-contrast = col(arrow(220, BLUE, sw=10), arrow(220, ORANGE, 'left', sw=10), gap=30)
# whereas: two different boxes side by side
eld-6-8-comparing-perspectives/whereas = row(box(shape('circle', 80, BLUE), w=150, h=150, color=BLUE), box(shape('triangle', 80, ORANGE), w=150, h=150, color=ORANGE), gap=24)
# viewpoint: an eye looking at a question mark
eld-6-8-comparing-perspectives/viewpoint = row(eye(150), T('?', 160, ORANGE), gap=20)
# slang: a speech bubble with a wink
eld-6-8-idioms-and-everyday-expressions/slang = bubble(face(110, 'wink'), size=240, color=PURPLE)
# reasoning: a chain linking two boxes
eld-6-8-lab-reports-and-claims/reasoning = row(box(w=110, h=110, color=BLUE), chain(2, 130), box(w=110, h=110, color=ORANGE), gap=-6)
# data shows: a line graph going down
eld-6-8-lab-reports-and-claims/data-shows = plot(lambda x: 8 - 0.7 * x + 0.6 * math.sin(x * 1.7), size=320, xr=(0, 10), yr=(0, 10), colors=(RED,), points=[(x, 8 - 0.7 * x + 0.6 * math.sin(x * 1.7), RED) for x in (1, 3, 5, 7, 9)])
# summarize: a long page shrinking into a short card
eld-6-8-summarizing-and-citing/summarize = row(page(220, lines=10), arrow(80), card(raw(80, 30, '<rect x="0" y="0" width="80" height="10" rx="5" fill="#8a8f9c"/><rect x="0" y="20" width="56" height="10" rx="5" fill="#8a8f9c"/>'), 120, 90, ORANGE), gap=10)
# cite: a quote with a small source tag
eld-6-8-summarizing-and-citing/cite = row(T('“', 110, BLUE), raw(180, 16, '<rect width="180" height="16" rx="8" fill="#8a8f9c"/>'), T('”', 110, BLUE), raw(90, 56, '<path d="M4 28 L20 6 H86 V50 H20 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><text x="52" y="38" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">(1)</text>'), gap=4)
# central idea: a bullseye target
eld-6-8-summarizing-and-citing/central-idea = target(270, arrow_=False)
# objective: a level balance scale
eld-6-8-summarizing-and-citing/objective = scale_icon(300)
# paraphrase: one speech bubble becoming another
eld-6-8-summarizing-and-citing/paraphrase = row(bubble(dots(3, size=24), 150, BLUE), arrow(60), bubble(dots(3, size=24, color=ORANGE), 150, ORANGE, tail='right'), gap=6)
# at least: a number line with a closed dot at 5 and an arrow right
eld-6-8-word-problems-decoded/at-least = numberline(0, 10, 440, closed=5, ray='right', color=BLUE)
# line up: footprints in a row by a door
eld-k-2-classroom-language/line-up = row(footprints(4, 70), door(170), gap=20, align='b')
# raise your hand: a hand raised high
eld-k-2-classroom-language/raise-your-hand = col(raw(60, 60, '<path d="M30 50 V10 M14 24 L30 8 L46 24" fill="none" stroke="#3a7bd5" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'), hand(230), gap=0)
# help: an open hand raised beside a help? bubble
eld-k-2-classroom-language/help = row(hand(170, 'open'), bubble(T('help?', 44), 170, tail='left'), gap=6, align='t')
# turn: two faces with a curved arrow passing to the second, now circled
eld-k-2-classroom-language/turn = row(face(100), curve_arrow(40, ORANGE), mark(face(100), 'circle', ORANGE), gap=10)
# repeat: a speech bubble with a circular arrow
eld-k-2-classroom-language/repeat = bubble(curve_arrow(50, ORANGE), size=240, color=BLUE)
# partner: two chairs side by side at a small table
eld-k-2-classroom-language/partner = raw(360, 240, '<rect x="110" y="90" width="140" height="20" rx="6" fill="#a0673a" stroke="#1f2430" stroke-width="5"/><path d="M130 110 V200 M230 110 V200" stroke="#1f2430" stroke-width="8"/>' + ''.join(f'<g transform="translate({x} 60)"><rect x="0" y="0" width="16" height="140" rx="4" fill="{c}" stroke="#1f2430" stroke-width="4"/><rect x="{0 if x < 180 else -50}" y="80" width="66" height="16" rx="4" fill="{c}" stroke="#1f2430" stroke-width="4"/><path d="M{60 if x < 180 else -44} 96 V140" stroke="#1f2430" stroke-width="6"/></g>' for x, c in ((20, BLUE), (324, ORANGE))))
# number: the number 7 and seven dots
eld-k-2-math-talk-numbers-and-shapes/number = row(T('7', 200, BLUE), dots(7, 4, 44, ORANGE), gap=30)
# shape: a circle, a square and a triangle
eld-k-2-math-talk-numbers-and-shapes/shape = row(shape('circle', 110, BLUE), shape('square', 110, ORANGE), shape('triangle', 110, GREEN), gap=20)
# equal: two cups with 4 beads each
eld-k-2-math-talk-numbers-and-shapes/equal = row(cup(150, inner=dots(4, 2, 30, ORANGE)), T('=', 90), cup(150, inner=dots(4, 2, 30, ORANGE)), gap=14)
# corner: a triangle with dots on its corners
eld-k-2-math-talk-numbers-and-shapes/corner = triangle(300, fill=soft(BLUE)) if 0 else poly(3, 300, GREEN, dots_=True)
# then: an arrow from one picture card to the next
eld-k-2-retelling-stories/then = row(card(egg(70), 130, 160, BLUE), arrow(80), card(duck(90), 130, 160, ORANGE), gap=10)
# problem: a frog with a question mark above it
eld-k-2-retelling-stories/problem = col(T('?', 110, RED), frog(220), gap=-10)
# tell: a speech bubble with a small book inside
eld-k-2-retelling-stories/tell = bubble(book(120), size=240, color=BLUE)
# heart rate: a heart with a pulse line
health-pe-3-5-fitness-components/heart-rate = row(heart(170), raw(200, 100, '<path d="M0 60 H50 L66 20 L86 96 L104 4 L122 80 L136 60 H200" fill="none" stroke="#e04848" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'), gap=0)
# open space: a field with dots and one empty area circled
health-pe-3-5-game-strategies/open-space = raw(360, 260, '<rect x="5" y="5" width="350" height="250" rx="14" fill="#d3f0de" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="{BLUE if i % 2 else ORANGE}" stroke="#1f2430" stroke-width="3"/>' for i, (x, y) in enumerate(((40, 40), (100, 70), (60, 150), (130, 210), (40, 220), (160, 40), (310, 220), (300, 40), (330, 120), (180, 200)))) + '<circle cx="240" cy="120" r="56" fill="none" stroke="#e04848" stroke-width="6" stroke-dasharray="12 8"/>')
# strategy: a whiteboard with Xs and Os
health-pe-3-5-game-strategies/strategy = raw(340, 240, '<rect x="5" y="5" width="330" height="230" rx="10" fill="#fff" stroke="#1f2430" stroke-width="7"/>' + ''.join(f'<path d="M{x - 18} {y - 18} L{x + 18} {y + 18} M{x + 18} {y - 18} L{x - 18} {y + 18}" stroke="#3a7bd5" stroke-width="7" stroke-linecap="round"/>' for x, y in ((60, 60), (90, 170), (180, 100))) + ''.join(f'<circle cx="{x}" cy="{y}" r="20" fill="none" stroke="#e04848" stroke-width="7"/>' for x, y in ((260, 60), (280, 170))) + '<path d="M80 80 Q140 40 240 70" fill="none" stroke="#2f9e5b" stroke-width="5" stroke-dasharray="10 7"/><path d="M246 72 l-18 -10 l2 18 z" fill="#2f9e5b"/>')
# teamwork: four arrows meeting at a star
health-pe-3-5-game-strategies/teamwork = over(raw(320, 320, ''.join(f'<line x1="{160 + 150 * math.cos(a):.1f}" y1="{160 + 150 * math.sin(a):.1f}" x2="{160 + 64 * math.cos(a):.1f}" y2="{160 + 64 * math.sin(a):.1f}" stroke="{c}" stroke-width="12" stroke-linecap="round"/><path d="M{160 + 44 * math.cos(a):.1f} {160 + 44 * math.sin(a):.1f} L{160 + 76 * math.cos(a) - 18 * math.sin(a):.1f} {160 + 76 * math.sin(a) + 18 * math.cos(a):.1f} L{160 + 76 * math.cos(a) + 18 * math.sin(a):.1f} {160 + 76 * math.sin(a) - 18 * math.cos(a):.1f} Z" fill="{c}"/>' for a, c in zip([math.pi / 4 + k * math.pi / 2 for k in range(4)], (BLUE, ORANGE, GREEN, PURPLE)))), star(90))
# germ: a hand with a magnifier showing tiny germs on it
health-pe-3-5-germs-and-disease-prevention/germ = over(hand(220, 'open'), magnifier(120, inner=raw(70, 70, ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/>' for x, y in ((18, 20), (48, 16), (30, 46), (56, 50))))), dx=60, dy=50)
# bacteria: rod-shaped cells under a microscope circle
health-pe-3-5-germs-and-disease-prevention/bacteria = raw(300, 300, '<circle cx="150" cy="150" r="140" fill="#fbfff4" stroke="#1f2430" stroke-width="10"/>' + ''.join(f'<rect x="{x}" y="{y}" width="60" height="22" rx="11" fill="#2f9e5b" stroke="#1f2430" stroke-width="3" transform="rotate({r} {x + 30} {y + 11})"/>' for x, y, r in ((60, 90, 20), (160, 70, -30), (110, 150, 70), (180, 170, 10), (70, 200, -15), (150, 230, 40), (200, 120, 80))))
# virus: a round virus particle with spikes
health-pe-3-5-germs-and-disease-prevention/virus = raw(260, 260, ''.join(f'<line x1="{130 + 70 * math.cos(a):.1f}" y1="{130 + 70 * math.sin(a):.1f}" x2="{130 + 110 * math.cos(a):.1f}" y2="{130 + 110 * math.sin(a):.1f}" stroke="#1f2430" stroke-width="6"/><circle cx="{130 + 114 * math.cos(a):.1f}" cy="{130 + 114 * math.sin(a):.1f}" r="11" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' for a in [k * math.pi / 6 for k in range(12)]) + '<circle cx="130" cy="130" r="78" fill="#8e5bc4" stroke="#1f2430" stroke-width="6"/><circle cx="110" cy="110" r="14" fill="#b893e0"/><circle cx="155" cy="150" r="10" fill="#b893e0"/>')
# immune system: a shield blocking dots
health-pe-3-5-germs-and-disease-prevention/immune-system = row(shield(220, BLUE), col(*[dot(26, GREEN) for _ in range(4)], gap=18), gap=-120) if 0 else raw(340, 260, g(shield(230, BLUE, inner=heart(80)), 0, 10) + ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/><path d="M{x - 16} {y} l-14 0" stroke="#8a8f9c" stroke-width="4"/>' for x, y in ((260, 50), (300, 110), (250, 170), (310, 220))))
# hormones: a messenger envelope traveling a path
health-pe-3-5-growing-up/hormones = raw(380, 240, '<path d="M30 200 C120 200 80 40 200 40 C300 40 260 200 350 200" fill="none" stroke="#8a8f9c" stroke-width="8" stroke-dasharray="14 10"/><circle cx="30" cy="200" r="18" fill="#8e5bc4" stroke="#1f2430" stroke-width="4"/><circle cx="350" cy="200" r="18" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/>' + g(envelope(110), 150, 10))
# trusted adult: a speech bubble with a heart
health-pe-3-5-growing-up/trusted-adult = bubble(heart(110), size=240, color=BLUE)
# body system: an outline of a stomach and intestines
health-pe-3-5-the-human-body-systems/body-system = torso(300, inner=stomach(150))
# organ: a simple heart organ outline
health-pe-3-5-the-human-body-systems/organ = heart_organ(260)
# circulatory system: a heart with red and blue vessels
health-pe-3-5-the-human-body-systems/circulatory-system = heart_organ(280, vessels=True)
# respiratory system: a pair of lungs
health-pe-3-5-the-human-body-systems/respiratory-system = lungs(280)
# skeletal system: a simple skeleton outline
health-pe-3-5-the-human-body-systems/skeletal-system = paint('a friendly cartoon human skeleton standing front view, clear skull, ribs, spine, arm and leg bones, plain white background')
# muscles: a muscle outline on an arm bone
health-pe-3-5-the-human-body-systems/muscles = paint('a bent upper arm cut-away showing the red biceps muscle attached to the white arm bones')
# digital footprint: a footprint made of pixels
health-pe-6-8-digital-wellness/digital-footprint = raw(240, 320, ''.join(f'<rect x="{20 + c * 25}" y="{90 + r * 25}" width="23" height="23" fill="{BLUE if (c + r) % 3 else '#6aa0e8'}"/>' for r in range(9) for c in range(8) if ((c - 3.5) / 4.0) ** 2 + ((r - 4) / 4.6) ** 2 <= 1) + ''.join(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{BLUE}"/>' for x, y, s in ((24, 46, 36), (72, 22, 28), (110, 18, 26), (146, 24, 24), (180, 40, 22))))
# privacy settings: a toggle switch and a lock
health-pe-6-8-digital-wellness/privacy-settings = row(toggle(True, 200), lock(150), gap=30)
# cyberbullying: a phone with an angry message bubble
health-pe-6-8-digital-wellness/cyberbullying = phone(260, inner=bubble(row(T('!', 70, RED), face(70, 'angry'), gap=4), 150, RED))
# algorithm: a funnel sorting video tiles
health-pe-6-8-digital-wellness/algorithm = row(funnel(180), arrow(60), col(*[box(raw(40, 40, '<path d="M10 4 L36 20 L10 36 Z" fill="#fff"/>'), w=80, h=60, color=c, fill=c, sw=0, p=0) for c in (BLUE, ORANGE, GREEN)], gap=10), gap=10) if 0 else col(row(*[box(raw(30, 30, '<path d="M6 2 L28 15 L6 28 Z" fill="#fff"/>'), w=70, h=56, color=c, fill=c, sw=0, p=0) for c in (BLUE, ORANGE, GREEN, PURPLE)], gap=10), funnel(200), box(raw(30, 30, '<path d="M6 2 L28 15 L6 28 Z" fill="#fff"/>'), w=70, h=56, color=GREEN, fill=GREEN, sw=0, p=0), gap=6)
# boundary: a line with a hand raised
health-pe-6-8-healthy-relationships/boundary = row(raw(30, 300, '<line x1="15" y1="0" x2="15" y2="300" stroke="#e04848" stroke-width="10" stroke-dasharray="20 12" stroke-linecap="round"/>'), stop_hand(220), gap=20)
# communication: two speech bubbles linked
health-pe-6-8-healthy-relationships/communication = row(bubble(dots(3, size=24), 150, BLUE), chain(2, 90), bubble(dots(3, size=24, color=ORANGE), 150, ORANGE, tail='right'), gap=0)
# I-statement: a speech bubble beginning with I
health-pe-6-8-healthy-relationships/i-statement = bubble(row(T('I', 110, BLUE), raw(150, 60, '<rect y="10" width="150" height="14" rx="7" fill="#8a8f9c"/><rect y="40" width="100" height="14" rx="7" fill="#8a8f9c"/>'), gap=20), w=340, h=200, color=BLUE)
# respect: a handshake between two kind speech bubbles
health-pe-6-8-healthy-relationships/respect = col(row(bubble(T('please', 30), 140, tail='left'), bubble(T('thanks', 30), 140, color=ORANGE, tail='right'), gap=40), handshake(280), gap=4)
# conflict resolution: two arrows turning into a handshake shape
health-pe-6-8-healthy-relationships/conflict-resolution = col(row(arrow(110, BLUE, sw=10), arrow(110, ORANGE, 'left', sw=10), gap=10), arrow(60, dir='down'), handshake(200), gap=6)
# anxiety: a wavy line calming into a straight line
health-pe-6-8-mental-and-emotional-health/anxiety = raw(400, 160, '<path d="M10 80 ' + ' '.join(f'L{10 + i * 10} {80 + (50 if i % 2 else -50) * max(0, 1 - i / 22):.0f}' for i in range(1, 39)) + '" fill="none" stroke="#8e5bc4" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>')
# FITT: four boxes labeled F, I, T, T
health-pe-6-8-personal-fitness-plans/fitt = row(*[box(T(c, 70, '#fff'), w=100, h=100, color=k, fill=k) for c, k in (('F', BLUE), ('I', ORANGE), ('T', GREEN), ('T', PURPLE))], gap=12)
# frequency: a calendar with four days checked
health-pe-6-8-personal-fitness-plans/frequency = calendar(300, checks=(1, 3, 5, 8))
# target heart rate: a heart rate gauge with a green zone
health-pe-6-8-personal-fitness-plans/target-heart-rate = meter(300, 0.62, zone=(0.5, 0.75))
# sportsmanship: a handshake beside a trophy: good play win or lose
health-pe-6-8-sport-skills-and-rules/sportsmanship = row(handshake(250), trophy(110), gap=14)
# transition: arrows reversing direction on a court
health-pe-6-8-sport-skills-and-rules/transition = raw(400, 260, '<rect x="5" y="5" width="390" height="250" rx="10" fill="#f6dfbd" stroke="#1f2430" stroke-width="6"/><line x1="200" y1="5" x2="200" y2="255" stroke="#1f2430" stroke-width="5"/><circle cx="200" cy="130" r="40" fill="none" stroke="#1f2430" stroke-width="5"/><path d="M60 90 H300" stroke="#3a7bd5" stroke-width="12" stroke-linecap="round"/><path d="M330 90 l-34 -20 v40 z" fill="#3a7bd5"/><path d="M340 175 H100" stroke="#f08a24" stroke-width="12" stroke-linecap="round"/><path d="M70 175 l34 -20 v40 z" fill="#f08a24"/>')
# nicotine: a vape pen with a warning sign
health-pe-6-8-substance-use-prevention/nicotine = row(raw(80, 300, '<rect x="20" y="20" width="40" height="270" rx="16" fill="#8a8f9c" stroke="#1f2430" stroke-width="6"/><rect x="28" y="40" width="24" height="60" rx="8" fill="#7fd0f0" stroke="#1f2430" stroke-width="4"/><rect x="30" y="6" width="20" height="20" rx="4" fill="#1f2430"/>'), warning(170), gap=20)
# addiction: a chain wrapped around a box
health-pe-6-8-substance-use-prevention/addiction = over(crate(220), chain(4, 280), dy=0)
# vaping: a vape device with a cloud
health-pe-6-8-substance-use-prevention/vaping = row(raw(80, 300, '<rect x="20" y="20" width="40" height="270" rx="16" fill="#8a8f9c" stroke="#1f2430" stroke-width="6"/><rect x="28" y="40" width="24" height="60" rx="8" fill="#7fd0f0" stroke="#1f2430" stroke-width="4"/><rect x="30" y="6" width="20" height="20" rx="4" fill="#1f2430"/>'), cloud(200, '#e8ebf0'), gap=-10, align='t')
# refusal skills: a stop hand
health-pe-6-8-substance-use-prevention/refusal-skills = stop_hand(280)
# peer pressure: several arrows pointing at one dot
health-pe-6-8-substance-use-prevention/peer-pressure = raw(320, 320, ''.join(f'<line x1="{160 + 150 * math.cos(a):.1f}" y1="{160 + 150 * math.sin(a):.1f}" x2="{160 + 60 * math.cos(a):.1f}" y2="{160 + 60 * math.sin(a):.1f}" stroke="#e04848" stroke-width="10" stroke-linecap="round"/><path d="M{160 + 40 * math.cos(a):.1f} {160 + 40 * math.sin(a):.1f} L{160 + 70 * math.cos(a) - 16 * math.sin(a):.1f} {160 + 70 * math.sin(a) + 16 * math.cos(a):.1f} L{160 + 70 * math.cos(a) + 16 * math.sin(a):.1f} {160 + 70 * math.sin(a) - 16 * math.cos(a):.1f} Z" fill="#e04848"/>' for a in [k * 2 * math.pi / 6 for k in range(6)]) + '<circle cx="160" cy="160" r="26" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>')
# consequence: a domino chain falling
health-pe-6-8-substance-use-prevention/consequence = raw(420, 220, ''.join(f'<g transform="rotate({ang} {30 + i * 70} 200)"><rect x="{12 + i * 70}" y="60" width="36" height="140" rx="6" fill="#fff" stroke="#1f2430" stroke-width="5"/><circle cx="{30 + i * 70}" cy="100" r="7" fill="#1f2430"/><circle cx="{30 + i * 70}" cy="160" r="7" fill="#1f2430"/><line x1="{14 + i * 70}" y1="130" x2="{46 + i * 70}" y2="130" stroke="#1f2430" stroke-width="4"/></g>' for i, ang in enumerate((60, 50, 38, 20, 0, 0))))
# feeling: four simple faces showing feelings
health-pe-k-2-feelings-and-friends/feeling = grid([face(120, 'happy'), face(120, 'sad'), face(120, 'angry'), face(120, 'surprised')], 2, gap=24)
# kind words: a speech bubble with a heart
health-pe-k-2-feelings-and-friends/kind-words = bubble(heart(110), size=240, color=PINK)
# ask for help: a raised hand with a heart
health-pe-k-2-feelings-and-friends/ask-for-help = row(hand(200), heart(110), gap=0, align='t')
# sorry: a speech bubble with a small bandage
health-pe-k-2-feelings-and-friends/sorry = bubble(raw(140, 70, '<g transform="rotate(-25 70 35)"><rect x="5" y="15" width="130" height="40" rx="20" fill="#f6d6bd" stroke="#1f2430" stroke-width="5"/><rect x="50" y="15" width="40" height="40" fill="#fbe9dc" stroke="#1f2430" stroke-width="3"/><circle cx="60" cy="27" r="3" fill="#c98b4f"/><circle cx="80" cy="27" r="3" fill="#c98b4f"/><circle cx="60" cy="43" r="3" fill="#c98b4f"/><circle cx="80" cy="43" r="3" fill="#c98b4f"/></g>'), size=240, color=BLUE)
# balanced meal: a plate split into four colored parts
health-pe-k-2-food-groups/balanced-meal = paint('a dinner plate seen from above divided into vegetables, fruit, grains and protein, with a glass of milk beside it')
# germs: tiny cartoon dots being washed away by bubbles
health-pe-k-2-healthy-habits/germs = raw(360, 260, ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d6f0fb" stroke="#3a7bd5" stroke-width="4"/><path d="M{x - r * 0.5:.0f} {y - r * 0.4:.0f} a{r * 0.5:.0f} {r * 0.5:.0f} 0 0 1 {r * 0.5:.0f} -{r * 0.25:.0f}" fill="none" stroke="#fff" stroke-width="4"/>' for x, y, r in ((60, 180, 50), (140, 100, 40), (120, 210, 30), (210, 160, 44), (40, 80, 26))) + ''.join(f'<g><circle cx="{x}" cy="{y}" r="14" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/><circle cx="{x - 4}" cy="{y - 3}" r="2.5" fill="#1f2430"/><circle cx="{x + 4}" cy="{y - 3}" r="2.5" fill="#1f2430"/></g>' for x, y in ((290, 60), (330, 120), (280, 200), (320, 230))) + '<path d="M240 110 l30 -14 M246 160 l34 0 M240 210 l30 14" stroke="#8a8f9c" stroke-width="5" stroke-linecap="round"/>')
# stranger: a closed gate with a stop hand
health-pe-k-2-safety/stranger = row(raw(240, 240, '<rect x="10" y="40" width="16" height="200" fill="#8a8f9c" stroke="#1f2430" stroke-width="4"/><rect x="214" y="40" width="16" height="200" fill="#8a8f9c" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<rect x="{34 + i * 30}" y="70" width="12" height="160" fill="#a0673a" stroke="#1f2430" stroke-width="3"/>' for i in range(6)) + '<rect x="26" y="90" width="188" height="14" fill="#a0673a" stroke="#1f2430" stroke-width="3"/><rect x="26" y="190" width="188" height="14" fill="#a0673a" stroke="#1f2430" stroke-width="3"/>'), stop_hand(150), gap=10)
# underhand: an arc arrow starting low
health-pe-k-2-throwing-and-catching/underhand = raw(360, 260, '<circle cx="40" cy="220" r="22" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M60 230 C150 280 260 120 320 40" fill="none" stroke="#3a7bd5" stroke-width="10" stroke-linecap="round" stroke-dasharray="20 10"/><path d="M336 18 l-6 40 l-28 -22 z" fill="#3a7bd5"/>')
# overhand: an arc arrow starting high
health-pe-k-2-throwing-and-catching/overhand = raw(360, 260, '<circle cx="40" cy="40" r="22" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M60 30 C160 -10 280 60 320 220" fill="none" stroke="#3a7bd5" stroke-width="10" stroke-linecap="round" stroke-dasharray="20 10"/><path d="M326 246 l-26 -30 l34 -6 z" fill="#3a7bd5"/>')
# step: two footprints, one forward
health-pe-k-2-throwing-and-catching/step = raw(220, 320, f'<g transform="translate(20 180)">{footprint(110).svg}</g><g transform="translate(110 20)">{footprint(110, BLUE).svg}</g>' + '<path d="M180 280 V150" stroke="#3a7bd5" stroke-width="8" stroke-dasharray="12 8"/><path d="M180 130 l-16 26 h32 z" fill="#3a7bd5"/>')
# credit: a book with a ribbon badge
library-3-5-giving-credit/credit = row(book(200, open_=False), raw(110, 170, '<path d="M30 80 L14 168 L40 150 L58 168 L56 90 Z M80 80 L96 168 L70 150 L52 168 L54 90 Z" fill="#e04848" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><circle cx="55" cy="56" r="50" fill="#f5c33b" stroke="#1f2430" stroke-width="6"/><circle cx="55" cy="56" r="32" fill="none" stroke="#fff" stroke-width="5"/>'), gap=-30)
# plagiarism: a copy icon with a red X
library-3-5-giving-credit/plagiarism = over(raw(200, 220, '<rect x="60" y="10" width="130" height="160" rx="10" fill="#fff" stroke="#1f2430" stroke-width="6"/><rect x="10" y="50" width="130" height="160" rx="10" fill="#fff" stroke="#1f2430" stroke-width="6"/>'), cross(160))
# quote: large quotation marks around lines
library-3-5-giving-credit/quote = row(T('“', 150, BLUE), col(*[raw(w, 16, f'<rect width="{w}" height="16" rx="8" fill="#8a8f9c"/>') for w in (180, 200, 140)], gap=18), T('”', 150, BLUE), gap=4)
# paraphrase: a speech bubble turning into a different speech bubble
library-3-5-giving-credit/paraphrase = row(bubble(dots(3, size=24), 150, BLUE), arrow(60), bubble(row(star(40), heart(40), gap=6), 150, ORANGE, tail='right'), gap=6)
# bibliography: a page titled with a list of book icons
library-3-5-giving-credit/bibliography = page(260, lines=0, title=True, pic=None) if 0 else box(col(raw(180, 24, '<rect width="180" height="24" rx="8" fill="#3a7bd5"/>'), *[row(book(50, c, open_=False), raw(150, 12, '<rect width="150" height="12" rx="6" fill="#8a8f9c"/>'), gap=12) for c in (BLUE, ORANGE, GREEN)], gap=16, align='l'), color=DARK, fill='#fff')
# call number: a book spine with a label reading 551.2
library-3-5-search-like-a-pro/call-number = raw(160, 320, '<rect x="20" y="5" width="120" height="310" rx="10" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><rect x="20" y="40" width="120" height="10" fill="#1f2430" opacity="0.3"/><rect x="34" y="200" width="92" height="90" rx="6" fill="#fff" stroke="#1f2430" stroke-width="4"/><text x="80" y="236" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">551</text><text x="80" y="272" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">.2</text>')
# database: a stack of cylinders like a data drum
library-3-5-search-like-a-pro/database = cylinders(3, 240)
# search engine: a browser window with a magnifying glass
library-3-5-search-like-a-pro/search-engine = browser(320, search=True)
# reliable: a browser window with a check mark
library-6-8-is-it-reliable/reliable = browser(320, check_=True)
# misinformation: a phone screen with a warning triangle
library-6-8-is-it-reliable/misinformation = phone(260, inner=warning(110))
# bias: a tilted scale
library-6-8-is-it-reliable/bias = scale_icon(300, tilt=26)
# lateral reading: one page with arrows out to two other pages to check it
library-6-8-is-it-reliable/lateral-reading = row(browser(220), col(arrow(60, ORANGE, 'ur'), arrow(60, ORANGE, 'dr'), gap=30), col(browser(140, check_=True), browser(140, search=True), gap=16), gap=8)
# fact-check: a magnifying glass over a check mark
library-6-8-is-it-reliable/fact-check = row(magnifier(170), check(120), gap=-30)
# research process: a loop of four arrows
library-6-8-the-research-process/research-process = cycle([magnifier(70), book(70), pencil(70, angle=-35), check(60)], r=130)
# narrow: a funnel
library-6-8-the-research-process/narrow = funnel(260)
# database: stacked cylinders
library-6-8-the-research-process/database = cylinders(3, 240)
# works cited: a page with an alphabetized list
library-6-8-the-research-process/works-cited = box(col(*[row(T(c, 40, BLUE), raw(170, 12, '<rect x="0" y="0" width="170" height="12" rx="6" fill="#8a8f9c"/>'), gap=12) for c in 'ABCD'], gap=14, align='l'), color=DARK, fill='#fff')
# who, what, where: four question cards
library-k-2-asking-good-questions/who-what-where = grid([card(T(w, 34, c), 150, 110, c) for w, c in (('Who?', BLUE), ('What?', ORANGE), ('Where?', GREEN), ('When?', PURPLE))], 2, gap=16)
# spine: a row of book spines with labels
library-k-2-finding-a-book/spine = raw(380, 300, ''.join(f'<rect x="{10 + i * 60}" y="{300 - h}" width="54" height="{h}" rx="6" fill="{c}" stroke="#1f2430" stroke-width="5"/><rect x="{17 + i * 60}" y="{300 - h + h * 0.62:.0f}" width="40" height="40" rx="4" fill="#fff" stroke="#1f2430" stroke-width="3"/><text x="{37 + i * 60}" y="{300 - h + h * 0.62 + 28:.0f}" font-family="Segoe UI" font-size="18" font-weight="700" text-anchor="middle" fill="#1f2430">{lab}</text>' for i, (h, c, lab) in enumerate(((260, BLUE, '398'), (230, ORANGE, '520'), (280, GREEN, '551'), (240, PURPLE, '599'), (270, RED, '612'), (250, TEAL, '796')))))
# borrow: a book with an arrow out and an arrow back
library-k-2-finding-a-book/borrow = row(book(170, open_=False), col(arrow(110, ORANGE, sw=10), arrow(110, BLUE, 'left', sw=10), gap=30), gap=14)
# add tens: three rods plus two rods of ten
math-1-adding-tens-and-ones/add-tens = row(base10(t=3), M('+', 90), base10(t=2, color=BLUE), gap=50)
# ten more: a hundred chart with an arrow from 42 down to 52
math-1-adding-tens-and-ones/ten-more = raw(320, 320, ''.join(f'<rect x="{10 + c * 30}" y="{10 + r * 30}" width="30" height="30" fill="{"#fde97a" if (r * 10 + c + 1) in (42, 52) else "#fff"}" stroke="#c4c8d0" stroke-width="2"/><text x="{25 + c * 30}" y="{31 + r * 30}" font-family="Segoe UI" font-size="13" text-anchor="middle" fill="#1f2430">{r * 10 + c + 1}</text>' for r in range(10) for c in range(10)) + '<path d="M55 145 C80 150 80 165 55 172" fill="none" stroke="#e04848" stroke-width="5"/><path d="M50 172 l12 -10 l4 14 z" fill="#e04848"/>')
# ten less: a hundred chart with an arrow from 70 up to 60
math-1-adding-tens-and-ones/ten-less = raw(320, 320, ''.join(f'<rect x="{10 + c * 30}" y="{10 + r * 30}" width="30" height="30" fill="{"#fde97a" if (r * 10 + c + 1) in (70, 60) else "#fff"}" stroke="#c4c8d0" stroke-width="2"/><text x="{25 + c * 30}" y="{31 + r * 30}" font-family="Segoe UI" font-size="13" text-anchor="middle" fill="#1f2430">{r * 10 + c + 1}</text>' for r in range(10) for c in range(10)) + '<path d="M300 222 C320 214 320 196 300 190" fill="none" stroke="#e04848" stroke-width="5"/><path d="M296 186 l14 2 l-8 12 z" fill="#e04848"/>')
# regroup: ten cubes snapping into a rod
math-1-adding-tens-and-ones/regroup = row(objects(10, cube_icon, cols=5, size=34, color=GREEN, gap=6), arrow(70), rod(10, 26), gap=16)
# base-ten blocks: three rods and six cubes
math-1-adding-tens-and-ones/base-ten-blocks = base10(t=3, o=6)
# mental math: a thought cloud with 40 + 30
math-1-adding-tens-and-ones/mental-math = cloud(320, inner=M('40 + 30', 64))
# word problem: a story card with a question mark
math-1-addition-and-subtraction-stories/word-problem = card(col(raw(150, 60, '<rect y="0" width="150" height="12" rx="6" fill="#8a8f9c"/><rect y="24" width="130" height="12" rx="6" fill="#8a8f9c"/><rect y="48" width="100" height="12" rx="6" fill="#8a8f9c"/>'), T('?', 100, ORANGE), gap=10), 230, 280, BLUE)
# add: 8 ducks and 5 ducks joining
math-1-addition-and-subtraction-stories/add = row(objects(8, duck, cols=4, size=50), M('+', 70), objects(5, duck, cols=3, size=50), gap=14)
# subtract: nine balloons, three float away, six are left: 9 − 3 = 6
math-1-addition-and-subtraction-stories/subtract = col(row(Item(230, 10, ''), *[raw(b.w, b.h, f'<g opacity="0.35">{b.svg}</g>') for b in [balloon(46, RED)] * 3], arrow(40, GRAY, 'up'), gap=8), row(*[balloon(54, RED) for _ in range(6)], gap=8), M('9 − 3 = 6', 70), gap=12)
# sum: 9 + 4 = 13 with 13 circled
math-1-addition-and-subtraction-stories/sum = row(M('9 + 4 =', 80), mark(M('13', 80), 'circle', RED), gap=14)
# difference: 12 − 5 = 7 with 7 circled
math-1-addition-and-subtraction-stories/difference = row(M('12 − 5 =', 80), mark(M('7', 80), 'circle', RED), gap=14)
# how many more: 7 red cars and 4 blue cars in rows
math-1-addition-and-subtraction-stories/how-many-more = row(col(*[car(90, RED) for _ in range(7)], gap=6), col(*[car(90, BLUE) for _ in range(4)], gap=6), gap=30, align='t')
# count: a number line from 98 to 105
math-1-counting-to-120/count = numberline(98, 105, 460, color=BLUE)
# numeral: the numeral 112 written large
math-1-counting-to-120/numeral = T('112', 220, BLUE)
# hundred chart: a 10 by 10 number chart
math-1-counting-to-120/hundred-chart = raw(320, 320, ''.join(f'<rect x="{10 + c * 30}" y="{10 + r * 30}" width="30" height="30" fill="{"#d6e6fb" if c == 9 else "#fff"}" stroke="#c4c8d0" stroke-width="2"/><text x="{25 + c * 30}" y="{31 + r * 30}" font-family="Segoe UI" font-size="13" text-anchor="middle" fill="#1f2430">{r * 10 + c + 1}</text>' for r in range(10) for c in range(10)) + '<rect x="10" y="10" width="300" height="300" fill="none" stroke="#1f2430" stroke-width="4"/>')
# before: a number line with 99 highlighted before 100
math-1-counting-to-120/before = numberline(96, 102, 460, marks={99: ORANGE, 100: GRAY}, color=BLUE)
# after: a number line with 120 highlighted after 119
math-1-counting-to-120/after = numberline(116, 122, 460, marks={119: GRAY, 120: ORANGE}, color=BLUE)
# one hundred twenty: twelve rods of ten cubes
math-1-counting-to-120/one-hundred-twenty = row(*[rod(10, 20) for _ in range(12)], gap=6)
# make a ten: a ten frame with 8 dots plus 2 more filling it
math-1-fact-strategies/make-a-ten = tenframe(8, 320, RED, extra=2, extra_color=BLUE)
# doubles: two dominoes with 6 dots each
math-1-fact-strategies/doubles = row(domino(6, 6, 150), domino(6, 6, 150, ), gap=30)
# count on: a number line with hops from 9 to 12
math-1-fact-strategies/count-on = numberline(7, 13, 460, hops=[(9, 10), (10, 11), (11, 12)], marks={9: ORANGE, 12: GREEN}, color=BLUE)
# fact family: a little house with 3, 4 and 7 on the roof
math-1-fact-strategies/fact-family = raw(260, 300, '<path d="M14 124 L130 20 L246 124 Z" fill="#f08a24" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><rect x="40" y="124" width="180" height="166" fill="#fde3c8" stroke="#1f2430" stroke-width="6"/><line x1="130" y1="140" x2="130" y2="270" stroke="#1f2430" stroke-width="4" stroke-dasharray="8 6"/><text x="130" y="108" font-family="Cambria Math" font-size="56" font-weight="700" text-anchor="middle" fill="#fff">7</text><text x="85" y="226" font-family="Cambria Math" font-size="70" font-weight="700" text-anchor="middle" fill="#3a7bd5">3</text><text x="175" y="226" font-family="Cambria Math" font-size="70" font-weight="700" text-anchor="middle" fill="#2f9e5b">4</text>')
# turnaround fact: 2 + 5 and 5 + 2 with a swap arrow
math-1-fact-strategies/turnaround-fact = col(M('2 + 5', 72), raw(160, 70, '<path d="M30 10 C30 50 130 50 130 10" fill="none" stroke="#f08a24" stroke-width="6"/><path d="M130 60 C130 20 30 20 30 60" fill="none" stroke="#3a7bd5" stroke-width="6"/><path d="M130 0 l-10 16 h20 z M30 70 l-10 -16 h20 z" fill="#1f2430"/>'), M('5 + 2', 72), gap=4)
# strategy: a lightbulb next to 7 + 7
math-1-fact-strategies/strategy = row(lightbulb_on(150), M('7 + 7', 80), gap=20)
# equal shares: a square sandwich cut into 2 equal parts
math-1-halves-and-fourths/equal-shares = raw(300, 300, '<rect x="20" y="20" width="260" height="260" rx="20" fill="#e0a85c" stroke="#1f2430" stroke-width="6"/><rect x="36" y="36" width="228" height="228" rx="12" fill="#fdf0c4"/><line x1="150" y1="10" x2="150" y2="290" stroke="#e04848" stroke-width="8" stroke-dasharray="16 10"/>')
# half: a circle with one of two halves shaded
math-1-halves-and-fourths/half = frac_circle(2, 1, 300, BLUE)
# fourths: a circle cut into four equal parts
math-1-halves-and-fourths/fourths = frac_circle(4, 0, 300, BLUE)
# quarter: a square with one of four parts shaded
math-1-halves-and-fourths/quarter = grid_shade(2, 2, 1, 280, ORANGE)
# whole: two halves joining into a full circle
math-1-halves-and-fourths/whole = row(raw(80, 160, '<path d="M76 4 A76 76 0 0 0 76 156 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>'), raw(80, 160, '<path d="M4 4 A76 76 0 0 1 4 156 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>'), arrow(60), frac_circle(2, 2, 160, BLUE), gap=8)
# unit: a row of paper clips
math-1-measuring-length/unit = raw(420, 120, ''.join(f'<path d="M{14 + i * 102} 30 H{96 + i * 102} A26 26 0 0 1 {96 + i * 102} 82 H{24 + i * 102} A18 18 0 0 1 {24 + i * 102} 46 H{86 + i * 102}" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/>' for i, c in enumerate((BLUE, ORANGE, GREEN, PURPLE))))
# no gaps: cubes in a row touching
math-1-measuring-length/no-gaps = row(*[cube_icon(70, c) for c in (BLUE, ORANGE, GREEN, PURPLE, RED)], gap=0)
# order: three snakes from short to long
math-1-measuring-length/order = col(*[raw(w, 50, f'<path d="M10 25 C{w * 0.3:.0f} 0 {w * 0.5:.0f} 50 {w - 30} 25" fill="none" stroke="{c}" stroke-width="22" stroke-linecap="round"/><circle cx="{w - 22}" cy="25" r="16" fill="{c}"/><circle cx="{w - 18}" cy="20" r="3" fill="#1f2430"/>') for w, c in ((140, GREEN), (240, ORANGE), (340, PURPLE))], gap=24, align='l')
# tally mark: tally marks in a group of five
math-1-picture-graphs-and-tallies/tally-mark = tally(5, 260)
# picture graph: rows of pet icons
math-1-picture-graphs-and-tallies/picture-graph = col(*[row(icon(54), *[icon(54) for _ in range(n - 1)], gap=10) for icon, n in ((cat_icon, 4), (dog_icon, 2), (fish, 3))], gap=20, align='l')
# category: three columns labeled with a cat, dog and fish icon
math-1-picture-graphs-and-tallies/category = row(*[col(icon(70), raw(90, 180, f'<rect x="5" y="5" width="80" height="170" rx="10" fill="{soft(c)}" stroke="{c}" stroke-width="5"/>'), gap=6) for icon, c in ((cat_icon, ORANGE), (dog_icon, BROWN), (fish, BLUE))], gap=20)
# data: a clipboard with tally marks
math-1-picture-graphs-and-tallies/data = clipboard(280, inner=col(tally(5, 70), tally(3, 70), tally(4, 70), gap=10, align='l'))
# survey: a clipboard with a question mark
math-1-picture-graphs-and-tallies/survey = clipboard(280, inner=T('?', 130, BLUE))
# fewest: three bars with the shortest starred
math-1-picture-graphs-and-tallies/fewest = bars([5, 2, 4], size=300, colors=[BLUE, ORANGE, GREEN], star_=1)
# clock: a clock face showing 3 o'clock
math-1-telling-time-to-the-half-hour/clock = clock(300, 3, 0)
# hour hand: a clock with the short hand on 7
math-1-telling-time-to-the-half-hour/hour-hand = clock(300, 7, 0, hl='h')
# minute hand: a clock at 9:00 with the long minute hand picked out
math-1-telling-time-to-the-half-hour/minute-hand = clock(300, 9, 0, hl='m')
# o'clock: a clock at 4:00: the minute hand points straight up to 12
math-1-telling-time-to-the-half-hour/o-clock = clock(300, 4, 0, hl='m')
# half past: a clock showing 8:30
math-1-telling-time-to-the-half-hour/half-past = clock(300, 8, 30)
# digital clock: a digital clock reading 4:30
math-1-telling-time-to-the-half-hour/digital-clock = digital('4:30', 320)
# tens: three rods of ten cubes
math-1-tens-and-ones/tens = row(rod(10, 24), rod(10, 24), rod(10, 24), gap=14)
# ones: four single cubes
math-1-tens-and-ones/ones = row(*[cube_icon(70, GREEN) for _ in range(4)], gap=20)
# place value: a tens and ones chart holding 5 and 2
math-1-tens-and-ones/place-value = place_chart(['tens', 'ones'], ['5', '2'], 300)
# greater than: 45 > 32 with the sign enlarged
math-1-tens-and-ones/greater-than = row(M('45', 100), Item(10, 10, ''), M('>', 150, color=RED), Item(10, 10, ''), M('32', 100), gap=24)
# less than: 19 < 61 with the sign enlarged
math-1-tens-and-ones/less-than = row(M('19', 100), Item(10, 10, ''), M('<', 150, color=RED), Item(10, 10, ''), M('61', 100), gap=24)
# digit: digit tiles 0 to 9
math-1-tens-and-ones/digit = grid([tile(str(i), (BLUE, ORANGE, GREEN, PURPLE, RED)[i % 5], 70) for i in range(10)], 5, gap=10)
# equal sign: a big equal sign
math-1-the-equal-sign/equal-sign = M('=', 300, color=BLUE)
# equation: a balance scale with 3 + 2 and 5 level
math-1-the-equal-sign/equation = col(row(box(M('3 + 2', 50), color=BLUE, p=14), box(M('5', 50), color=ORANGE, p=14), gap=110), scale_icon(340), gap=-60)
# true: a green check mark
math-1-the-equal-sign/true = check(260)
# false: a red X
math-1-the-equal-sign/false = cross(240)
# unknown: 7 + a box with a question mark = 10
math-1-the-equal-sign/unknown = row(M('7 +', 80), box(T('?', 70, ORANGE), w=90, h=90, color=ORANGE, dashed=True), M('= 10', 80), gap=12)
# balance: a level balance scale with blocks on each side
math-1-the-equal-sign/balance = scale_icon(320, row(cube_icon(36, BLUE), cube_icon(36, BLUE), gap=0), row(cube_icon(36, ORANGE), cube_icon(36, ORANGE), gap=0))
# arc: a circle with a highlighted arc
math-10-circles/arc = circle_parts(300, arc=True)
# chord: a circle with a chord
math-10-circles/chord = circle_parts(300, chord=True)
# tangent line: a circle with a line touching one point
math-10-circles/tangent-line = circle_parts(300, tangent=True)
# inscribed angle: an angle with its vertex on the circle
math-10-circles/inscribed-angle = circle_parts(300, inscribed=True)
# sector: a circle with a shaded wedge
math-10-circles/sector = circle_parts(300, sector=True)
# radian: a circle with an arc equal to its radius
math-10-circles/radian = circle_parts(300, radian=True)
# distance formula: two points with a right triangle
math-10-coordinate-geometry/distance-formula = plot(size=320, xr=(0, 8), yr=(0, 8), grid_=True, points=[(1, 1, RED), (6, 5, RED)], segs=[((1, 1), (6, 5), BLUE, False), ((1, 1), (6, 1), ORANGE, True), ((6, 1), (6, 5), ORANGE, True)])
# midpoint: a segment with its center dot
math-10-coordinate-geometry/midpoint = raw(400, 80, '<line x1="20" y1="40" x2="380" y2="40" stroke="#1f2430" stroke-width="7"/><circle cx="20" cy="40" r="12" fill="#1f2430"/><circle cx="380" cy="40" r="12" fill="#1f2430"/><circle cx="200" cy="40" r="17" fill="#e04848" stroke="#1f2430" stroke-width="4"/><path d="M110 22 V58 M290 22 V58" stroke="#3a7bd5" stroke-width="5"/>')
# equation of a circle: a circle on a grid
math-10-coordinate-geometry/equation-of-a-circle = plot(size=320, xr=(-5, 5), yr=(-5, 5), grid_=True, curves=[([1 + 3 * math.cos(t / 20 * math.pi) for t in range(41)], [1 + 3 * math.sin(t / 20 * math.pi) for t in range(41)])], points=[(1, 1, RED)])
# parabola: a parabola with focus and directrix
math-10-coordinate-geometry/parabola = plot(lambda x: x * x / 4, size=320, xr=(-5, 5), yr=(-2, 7), hlines=[-1], points=[(0, 1, RED)])
# slope criteria: two lines crossing at a right angle
math-10-coordinate-geometry/slope-criteria = plot(lambda x: 0.8 * x, lambda x: -1.25 * x, size=320, xr=(-5, 5), yr=(-5, 5), grid_=True)
# coordinate proof: a quadrilateral on a grid
math-10-coordinate-geometry/coordinate-proof = plot(size=320, xr=(0, 8), yr=(0, 8), grid_=True, segs=[((1, 1), (5, 1), BLUE, False), ((5, 1), (7, 5), BLUE, False), ((7, 5), (3, 5), BLUE, False), ((3, 5), (1, 1), BLUE, False)], points=[(1, 1, RED), (5, 1, RED), (7, 5, RED), (3, 5, RED)])
# density: a square full of dots
math-10-modeling-with-geometry/density = raw(300, 300, '<rect x="10" y="10" width="280" height="280" rx="10" fill="#fff" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{24 + c * 21 + (r % 2) * 10}" cy="{24 + r * 21}" r="7" fill="#3a7bd5"/>' for r in range(13) for c in range(12)))
# optimization: three cans that hold the same amount; the one that uses the least metal gets a star
math-10-modeling-with-geometry/optimization = col(T('same amount inside', 32, GRAY), raw(420, 250, ''.join(f'<rect x="{cx - w / 2}" y="{232 - h}" width="{w}" height="{h}" fill="{c}" stroke="#1f2430" stroke-width="5"/><path d="M{cx - w / 2} 232 A{w / 2} {w / 6:.1f} 0 0 0 {cx + w / 2} 232" fill="{c}" stroke="#1f2430" stroke-width="5"/><ellipse cx="{cx}" cy="{232 - h}" rx="{w / 2}" ry="{w / 6:.1f}" fill="#fff" stroke="#1f2430" stroke-width="5"/>' for cx, w, h, c in ((60, 44, 200, '#c9ced8'), (210, 96, 96, '#d3f0de'), (350, 130, 46, '#c9ced8'))) + g(star(64), 178, 40)), T('least metal', 32, GREEN), gap=6)
# blueprint: a floor plan with a scale bar
math-10-modeling-with-geometry/blueprint = raw(400, 300, '<rect x="5" y="5" width="390" height="290" fill="#2c5ea8"/>' + '<path d="M40 30 H360 V220 H40 Z M200 30 V130 M40 130 H250 M300 130 V220" fill="none" stroke="#fff" stroke-width="6"/><path d="M200 100 A30 30 0 0 1 230 130" fill="none" stroke="#fff" stroke-width="3"/><line x1="40" y1="260" x2="200" y2="260" stroke="#fff" stroke-width="5"/>' + ''.join(f'<line x1="{x}" y1="250" x2="{x}" y2="270" stroke="#fff" stroke-width="4"/>' for x in (40, 120, 200)) + '<text x="260" y="270" font-family="Segoe UI" font-size="24" fill="#fff">1 m</text>')
# approximate: a tree trunk beside a cylinder
math-10-modeling-with-geometry/approximate = row(raw(110, 260, '<path d="M15 20 C10 100 20 180 8 250 H102 C90 180 100 100 95 20 Z" fill="#a0673a" stroke="#1f2430" stroke-width="5"/><path d="M40 60 C38 90 44 120 40 150 M70 100 C72 130 66 170 72 210" stroke="#7a4a24" stroke-width="4" fill="none"/>'), M('≈', 80), solid('cylinder', 150, BROWN), gap=14)
# design constraint: a box under a dashed limit line
math-10-modeling-with-geometry/design-constraint = raw(300, 300, '<line x1="10" y1="60" x2="290" y2="60" stroke="#e04848" stroke-width="7" stroke-dasharray="18 10"/>' + g(solid('box', 220, BLUE), 40, 110))
# independent events: two coins
math-10-probability-rules/independent-events = row(coin(160, 'H'), coin(160, 'T'), gap=30)
# conditional probability: a Venn diagram with B highlighted
math-10-probability-rules/conditional-probability = venn(2, labels=['A', 'B'], shade='B')
# addition rule: two overlapping circles
math-10-probability-rules/addition-rule = venn(2, labels=['A', 'B'])
# mutually exclusive: two separate circles
math-10-probability-rules/mutually-exclusive = venn(2, labels=['A', 'B'], sep=True)
# Venn diagram: two overlapping circles
math-10-probability-rules/venn-diagram = venn(2)
# complement: a shaded region outside a circle
math-10-probability-rules/complement = venn(1 if 0 else 2, labels=['A'], shade='outside')
# proof: a two-column table
math-10-proofs-and-constructions/proof = table(cells=[['Statement', 'Reason'], ['', ''], ['', ''], ['', '']], size=340)
# theorem: crossing lines with angles marked
math-10-proofs-and-constructions/theorem = raw(320, 300, '<line x1="20" y1="60" x2="300" y2="240" stroke="#1f2430" stroke-width="7"/><line x1="20" y1="240" x2="300" y2="60" stroke="#1f2430" stroke-width="7"/><path d="M110 118 A60 60 0 0 1 110 182" fill="none" stroke="#3a7bd5" stroke-width="7"/><path d="M210 118 A60 60 0 0 0 210 182" fill="none" stroke="#3a7bd5" stroke-width="7"/><path d="M120 108 A60 60 0 0 1 200 108" fill="none" stroke="#f08a24" stroke-width="7"/><path d="M120 192 A60 60 0 0 0 200 192" fill="none" stroke="#f08a24" stroke-width="7"/>')
# postulate: two points joined by a line
math-10-proofs-and-constructions/postulate = raw(400, 120, '<line x1="0" y1="60" x2="400" y2="60" stroke="#3a7bd5" stroke-width="7"/><path d="M0 60 l24 -14 v28 z M400 60 l-24 -14 v28 z" fill="#3a7bd5"/><circle cx="110" cy="60" r="16" fill="#e04848" stroke="#1f2430" stroke-width="4"/><circle cx="290" cy="60" r="16" fill="#e04848" stroke="#1f2430" stroke-width="4"/><text x="110" y="28" font-family="Cambria Math" font-size="34" font-weight="700" text-anchor="middle" fill="#1f2430">A</text><text x="290" y="28" font-family="Cambria Math" font-size="34" font-weight="700" text-anchor="middle" fill="#1f2430">B</text>')
# perpendicular bisector: a segment cut by a perpendicular line
math-10-proofs-and-constructions/perpendicular-bisector = raw(380, 320, '<line x1="20" y1="200" x2="360" y2="200" stroke="#1f2430" stroke-width="7"/><circle cx="20" cy="200" r="11" fill="#1f2430"/><circle cx="360" cy="200" r="11" fill="#1f2430"/><line x1="190" y1="20" x2="190" y2="310" stroke="#e04848" stroke-width="7"/><path d="M190 176 h24 v24" fill="none" stroke="#1f2430" stroke-width="4"/><path d="M100 186 V214 M280 186 V214" stroke="#3a7bd5" stroke-width="5"/>')
# alternate interior angles: two parallel lines cut by a slanted line
math-10-proofs-and-constructions/alternate-interior-angles = raw(380, 300, '<path d="M228.6 90 L188.6 90 A40 40 0 0 0 207 123.6 Z" fill="#f08a24"/><path d="M151.4 210 L191.4 210 A40 40 0 0 0 173 176.4 Z" fill="#f08a24"/><line x1="10" y1="90" x2="370" y2="90" stroke="#1f2430" stroke-width="7"/><line x1="10" y1="210" x2="370" y2="210" stroke="#1f2430" stroke-width="7"/><line x1="100" y1="290" x2="280" y2="10" stroke="#3a7bd5" stroke-width="7"/>')
# parallelogram: a parallelogram with diagonals
math-10-proofs-and-constructions/parallelogram = raw(380, 240, '<path d="M90 20 H370 L290 220 H10 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><line x1="90" y1="20" x2="290" y2="220" stroke="#f08a24" stroke-width="5" stroke-dasharray="14 8"/><line x1="370" y1="20" x2="10" y2="220" stroke="#f08a24" stroke-width="5" stroke-dasharray="14 8"/><circle cx="190" cy="120" r="9" fill="#e04848"/>')
# sine: a right triangle with angle θ marked; the opposite side and hypotenuse highlighted
math-10-right-triangle-trigonometry/sine = triangle(320, pts=((10, 150), (150, 150), (150, 20)), right_at=1, hl_side=[1, 2], sides=['', 'opp', 'hyp'], theta=0)
# cosine: a right triangle with angle θ marked; the adjacent side and hypotenuse highlighted
math-10-right-triangle-trigonometry/cosine = triangle(320, pts=((10, 150), (150, 150), (150, 20)), right_at=1, hl_side=[0, 2], sides=['adj', '', 'hyp'], theta=0)
# tangent: a right triangle with angle θ marked; the opposite and adjacent sides highlighted
math-10-right-triangle-trigonometry/tangent = triangle(320, pts=((10, 150), (150, 150), (150, 20)), right_at=1, hl_side=[0, 1], sides=['adj', 'opp', ''], theta=0)
# angle of elevation: a line up to a kite with an angle marked
math-10-right-triangle-trigonometry/angle-of-elevation = raw(400, 300, '<line x1="10" y1="280" x2="390" y2="280" stroke="#1f2430" stroke-width="6"/><line x1="40" y1="280" x2="320" y2="70" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="14 8"/><path d="M120 280 A80 80 0 0 0 104 232" fill="none" stroke="#e04848" stroke-width="6"/><path d="M320 30 L350 70 L320 110 L290 70 Z" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M320 30 V110 M290 70 H350" stroke="#1f2430" stroke-width="3"/><path d="M320 110 C310 140 330 160 316 190" fill="none" stroke="#1f2430" stroke-width="3"/>')
# SOH CAH TOA: the letters SOH CAH TOA
math-10-right-triangle-trigonometry/soh-cah-toa = col(T('SOH', 100, BLUE), T('CAH', 100, ORANGE), T('TOA', 100, GREEN), gap=0)
# inverse trig function: sin⁻¹(0.5) = 30°
math-10-right-triangle-trigonometry/inverse-trig-function = M('sin⁻¹(0.5) = 30°', 60)
# rigid motion: a triangle and the same triangle turned, same size and shape
math-10-rigid-motions-and-congruence/rigid-motion = [row(t, curve_arrow(40, ORANGE), raw(t.w, t.h, f'<g transform="rotate(90 {t.w / 2:.1f} {t.h / 2:.1f})">{t.svg}</g>'), gap=24) for t in [triangle(150, pts=((10, 140), (140, 140), (50, 20)), color=BLUE)]][0]
# congruent: two matching triangles with tick marks
math-10-rigid-motions-and-congruence/congruent = row(triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 2, 3]), triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 2, 3], color=ORANGE), gap=20)
# SAS: two triangles with two sides and an angle marked
math-10-rigid-motions-and-congruence/sas = row(triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 2, 0], angles=[1]), triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 2, 0], angles=[1], color=ORANGE), gap=20)
# ASA: two triangles with two angles and a side marked
math-10-rigid-motions-and-congruence/asa = row(triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 0, 0], angles=[0, 1]), triangle(170, pts=((10, 150), (160, 150), (60, 20)), ticks=[1, 0, 0], angles=[0, 1], color=ORANGE), gap=20)
# corresponding parts: two triangles with matching colors
math-10-rigid-motions-and-congruence/corresponding-parts = row(*[raw(170, 170, '<polygon points="10,150 160,150 60,20" fill="#fff" stroke="none"/><line x1="10" y1="150" x2="160" y2="150" stroke="#3a7bd5" stroke-width="9" stroke-linecap="round"/><line x1="160" y1="150" x2="60" y2="20" stroke="#f08a24" stroke-width="9" stroke-linecap="round"/><line x1="60" y1="20" x2="10" y2="150" stroke="#2f9e5b" stroke-width="9" stroke-linecap="round"/>') for _ in range(2)], gap=30)
# image: a point A and its image A′
math-10-rigid-motions-and-congruence/image = plot(size=320, xr=(-5, 5), yr=(-5, 5), grid_=True, points=[(-3, 2, BLUE), (3, 2, ORANGE)], texts=[(-3, 3, 'A', BLUE), (3, 3, 'A′', ORANGE)], vlines=[0])
# similar: a small and a large similar triangle
math-10-similarity/similar = row(triangle(110, pts=((5, 100), (105, 100), (40, 20)), color=BLUE), triangle(220, pts=((10, 200), (210, 200), (80, 40)), color=ORANGE), gap=20, align='b')
# dilation: a small and large figure with rays from a center
math-10-similarity/dilation = raw(320, 300, ''.join(f'<line x1="20" y1="280" x2="{x}" y2="{y}" stroke="#8a8f9c" stroke-width="3" stroke-dasharray="8 6"/>' for x, y in ((310, 230), (310, 30), (190, 30))) + '<polygon points="180,230 300,230 180,40" fill="#fde3c8" stroke="#f08a24" stroke-width="6" stroke-linejoin="round"/><polygon points="100,255 160,255 100,160" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6" stroke-linejoin="round"/><circle cx="20" cy="280" r="12" fill="#e04848" stroke="#1f2430" stroke-width="4"/>')
# scale factor: two similar rectangles labeled
math-10-similarity/scale-factor = row(box(w=90, h=60, color=BLUE), arrow(70, text='×3'), box(w=270, h=180, color=ORANGE), gap=10)
# AA similarity: two triangles with two matching angles
math-10-similarity/aa-similarity = row(triangle(150, pts=((5, 130), (145, 130), (50, 20)), angles=[0, 1]), triangle(220, pts=((10, 200), (210, 200), (75, 40)), angles=[0, 1], color=ORANGE), gap=20, align='b')
# proportion: 3/6 = x/10
math-10-similarity/proportion = eq(('3', '6'), '=', ('x', '10'), size=90)
# center of dilation: rays spreading from one point
math-10-similarity/center-of-dilation = raw(320, 320, '<circle cx="160" cy="160" r="16" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<line x1="{160 + 22 * math.cos(a):.1f}" y1="{160 + 22 * math.sin(a):.1f}" x2="{160 + 140 * math.cos(a):.1f}" y2="{160 + 140 * math.sin(a):.1f}" stroke="#3a7bd5" stroke-width="6" stroke-linecap="round"/><path d="M{160 + 156 * math.cos(a):.1f} {160 + 156 * math.sin(a):.1f} L{160 + 132 * math.cos(a) - 12 * math.sin(a):.1f} {160 + 132 * math.sin(a) + 12 * math.cos(a):.1f} L{160 + 132 * math.cos(a) + 12 * math.sin(a):.1f} {160 + 132 * math.sin(a) - 12 * math.cos(a):.1f} Z" fill="#3a7bd5"/>' for a in [k * 2 * math.pi / 8 for k in range(8)]))
# cross section: a cone sliced horizontally
math-10-volume-and-cross-sections/cross-section = raw(300, 320, '<path d="M150 10 L280 290 H20 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><ellipse cx="150" cy="290" rx="130" ry="22" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><ellipse cx="150" cy="170" rx="74" ry="14" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><line x1="40" y1="170" x2="260" y2="170" stroke="#e04848" stroke-width="5" stroke-dasharray="12 8"/>')
# solid of rotation: a rectangle spinning into a cylinder
math-10-volume-and-cross-sections/solid-of-rotation = row(raw(140, 240, '<line x1="20" y1="10" x2="20" y2="230" stroke="#e04848" stroke-width="5" stroke-dasharray="12 8"/><rect x="20" y="40" width="90" height="160" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><path d="M120 60 A40 14 0 1 1 120 90" fill="none" stroke="#f08a24" stroke-width="5"/>'), arrow(60), solid('cylinder', 180, BLUE), gap=10)
# pyramid: a square pyramid
math-10-volume-and-cross-sections/pyramid = solid('pyramid', 280, ORANGE)
# prism: a triangular prism
math-10-volume-and-cross-sections/prism = solid('prism', 300, GREEN)
# lateral area: an unrolled cylinder label
math-10-volume-and-cross-sections/lateral-area = row(solid('cylinder', 150, BLUE), arrow(60), col(shape('circle', 70, BLUE), raw(200, 140, '<rect x="5" y="5" width="190" height="130" fill="#fde3c8" stroke="#f08a24" stroke-width="7"/>'), shape('circle', 70, BLUE), gap=4), gap=14)
# inverse function: a curve mirrored over y = x
math-11-building-and-inverting-functions/inverse-function = plot(lambda x: 2 ** x if x < 2.4 else None, lambda x: math.log2(x) if x > 0.18 else None, lambda x: x, size=320, xr=(-4, 5), yr=(-4, 5), colors=(BLUE, ORANGE, GRAY))
# composition: two machines in a row
math-11-building-and-inverting-functions/composition = raw(440, 160, '<path d="M0 80 H40 M160 80 H260 M380 80 H430" stroke="#1f2430" stroke-width="7"/><path d="M50 80 l-16 -10 v20 z M270 80 l-16 -10 v20 z M440 80 l-16 -10 v20 z" fill="#1f2430"/><rect x="50" y="20" width="110" height="120" rx="14" fill="#8e5bc4" stroke="#1f2430" stroke-width="5"/><rect x="270" y="20" width="110" height="120" rx="14" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><text x="105" y="100" font-family="Cambria Math" font-style="italic" font-size="64" font-weight="700" text-anchor="middle" fill="#fff">f</text><text x="325" y="96" font-family="Cambria Math" font-style="italic" font-size="64" font-weight="700" text-anchor="middle" fill="#fff">g</text>')
# one-to-one: arrows pairing inputs to outputs one each
math-11-building-and-inverting-functions/one-to-one = raw(360, 300, ''.join(f'<rect x="{x}" y="10" width="110" height="280" rx="50" fill="{c}" stroke="#1f2430" stroke-width="5"/>' for x, c in ((10, soft(BLUE)), (240, soft(ORANGE)))) + ''.join(f'<circle cx="65" cy="{y}" r="12" fill="#3a7bd5"/><circle cx="295" cy="{y2}" r="12" fill="#f08a24"/><line x1="80" y1="{y}" x2="275" y2="{y2}" stroke="#1f2430" stroke-width="4"/><path d="M280 {y2} l-18 -9 v18 z" fill="#1f2430" transform="rotate({math.degrees(math.atan2(y2 - y, 195)):.0f} 280 {y2})"/>' for y, y2 in ((70, 110), (150, 70), (230, 230))))
# horizontal line test: a parabola crossed by a horizontal line twice
math-11-building-and-inverting-functions/horizontal-line-test = plot(lambda x: x * x - 2, size=320, xr=(-4, 4), yr=(-3, 6), hlines=[2], points=[(-2, 2, RED), (2, 2, RED)])
# piecewise function: a graph made of separate line pieces
math-11-building-and-inverting-functions/piecewise-function = plot(size=320, xr=(-5, 5), yr=(-5, 5), segs=[((-5, -3), (-1, -1), BLUE, False), ((0, 2), (3, 2), ORANGE, False), ((3, 4), (5, 0), GREEN, False)], points=[(-1, -1, BLUE), (0, 2, ORANGE), (3, 4, GREEN)], open_points=[(3, 2)])
# reflection: a curve and its mirror under the x-axis
math-11-building-and-inverting-functions/reflection = plot(lambda x: 0.3 * x * x - 3, lambda x: -(0.3 * x * x - 3), size=320, xr=(-5, 5), yr=(-5, 5), colors=(BLUE, ORANGE))
# complex number: a point on a complex plane
math-11-complex-numbers/complex-number = raw(320, 320, '<line x1="10" y1="160" x2="310" y2="160" stroke="#1f2430" stroke-width="5"/><line x1="160" y1="10" x2="160" y2="310" stroke="#1f2430" stroke-width="5"/><text x="300" y="150" font-family="Cambria Math" font-size="28" text-anchor="end" fill="#1f2430">Re</text><text x="170" y="34" font-family="Cambria Math" font-size="28" fill="#1f2430">Im</text><line x1="160" y1="160" x2="250" y2="70" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="10 7"/><circle cx="250" cy="70" r="14" fill="#e04848" stroke="#1f2430" stroke-width="4"/><text x="228" y="40" font-family="Cambria Math" font-size="30" font-weight="700" fill="#1f2430">3 + 3i</text>')
# imaginary unit: i² = −1
math-11-complex-numbers/imaginary-unit = M('i² = −1', 110, hl={'i': BLUE})
# complex conjugate: 3 + 2i and 3 − 2i mirrored
math-11-complex-numbers/complex-conjugate = raw(320, 320, '<line x1="10" y1="160" x2="310" y2="160" stroke="#1f2430" stroke-width="5"/><line x1="120" y1="10" x2="120" y2="310" stroke="#1f2430" stroke-width="5"/><circle cx="240" cy="80" r="14" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><circle cx="240" cy="240" r="14" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><line x1="240" y1="96" x2="240" y2="224" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="8 6"/><text x="230" y="50" font-family="Cambria Math" font-size="34" font-weight="700" text-anchor="middle" fill="#3a7bd5">3 + 2i</text><text x="230" y="292" font-family="Cambria Math" font-size="34" font-weight="700" text-anchor="middle" fill="#f08a24">3 − 2i</text>')
# real part: 5 − 4i with 5 highlighted
math-11-complex-numbers/real-part = M('5 − 4i', 130, hl={'5': ORANGE})
# complex plane: a grid with axes labeled Re and Im
math-11-complex-numbers/complex-plane = raw(320, 320, ''.join(f'<line x1="{20 + i * 28}" y1="20" x2="{20 + i * 28}" y2="300" stroke="#dfe3ea" stroke-width="2"/><line x1="20" y1="{20 + i * 28}" x2="300" y2="{20 + i * 28}" stroke="#dfe3ea" stroke-width="2"/>' for i in range(11)) + '<line x1="10" y1="160" x2="310" y2="160" stroke="#1f2430" stroke-width="5"/><line x1="160" y1="10" x2="160" y2="310" stroke="#1f2430" stroke-width="5"/><rect x="250" y="168" width="60" height="38" rx="6" fill="#fff"/><text x="300" y="198" font-family="Cambria Math" font-size="32" font-weight="700" text-anchor="end" fill="#3a7bd5">Re</text><rect x="168" y="12" width="56" height="38" rx="6" fill="#fff"/><text x="172" y="42" font-family="Cambria Math" font-size="32" font-weight="700" fill="#f08a24">Im</text>')
# complex solution: x = ±i
math-11-complex-numbers/complex-solution = M('x = ±i', 120, hl={'±i': BLUE})
# logarithm: log₂ 8 = 3
math-11-exponential-and-logarithmic-functions/logarithm = M('log₂ 8 = 3', 100)
# natural log: ln e = 1
math-11-exponential-and-logarithmic-functions/natural-log = M('ln e = 1', 110)
# e: e ≈ 2.718
math-11-exponential-and-logarithmic-functions/e = M('e ≈ 2.718', 100, hl={'e': BLUE})
# compound interest: a curve of growing savings
math-11-exponential-and-logarithmic-functions/compound-interest = plot(lambda x: 1.5 * 1.25 ** x, size=320, xr=(0, 10), yr=(0, 15), colors=(GREEN,), points=[(x, 1.5 * 1.25 ** x, GREEN) for x in (0, 2, 4, 6, 8, 10)])
# half-life: a curve halving every step
math-11-exponential-and-logarithmic-functions/half-life = plot(lambda x: 8 * 0.5 ** x, size=320, xr=(0, 5), yr=(0, 9), colors=(PURPLE,), points=[(x, 8 * 0.5 ** x, RED) for x in range(5)], hlines=[4, 2, 1])
# logarithmic scale: a log scale: 1, 10, 100, 1000 equally spaced, each step ×10
math-11-exponential-and-logarithmic-functions/logarithmic-scale = raw(440, 170, '<line x1="10" y1="110" x2="430" y2="110" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<line x1="{40 + i * 120}" y1="94" x2="{40 + i * 120}" y2="126" stroke="#1f2430" stroke-width="5"/><text x="{40 + i * 120}" y="162" font-family="Cambria Math" font-size="32" font-weight="700" text-anchor="middle" fill="#1f2430">{v}</text>' for i, v in enumerate(('1', '10', '100', '1000'))) + ''.join(f'<path d="M{48 + i * 120} 90 Q{100 + i * 120} 34 {150 + i * 120} 86" fill="none" stroke="#f08a24" stroke-width="5"/><path d="M{154 + i * 120} 92 l-4 -18 l-12 10 z" fill="#f08a24"/><text x="{100 + i * 120}" y="40" font-family="Cambria Math" font-size="28" font-weight="700" text-anchor="middle" fill="#f08a24">×10</text>' for i in range(3)))
# remainder theorem: divide f(x) by (x − 2); the remainder equals f(2)
math-11-polynomial-functions/remainder-theorem = col(M('f(x) ÷ (x − 2)', 60, hl={'2': RED}), M('remainder = f(2)', 60, hl={'2': RED}), gap=10)
# end behavior: a curve with both ends rising
math-11-polynomial-functions/end-behavior = plot(lambda x: 0.12 * x ** 4 - 0.9 * x * x + 0.5, size=320, xr=(-4, 4), yr=(-3, 6), colors=(BLUE,))
# multiplicity: a curve bouncing off the x-axis
math-11-polynomial-functions/multiplicity = plot(lambda x: 0.25 * (x + 2) * (x - 1.5) ** 2, size=320, xr=(-4, 4), yr=(-4, 4), points=[(1.5, 0, RED), (-2, 0, ORANGE)])
# synthetic division: a synthetic division layout
math-11-polynomial-functions/synthetic-division = raw(360, 220, '<path d="M60 20 V120 H340" fill="none" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<text x="{x}" y="{y}" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="{c}">{t}</text>' for x, y, t, c in ((32, 70, '2', ORANGE), (110, 70, '1', DARK), (180, 70, '−3', DARK), (250, 70, '0', DARK), (320, 70, '4', DARK), (180, 108, '2', BLUE), (250, 108, '−2', BLUE), (320, 108, '−4', BLUE), (110, 170, '1', DARK), (180, 170, '−1', DARK), (250, 170, '−2', DARK), (320, 170, '0', RED))))
# polynomial identity: a square split into four regions
math-11-polynomial-functions/polynomial-identity = raw(300, 300, '<rect x="10" y="10" width="180" height="180" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="190" y="10" width="100" height="180" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><rect x="10" y="190" width="180" height="100" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><rect x="190" y="190" width="100" height="100" fill="#d3f0de" stroke="#1f2430" stroke-width="5"/><text x="100" y="114" font-family="Cambria Math" font-size="46" font-weight="700" text-anchor="middle" fill="#1f2430">a²</text><text x="240" y="114" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">ab</text><text x="100" y="254" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">ab</text><text x="240" y="254" font-family="Cambria Math" font-size="42" font-weight="700" text-anchor="middle" fill="#1f2430">b²</text>')
# turning point: a cubic with two bends marked
math-11-polynomial-functions/turning-point = plot(lambda x: 0.3 * x ** 3 - 1.8 * x, size=320, xr=(-4, 4), yr=(-5, 5), points=[(-math.sqrt(2), 0.3 * (-math.sqrt(2)) ** 3 + 1.8 * math.sqrt(2), RED), (math.sqrt(2), 0.3 * math.sqrt(2) ** 3 - 1.8 * math.sqrt(2), RED)])
# rational expression: (x + 1)/(x − 2)
math-11-rational-expressions-and-equations/rational-expression = eq(('x + 1', 'x − 2'), size=90)
# asymptote: a curve approaching a dashed line
math-11-rational-expressions-and-equations/asymptote = plot(lambda x: 1 / (x - 1) + 1 if abs(x - 1) > 0.12 else None, size=320, xr=(-4, 5), yr=(-4, 5), vlines=[1], hlines=[1])
# excluded value: x ≠ 2
math-11-rational-expressions-and-equations/excluded-value = M('x ≠ 2', 120, hl={'≠': RED})
# least common denominator: 1/4 + 1/6: list multiples of 4 and 6; the first shared one, 12, is the LCD
math-11-rational-expressions-and-equations/least-common-denominator = col(row(F('1', '4', 80, hd=ORANGE), M('+', 64), F('1', '6', 80, hd=BLUE), gap=16), M('4: 4, 8, 12', 44, hl={'12': RED}), M('6: 6, 12', 44, hl={'12': RED}), T('LCD = 12', 44, RED), gap=8)
# extraneous solution: a crossed-out value
math-11-rational-expressions-and-equations/extraneous-solution = M('x = 5', 120, strike='x = 5')
# hole: a line with an open circle
math-11-rational-expressions-and-equations/hole = plot(lambda x: 0.6 * x + 1, size=320, xr=(-5, 5), yr=(-5, 5), open_points=[(2, 2.2)])
# sequence: a row of numbered dots
math-11-sequences-and-series/sequence = row(*[col(dot(56, c), T(str(i + 1), 34)) for i, c in enumerate((BLUE, ORANGE, GREEN, PURPLE, RED))], gap=16)
# arithmetic sequence: equal steps on a number line
math-11-sequences-and-series/arithmetic-sequence = numberline(0, 12, 460, hops=[(0, 3), (3, 6), (6, 9), (9, 12)], marks={0: ORANGE, 3: ORANGE, 6: ORANGE, 9: ORANGE, 12: ORANGE}, every=3, color=BLUE)
# geometric sequence: bars doubling in height
math-11-sequences-and-series/geometric-sequence = bars([1, 2, 4, 8], size=300, colors=[BLUE, ORANGE, GREEN, PURPLE])
# series: stacked blocks summing
math-11-sequences-and-series/series = row(*[col(*[cube_icon(50, c) for _ in range(n)], gap=0) for n, c in ((1, BLUE), (2, ORANGE), (3, GREEN), (4, PURPLE))], M('= 10', 70), gap=10, align='b')
# common ratio: ×2 arrows between terms
math-11-sequences-and-series/common-ratio = row(box(M('3', 60), color=BLUE, p=16), arrow(60, ORANGE, text='×2'), box(M('6', 60), color=BLUE, p=16), arrow(60, ORANGE, text='×2'), box(M('12', 60), color=BLUE, p=16), gap=6)
# recursive formula: an arrow looping from one term to the next
math-11-sequences-and-series/recursive-formula = row(box(M('aₙ', 60), color=BLUE, p=16), curve_arrow(46, ORANGE, start=200, end=340), box(M('aₙ₊₁', 60), color=ORANGE, p=16), gap=6)
# normal distribution: a bell curve
math-11-statistical-inference/normal-distribution = plot(bell(), size=320, xr=(-4, 4), yr=(-0.3, 5), shade=(bell(), -4, 4), axes=False)
# margin of error: a dot with error bars
math-11-statistical-inference/margin-of-error = raw(320, 300, '<line x1="160" y1="40" x2="160" y2="260" stroke="#3a7bd5" stroke-width="7"/><line x1="120" y1="40" x2="200" y2="40" stroke="#3a7bd5" stroke-width="7"/><line x1="120" y1="260" x2="200" y2="260" stroke="#3a7bd5" stroke-width="7"/><circle cx="160" cy="150" r="22" fill="#e04848" stroke="#1f2430" stroke-width="5"/><text x="230" y="70" font-family="Cambria Math" font-size="44" font-weight="700" fill="#3a7bd5">+</text><text x="230" y="270" font-family="Cambria Math" font-size="44" font-weight="700" fill="#3a7bd5">−</text>')
# randomized experiment: dots split randomly into two groups
math-11-statistical-inference/randomized-experiment = row(grid([dot(30, (BLUE, ORANGE)[(i * 7) % 3 % 2]) for i in range(16)], 4, gap=8), arrow(60), col(box(dots(4, 4, 26, BLUE), color=BLUE, p=10), box(dots(4, 4, 26, ORANGE), color=ORANGE, p=10), gap=10), gap=10)
# observational study: an eye over a group of dots
math-11-statistical-inference/observational-study = col(eye(150), grid([dot(30, (BLUE, ORANGE, GREEN)[i % 3]) for i in range(12)], 6, gap=10), gap=16)
# z-score: a bell curve with a marker at +2
math-11-statistical-inference/z-score = plot(bell(), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, vlines=[0], segs=[((2, 0), (2, 3.2), RED, False)], texts=[(2, 3.9, '+2', RED)])
# sampling distribution: a tall narrow bell curve
math-11-statistical-inference/sampling-distribution = plot(bell(0, 0.45), bell(0, 1.2), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, colors=(BLUE, GRAY))
# unit circle: a unit circle with radius 1 and the angles 0°, 90°, 180°, 270° outside it
math-11-trigonometric-functions/unit-circle = raw(380, 320, g(raw(320, 320, '<line x1="10" y1="160" x2="310" y2="160" stroke="#1f2430" stroke-width="4"/><line x1="160" y1="10" x2="160" y2="310" stroke="#1f2430" stroke-width="4"/><circle cx="160" cy="160" r="120" fill="none" stroke="#3a7bd5" stroke-width="7"/><line x1="160" y1="160" x2="264" y2="100" stroke="#f08a24" stroke-width="6"/><circle cx="264" cy="100" r="9" fill="#e04848"/><path d="M200 160 A40 40 0 0 0 195 140" fill="none" stroke="#e04848" stroke-width="5"/><text x="205" y="120" font-family="Cambria Math" font-size="30" font-weight="700" fill="#f08a24">1</text>' + ''.join(f'<text x="{x}" y="{y}" font-family="Cambria Math" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for x, y, t in ((300, 190, '0°'), (190, 30, '90°'), (196, 306, '270°')))), 60, 0) + '<text x="94" y="192" font-family="Cambria Math" font-size="26" font-weight="700" text-anchor="end" fill="#1f2430">180°</text>')
# period: one wave cycle bracketed
math-11-trigonometric-functions/period = wave(380, 2, marks='period')
# amplitude: a sine wave with its height marked
math-11-trigonometric-functions/amplitude = wave(380, 2, marks='amplitude')
# midline: a wave with a dashed center line
math-11-trigonometric-functions/midline = wave(380, 2, midline=True)
# periodic function: a repeating wave
math-11-trigonometric-functions/periodic-function = wave(380, 3)
# phase shift: two waves, one slid sideways; an arrow shows the shift between their peaks
math-11-trigonometric-functions/phase-shift = over(wave(400, 2, second=(1.0, -math.pi / 2, ORANGE)), raw(400, 200, '<path d="M52 14 H86" stroke="#e04848" stroke-width="5"/><path d="M100 14 l-16 -9 v18 z" fill="#e04848"/>'))
# critical point: a curve with flat points marked
math-12-applications-of-derivatives/critical-point = plot(lambda x: 0.15 * x ** 3 - 1.4 * x, size=320, xr=(-5, 5), yr=(-5, 5), points=[(-math.sqrt(1.4 / 0.45), 0.15 * (-math.sqrt(1.4 / 0.45)) ** 3 + 1.4 * math.sqrt(1.4 / 0.45), RED), (math.sqrt(1.4 / 0.45), 0.15 * math.sqrt(1.4 / 0.45) ** 3 - 1.4 * math.sqrt(1.4 / 0.45), RED)], segs=[((-2.8, 2.9), (-0.7, 2.9), RED, True), ((0.7, -2.9), (2.8, -2.9), RED, True)])
# concavity: a cup-up and a cup-down curve
math-12-applications-of-derivatives/concavity = row(plot(lambda x: 0.4 * x * x, size=200, xr=(-3, 3), yr=(-1, 4), axes=False, colors=(GREEN,), sw=18), plot(lambda x: -0.4 * x * x + 3, size=200, xr=(-3, 3), yr=(-1, 4), axes=False, colors=(RED,), sw=18), gap=20)
# inflection point: an S-curve with its middle marked
math-12-applications-of-derivatives/inflection-point = plot(lambda x: 0.1 * x ** 3, size=320, xr=(-4, 4), yr=(-5, 5), points=[(0, 0, RED)])
# local maximum: a hump with its top marked
math-12-applications-of-derivatives/local-maximum = plot(lambda x: -0.4 * (x - 0.5) ** 2 + 3, size=320, xr=(-4, 5), yr=(-3, 5), points=[(0.5, 3, RED)])
# area between curves: shaded region between two curves
math-12-applications-of-integrals/area-between-curves = plot(lambda x: 0.3 * x * x - 1, lambda x: 0.5 * x + 2, size=320, xr=(-4, 5), yr=(-3, 6), fill_between=(lambda x: 0.5 * x + 2, lambda x: 0.3 * x * x - 1, -2.4, 4.1))
# disc method: a solid made of thin discs
math-12-applications-of-integrals/disc-method = raw(380, 260, '<line x1="10" y1="130" x2="370" y2="130" stroke="#1f2430" stroke-width="4" stroke-dasharray="10 6"/>' + ''.join(f'<ellipse cx="{40 + i * 30}" cy="130" rx="11" ry="{20 + i * 11}" fill="{soft(BLUE)}" stroke="#3a7bd5" stroke-width="4"/>' for i in range(10)))
# washer method: a ring-shaped slice
math-12-applications-of-integrals/washer-method = raw(300, 300, '<circle cx="150" cy="150" r="130" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="7"/><circle cx="150" cy="150" r="60" fill="#fff" stroke="#3a7bd5" stroke-width="7"/><line x1="150" y1="150" x2="280" y2="150" stroke="#f08a24" stroke-width="5"/><line x1="150" y1="150" x2="150" y2="90" stroke="#2f9e5b" stroke-width="5"/><text x="226" y="140" font-family="Cambria Math" font-size="30" font-weight="700" fill="#f08a24">R</text><text x="156" y="128" font-family="Cambria Math" font-size="30" font-weight="700" fill="#2f9e5b">r</text>')
# net change: area above and below an axis
math-12-applications-of-integrals/net-change = plot(lambda x: 2.5 * math.sin(x * 0.9), size=320, xr=(0, 7), yr=(-4, 4), fill_between=(lambda x: 2.5 * math.sin(x * 0.9), lambda x: 0, 0, 7))
# displacement: a curvy path from start to end; a straight red arrow is the displacement
math-12-applications-of-integrals/displacement = raw(360, 270, '<path d="M60 210 C40 60 200 20 300 80 C340 110 330 170 290 200" fill="none" stroke="#3a7bd5" stroke-width="7" stroke-dasharray="14 8" stroke-linecap="round"/><line x1="60" y1="210" x2="266" y2="203" stroke="#e04848" stroke-width="8"/><path d="M290 202 l-26 -12 v24 z" fill="#e04848"/><circle cx="60" cy="210" r="10" fill="#1f2430"/><text x="175" y="250" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">displacement</text><text x="170" y="34" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#3a7bd5">path</text>')
# chi-square test: χ² with bar pairs
math-12-chi-square-and-regression-inference/chi-square-test = col(M('χ²', 110), bars([5, 4, 3, 6, 4, 2], size=280, colors=[BLUE, ORANGE] * 3), gap=0)
# expected count: a table with expected values
math-12-chi-square-and-regression-inference/expected-count = table(cells=[['', 'A', 'B'], ['X', '12', '18'], ['Y', '8', '12']], size=320)
# degrees of freedom: df = 4
math-12-chi-square-and-regression-inference/degrees-of-freedom = M('df = 4', 120)
# test for independence: a two-way table
math-12-chi-square-and-regression-inference/test-for-independence = table(cells=[['', 'Yes', 'No'], ['Boys', '', ''], ['Girls', '', '']], size=320, hl_col=0)
# slope inference: a regression line with a band
math-12-chi-square-and-regression-inference/slope-inference = scatter(14, 1.0, 0.8, 300, line=True, band=True)
# residual plot: scattered dots around a zero line
math-12-chi-square-and-regression-inference/residual-plot = scatter(14, 0, 1.0, 300, zero=True)
# confidence interval: a dot with a bracket around it
math-12-confidence-intervals-and-significance-tests/confidence-interval = raw(380, 140, '<line x1="10" y1="90" x2="370" y2="90" stroke="#1f2430" stroke-width="5"/><path d="M90 50 H70 V130 H90 M290 50 H310 V130 H290" fill="none" stroke="#3a7bd5" stroke-width="8"/><circle cx="190" cy="90" r="20" fill="#e04848" stroke="#1f2430" stroke-width="5"/>')
# null hypothesis: H₀
math-12-confidence-intervals-and-significance-tests/null-hypothesis = M('H₀', 200)
# p-value: a shaded tail of a bell curve
math-12-confidence-intervals-and-significance-tests/p-value = plot(bell(), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, fill_between=(bell(), lambda x: 0, 1.4, 4), vlines=[1.4])
# significance level: α = 0.05
math-12-confidence-intervals-and-significance-tests/significance-level = M('α = 0.05', 100, hl={'α': BLUE})
# t-distribution: a bell curve with thicker tails
math-12-confidence-intervals-and-significance-tests/t-distribution = plot(bell(0, 1), lambda x: 3.6 / (1 + x * x / 2) ** 1.5, size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, colors=(GRAY, BLUE))
# conic section: a cone sliced by a plane
math-12-conic-sections/conic-section = raw(320, 320, '<path d="M160 10 L270 300 H50 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><ellipse cx="160" cy="300" rx="110" ry="16" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><path d="M20 230 L300 110 L300 150 L20 270 Z" fill="#f08a24" fill-opacity="0.45" stroke="#f08a24" stroke-width="4"/><ellipse cx="160" cy="190" rx="90" ry="30" transform="rotate(-23 160 190)" fill="none" stroke="#e04848" stroke-width="6"/>')
# ellipse: an ellipse with two foci
math-12-conic-sections/ellipse = raw(380, 240, '<ellipse cx="190" cy="120" rx="170" ry="100" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="7"/><circle cx="51" cy="120" r="11" fill="#e04848"/><circle cx="329" cy="120" r="11" fill="#e04848"/><line x1="51" y1="120" x2="240" y2="30" stroke="#f08a24" stroke-width="4" stroke-dasharray="10 6"/><line x1="329" y1="120" x2="240" y2="30" stroke="#f08a24" stroke-width="4" stroke-dasharray="10 6"/>')
# hyperbola: a two-branch hyperbola with asymptotes
math-12-conic-sections/hyperbola = plot(None, size=320, xr=(-5, 5), yr=(-5, 5), segs=[((-5, -5), (5, 5), GRAY, True), ((-5, 5), (5, -5), GRAY, True)], curves=[([math.cosh(t) * 1.4 for t in [i / 10 - 1.6 for i in range(33)]], [math.sinh(t) * 1.4 for t in [i / 10 - 1.6 for i in range(33)]]), ([-math.cosh(t) * 1.4 for t in [i / 10 - 1.6 for i in range(33)]], [math.sinh(t) * 1.4 for t in [i / 10 - 1.6 for i in range(33)]])])
# directrix: a parabola with a dashed line below
math-12-conic-sections/directrix = plot(lambda x: x * x / 4, size=320, xr=(-5, 5), yr=(-2, 7), hlines=[-1], points=[(0, 1, RED)], axes=False)
# eccentricity: a circle beside a long ellipse
math-12-conic-sections/eccentricity = row(shape('circle', 140, BLUE), raw(260, 120, '<ellipse cx="130" cy="60" rx="124" ry="44" fill="#fde3c8" stroke="#f08a24" stroke-width="7"/>'), gap=20)
# differential equation: dy/dx = ky
math-12-differential-equations/differential-equation = M('dy/dx = ky', 100)
# slope field: a grid of tiny slanted lines
math-12-differential-equations/slope-field = raw(320, 320, ''.join(f'<line x1="{30 + c * 37 - 14 * math.cos(math.atan(0.25 * (c - 3.5) * (r - 3.5) / 3))}" y1="{30 + r * 37 + 14 * math.sin(math.atan(0.25 * (c - 3.5) * (r - 3.5) / 3))}" x2="{30 + c * 37 + 14 * math.cos(math.atan(0.25 * (c - 3.5) * (r - 3.5) / 3))}" y2="{30 + r * 37 - 14 * math.sin(math.atan(0.25 * (c - 3.5) * (r - 3.5) / 3))}" stroke="#3a7bd5" stroke-width="5" stroke-linecap="round"/>' for r in range(8) for c in range(8)))
# initial condition: a curve through one marked point
math-12-differential-equations/initial-condition = plot(lambda x: 0.8 * math.exp(0.35 * x), size=320, xr=(-4, 5), yr=(-1, 6), points=[(0, 0.8, RED)])
# separation of variables: dy/y = x dx
math-12-differential-equations/separation-of-variables = M('dy/y = x dx', 90)
# exponential model: a rising exponential curve
math-12-differential-equations/exponential-model = plot(lambda x: 0.4 * math.exp(0.55 * x), size=320, xr=(-1, 5.5), yr=(-0.5, 8), colors=(GREEN,))
# general solution: several curves stacked
math-12-differential-equations/general-solution = plot(*[(lambda c: (lambda x: 0.12 * x * x + c))(c) for c in (-3, -1.5, 0, 1.5, 3)], size=320, xr=(-5, 5), yr=(-5, 7), colors=(BLUE, ORANGE, GREEN, PURPLE, RED))
# distribution: a histogram
math-12-exploring-data/distribution = histogram((2, 5, 8, 6, 3, 1), 320)
# categorical variable: a bar chart
math-12-exploring-data/categorical-variable = bars([5, 3, 6, 2], size=300, colors=[BLUE, ORANGE, GREEN, PURPLE])
# outlier: a box plot with a separate dot
math-12-exploring-data/outlier = boxplot(380, outlier=True)
# least-squares regression line: a line through scattered dots
math-12-exploring-data/least-squares-regression-line = scatter(14, 1.0, 0.8, 300, line=True)
# coefficient of determination: r² = 0.81
math-12-exploring-data/coefficient-of-determination = M('r² = 0.81', 110)
# function family: several parabolas from one parent
math-12-functions-and-their-graphs/function-family = plot(lambda x: x * x, lambda x: x * x + 2, lambda x: (x - 2) ** 2, lambda x: 0.4 * x * x - 3, size=320, xr=(-5, 5), yr=(-4, 7), colors=(DARK, BLUE, ORANGE, GREEN))
# horizontal asymptote: a curve flattening toward a dashed line
math-12-functions-and-their-graphs/horizontal-asymptote = plot(lambda x: 2 - 3 * math.exp(-0.7 * x) if x > -1.5 else None, size=320, xr=(-2, 8), yr=(-3, 4), hlines=[2])
# even function: a graph mirrored across the y-axis
math-12-functions-and-their-graphs/even-function = plot(lambda x: 0.25 * x ** 4 - 1.5 * x * x + 1, size=320, xr=(-3, 3), yr=(-3, 4), vlines=[0])
# odd function: a graph symmetric about the origin
math-12-functions-and-their-graphs/odd-function = plot(lambda x: 0.15 * x ** 3 - 1.2 * x, size=320, xr=(-5, 5), yr=(-5, 5), points=[(0, 0, RED)])
# interval of increase: a curve going down then up; the x-values where it rises are marked by a green arrow
math-12-functions-and-their-graphs/interval-of-increase = plot((lambda x: 0.4 * (x + 1) ** 2 - 3, -5, -1), (lambda x: 0.4 * (x + 1) ** 2 - 3, -1, 4), size=320, xr=(-5, 4), yr=(-4, 6), colors=(GRAY, GREEN), points=[(-1, -3, RED)], vlines=(-1,), arrows_=[(-1, 0, 3.9, 0, GREEN)])
# transformation: a curve and its stretched copy
math-12-functions-and-their-graphs/transformation = plot(lambda x: 0.3 * x * x, lambda x: 0.9 * x * x, size=320, xr=(-4, 4), yr=(-1, 6), colors=(BLUE, ORANGE))
# continuous: an unbroken curve
math-12-limits-and-continuity/continuous = plot(lambda x: 1.6 * math.sin(0.9 * x) + 0.2 * x, size=320, xr=(-5, 5), yr=(-4, 4), colors=(GREEN,), sw=8)
# discontinuity: a graph that jumps at x = 1: an open dot on the left piece, a closed dot on the right piece
math-12-limits-and-continuity/discontinuity = plot((lambda x: 0.5 * x + 2, -5, 1), (lambda x: 0.5 * x - 1.5, 1, 5), size=320, xr=(-5, 5), yr=(-4, 5), colors=(BLUE, BLUE), points=[(1, -1, BLUE)], open_points=[(1, 2.5)])
# one-sided limit: an arrow approaching from the left
math-12-limits-and-continuity/one-sided-limit = plot(lambda x: 0.4 * x * x - 1 if x < 2 else None, size=320, xr=(-3, 4), yr=(-2, 4), open_points=[(2, 0.6)], arrows_=[(0.4, -1.5, 1.7, -1.5, RED)])
# intermediate value theorem: a curve crossing a horizontal line
math-12-limits-and-continuity/intermediate-value-theorem = plot(lambda x: 0.12 * x ** 3 - 0.5 * x + 0.4, size=320, xr=(-4, 4), yr=(-5, 5), hlines=[1.2], points=[(-3, 0.12 * -27 + 1.5 + 0.4, BLUE), (3, 0.12 * 27 - 1.5 + 0.4, BLUE)])
# infinite limit: a curve shooting upward near an asymptote
math-12-limits-and-continuity/infinite-limit = plot(lambda x: 1 / (x - 1) ** 2 if abs(x - 1) > 0.2 else None, size=320, xr=(-3, 5), yr=(-1, 8), vlines=[1])
# squeeze theorem: a wiggly curve trapped between two curves that meet at the same point
math-12-limits-and-continuity/squeeze-theorem = plot(lambda x: 0.5 * x * x, lambda x: -0.5 * x * x, lambda x: 0.5 * x * x * math.sin(2.5 / x) if x else 0, size=320, xr=(-2.5, 2.5), yr=(-3.5, 3.5), colors=(GRAY, GRAY, BLUE), points=[(0, 0, RED)])
# limit: a curve with an arrow to a point
math-12-limits-and-rates-of-change/limit = plot(lambda x: 0.3 * x * x + 0.5 if abs(x - 2) > 0.01 else None, size=320, xr=(-1, 5), yr=(-1, 6), points=[(2, 1.7, RED)], arrows_=[(0.2, -0.4, 1.6, -0.4, ORANGE), (3.8, -0.4, 2.4, -0.4, ORANGE)], vlines=[2])
# secant line: a curve with a line through two points
math-12-limits-and-rates-of-change/secant-line = plot(lambda x: 0.25 * x * x, lambda x: 0.25 * (-1 + 3) * x - 0.25 * (-1 * 3), size=320, xr=(-4, 5), yr=(-2, 6), colors=(BLUE, ORANGE), points=[(-1, 0.25, RED), (3, 2.25, RED)])
# tangent line: a curve with a line touching one point
math-12-limits-and-rates-of-change/tangent-line = plot(lambda x: 0.25 * x * x, lambda x: 0.5 * 2 * (x - 2) + 1, size=320, xr=(-4, 5), yr=(-2, 6), colors=(BLUE, ORANGE), points=[(2, 1, RED)])
# approach: dots closing in on a point
math-12-limits-and-rates-of-change/approach = raw(320, 320, '<circle cx="160" cy="160" r="14" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<circle cx="{160 + d * math.cos(a):.1f}" cy="{160 + d * math.sin(a):.1f}" r="{4 + d / 20:.1f}" fill="#3a7bd5"/>' for a in (0.3, 2.4, 4.1) for d in (140, 100, 68, 44, 28)))
# difference quotient: the difference quotient formula
math-12-limits-and-rates-of-change/difference-quotient = eq(('f(x + h) − f(x)', 'h'), size=64)
# matrix: a bracketed grid of numbers
math-12-matrices/matrix = raw(320, 260, '<path d="M30 10 H10 V250 H30 M290 10 H310 V250 H290" fill="none" stroke="#1f2430" stroke-width="8"/>' + ''.join(f'<text x="{80 + c * 80}" y="{70 + r * 75}" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">{v}</text>' for r, rowv in enumerate(((2, 0, 5), (1, 3, 4), (7, 6, 1))) for c, v in enumerate(rowv)))
# determinant: a 2 by 2 grid with ad − bc
math-12-matrices/determinant = col(raw(240, 200, '<line x1="20" y1="10" x2="20" y2="190" stroke="#1f2430" stroke-width="8"/><line x1="220" y1="10" x2="220" y2="190" stroke="#1f2430" stroke-width="8"/>' + ''.join(f'<text x="{x}" y="{y}" font-family="Cambria Math" font-size="64" font-style="italic" font-weight="700" text-anchor="middle" fill="{c}">{t}</text>' for x, y, t, c in ((75, 80, 'a', BLUE), (165, 80, 'b', ORANGE), (75, 170, 'c', ORANGE), (165, 170, 'd', BLUE)))), M('ad − bc', 64, hl={'ad': BLUE, 'bc': ORANGE}), gap=10)
# identity matrix: a grid with 1s on the diagonal
math-12-matrices/identity-matrix = raw(320, 260, '<path d="M30 10 H10 V250 H30 M290 10 H310 V250 H290" fill="none" stroke="#1f2430" stroke-width="8"/>' + ''.join(f'<text x="{80 + c * 80}" y="{70 + r * 75}" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="{RED if r == c else GRAY}">{1 if r == c else 0}</text>' for r in range(3) for c in range(3)))
# inverse matrix: A × A⁻¹ = I
math-12-matrices/inverse-matrix = M('A × A⁻¹ = I', 90)
# dimensions: a grid labeled 3 rows, 3 columns
math-12-matrices/dimensions = col(raw(260, 200, '<path d="M30 10 H10 V190 H30 M230 10 H250 V190 H230" fill="none" stroke="#1f2430" stroke-width="8"/>' + ''.join(f'<circle cx="{60 + c * 70}" cy="{40 + r * 60}" r="16" fill="#3a7bd5"/>' for r in range(3) for c in range(3))), M('3 × 3', 70, color=ORANGE), gap=10)
# scalar multiplication: 2 times a grid
math-12-matrices/scalar-multiplication = row(M('2 ×', 90, color=ORANGE), raw(200, 180, '<path d="M24 8 H8 V172 H24 M176 8 H192 V172 H176" fill="none" stroke="#1f2430" stroke-width="7"/>' + ''.join(f'<text x="{65 + c * 70}" y="{72 + r * 72}" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">{v}</text>' for r, rowv in enumerate(((1, 3), (4, 2))) for c, v in enumerate(rowv))), gap=10)
# polar coordinates: a point with radius and angle
math-12-polar-coordinates-and-complex-plane/polar-coordinates = raw(320, 320, '<line x1="10" y1="160" x2="310" y2="160" stroke="#1f2430" stroke-width="4"/><line x1="160" y1="10" x2="160" y2="310" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<circle cx="160" cy="160" r="{r}" fill="none" stroke="#dfe3ea" stroke-width="3"/>' for r in (50, 100, 150)) + '<line x1="160" y1="160" x2="260" y2="70" stroke="#3a7bd5" stroke-width="7"/><circle cx="260" cy="70" r="12" fill="#e04848" stroke="#1f2430" stroke-width="4"/><path d="M215 160 A55 55 0 0 0 201 123" fill="none" stroke="#f08a24" stroke-width="6"/><text x="228" y="140" font-family="Cambria Math" font-size="34" font-weight="700" fill="#f08a24">θ</text><text x="186" y="100" font-family="Cambria Math" font-size="34" font-weight="700" fill="#3a7bd5">r</text>')
# polar form: an arrow on the complex plane with r and θ
math-12-polar-coordinates-and-complex-plane/polar-form = raw(320, 320, '<line x1="10" y1="200" x2="310" y2="200" stroke="#1f2430" stroke-width="4"/><line x1="80" y1="10" x2="80" y2="310" stroke="#1f2430" stroke-width="4"/><line x1="80" y1="200" x2="250" y2="60" stroke="#3a7bd5" stroke-width="7"/><path d="M262 50 l-30 4 l14 22 z" fill="#3a7bd5"/><path d="M140 200 A60 60 0 0 0 126 162" fill="none" stroke="#f08a24" stroke-width="6"/><text x="150" y="186" font-family="Cambria Math" font-size="34" font-weight="700" fill="#f08a24">θ</text><text x="140" y="110" font-family="Cambria Math" font-size="36" font-weight="700" fill="#3a7bd5">r</text>')
# modulus: an arrow from 0 to 3 + 4i
math-12-polar-coordinates-and-complex-plane/modulus = raw(320, 320, '<line x1="10" y1="270" x2="310" y2="270" stroke="#1f2430" stroke-width="4"/><line x1="50" y1="10" x2="50" y2="310" stroke="#1f2430" stroke-width="4"/><line x1="50" y1="270" x2="230" y2="30" stroke="#3a7bd5" stroke-width="8"/><line x1="230" y1="270" x2="230" y2="30" stroke="#8a8f9c" stroke-width="3" stroke-dasharray="8 6"/><line x1="50" y1="270" x2="230" y2="270" stroke="#8a8f9c" stroke-width="3" stroke-dasharray="8 6"/><circle cx="230" cy="30" r="12" fill="#e04848"/><text x="140" y="300" font-family="Cambria Math" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">3</text><text x="250" y="160" font-family="Cambria Math" font-size="30" font-weight="700" fill="#1f2430">4</text><text x="100" y="140" font-family="Cambria Math" font-size="40" font-weight="700" fill="#3a7bd5">5</text>')
# argument: an angle on the complex plane
math-12-polar-coordinates-and-complex-plane/argument = raw(320, 320, '<line x1="10" y1="200" x2="310" y2="200" stroke="#1f2430" stroke-width="4"/><line x1="80" y1="10" x2="80" y2="310" stroke="#1f2430" stroke-width="4"/><line x1="80" y1="200" x2="250" y2="60" stroke="#8a8f9c" stroke-width="6"/><path d="M80 200 L180 200 A100 100 0 0 0 157 136 Z" fill="#f08a24" fill-opacity="0.5" stroke="#f08a24" stroke-width="6"/><text x="190" y="176" font-family="Cambria Math" font-size="40" font-weight="700" fill="#f08a24">θ</text>')
# rose curve: a three-petal curve
math-12-polar-coordinates-and-complex-plane/rose-curve = raw(320, 320, '<path d="' + ' '.join(f'{"M" if i == 0 else "L"}{160 + 140 * math.cos(3 * t) * math.cos(t):.1f} {160 - 140 * math.cos(3 * t) * math.sin(t):.1f}' for i, t in enumerate([k * math.pi / 180 for k in range(181)])) + ' Z" fill="#f6c6dc" stroke="#e05a9a" stroke-width="6" stroke-linejoin="round"/>')
# De Moivre's theorem: De Moivre's theorem on two lines
math-12-polar-coordinates-and-complex-plane/de-moivre-s-theorem = col(M('[r(cos θ + i sin θ)]ⁿ', 46), M('= rⁿ(cos nθ + i sin nθ)', 46), gap=10, align='l')
# random variable: X = number of heads
math-12-probability-and-random-variables/random-variable = row(coin(110, 'H'), coin(110, 'T'), coin(110, 'H'), M('X = 2', 70, color=BLUE), gap=16)
# expected value: E(X) = Σ x·p
math-12-probability-and-random-variables/expected-value = M('E(X) = Σ x·p', 80)
# probability distribution: a bar chart of probabilities
math-12-probability-and-random-variables/probability-distribution = bars([1, 3, 3, 1], labels=['0', '1', '2', '3'], size=300, color=PURPLE)
# random assignment: dots shuffled into two groups
math-12-sampling-and-experiments/random-assignment = row(grid([dot(30, (BLUE, ORANGE)[(i * 5) % 3 % 2]) for i in range(16)], 4, gap=8), arrow(60, text='?'), col(box(dots(4, 4, 26, BLUE), color=BLUE, p=10), box(dots(4, 4, 26, ORANGE), color=ORANGE, p=10), gap=10), gap=10)
# control group: two groups, one marked control
math-12-sampling-and-experiments/control-group = row(box(dots(6, 3, 28, BLUE), color=BLUE, p=16), col(box(dots(6, 3, 28, GRAY), color=GRAY, p=16, dashed=True), T('control', 34, GRAY), gap=6), gap=24, align='t')
# confounding variable: a third box pointing to two others
math-12-sampling-and-experiments/confounding-variable = raw(380, 280, '<rect x="130" y="10" width="120" height="70" rx="12" fill="#fde97a" stroke="#1f2430" stroke-width="5"/><text x="190" y="58" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">?</text><rect x="10" y="190" width="120" height="70" rx="12" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="5"/><rect x="250" y="190" width="120" height="70" rx="12" fill="#fde3c8" stroke="#f08a24" stroke-width="5"/><path d="M160 80 L90 180 M220 80 L290 180" stroke="#1f2430" stroke-width="6"/><path d="M84 190 l2 -26 l20 12 z M296 190 l-2 -26 l-20 12 z" fill="#1f2430"/><path d="M130 225 H250" stroke="#8a8f9c" stroke-width="5" stroke-dasharray="10 8"/>')
# stratified random sample: layers with dots picked from each
math-12-sampling-and-experiments/stratified-random-sample = col(*[box(row(*[dot(28, c if i == k else soft(c)) for i in range(6)], gap=10), color=c, fill=soft(c), p=12) for k, c in ((2, BLUE), (4, ORANGE), (1, GREEN))], gap=8)
# response bias: a leading question gets lopsided answers: 9 yes, 1 no
math-12-sampling-and-experiments/response-bias = col(bubble(T("You love it, right?", 30), 300, tail='left'), bars([9, 1], labels=['yes', 'no'], size=260, colors=[GREEN, RED]), gap=10)
# statistic: x̄
math-12-sampling-distributions/statistic = M('x̄', 240, color=BLUE)
# parameter: μ
math-12-sampling-distributions/parameter = M('μ', 240, color=ORANGE)
# central limit theorem: a skewed shape turning into a bell
math-12-sampling-distributions/central-limit-theorem = row(bars([7, 5, 3, 2, 1, 1], size=150, axis=False, touch=True, color=ORANGE), arrow(60), plot(bell(), size=170, xr=(-3.5, 3.5), yr=(-0.3, 5), axes=False, shade=(bell(), -3.5, 3.5)), gap=10)
# standard error: a narrow bell curve
math-12-sampling-distributions/standard-error = plot(bell(0, 0.5), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, shade=(bell(0, 0.5), -4, 4))
# unbiased estimator: a bell centered on a target line
math-12-sampling-distributions/unbiased-estimator = plot(bell(), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, vlines=[0], shade=(bell(), -4, 4))
# sampling variability: three samples from the same group give three different means (red lines)
math-12-sampling-distributions/sampling-variability = col(dotplot((2, 3, 4, 4, 5, 6), 340, a=0, b=10, center=4), dotplot((4, 5, 5, 6, 6, 7), 340, a=0, b=10, center=5.5), dotplot((3, 4, 5, 5, 6, 7), 340, a=0, b=10, center=5), gap=4)
# derivative: a tangent line on a curve
math-12-the-derivative/derivative = plot(lambda x: 0.25 * x * x, lambda x: 0.5 * 2 * (x - 2) + 1, size=320, xr=(-4, 5), yr=(-2, 6), colors=(BLUE, ORANGE), points=[(2, 1, RED)])
# power rule: d/dx xⁿ = nxⁿ⁻¹
math-12-the-derivative/power-rule = M('d/dx xⁿ = nxⁿ⁻¹', 70)
# chain rule: f(g(x))′ = f′(g(x))·g′(x)
math-12-the-derivative/chain-rule = M("f(g(x))′ = f′(g(x))·g′(x)", 44)
# product rule: (uv)′ = u′v + uv′
math-12-the-derivative/product-rule = M("(uv)′ = u′v + uv′", 64)
# differentiable: a smooth curve with a tangent line touching it at one point
math-12-the-derivative/differentiable = plot(lambda x: 0.25 * x * x + 0.5, lambda x: x - 0.5, size=320, xr=(-4, 4), yr=(-1, 5), colors=(BLUE, ORANGE), points=[(2, 1.5, RED)])
# quotient rule: (u/v)′ = (u′v − uv′)/v²
math-12-the-derivative/quotient-rule = eq("(u/v)′ =", ("u′v − uv′", "v²"), size=60)
# integral: shaded area under a curve
math-12-the-integral/integral = plot(lambda x: 0.15 * x * x + 1, size=320, xr=(0, 6), yr=(0, 7), shade=(lambda x: 0.15 * x * x + 1, 1, 5))
# Riemann sum: rectangles under a curve
math-12-the-integral/riemann-sum = plot(lambda x: 0.15 * x * x + 1, size=320, xr=(0, 6), yr=(0, 7), rects=(lambda x: 0.15 * x * x + 1, 1, 5, 6))
# antiderivative: ∫2x dx = x² + C
math-12-the-integral/antiderivative = M('∫2x dx = x² + C', 72)
# Fundamental Theorem of Calculus: ∫ₐᵇ f′(x)dx = f(b) − f(a)
math-12-the-integral/fundamental-theorem-of-calculus = M('∫ₐᵇ f′(x)dx = f(b) − f(a)', 48)
# definite integral: shaded area between two bounds
math-12-the-integral/definite-integral = plot(lambda x: 0.4 * math.sin(x) + 2, size=320, xr=(0, 7), yr=(0, 4), shade=(lambda x: 0.4 * math.sin(x) + 2, 1.5, 5.5), vlines=[1.5, 5.5])
# identity: sin²x + cos²x = 1
math-12-trigonometric-identities-and-equations/identity = M('sin²x + cos²x = 1', 64)
# Pythagorean identity: a unit circle triangle
math-12-trigonometric-identities-and-equations/pythagorean-identity = raw(320, 320, '<circle cx="140" cy="180" r="130" fill="none" stroke="#c4c8d0" stroke-width="5"/><polygon points="140,180 244,180 244,102" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M228 180 v-16 h16" fill="none" stroke="#1f2430" stroke-width="4"/><text x="170" y="130" font-family="Cambria Math" font-size="34" font-weight="700" fill="#e04848">1</text><text x="190" y="220" font-family="Cambria Math" font-size="30" font-weight="700" text-anchor="middle" fill="#3a7bd5">cos</text><text x="256" y="150" font-family="Cambria Math" font-size="30" font-weight="700" fill="#f08a24">sin</text>')
# double-angle formula: sin 2x = 2 sin x cos x
math-12-trigonometric-identities-and-equations/double-angle-formula = M('sin 2x = 2 sin x cos x', 54)
# general solution: repeating dots on a wave
math-12-trigonometric-identities-and-equations/general-solution = wave(380, 3, marks=None) if 0 else plot(lambda x: 2.5 * math.sin(x), size=320, xr=(-7, 7), yr=(-4, 4), hlines=[0], points=[(k * math.pi + 0.0, 0, RED) for k in range(-2, 3)])
# reciprocal function: sec x = 1/cos x
math-12-trigonometric-identities-and-equations/reciprocal-function = M('sec x = 1/cos x', 72)
# arcsine: sin⁻¹ 1 = π/2
math-12-trigonometric-identities-and-equations/arcsine = M('sin⁻¹ 1 = π/2', 80)
# vector: an arrow on a grid
math-12-vectors/vector = plot(size=320, xr=(-1, 7), yr=(-1, 7), grid_=True, arrows_=[(0, 0, 5, 4, BLUE)])
# magnitude: an arrow with its length labeled
math-12-vectors/magnitude = raw(360, 260, '<line x1="20" y1="230" x2="300" y2="50" stroke="#3a7bd5" stroke-width="9"/><path d="M320 37 l-38 4 l16 26 z" fill="#3a7bd5"/><path d="M40 260 L330 74" stroke="#f08a24" stroke-width="4"/><path d="M34 252 l12 18 M324 66 l12 18" stroke="#f08a24" stroke-width="4"/><text x="210" y="200" font-family="Cambria Math" font-size="44" font-weight="700" fill="#f08a24">|v| = 5</text>')
# component: a vector split into two legs
math-12-vectors/component = raw(340, 280, '<line x1="20" y1="260" x2="290" y2="60" stroke="#3a7bd5" stroke-width="9"/><path d="M310 45 l-38 6 l18 26 z" fill="#3a7bd5"/><line x1="20" y1="260" x2="296" y2="260" stroke="#f08a24" stroke-width="7" stroke-dasharray="14 8"/><line x1="310" y1="260" x2="310" y2="60" stroke="#2f9e5b" stroke-width="7" stroke-dasharray="14 8"/>')
# resultant: two arrows tip to tail and their sum
math-12-vectors/resultant = raw(360, 280, '<line x1="20" y1="260" x2="200" y2="200" stroke="#3a7bd5" stroke-width="9"/><path d="M220 193 l-34 -6 l8 28 z" fill="#3a7bd5"/><line x1="214" y1="196" x2="300" y2="50" stroke="#f08a24" stroke-width="9"/><path d="M310 32 l-26 22 l26 12 z" fill="#f08a24"/><line x1="20" y1="260" x2="290" y2="50" stroke="#2f9e5b" stroke-width="8" stroke-dasharray="16 10"/><path d="M306 38 l-34 6 l16 24 z" fill="#2f9e5b"/>')
# dot product: two arrows at a right angle: a · b = 0
math-12-vectors/dot-product = raw(300, 300, '<line x1="40" y1="260" x2="260" y2="260" stroke="#3a7bd5" stroke-width="9"/><path d="M286 260 l-32 -16 v32 z" fill="#3a7bd5"/><line x1="40" y1="260" x2="40" y2="40" stroke="#f08a24" stroke-width="9"/><path d="M40 14 l-16 32 h32 z" fill="#f08a24"/><path d="M40 230 h30 v30" fill="none" stroke="#1f2430" stroke-width="5"/><text x="246" y="246" font-family="Cambria Math" font-size="40" font-weight="700" font-style="italic" fill="#3a7bd5">b</text><text x="56" y="56" font-family="Cambria Math" font-size="40" font-weight="700" font-style="italic" fill="#f08a24">a</text><text x="170" y="160" font-family="Cambria Math" font-size="44" font-weight="700" text-anchor="middle" fill="#1f2430"><tspan fill="#f08a24" font-style="italic">a</tspan> · <tspan fill="#3a7bd5" font-style="italic">b</tspan> = 0</text>')
# unit vector: a short arrow labeled 1
math-12-vectors/unit-vector = raw(300, 200, '<line x1="30" y1="140" x2="220" y2="140" stroke="#3a7bd5" stroke-width="10"/><path d="M250 140 l-36 -20 v40 z" fill="#3a7bd5"/><text x="130" y="110" font-family="Cambria Math" font-size="60" font-weight="700" text-anchor="middle" fill="#f08a24">1</text>')
# regroup: ten rods snapping into a hundred flat
math-2-adding-and-subtracting-to-1000/regroup = row(row(*[rod(10, 18) for _ in range(10)], gap=3), arrow(60), flat(200), gap=14)
# add: 256 + 132 stacked
math-2-adding-and-subtracting-to-1000/add = col(M('  256', 80), M('+ 132', 80), raw(240, 8, '<rect width="240" height="8" fill="#1f2430"/>'), M('  388', 80, color=BLUE), gap=0, align='r')
# subtract: 480 − 120 stacked
math-2-adding-and-subtracting-to-1000/subtract = col(M('  480', 80), M('− 120', 80), raw(240, 8, '<rect width="240" height="8" fill="#1f2430"/>'), M('  360', 80, color=BLUE), gap=0, align='r')
# hundred: ten rods making a square
math-2-adding-and-subtracting-to-1000/hundred = row(row(*[rod(10, 18) for _ in range(10)], gap=3), M('=', 70), flat(200), gap=14)
# open number line: a blank line with three jump arcs
math-2-adding-and-subtracting-to-1000/open-number-line = raw(420, 170, '<line x1="10" y1="140" x2="410" y2="140" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<path d="M{a} 136 Q{(a + b) / 2} 30 {b} 136" fill="none" stroke="{c}" stroke-width="6"/><path d="M{b} 138 l-6 -24 l-14 14 z" fill="{c}"/>' for a, b, c in ((30, 190, BLUE), (190, 300, ORANGE), (300, 390, GREEN))) + ''.join(f'<line x1="{x}" y1="128" x2="{x}" y2="152" stroke="#1f2430" stroke-width="5"/>' for x in (30, 190, 300, 390)))
# estimate: a wavy equal sign next to 500
math-2-adding-and-subtracting-to-1000/estimate = row(M('≈', 160, color=ORANGE), M('500', 120), gap=14)
# doubles plus one: two rows of 7 dots and one extra dot
math-2-fluency-within-20/doubles-plus-one = col(dots(7, 7, 40, BLUE), dots(7, 7, 40, BLUE, extra=1, extra_color=ORANGE), gap=12, align='l')
# make ten: a ten frame with 9 dots plus one more
math-2-fluency-within-20/make-ten = tenframe(9, 320, RED, extra=1, extra_color=BLUE)
# think addition: 15 − 7 next to 7 + ? = 15
math-2-fluency-within-20/think-addition = row(M('15 − 7', 70), raw(8, 120, '<rect width="8" height="120" fill="#c4c8d0"/>'), row(M('7 +', 70), box(T('?', 56, ORANGE), w=70, h=80, color=ORANGE, dashed=True), M('= 15', 70), gap=8), gap=20)
# mental math: a thought cloud with 10 + 9
math-2-fluency-within-20/mental-math = cloud(320, inner=M('10 + 9', 64))
# fact: 6 + 4 = 10 on a flash card
math-2-fluency-within-20/fact = card(M('6 + 4 = 10', 64), 360, 200, BLUE)
# hundreds: three flat squares of 100
math-2-hundreds-tens-and-ones/hundreds = row(flat(130), flat(130), flat(130), gap=14)
# tens: four rods of ten
math-2-hundreds-tens-and-ones/tens = row(*[rod(10, 26) for _ in range(4)], gap=16)
# ones: five single cubes
math-2-hundreds-tens-and-ones/ones = row(*[cube_icon(66, GREEN) for _ in range(5)], gap=16)
# place value: a hundreds, tens and ones chart with 3, 4, 5
math-2-hundreds-tens-and-ones/place-value = place_chart(['hundreds', 'tens', 'ones'], ['3', '4', '5'], 340)
# expanded form: 345 = 300 + 40 + 5, each digit colored to match its part
math-2-hundreds-tens-and-ones/expanded-form = M('345 = 300 + 40 + 5', 56, hl={'300': GREEN, '40': BLUE, '5': ORANGE, '3': GREEN, '4': BLUE})
# skip count: a number line with hops of 5
math-2-hundreds-tens-and-ones/skip-count = numberline(0, 20, 460, hops=[(0, 5), (5, 10), (10, 15), (15, 20)], every=5, marks={5: ORANGE, 10: ORANGE, 15: ORANGE, 20: ORANGE}, color=BLUE)
# bar graph: a bar graph with four bars
math-2-line-plots-and-bar-graphs/bar-graph = bars([3, 5, 2, 4], size=300, colors=[BLUE, ORANGE, GREEN, PURPLE], ticks=True)
# line plot: a line plot: X marks stacked over each value
math-2-line-plots-and-bar-graphs/line-plot = numberline(1, 5, 420, dots_={1: 2, 2: 4, 3: 3, 4: 1, 5: 2}, color=BLUE, xs=True)
# data: a clipboard with tally marks
math-2-line-plots-and-bar-graphs/data = clipboard(280, inner=col(tally(5, 70), tally(3, 70), tally(4, 70), gap=10, align='l'))
# title: a bar graph with its title, Our Pets, on top
math-2-line-plots-and-bar-graphs/title = col(T('Our Pets', 48), bars([3, 5, 2, 4], labels=['cat', 'dog', 'fish', 'bird'], size=300, colors=[BLUE, ORANGE, GREEN, PURPLE]), gap=10)
# label: a bar graph with words under each bar
math-2-line-plots-and-bar-graphs/label = bars([3, 5, 2], labels=['cats', 'dogs', 'fish'], size=300, colors=[ORANGE, BROWN, BLUE])
# compare: two bars of different heights
math-2-line-plots-and-bar-graphs/compare = bars([3, 7], size=260, colors=[ORANGE, BLUE])
# even: 8 dots in two rows of 4
math-2-odd-even-and-arrays/even = dots(8, 4, 50, BLUE)
# odd: 7 dots paired with one left over
math-2-odd-even-and-arrays/odd = row(col(dots(3, 3, 50, BLUE), dots(3, 3, 50, BLUE), gap=12), dot(50, ORANGE), gap=12, align='t')
# array: a 3 by 4 array of dots
math-2-odd-even-and-arrays/array = dots(12, 4, 50, BLUE)
# row: a row of 5 stars
math-2-odd-even-and-arrays/row = row(*[star(90) for _ in range(5)], gap=8)
# column: a column of 3 stars
math-2-odd-even-and-arrays/column = col(*[star(80) for _ in range(3)], gap=10)
# centimeter: a centimeter ruler with the first centimeter shaded
math-2-rulers-and-units/centimeter = ruler(420, 10, 'cm', first='1 cm')
# angle: a triangle with its angles marked
math-2-shapes-and-equal-shares/angle = triangle(300, angles=[0, 1, 2])
# face: a cube with one face shaded
math-2-shapes-and-equal-shares/face = solid('cube', 260, BLUE, hl_face=True)
# pentagon: a plain pentagon
math-2-shapes-and-equal-shares/pentagon = poly(5, 280, GREEN)
# hexagon: a plain hexagon
math-2-shapes-and-equal-shares/hexagon = poly(6, 280, PURPLE)
# thirds: a bar cut into 3 equal parts
math-2-shapes-and-equal-shares/thirds = frac_bar(3, 0, 360, 100, ORANGE)
# equal shares: a square cut into 4 equal parts
math-2-shapes-and-equal-shares/equal-shares = grid_shade(2, 2, 0, 280, BLUE)
# quarter past: a clock showing 10:15
math-2-time-and-money/quarter-past = clock(300, 10, 15)
# two-step problem: two stair steps marked 1 and 2
math-2-two-step-word-problems/two-step-problem = stairs(2, 300, labels=['1', '2'], color=BLUE)
# step: a single stair step marked 1
math-2-two-step-word-problems/step = stairs(1, 240, labels=['1'], color=BLUE)
# add: 25 + 13 in a box
math-2-two-step-word-problems/add = box(M('25 + 13', 80), color=BLUE, p=24)
# subtract: 50 − 18 in a box
math-2-two-step-word-problems/subtract = box(M('50 − 18', 80), color=ORANGE, p=24)
# tape diagram: a tape diagram: parts 20 and 10 under a bracket for the whole, 30
math-2-two-step-word-problems/tape-diagram = col(T('30', 48, RED), raw(420, 24, '<path d="M10 22 V6 H410 V22" fill="none" stroke="#e04848" stroke-width="5"/>'), raw(420, 120, '<rect x="10" y="10" width="267" height="80" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="277" y="10" width="133" height="80" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><text x="143" y="66" font-family="Cambria Math" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">20</text><text x="343" y="66" font-family="Cambria Math" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">10</text>'), gap=0)
# check: a check mark next to an equation
math-2-two-step-word-problems/check = row(M('4 + 3 = 7', 72), check(90), gap=20)
# area: a 3 by 4 rectangle filled with unit squares
math-3-area/area = rect_dims(4, 3, 320)
# square unit: one square with each side marked 1
math-3-area/square-unit = raw(260, 260, '<rect x="40" y="30" width="180" height="180" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/><text x="130" y="250" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">1</text><text x="236" y="134" font-family="Cambria Math" font-size="40" font-weight="700" fill="#1f2430">1</text><text x="20" y="134" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">1</text><text x="130" y="22" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">1</text>')
# tile: a rectangle partly covered with square tiles
math-3-area/tile = rect_dims(5, 3, 320, partial=8)
# row: a 3 by 4 array of squares with one row highlighted
math-3-area/row = rect_dims(4, 3, 320, hl_row=1)
# fraction: a circle cut into 4 equal parts with 1 part shaded
math-3-fractions-as-numbers/fraction = frac_circle(4, 1, 280, BLUE)
# numerator: the fraction 3/4 with the 3 highlighted beside a circle with 3 of 4 parts shaded
math-3-fractions-as-numbers/numerator = row(F('3', '4', 100, hn=RED), frac_circle(4, 3, 200, BLUE), gap=30)
# denominator: the fraction 3/4 with the 4 highlighted beside a circle cut into 4 parts
math-3-fractions-as-numbers/denominator = row(F('3', '4', 100, hd=RED), frac_circle(4, 0, 200, BLUE), gap=30)
# unit fraction: a bar cut into 8 equal parts with 1 part shaded
math-3-fractions-as-numbers/unit-fraction = frac_bar(8, 1, 400, 90, GREEN)
# equivalent fractions: a bar in halves and a bar in fourths with the same length shaded
math-3-fractions-as-numbers/equivalent-fractions = col(frac_bar(2, 1, 360, 70, BLUE), frac_bar(4, 2, 360, 70, ORANGE), gap=16)
# whole: a circle cut into 4 parts with all 4 shaded
math-3-fractions-as-numbers/whole = frac_circle(4, 4, 280, BLUE)
# number line: a number line from 0 to 1 marked in fourths
math-3-fractions-as-numbers/number-line = numberline(0, 4, 440, labels=['0', '1/4', '2/4', '3/4', '1'], color=BLUE)
# multiply: 3 bags with 4 apples in each
math-3-meaning-of-multiplication-and-division/multiply = grid([groups(1, 4, apple, 'bag', 50, per_row=2) for _ in range(3)], 3, gap=14)
# divide: 12 cookies shared onto 4 plates of 3
math-3-meaning-of-multiplication-and-division/divide = grid([groups(1, 3, cookie, 'plate', 50) for _ in range(4)], 2, gap=20)
# equal groups: 5 circles with 2 dots in each
math-3-meaning-of-multiplication-and-division/equal-groups = grid([groups(1, 2, dot, 'circle', 50) for _ in range(5)], 3, gap=16)
# array: an egg carton with 2 rows of 6 eggs
math-3-meaning-of-multiplication-and-division/array = raw(400, 200, '<rect x="5" y="20" width="390" height="170" rx="20" fill="#c9b79c" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<ellipse cx="{45 + c * 62}" cy="{65 + r * 78}" rx="24" ry="30" fill="#fdf6e8" stroke="#1f2430" stroke-width="4"/>' for r in range(2) for c in range(6)))
# factor: 3 × 5 = 15 with the 3 and the 5 circled
math-3-meaning-of-multiplication-and-division/factor = row(mark(M('3', 80), 'circle', BLUE), M('×', 70), mark(M('5', 80), 'circle', BLUE), M('= 15', 80), gap=12)
# product: 3 × 5 = 15 with the 15 circled
math-3-meaning-of-multiplication-and-division/product = row(M('3 × 5 =', 80), mark(M('15', 80), 'circle', RED), gap=14)
# quotient: 12 ÷ 4 = 3 with the 3 circled
math-3-meaning-of-multiplication-and-division/quotient = row(M('12 ÷ 4 =', 80), mark(M('3', 80), 'circle', RED), gap=14)
# pattern: number tiles 2, 4, 6, 8 joined by +2 arrows
math-3-patterns-and-two-step-problems/pattern = row(tile('2', BLUE, 80), arrow(60, ORANGE, text='+2'), tile('4', BLUE, 80), arrow(60, ORANGE, text='+2'), tile('6', BLUE, 80), arrow(60, ORANGE, text='+2'), tile('8', BLUE, 80), gap=4)
# rule: number tiles 5, 10, 15, 20 joined by +5 arrows
math-3-patterns-and-two-step-problems/rule = row(tile('5', GREEN, 80), arrow(60, ORANGE, text='+5'), tile('10', GREEN, 80), arrow(60, ORANGE, text='+5'), tile('15', GREEN, 80), arrow(60, ORANGE, text='+5'), tile('20', GREEN, 80), gap=4)
# two-step problem: two stair steps marked 1 and 2
math-3-patterns-and-two-step-problems/two-step-problem = stairs(2, 300, labels=['1', '2'], color=BLUE)
# equation: a balance scale with 3 × 4 on one side and 12 on the other
math-3-patterns-and-two-step-problems/equation = col(row(box(M('3 × 4', 50), color=BLUE, p=14), box(M('12', 50), color=ORANGE, p=14), gap=110), scale_icon(340), gap=-60)
# unknown: 5 × a box with a question mark = 20
math-3-patterns-and-two-step-problems/unknown = row(M('5 ×', 80), box(T('?', 70, ORANGE), w=90, h=90, color=ORANGE, dashed=True), M('= 20', 80), gap=12)
# perimeter: a rectangular garden with arrows tracing its edge
math-3-perimeter/perimeter = raw(400, 280, '<rect x="40" y="40" width="320" height="200" rx="6" fill="#bfe3b0" stroke="#7a4a24" stroke-width="10"/>' + ''.join(f'<circle cx="{95 + c * 70}" cy="{90 + r * 50}" r="15" fill="#2f9e5b"/>' for r in range(3) for c in range(4)) + '<path d="M40 20 H340" stroke="#e04848" stroke-width="7"/><path d="M360 20 l-24 -12 v24 z" fill="#e04848"/><path d="M380 40 V220" stroke="#e04848" stroke-width="7"/><path d="M380 240 l-12 -24 h24 z" fill="#e04848"/><path d="M360 260 H60" stroke="#e04848" stroke-width="7"/><path d="M40 260 l24 -12 v24 z" fill="#e04848"/><path d="M20 240 V60" stroke="#e04848" stroke-width="7"/><path d="M20 40 l-12 24 h24 z" fill="#e04848"/>')
# side: a triangle with one side highlighted
math-3-perimeter/side = triangle(300, hl_side=0)
# width: a rectangle with a red arrow across it from side to side
math-3-perimeter/width = raw(360, 240, '<rect x="20" y="20" width="320" height="160" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/><path d="M34 210 H326" stroke="#e04848" stroke-width="7"/><path d="M20 210 l22 -12 v24 z M340 210 l-22 -12 v24 z" fill="#e04848"/>')
# polygon: a plain red octagon
math-3-perimeter/polygon = poly(8, 280, RED, fill=RED, rot=22.5)
# quadrilateral: four different four-sided shapes
math-3-quadrilaterals/quadrilateral = grid([shape('square', 110, BLUE), shape('rectangle', 130, ORANGE), shape('trapezoid', 130, GREEN), shape('rhombus', 120, PURPLE)], 2, gap=20)
# right angle: a corner with a small square mark in it
math-3-quadrilaterals/right-angle = raw(280, 280, '<path d="M40 20 V240 H260" fill="none" stroke="#1f2430" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 190 H90 V240" fill="none" stroke="#e04848" stroke-width="7"/>')
# attribute: a rectangle with its sides numbered 1 to 4
math-3-quadrilaterals/attribute = raw(360, 260, '<rect x="40" y="40" width="280" height="170" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="#f08a24" stroke-width="5"/><text x="{x}" y="{y + 11}" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for x, y, t in ((180, 40, 1), (320, 125, 2), (180, 210, 3), (40, 125, 4))))
# round: 47 on a number line with a red arrow to 50, circled
math-3-rounding-and-multi-digit-operations/round = numberline(40, 50, 460, marks={47: RED}, hl=50, every=5, color=BLUE, to=(47, 50))
# nearest ten: 82 on a number line with a red arrow to the nearest ten, 80, circled
math-3-rounding-and-multi-digit-operations/nearest-ten = numberline(80, 90, 460, marks={82: RED}, hl=80, every=5, color=BLUE, to=(82, 80))
# place value: a hundreds, tens and ones chart holding 3, 5 and 2
math-3-rounding-and-multi-digit-operations/place-value = place_chart(['hundreds', 'tens', 'ones'], ['3', '5', '2'], 340)
# digit: the digits 0 to 9 on tiles
math-3-rounding-and-multi-digit-operations/digit = grid([tile(str(i), (BLUE, ORANGE, GREEN, PURPLE, RED)[i % 5], 70) for i in range(10)], 5, gap=10)
# regroup: ten unit cubes becoming one rod of ten
math-3-rounding-and-multi-digit-operations/regroup = row(objects(10, cube_icon, cols=5, size=34, color=GREEN, gap=6), arrow(70), rod(10, 26), gap=16)
# sum: 200 + 150 = 350 with the 350 circled
math-3-rounding-and-multi-digit-operations/sum = row(M('200 + 150 =', 64), mark(M('350', 64), 'circle', RED), gap=10)
# difference: 500 − 120 = 380 with the 380 circled
math-3-rounding-and-multi-digit-operations/difference = row(M('500 − 120 =', 64), mark(M('380', 64), 'circle', RED), gap=10)
# bar graph: a bar graph with four bars of different heights
math-3-scaled-graphs/bar-graph = bars([3, 6, 2, 5], size=300, colors=[BLUE, ORANGE, GREEN, PURPLE], ticks=True)
# picture graph: a picture graph with rows of apple icons
math-3-scaled-graphs/picture-graph = col(*[row(*[apple(56) for _ in range(n)], gap=8) for n in (4, 2, 5)], gap=16, align='l')
# scale: a graph axis marked 0, 5, 10, 15, 20
math-3-scaled-graphs/scale = raw(200, 320, '<line x1="80" y1="10" x2="80" y2="300" stroke="#1f2430" stroke-width="7"/>' + ''.join(f'<line x1="66" y1="{300 - i * 70}" x2="94" y2="{300 - i * 70}" stroke="#1f2430" stroke-width="6"/><text x="56" y="{312 - i * 70}" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#1f2430">{i * 5}</text>' for i in range(5)))
# key: a box showing one star = 10
math-3-scaled-graphs/key = box(row(star(90), M('= 10', 80), gap=14), color=DARK, p=20)
# line plot: a line plot: X marks stacked over each value
math-3-scaled-graphs/line-plot = numberline(3, 7, 420, dots_={3: 1, 4: 3, 5: 4, 6: 2, 7: 1}, color=BLUE, xs=True)
# data: a tally chart with three rows of tally marks
math-3-scaled-graphs/data = table(cells=[['', ''], ['A', ''], ['B', ''], ['C', '']], size=300) if 0 else col(*[row(T(c, 50, k), tally(n, 80), gap=20) for c, k, n in (('A', BLUE, 4), ('B', ORANGE, 5), ('C', GREEN, 2))], gap=14, align='l')
# elapsed time: two clocks showing 2:00 and 2:45 joined by an arrow
math-3-time-volume-and-mass/elapsed-time = row(clock(170, 2, 0), arrow(70, ORANGE, text='45 min'), clock(170, 2, 45), gap=10)
# minute: a clock face with the minute hand sweeping 20 minutes
math-3-time-volume-and-mass/minute = clock(300, 12, 20, hl='minute')
# times table: a 10 by 10 multiplication chart with the 5 row shaded
math-3-times-tables-fluency/times-table = raw(320, 320, ''.join(f'<rect x="{10 + c * 30}" y="{10 + r * 30}" width="30" height="30" fill="{"#fde97a" if r == 4 else "#fff"}" stroke="#c4c8d0" stroke-width="2"/><text x="{25 + c * 30}" y="{31 + r * 30}" font-family="Segoe UI" font-size="13" text-anchor="middle" fill="#1f2430">{(r + 1) * (c + 1)}</text>' for r in range(10) for c in range(10)) + '<rect x="10" y="10" width="300" height="300" fill="none" stroke="#1f2430" stroke-width="4"/>')
# fact family: a small house with 3, 4 and 12 on the roof and four facts inside
math-3-times-tables-fluency/fact-family = raw(280, 320, '<path d="M14 120 L140 16 L266 120 Z" fill="#f08a24" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><rect x="34" y="120" width="212" height="190" fill="#fde3c8" stroke="#1f2430" stroke-width="6"/><text x="140" y="102" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#fff">3  4  12</text>' + ''.join(f'<text x="140" y="{160 + i * 40}" font-family="Cambria Math" font-size="32" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for i, t in enumerate(('3 × 4 = 12', '4 × 3 = 12', '12 ÷ 3 = 4', '12 ÷ 4 = 3'))))
# multiple: a number line with hops of 5 landing on 5, 10 and 15
math-3-times-tables-fluency/multiple = numberline(0, 15, 460, hops=[(0, 5), (5, 10), (10, 15)], every=5, marks={5: ORANGE, 10: ORANGE, 15: ORANGE}, color=BLUE)
# skip count: a frog hopping along a number line by 3s
math-3-times-tables-fluency/skip-count = col(row(Item(260, 10, ''), frog(90), gap=0), numberline(0, 12, 460, hops=[(0, 3), (3, 6), (6, 9), (9, 12)], every=3, color=GREEN), gap=-10)
# commutative property: a 4 by 6 array turning into a 6 by 4 array
math-3-times-tables-fluency/commutative-property = row(dots(24, 6, 24, BLUE, gap=8), curve_arrow(40, ORANGE), dots(24, 4, 24, ORANGE, gap=8), gap=12)
# unit fraction: a bar cut into sixths with one shaded
math-4-adding-and-multiplying-fractions/unit-fraction = frac_bar(6, 1, 400, 90, BLUE)
# mixed number: two whole circles and a quarter circle
math-4-adding-and-multiplying-fractions/mixed-number = row(frac_circle(4, 4, 140, BLUE), frac_circle(4, 4, 140, BLUE), frac_circle(4, 1, 140, BLUE), gap=14)
# improper fraction: two whole circles of fourths plus one more fourth: 9/4
math-4-adding-and-multiplying-fractions/improper-fraction = row(frac_circle(4, 4, 120, BLUE), frac_circle(4, 4, 120, BLUE), frac_circle(4, 1, 120, BLUE), M('=', 60), F('9', '4', 70), gap=12)
# decompose: five parts broken into three parts and two parts: 5 = 3 + 2
math-4-adding-and-multiplying-fractions/decompose = col(frac_bar(5, 5, 360, 70, ORANGE), arrow(40, dir='down'), row(frac_bar(3, 3, 216, 70, ORANGE), frac_bar(2, 2, 144, 70, BLUE), gap=20), M('5 = 3 + 2', 60), gap=8)
# like denominators: 2/8 + 3/8 = 5/8
math-4-adding-and-multiplying-fractions/like-denominators = eq(('2', '8'), '+', ('3', '8'), '=', ('5', '8'), size=80)
# whole: a circle cut into four shaded fourths
math-4-adding-and-multiplying-fractions/whole = frac_circle(4, 4, 280, BLUE)
# angle: two rays meeting at a point
math-4-angles-and-line-plots/angle = angle(300, 50)
# degree: a full turn around a circle is 360 degrees
math-4-angles-and-line-plots/degree = raw(300, 340, '<circle cx="150" cy="150" r="120" fill="#d6e6fb" stroke="#1f2430" stroke-width="7"/><path d="M150 150 L270 150" stroke="#1f2430" stroke-width="5"/><circle cx="150" cy="150" r="7" fill="#1f2430"/><path d="M200 150 A50 50 0 1 1 199.6 143.7" fill="none" stroke="#e04848" stroke-width="6"/><path d="M200 140 l-10 14 l18 2 z" fill="#e04848"/><text x="150" y="330" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#e04848">360°</text>')
# vertex: an angle with its corner dotted
math-4-angles-and-line-plots/vertex = angle(300, 50, vertex_dot=True)
# ray: a dot with an arrow going right
math-4-angles-and-line-plots/ray = raw(400, 100, '<circle cx="30" cy="50" r="16" fill="#1f2430"/><line x1="30" y1="50" x2="360" y2="50" stroke="#1f2430" stroke-width="8"/><path d="M390 50 l-36 -20 v40 z" fill="#1f2430"/>')
# line plot: a line plot of fractions: X marks stacked over each value
math-4-angles-and-line-plots/line-plot = numberline(0, 4, 440, labels=['0', '1/4', '1/2', '3/4', '1'], dots_={0: 1, 1: 3, 2: 4, 3: 2, 4: 1}, color=BLUE, xs=True)
# decimal: 0.5 next to a half-shaded square
math-4-decimals/decimal = row(M('0.5', 110), grid_shade(10, 10, 50, 220, BLUE), gap=24)
# decimal point: $3.25 with the point circled
math-4-decimals/decimal-point = row(M('$3', 120), mark(M('.', 120), 'circle', RED), M('25', 120), gap=0)
# tenths: a bar cut into 10 with 3 shaded
math-4-decimals/tenths = frac_bar(10, 3, 420, 80, GREEN)
# hundredths: a 10 by 10 grid with 25 squares shaded
math-4-decimals/hundredths = grid_shade(10, 10, 25, 300, ORANGE)
# place value: a place value chart for 0.45 with the decimal point after the ones
math-4-decimals/place-value = place_chart(['ones', 'tenths', 'hundredths'], ['0', '4', '5'], 360, point=0)
# compare: 0.6 > 0.45 with shaded grids
math-4-decimals/compare = row(col(grid_shade(10, 10, 60, 150, BLUE), M('0.6', 50), gap=6), M('>', 80, color=RED), col(grid_shade(10, 10, 45, 150, ORANGE), M('0.45', 50), gap=6), gap=14)
# equivalent fractions: two bars, one cut in halves, one in fourths
math-4-equivalent-fractions-and-comparing/equivalent-fractions = col(frac_bar(2, 1, 360, 70, BLUE), frac_bar(4, 2, 360, 70, ORANGE), gap=16)
# numerator: 3/5 with the 3 highlighted
math-4-equivalent-fractions-and-comparing/numerator = F('3', '5', 150, hn=RED)
# denominator: 3/5 with the 5 highlighted
math-4-equivalent-fractions-and-comparing/denominator = F('3', '5', 150, hd=RED)
# benchmark fraction: a number line with 0, 1/2 and 1
math-4-equivalent-fractions-and-comparing/benchmark-fraction = numberline(0, 2, 440, labels=['0', '1/2', '1'], marks={1: ORANGE}, color=BLUE)
# common denominator: two bars cut into twelfths
math-4-equivalent-fractions-and-comparing/common-denominator = col(frac_bar(12, 8, 400, 60, BLUE), frac_bar(12, 9, 400, 60, ORANGE), gap=16)
# greater than: 3/4 > 1/2
math-4-equivalent-fractions-and-comparing/greater-than = row(F('3', '4', 110), M('>', 110, color=RED), F('1', '2', 110), gap=20)
# factor: a 3 by 4 array
math-4-factors-and-multiples/factor = dots(12, 4, 50, BLUE)
# multiple: a number line with jumps of 5
math-4-factors-and-multiples/multiple = numberline(0, 20, 460, hops=[(0, 5), (5, 10), (10, 15), (15, 20)], every=5, color=BLUE)
# factor pair: a 3 by 4 rectangle labeled 12
math-4-factors-and-multiples/factor-pair = col(grid_shade(4, 3, 12, 280, GREEN) if 0 else rect_dims(4, 3, 300), M('12', 60, color=ORANGE), gap=6)
# prime number: 7 dots that only make one row
math-4-factors-and-multiples/prime-number = dots(7, 7, 44, ORANGE)
# composite number: three different rectangles of 12 dots
math-4-factors-and-multiples/composite-number = col(dots(12, 12, 22, BLUE, gap=6), dots(12, 6, 22, ORANGE, gap=6), dots(12, 4, 22, GREEN, gap=6), gap=20)
# divisible: 18 dots in 3 even groups
math-4-factors-and-multiples/divisible = grid([box(dots(6, 3, 30, BLUE), color=BLUE, p=10) for _ in range(3)], 3, gap=14)
# parallel: two parallel lines
math-4-lines-angles-and-symmetry/parallel = lines_pair('parallel', 300)
# perpendicular: two lines crossing at a right angle
math-4-lines-angles-and-symmetry/perpendicular = lines_pair('perpendicular', 300)
# right angle: an angle with a small square at the corner
math-4-lines-angles-and-symmetry/right-angle = angle(300, 90, right=True)
# convert: a 12-inch ruler: 1 foot = 12 inches
math-4-measurement-conversions/convert = col(ruler(420, 12, 'in', inches=True), T('1 foot = 12 inches', 40), gap=12)
# unit: a ruler marked in inches
math-4-measurement-conversions/unit = ruler(420, 6, 'in', inches=True)
# perimeter: a rectangle with its edges traced
math-4-measurement-conversions/perimeter = rect_dims(5, 3, 320, units=False, trace=True)
# area: a rectangle filled with unit squares
math-4-measurement-conversions/area = rect_dims(5, 3, 320)
# formula: A = l × w
math-4-measurement-conversions/formula = M('A = l × w', 110)
# product: 23 × 4 = 92
math-4-multi-digit-multiplication-and-division/product = M('23 × 4 = 92', 90)
# partial products: 23 × 4 as an area model: 20 × 4 = 80 and 3 × 4 = 12, then 80 + 12 = 92
math-4-multi-digit-multiplication-and-division/partial-products = raw(420, 290, '<text x="165" y="40" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#3a7bd5">20</text><text x="345" y="40" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#f08a24">3</text><text x="20" y="140" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">4</text><rect x="40" y="56" width="250" height="140" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="290" y="56" width="110" height="140" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><text x="165" y="142" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">80</text><text x="345" y="142" font-family="Cambria Math" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">12</text><text x="220" y="262" font-family="Cambria Math" font-size="46" font-weight="700" text-anchor="middle" fill="#e04848">80 + 12 = 92</text>')
# area model: a rectangle split into four boxes
math-4-multi-digit-multiplication-and-division/area-model = raw(340, 260, '<rect x="10" y="10" width="220" height="150" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><rect x="230" y="10" width="100" height="150" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><rect x="10" y="160" width="220" height="90" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><rect x="230" y="160" width="100" height="90" fill="#d3f0de" stroke="#1f2430" stroke-width="5"/>')
# quotient: 84 ÷ 4 = 21
math-4-multi-digit-multiplication-and-division/quotient = M('84 ÷ 4 = 21', 90)
# dividend: 84 ÷ 4 with 84 highlighted
math-4-multi-digit-multiplication-and-division/dividend = M('84 ÷ 4', 120, hl={'84': RED})
# divisor: 84 ÷ 4 with 4 highlighted
math-4-multi-digit-multiplication-and-division/divisor = M('84 ÷ 4', 120, hl={'4': RED}) if 0 else row(M('84 ÷', 120), M('4', 120, color=RED), gap=20)
# times as many: one bar and a bar three times as long
math-4-multiplicative-comparison/times-as-many = col(raw(110, 60, '<rect x="5" y="5" width="100" height="50" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>'), raw(320, 60, ''.join(f'<rect x="{5 + i * 100}" y="5" width="100" height="50" fill="#f08a24" stroke="#1f2430" stroke-width="5"/>' for i in range(3))), gap=16, align='l')
# multiply: 4 rows of 6 dots
math-4-multiplicative-comparison/multiply = dots(24, 6, 40, BLUE)
# remainder: 17 dots in 3 groups of 5 with 2 left over
math-4-multiplicative-comparison/remainder = row(*[box(dots(5, 5, 26, BLUE, gap=6), color=BLUE, p=10) for _ in range(3)], dots(2, 1, 26, ORANGE, gap=8), gap=12) if 0 else col(*[box(dots(5, 5, 32, BLUE, gap=6), color=BLUE, p=10) for _ in range(3)], row(dot(32, ORANGE), dot(32, ORANGE), gap=10), gap=10)
# equation: 5 × 3 = 15
math-4-multiplicative-comparison/equation = M('5 × 3 = 15', 100)
# unknown: 4 × □ = 28
math-4-multiplicative-comparison/unknown = row(M('4 ×', 90), box(w=80, h=90, color=ORANGE, dashed=True), M('= 28', 90), gap=12)
# pattern: four boxes holding 3, 6, 9, 12
math-4-number-patterns/pattern = row(*[box(M(str(v), 60), color=BLUE, w=100, h=100) for v in (3, 6, 9, 12)], gap=14)
# rule: 3, 7, 11, 15: the rule is add 4 each time
math-4-number-patterns/rule = numberline(3, 15, 460, step=4, hops=[(3, 7), (7, 11), (11, 15)], hop_label='+4', marks={3: RED, 7: RED, 11: RED, 15: RED})
# term: a row of numbers with the fifth one circled
math-4-number-patterns/term = row(*[mark(T(str(v), 64), 'circle', RED) if i == 4 else T(str(v), 64) for i, v in enumerate((3, 6, 9, 12, 15, 18))], gap=20)
# sequence: 2, 4, 8, 16 in a row
math-4-number-patterns/sequence = row(*[tile(str(v), c, 90) for v, c in ((2, BLUE), (4, ORANGE), (8, GREEN), (16, PURPLE))], gap=14)
# input: a machine with 5 going in
math-4-number-patterns/input = machine(380, '5', None, 'f')
# output: a machine with 10 coming out
math-4-number-patterns/output = machine(380, None, '10', 'f')
# million: 1,000,000 with commas highlighted
math-4-place-value-to-a-million/million = M('1,000,000', 110, hl={',': RED})
# period: 452,310 with the first three digits boxed
math-4-place-value-to-a-million/period = row(col(box(M('452', 90), color=ORANGE, p=10), T('thousands', 30, ORANGE), gap=6), col(M(',', 90), T(' ', 30), gap=6), col(box(M('310', 90), color=BLUE, p=10), T('ones', 30, BLUE), gap=6), gap=4, align='b')
# digit: the digits 0 to 9
math-4-place-value-to-a-million/digit = grid([tile(str(i), (BLUE, ORANGE, GREEN, PURPLE, RED)[i % 5], 70) for i in range(10)], 5, gap=10)
# round: 4,800 on a number line with a red arrow to 5,000, circled
math-4-place-value-to-a-million/round = numberline(4000, 5000, 460, step=500, marks={4800: RED}, hl=5000, color=BLUE, to=(4800, 5000))
# standard form: 305,120 in bold
math-4-place-value-to-a-million/standard-form = M('305,120', 130)
# word form: 1,200 next to a written word line
math-4-place-value-to-a-million/word-form = col(M('1,200', 100), T('one thousand two hundred', 34, BLUE, bold=True), gap=16)
# unlike denominators: a bar in thirds and a bar in fourths
math-5-adding-unlike-fractions/unlike-denominators = col(frac_bar(3, 1, 360, 70, BLUE), frac_bar(4, 1, 360, 70, ORANGE), gap=16)
# common denominator: two bars cut into twelfths
math-5-adding-unlike-fractions/common-denominator = col(frac_bar(12, 8, 400, 60, BLUE), frac_bar(12, 9, 400, 60, ORANGE), gap=16)
# least common multiple: number lines of 4s and 6s meeting at 12
math-5-adding-unlike-fractions/least-common-multiple = col(numberline(0, 12, 440, hops=[(0, 4), (4, 8), (8, 12)], every=4, marks={12: RED}, color=BLUE), numberline(0, 12, 440, hops=[(0, 6), (6, 12)], every=6, marks={12: RED}, color=ORANGE), gap=6)
# equivalent: two bars with equal shaded lengths
math-5-adding-unlike-fractions/equivalent = col(frac_bar(3, 2, 360, 70, BLUE), frac_bar(6, 4, 360, 70, ORANGE), gap=16)
# simplify: 6/8 = 3/4
math-5-adding-unlike-fractions/simplify = eq(('6', '8'), '=', ('3', '4'), size=110)
# benchmark: a number line with 1/2 marked
math-5-adding-unlike-fractions/benchmark = numberline(0, 2, 440, labels=['0', '1/2', '1'], marks={1: RED}, color=BLUE)
# polygon: a triangle, a square and a hexagon
math-5-classifying-2d-figures/polygon = row(shape('triangle', 120, BLUE), shape('square', 110, ORANGE), poly(6, 120, GREEN), gap=20)
# parallelogram: a slanted parallelogram
math-5-classifying-2d-figures/parallelogram = shape('parallelogram', 300, BLUE)
# rhombus: a rhombus
math-5-classifying-2d-figures/rhombus = shape('rhombus', 280, ORANGE)
# trapezoid: a trapezoid
math-5-classifying-2d-figures/trapezoid = shape('trapezoid', 300, GREEN)
# hierarchy: a tree diagram of shape groups
math-5-classifying-2d-figures/hierarchy = raw(400, 300, '<rect x="130" y="10" width="140" height="60" rx="12" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="5"/><rect x="20" y="130" width="140" height="60" rx="12" fill="#fde3c8" stroke="#f08a24" stroke-width="5"/><rect x="240" y="130" width="140" height="60" rx="12" fill="#fde3c8" stroke="#f08a24" stroke-width="5"/><rect x="180" y="230" width="100" height="60" rx="12" fill="#d3f0de" stroke="#2f9e5b" stroke-width="5"/><rect x="290" y="230" width="100" height="60" rx="12" fill="#d3f0de" stroke="#2f9e5b" stroke-width="5"/><path d="M200 70 L90 130 M200 70 L310 130 M310 190 L230 230 M310 190 L340 230" stroke="#1f2430" stroke-width="5"/>' + '<polygon points="200,25 222,55 178,55" fill="#3a7bd5"/><rect x="70" y="145" width="40" height="30" fill="#f08a24"/><polygon points="290,175 330,175 340,145 300,145" fill="#f08a24"/><rect x="215" y="245" width="30" height="30" fill="#2f9e5b"/><rect x="320" y="248" width="40" height="24" fill="#2f9e5b"/>')
# expression: 3 × (4 + 2)
math-5-expressions-and-order-of-operations/expression = M('3 × (4 + 2)', 100)
# order of operations: a stack of steps: ( ), ×÷, +−
math-5-expressions-and-order-of-operations/order-of-operations = col(box(M('( )', 60), color=RED, w=220, h=80), box(M('× ÷', 60), color=ORANGE, w=220, h=80), box(M('+ −', 60), color=BLUE, w=220, h=80), gap=10)
# parentheses: large parentheses around 4 + 2
math-5-expressions-and-order-of-operations/parentheses = row(M('(', 220, color=BLUE), M('4 + 2', 90), M(')', 220, color=BLUE), gap=4)
# brackets: [2 × (3 + 1)]
math-5-expressions-and-order-of-operations/brackets = M('[2 × (3 + 1)]', 90, hl={'[': ORANGE, ']': ORANGE})
# evaluate: 10 − 2 × 3 = 4
math-5-expressions-and-order-of-operations/evaluate = M('10 − 2 × 3 = 4', 80)
# sum: 6 + 7 = 13
math-5-expressions-and-order-of-operations/sum = M('6 + 7 = 13', 110)
# scaling: a bar and a bar half as long
math-5-multiplying-and-dividing-fractions/scaling = col(raw(360, 60, '<rect x="5" y="5" width="350" height="50" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>'), raw(360, 60, '<rect x="5" y="5" width="175" height="50" fill="#f08a24" stroke="#1f2430" stroke-width="5"/>'), gap=16, align='l')
# product: a square with one sixth double-shaded
math-5-multiplying-and-dividing-fractions/product = raw(300, 300, '<rect x="10" y="10" width="280" height="280" fill="#fff" stroke="#1f2430" stroke-width="5"/><rect x="10" y="10" width="140" height="280" fill="#3a7bd5" fill-opacity="0.35"/><rect x="10" y="10" width="280" height="93" fill="#f08a24" fill-opacity="0.45"/><path d="M150 10 V290 M10 103 H290 M10 196 H290" stroke="#1f2430" stroke-width="4"/><rect x="10" y="10" width="140" height="93" fill="none" stroke="#e04848" stroke-width="7"/>')
# reciprocal: 2/3 with an arrow flipping it to 3/2
math-5-multiplying-and-dividing-fractions/reciprocal = row(F('2', '3', 110), curve_arrow(40, ORANGE), F('3', '2', 110), gap=14)
# unit fraction: 3 bars each cut into fourths
math-5-multiplying-and-dividing-fractions/unit-fraction = col(*[frac_bar(4, 1, 340, 56, c) for c in (BLUE, ORANGE, GREEN)], gap=12)
# of: 8 dots with half circled
math-5-multiplying-and-dividing-fractions/of = row(mark(dots(4, 2, 40, ORANGE), 'circle', RED), dots(4, 2, 40, BLUE), gap=20)
# area model: a rectangle with overlapping shaded parts
math-5-multiplying-and-dividing-fractions/area-model = raw(300, 300, '<rect x="10" y="10" width="280" height="280" fill="#fff" stroke="#1f2430" stroke-width="5"/><rect x="10" y="10" width="187" height="280" fill="#3a7bd5" fill-opacity="0.35"/><rect x="10" y="10" width="280" height="140" fill="#f08a24" fill-opacity="0.45"/><path d="M103 10 V290 M197 10 V290 M10 150 H290" stroke="#1f2430" stroke-width="4"/>')
# algorithm: a stacked multiplication problem
math-5-operations-with-whole-numbers-and-decimals/algorithm = col(M('  34', 80), M('× 12', 80), raw(200, 8, '<rect width="200" height="8" fill="#1f2430"/>'), M('  68', 80, color=BLUE), M('340', 80, color=ORANGE), raw(200, 8, '<rect width="200" height="8" fill="#1f2430"/>'), M('408', 80), gap=0, align='r')
# estimate: 4.9 × 3 ≈ 15
math-5-operations-with-whole-numbers-and-decimals/estimate = M('4.9 × 3 ≈ 15', 90, hl={'≈': ORANGE})
# long division: a long division bracket with 728
math-5-operations-with-whole-numbers-and-decimals/long-division = raw(320, 160, '<path d="M60 40 Q80 80 60 140" fill="none" stroke="#1f2430" stroke-width="7"/><line x1="60" y1="40" x2="300" y2="40" stroke="#1f2430" stroke-width="7"/><text x="40" y="112" font-family="Cambria Math" font-size="60" font-weight="700" text-anchor="end" fill="#3a7bd5">4</text><text x="180" y="112" font-family="Cambria Math" font-size="70" font-weight="700" text-anchor="middle" fill="#1f2430">728</text>')
# decimal: 2.50 + 1.25 stacked
math-5-operations-with-whole-numbers-and-decimals/decimal = col(M('  2.50', 80), M('+ 1.25', 80), raw(230, 8, '<rect width="230" height="8" fill="#1f2430"/>'), M('  3.75', 80, color=BLUE), gap=0, align='r')
# line up: two decimals stacked with points aligned
math-5-operations-with-whole-numbers-and-decimals/line-up = raw(340, 220, '<text x="190" y="90" font-family="Cambria Math" font-size="80" font-weight="700" text-anchor="end" fill="#1f2430">12</text><text x="190" y="90" font-family="Cambria Math" font-size="80" font-weight="700" fill="#1f2430">.50</text><text x="190" y="190" font-family="Cambria Math" font-size="80" font-weight="700" text-anchor="end" fill="#1f2430">3</text><text x="190" y="190" font-family="Cambria Math" font-size="80" font-weight="700" fill="#1f2430">.25</text><line x1="195" y1="10" x2="195" y2="210" stroke="#e04848" stroke-width="5" stroke-dasharray="10 8"/>')
# reasonable: 4.9 × 3 = 14.7 is close to 5 × 3 = 15, so the answer makes sense
math-5-operations-with-whole-numbers-and-decimals/reasonable = col(M('4.9 × 3 = 14.7', 64), M('≈ 5 × 3 = 15', 64, color=GRAY), check(70), gap=8)
# ordered pair: a point on a grid with dashed lines to each axis and its (x, y) label
math-5-patterns-and-relationships/ordered-pair = coord(320, points=[(3, 5)], first=True, n=6, guides=True)
# relationship: two rows, 1 2 3 and 2 4 6, joined by arrows
math-5-patterns-and-relationships/relationship = col(row(*[tile(str(v), BLUE, 80) for v in (1, 2, 3)], gap=40), row(*[arrow(50, ORANGE, 'down') for _ in range(3)], gap=70), row(*[tile(str(v), ORANGE, 80) for v in (2, 4, 6)], gap=40), gap=6)
# x-axis: a graph with the horizontal axis highlighted
math-5-patterns-and-relationships/x-axis = coord(320, first=True, hl_axis='x', n=6)
# y-axis: a graph with the vertical axis highlighted
math-5-patterns-and-relationships/y-axis = coord(320, first=True, hl_axis='y', n=6)
# corresponding terms: two number rows with matching positions circled
math-5-patterns-and-relationships/corresponding-terms = col(row(*[mark(tile(str(v), BLUE, 70), 'circle', RED) if v == 3 else tile(str(v), BLUE, 70) for v in (1, 2, 3, 4)], gap=16), row(*[mark(tile(str(v), ORANGE, 70), 'circle', RED) if v == 9 else tile(str(v), ORANGE, 70) for v in (3, 6, 9, 12)], gap=16), gap=20)
# graph: dots on a grid forming a line
math-5-patterns-and-relationships/graph = plot(size=320, xr=(0, 7), yr=(0, 7), grid_=True, points=[(x, x, RED) for x in range(1, 7)])
# power of ten: 10, 100, 1,000 in growing boxes
math-5-powers-of-ten-and-decimals/power-of-ten = row(box(M('10', 40), color=BLUE, w=80, h=80), box(M('100', 50), color=ORANGE, w=120, h=120), box(M('1,000', 56), color=GREEN, w=180, h=180), gap=14, align='b')
# exponent: 10³ with the 3 highlighted
math-5-powers-of-ten-and-decimals/exponent = row(M('10', 150), M('3', 90, color=RED), gap=0, align='t')
# thousandths: 0.125 in a place value chart with the thousandths column picked out
math-5-powers-of-ten-and-decimals/thousandths = place_chart(['ones', 'tenths', 'hundredths', 'thousandths'], ['0', '1', '2', '5'], 420, hl=3, point=0)
# expanded form: 3.25 = 3 + 0.2 + 0.05
math-5-powers-of-ten-and-decimals/expanded-form = M('3.25 = 3 + 0.2 + 0.05', 54)
# round: 2.63 on a number line with a red arrow to 2.6, circled
math-5-powers-of-ten-and-decimals/round = numberline(0, 10, 460, labels=['2.6', '', '', '', '', '2.65', '', '', '', '', '2.7'], marks={3: RED}, hl=0, color=BLUE, to=(3, 0))
# place value chart: a place value chart for 3.142 with the decimal point after the ones
math-5-powers-of-ten-and-decimals/place-value-chart = place_chart(['ones', 'tenths', 'hundredths', 'thousandths'], ['3', '1', '4', '2'], 420, point=0)
# coordinate plane: a first-quadrant grid with a star
math-5-the-coordinate-plane/coordinate-plane = coord(320, first=True, star_at=(4, 3), n=6)
# origin: a grid with a dot at the corner
math-5-the-coordinate-plane/origin = coord(320, first=True, origin=True, n=6)
# coordinates: a star on a grid at (4, 2), with dashed lines to each axis
math-5-the-coordinate-plane/coordinates = coord(320, first=True, star_at=(4, 2), n=6, guides=True)
# plot: a pencil tip on a grid dot
math-5-the-coordinate-plane/plot = over(coord(320, first=True, points=[(3, 4)], n=6), pencil(180, angle=-35), dx=60, dy=-50)
# quadrant: a plane with the top-right quarter shaded
math-5-the-coordinate-plane/quadrant = coord(320, quad=1)
# axis: a coordinate grid with the x-axis drawn thick and named
math-5-the-coordinate-plane/axis = coord(320, hl_axis='x')
# convert: a meter stick marked in centimeters: 1 m = 100 cm
math-5-units-and-line-plots/convert = col(ruler(440, 100, 'cm', every=10), T('1 m = 100 cm', 40), gap=12)
# line plot: a line plot of fractions: X marks stacked over each value
math-5-units-and-line-plots/line-plot = numberline(0, 4, 440, labels=['0', '1/4', '1/2', '3/4', '1'], dots_={1: 2, 2: 3, 3: 1}, color=BLUE, xs=True)
# volume: a box built from unit cubes
math-5-volume/volume = solid('box', 300, BLUE, units=(4, 2, 3))
# cubic unit: a single unit cube
math-5-volume/cubic-unit = solid('cube', 220, GREEN)
# length × width × height: a box with l, w and h labeled
math-5-volume/length-width-height = solid('box', 300, BLUE, labels=('l', 'w', 'h'))
# base: a prism with its bottom face shaded
math-5-volume/base = raw(340, 290, '<path d="M40 250 L100 190 H300 L240 250 Z" fill="#f08a24" stroke="#1f2430" stroke-width="4" stroke-dasharray="10 7"/><rect x="40" y="90" width="200" height="160" fill="#d6e6fb" fill-opacity="0.35" stroke="#1f2430" stroke-width="6"/><path d="M40 90 L100 30 H300 L240 90 M240 250 L300 190 V30" fill="none" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M40 250 H240" stroke="#f08a24" stroke-width="10"/>')
# layer: a box split into two cube layers
math-5-volume/layer = solid('box', 300, ORANGE, units=(4, 2, 2))
# area: a 5 by 3 rectangle of unit squares: area 15 square units
math-6-area-surface-area-and-volume/area = col(rect_dims(5, 3, 320, labels=['5', '3']), T('15 square units', 40), gap=8)
# net: a cross-shaped cube net
math-6-area-surface-area-and-volume/net = raw(300, 380, ''.join(f'<rect x="{x}" y="{y}" width="90" height="90" fill="{c}" stroke="#1f2430" stroke-width="5"/>' for x, y, c in ((105, 10, '#d6e6fb'), (15, 100, '#fde3c8'), (105, 100, '#d6e6fb'), (195, 100, '#fde3c8'), (105, 190, '#d6e6fb'), (105, 280, '#d3f0de'))))
# surface area: an unfolded box with faces labeled
math-6-area-surface-area-and-volume/surface-area = raw(400, 300, ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="#1f2430" stroke-width="5"/><text x="{x + w / 2}" y="{y + h / 2 + 12}" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for x, y, w, h, c, t in ((100, 10, 160, 60, '#d3f0de', 'top'), (10, 70, 90, 120, '#fde3c8', 'side'), (100, 70, 160, 120, '#d6e6fb', 'front'), (260, 70, 90, 120, '#fde3c8', 'side'), (100, 190, 160, 60, '#d3f0de', 'bottom'))))
# volume: a box with fractional edges
math-6-area-surface-area-and-volume/volume = solid('box', 300, PURPLE, labels=('1/2', '1/3', '3/4'))
# base: a parallelogram with base marked
math-6-area-surface-area-and-volume/base = raw(380, 240, '<path d="M90 20 H370 L290 220 H10 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><line x1="10" y1="220" x2="290" y2="220" stroke="#e04848" stroke-width="12"/><text x="150" y="200" font-family="Cambria Math" font-size="44" font-weight="700" text-anchor="middle" fill="#e04848">b</text>')
# height: a triangle with a dashed height
math-6-area-surface-area-and-volume/height = triangle(320, pts=((10, 150), (190, 150), (70, 20)), height=True)
# independent variable: hours go in, times $10, pay comes out: hours is the independent variable (x)
math-6-dependent-and-independent-variables/independent-variable = row(mark(col(clock(100, 3, 0), T('hours (x)', 30, BLUE), gap=4), 'box', RED), arrow(50), box(M('× $10', 44), color=PURPLE, p=12), arrow(50), col(T('$', 100, GREEN), T('pay (y)', 30, GREEN), gap=0), gap=8)
# dependent variable: hours go in, times $10, pay comes out: pay is the dependent variable (y)
math-6-dependent-and-independent-variables/dependent-variable = row(col(clock(100, 3, 0), T('hours (x)', 30, BLUE), gap=4), arrow(50), box(M('× $10', 44), color=PURPLE, p=12), arrow(50), mark(col(T('$', 100, GREEN), T('pay (y)', 30, GREEN), gap=0), 'box', RED), gap=8)
# relationship: a straight line graph
math-6-dependent-and-independent-variables/relationship = plot(lambda x: 0.8 * x + 0.5, size=320, xr=(0, 8), yr=(0, 8))
# table of values: a two-column table
math-6-dependent-and-independent-variables/table-of-values = table(cells=[['x', 'y'], ['1', '3'], ['2', '6'], ['3', '9']], size=280)
# graph: a rising line on a grid
math-6-dependent-and-independent-variables/graph = plot(lambda x: 0.8 * x + 0.5, size=320, xr=(0, 8), yr=(0, 8), grid_=True)
# equation: y = 3x
math-6-dependent-and-independent-variables/equation = M('y = 3x', 140)
# reciprocal: 3/4 flipping into 4/3
math-6-dividing-fractions/reciprocal = row(F('3', '4', 110), curve_arrow(40, ORANGE), F('4', '3', 110), gap=14)
# quotient: 12 split into 3 equal groups of 4: 12 ÷ 3 = 4, the quotient boxed
math-6-dividing-fractions/quotient = col(groups(3, 4, size=34), row(M('12 ÷ 3 =', 70), mark(M('4', 70), 'box', RED), gap=10), gap=16)
# divisor: 3/4 ÷ 1/8 with 1/8 highlighted
math-6-dividing-fractions/divisor = row(F('3', '4', 90), M('÷', 80), mark(F('1', '8', 90), 'circle', RED), gap=16)
# how many groups: 3/4 measured in eighths: six eighths fit, so 3/4 ÷ 1/8 = 6
math-6-dividing-fractions/how-many-groups = col(frac_bar(4, 3, 360, 60, BLUE), frac_bar(8, 6, 360, 60, ORANGE), raw(365, 34, ''.join(f'<text x="{2.5 + (i + 0.5) * 45:.1f}" y="28" font-family="Cambria Math" font-size="28" font-weight="700" text-anchor="middle" fill="#f08a24">{i + 1}</text>' for i in range(6))), eq(('3', '4'), '÷', ('1', '8'), '= 6', size=50), gap=8)
# multiply by the reciprocal: ÷ 2/5 turning into × 5/2
math-6-dividing-fractions/multiply-by-the-reciprocal = row(M('÷', 80), F('2', '5', 100), arrow(70, ORANGE), M('×', 80, color=ORANGE), F('5', '2', 100, color=ORANGE), gap=12)
# tape diagram: a bar with three quarters shaded and split
math-6-dividing-fractions/tape-diagram = frac_bar(4, 3, 400, 90, BLUE)
# variable: 3x + 2 with x highlighted
math-6-expressions-and-exponents/variable = M('3x + 2', 140, hl={'x': RED})
# coefficient: 3x with 3 highlighted
math-6-expressions-and-exponents/coefficient = M('3x', 200, hl={'3': RED})
# exponent: 2⁵ with 5 highlighted
math-6-expressions-and-exponents/exponent = row(M('2', 180), M('5', 100, color=RED), gap=0, align='t')
# term: 3x + 2 with two boxes
math-6-expressions-and-exponents/term = row(box(M('3x', 80), color=BLUE, p=14), M('+', 80), box(M('2', 80), color=ORANGE, p=14), gap=14)
# like terms: 3x and 5x in matching boxes
math-6-expressions-and-exponents/like-terms = row(box(M('3x', 80), color=BLUE, p=14), box(M('5x', 80), color=BLUE, p=14), gap=24)
# evaluate: 2(4) + 1 = 9
math-6-expressions-and-exponents/evaluate = M('2(4) + 1 = 9', 90)
# greatest common factor: factor lists with 6 circled
math-6-multi-digit-and-decimal-fluency/greatest-common-factor = col(row(M('12:', 50), *[mark(M(v, 50), 'circle', RED) if v == '6' else M(v, 50) for v in ('1', '2', '3', '4', '6', '12')], gap=14), row(M('18:', 50), *[mark(M(v, 50), 'circle', RED) if v == '6' else M(v, 50) for v in ('1', '2', '3', '6', '9', '18')], gap=14), gap=24, align='l')
# least common multiple: number lines meeting at 12
math-6-multi-digit-and-decimal-fluency/least-common-multiple = col(numberline(0, 12, 440, hops=[(0, 4), (4, 8), (8, 12)], every=4, marks={12: RED}, color=BLUE), numberline(0, 12, 440, hops=[(0, 6), (6, 12)], every=6, marks={12: RED}, color=ORANGE), gap=6)
# standard algorithm: a long division layout
math-6-multi-digit-and-decimal-fluency/standard-algorithm = raw(340, 260, '<path d="M90 30 Q110 70 90 120" fill="none" stroke="#1f2430" stroke-width="7"/><line x1="90" y1="30" x2="320" y2="30" stroke="#1f2430" stroke-width="7"/><text x="70" y="100" font-family="Cambria Math" font-size="56" font-weight="700" text-anchor="end" fill="#3a7bd5">4</text><text x="200" y="100" font-family="Cambria Math" font-size="60" font-weight="700" text-anchor="middle" fill="#1f2430">728</text><text x="200" y="20" font-family="Cambria Math" font-size="0" fill="#fff"></text><text x="140" y="160" font-family="Cambria Math" font-size="48" font-weight="700" fill="#8a8f9c">−4</text><line x1="120" y1="176" x2="200" y2="176" stroke="#1f2430" stroke-width="5"/><text x="150" y="226" font-family="Cambria Math" font-size="48" font-weight="700" fill="#8a8f9c">32</text>')
# distributive property: 6(3 + 4) = 6·3 + 6·4
math-6-multi-digit-and-decimal-fluency/distributive-property = M('6(3 + 4) = 6·3 + 6·4', 56, hl={'6': ORANGE})
# decimal: 2.5 × 1.2 = 3.0
math-6-multi-digit-and-decimal-fluency/decimal = M('2.5 × 1.2 = 3.0', 84)
# dividend: 7,452 ÷ 23 with 7,452 highlighted
math-6-multi-digit-and-decimal-fluency/dividend = row(M('7,452', 100, color=RED), M('÷ 23', 100), gap=16)
# negative number: a number line with −5 marked
math-6-negative-numbers/negative-number = numberline(-6, 6, 460, marks={-5: RED}, every=1, color=BLUE)
# integer: a number line with a dot on every whole number, negative and positive
math-6-negative-numbers/integer = numberline(-5, 5, 460, color=BLUE, marks={v: RED for v in range(-5, 6)})
# opposite: 4 and −4 mirrored around 0
math-6-negative-numbers/opposite = numberline(-5, 5, 460, marks={-4: ORANGE, 4: ORANGE}, hl=0, color=BLUE)
# absolute value: a bracket from −8 to 0 labeled 8
math-6-negative-numbers/absolute-value = numberline(-10, 2, 460, bracket=(-8, 0, '8'), marks={-8: RED}, every=2, color=BLUE)
# rational number: a number line with −1/2 marked
math-6-negative-numbers/rational-number = numberline(-2, 2, 460, labels=['−1', '−1/2', '0', '1/2', '1'], marks={-1: RED}, color=BLUE)
# quadrant: a four-quadrant grid with a dot
math-6-negative-numbers/quadrant = coord(320, points=[(-3, 2)])
# equation: a balance with x + 5 and 12
math-6-one-step-equations-and-inequalities/equation = col(row(box(M('x + 5', 50), color=BLUE, p=14), box(M('12', 50), color=ORANGE, p=14), gap=110), scale_icon(340), gap=-60)
# inequality: a number line with an open dot at 3 and an arrow right
math-6-one-step-equations-and-inequalities/inequality = numberline(0, 10, 460, open_=3, ray='right', color=BLUE)
# solution: a balanced scale with 7 + 5 and 12
math-6-one-step-equations-and-inequalities/solution = col(row(box(M('7 + 5', 50), color=BLUE, p=14), box(M('12', 50), color=ORANGE, p=14), gap=110), scale_icon(340), gap=-60)
# inverse operation: + 5 and − 5 arrows canceling
math-6-one-step-equations-and-inequalities/inverse-operation = row(arrow(120, GREEN, text='+ 5', sw=10), arrow(120, RED, 'left', text='− 5', sw=10), gap=6)
# solve: 4x = 20 → x = 5
math-6-one-step-equations-and-inequalities/solve = col(M('4x = 20', 90), arrow(50, dir='down'), M('x = 5', 90, color=BLUE), gap=4)
# substitute: an x tile swapped for a 5 tile
math-6-one-step-equations-and-inequalities/substitute = row(tile('x', BLUE, 110), curve_arrow(40, ORANGE), tile('5', ORANGE, 110), gap=10)
# ratio: 3 cat icons and 2 dog icons
math-6-ratios-and-rates/ratio = row(*[cat_icon(80) for _ in range(3)], Item(20, 10, ''), *[dog_icon(80) for _ in range(2)], gap=8)
# percent: a 10 by 10 grid with 40 squares shaded
math-6-ratios-and-rates/percent = grid_shade(10, 10, 40, 300, GREEN)
# double number line: two lined-up number lines with matching ticks
math-6-ratios-and-rates/double-number-line = col(numberline(0, 4, 440, labels=['0', '3', '6', '9', '12'], color=BLUE), numberline(0, 4, 440, labels=['0', '$2', '$4', '$6', '$8'], color=ORANGE), gap=10)
# equivalent ratios: a ratio table with 2:3, 4:6, 6:9
math-6-ratios-and-rates/equivalent-ratios = table(cells=[['A', 'B'], ['2', '3'], ['4', '6'], ['6', '9']], size=280)
# statistical question: a question with many different answers, shown as a dot plot
math-6-statistical-variability/statistical-question = col(bubble(T('How tall are we?', 32), 300, tail='left'), dotplot((48, 50, 51, 51, 52, 53, 53, 53, 55), 380), gap=8)
# variability: scattered dots on a number line
math-6-statistical-variability/variability = numberline(0, 10, 460, dots_={1: 1, 3: 2, 4: 1, 6: 1, 8: 2, 9: 1}, color=BLUE)
# distribution: a histogram with a long right tail
math-6-statistical-variability/distribution = histogram((3, 8, 6, 4, 2, 1, 1), 320)
# measure of center: a number line with a center arrow
math-6-statistical-variability/measure-of-center = numberline(0, 10, 460, dots_={3: 1, 4: 2, 5: 3, 6: 2, 7: 1}, hl=5, color=BLUE) if 0 else col(arrow(60, RED, 'down', sw=10), numberline(0, 10, 460, dots_={3: 1, 4: 2, 5: 3, 6: 2, 7: 1}, color=BLUE), gap=-10)
# range: a dot plot with a bracket from the least to the greatest value: range = 8 − 2 = 6
math-6-statistical-variability/range = col(dotplot((2, 3, 3, 4, 4, 4, 5, 6, 8), 400, bracket=True), M('range = 8 − 2 = 6', 50), gap=10)
# cluster: dots bunched on a number line
math-6-statistical-variability/cluster = dotplot((1, 5, 5, 5, 6, 6, 6, 6, 7, 7, 10), 400)
# mean: three bars leveled to equal height
math-6-summarizing-data/mean = row(blocks_stack((2, 5, 2), 220, colors=[BLUE, ORANGE, GREEN]), arrow(60), blocks_stack((3, 3, 3), 220, colors=[BLUE, ORANGE, GREEN]), gap=12)
# median: three ordered numbers with the middle circled
math-6-summarizing-data/median = row(T('3', 90), mark(T('7', 90), 'circle', RED), T('12', 90), gap=30)
# mean absolute deviation: dots with distance bars to a center line
math-6-summarizing-data/mean-absolute-deviation = dotplot((1, 3, 4, 5, 6, 7, 9), 400, center=5, dev=True)
# histogram: touching bars of different heights
math-6-summarizing-data/histogram = histogram((2, 5, 8, 6, 3, 1), 320)
# box plot: a box with whiskers
math-6-summarizing-data/box-plot = boxplot(400)
# interquartile range: a box plot with the box bracketed
math-6-summarizing-data/interquartile-range = boxplot(400, bracket=True)
# circumference: a circle with its edge traced
math-7-circles-angles-area-and-volume/circumference = circle_parts(300, trace=True)
# radius: a circle with a radius line
math-7-circles-angles-area-and-volume/radius = circle_parts(300, radius=True)
# diameter: a circle with a diameter line
math-7-circles-angles-area-and-volume/diameter = circle_parts(300, diameter=True)
# pi: the symbol π
math-7-circles-angles-area-and-volume/pi = M('π', 260, color=BLUE)
# supplementary angles: two angles forming a straight line
math-7-circles-angles-area-and-volume/supplementary-angles = raw(400, 200, '<line x1="10" y1="170" x2="390" y2="170" stroke="#1f2430" stroke-width="8" stroke-linecap="round"/><line x1="200" y1="170" x2="290" y2="20" stroke="#1f2430" stroke-width="8" stroke-linecap="round"/><path d="M270 170 A70 70 0 0 0 236 110" fill="none" stroke="#f08a24" stroke-width="8"/><path d="M221 136 A40 40 0 0 0 160 170" fill="none" stroke="#3a7bd5" stroke-width="8"/><circle cx="200" cy="170" r="7" fill="#1f2430"/>')
# vertical angles: two crossing lines with opposite angles marked
math-7-circles-angles-area-and-volume/vertical-angles = raw(360, 280, '<line x1="20" y1="40" x2="340" y2="240" stroke="#1f2430" stroke-width="8" stroke-linecap="round"/><line x1="20" y1="240" x2="340" y2="40" stroke="#1f2430" stroke-width="8" stroke-linecap="round"/><path d="M137.6 113.5 A50 50 0 0 0 137.6 166.5" fill="none" stroke="#f08a24" stroke-width="9"/><path d="M222.4 113.5 A50 50 0 0 1 222.4 166.5" fill="none" stroke="#f08a24" stroke-width="9"/><path d="M149.5 120.9 A36 36 0 0 1 210.5 120.9" fill="none" stroke="#3a7bd5" stroke-width="9"/><path d="M149.5 159.1 A36 36 0 0 0 210.5 159.1" fill="none" stroke="#3a7bd5" stroke-width="9"/>')
# equivalent expressions: 2(x + 3) = 2x + 6
math-7-equivalent-expressions/equivalent-expressions = M('2(x + 3) = 2x + 6', 70)
# factor: 6x + 9 = 3(2x + 3)
math-7-equivalent-expressions/factor = M('6x + 9 = 3(2x + 3)', 66, hl={'3(': ORANGE})
# expand: 4(x − 2) = 4x − 8
math-7-equivalent-expressions/expand = M('4(x − 2) = 4x − 8', 70)
# combine like terms: 3x + 2x = 5x
math-7-equivalent-expressions/combine-like-terms = row(box(M('3x', 70), color=BLUE, p=12), M('+', 70), box(M('2x', 70), color=BLUE, p=12), M('=', 70), box(M('5x', 70), color=GREEN, p=12), gap=10)
# commutative property: a + b = b + a
math-7-equivalent-expressions/commutative-property = M('a + b = b + a', 100)
# associative property: (a + b) + c = a + (b + c)
math-7-equivalent-expressions/associative-property = M('(a + b) + c = a + (b + c)', 52)
# multi-step equation: 3x + 4 = 19 with two arrows
math-7-multi-step-equations-and-inequalities/multi-step-equation = col(M('3x + 4 = 19', 80), arrow(40, RED, 'down', text='− 4'), M('3x = 15', 80), arrow(40, RED, 'down', text='÷ 3'), M('x = 5', 80, color=BLUE), gap=2)
# isolate: x alone on one pan of a balance
math-7-multi-step-equations-and-inequalities/isolate = col(row(box(M('x', 60), color=BLUE, p=14), box(M('5', 60), color=ORANGE, p=14), gap=150), scale_icon(340), gap=-60)
# inequality: a number line with an open dot at 5
math-7-multi-step-equations-and-inequalities/inequality = numberline(0, 10, 460, open_=5, ray='right', color=BLUE)
# flip the sign: < turning into >
math-7-multi-step-equations-and-inequalities/flip-the-sign = row(M('<', 160, color=BLUE), curve_arrow(50, ORANGE), M('>', 160, color=RED), gap=20)
# solution set: a shaded ray left of 5
math-7-multi-step-equations-and-inequalities/solution-set = numberline(0, 10, 460, closed=5, ray='left', color=BLUE)
# check: a check mark beside an equation
math-7-multi-step-equations-and-inequalities/check = row(M('2(5) + 1 = 11', 70), check(100), gap=16)
# additive inverse: 6 and −6 summing to 0
math-7-operations-with-rational-numbers/additive-inverse = M('6 + (−6) = 0', 84)
# signed number: + and − tiles
math-7-operations-with-rational-numbers/signed-number = row(tile('+', YELLOW, 110), tile('−', RED, 110), gap=20)
# zero pair: a +1 and −1 tile side by side
math-7-operations-with-rational-numbers/zero-pair = row(tile('+1', YELLOW, 120), tile('−1', RED, 120), gap=10)
# product of negatives: (−3)(−4) = 12
math-7-operations-with-rational-numbers/product-of-negatives = row(M('(−3)(−4) = 12', 72), Item(50, 10, ''), gap=0)
# repeating decimal: 0.3 with a bar over the 3
math-7-operations-with-rational-numbers/repeating-decimal = raw(320, 200, '<text x="160" y="160" font-family="Cambria Math" font-size="130" font-weight="700" text-anchor="middle" fill="#1f2430">0.3</text><line x1="168" y1="48" x2="226" y2="48" stroke="#e04848" stroke-width="10" stroke-linecap="round"/>')
# terminating decimal: 0.25
math-7-operations-with-rational-numbers/terminating-decimal = M('0.25', 180)
# sample space: six die faces
math-7-probability/sample-space = grid([dice(i, 90) for i in range(1, 7)], 3, gap=16)
# tree diagram: a branching tree of options
math-7-probability/tree-diagram = tree_diagram(340, (2, 2))
# proportional relationship: a straight line through the origin
math-7-proportional-relationships/proportional-relationship = plot(lambda x: 0.8 * x, size=320, xr=(0, 8), yr=(0, 8), grid_=True, points=[(0, 0, RED)])
# constant of proportionality: y = 4x with 4 highlighted
math-7-proportional-relationships/constant-of-proportionality = M('y = 4x', 140, hl={'4': RED})
# proportion: 3/5 = x/20
math-7-proportional-relationships/proportion = eq(('3', '5'), '=', ('x', '20'), size=110)
# percent increase: an arrow up with 20%
math-7-proportional-relationships/percent-increase = row(bars([5, 6], size=200, colors=[BLUE, ORANGE]), col(T('20%', 60, GREEN), arrow(90, GREEN, 'up', sw=12), gap=4), gap=10)
# population: a large grid of dots
math-7-sampling-and-inference/population = dots(80, 10, 22, BLUE, gap=8)
# sample: a grid of dots with 50 circled
math-7-sampling-and-inference/sample = over(dots(80, 10, 22, BLUE, gap=8), raw(180, 180, '<ellipse cx="90" cy="90" rx="84" ry="84" fill="none" stroke="#e04848" stroke-width="7"/>'), dx=40, dy=40)
# variation: several dot plots slightly different
math-7-sampling-and-inference/variation = col(dotplot((3, 4, 4, 5, 5, 6), 340), dotplot((3, 4, 5, 5, 6, 6), 340, color=ORANGE), dotplot((2, 4, 4, 5, 5, 7), 340, color=GREEN), gap=6)
# scale drawing: a floor plan with a scale bar
math-7-scale-drawings-and-constructions/scale-drawing = col(raw(360, 240, '<rect x="10" y="10" width="340" height="220" fill="#fff" stroke="#1f2430" stroke-width="7"/><path d="M180 10 V130 M180 170 V230 M10 120 H120 M150 120 H180" stroke="#1f2430" stroke-width="6"/><text x="90" y="70" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#3a7bd5">bedroom</text><text x="270" y="130" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#f08a24">kitchen</text>'), scale_bar(300, ('0', '5', '10 ft')), gap=12)
# scale factor: a small and a double-size triangle
math-7-scale-drawings-and-constructions/scale-factor = raw(400, 220, '<path d="M10 200 H90 V140 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M230 200 H390 V80 Z" fill="#fde3c8" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M110 170 H190" stroke="#f08a24" stroke-width="8"/><path d="M210 170 l-22 -12 v24 z" fill="#f08a24"/><text x="150" y="150" font-family="Cambria Math" font-size="40" font-weight="700" text-anchor="middle" fill="#f08a24">× 2</text>')
# cross section: a cylinder sliced to show a circle
math-7-scale-drawings-and-constructions/cross-section = solid('cylinder', 300, BLUE, slice_=True)
# triangle inequality: three sticks that cannot close
math-7-scale-drawings-and-constructions/triangle-inequality = raw(380, 220, '<line x1="40" y1="190" x2="340" y2="190" stroke="#2f9e5b" stroke-width="14" stroke-linecap="round"/><line x1="40" y1="190" x2="100" y2="110" stroke="#3a7bd5" stroke-width="14" stroke-linecap="round"/><line x1="340" y1="190" x2="290" y2="120" stroke="#f08a24" stroke-width="14" stroke-linecap="round"/><path d="M110 95 L280 105" stroke="#e04848" stroke-width="5" stroke-dasharray="10 9"/><text x="195" y="80" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#e04848">?</text>')
# scale: a map scale bar
math-7-scale-drawings-and-constructions/scale = scale_bar(420, ('0', '1', '2', '3 km'))
# scatter plot: scattered dots trending up
math-8-bivariate-data/scatter-plot = scatter(16, 1.0, 0.8, 320)
# line of fit: a straight line through scattered dots
math-8-bivariate-data/line-of-fit = scatter(16, 1.0, 0.8, 320, line=True)
# association: dots rising left to right
math-8-bivariate-data/association = scatter(16, 1.0, 0.5, 320, seed=5)
# two-way table: a 2 by 2 table with counts
math-8-bivariate-data/two-way-table = table(cells=[['', 'yes', 'no'], ['A', '12', '8'], ['B', '5', '15']], size=330)
# relative frequency: a pie with 60% shaded
math-8-bivariate-data/relative-frequency = col(pie(0.6, 260, GREEN), T('60%', 60, GREEN), gap=8)
# function: an input-output machine
math-8-defining-functions/function = machine(380, 'in', 'out', 'f')
# input: 3 entering a machine
math-8-defining-functions/input = machine(380, '3', None, 'f')
# output: 9 leaving a machine
math-8-defining-functions/output = machine(380, None, '9', 'f')
# linear function: a straight line
math-8-defining-functions/linear-function = plot(lambda x: 0.7 * x + 1, size=320)
# nonlinear function: a curved parabola
math-8-defining-functions/nonlinear-function = plot(lambda x: 0.4 * x * x - 3, size=320)
# vertical line test: a circle crossed by a vertical line at two points
math-8-defining-functions/vertical-line-test = plot(size=320, curves=[([3 * math.cos(t / 20 * math.pi) for t in range(41)], [3 * math.sin(t / 20 * math.pi) for t in range(41)])], vlines=[1.5], points=[(1.5, 2.6, RED), (1.5, -2.6, RED)])
# scientific notation: 3 × 10⁶
math-8-exponents-roots-and-scientific-notation/scientific-notation = M('3 × 10⁶', 140)
# cube root: a 3 by 3 by 3 cube of 27 blocks: the cube root of 27 is 3
math-8-exponents-roots-and-scientific-notation/cube-root = col(solid('cube', 260, BLUE, units=(3, 3, 3)), M('∛27 = 3', 64), gap=8)
# negative exponent: 10⁻² = 1/100
math-8-exponents-roots-and-scientific-notation/negative-exponent = row(M('10⁻² =', 90), F('1', '100', 90), gap=16)
# zero exponent: 5⁰ = 1
math-8-exponents-roots-and-scientific-notation/zero-exponent = M('5⁰ = 1', 150)
# perfect square: a 6 by 6 square
math-8-exponents-roots-and-scientific-notation/perfect-square = grid_shade(6, 6, 36, 300, BLUE)
# power: 2³ = 8
math-8-exponents-roots-and-scientific-notation/power = M('2³ = 8', 150)
# irrational number: √2 on a number line between 1 and 2
math-8-irrational-numbers/irrational-number = numberline(0, 3, 440, marks={1.41: RED}, labels=['0', '1', '2', '3']) if 0 else col(T('√2', 60, RED), numberline(0, 30, 440, every=10, labels=[str(i // 10) if i % 10 == 0 else '' for i in range(31)], marks={14: RED}, color=BLUE), gap=0)
# rational approximation: a zoomed number line near 1.41
math-8-irrational-numbers/rational-approximation = col(T('√2 ≈ 1.414', 56, RED), numberline(0, 10, 440, labels=['1.40', '', '', '', '', '1.41', '', '', '', '', '1.42'], marks={4: RED}, color=BLUE), gap=4)
# real numbers: a continuous number line
math-8-irrational-numbers/real-numbers = numberline(-5, 5, 460, seg=(-5, 5), color=BLUE)
# non-repeating decimal: 3.14159... trailing off
math-8-irrational-numbers/non-repeating-decimal = raw(440, 160, '<text x="10" y="110" font-family="Cambria Math" font-size="96" font-weight="700" fill="#1f2430">3.14159</text><text x="340" y="110" font-family="Cambria Math" font-size="96" font-weight="700" fill="#8a8f9c">...</text>')
# square root: a 7 by 7 square of 49 units
math-8-irrational-numbers/square-root = col(grid_shade(7, 7, 49, 280, BLUE), M('√49 = 7', 60), gap=6)
# estimate: √50 between 7 and 8 on a number line
math-8-irrational-numbers/estimate = col(T('√50', 60, RED), numberline(6, 9, 440, marks={7.07: RED}, color=BLUE), gap=0)
# linear equation: a straight line on a grid
math-8-linear-equations-and-systems/linear-equation = plot(lambda x: 0.7 * x + 1, size=320, grid_=True)
# system of equations: two lines crossing
math-8-linear-equations-and-systems/system-of-equations = plot(lambda x: 0.8 * x + 1, lambda x: -x + 2, size=320, grid_=True)
# point of intersection: two lines crossing with a dot
math-8-linear-equations-and-systems/point-of-intersection = plot(lambda x: 0.8 * x + 1, lambda x: -x + 2, size=320, grid_=True, points=[(0.56, 1.44, RED)])
# substitution: an expression sliding into a variable slot
math-8-linear-equations-and-systems/substitution = col(M('y = 2x', 70), row(M('x + ', 70), box(M('2x', 60), color=ORANGE, p=8, dashed=True), M(' = 9', 70), gap=4), gap=20)
# elimination: two stacked equations with y-terms canceling
math-8-linear-equations-and-systems/elimination = col(M(' 2x + y = 7', 70), M('+ x − y = 2', 70), raw(380, 8, '<rect width="380" height="8" fill="#1f2430"/>'), M('3x       = 9', 70, color=BLUE), gap=4, align='r')
# no solution: two parallel lines
math-8-linear-equations-and-systems/no-solution = plot(lambda x: 0.7 * x + 2, lambda x: 0.7 * x - 2, size=320, grid_=True)
# rate of change: a slope triangle
math-8-modeling-with-functions/rate-of-change = plot(lambda x: 0.75 * x, size=320, xr=(0, 8), yr=(0, 8), grid_=True, tri=((2, 1.5), (6, 4.5)))
# increasing: a line going up
math-8-modeling-with-functions/increasing = plot(lambda x: 0.7 * x, size=320, colors=(GREEN,), sw=9)
# decreasing: a line going down
math-8-modeling-with-functions/decreasing = plot(lambda x: -0.7 * x, size=320, colors=(RED,), sw=9)
# qualitative graph: an unlabeled curve going up and down
math-8-modeling-with-functions/qualitative-graph = plot(lambda x: 2 * math.sin(x * 1.1) + 0.3 * x, size=320, axes=True, ticks=False)
# slope: a line with a rise-run triangle
math-8-slope-and-proportional-relationships/slope = plot(lambda x: 0.75 * x, size=320, xr=(0, 8), yr=(0, 8), grid_=True, tri=((2, 1.5), (6, 4.5)))
# rise: a vertical arrow on a grid
math-8-slope-and-proportional-relationships/rise = plot(size=320, xr=(0, 8), yr=(0, 8), grid_=True, arrows_=[(4, 1, 4, 7, RED)])
# run: a horizontal arrow on a grid
math-8-slope-and-proportional-relationships/run = plot(size=320, xr=(0, 8), yr=(0, 8), grid_=True, arrows_=[(1, 4, 7, 4, BLUE)])
# similar triangles: two right triangles along a line
math-8-slope-and-proportional-relationships/similar-triangles = plot(lambda x: 0.75 * x, size=320, xr=(0, 8), yr=(0, 8), grid_=True, segs=[((2, 1.5), (4, 1.5), ORANGE, False), ((4, 1.5), (4, 3), ORANGE, False), ((4, 3), (8, 3), GREEN, False), ((8, 3), (8, 6), GREEN, False)])
# y-intercept: a line crossing the y-axis at 4
math-8-slope-and-proportional-relationships/y-intercept = plot(lambda x: 0.5 * x + 4, size=320, xr=(-2, 8), yr=(-2, 8), grid_=True, points=[(0, 4, RED)])
# unit rate: a step of 1 right and up the slope
math-8-slope-and-proportional-relationships/unit-rate = plot(lambda x: 0.75 * x, size=320, xr=(0, 8), yr=(0, 8), grid_=True, segs=[((4, 3), (5, 3), RED, False), ((5, 3), (5, 3.75), RED, False)], texts=[(4.5, 2.4, '1', RED)])
# hypotenuse: a right triangle with its longest side bold
math-8-the-pythagorean-theorem/hypotenuse = triangle(320, pts=((30, 150), (190, 150), (30, 20)), right_at=0, hl_side=1)
# leg: a right triangle with legs marked
math-8-the-pythagorean-theorem/leg = triangle(320, pts=((30, 150), (190, 150), (30, 20)), right_at=0, hl_side=[0, 2])
# right triangle: a right triangle
math-8-the-pythagorean-theorem/right-triangle = triangle(320, pts=((10, 150), (190, 150), (10, 20)), right_at=0, fill=soft(BLUE))
# converse: a 5-12-13 triangle: since 5² + 12² = 13², it must be a right triangle
math-8-the-pythagorean-theorem/converse = col(triangle(300, pts=((10, 150), (190, 150), (10, 75)), sides=['12', '13', '5'], fill=soft(GREEN), right_at=0), Item(10, 14, ''), M('5² + 12² = 13²', 44), T('so it is a right triangle', 30, GREEN), gap=6)
# distance: two points with a slanted segment
math-8-the-pythagorean-theorem/distance = plot(size=320, xr=(0, 8), yr=(0, 8), grid_=True, segs=[((1, 1), (7, 6), RED, False)], points=[(1, 1, BLUE), (7, 6, BLUE)])
# transformation: a shape and its moved copy
math-8-transformations/transformation = plot(size=320, xr=(0, 10), yr=(0, 10), grid_=True, curves=[([1, 4, 1, 1], [1, 1, 4, 1]), ([5, 8, 5, 5], [5, 5, 8, 5])], arrows_=[(3, 3, 5.5, 5.5, ORANGE)])
# translation: a triangle sliding right
math-8-transformations/translation = plot(size=320, xr=(0, 10), yr=(0, 10), grid_=True, curves=[([1, 4, 1, 1], [3, 3, 6, 3]), ([6, 9, 6, 6], [3, 3, 6, 3])], arrows_=[(3.5, 4.5, 6, 4.5, ORANGE)])
# reflection: a shape mirrored across a line
math-8-transformations/reflection = plot(size=320, xr=(-5, 5), yr=(-5, 5), grid_=True, curves=[([-4, -1, -4, -4], [-2, -2, 3, -2]), ([4, 1, 4, 4], [-2, -2, 3, -2])], vlines=[0])
# rotation: a flag turned 90 degrees around a fixed point
math-8-transformations/rotation = raw(300, 290, '<g opacity="0.35"><line x1="110" y1="200" x2="110" y2="90" stroke="#1f2430" stroke-width="7" stroke-linecap="round"/><path d="M113 94 H170 L156 112 L170 130 H113 Z" fill="#e04848" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/></g><g transform="rotate(90 110 200)"><line x1="110" y1="200" x2="110" y2="90" stroke="#1f2430" stroke-width="7" stroke-linecap="round"/><path d="M113 94 H170 L156 112 L170 130 H113 Z" fill="#e04848" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/></g><path d="M110 64 A136 136 0 0 1 240 186" fill="none" stroke="#f08a24" stroke-width="6"/><path d="M246 204 l-16 -18 h22 z" fill="#f08a24"/><text x="226" y="84" font-family="Cambria Math" font-size="34" font-weight="700" fill="#f08a24">90°</text><circle cx="110" cy="200" r="10" fill="#1f2430"/>')
# dilation: a small and a large square
math-8-transformations/dilation = row(shape('square', 90, ORANGE), arrow(60), shape('square', 210, ORANGE), gap=10, align='b')
# congruent: two identical triangles
math-8-transformations/congruent = row(triangle(180, pts=((10, 150), (190, 150), (70, 20)), fill=soft(BLUE), ticks=[1, 2, 3]), triangle(180, pts=((10, 150), (190, 150), (70, 20)), fill=soft(BLUE), ticks=[1, 2, 3]), gap=20)
# volume: a cylinder with r and h labeled
math-8-volume-of-cylinders-cones-and-spheres/volume = solid('cylinder', 300, BLUE, labels=('r', 'h'))
# one-third: a cone inside a cylinder of equal size
math-8-volume-of-cylinders-cones-and-spheres/one-third = over(solid('cylinder', 300, BLUE), raw(300, 300, '<path d="M150 50 L60 250 A90 30 0 0 0 240 250 Z" fill="#f08a24" fill-opacity="0.6" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), dx=0, dy=0)
# cubic units: a unit cube
math-8-volume-of-cylinders-cones-and-spheres/cubic-units = solid('cube', 220, GREEN)
# constraint: a shaded region under a line
math-9-creating-equations/constraint = plot(lambda x: 0.6 * x + 1, size=320, grid_=True, shade=None, fill_between=(lambda x: -5, lambda x: 0.6 * x + 1, -5, 5))
# literal equation: d = rt → t = d/r
math-9-creating-equations/literal-equation = col(M('d = rt', 90), arrow(50, dir='down'), M('t = d/r', 90, color=BLUE), gap=4)
# formula: A = lw beside a rectangle
math-9-creating-equations/formula = row(M('A = lw', 80), raw(220, 170, '<rect x="10" y="10" width="150" height="100" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/><text x="85" y="160" font-family="Cambria Math" font-size="56" font-weight="700" text-anchor="middle" fill="#e04848">l</text><text x="172" y="76" font-family="Cambria Math" font-size="56" font-weight="700" fill="#e04848">w</text>'), gap=20)
# define a variable: n = hours
math-9-creating-equations/define-a-variable = row(M('n', 120, color=BLUE), M('=', 100), T('hours', 70, ORANGE), gap=24)
# correlation: dots tightly rising
math-9-data-in-one-and-two-variables/correlation = scatter(16, 1.0, 0.2, 320, tight=True)
# correlation coefficient: r = 0.92
math-9-data-in-one-and-two-variables/correlation-coefficient = M('r = 0.92', 130)
# residual: a dot with a vertical gap to a line
math-9-data-in-one-and-two-variables/residual = plot(lambda x: 0.8 * x + 1, size=320, xr=(0, 8), yr=(0, 8), colors=(ORANGE,), points=[(1, 2.3, BLUE), (2, 2.2, BLUE), (4, 4.6, BLUE), (5, 4.5, BLUE), (6, 6.2, BLUE), (3, 6, RED)], segs=[((3, 6), (3, 3.4), RED, True)])
# causation: an arrow from one box to another
math-9-data-in-one-and-two-variables/causation = row(box(T('A', 70), color=BLUE, w=120, h=120), arrow(110, RED, sw=12), box(T('B', 70), color=ORANGE, w=120, h=120), gap=10)
# standard deviation: a bell curve with spread marked
math-9-data-in-one-and-two-variables/standard-deviation = plot(bell(0, 1.2), size=320, xr=(-4, 4), yr=(-0.3, 5), axes=False, vlines=[0], segs=[((-1.2, 2.55), (1.2, 2.55), RED, False)], points=[(-1.2, 2.55, RED), (1.2, 2.55, RED)])
# skewed: a histogram with a long right tail
math-9-data-in-one-and-two-variables/skewed = histogram((3, 8, 6, 4, 2, 1, 1), 320)
# function notation: f(3) = 7
math-9-function-notation-and-graphs/function-notation = M('f(3) = 7', 140)
# domain: a horizontal axis fully shaded
math-9-function-notation-and-graphs/domain = plot(size=320, segs=[((-5, 0), (5, 0), RED, False)], sw=12) if 0 else raw(400, 200, '<line x1="20" y1="100" x2="380" y2="100" stroke="#1f2430" stroke-width="5"/><line x1="200" y1="10" x2="200" y2="190" stroke="#1f2430" stroke-width="5"/><rect x="20" y="88" width="360" height="24" rx="12" fill="#3a7bd5" fill-opacity="0.6"/>')
# range: a vertical axis shaded above 0
math-9-function-notation-and-graphs/range = raw(240, 340, '<line x1="20" y1="300" x2="220" y2="300" stroke="#1f2430" stroke-width="5"/><line x1="120" y1="10" x2="120" y2="330" stroke="#1f2430" stroke-width="5"/><rect x="108" y="10" width="24" height="290" rx="12" fill="#f08a24" fill-opacity="0.7"/>')
# x-intercept: a line crossing the x-axis
math-9-function-notation-and-graphs/x-intercept = plot(lambda x: 0.8 * x + 2, size=320, grid_=True, points=[(-2.5, 0, RED)])
# average rate of change: a curve with a secant line
math-9-function-notation-and-graphs/average-rate-of-change = plot(lambda x: 0.15 * x ** 3 - x + 1, size=320, segs=[((-2, 1.8), (3, 2.05), RED, False)], points=[(-2, 1.8, RED), (3, 2.05, RED)])
# maximum: a downward parabola with its peak marked
math-9-function-notation-and-graphs/maximum = plot(lambda x: -0.5 * x * x + 3, size=320, points=[(0, 3, RED)])
# exponential growth: a curve rising faster and faster
math-9-linear-quadratic-and-exponential-models/exponential-growth = plot(lambda x: 0.2 * 2 ** x, size=320, xr=(-1, 6), yr=(-1, 7), colors=(GREEN,))
# exponential decay: a curve dropping and leveling
math-9-linear-quadratic-and-exponential-models/exponential-decay = plot(lambda x: 6 * 0.5 ** x, size=320, xr=(-1, 6), yr=(-1, 7), colors=(RED,))
# growth factor: ×1.05 arrows between bars
math-9-linear-quadratic-and-exponential-models/growth-factor = col(bars([10, 10.5, 11.0, 11.6], size=300, colors=[GREEN] * 4), T('× 1.05 each step', 40, ORANGE), gap=8)
# quadratic function: a parabola
math-9-linear-quadratic-and-exponential-models/quadratic-function = plot(lambda x: 0.5 * x * x - 2, size=320)
# vertical shift: two copies of a curve stacked
math-9-linear-quadratic-and-exponential-models/vertical-shift = plot(lambda x: 0.4 * x * x - 3, lambda x: 0.4 * x * x, size=320, arrows_=[(0, -2.6, 0, -0.4, ORANGE)])
# parent function: a basic parabola through the origin
math-9-linear-quadratic-and-exponential-models/parent-function = plot(lambda x: x * x, size=320, points=[(0, 0, RED)])
# polynomial: 3x² + 2x − 1
math-9-polynomial-arithmetic/polynomial = M('3x² + 2x − 1', 110)
# degree: x³ + x with 3 highlighted
math-9-polynomial-arithmetic/degree = M('x³ + x', 150, hl={'³': RED})
# binomial: x + 5
math-9-polynomial-arithmetic/binomial = row(box(M('x', 90), color=BLUE, p=14), M('+', 90), box(M('5', 90), color=ORANGE, p=14), gap=12)
# trinomial: x² + 5x + 6
math-9-polynomial-arithmetic/trinomial = row(box(M('x²', 70), color=BLUE, p=10), M('+', 70), box(M('5x', 70), color=ORANGE, p=10), M('+', 70), box(M('6', 70), color=GREEN, p=10), gap=8)
# leading coefficient: 4x² − x with 4 highlighted
math-9-polynomial-arithmetic/leading-coefficient = M('4x² − x', 140, hl={'4': RED})
# standard form: x² − 3x + 2
math-9-polynomial-arithmetic/standard-form = M('x² − 3x + 2', 120)
# quadratic formula: the quadratic formula
math-9-quadratic-equations/quadratic-formula = raw(460, 200, '<text x="10" y="120" font-family="Cambria Math" font-size="52" font-weight="700" fill="#1f2430">x =</text><text x="290" y="88" font-family="Cambria Math" font-size="42" font-weight="700" text-anchor="middle" fill="#1f2430">−b ± √(b² − 4ac)</text><line x1="115" y1="106" x2="455" y2="106" stroke="#1f2430" stroke-width="5"/><text x="290" y="160" font-family="Cambria Math" font-size="46" font-weight="700" text-anchor="middle" fill="#1f2430">2a</text>')
# discriminant: b² − 4ac boxed
math-9-quadratic-equations/discriminant = box(M('b² − 4ac', 110), color=RED, p=20)
# zero: a parabola crossing at −2 and 2
math-9-quadratic-equations/zero = plot(lambda x: 0.5 * x * x - 2, size=320, points=[(-2, 0, RED), (2, 0, RED)])
# root: a parabola crossing the x-axis at its two roots
math-9-quadratic-equations/root = plot(lambda x: 0.5 * (x + 3) * (x - 2), size=320, points=[(-3, 0, RED), (2, 0, RED)])
# zero product property: (x − 2)(x + 5) = 0
math-9-quadratic-equations/zero-product-property = M('(x − 2)(x + 5) = 0', 70)
# vertex: a parabola with its lowest point marked
math-9-quadratic-equations/vertex = plot(lambda x: 0.5 * (x - 1) ** 2 - 3, size=320, points=[(1, -3, RED)])
# rational exponent: x^(1/2) = √x
math-9-rational-exponents-and-real-numbers/rational-exponent = row(M('x', 120), M('½', 60, color=RED), Item(30, 10, ''), M('=', 110), M('√x', 120), gap=10, align='t')
# radical: the root symbol over 18
math-9-rational-exponents-and-real-numbers/radical = raw(300, 200, '<path d="M20 110 L50 100 L80 180 L120 20 H290" fill="none" stroke="#1f2430" stroke-width="10" stroke-linejoin="round"/><text x="205" y="160" font-family="Cambria Math" font-size="110" font-weight="700" text-anchor="middle" fill="#1f2430">18</text>')
# index: a cube root with 3 highlighted
math-9-rational-exponents-and-real-numbers/index = raw(300, 200, '<text x="30" y="90" font-family="Cambria Math" font-size="60" font-weight="700" fill="#e04848">3</text><path d="M20 110 L50 100 L80 180 L120 20 H290" fill="none" stroke="#1f2430" stroke-width="10" stroke-linejoin="round"/><text x="205" y="160" font-family="Cambria Math" font-size="110" font-weight="700" text-anchor="middle" fill="#1f2430">27</text>')
# closure: adding two whole numbers always gives a whole number: 2 + 3 = 5 stays inside
math-9-rational-exponents-and-real-numbers/closure = over(raw(300, 300, '<circle cx="150" cy="150" r="130" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="8"/><text x="150" y="82" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#3a7bd5">whole numbers</text>'), M('2 + 3 = 5', 56))
# simplify: √50 = 5√2
math-9-rational-exponents-and-real-numbers/simplify = M('√50 = 5√2', 120)
# irrational: √3 on a number line
math-9-rational-exponents-and-real-numbers/irrational = col(T('√3', 60, RED), numberline(0, 30, 440, every=10, labels=[str(i // 10) if i % 10 == 0 else '' for i in range(31)], marks={17: RED}, color=BLUE), gap=0)
# linear equation: 3x − 7 = 11
math-9-solving-linear-equations-and-inequalities/linear-equation = M('3x − 7 = 11', 110)
# compound inequality: a number line segment from −2 to 5
math-9-solving-linear-equations-and-inequalities/compound-inequality = numberline(-4, 7, 460, seg=(-2, 5), closed=-2, open_=5, color=BLUE)
# identity: a fully shaded number line
math-9-solving-linear-equations-and-inequalities/identity = numberline(-5, 5, 460, seg=(-5, 5), color=BLUE)
# extraneous solution: a crossed-out x value
math-9-solving-linear-equations-and-inequalities/extraneous-solution = row(M('x = 4', 110), cross(90), gap=16)
# interval notation: [3, ∞) beside a shaded ray
math-9-solving-linear-equations-and-inequalities/interval-notation = col(M('[3, ∞)', 90), numberline(0, 10, 440, closed=3, ray='right', color=BLUE), gap=10)
# properties of equality: a balance with equal changes on both pans
math-9-solving-linear-equations-and-inequalities/properties-of-equality = col(row(box(col(M('x + 2', 44), T('− 2', 34, RED), gap=0), color=BLUE, p=10), box(col(M('5', 44), T('− 2', 34, RED), gap=0), color=ORANGE, p=10), gap=110), scale_icon(340), gap=-60)
# factoring: x² − 9 = (x + 3)(x − 3)
math-9-structure-of-expressions/factoring = M('x² − 9 = (x + 3)(x − 3)', 54)
# completing the square: an x-by-x square with strips and a missing corner
math-9-structure-of-expressions/completing-the-square = raw(320, 320, '<rect x="20" y="20" width="200" height="200" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><rect x="220" y="20" width="80" height="200" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><rect x="20" y="220" width="200" height="80" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><rect x="220" y="220" width="80" height="80" fill="#fff" stroke="#e04848" stroke-width="5" stroke-dasharray="10 7"/><text x="120" y="135" font-family="Cambria Math" font-size="56" font-weight="700" text-anchor="middle" fill="#fff">x²</text><text x="260" y="275" font-family="Segoe UI" font-size="56" font-weight="700" text-anchor="middle" fill="#e04848">?</text>')
# difference of squares: a big square minus a small square
math-9-structure-of-expressions/difference-of-squares = raw(320, 320, '<rect x="20" y="20" width="280" height="280" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><rect x="200" y="200" width="100" height="100" fill="#fff" stroke="#e04848" stroke-width="6" stroke-dasharray="12 8"/><text x="110" y="170" font-family="Cambria Math" font-size="70" font-weight="700" text-anchor="middle" fill="#fff">a²</text><text x="250" y="266" font-family="Cambria Math" font-size="50" font-weight="700" text-anchor="middle" fill="#e04848">b²</text>')
# vertex form: a parabola with its vertex marked
math-9-structure-of-expressions/vertex-form = col(M('y = (x − 1)² − 3', 50), plot(lambda x: 0.5 * (x - 1) ** 2 - 3, size=280, points=[(1, -3, RED)]), gap=6)
# greatest common factor: 8x² + 12x = 4x(2x + 3)
math-9-structure-of-expressions/greatest-common-factor = M('8x² + 12x = 4x(2x + 3)', 52, hl={'4x': RED})
# equivalent form: two expressions joined by =
math-9-structure-of-expressions/equivalent-form = row(box(M('2(x + 1)', 60), color=BLUE, p=12), M('=', 70), box(M('2x + 2', 60), color=ORANGE, p=12), gap=12)
# system: two crossing lines
math-9-systems-of-equations/system = plot(lambda x: 0.8 * x + 1, lambda x: -x + 2, size=320, grid_=True)
# substitution: an expression dropping into a slot
math-9-systems-of-equations/substitution = col(M('y = 2x', 70), row(M('x + ', 70), box(M('2x', 60), color=ORANGE, p=8, dashed=True), M(' = 9', 70), gap=4), gap=20)
# elimination: two equations stacked with y canceling
math-9-systems-of-equations/elimination = col(M(' 2x + y = 7', 70), M('+ x − y = 2', 70), raw(380, 8, '<rect width="380" height="8" fill="#1f2430"/>'), M('3x       = 9', 70, color=BLUE), gap=4, align='r')
# infinitely many solutions: two lines drawn on top of each other
math-9-systems-of-equations/infinitely-many-solutions = plot(lambda x: 0.7 * x + 1, lambda x: 0.7 * x + 1, size=320, grid_=True, colors=(BLUE, ORANGE), sw=10) if 0 else plot(lambda x: 0.7 * x + 1, size=320, grid_=True, colors=(BLUE,), sw=16, segs=[((-5, -2.5), (5, 4.5), ORANGE, True)])
# feasible region: two boundary lines; the region that meets both rules is shaded
math-9-systems-of-equations/feasible-region = plot(lambda x: -0.7 * x + 2, lambda x: 0.8 * x - 2, size=320, grid_=True, colors=(BLUE, ORANGE), regions=[([(-5, 5.5), (2.667, 0.133), (-5, -6)], GREEN, 0.3)], points=[(2.667, 0.133, RED)])
# consistent: two lines crossing
math-9-systems-of-equations/consistent = plot(lambda x: 0.8 * x + 1, lambda x: -x + 2, size=320, grid_=True, points=[(0.56, 1.44, RED)])
# unit conversion: a fraction chain canceling units
math-9-units-and-quantities/unit-conversion = row(M('60 min', 60), M('×', 60), F('1 h', '60 min', 56), M('= 1 h', 60), gap=10)
# dimensional analysis: units canceling diagonally
math-9-units-and-quantities/dimensional-analysis = raw(460, 200, '<text x="90" y="80" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">3 ft</text><line x1="20" y1="100" x2="160" y2="100" stroke="#1f2430" stroke-width="5"/><text x="90" y="160" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">1</text><text x="190" y="115" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">×</text><text x="300" y="80" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">12 in</text><line x1="220" y1="100" x2="380" y2="100" stroke="#1f2430" stroke-width="5"/><text x="300" y="160" font-family="Cambria Math" font-size="52" font-weight="700" text-anchor="middle" fill="#1f2430">1 ft</text><line x1="94" y1="44" x2="150" y2="70" stroke="#e04848" stroke-width="6"/><line x1="290" y1="130" x2="346" y2="156" stroke="#e04848" stroke-width="6"/>')
# quantity: 12 m/s
math-9-units-and-quantities/quantity = M('12 m/s', 150)
# side: a triangle with its sides highlighted
math-k-build-a-shape/side = triangle(300, hl_side=[0, 1, 2])
# corner: a square with dots on its corners
math-k-build-a-shape/corner = raw(280, 280, '<rect x="40" y="40" width="200" height="200" fill="#d6e6fb" stroke="#1f2430" stroke-width="7"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="18" fill="#e04848"/>' for x in (40, 240) for y in (40, 240)))
# flat: a circle drawn on a sheet of paper
math-k-build-a-shape/flat = raw(320, 280, '<path d="M30 30 H260 L290 60 V250 H30 Z" fill="#fff" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><circle cx="160" cy="145" r="80" fill="#3a7bd5"/>')
# build: a square with a triangle on top making a house
math-k-build-a-shape/build = paint('colorful building blocks being stacked into a small tower, one block mid-air about to land')
# curve: a curved line
math-k-build-a-shape/curve = raw(360, 200, '<path d="M20 150 C 100 -20, 200 260, 340 50" fill="none" stroke="#9b59d0" stroke-width="16" stroke-linecap="round"/>')
# count: ten dots counted 1 to 10
math-k-counting-to-100/count = row(*[col(dot(36, BLUE), T(str(i), 26), gap=4) for i in range(1, 11)], gap=6)
# number: the number 5 next to five stars
math-k-counting-to-100/number = row(M('5', 160), col(row(*[star(60) for _ in range(3)], gap=6), row(*[star(60) for _ in range(2)], gap=6), gap=6), gap=24)
# ones: single cubes in a row
math-k-counting-to-100/ones = objects(5, cube_icon, cols=5, size=60, gap=10, color=GREEN)
# tens: three rods of ten cubes
math-k-counting-to-100/tens = row(rod(10, 28), rod(10, 28), rod(10, 28), gap=24)
# hundred: a 10 by 10 grid of dots
math-k-counting-to-100/hundred = dots(100, 10, 22, BLUE, gap=6)
# next: a number line with 7 and an arrow to an empty box
math-k-counting-to-100/next = row(tile('5', BLUE, 90), tile('6', BLUE, 90), tile('7', RED, 90), arrow(60, ORANGE), tile('?', ORANGE, 90, dashed=True), gap=10)
# how many: a basket with 4 apples
math-k-how-many/how-many = basket(300, inner=row(*[apple(56) for _ in range(4)], gap=4))
# one-to-one: four toy bears with a dot over each one
math-k-how-many/one-to-one = row(*[col(dot(30, RED), bear(80), gap=6) for _ in range(4)], gap=14)
# total: 6 ducks in a row
math-k-how-many/total = objects(6, duck, cols=6, size=64, gap=8)
# last number: five blocks with the number 5 over the last one
math-k-how-many/last-number = col(row(Item(330, 10, ''), T('5', 70, RED), gap=0), row(*[tile('', (BLUE, ORANGE, GREEN, PURPLE, RED)[i], 66) for i in range(5)], gap=10), gap=6)
# ten frame: a ten frame with 7 dots
math-k-how-many/ten-frame = tenframe(7, 340)
# measure: a shoe with a row of cubes beside it
math-k-longer-heavier-bigger/measure = row(raw(220, 110, '<path d="M14 80 C14 40 50 30 80 34 C110 38 120 56 160 60 C200 64 210 74 210 90 V100 H14 Z" fill="#a0522d" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>'), gap=0) if 0 else col(raw(260, 110, '<path d="M14 80 C14 40 50 30 80 34 C110 38 140 56 190 60 C230 64 240 74 240 90 V100 H14 Z" fill="#a0522d" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>'), objects(6, cube_icon, cols=6, size=38, gap=2, color=GREEN), gap=8, align='l')
# more: 5 dots and 3 dots; the bigger group of 5 is circled
math-k-more-less-same/more = row(mark(dots(5, 3, 44, BLUE, gap=10)), Item(30, 10, ''), dots(3, 2, 44, ORANGE, gap=10), gap=10)
# less: 2 dots and 4 dots; the smaller group of 2 is circled
math-k-more-less-same/less = row(mark(dots(2, 2, 44, BLUE, gap=10)), Item(30, 10, ''), dots(4, 2, 44, ORANGE, gap=10), gap=10)
# same: two plates with 3 grapes each
math-k-more-less-same/same = row(plate(170, objects(3, grape, cols=3, size=40, gap=4)), plate(170, objects(3, grape, cols=3, size=40, gap=4)), gap=20)
# compare: a tall block tower and a short block tower
math-k-more-less-same/compare = blocks_stack((6, 2), 280, colors=[BLUE, ORANGE])
# match: cups lined up with straws above them
math-k-more-less-same/match = raw(380, 260, ''.join(f'<line x1="{60 + i * 90}" y1="20" x2="{60 + i * 90}" y2="110" stroke="{c}" stroke-width="10" stroke-linecap="round"/><path d="M{30 + i * 90} 140 h60 l-8 100 h-44 z" fill="{c}" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>' for i, c in enumerate(('#3a7bd5', '#f08a24', '#2f9e5b', '#9b59d0'))))
# greater: the numbers 8 and 6 with the 8 bigger
math-k-more-less-same/greater = row(M('8', 220, color=BLUE), M('6', 110, color=ORANGE), gap=30, align='b')
# add: 2 apples and 3 apples sliding together
math-k-putting-together-and-taking-apart/add = row(objects(2, apple, size=70, gap=6), arrow(50, ORANGE), arrow(50, ORANGE, 'left'), objects(3, apple, size=70, gap=6), gap=10)
# subtract: 4 balloons with 1 floating away
math-k-putting-together-and-taking-apart/subtract = row(objects(3, balloon, size=80, gap=6), col(balloon(80), Item(10, 80, ''), gap=0), gap=30, align='b')
# plus: a big plus sign
math-k-putting-together-and-taking-apart/plus = M('+', 300, color=GREEN)
# minus: a big minus sign
math-k-putting-together-and-taking-apart/minus = M('−', 300, color=RED)
# equals: a big equal sign
math-k-putting-together-and-taking-apart/equals = M('=', 300, color=BLUE)
# in all: 4 birds on a wire joined by 3 more
math-k-putting-together-and-taking-apart/in-all = raw(440, 120, '<line x1="0" y1="96" x2="440" y2="96" stroke="#1f2430" stroke-width="4"/>') if 0 else col(row(*[bird(70, BLUE) for _ in range(4)], Item(30, 10, ''), *[bird(70, ORANGE) for _ in range(3)], gap=4), raw(600, 10, '<rect width="600" height="6" fill="#1f2430"/>'), gap=0)
# circle: a plain circle
math-k-shapes-all-around/circle = shape('circle', 280, BLUE)
# square: a plain square
math-k-shapes-all-around/square = shape('square', 260, ORANGE)
# triangle: a plain triangle
math-k-shapes-all-around/triangle = shape('triangle', 280, GREEN)
# rectangle: a plain rectangle
math-k-shapes-all-around/rectangle = shape('rectangle', 320, PURPLE)
# sort: buttons in a red pile and a blue pile
math-k-sort-and-count/sort = row(raw(200, 160, ''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#e04848" stroke="#1f2430" stroke-width="4"/><circle cx="{x - 7}" cy="{y - 6}" r="4" fill="#1f2430"/><circle cx="{x + 7}" cy="{y + 6}" r="4" fill="#1f2430"/>' for x, y in ((60, 110), (110, 120), (160, 108), (85, 65), (135, 70)))), raw(200, 160, ''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><circle cx="{x - 7}" cy="{y - 6}" r="4" fill="#1f2430"/><circle cx="{x + 7}" cy="{y + 6}" r="4" fill="#1f2430"/>' for x, y in ((60, 110), (110, 120), (160, 108), (110, 68)))), gap=40)
# group: a circle with only blue blocks inside
math-k-sort-and-count/group = row(box(grid([cube_icon(60, BLUE) for _ in range(4)], 2, gap=10), color=BLUE, rx=90, p=30), col(cube_icon(60, RED), cube_icon(60, YELLOW), gap=20), gap=30)
# different: four blue blocks and one red block
math-k-sort-and-count/different = row(*[cube_icon(80, BLUE) for _ in range(4)], cube_icon(80, RED), gap=14)
# teen number: the numbers 11 to 19 on tiles
math-k-teen-numbers/teen-number = grid([tile(str(i), (BLUE, ORANGE, GREEN, PURPLE, RED)[i % 5], 70) for i in range(11, 20)], 5, gap=10)
# ten: a full ten frame
math-k-teen-numbers/ten = tenframe(10, 340)
# ten and some more: a full ten frame plus 3 dots
math-k-teen-numbers/ten-and-some-more = row(tenframe(10, 280), dots(3, 1, 40, BLUE, gap=10), gap=20)
# ones: a ten frame with 6 loose cubes beside it
math-k-teen-numbers/ones = row(tenframe(10, 260), objects(6, cube_icon, cols=2, size=40, gap=8, color=ORANGE), gap=24)
# group: ten cubes in a circle
math-k-teen-numbers/group = box(objects(10, cube_icon, cols=5, size=50, gap=8, color=GREEN), color=BLUE, rx=120, p=34)
# break apart: a rod of 15 cubes snapping into 10 and 5
math-k-teen-numbers/break-apart = col(raw(450, 40, ''.join(f'<rect x="{5 + i * 29}" y="5" width="27" height="30" fill="{"#2f9e5b" if i < 10 else "#f08a24"}" stroke="#1f2430" stroke-width="3"/>' for i in range(15))), arrow(40, dir='down'), raw(470, 40, ''.join(f'<rect x="{5 + i * 29 + (30 if i >= 10 else 0)}" y="5" width="27" height="30" fill="{"#2f9e5b" if i < 10 else "#f08a24"}" stroke="#1f2430" stroke-width="3"/>' for i in range(15))), gap=10)
# root: a plant with its roots in soil highlighted
science-1-plant-and-animal-parts/root = raw(300, 340, '<rect x="0" y="150" width="300" height="190" fill="#a0724a"/><path d="M150 150 V40" stroke="#2f9e5b" stroke-width="10"/><path d="M150 90 C110 60 90 70 80 50 C110 40 140 60 150 90 M150 70 C190 40 210 50 220 30 C190 20 160 40 150 70" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><path d="M150 150 V240 M150 180 L100 230 M150 180 L200 225 M150 210 L115 290 M150 210 L190 285 M150 240 L150 310" stroke="#fde97a" stroke-width="9" stroke-linecap="round"/>')
# soft: a speech bubble with tiny dots
science-1-sound-and-vibration/soft = paint('a small cat tiptoeing on a soft rug past a sleeping puppy')
# pH: a color scale from 0 to 14
science-10-acids-bases-and-solutions/ph = raw(500, 130, ''.join(f'<rect x="{5 + i * 32}" y="10" width="32" height="70" fill="{c}"/>' for i, c in enumerate(('#e0302a', '#e8502a', '#f07a2a', '#f5a524', '#f5c524', '#e8df2a', '#b8d83a', '#5fbf4a', '#2f9e7b', '#2a8fb0', '#2a6fc0', '#3a4fc0', '#5a3fb0', '#6a2f9a', '#5a2080'))) + '<rect x="5" y="10" width="480" height="70" fill="none" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<text x="{21 + i * 32}" y="115" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">{i}</text>' for i in (0, 7, 14)))
# molarity: a flask labeled 0.5 M
science-10-acids-bases-and-solutions/molarity = flask(280, BLUE, label='0.5 M', level=0.55)
# proton: a nucleus with plus signs
science-10-atomic-structure-and-the-periodic-table/proton = nucleus(4, 0, 260, plus=True)
# electron: dots on rings around a nucleus
science-10-atomic-structure-and-the-periodic-table/electron = atom(300, shells=(2, 4))
# neutron: a nucleus with gray balls
science-10-atomic-structure-and-the-periodic-table/neutron = raw(220, 220, ''.join(f'<circle cx="{x}" cy="{y}" r="30" fill="#b8bcc6" stroke="#1f2430" stroke-width="5"/>' for x, y in ((80, 80), (140, 80), (110, 130), (80, 150), (140, 150))))
# isotope: two nuclei with different neutron counts
science-10-atomic-structure-and-the-periodic-table/isotope = row(nucleus(3, 3, 170), nucleus(3, 5, 190), gap=40)
# valence electron: one dot on the outer ring
science-10-atomic-structure-and-the-periodic-table/valence-electron = atom(300, shells=(2, 1), hl_outer=True)
# periodic trend: a table with an arrow showing size change
science-10-atomic-structure-and-the-periodic-table/periodic-trend = col(raw(400, 200, ''.join(f'<rect x="{10 + c * 48}" y="{10 + r * 48}" width="44" height="44" rx="5" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="3"/>' for r in range(4) for c in range(8))), raw(400, 70, '<path d="M30 35 H370" stroke="#e04848" stroke-width="10"/><path d="M390 35 l-26 -16 v32 z" fill="#e04848"/><circle cx="60" cy="35" r="26" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><circle cx="330" cy="35" r="12" fill="#f08a24" stroke="#1f2430" stroke-width="4"/>'), gap=6)
# ionic bond: an electron jumping from Na to Cl
science-10-bonding-and-intermolecular-forces/ionic-bond = raw(440, 220, '<circle cx="100" cy="110" r="70" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><circle cx="340" cy="110" r="80" fill="#d3f0de" stroke="#2f9e5b" stroke-width="6"/><text x="100" y="128" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">Na</text><text x="340" y="128" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">Cl</text><circle cx="168" cy="70" r="12" fill="#e04848"/><path d="M180 64 Q220 20 262 58" fill="none" stroke="#e04848" stroke-width="6" stroke-dasharray="10 7"/><path d="M272 66 l-6 -22 l-16 16 z" fill="#e04848"/>')
# covalent bond: two atoms sharing a pair of dots
science-10-bonding-and-intermolecular-forces/covalent-bond = raw(400, 220, '<circle cx="140" cy="110" r="90" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6" fill-opacity="0.8"/><circle cx="260" cy="110" r="90" fill="#d3f0de" stroke="#2f9e5b" stroke-width="6" fill-opacity="0.8"/><circle cx="200" cy="90" r="13" fill="#e04848"/><circle cx="200" cy="130" r="13" fill="#e04848"/><text x="100" y="128" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">H</text><text x="300" y="128" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#1f2430">H</text>')
# electronegativity: an atom tugging a dot toward itself
science-10-bonding-and-intermolecular-forces/electronegativity = raw(420, 200, '<circle cx="100" cy="100" r="50" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><circle cx="310" cy="100" r="85" fill="#fde3c8" stroke="#f08a24" stroke-width="6"/><text x="100" y="118" font-family="Segoe UI" font-size="44" font-weight="700" text-anchor="middle" fill="#1f2430">H</text><text x="310" y="122" font-family="Segoe UI" font-size="56" font-weight="700" text-anchor="middle" fill="#1f2430">F</text><circle cx="200" cy="100" r="14" fill="#e04848"/><path d="M220 100 H250" stroke="#e04848" stroke-width="7"/><path d="M262 100 l-16 -10 v20 z" fill="#e04848"/>')
# hydrogen bond: dotted lines between water molecules
science-10-bonding-and-intermolecular-forces/hydrogen-bond = row(water(140), raw(80, 60, '<line x1="5" y1="30" x2="75" y2="30" stroke="#3a7bd5" stroke-width="6" stroke-dasharray="8 8"/>'), water(140), gap=0)
# intermolecular force: molecules with dashed attractions
science-10-bonding-and-intermolecular-forces/intermolecular-force = raw(400, 300, ''.join(f'<ellipse cx="{x}" cy="{y}" rx="44" ry="30" fill="#fde3c8" stroke="#f08a24" stroke-width="5"/>' for x, y in ((90, 80), (300, 90), (110, 230), (300, 230))) + ''.join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="9 8"/>' for a, b, c, d in ((140, 80, 250, 90), (90, 115, 105, 195), (300, 125, 300, 195), (155, 230, 250, 230))))
# Lewis structure: O=C=O with dots
science-10-bonding-and-intermolecular-forces/lewis-structure = raw(440, 180, '<text x="70" y="115" font-family="Segoe UI" font-size="64" font-weight="700" text-anchor="middle" fill="#e04848">O</text><text x="220" y="115" font-family="Segoe UI" font-size="64" font-weight="700" text-anchor="middle" fill="#1f2430">C</text><text x="370" y="115" font-family="Segoe UI" font-size="64" font-weight="700" text-anchor="middle" fill="#e04848">O</text><path d="M110 82 H180 M110 102 H180 M260 82 H330 M260 102 H330" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#3a7bd5"/>' for x, y in ((56, 30), (82, 30), (56, 150), (82, 150), (12, 78), (12, 102), (356, 30), (382, 30), (356, 150), (382, 150), (428, 78), (428, 102))))
# chemical equation: CH₄ + 2O₂ → CO₂ + 2H₂O with the reactants and products named
science-10-chemical-reactions-and-equations/chemical-equation = row(col(M('CH₄ + 2O₂', 48), T('reactants', 28, BLUE), gap=4), M('→', 48), col(M('CO₂ + 2H₂O', 48), T('products', 28, GREEN), gap=4), gap=20, align='t')
# coefficient: 2H₂O with 2 highlighted
science-10-chemical-reactions-and-equations/coefficient = M('2H₂O', 160, hl={'2H': RED}) if 0 else row(M('2', 160, color=RED), M('H₂O', 160), gap=6)
# decomposition reaction: two water molecules break apart into two hydrogen molecules and one oxygen molecule
science-10-chemical-reactions-and-equations/decomposition-reaction = col(M('2H₂O → 2H₂ + O₂', 54), row(col(molecule(100), molecule(100), gap=6), arrow(60), col(molecule(70, atoms=(('H', '#fff', -18, 0, 20), ('H', '#fff', 18, 0, 20)), bonds=((0, 1),)), molecule(70, atoms=(('H', '#fff', -18, 0, 20), ('H', '#fff', 18, 0, 20)), bonds=((0, 1),)), gap=10), molecule(100, atoms=(('O', RED, -26, 0, 30), ('O', RED, 26, 0, 30)), bonds=((0, 1),)), gap=16), gap=12)
# bond energy: a bond being snapped
science-10-energy-in-reactions/bond-energy = raw(400, 160, '<circle cx="80" cy="80" r="50" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><circle cx="320" cy="80" r="50" fill="#d3f0de" stroke="#2f9e5b" stroke-width="6"/><path d="M130 80 H180 M220 80 H270" stroke="#1f2430" stroke-width="10"/><path d="M180 60 L196 80 L180 100 M220 60 L204 80 L220 100" fill="none" stroke="#e04848" stroke-width="6" stroke-linejoin="round"/><path d="M200 20 l-6 18 l10 -2 l-6 18" fill="none" stroke="#f5c524" stroke-width="6"/>')
# activation energy: an energy hill with a peak
science-10-energy-in-reactions/activation-energy = plot(lambda x: (4 if x < 4.6 else 2.2) + (4.6 if x < 4.6 else 6.4) * math.exp(-((x - 4.6) / 1.4) ** 2), size=320, xr=(0, 10), yr=(0, 10), arrows_=[(4.6, 4, 4.6, 8.4, RED)], hlines=[4])
# enthalpy: ΔH < 0 on an energy diagram
science-10-energy-in-reactions/enthalpy = plot(lambda x: (6.5 if x < 4.6 else 2.2) + (2.5 if x < 4.6 else 6.8) * math.exp(-((x - 4.6) / 1.4) ** 2), size=320, xr=(0, 10), yr=(0, 10), arrows_=[(9, 6.5, 9, 2.6, RED)], hlines=[6.5, 2.2], texts=[(7.6, 4.4, 'ΔH', RED)])
# energy diagram: a curve with a hump
science-10-energy-in-reactions/energy-diagram = plot(lambda x: (4 if x < 4.6 else 2.2) + (4.6 if x < 4.6 else 6.4) * math.exp(-((x - 4.6) / 1.4) ** 2), size=320, xr=(0, 10), yr=(0, 10))
# kinetic molecular theory: dots bouncing in a box
science-10-gases-and-kinetic-theory/kinetic-molecular-theory = raw(320, 280, '<rect x="10" y="10" width="300" height="260" rx="10" fill="#f4f5f7" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="#3a7bd5"/><line x1="{x}" y1="{y}" x2="{x + dx}" y2="{y + dy}" stroke="#f08a24" stroke-width="5"/><path d="M{x + dx * 1.3:.0f} {y + dy * 1.3:.0f} l{-dx * 0.3 - dy * 0.15:.0f} {-dy * 0.3 + dx * 0.15:.0f} l{dy * 0.3:.0f} {-dx * 0.3:.0f} z" fill="#f08a24"/>' for x, y, dx, dy in ((60, 60, 40, 20), (200, 50, -30, 40), (250, 160, 30, -40), (90, 200, 40, -30), (170, 140, -40, -10), (230, 230, -40, 0))))
# ideal gas law: PV = nRT
science-10-gases-and-kinetic-theory/ideal-gas-law = M('PV = nRT', 140)
# absolute zero: a thermometer at 0 K
science-10-gases-and-kinetic-theory/absolute-zero = thermometer(300, 0.02, label='0 K', color=BLUE)
# fission: a nucleus splitting into two
science-10-nuclear-chemistry/fission = row(nucleus(5, 5, 150), arrow(60, RED), col(nucleus(3, 2, 100), nucleus(2, 3, 100), gap=20), gap=10)
# alpha particle: a cluster of four balls
science-10-nuclear-chemistry/alpha-particle = nucleus(2, 2, 240)
# beta particle: a nucleus shooting out a fast electron (e⁻), the beta particle
science-10-nuclear-chemistry/beta-particle = row(nucleus(5, 6, 160), arrow(110, BLUE, sw=8), over(dot(76, BLUE), M('e⁻', 34, color='#fff')), gap=8)
# gamma ray: a wavy line through a lead block
science-10-nuclear-chemistry/gamma-ray = raw(440, 200, '<rect x="190" y="20" width="80" height="160" fill="#8a8f9c" stroke="#1f2430" stroke-width="6"/><text x="230" y="110" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#fff">Pb</text><path d="' + 'M10 100 ' + ' '.join(f'Q{20 + i * 40} {60 if i % 2 == 0 else 140} {40 + i * 40} 100' for i in range(4)) + '" fill="none" stroke="#9b59d0" stroke-width="7"/><path d="' + 'M280 100 ' + ' '.join(f'Q{290 + i * 40} {60 if i % 2 == 0 else 140} {310 + i * 40} 100' for i in range(3)) + '" fill="none" stroke="#9b59d0" stroke-width="7" opacity="0.6"/>')
# radioactive decay: a decay curve
science-10-nuclear-chemistry/radioactive-decay = plot(lambda x: 7 * 0.5 ** x, size=320, xr=(-0.5, 6), yr=(-0.5, 8), colors=(RED,))
# reaction rate: a steep curve beside a gentle one
science-10-reaction-rates-and-equilibrium/reaction-rate = plot(lambda x: 7 * (1 - math.exp(-1.4 * x)), lambda x: 7 * (1 - math.exp(-0.3 * x)), size=320, xr=(0, 8), yr=(0, 8), colors=(RED, BLUE))
# collision theory: particles colliding
science-10-reaction-rates-and-equilibrium/collision-theory = raw(400, 200, '<circle cx="90" cy="100" r="40" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><circle cx="310" cy="100" r="40" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><path d="M10 100 H40 M360 100 H390" stroke="#8a8f9c" stroke-width="5"/><path d="M140 100 H170 M230 100 H260" stroke="#1f2430" stroke-width="7"/><path d="M180 100 l-14 -10 v20 z M220 100 l14 -10 v20 z" fill="#1f2430"/><path d="M200 60 l8 22 l20 -10 l-12 20 l22 8 l-22 8 l12 20 l-20 -10 l-8 22 l-8 -22 l-20 10 l12 -20 l-22 -8 l22 -8 l-12 -20 l20 10 z" fill="#f5c524" stroke="#1f2430" stroke-width="3"/>')
# equilibrium: double arrows ⇌
science-10-reaction-rates-and-equilibrium/equilibrium = M('⇌', 260, color=BLUE)
# Le Chatelier's principle: a seesaw rebalancing
science-10-reaction-rates-and-equilibrium/le-chatelier-s-principle = row(seesaw(200, tilt=-14), arrow(60, ORANGE), seesaw(200, tilt=0), gap=10)
# concentration: a crowded beaker beside a sparse one
science-10-reaction-rates-and-equilibrium/concentration = row(flask(180, BLUE, beaker=True, dots=24), flask(180, BLUE, beaker=True, dots=5), gap=30)
# mole: 6.02 × 10²³
science-10-stoichiometry-and-the-mole/mole = M('6.02 × 10²³', 110)
# stoichiometry: a mole ratio chain
science-10-stoichiometry-and-the-mole/stoichiometry = col(box(T('mol A', 48), color=BLUE, p=14), arrow(50, dir='down', text='× 2'), box(T('mol B', 48), color=ORANGE, p=14), arrow(50, dir='down', text='× 18'), box(T('grams', 48), color=GREEN, p=14), gap=4)
# molar mass: a periodic table tile for carbon
science-10-stoichiometry-and-the-mole/molar-mass = box(col(T('6', 40, bold=True), T('C', 110, BLUE), T('12.01', 36), gap=0), color=DARK, w=220, h=240, rx=10)
# limiting reactant: unmatched bread and cheese slices
science-10-stoichiometry-and-the-mole/limiting-reactant = col(row(*[raw(80, 60, '<path d="M8 50 V24 C8 6 72 6 72 24 V50 Z" fill="#e8c27a" stroke="#1f2430" stroke-width="4"/>') for _ in range(4)], gap=10), row(*[raw(80, 40, '<path d="M6 34 L74 34 L60 8 L20 8 Z" fill="#f5c524" stroke="#1f2430" stroke-width="4"/>') for _ in range(2)], Item(180, 40, ''), gap=10), gap=10, align='l')
# percent yield: 85% on a bar
science-10-stoichiometry-and-the-mole/percent-yield = col(raw(420, 80, '<rect x="10" y="10" width="400" height="60" rx="10" fill="#fff" stroke="#1f2430" stroke-width="5"/><rect x="10" y="10" width="340" height="60" rx="10" fill="#2f9e5b"/>'), T('85%', 70, GREEN), gap=6)
# Avogadro's number: 6.02 × 10²³
science-10-stoichiometry-and-the-mole/avogadro-s-number = M('6.02 × 10²³', 110, color=BLUE)
# current: arrows along a wire
science-11-electricity-and-magnetism/current = raw(420, 200, '<path d="M20 100 H400" stroke="#b87333" stroke-width="16" stroke-linecap="round"/>' + ''.join(f'<path d="M{60 + i * 100} 60 h40" stroke="#e04848" stroke-width="6"/><path d="M{110 + i * 100} 60 l-14 -9 v18 z" fill="#e04848"/>' for i in range(4)) + ''.join(f'<circle cx="{40 + i * 50}" cy="100" r="6" fill="#f5c524"/>' for i in range(8)))
# resistance: a resistor symbol
science-11-electricity-and-magnetism/resistance = resistor(380)
# Ohm's law: V = IR
science-11-electricity-and-magnetism/ohm-s-law = M('V = IR', 160)
# series circuit: bulbs in a single loop
science-11-electricity-and-magnetism/series-circuit = circuit(320, bulbs=2, series=True)
# electromagnetic induction: a magnet moving in a coil
science-11-electricity-and-magnetism/electromagnetic-induction = raw(420, 200, '<path d="' + ''.join(f'M{170 + i * 30} 40 a30 60 0 0 1 0 120 ' for i in range(6)) + '" fill="none" stroke="#b87333" stroke-width="8"/><rect x="10" y="78" width="70" height="44" fill="#e04848" stroke="#1f2430" stroke-width="5"/><rect x="80" y="78" width="70" height="44" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><path d="M90 60 H140" stroke="#f08a24" stroke-width="6"/><path d="M156 60 l-16 -10 v20 z" fill="#f08a24"/>')
# work: a crate lifted up: a force upward and the distance it moved
science-11-energy-and-work/work = raw(320, 320, '<g opacity="0.3">' + g(crate(90), 50, 210) + '</g>' + g(crate(90), 50, 60) + '<line x1="20" y1="302" x2="300" y2="302" stroke="#8a8f9c" stroke-width="10"/><line x1="95" y1="54" x2="95" y2="24" stroke="#e04848" stroke-width="10"/><path d="M95 4 l-14 24 h28 z" fill="#e04848"/><text x="122" y="34" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700" fill="#e04848">force</text><line x1="180" y1="122" x2="180" y2="256" stroke="#3a7bd5" stroke-width="6"/><path d="M180 104 l-12 22 h24 z M180 272 l-12 -22 h24 z" fill="#3a7bd5"/><text x="196" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700" fill="#3a7bd5">distance</text>')
# conservation of energy: a swinging pendulum
science-11-energy-and-work/conservation-of-energy = raw(380, 300, '<line x1="80" y1="20" x2="300" y2="20" stroke="#1f2430" stroke-width="8"/><line x1="190" y1="20" x2="90" y2="200" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="8 7"/><line x1="190" y1="20" x2="290" y2="200" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="8 7"/><line x1="190" y1="20" x2="190" y2="240" stroke="#1f2430" stroke-width="5"/><circle cx="90" cy="200" r="24" fill="#f5c524" stroke="#1f2430" stroke-width="4" opacity="0.6"/><circle cx="290" cy="200" r="24" fill="#f5c524" stroke="#1f2430" stroke-width="4" opacity="0.6"/><circle cx="190" cy="240" r="28" fill="#f5c524" stroke="#1f2430" stroke-width="5"/><path d="M110 250 Q190 300 270 250" fill="none" stroke="#f08a24" stroke-width="6"/><path d="M272 250 l-4 18 l-14 -12 z" fill="#f08a24"/>')
# law of universal gravitation: two spheres with arrows toward each other
science-11-gravity-and-electrostatics/law-of-universal-gravitation = raw(440, 200, '<circle cx="90" cy="100" r="70" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><circle cx="370" cy="100" r="44" fill="#a0724a" stroke="#1f2430" stroke-width="6"/><path d="M170 100 H210 M330 100 H290" stroke="#e04848" stroke-width="8"/><path d="M232 100 l-24 -14 v28 z M268 100 l24 -14 v28 z" fill="#e04848"/>')
# Coulomb's law: two charges close together push hard (long arrows); far apart they push weakly (short arrows)
science-11-gravity-and-electrostatics/coulomb-s-law = col(row(arrow(90, RED, 'left', sw=10), charge('+', 80), charge('+', 80), arrow(90, RED, sw=10), gap=4), row(arrow(34, RED, 'left', sw=8), charge('+', 80), Item(150, 10, ''), charge('+', 80), arrow(34, RED, sw=8), gap=4), gap=36)
# inverse square law: spreading lines through larger squares
science-11-gravity-and-electrostatics/inverse-square-law = raw(440, 260, '<circle cx="30" cy="130" r="16" fill="#f5c524" stroke="#1f2430" stroke-width="4"/><path d="M30 130 L430 20 M30 130 L430 240 M30 130 L430 130" stroke="#8a8f9c" stroke-width="3" stroke-dasharray="8 6"/>' + ''.join(f'<rect x="{x}" y="{130 - h / 2}" width="10" height="{h}" fill="{c}" stroke="#1f2430" stroke-width="3"/>' for x, h, c in ((120, 50, '#3a7bd5'), (230, 110, '#f08a24'), (340, 170, '#2f9e5b'))))
# field: field lines around a sphere
science-11-gravity-and-electrostatics/field = field_lines(320, 'sphere')
# charge: two plus signs pushing apart
science-11-gravity-and-electrostatics/charge = row(charge('+', 110), Item(10, 10, ''), arrow(60, RED, 'left', sw=10), arrow(60, RED, sw=10), Item(10, 10, ''), charge('+', 110), gap=0) if 0 else row(arrow(70, RED, 'left', sw=10), charge('+', 110), Item(50, 10, ''), charge('+', 110), arrow(70, RED, sw=10), gap=6)
# electromagnetic spectrum: a band from radio to gamma
science-11-light-and-the-electromagnetic-spectrum/electromagnetic-spectrum = spectrum(440)
# photon: a wavy packet
science-11-light-and-the-electromagnetic-spectrum/photon = raw(420, 160, '<path d="' + 'M20 80 ' + ' '.join(f'L{20 + i * 4} {80 - 50 * math.sin(i * 0.5) * math.exp(-((i - 45) / 22) ** 2):.1f}' for i in range(1, 92)) + '" fill="none" stroke="#9b59d0" stroke-width="7" stroke-linejoin="round"/><path d="M390 80 l-20 -12 v24 z" fill="#9b59d0"/>')
# wave-particle duality: a wave beside a dot
science-11-light-and-the-electromagnetic-spectrum/wave-particle-duality = row(wave(200, 2, color=PURPLE), T('+', 60), dot(70, PURPLE), gap=20)
# conservation of momentum: two carts pushing apart
science-11-momentum-and-collisions/conservation-of-momentum = row(arrow(70, RED, 'left', sw=10), raw(150, 110, '<rect x="5" y="10" width="140" height="66" rx="8" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><circle cx="35" cy="88" r="16" fill="#1f2430"/><circle cx="115" cy="88" r="16" fill="#1f2430"/>'), raw(150, 110, '<rect x="5" y="10" width="140" height="66" rx="8" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><circle cx="35" cy="88" r="16" fill="#1f2430"/><circle cx="115" cy="88" r="16" fill="#1f2430"/>'), arrow(70, RED, sw=10), gap=4, align='c')
# displacement: an arrow from start to finish
science-11-motion-and-kinematics/displacement = raw(420, 240, '<path d="M40 190 C 100 40, 200 260, 260 110 S 360 60, 380 50" fill="none" stroke="#8a8f9c" stroke-width="5" stroke-dasharray="10 8"/><line x1="40" y1="190" x2="360" y2="62" stroke="#e04848" stroke-width="9"/><path d="M384 52 l-28 -2 l12 22 z" fill="#e04848"/><circle cx="40" cy="190" r="14" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><path d="M380 50 V10 l30 10 l-30 10" fill="#e04848" stroke="#1f2430" stroke-width="3"/>')
# velocity: an arrow with a speed label
science-11-motion-and-kinematics/velocity = col(T('20 m/s', 60, RED), arrow(340, RED, sw=14), gap=6)
# acceleration: a ball falling with growing gaps
science-11-motion-and-kinematics/acceleration = raw(200, 380, ''.join(f'<circle cx="100" cy="{y}" r="20" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' for y in (24, 70, 126, 192, 268, 354)))
# vector: an arrow
science-11-motion-and-kinematics/vector = arrow(340, BLUE, sw=16)
# scalar: a number with no arrow
science-11-motion-and-kinematics/scalar = T('25 kg', 140, DARK)
# free fall: a ball dropping
science-11-motion-and-kinematics/free-fall = raw(200, 360, '<circle cx="100" cy="70" r="40" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M100 130 V310" stroke="#1f2430" stroke-width="7" stroke-dasharray="14 10"/><path d="M100 340 l-20 -34 h40 z" fill="#1f2430"/><path d="M60 20 h80" stroke="#8a8f9c" stroke-width="5" opacity="0"/>')
# Newton's second law: F = ma
science-11-newton-s-laws/newton-s-second-law = M('F = ma', 160)
# free-body diagram: a box with arrows pointing out
science-11-newton-s-laws/free-body-diagram = col(arrow(70, BLUE, 'up', sw=10), row(arrow(70, ORANGE, 'left', sw=10), crate(140), arrow(70, GREEN, sw=10), gap=4), arrow(70, RED, 'down', sw=10), gap=4)
# normal force: a box on a table with an up arrow
science-11-newton-s-laws/normal-force = col(arrow(80, GREEN, 'up', sw=12), crate(130), raw(300, 60, '<rect x="10" y="0" width="280" height="18" fill="#a0724a" stroke="#1f2430" stroke-width="4"/><rect x="30" y="18" width="16" height="40" fill="#a0724a"/><rect x="254" y="18" width="16" height="40" fill="#a0724a"/>'), gap=4)
# transverse wave: a wave with up-down arrows
science-11-waves-and-sound/transverse-wave = wave(380, 2, arrows_=True)
# longitudinal wave: a spring with compressed bands
science-11-waves-and-sound/longitudinal-wave = spring(400)
# wave speed: v = fλ
science-11-waves-and-sound/wave-speed = M('v = fλ', 160)
# biome: three biomes side by side: forest, desert, tundra
science-12-ecosystems-and-biomes/biome = row(col(box(row(pine(60), pine(76), gap=0, align='b'), w=130, h=130, color=GREEN, rx=10), T('forest', 28, GREEN), gap=6), col(box(raw(90, 100, '<circle cx="70" cy="20" r="16" fill="#f5c524"/><path d="M36 96 V40 a9 9 0 0 1 18 0 V96 Z M36 70 H22 V52 a7 7 0 0 1 14 0 M54 62 H68 V46 a7 7 0 0 0 -14 0" fill="#2f9e5b" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>'), w=130, h=130, color=ORANGE, fill='#fbe7b5', rx=10), T('desert', 28, ORANGE), gap=6), col(box(raw(100, 90, '<path d="M4 80 L36 30 L56 56 L70 40 L96 80 Z" fill="#fff" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#8fb6ea"/>' for x, y in ((10, 10), (40, 6), (70, 16), (90, 6), (24, 26)))), w=130, h=130, color=BLUE, fill='#eef3f8', rx=10), T('tundra', 28, BLUE), gap=6), gap=14)
# energy return on investment: a small arrow in, big arrow out
science-12-energy-sources/energy-return-on-investment = row(arrow(80, RED, sw=8), box(T('energy', 34), color=GRAY, p=16), arrow(180, GREEN, sw=24), gap=6)
# systems thinking: a web of connected boxes
science-12-engineering-for-global-challenges/systems-thinking = raw(380, 300, ''.join(f'<path d="M{a} {b} L{c} {d}" stroke="#8a8f9c" stroke-width="5"/>' for a, b, c, d in ((80, 60, 300, 60), (80, 60, 190, 150), (300, 60, 190, 150), (190, 150, 80, 240), (190, 150, 300, 240), (80, 240, 300, 240), (80, 60, 80, 240))) + ''.join(f'<rect x="{x - 40}" y="{y - 28}" width="80" height="56" rx="10" fill="{c}" stroke="#1f2430" stroke-width="4"/>' for x, y, c in ((80, 60, '#d6e6fb'), (300, 60, '#fde3c8'), (190, 150, '#d3f0de'), (80, 240, '#ead7f7'), (300, 240, '#fde97a'))))
# tradeoff: a scale with cost on one side and safety on the other: gaining one means giving up some of the other
science-12-engineering-for-global-challenges/tradeoff = col(arrow(170, ORANGE, double=True), scale_icon(320, coin(70), shield(70), tilt=0), gap=4)
# life cycle assessment: a loop from raw material to landfill
science-12-engineering-for-global-challenges/life-cycle-assessment = cycle(['raw', 'make', 'use', 'waste'], r=140)
# subproblem: one big box splitting into small boxes
science-12-engineering-for-global-challenges/subproblem = col(box(w=300, h=70, color=BLUE), row(*[arrow(30, dir='down') for _ in range(3)], gap=70), row(*[box(w=80, h=60, color=ORANGE) for _ in range(3)], gap=20), gap=6)
# criteria: a checklist
science-12-engineering-for-global-challenges/criteria = clipboard(280, inner=col(*[row(check(34), raw(140, 16, '<rect width="140" height="12" rx="6" fill="#c4c8d0"/>'), gap=10) for _ in range(3)], gap=16))
# demographic transition: two lines falling over time
science-12-population-and-resources/demographic-transition = plot(size=320, xr=(0, 10), yr=(0, 10), curves=[([0, 2, 4, 6, 8, 10], [8, 8, 5, 3, 2.5, 2.5]), ([0, 2, 4, 6, 8, 10], [8.5, 6, 3.5, 2.5, 2.3, 2.2])], colors=(BLUE, RED))
# ecological footprint: a footprint filled with a globe
science-12-population-and-resources/ecological-footprint = over(footprint(320, GREEN), globe(110), dx=110, dy=120)
# birth rate: a line falling
science-12-population-and-resources/birth-rate = plot(lambda x: 8 - 0.6 * x, size=320, xr=(0, 10), yr=(0, 10), colors=(RED,))
# age structure: a population pyramid
science-12-population-and-resources/age-structure = pop_pyramid(320)
# reversible: an ice cube and a puddle with arrows both ways
science-2-heating-and-cooling/reversible = row(raw(110, 110, '<rect x="10" y="10" width="90" height="90" rx="12" fill="#d6eefc" stroke="#3a7bd5" stroke-width="6"/><path d="M28 28 L50 40" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'), col(arrow(90, RED), arrow(90, BLUE, 'left'), gap=10), raw(170, 80, '<ellipse cx="85" cy="50" rx="80" ry="24" fill="#a8d4f5" stroke="#3a7bd5" stroke-width="5"/>'), gap=14)
# balanced forces: a rope with two equal arrows pulling opposite ways and a flag at the center
science-3-balanced-and-unbalanced-forces/balanced-forces = raw(460, 160, '<path d="M60 80 H400" stroke="#a0724a" stroke-width="12" stroke-linecap="round"/><path d="M230 80 V30 l40 12 l-40 12" fill="#e04848" stroke="#1f2430" stroke-width="3"/><path d="M110 120 H30" stroke="#3a7bd5" stroke-width="12"/><path d="M10 120 l26 -16 v32 z" fill="#3a7bd5"/><path d="M350 120 H430" stroke="#3a7bd5" stroke-width="12"/><path d="M450 120 l-26 -16 v32 z" fill="#3a7bd5"/>')
# unbalanced forces: a box with a big arrow on one side and a small arrow on the other
science-3-balanced-and-unbalanced-forces/unbalanced-forces = row(arrow(170, RED, sw=20), crate(140), arrow(60, BLUE, 'left', sw=8), gap=4)
# rock layer: a cliff with colored bands of rock and small fossils in them
science-3-fossils-and-changing-environments/rock-layer = layers(5, 320, fossils=((1, 120), (3, 220)))
# life cycle: a circle of frog stages: eggs, tadpole, froglet, frog
science-3-life-cycles/life-cycle = cycle(['eggs', 'tadpole', 'froglet', 'frog'], r=140, colors=[BLUE, TEAL, GREEN, GREEN])
# attract: two bar magnets, N facing S, with arrows pointing together
science-3-magnets-and-static-electricity/attract = row(magnet(180), arrow(40, GREEN), arrow(40, GREEN, 'left'), magnet(180), gap=6)
# repel: two bar magnets, N facing N, with arrows pointing apart
science-3-magnets-and-static-electricity/repel = row(arrow(40, RED, 'left'), magnet(180, flip=True), Item(40, 10, ''), magnet(180), arrow(40, RED), gap=6)
# pole: a bar magnet with a red N end and a blue S end
science-3-magnets-and-static-electricity/pole = magnet(380)
# non-contact force: a magnet pulling a paper clip across a small gap
science-3-magnets-and-static-electricity/non-contact-force = row(magnet(220, flip=True), raw(60, 40, '<path d="M8 20 h44" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="6 6"/>'), raw(110, 60, '<path d="M20 15 H90 A15 15 0 0 1 90 45 H30 A10 10 0 0 1 30 25 H80" fill="none" stroke="#8a8f9c" stroke-width="7" stroke-linecap="round"/>'), gap=0)
# forecast: a weather map with sun and cloud symbols
science-3-weather-and-climate/forecast = map_tile(340, roads=False, pins=()) if 0 else over(us_map(420, color=GREEN), row(sun(90), raincloud(110), gap=80), dx=60, dy=40)
# circuit: a battery, wire and bulb in a loop
science-4-energy-conversion-devices/circuit = circuit(320, bulbs=1)
# internal: a body outline with a heart inside
science-4-structures-and-senses/internal = raw(220, 340, '<circle cx="110" cy="50" r="38" fill="none" stroke="#1f2430" stroke-width="6"/><path d="M60 100 Q110 88 160 100 L180 240 H40 Z" fill="none" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M60 120 L30 230 M160 120 L190 230 M80 240 L75 330 M140 240 L145 330" stroke="#1f2430" stroke-width="6" stroke-linecap="round"/><path d="M122 140 c-6 -14 -26 -10 -24 6 c2 14 24 26 24 26 s22 -12 24 -26 c2 -16 -18 -20 -24 -6 z" fill="#e04848" stroke="#1f2430" stroke-width="4"/>')
# reflect: light bouncing off a mirror: the angle in equals the angle out
science-4-structures-and-senses/reflect = raw(440, 270, '<line x1="40" y1="226" x2="400" y2="226" stroke="#8a8f9c" stroke-width="12"/><line x1="220" y1="218" x2="220" y2="80" stroke="#1f2430" stroke-width="3" stroke-dasharray="8 6"/><circle cx="60" cy="56" r="30" fill="#f5c524" stroke="#1f2430" stroke-width="5"/><path d="M84 74 L220 218 L360 72" fill="none" stroke="#f08a24" stroke-width="7" stroke-linejoin="round"/><path d="M150 144 L126.9 135.6 L142.9 120.4 Z M362 70 L352.9 93.6 L336.9 78.4 Z" fill="#f08a24"/><path d="M220 168 A50 50 0 0 0 185.7 181.6" fill="none" stroke="#e04848" stroke-width="5"/><path d="M220 168 A50 50 0 0 1 254.3 181.6" fill="none" stroke="#e04848" stroke-width="5"/><text x="220" y="40" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">equal angles</text><text x="400" y="262" font-family="Segoe UI, Arial, sans-serif" font-size="24" font-weight="700" text-anchor="end" fill="#5a5f6c">mirror</text>')
# pupil: an eye with a large pupil
science-4-structures-and-senses/pupil = eye(300, pupil=0.55)
# amplitude: two waves, one tall and one short
science-4-waves-and-information/amplitude = col(wave(380, 2, amp=1.0), wave(380, 2, amp=0.35, color=ORANGE), gap=0)
# wavelength: a wave with one peak-to-peak span marked
science-4-waves-and-information/wavelength = wave(400, 2, marks='wavelength')
# code: dots and dashes in a row
science-4-waves-and-information/code = raw(440, 80, ''.join(f'<circle cx="{x}" cy="40" r="14" fill="#1f2430"/>' if k == '.' else f'<rect x="{x - 24}" y="30" width="48" height="20" rx="10" fill="#1f2430"/>' for x, k in zip(range(30, 440, 56), '.-..--.-')))
# pattern: a regular wave pattern
science-4-waves-and-information/pattern = wave(400, 3)
# system: air, water, land and life linked in a cycle
science-5-earth-s-spheres/system = cycle(['air', 'water', 'land', 'life'], r=140, colors=[BLUE, TEAL, BROWN, GREEN])
# food web: a food web: arrows point from each food to the animal that eats it
science-5-food-webs-and-matter-cycles/food-web = web({'grass': (210, 305, GREEN), 'rabbit': (95, 205, ORANGE), 'mouse': (325, 205, ORANGE), 'fox': (95, 50, RED), 'hawk': (325, 50, PURPLE)}, [('grass', 'rabbit'), ('grass', 'mouse'), ('rabbit', 'fox'), ('mouse', 'fox'), ('mouse', 'hawk'), ('rabbit', 'hawk')], 400)
# carbon dioxide: a leaf with an arrow of CO₂ going in
science-5-food-webs-and-matter-cycles/carbon-dioxide = row(col(T('CO₂', 48, GRAY), arrow(80, GRAY, sw=8), gap=0), raw(200, 140, '<path d="M10 70 C40 10 150 0 190 70 C150 140 40 130 10 70 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M10 70 H170" stroke="#1f2430" stroke-width="4"/>'), gap=6)
# force: an arrow pointing down at a ball
science-5-gravity/force = col(arrow(100, RED, 'down', sw=14), ball(150, BLUE), gap=6)
# orbit: the Moon on a circular path around Earth
science-5-gravity/orbit = orbit(340, center=earth(110), body=moon(50), sun_size=110)
# downward: arrows pointing down to the ground
science-5-gravity/downward = col(row(*[arrow(110, RED, 'down', sw=10) for _ in range(4)], gap=40), raw(380, 30, '<rect width="380" height="24" fill="#a0724a"/>'), gap=0)
# Earth's center: Earth with arrows pointing to its middle
science-5-gravity/earth-s-center = raw(320, 320, '<circle cx="160" cy="160" r="110" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><path d="M110 120 c20 -30 50 -10 60 10 c10 20 -20 40 -40 30 z M190 200 c20 -10 40 10 30 30 c-10 10 -30 0 -30 -30 z" fill="#2f9e5b"/>' + ''.join(f'<line x1="{160 + 150 * math.cos(a):.0f}" y1="{160 + 150 * math.sin(a):.0f}" x2="{160 + 122 * math.cos(a):.0f}" y2="{160 + 122 * math.sin(a):.0f}" stroke="#e04848" stroke-width="7"/><path d="M{160 + 116 * math.cos(a):.0f} {160 + 116 * math.sin(a):.0f} l{12 * math.cos(a) - 9 * math.sin(a):.0f} {12 * math.sin(a) + 9 * math.cos(a):.0f} l{18 * math.sin(a):.0f} {-18 * math.cos(a):.0f} z" fill="#e04848"/>' for a in [k * math.pi / 4 for k in range(8)]) + '<circle cx="160" cy="160" r="8" fill="#e04848"/>')
# particle: a sugar cube breaking into dots
science-5-matter-is-made-of-particles/particle = row(raw(130, 130, '<path d="M20 50 L60 20 H120 V90 L80 120 H20 Z M20 50 H80 L120 20 M80 50 V120" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), arrow(60), raw(140, 130, ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" stroke="#1f2430" stroke-width="3"/>' for x, y in ((20, 30), (60, 20), (100, 40), (130, 70), (40, 70), (80, 90), (110, 110), (30, 110), (70, 120), (120, 20)))), gap=10)
# conservation of mass: four blocks balance 100 g; rearranged, they still balance 100 g
science-5-matter-is-made-of-particles/conservation-of-mass = row(scale_icon(220, row(*[cube_icon(26, c) for c in (BLUE, ORANGE, GREEN, PURPLE)], gap=0), tile('100 g', GRAY, 44)), arrow(50, ORANGE), scale_icon(220, grid([cube_icon(26, c) for c in (BLUE, ORANGE, GREEN, PURPLE)], 2, gap=0), tile('100 g', GRAY, 44)), gap=10)
# rotate: Earth with a curved arrow around its axis
science-5-sun-stars-and-shadows/rotate = raw(320, 320, '<line x1="120" y1="30" x2="200" y2="290" stroke="#1f2430" stroke-width="5" stroke-dasharray="10 8"/><circle cx="160" cy="160" r="100" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><path d="M110 120 c20 -30 50 -10 60 10 c10 20 -20 40 -40 30 z M190 200 c20 -10 40 10 30 30 c-10 10 -30 0 -30 -30 z" fill="#2f9e5b"/><path d="M60 250 Q160 320 270 240" fill="none" stroke="#f08a24" stroke-width="9"/><path d="M285 228 l-26 2 l12 22 z" fill="#f08a24"/>')
# revolve: Earth on a path around the Sun
science-5-sun-stars-and-shadows/revolve = orbit(360, center=sun(110), body=earth(60), sun_size=100)
# constellation: seven star dots joined in a dipper shape
science-5-sun-stars-and-shadows/constellation = raw(420, 260, ''.join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#8a8f9c" stroke-width="4"/>' for a, b, c, d in ((30, 70, 110, 60), (110, 60, 180, 90), (180, 90, 250, 120), (250, 120, 270, 200), (270, 200, 380, 210), (380, 210, 390, 130), (390, 130, 250, 120))) + ''.join(f'<path d="M{x} {y - 16} l5 11 l12 1 l-9 8 l3 12 l-11 -6 l-11 6 l3 -12 l-9 -8 l12 -1 z" fill="#f5c524" stroke="#1f2430" stroke-width="2"/>' for x, y in ((30, 70), (110, 60), (180, 90), (250, 120), (270, 200), (380, 210), (390, 130))))
# cell: a round cell with a nucleus
science-6-cells-and-body-systems/cell = cell(300)
# organelle: a cell with leader lines to three organelles: nucleus, mitochondria, membrane
science-6-cells-and-body-systems/organelle = raw(480, 220, g(cell(260), 0, 6) + ''.join(f'<line x1="{x}" y1="{y}" x2="282" y2="{ty - 9}" stroke="#1f2430" stroke-width="3"/><circle cx="{x}" cy="{y}" r="5" fill="#1f2430"/><text x="288" y="{ty}" font-family="Segoe UI, Arial, sans-serif" font-size="28" font-weight="700" fill="{c}">{t}</text>' for x, y, ty, t, c in ((130, 110, 50, 'nucleus', PURPLE), (195, 172, 120, 'mitochondria', ORANGE), (252, 110, 196, 'membrane', GREEN))))
# nucleus: a cell with a dark center
science-6-cells-and-body-systems/nucleus = cell(300, organelles=False, nucleus_='dark')
# cell membrane: a cell with a highlighted outer edge
science-6-cells-and-body-systems/cell-membrane = cell(300, membrane_hl=True)
# tissue: a cluster of matching cells
science-6-cells-and-body-systems/tissue = grid([cell(110, organelles=False) for _ in range(9)], 3, gap=0)
# organ system: a torso outline with the stomach and intestines
science-6-cells-and-body-systems/organ-system = torso(300, inner=stomach(120))
# ocean current: the North Atlantic: currents circle clockwise, warm water north, cold water south
science-6-climate-and-ocean-circulation/ocean-current = world_map(440, view=(-100, -5, 10, 65), flows=[([(-80, 25), (-75, 35), (-58, 41), (-38, 46), (-18, 50)], RED, 14), ([(-14, 44), (-18, 32), (-22, 20)], BLUE, 14), ([(-26, 14), (-48, 13), (-68, 18)], ORANGE, 14)], labels=[(-62, 46.5, 'Gulf Stream', RED, 24)])
# Coriolis effect: a globe with curved wind arrows
science-6-climate-and-ocean-circulation/coriolis-effect = raw(320, 320, '<circle cx="160" cy="160" r="130" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><line x1="30" y1="160" x2="290" y2="160" stroke="#fff" stroke-width="3" stroke-dasharray="8 6"/><path d="M110 70 Q150 110 200 100" fill="none" stroke="#f5c524" stroke-width="8"/><path d="M214 96 l-22 -10 l2 22 z" fill="#f5c524"/><path d="M110 250 Q150 210 200 220" fill="none" stroke="#f5c524" stroke-width="8"/><path d="M214 224 l-22 10 l2 -22 z" fill="#f5c524"/>')
# convection: a loop of red and blue arrows
science-6-climate-and-ocean-circulation/convection = raw(320, 300, '<rect x="10" y="10" width="300" height="280" rx="12" fill="#f4f5f7" stroke="#1f2430" stroke-width="5"/><path d="M110 230 V80" stroke="#e04848" stroke-width="10"/><path d="M110 64 l-16 24 h32 z" fill="#e04848"/><path d="M130 60 H190" stroke="#e04848" stroke-width="10"/><path d="M210 80 V230" stroke="#3a7bd5" stroke-width="10"/><path d="M210 246 l-16 -24 h32 z" fill="#3a7bd5"/><path d="M190 260 H130" stroke="#3a7bd5" stroke-width="10"/><path d="M80 270 l10 -20 l10 20 l10 -20 l10 20" fill="none" stroke="#f08a24" stroke-width="5"/>')
# latitude: a globe with horizontal lines
science-6-climate-and-ocean-circulation/latitude = globe(300, lat=True)
# prevailing winds: prevailing winds: trade winds blow west near the equator, westerlies east farther out
science-6-climate-and-ocean-circulation/prevailing-winds = col(world_map(440, flows=[([(lo + 40, la), (lo, la)], c, 10) for la, c in ((15, ORANGE), (-15, ORANGE), (70, PURPLE), (-70, PURPLE)) for lo in (-150, -60, 30, 120)] + [([(lo, la), (lo + 40, la)], BLUE, 10) for la in (45, -45) for lo in (-150, -60, 30, 120)]), row(T('trade winds', 26, ORANGE), T('westerlies', 26, BLUE), T('polar easterlies', 26, PURPLE), gap=20), gap=8)
# moon phase: eight Moon shapes from new to full
science-6-earth-sun-moon-system/moon-phase = grid([moon(80, p) for p in (0, 1, 2, 3, 4, 5, 6, 7)], 4, gap=14)
# eclipse: Sun, Moon and Earth in a line with a shadow
science-6-earth-sun-moon-system/eclipse = raw(460, 200, '<path d="M120 60 L330 85 L330 115 L120 140 Z" fill="#c4c8d0" opacity="0.5"/><circle cx="60" cy="100" r="56" fill="#f5c524" stroke="#1f2430" stroke-width="5"/><circle cx="250" cy="100" r="18" fill="#c4c8d0" stroke="#1f2430" stroke-width="4"/><path d="M268 92 L400 76 V124 L268 108 Z" fill="#3b4256" opacity="0.7"/><circle cx="400" cy="100" r="44" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/>')
# axis: a tilted globe with a line through the poles
science-6-earth-sun-moon-system/axis = raw(300, 320, '<g transform="rotate(23 150 160)"><line x1="150" y1="10" x2="150" y2="310" stroke="#e04848" stroke-width="7"/><circle cx="150" cy="160" r="110" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><line x1="150" y1="10" x2="150" y2="50" stroke="#e04848" stroke-width="7"/><line x1="150" y1="270" x2="150" y2="310" stroke="#e04848" stroke-width="7"/><line x1="40" y1="160" x2="260" y2="160" stroke="#fff" stroke-width="3" stroke-dasharray="8 6"/></g>')
# rotation: a globe with a curved arrow around it
science-6-earth-sun-moon-system/rotation = raw(320, 320, '<circle cx="160" cy="160" r="100" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><path d="M110 120 c20 -30 50 -10 60 10 c10 20 -20 40 -40 30 z M190 200 c20 -10 40 10 30 30 c-10 10 -30 0 -30 -30 z" fill="#2f9e5b"/><path d="M40 200 A130 60 0 0 0 280 200" fill="none" stroke="#f08a24" stroke-width="9"/><path d="M292 190 l-26 2 l12 22 z" fill="#f08a24"/>')
# revolution: an orbit path around the Sun
science-6-earth-sun-moon-system/revolution = orbit(360, center=sun(110), body=earth(60), sun_size=100)
# season: Earth at four points around the Sun
science-6-earth-sun-moon-system/season = raw(440, 300, '<ellipse cx="220" cy="150" rx="190" ry="110" fill="none" stroke="#8a8f9c" stroke-width="4" stroke-dasharray="10 8"/><circle cx="220" cy="150" r="46" fill="#f5c524" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<g transform="translate({x} {y}) rotate(23)"><circle r="24" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><line x1="0" y1="-34" x2="0" y2="34" stroke="#e04848" stroke-width="4"/></g>' for x, y in ((30, 150), (410, 150), (220, 40), (220, 260))))
# geologic time scale: a long bar split into colored eras
science-6-geologic-time/geologic-time-scale = raw(460, 120, ''.join(f'<rect x="{x}" y="20" width="{w}" height="60" fill="{c}" stroke="#1f2430" stroke-width="4"/>' for x, w, c in ((10, 300, '#ead7f7'), (310, 70, '#d6e6fb'), (380, 45, '#d3f0de'), (425, 25, '#fde97a'))) + '<path d="M10 100 H450" stroke="#1f2430" stroke-width="4"/><path d="M460 100 l-14 -8 v16 z" fill="#1f2430"/>')
# stratum: stacked rock bands
science-6-geologic-time/stratum = layers(5, 320)
# law of superposition: rock layers with an arrow pointing to the oldest at bottom
science-6-geologic-time/law-of-superposition = row(layers(5, 260), col(T('oldest', 34, RED), arrow(80, RED, 'left', sw=8), gap=0), gap=6, align='b')
# gravity: arrows pulling a small ball toward a big one
science-6-gravity-and-the-solar-system/gravity = row(ball(70, GRAY), arrow(80, RED, sw=10), raw(200, 200, '<circle cx="100" cy="100" r="90" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/>'), gap=8)
# orbit: an oval path around a planet
science-6-gravity-and-the-solar-system/orbit = orbit(360, center=raw(120, 120, '<circle cx="60" cy="60" r="54" fill="#f08a24" stroke="#1f2430" stroke-width="5"/>'), body=ball(40, GRAY), ellipse_=True)
# solar system: the Sun with eight orbit rings
science-6-gravity-and-the-solar-system/solar-system = solar_system(440)
# astronomical unit: a line from Sun to Earth labeled 1 AU
science-6-gravity-and-the-solar-system/astronomical-unit = raw(460, 160, '<circle cx="60" cy="80" r="50" fill="#f5c524" stroke="#1f2430" stroke-width="5"/><circle cx="410" cy="80" r="22" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><path d="M120 80 H380" stroke="#e04848" stroke-width="6"/><path d="M120 66 V94 M380 66 V94" stroke="#e04848" stroke-width="6"/><text x="250" y="60" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#e04848">1 AU</text>')
# plate tectonics: a globe with plate outlines
science-6-plate-tectonics/plate-tectonics = raw(320, 320, '<circle cx="160" cy="160" r="140" fill="#3a7bd5" stroke="#1f2430" stroke-width="6"/><path d="M60 80 c40 -20 80 0 90 30 c10 40 -40 60 -70 50 c-30 -10 -40 -50 -20 -80 z M180 170 c30 -20 70 0 70 40 c0 40 -40 60 -70 50 c-20 -10 -30 -60 0 -90 z M190 50 c30 0 60 20 50 50 c-20 10 -50 0 -50 -50 z" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/><path d="M40 160 C90 140 120 200 170 150 C210 110 250 140 300 120 M160 20 C150 70 190 110 170 150 C150 200 180 260 150 300" fill="none" stroke="#e04848" stroke-width="6" stroke-dasharray="12 7"/>')
# subduction: one plate diving under another
science-6-plate-tectonics/subduction = raw(440, 250, '<path d="M10 60 H230 L410 230 L380 245 L210 100 H10 Z" fill="#8a8f9c" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M230 60 H430 V150 H300 Z" fill="#a0724a" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M60 35 H170" stroke="#e04848" stroke-width="8"/><path d="M188 35 l-20 -12 v24 z" fill="#e04848"/><path d="M290 175 l50 46" stroke="#e04848" stroke-width="8"/><path d="M354 234 l-8 -24 l-14 16 z" fill="#e04848"/>')
# rock cycle: a loop linking three rock types
science-6-plate-tectonics/rock-cycle = cycle(['igneous', 'sedimentary', 'metamorphic'], r=140, colors=[RED, ORANGE, PURPLE])
# continental drift: South America and Africa fitting together
science-6-plate-tectonics/continental-drift = raw(420, 300, '<path d="M60 40 C120 20 170 60 180 100 C170 140 150 170 130 220 C120 260 100 290 90 280 C80 240 70 200 40 150 C20 110 30 60 60 40 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M230 60 C280 40 340 50 380 90 C400 130 380 150 350 160 C330 200 320 250 290 280 C270 270 260 220 250 180 C230 150 210 130 214 100 C200 90 210 70 230 60 Z" fill="#e8c27a" stroke="#1f2430" stroke-width="5"/><path d="M190 120 l20 0 M200 110 l10 10 l-10 10" stroke="#e04848" stroke-width="5" fill="none"/>')
# radiation: wavy lines from the Sun to Earth
science-6-thermal-energy/radiation = row(sun(130), raw(170, 120, ''.join(f'<path d="M10 {y} q20 -16 40 0 t40 0 t40 0" fill="none" stroke="#e04848" stroke-width="6"/><path d="M146 {y} l-16 -10 v20 z" fill="#e04848"/>' for y in (30, 60, 90))), raw(130, 130, '<circle cx="65" cy="65" r="58" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><path d="M40 45 c15 -20 40 -5 40 10 c0 15 -20 25 -35 15 z" fill="#2f9e5b"/>'), gap=6)
# air mass: a big blue arrow over a map
science-6-water-cycle-and-weather/air-mass = over(us_map(420, color=GREEN), raw(420, 260, '<path d="M60 70 H300" stroke="#3a7bd5" stroke-width="40" stroke-linecap="round" opacity="0.8"/><path d="M360 70 l-60 -40 v80 z" fill="#3a7bd5" opacity="0.8"/>'), dx=0, dy=0)
# front: cold air pushing into warm air; the blue line with triangles is the cold front
science-6-water-cycle-and-weather/front = raw(440, 230, '<rect x="5" y="5" width="215" height="220" fill="#d6e6fb"/><rect x="220" y="5" width="215" height="220" fill="#fbdada"/><line x1="220" y1="5" x2="220" y2="225" stroke="#3a7bd5" stroke-width="8"/>' + ''.join(f'<path d="M220 {y - 22} L256 {y} L220 {y + 22} Z" fill="#3a7bd5"/>' for y in (45, 115, 185)) + '<text x="110" y="122" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" text-anchor="middle" fill="#3a7bd5">cold air</text><text x="340" y="122" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" text-anchor="middle" fill="#e04848">warm air</text><line x1="70" y1="170" x2="150" y2="170" stroke="#3a7bd5" stroke-width="7"/><path d="M170 170 l-22 -12 v24 z" fill="#3a7bd5"/>')
# atom: a nucleus with orbiting dots
science-7-atoms-and-molecules/atom = atom(300, shells=(2, 3))
# molecule: one big ball with two small balls attached
science-7-atoms-and-molecules/molecule = molecule(300)
# periodic table: a grid of element boxes
science-7-atoms-and-molecules/periodic-table = raw(440, 260, ''.join(f'<rect x="{10 + c * 23}" y="{10 + r * 34}" width="21" height="32" rx="3" fill="{["#fde3c8", "#fde97a", "#d3f0de", "#d6e6fb", "#ead7f7"][c // 4 % 5]}" stroke="#1f2430" stroke-width="2"/>' for r in range(7) for c in range(18) if r > 2 or c in (0, 17) or (r > 0 and (c < 2 or c > 11))))
# product: an arrow pointing to CO₂
science-7-chemical-reactions/product = row(arrow(120, DARK, sw=10), molecule(220, atoms=(('C', '#3b4256', 0, 0, 28), ('O', RED, -50, 0, 24), ('O', RED, 50, 0, 24)), bonds=((0, 1), (0, 2))), gap=14)
# conservation of mass: a balanced scale with a sealed flask
science-7-chemical-reactions/conservation-of-mass = col(raw(150, 150, '<path d="M50 10 H100 V30 H95 V60 L140 130 Q145 145 130 145 H20 Q5 145 10 130 L55 60 V30 H50 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="48" y="2" width="54" height="16" rx="4" fill="#e04848"/>'), scale_icon(300, tilt=0), gap=-50)
# groundwater: soil layers with water below
science-7-earth-s-resources/groundwater = layers(4, 320, water_=True)
# succession: bare ground, grass, shrubs, then trees
science-7-ecosystem-change-and-biodiversity/succession = row(raw(90, 90, '<rect x="5" y="60" width="80" height="25" fill="#a0724a"/>'), arrow(30), raw(90, 90, '<rect x="5" y="60" width="80" height="25" fill="#a0724a"/><path d="M15 60 l5 -20 l5 20 M35 60 l5 -24 l5 24 M55 60 l5 -18 l5 18" stroke="#2f9e5b" stroke-width="5" fill="none"/>'), arrow(30), raw(90, 90, '<rect x="5" y="60" width="80" height="25" fill="#a0724a"/><circle cx="30" cy="44" r="18" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/><circle cx="60" cy="40" r="22" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/>'), arrow(30), tree(110), gap=4, align='b')
# food web: a food web: arrows point from each food to the animal that eats it
science-7-matter-and-energy-in-ecosystems/food-web = web({'plants': (210, 305, GREEN), 'mouse': (95, 205, ORANGE), 'rabbit': (325, 205, ORANGE), 'snake': (95, 50, BROWN), 'owl': (325, 50, PURPLE)}, [('plants', 'mouse'), ('plants', 'rabbit'), ('mouse', 'snake'), ('mouse', 'owl'), ('rabbit', 'owl'), ('snake', 'owl')], 400)
# energy pyramid: a stacked triangle with four levels
science-7-matter-and-energy-in-ecosystems/energy-pyramid = pyramid_levels(4, 320)
# carbon cycle: carbon moves from the air into a tree, into the soil and back to the air
science-7-matter-and-energy-in-ecosystems/carbon-cycle = cycle(['air', 'tree', 'soil'], r=140, colors=[BLUE, GREEN, BROWN])
# cellular respiration: sugar and oxygen arrows into a cell
science-7-photosynthesis-and-respiration/cellular-respiration = row(col(T('sugar', 34, ORANGE), arrow(80, ORANGE, sw=8), T('O₂', 34, BLUE), arrow(80, BLUE, sw=8), gap=2), cell(220, color=PURPLE), gap=8)
# chloroplast: a plant cell with one chloroplast circled
science-7-photosynthesis-and-respiration/chloroplast = col(cell(320, plant=True, focus='chloroplast'), T('chloroplast', 34, GREEN), gap=6)
# glucose: a hexagon ring molecule
science-7-photosynthesis-and-respiration/glucose = raw(260, 260, '<polygon points="130,30 216,80 216,180 130,230 44,180 44,80" fill="#fde97a" stroke="#1f2430" stroke-width="7"/><text x="130" y="145" font-family="Segoe UI" font-size="42" font-weight="700" text-anchor="middle" fill="#1f2430">O</text>')
# carbon dioxide: CO₂ bubbles entering a leaf
science-7-photosynthesis-and-respiration/carbon-dioxide = row(col(*[raw(60, 60, '<circle cx="30" cy="30" r="24" fill="#d6e6fb" stroke="#8a8f9c" stroke-width="4"/><text x="30" y="38" font-family="Segoe UI" font-size="18" font-weight="700" text-anchor="middle" fill="#1f2430">CO₂</text>') for _ in range(3)], gap=6), arrow(60, GRAY), raw(200, 140, '<path d="M10 70 C40 10 150 0 190 70 C150 140 40 130 10 70 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M10 70 H170" stroke="#1f2430" stroke-width="4"/>'), gap=8)
# mitochondria: bean-shaped organelles with folds
science-7-photosynthesis-and-respiration/mitochondria = row(raw(200, 110, '<ellipse cx="100" cy="55" rx="92" ry="48" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><path d="M24 55 Q40 20 56 55 T88 55 T120 55 T152 55 T176 55" fill="none" stroke="#1f2430" stroke-width="5"/>'), raw(160, 90, '<ellipse cx="80" cy="45" rx="74" ry="38" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><path d="M20 45 Q34 18 48 45 T76 45 T104 45 T132 45 T146 45" fill="none" stroke="#1f2430" stroke-width="5"/>'), gap=16)
# particle motion: dots with motion lines in a box
science-7-states-of-matter/particle-motion = raw(320, 280, '<rect x="10" y="10" width="300" height="260" rx="10" fill="#f4f5f7" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="#3a7bd5"/><path d="M{x - 22} {y - 6} h-24 M{x - 22} {y + 6} h-18" stroke="#8a8f9c" stroke-width="4" stroke-linecap="round"/>' for x, y in ((100, 60), (230, 80), (140, 150), (260, 190), (90, 220), (200, 240))))
# magnetic field: curved lines around a bar magnet
science-8-electric-and-magnetic-forces/magnetic-field = field_lines(340, 'magnet')
# charge: a plus and minus pulling together
science-8-electric-and-magnetic-forces/charge = row(charge('+', 110), arrow(50, GREEN), arrow(50, GREEN, 'left'), charge('−', 110), gap=6)
# repel: two magnets pushing apart
science-8-electric-and-magnetic-forces/repel = row(arrow(40, RED, 'left'), magnet(180, flip=True), Item(40, 10, ''), magnet(180), arrow(40, RED), gap=6)
# electric field: arrows radiating from a plus sign
science-8-electric-and-magnetic-forces/electric-field = field_lines(320, 'plus')
# optimize: a curve with its peak marked
science-8-engineering-design/optimize = plot(lambda x: -0.3 * (x - 5) ** 2 + 7, size=320, xr=(0, 10), yr=(0, 9), points=[(5, 7, RED)])
# iterate: a circular arrow with steps
science-8-engineering-design/iterate = cycle(['plan', 'build', 'test', 'improve'], r=140)
# fossil record: rock layers with fossils at different depths
science-8-evolution-and-natural-selection/fossil-record = layers(5, 320, fossils=((0, 90), (2, 200), (4, 140)))
# homologous structures: a bat wing and an arm skeleton side by side
science-8-evolution-and-natural-selection/homologous-structures = paint('a bat wing, a whale flipper and a cat front leg side by side, matching bones colored the same in each')
# force: an arrow pushing a box
science-8-forces-and-motion/force = row(arrow(140, RED, sw=16), crate(150), gap=4)
# net force: two equal arrows pushing opposite ways
science-8-forces-and-motion/net-force = row(arrow(110, RED, sw=14), crate(130), arrow(110, RED, 'left', sw=14), gap=4)
# acceleration: a car moving faster and faster: the gaps between its places grow
science-8-forces-and-motion/acceleration = row(*sum(([Item(gp, 10, ''), raw(c.w, c.h, f'<g opacity="{op}">{c.svg}</g>')] for gp, op, c in ((0, 0.25, car(110, RED)), (12, 0.45, car(110, RED)), (40, 0.7, car(110, RED)), (84, 1, car(110, RED)))), []), gap=0, align='b')
# speed: a speedometer
science-8-kinetic-and-potential-energy/speed = meter(320, 0.75)
# greenhouse gas: heat arrows bouncing under a layer
science-8-natural-hazards-and-human-impact/greenhouse-gas = raw(420, 300, '<path d="M10 90 Q210 50 410 90" fill="none" stroke="#8a8f9c" stroke-width="18" opacity="0.6"/><circle cx="60" cy="40" r="30" fill="#f5c524" stroke="#1f2430" stroke-width="4"/><path d="M80 60 L180 270" stroke="#f5c524" stroke-width="7"/><path d="M180 270 L250 110" stroke="#e04848" stroke-width="7"/><path d="M250 110 L310 250" stroke="#e04848" stroke-width="7"/><path d="M318 268 l-2 -24 l-16 10 z" fill="#e04848"/><rect x="0" y="270" width="420" height="30" fill="#2f9e5b"/>')
# gene: a highlighted segment on a DNA strand
science-8-reproduction-and-heredity/gene = dna(380, hl=(4, 7))
# mutation: a DNA ladder with one rung changed
science-8-reproduction-and-heredity/mutation = dna(380, changed=5)
# Punnett square: a 2 by 2 grid with letters
science-8-reproduction-and-heredity/punnett-square = table(cells=[['', 'B', 'b'], ['B', 'BB', 'Bb'], ['b', 'Bb', 'bb']], size=320)
# amplitude: a wave with its height marked
science-8-waves/amplitude = wave(380, 2, marks='amplitude')
# wavelength: a wave with crest-to-crest bracket
science-8-waves/wavelength = wave(400, 2, marks='wavelength')
# frequency: tightly packed waves
science-8-waves/frequency = wave(400, 6, amp=0.8)
# reflection: a wave bouncing off a wall
science-8-waves/reflection = raw(400, 240, '<rect x="340" y="10" width="50" height="220" fill="#8a8f9c" stroke="#1f2430" stroke-width="5"/><path d="M20 70 q25 -30 50 0 t50 0 t50 0 t50 0 t50 0" fill="none" stroke="#3a7bd5" stroke-width="7"/><path d="M330 70 l-14 -10 v20 z" fill="#3a7bd5"/><path d="M320 170 q-25 -30 -50 0 t-50 0 t-50 0 t-50 0 t-50 0" fill="none" stroke="#f08a24" stroke-width="7"/><path d="M60 170 l14 -10 v20 z" fill="#f08a24"/>')
# digital signal: a square stepped wave
science-8-waves/digital-signal = wave(400, cycles=3, square=True, color=BLUE)
# mitosis: one cell splitting into two
science-9-cell-division-and-differentiation/mitosis = flow(cell(150, color=PINK), row(cell(110, color=PINK), cell(110, color=PINK), gap=10))
# cell cycle: the cell cycle: grow, copy DNA, grow more, divide, then around again
science-9-cell-division-and-differentiation/cell-cycle = cycle(['grow', 'copy DNA', 'grow more', 'divide'], r=150, colors=[GREEN, BLUE, ORANGE, PURPLE])
# chromosome: an X-shaped chromosome
science-9-cell-division-and-differentiation/chromosome = chromosome(220)
# differentiation: one cell branching into several types
science-9-cell-division-and-differentiation/differentiation = row(cell(130, color=YELLOW), col(arrow(70), arrow(70), arrow(70), gap=40), col(neuron(150), cell(100, color=RED, organelles=False, nucleus_=False), cell(110, rod=True, color=PINK), gap=16), gap=14)
# stem cell: a round cell with arrows to different shapes
science-9-cell-division-and-differentiation/stem-cell = row(cell(150, color=YELLOW, organelles=False), col(arrow(70), arrow(70), gap=60), col(shape('star', 90, ORANGE), shape('triangle', 90, GREEN), gap=20), gap=14)
# cancer: a cluster of crowded cells
science-9-cell-division-and-differentiation/cancer = raw(320, 260, ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#f6c3d0" stroke="#1f2430" stroke-width="4"/><circle cx="{x}" cy="{y}" r="{r * 0.4:.1f}" fill="#7a3fa0"/>' for x, y, r in ((90, 90, 46), (160, 70, 40), (230, 100, 48), (120, 160, 44), (200, 170, 46), (270, 180, 38), (60, 180, 36), (150, 225, 32), (240, 240, 30))))
# organelle: a cell with labeled organelles
science-9-cell-structure-and-function/organelle = cell(320)
# prokaryote: a simple rod-shaped cell
science-9-cell-structure-and-function/prokaryote = cell(320, rod=True, color=PINK)
# eukaryote: a cell with a nucleus
science-9-cell-structure-and-function/eukaryote = cell(320, organelles=False, color=BLUE)
# selectively permeable: a membrane letting small dots pass, blocking big ones
science-9-cell-structure-and-function/selectively-permeable = raw(380, 260, '<rect x="180" y="0" width="22" height="260" rx="6" fill="#f08a24" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="10" fill="#3a7bd5"/>' for x, y in ((60, 50), (110, 120), (70, 200), (260, 80), (320, 170), (190, 140))) + ''.join(f'<circle cx="{x}" cy="{y}" r="34" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' for x, y in ((80, 130), (130, 210))) + '<path d="M140 140 H230" stroke="#2f9e5b" stroke-width="6"/><path d="M244 140 l-16 -10 v20 z" fill="#2f9e5b"/>')
# ribosome: two small blobs on a strand
science-9-cell-structure-and-function/ribosome = raw(400, 180, '<path d="M10 120 C80 100 140 140 210 120 C280 100 340 140 390 120" fill="none" stroke="#9b5de5" stroke-width="7"/><ellipse cx="200" cy="96" rx="58" ry="36" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><ellipse cx="200" cy="140" rx="74" ry="34" fill="#f5b85c" stroke="#1f2430" stroke-width="5"/>')
# specialized cell: a long branching nerve cell
science-9-cell-structure-and-function/specialized-cell = neuron(400)
# greenhouse effect: heat arrows trapped under a layer
science-9-climate-systems/greenhouse-effect = raw(400, 300, '<rect x="0" y="230" width="400" height="70" fill="#5fbf4a" stroke="#1f2430" stroke-width="4"/><path d="M0 70 Q200 20 400 70" fill="none" stroke="#8a8f9c" stroke-width="18" opacity="0.7"/><circle cx="62" cy="28" r="24" fill="#f5c524" stroke="#1f2430" stroke-width="4"/>' + '<path d="M80 0 L150 220" stroke="#f5c524" stroke-width="8"/><path d="M150 220 L230 70 L280 220 L330 80" fill="none" stroke="#e04848" stroke-width="7" stroke-dasharray="12 8"/><path d="M330 80 l-2 22 l18 -12 z" fill="#e04848"/>')
# climate model: a globe with a grid
science-9-climate-systems/climate-model = globe(300, grid_=True)
# radiative balance: equal arrows in and out of Earth
science-9-climate-systems/radiative-balance = row(col(arrow(100, color=YELLOW, dir='down', sw=12), T('in', 32), gap=6), earth(180), col(arrow(100, color=RED, dir='up', sw=12), T('out', 32), gap=6), gap=24)
# DNA: a double helix
science-9-dna-and-protein-synthesis/dna = raw(420, 220, ''.join(f'<line x1="{20 + i * 34}" y1="{110 + 70 * math.sin((20 + i * 34) / 380 * 4 * math.pi):.1f}" x2="{20 + i * 34}" y2="{110 - 70 * math.sin((20 + i * 34) / 380 * 4 * math.pi):.1f}" stroke="{('#f08a24', '#2f9e5b', '#e04848', '#f5c524')[i % 4]}" stroke-width="7"/>' for i in range(12)) + ''.join('<path d="M' + ' L'.join(f'{x} {110 + s * 70 * math.sin(x / 380 * 4 * math.pi):.1f}' for x in range(10, 411, 5)) + f'" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"/>' for s, c in ((1, '#3a7bd5'), (-1, '#9b5de5'))))
# transcription: a DNA strand with an RNA copy peeling off
science-9-dna-and-protein-synthesis/transcription = col(raw(420, 220, ''.join(f'<line x1="{20 + i * 34}" y1="{110 + 70 * math.sin((20 + i * 34) / 380 * 4 * math.pi):.1f}" x2="{20 + i * 34}" y2="{110 - 70 * math.sin((20 + i * 34) / 380 * 4 * math.pi):.1f}" stroke="{('#f08a24', '#2f9e5b', '#e04848', '#f5c524')[i % 4]}" stroke-width="7"/>' for i in range(12)) + ''.join('<path d="M' + ' L'.join(f'{x} {110 + s * 70 * math.sin(x / 380 * 4 * math.pi):.1f}' for x in range(10, 411, 5)) + f'" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"/>' for s, c in ((1, '#3a7bd5'), (-1, '#9b5de5')))), raw(420, 60, '<path d="M20 30 C110 10 170 50 250 20 C300 4 340 30 380 40" fill="none" stroke="#f08a24" stroke-width="9" stroke-linecap="round"/><path d="M408 46 l-26 6 l8 -22 z" fill="#f08a24"/>'), gap=0)
# translation: a ribosome reading a strand and building a chain
science-9-dna-and-protein-synthesis/translation = raw(420, 240, '<path d="M10 170 H410" stroke="#9b5de5" stroke-width="7"/><ellipse cx="200" cy="146" rx="62" ry="38" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><ellipse cx="200" cy="190" rx="78" ry="34" fill="#f5b85c" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{200 - i * 10}" cy="{100 - i * 30}" r="14" fill="{c}" stroke="#1f2430" stroke-width="3"/>' for i, c in enumerate(('#3a7bd5', '#2f9e5b', '#e04848', '#f5c524'))))
# codon: three letter tiles A U G
science-9-dna-and-protein-synthesis/codon = tiles('A', 'U', 'G', colors=(GREEN, ORANGE, BLUE), size=110)
# amino acid: a chain of colored beads
science-9-dna-and-protein-synthesis/amino-acid = raw(440, 80, '<line x1="20" y1="40" x2="420" y2="40" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<circle cx="{40 + i * 60}" cy="40" r="26" fill="{c}" stroke="#1f2430" stroke-width="4"/>' for i, c in enumerate(('#3a7bd5', '#2f9e5b', '#e04848', '#f5c524', '#9b5de5', '#f08a24', '#3a7bd5'))))
# base pair: a ladder rung with A and T
science-9-dna-and-protein-synthesis/base-pair = raw(400, 160, '<line x1="20" y1="20" x2="380" y2="20" stroke="#3a7bd5" stroke-width="12"/><line x1="20" y1="140" x2="380" y2="140" stroke="#9b5de5" stroke-width="12"/><rect x="60" y="26" width="140" height="108" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><rect x="200" y="26" width="140" height="108" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><text x="130" y="100" font-family="Segoe UI" font-size="60" font-weight="700" text-anchor="middle" fill="#fff">A</text><text x="270" y="100" font-family="Segoe UI" font-size="60" font-weight="700" text-anchor="middle" fill="#fff">T</text>')
# feedback loop: a circular arrow with labels
science-9-earth-s-systems-and-feedback/feedback-loop = cycle(['cause', 'effect', 'change'], r=130)
# mantle convection: loops of arrows inside Earth
science-9-earth-s-systems-and-feedback/mantle-convection = raw(340, 340, '<circle cx="170" cy="170" r="160" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><circle cx="170" cy="170" r="60" fill="#e04848" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<path d="M{a} C{b}" fill="none" stroke="#fff" stroke-width="7"/>' for a, b in (('170 100', '120 60 60 90 60 170 S120 250 170 240', ), ('170 100', '220 60 280 90 280 170 S220 250 170 240'))) + '<path d="M60 160 l-10 20 l22 -4 z M280 160 l10 20 l-22 -4 z" fill="#fff"/>')
# carrying capacity: a curve leveling off at a dashed line
science-9-ecology-and-populations/carrying-capacity = plot(lambda x: 8 / (1 + math.exp(-1.4 * (x - 4))), xr=(0, 10), yr=(0, 10), hlines=(8,), colors=(GREEN,))
# trophic level: a stacked pyramid
science-9-ecology-and-populations/trophic-level = pyramid_levels(4, 320)
# logistic growth: an S-shaped curve
science-9-ecology-and-populations/logistic-growth = plot(lambda x: 8 / (1 + math.exp(-1.4 * (x - 4))), xr=(0, 10), yr=(0, 10), colors=(BLUE,))
# density-dependent factor: crowded dots with a warning sign
science-9-ecology-and-populations/density-dependent-factor = row(raw(220, 220, '<rect x="5" y="5" width="210" height="210" rx="10" fill="#fff" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{20 + (i * 37) % 190}" cy="{20 + (i * 53) % 190}" r="9" fill="#3a7bd5"/>' for i in range(60))), warning(120), gap=20)
# biomass: a pyramid of stacked blocks
science-9-ecology-and-populations/biomass = pyramid_levels(4, 320, blocks=True)
# common ancestry: a branching tree
science-9-evolution/common-ancestry = branch_tree(340, leaves=4)
# cladogram: a branching cladogram
science-9-evolution/cladogram = branch_tree(340, leaves=4, cladogram=True)
# vestigial structure: a small tailbone on a spine
science-9-evolution/vestigial-structure = raw(160, 340, ''.join(f'<rect x="{60 - i * 0.6:.1f}" y="{10 + i * 30}" width="{40 + i * 1.2:.1f}" height="24" rx="8" fill="#f4efe2" stroke="#1f2430" stroke-width="4"/>' for i in range(9)) + ''.join(f'<rect x="{68 + j * 2}" y="{282 + j * 14}" width="{24 - j * 4}" height="12" rx="5" fill="#f08a24" stroke="#1f2430" stroke-width="3"/>' for j in range(3)))
# genetic drift: marbles randomly chosen from a jar
science-9-evolution/genetic-drift = row(raw(160, 220, '<path d="M30 30 V190 Q30 210 50 210 H110 Q130 210 130 190 V30" fill="#eef3fa" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{50 + (i % 4) * 20}" cy="{190 - (i // 4) * 22}" r="9" fill="{"#e04848" if i % 3 else "#3a7bd5"}" stroke="#1f2430" stroke-width="2"/>' for i in range(24))), arrow(70), raw(120, 60, ''.join(f'<circle cx="{20 + i * 26}" cy="30" r="10" fill="{c}" stroke="#1f2430" stroke-width="2"/>' for i, c in enumerate(('#e04848', '#e04848', '#e04848', '#3a7bd5')))), gap=14)
# meiosis: one cell dividing into four
science-9-genetics-and-inheritance/meiosis = row(cell(150, color=PINK), arrow(60), grid([cell(80, color=PINK, organelles=False) for _ in range(4)], 2, gap=10), gap=16)
# genotype: two letters B and b
science-9-genetics-and-inheritance/genotype = tiles('B', 'b', colors=(BLUE, ORANGE), size=130)
# dominant: Bb: the dominant B shows, the faded b is hidden, so the eye is brown
science-9-genetics-and-inheritance/dominant = row(T('Bb', 150, hl={'b': '#c9ced8'}), arrow(60), eye(160, color=BROWN), gap=12)
# recessive: lowercase b b
science-9-genetics-and-inheritance/recessive = tiles('b', 'b', colors=(ORANGE, ORANGE), size=130)
# crossing over: two chromosomes exchanging segments
science-9-genetics-and-inheritance/crossing-over = raw(300, 260, '<path d="M60 20 V240" stroke="#3a7bd5" stroke-width="30" stroke-linecap="round"/><path d="M240 20 V240" stroke="#e04848" stroke-width="30" stroke-linecap="round"/><path d="M60 170 V240" stroke="#e04848" stroke-width="30" stroke-linecap="round"/><path d="M240 170 V240" stroke="#3a7bd5" stroke-width="30" stroke-linecap="round"/><path d="M90 150 C130 120 170 180 210 150" fill="none" stroke="#1f2430" stroke-width="5" stroke-dasharray="8 6"/>')
# homeostasis: a thermostat set to 37°C
science-9-homeostasis/homeostasis = col(thermometer(200, level=0.6), T('37°C', 60), gap=10)
# negative feedback: a loop with a minus sign
science-9-homeostasis/negative-feedback = curve_arrow(110, color=BLUE, start=-80, end=240, inner=T('−', 120, color=BLUE))
# positive feedback: a loop with a plus sign
science-9-homeostasis/positive-feedback = curve_arrow(110, color=RED, start=-80, end=240, inner=T('+', 110, color=RED))
# insulin: a key unlocking a cell
science-9-homeostasis/insulin = row(key(140), arrow(60), cell(170, color=PINK), gap=16)
# stimulus: bright light (the stimulus) makes the pupil shrink
science-9-homeostasis/stimulus = col(sun(100), row(eye(150, pupil=0.4), arrow(60), eye(150, pupil=0.15), gap=12), gap=10)
# Kepler's laws: an ellipse with the Sun at one focus
science-9-orbits-and-earth-s-history/kepler-s-laws = orbit(360, center=sun(70), body=earth(40), ellipse_=True, foci=True)
# ellipse: an ellipse with two dots inside
science-9-orbits-and-earth-s-history/ellipse = raw(380, 240, '<ellipse cx="190" cy="120" rx="170" ry="100" fill="none" stroke="#3a7bd5" stroke-width="8"/><circle cx="110" cy="120" r="12" fill="#e04848"/><circle cx="270" cy="120" r="12" fill="#e04848"/>')
# radiometric dating: a decay curve halving each step
science-9-orbits-and-earth-s-history/radiometric-dating = plot(lambda x: 8 * 0.5 ** (x / 2), xr=(0, 10), yr=(0, 10), points=((0, 8), (2, 4), (4, 2), (6, 1)), colors=(PURPLE,))
# half-life: a bar halving three times
science-9-orbits-and-earth-s-history/half-life = col(*[raw(400, 50, f'<rect x="5" y="5" width="{390 / 2 ** i:.1f}" height="40" rx="6" fill="#9b5de5" stroke="#1f2430" stroke-width="4"/>') for i in range(4)], gap=10, align='l')
# seafloor spreading: a ridge with arrows pointing outward
science-9-orbits-and-earth-s-history/seafloor-spreading = raw(440, 200, '<rect x="0" y="110" width="440" height="90" fill="#a0724a"/><path d="M0 110 H180 L210 70 L230 70 L260 110 H440" fill="#3a3f4c" stroke="#1f2430" stroke-width="4"/><path d="M220 120 V200" stroke="#e04848" stroke-width="10"/><path d="M190 40 H60" stroke="#e04848" stroke-width="9"/><path d="M40 40 l24 -14 v28 z" fill="#e04848"/><path d="M250 40 H380" stroke="#e04848" stroke-width="9"/><path d="M400 40 l-24 -14 v28 z" fill="#e04848"/>')
# ATP: a molecule with three phosphate beads
science-9-photosynthesis-and-cellular-respiration/atp = raw(420, 180, '<path d="M30 90 L80 50 L130 90 L80 130 Z" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><path d="M130 90 H330" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<circle cx="{190 + i * 70}" cy="90" r="30" fill="#f5c524" stroke="#1f2430" stroke-width="5"/><text x="{190 + i * 70}" y="102" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#1f2430">P</text>' for i in range(3)))
# macromolecule: a long chain of linked units
science-9-photosynthesis-and-cellular-respiration/macromolecule = raw(440, 120, ''.join(f'<rect x="{10 + i * 54}" y="35" width="44" height="50" rx="10" fill="{("#3a7bd5", "#2f9e5b", "#f08a24")[i % 3]}" stroke="#1f2430" stroke-width="4"/>' for i in range(8)) + ''.join(f'<line x1="{54 + i * 54}" y1="60" x2="{64 + i * 54}" y2="60" stroke="#1f2430" stroke-width="6"/>' for i in range(7)))
# enzyme: a lock-and-key shape
science-9-photosynthesis-and-cellular-respiration/enzyme = puzzle(240, fits=True)
# light-dependent reactions: sunlight hitting a stack of discs
science-9-photosynthesis-and-cellular-respiration/light-dependent-reactions = row(sun(110), col(arrow(70, color=YELLOW, sw=10), gap=0), raw(140, 200, ''.join(f'<ellipse cx="70" cy="{30 + i * 34}" rx="60" ry="15" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/>' for i in range(5))), gap=14)
# Calvin cycle: CO₂ goes into a loop that builds sugar
science-9-photosynthesis-and-cellular-respiration/calvin-cycle = row(M('CO₂', 60), arrow(46), box(curve_arrow(60, color=DARK, start=-80, end=240), color=GREEN, rx=100, p=24), arrow(46), col(poly(6, 90, ORANGE), T('sugar', 28), gap=4), gap=8)
# aquifer: an underground layer filled with water
science-9-resources-and-sustainability/aquifer = layers(4, 340, colors=('#7bc96f', '#c98b4f', '#9cc3e8', '#8f6a4f'), water_=True)
# cost-benefit analysis: a scale with coins and a leaf
science-9-resources-and-sustainability/cost-benefit-analysis = scale_icon(300, left=coin(50), right=tree(60))
# hazard map: a map with shaded risk zones
science-9-resources-and-sustainability/hazard-map = raw(320, 260, '<rect x="5" y="5" width="310" height="250" rx="10" fill="#e9f3dc" stroke="#1f2430" stroke-width="5"/><path d="M5 120 C80 90 120 170 200 140 C260 120 290 160 315 150 V255 H5 Z" fill="#f5c524" opacity="0.7"/><path d="M5 190 C80 170 140 230 200 210 C260 190 290 220 315 215 V255 H5 Z" fill="#e04848" opacity="0.8"/>')
# Big Bang: a burst of expanding dots
science-9-stars-and-the-big-bang/big-bang = raw(320, 320, ''.join(f'<circle cx="{160 + r * math.cos(a):.1f}" cy="{160 + r * math.sin(a):.1f}" r="{4 + r / 30:.1f}" fill="{("#f5c524", "#f08a24", "#e04848", "#9b5de5")[int(r / 40) % 4]}"/>' for r in range(20, 150, 30) for a in [k * 0.55 + r * 0.01 for k in range(12)]) + ''.join(f'<path d="M{160 + 40 * math.cos(a):.1f} {160 + 40 * math.sin(a):.1f} L{160 + 150 * math.cos(a):.1f} {160 + 150 * math.sin(a):.1f}" stroke="#f08a24" stroke-width="3" opacity="0.5"/>' for a in [k * 0.785 for k in range(8)]) + '<circle cx="160" cy="160" r="20" fill="#fff4b0" stroke="#f5c524" stroke-width="5"/>')
# redshift: a spectrum with lines shifted toward red
science-9-stars-and-the-big-bang/redshift = raw(420, 230, ''.join(f'<rect x="{10 + i * 57}" y="{y}" width="57" height="60" fill="{c}"/>' for y in (10, 110) for i, c in enumerate(('#9b5de5', '#3a4fc0', '#3a7bd5', '#2f9e5b', '#f5c524', '#f08a24', '#e04848'))) + ''.join(f'<rect x="{x}" y="{y}" width="7" height="60" fill="#1f2430"/>' for y, xs in ((10, (90, 170, 250)), (110, (140, 220, 300))) for x in xs) + '<rect x="10" y="10" width="399" height="60" fill="none" stroke="#1f2430" stroke-width="4"/><rect x="10" y="110" width="399" height="60" fill="none" stroke="#1f2430" stroke-width="4"/><path d="M140 205 H330" stroke="#e04848" stroke-width="9"/><path d="M352 205 l-26 -15 v30 z" fill="#e04848"/>')
# main sequence: a diagonal band on a star chart
science-9-stars-and-the-big-bang/main-sequence = raw(320, 300, '<path d="M30 10 V270 H310" fill="none" stroke="#1f2430" stroke-width="5"/><path d="M60 40 C120 90 200 180 290 250" fill="none" stroke="#f5c524" stroke-width="34" stroke-linecap="round" opacity="0.6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y, r, c in ((60, 40, 14, "#3a7bd5"), (120, 90, 11, "#8fb8f0"), (180, 150, 10, "#fff4b0"), (230, 200, 9, "#f5c524"), (280, 245, 8, "#e04848"), (250, 60, 18, "#e04848"), (100, 240, 6, "#fff")) ) + '<circle cx="100" cy="240" r="6" fill="none" stroke="#1f2430" stroke-width="2"/>')
# cosmic microwave background: an oval sky map with mottled spots
science-9-stars-and-the-big-bang/cosmic-microwave-background = raw(420, 230, '<defs><clipPath id="cmb"><ellipse cx="210" cy="115" rx="200" ry="105"/></clipPath></defs><ellipse cx="210" cy="115" rx="200" ry="105" fill="#3a7bd5"/>' + '<g clip-path="url(#cmb)">' + ''.join(f'<circle cx="{(i * 67) % 420}" cy="{(i * 41) % 230}" r="{14 + (i * 7) % 18}" fill="{("#e04848", "#f5c524", "#8fb8f0", "#f08a24")[i % 4]}" opacity="0.75"/>' for i in range(70)) + '</g><ellipse cx="210" cy="115" rx="200" ry="105" fill="none" stroke="#1f2430" stroke-width="5"/>')
# polarity: a water molecule with + and − ends
science-9-water-and-earth-materials/polarity = raw(340, 260, '<circle cx="170" cy="150" r="70" fill="#e04848" stroke="#1f2430" stroke-width="5"/><circle cx="70" cy="80" r="44" fill="#fff" stroke="#1f2430" stroke-width="5"/><circle cx="270" cy="80" r="44" fill="#fff" stroke="#1f2430" stroke-width="5"/><text x="170" y="250" font-family="Segoe UI" font-size="56" font-weight="700" text-anchor="middle" fill="#e04848">−</text><text x="70" y="40" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#3a7bd5">+</text><text x="270" y="40" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#3a7bd5">+</text><text x="170" y="168" font-family="Segoe UI" font-size="48" font-weight="700" text-anchor="middle" fill="#fff">O</text><text x="70" y="96" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">H</text><text x="270" y="96" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#1f2430">H</text>')
# solvent: sugar dissolving in water
science-9-water-and-earth-materials/solvent = row(flask(220, BLUE, dots=False, level=0.6) if 0 else cup(150), arrow(60), raw(180, 220, '<path d="M20 20 L40 210 H140 L160 20" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><path d="M28 90 H152" stroke="#3a7bd5" stroke-width="4"/>' + ''.join(f'<rect x="{50 + (i * 23) % 80}" y="{110 + (i * 31) % 80}" width="8" height="8" fill="#fff" stroke="#8a8f9c" stroke-width="2"/>' for i in range(10))), gap=14)
# direction: a ball bouncing off a wall with an arrow
science-k-pushes-and-pulls/direction = raw(400, 260, '<rect x="340" y="10" width="40" height="240" fill="#c98b4f" stroke="#1f2430" stroke-width="5"/><circle cx="310" cy="130" r="30" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M40 60 L260 120" stroke="#3a7bd5" stroke-width="8" stroke-dasharray="14 8"/><path d="M276 124 l-26 -16 l-4 26 z" fill="#3a7bd5"/><path d="M270 170 L60 230" stroke="#e04848" stroke-width="9"/><path d="M44 234 l26 -18 l6 26 z" fill="#e04848"/>')
# season: four trees showing spring, summer, fall and winter
science-k-weather-watch/season = row(tree(110, color='#f4a6c0'), tree(110), tree(110, color=ORANGE), tree(110, color='#fff'), gap=10)
# air: swirling lines of wind around a leaf
science-k-what-living-things-need/air = raw(320, 240, '<path d="M160 200 C90 160 110 70 200 40 C230 110 220 180 160 200 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M160 200 C170 140 185 100 200 40" fill="none" stroke="#1f2430" stroke-width="3"/>' + ''.join(f'<path d="{d}" fill="none" stroke="#8fb8f0" stroke-width="7" stroke-linecap="round"/>' for d in ('M10 60 C60 30 100 80 60 100 C40 110 30 90 44 84', 'M20 150 C90 130 120 160 80 190', 'M240 150 C290 130 310 170 280 190 C260 200 250 180 262 176', 'M230 30 C270 10 300 40 290 70')))
# effort: an arrow climbing a mountain
sel-3-5-growth-mindset-and-goals/effort = mountain(320, path=True, flag_=True)
# perspective: two eyes viewing a shape from different sides
sel-3-5-perspective-taking/perspective = row(eye(90), arrow(60), shape('cube', 140, ORANGE) if 0 else cube_icon(140, ORANGE), arrow(60, dir='left'), eye(90), gap=10)
# empathy: two hearts linked
sel-3-5-perspective-taking/empathy = row(heart(140, RED), chain(2, 100), heart(140, PINK), gap=0)
# body language: a simple outline with crossed arms
sel-3-5-perspective-taking/body-language = raw(220, 280, '<circle cx="110" cy="50" r="38" fill="#fff" stroke="#1f2430" stroke-width="5"/><path d="M50 270 V140 C50 110 70 96 110 96 C150 96 170 110 170 140 V270" fill="#fff" stroke="#1f2430" stroke-width="5"/><path d="M40 150 L180 200 M180 150 L40 200" stroke="#1f2430" stroke-width="22" stroke-linecap="round"/><path d="M40 150 L180 200 M180 150 L40 200" stroke="#fff" stroke-width="12" stroke-linecap="round"/>')
# listen: an ear with sound waves
sel-3-5-perspective-taking/listen = ear(260)
# respect: a heart between two people of equal size
sel-3-5-perspective-taking/respect = row(person(150, BLUE), heart(80), person(150, ORANGE), gap=16)
# compromise: two arrows meeting in the middle
sel-6-8-conflict-resolution/compromise = row(arrow(140, color=BLUE), raw(30, 60, '<circle cx="15" cy="30" r="12" fill="#2f9e5b"/>'), arrow(140, color=ORANGE, dir='left'), gap=4)
# active listening: an ear with a check mark
sel-6-8-conflict-resolution/active-listening = row(ear(200, waves=False), check(110), gap=10)
# de-escalate: a downward arrow over a flame
sel-6-8-conflict-resolution/de-escalate = col(arrow(110, color=BLUE, dir='down', sw=12), raw(140, 160, '<path d="M70 150 C20 140 10 90 40 60 C40 90 60 90 60 70 C60 40 80 20 90 0 C100 40 140 60 130 110 C126 140 100 150 70 150 Z" fill="#f08a24" stroke="#1f2430" stroke-width="5"/><path d="M70 150 C50 140 50 110 70 96 C90 110 90 140 70 150 Z" fill="#f5c524"/>'), gap=6)
# mediation: a bridge between two sides
sel-6-8-conflict-resolution/mediation = bridge(360)
# win-win: two trophies side by side
sel-6-8-conflict-resolution/win-win = row(trophy(160), trophy(160, BLUE), gap=24)
# decision: a fork in a road
sel-6-8-responsible-decisions/decision = fork(320)
# consequence: a row of falling dominoes
sel-6-8-responsible-decisions/consequence = raw(440, 200, ''.join(f'<rect x="{30 + i * 70}" y="{40}" width="26" height="140" rx="4" fill="{("#3a7bd5", "#f08a24", "#2f9e5b", "#9b5de5", "#e04848", "#f5c524")[i]}" stroke="#1f2430" stroke-width="4" transform="rotate({min(64, i * 18 if i < 4 else 64)} {56 + i * 70} 180)"/>' for i in range(6))[::-1] if 0 else ''.join(f'<rect x="{40 + i * 64}" y="40" width="24" height="140" rx="4" fill="{c}" stroke="#1f2430" stroke-width="4" transform="rotate({a} {64 + i * 64} 180)"/>' for i, (c, a) in enumerate((("#3a7bd5", 62), ("#f08a24", 50), ("#2f9e5b", 34), ("#9b5de5", 16), ("#e04848", 0), ("#f5c524", 0)))))
# pros and cons: a two-column list with plus and minus
sel-6-8-responsible-decisions/pros-and-cons = table(4, 2, cells=[['+', '−'], ['', ''], ['', ''], ['', '']], size=300, header=True, fs=48)
# values: a compass
sel-6-8-responsible-decisions/values = compass(300)
# impulse: a lightning bolt with a pause sign
sel-6-8-responsible-decisions/impulse = row(raw(120, 180, '<path d="M80 0 L20 100 H60 L30 180 L110 70 H66 L100 0 Z" fill="#f5c524" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), raw(140, 140, '<circle cx="70" cy="70" r="64" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><rect x="44" y="38" width="18" height="64" rx="4" fill="#fff"/><rect x="78" y="38" width="18" height="64" rx="4" fill="#fff"/>'), gap=24)
# ethical: a balanced scale
sel-6-8-responsible-decisions/ethical = scale_icon(300)
# breathe: a balloon getting bigger and smaller
sel-k-2-calm-down-strategies/breathe = row(balloon(90), arrow(50, double=True), balloon(170), gap=16)
# calm down: the numbers 1 to 5 on soft clouds
sel-k-2-calm-down-strategies/calm-down = grid([over(cloud(150), T(str(i), 54)) for i in range(1, 6)], 3, gap=10)
# count: five dots counted 1 to 5
sel-k-2-calm-down-strategies/count = row(*[col(dot(60, ORANGE), T(str(i), 36), gap=4) for i in range(1, 6)], gap=16)
# stretch: two arrows pointing up
# feelings: a row of simple faces
sel-k-2-naming-feelings/feelings = grid([face(120, m) for m in ('happy', 'sad', 'angry', 'scared', 'calm', 'tired')], 3, gap=18)
# language: two speech bubbles with different letters
social-studies-1-cultures-around-the-world/language = row(bubble(T('Aa', 54), 170), bubble(T('あ', 54), 170, color=ORANGE, tail='right'), gap=20)
# custom: a small Japanese flag next to a greeting card
social-studies-1-cultures-around-the-world/custom = row(raw(180, 120, '<rect x="4" y="4" width="172" height="112" fill="#fff" stroke="#1f2430" stroke-width="5"/><circle cx="90" cy="60" r="34" fill="#e04848"/>'), raw(170, 130, '<rect x="5" y="5" width="160" height="120" rx="8" fill="#fde3c8" stroke="#1f2430" stroke-width="5"/><path d="M5 5 L85 70 L165 5" fill="none" stroke="#1f2430" stroke-width="4"/><path d="M85 112 C60 92 66 76 85 86 C104 76 110 92 85 112 Z" fill="#e04848"/>'), gap=24)
# choice: two items with an arrow to one
social-studies-1-goods-and-services/choice = row(col(arrow(70, dir='down', color=GREEN), apple(120), gap=6), col(raw(10, 76, ''), banana(120), gap=6), gap=50)
# map key: a map key box with tree, house and road symbols
social-studies-1-maps-and-globes/map-key = legend_box(300)
# north: a compass with N highlighted
social-studies-1-maps-and-globes/north = compass(300, hl='N')
# south: a compass with S highlighted
social-studies-1-maps-and-globes/south = compass(300, hl='S')
# east and west: a compass with E and W highlighted
social-studies-1-maps-and-globes/east-and-west = compass(300, hl='EW')
# continent: a world map with continents in colors
social-studies-1-maps-and-globes/continent = world_map(440, continents=True)
# timeline: a line with dots and small pictures
social-studies-1-timelines-and-me/timeline = timeline(4, 420, pics=(house(1), star(1), heart(1), tree(1)))
# year: twelve small calendars: one for each month of a year
social-studies-1-timelines-and-me/year = col(grid([calendar(70) for _ in range(12)], 4, gap=8), T('12 months', 36), gap=8)
# before: two dots on a line with the left one circled
social-studies-1-timelines-and-me/before = timeline(2, 380, hl=0)
# after: two dots on a line with the right one circled
social-studies-1-timelines-and-me/after = timeline(2, 380, hl=1)
# neuron: a branching nerve cell
social-studies-12-brain-and-behavior/neuron = neuron(400)
# neurotransmitter: dots crossing a gap between two cells
social-studies-12-brain-and-behavior/neurotransmitter = raw(400, 200, '<path d="M0 60 H140 C170 60 180 70 180 100 C180 130 170 140 140 140 H0" fill="#f6c3d0" stroke="#1f2430" stroke-width="5"/><path d="M400 50 H260 C230 50 220 70 220 100 C220 130 230 150 260 150 H400" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="#f08a24"/>' for x, y in ((190, 80), (200, 105), (196, 125), (208, 90), (212, 116))) + '<path d="M150 30 H240" stroke="#e04848" stroke-width="5"/><path d="M252 30 l-14 -9 v18 z" fill="#e04848"/>')
# synapse: a narrow gap between nerve endings
social-studies-12-brain-and-behavior/synapse = raw(400, 200, '<path d="M0 60 H140 C170 60 180 70 180 100 C180 130 170 140 140 140 H0" fill="#f6c3d0" stroke="#1f2430" stroke-width="5"/><path d="M400 50 H260 C230 50 220 70 220 100 C220 130 230 150 260 150 H400" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><path d="M186 100 H214" stroke="#e04848" stroke-width="4" stroke-dasharray="4 4"/><path d="M186 70 V130 M214 70 V130" stroke="#e04848" stroke-width="4"/>')
# cerebral cortex: a brain with its thin wrinkled outer layer colored
social-studies-12-brain-and-behavior/cerebral-cortex = col(brain(340, cortex=True), T('outer layer', 30, PURPLE), gap=6)
# amygdala: a brain with a small region highlighted
social-studies-12-brain-and-behavior/amygdala = brain(360, hl=True)
# neuroplasticity: new links forming between dots
social-studies-12-brain-and-behavior/neuroplasticity = raw(320, 240, '<line x1="60" y1="60" x2="160" y2="40" stroke="#8a8f9c" stroke-width="6"/><line x1="160" y1="40" x2="260" y2="90" stroke="#8a8f9c" stroke-width="6"/><line x1="60" y1="60" x2="100" y2="190" stroke="#8a8f9c" stroke-width="6"/><line x1="100" y1="190" x2="240" y2="200" stroke="#2f9e5b" stroke-width="8" stroke-dasharray="12 7"/><line x1="160" y1="40" x2="100" y2="190" stroke="#2f9e5b" stroke-width="8" stroke-dasharray="12 7"/><line x1="260" y1="90" x2="240" y2="200" stroke="#8a8f9c" stroke-width="6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#9b5de5" stroke="#1f2430" stroke-width="4"/>' for x, y in ((60, 60), (160, 40), (260, 90), (100, 190), (240, 200))))
# business cycle: a wave with peaks and troughs
social-studies-12-macroeconomics/business-cycle = wave(400, cycles=2, midline=True, color=GREEN)
# production possibilities curve: a curved frontier on a graph
social-studies-12-scarcity-and-choice/production-possibilities-curve = plot(lambda x: (64 - x * x) ** 0.5 if x <= 8 else None, xr=(0, 10), yr=(0, 10), colors=(PURPLE,), points=((4, 5),))
# demand: a downward-sloping line
social-studies-12-supply-and-demand/demand = plot(lambda x: 9 - 0.8 * x, xr=(0, 10), yr=(0, 10), colors=(BLUE,))
# supply: an upward-sloping line
social-studies-12-supply-and-demand/supply = plot(lambda x: 1 + 0.8 * x, xr=(0, 10), yr=(0, 10), colors=(ORANGE,))
# equilibrium price: two lines crossing
social-studies-12-supply-and-demand/equilibrium-price = plot(lambda x: 9 - 0.8 * x, lambda x: 1 + 0.8 * x, xr=(0, 10), yr=(0, 10), colors=(BLUE, ORANGE), points=((5, 5),), hlines=(5,))
# shortage: a gap below equilibrium
social-studies-12-supply-and-demand/shortage = plot(lambda x: 9 - 0.8 * x, lambda x: 1 + 0.8 * x, xr=(0, 10), yr=(0, 10), colors=(BLUE, ORANGE), segs=(((2.5, 3), (7.5, 3), RED, False),), hlines=(3,))
# surplus: a gap above equilibrium
social-studies-12-supply-and-demand/surplus = plot(lambda x: 9 - 0.8 * x, lambda x: 1 + 0.8 * x, xr=(0, 10), yr=(0, 10), colors=(BLUE, ORANGE), segs=(((2.5, 7), (7.5, 7), RED, False),), hlines=(7,))
# brave: a shield with a star
social-studies-2-heroes-and-changemakers/brave = shield(260, inner=star(110))
# fair: a level balance scale
social-studies-2-heroes-and-changemakers/fair = scale_icon(300)
# continent: a world map with each continent in its own color
social-studies-3-communities-around-the-world/continent = world_map(440, continents=True)
# change: a dirt road and the same road paved, side by side
social-studies-3-local-history/change = row(raw(200, 200, '<rect x="0" y="0" width="200" height="200" rx="10" fill="#7bc96f" stroke="#1f2430" stroke-width="5"/><path d="M70 200 L90 0 H110 L130 200 Z" fill="#c9a26b"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#8f6a4f"/>' for x, y in ((100, 40), (95, 100), (112, 150), (104, 180)))), arrow(60), raw(200, 200, '<rect x="0" y="0" width="200" height="200" rx="10" fill="#7bc96f" stroke="#1f2430" stroke-width="5"/><path d="M60 200 L85 0 H115 L140 200 Z" fill="#4a4f5c"/><path d="M100 10 V190" stroke="#f5c524" stroke-width="5" stroke-dasharray="16 12"/>'), gap=14)
# timeline: a timeline with dots and dates
social-studies-3-local-history/timeline = timeline(4, 420, labels=('1900', '1950', '2000', '2025'))
# compass rose: a compass rose marked N, E, S and W
social-studies-3-map-skills-and-regions/compass-rose = compass(300)
# legend: a map legend box with a tree, a house and a road symbol
social-studies-3-map-skills-and-regions/legend = legend_box(300)
# scale: a map scale bar
social-studies-3-map-skills-and-regions/scale = scale_bar(380)
# grid: a map with lettered columns and numbered rows
social-studies-3-map-skills-and-regions/grid = map_tile(340, grid_=True, roads=False, river=True, houses=((40, 30),))
# bill: a document with a check mark stamp
social-studies-4-state-government/bill = col(page(200) if 0 else raw(200, 240, '<rect x="10" y="10" width="180" height="220" rx="8" fill="#fff" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<rect x="34" y="{40 + i * 26}" width="{130 - (i % 2) * 30}" height="9" rx="4" fill="#b8bcc6"/>' for i in range(5)) + '<circle cx="140" cy="186" r="34" fill="none" stroke="#2f9e5b" stroke-width="6"/><path d="M122 186 l12 12 l24 -26" fill="none" stroke="#2f9e5b" stroke-width="7" stroke-linecap="round"/>'), gap=0)
# border: a map with a river as a line between two states
social-studies-4-us-regions-and-states/border = raw(360, 260, '<rect x="5" y="5" width="350" height="250" rx="10" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/><path d="M5 5 H170 C150 80 210 150 180 255 H5 Z" fill="#fde3c8" stroke="#1f2430" stroke-width="3"/><path d="M170 5 C150 80 210 150 180 255" fill="none" stroke="#3a7bd5" stroke-width="14"/>' if 0 else '<rect x="5" y="5" width="350" height="250" rx="10" fill="#d3f0de" stroke="#1f2430" stroke-width="5"/><path d="M5 5 H170 C150 80 210 150 180 255 H5 Z" fill="#fde3c8"/><path d="M170 5 C150 80 210 150 180 255" fill="none" stroke="#3a7bd5" stroke-width="14"/><rect x="5" y="5" width="350" height="250" rx="10" fill="none" stroke="#1f2430" stroke-width="5"/>')
# compass rose: a compass rose with N, S, E, W
social-studies-4-us-regions-and-states/compass-rose = compass(300)
# enslaved: an iron shackle and a heavy unbroken chain
social-studies-5-colonial-economies/enslaved = row(raw(120, 120, '<circle cx="60" cy="66" r="42" fill="none" stroke="#5a5f6c" stroke-width="18"/><rect x="46" y="4" width="28" height="30" rx="4" fill="#5a5f6c" stroke="#1f2430" stroke-width="3"/>'), chain(4, 320, color=DARK), gap=4)
# triangular trade: the triangular trade: ships carried goods to Africa, enslaved Africans to the Americas, and crops back to Europe
social-studies-5-colonial-economies/triangular-trade = world_map(440, view=(-100, -30, 35, 62), flows=[([(-5, 46), (-14, 30), (-12, 12)], BLUE, 14), ([(-16, 9), (-40, 10), (-62, 15)], RED, 14), ([(-72, 28), (-55, 36), (-30, 44), (-10, 48)], GREEN, 14)], labels=[(18, 52, 'Europe', DARK, 24), (20, 6, 'Africa', DARK, 24), (-88, 36, 'Americas', DARK, 24), (-22, 23, 'goods', BLUE, 22), (-38, 4, 'enslaved Africans', RED, 22), (-40, 47, 'sugar, cotton', GREEN, 22)])
# thirteen colonies: a map of the east coast with thirteen shaded areas
social-studies-5-exploration-and-colonization/thirteen-colonies = us_map(420, shade=('NH', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'DE', 'MD', 'VA', 'NC', 'SC', 'GA'))
# rights: a written list of rights and the people it protects
social-studies-5-the-constitution-and-bill-of-rights/rights = row(page(170, lines=6, title=True), row(person(80, BLUE), person(80, ORANGE), person(80, GREEN), gap=6), gap=20)
# checks and balances: a balance scale with three weights
social-studies-5-the-constitution-and-bill-of-rights/checks-and-balances = scale_icon(320, left=row(tile('', BLUE, 30), tile('', ORANGE, 30), gap=4), right=tile('', GREEN, 34))
# empire: the Roman Empire at its largest, around the Mediterranean Sea
social-studies-6-ancient-rome/empire = world_map(440, view=(-15, 20, 50, 58), land='#efe6d2', polys=[([(-10, 44), (-5, 48.5), (2, 51.5), (6, 52), (7, 50), (8, 47.5), (13, 48), (17, 48), (20, 46), (22, 48.5), (27, 48.5), (29, 45), (30, 44), (28, 42), (30, 41.5), (34, 42), (40, 41), (42, 40), (44, 38), (40, 36), (38, 33), (35, 30), (35, 28), (33, 24), (31, 23), (29, 30), (25, 31), (20, 30), (15, 31), (10, 33), (9, 30), (5, 34), (-2, 34), (-6, 33), (-10, 35)], RED), ([(-6, 50), (2, 51), (1, 53), (-2, 55.5), (-6, 55.5), (-5, 52)], RED)])
# location: a map pin on a grid
social-studies-6-five-themes-of-geography/location = map_tile(320, grid_=True, roads=False, pins=((150, 120),))
# movement: arrows between cities on a map
social-studies-6-five-themes-of-geography/movement = map_tile(320, roads=False, pins=((60, 60), (240, 190))) if 0 else world_map(440, arrows_=[(-74, 40, -0, 51), (2, 48, 77, 28), (139, 35, -122, 37)], pins=())
# absolute location: a globe with lines of latitude and longitude; a pin marks where two lines cross
social-studies-6-five-themes-of-geography/absolute-location = [raw(gl.w, gl.h, gl.svg + g(pin(70), 240.3 - 24.3, 105 - 70)) for gl in [globe(300, lat=True, grid_=True)]][0]
# population density: a square crowded with dots
social-studies-6-world-regions-today/population-density = raw(260, 260, '<rect x="5" y="5" width="250" height="250" rx="10" fill="#fff" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<circle cx="{20 + 220 * ((math.sin(i * 12.9898) * 43758.5453) % 1):.1f}" cy="{20 + 220 * ((math.sin(i * 78.233) * 24634.6345) % 1):.1f}" r="7" fill="#e04848"/>' for i in range(130)))
# GDP: a bar chart of countries
social-studies-6-world-regions-today/gdp = bars((8, 5, 3, 6, 2), labels=('A', 'B', 'C', 'D', 'E'), colors=(BLUE, ORANGE, GREEN, PURPLE, RED), size=320)
# migration: arrows crossing a map
social-studies-6-world-regions-today/migration = world_map(440, arrows_=[(20, 5, 10, 50), (-90, 15, -100, 40), (80, 20, 50, 25)])
# colony: a map with an arrow across the ocean
social-studies-7-age-of-exploration/colony = world_map(440, arrows_=[(-5, 45, -70, 15)])
# Atlantic slave trade: arrows crossing the Atlantic
social-studies-7-age-of-exploration/atlantic-slave-trade = world_map(440, arrows_=[(5, 8, -45, -10), (8, 0, -78, 25)])
# Aztec: an island city with causeways
social-studies-7-civilizations-of-the-americas/aztec = raw(340, 300, '<rect x="0" y="0" width="340" height="300" rx="10" fill="#8fb8f0" stroke="#1f2430" stroke-width="5"/><ellipse cx="170" cy="150" rx="70" ry="56" fill="#f4e3b4" stroke="#1f2430" stroke-width="5"/><path d="M170 94 V0 M100 150 H0 M240 150 H340 M170 206 V300" stroke="#c9a26b" stroke-width="16"/><rect x="150" y="128" width="40" height="40" fill="#e04848" stroke="#1f2430" stroke-width="4"/>')
# Constantinople: a city on a strait between two continents
social-studies-7-fall-of-rome-and-the-byzantine-empire/constantinople = raw(360, 260, '<rect x="0" y="0" width="360" height="260" rx="10" fill="#8fb8f0" stroke="#1f2430" stroke-width="5"/><path d="M0 0 H150 C170 80 160 140 150 200 C130 230 80 260 0 260 Z" fill="#d3f0de" stroke="#1f2430" stroke-width="4"/><path d="M360 0 H210 C190 80 200 140 210 200 C230 230 280 260 360 260 Z" fill="#fde3c8" stroke="#1f2430" stroke-width="4"/><circle cx="140" cy="130" r="22" fill="#e04848" stroke="#1f2430" stroke-width="4"/><text x="60" y="40" font-family="Segoe UI" font-size="26" font-weight="700" fill="#1f2430">Europe</text><text x="250" y="40" font-family="Segoe UI" font-size="26" font-weight="700" fill="#1f2430">Asia</text>')
# continuity: an unbroken line across a timeline
social-studies-7-fall-of-rome-and-the-byzantine-empire/continuity = timeline(5, 420, keep_going=0)
# caliphate: a round city plan
social-studies-7-islamic-civilizations/caliphate = raw(300, 300, '<circle cx="150" cy="150" r="130" fill="#f4e3b4" stroke="#1f2430" stroke-width="6"/><circle cx="150" cy="150" r="90" fill="none" stroke="#c9a26b" stroke-width="5"/><circle cx="150" cy="150" r="34" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<line x1="{150 + 34 * math.cos(a):.1f}" y1="{150 + 34 * math.sin(a):.1f}" x2="{150 + 130 * math.cos(a):.1f}" y2="{150 + 130 * math.sin(a):.1f}" stroke="#c9a26b" stroke-width="7"/>' for a in [math.pi / 4 + k * math.pi / 2 for k in range(4)]))
# algebra: x + 3 = 7
social-studies-7-islamic-civilizations/algebra = M('x + 3 = 7', 80)
# Mongol Empire: the Mongol Empire across Asia
social-studies-7-medieval-asia/mongol-empire = world_map(440, view=(10, 5, 150, 70), land='#efe6d2', polys=[([(25, 50), (40, 57), (60, 58), (80, 55), (100, 55), (120, 53), (135, 48), (130, 40), (122, 30), (120, 22), (110, 20), (100, 22), (97, 28), (90, 28), (80, 32), (70, 35), (60, 28), (50, 30), (45, 33), (38, 36), (36, 40), (40, 44), (30, 46)], ORANGE)])
# Black Death: a map shading Europe by year
social-studies-7-medieval-europe/black-death = world_map(440, shade=[(-10, 36, 10, 45, RED), (0, 45, 20, 52, ORANGE), (10, 52, 40, 70, YELLOW)])
# Great Compromise: two chambers side by side
social-studies-8-creating-the-constitution/great-compromise = row(box(T('Senate', 36), w=170, h=150, color=BLUE), box(T('House', 36), w=170, h=150, color=ORANGE), gap=30)
# federalism: two linked government buildings
social-studies-8-creating-the-constitution/federalism = row(pillars(3, 150), chain(2, 90), pillars(3, 120, color=ORANGE), gap=6)
# sectionalism: a U.S. map split in two
social-studies-8-slavery-and-sectionalism/sectionalism = us_map(420, split=True)
# Missouri Compromise: a map with a line across the west
social-studies-8-slavery-and-sectionalism/missouri-compromise = us_map(420, shade=('MO',), color=ORANGE, line='M380 395 H700')
# secession: a state breaking away from a map
social-studies-8-the-civil-war/secession = row(us_map(330, shade=()) if 0 else us_map(330), arrow(50, color=RED), raw(80, 80, '<path d="M5 20 L60 5 L75 60 L20 75 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/>'), gap=8)
# Monroe Doctrine: a stop hand beside the Americas: Europe, keep out
social-studies-8-the-early-republic/monroe-doctrine = row(stop_hand(130), world_map(320, shade=[(-170, -55, -35, 75, BLUE)], arrows_=[(15, 50, -35, 35)]), gap=10)
# Louisiana Purchase: a U.S. map with the middle shaded
social-studies-8-westward-expansion/louisiana-purchase = us_map(420, shade=('LA', 'AR', 'MO', 'IA', 'MN', 'ND', 'SD', 'NE', 'KS', 'OK', 'MT', 'WY', 'CO'))
# Indian Removal Act: a map with arrows pointing west
social-studies-8-westward-expansion/indian-removal-act = us_map(420, arrows_=[(780, 380, 520, 360), (760, 300, 520, 320)])
# Trail of Tears: a map route from Georgia to Oklahoma
social-studies-8-westward-expansion/trail-of-tears = us_map(420, shade=('GA', 'OK'), color=ORANGE, arrows_=[(760, 400, 500, 380)])
# imperialism: a map of Africa with drawn borders
social-studies-9-imperialism/imperialism = world_map(440, shade=[(-18, -35, 52, 37, ORANGE)])
# Scramble for Africa: Africa in 1914 colored by the European country that ruled each part; Ethiopia and Liberia stayed free
social-studies-9-imperialism/scramble-for-africa = col(world_map(420, view=(-20, -36, 55, 38), land='#f4f1ea', polys=[([(-17, 28), (-9, 36), (8, 37), (9, 30), (12, 23), (15, 23), (24, 20), (24, 10), (19, 3), (18, -4), (12, -5), (9, 1), (10, 6), (3, 6), (2, 10), (-3, 5), (-8, 5), (-13, 8), (-17, 14)], BLUE), ([(25, 31.5), (34, 31), (37, 22), (38, 18), (36, 12), (34, 4), (30, 4), (24, 9), (24, 22)], RED), ([(34, 4), (41, 4), (41, -2), (39, -5), (33, -1), (30, -1), (30, 2)], RED), ([(16, -29), (18, -35), (28, -34), (33, -27), (32, -22), (33, -17), (30, -15), (33, -9), (28, -9), (24, -12), (22, -17), (20, -22), (20, -25)], RED), ([(3, 6), (3, 13), (10, 13), (14, 13), (14, 10), (9, 4)], RED), ([(-3, 5), (-3, 11), (0, 11), (1, 6)], RED), ([(43, 11), (48, 8), (51, 11), (44, 11.5)], RED), ([(9, 2), (9, 4), (14, 11), (15, 10), (16, 2), (13, 2)], PURPLE), ([(0, 6), (0, 11), (1.5, 11), (1.5, 6)], PURPLE), ([(12, -17), (20, -17), (20, -22), (20, -28), (16, -29), (14, -23)], PURPLE), ([(30, -1), (39, -5), (40, -11), (34, -11), (30, -8)], PURPLE), ([(12, -5), (18, -4), (19, 3), (24, 5), (30, 4), (30, -1), (30, -8), (28, -9), (24, -12), (22, -11), (17, -7), (12, -6)], ORANGE), ([(12, -6), (17, -7), (22, -11), (24, -12), (22, -17), (12, -17)], GREEN), ([(30, -15), (33, -17), (32, -22), (33, -27), (36, -24), (35, -20), (40, -16), (40, -11), (34, -11)], GREEN), ([(9, 30), (12, 33), (20, 31), (25, 31.5), (25, 20), (24, 20), (15, 23), (12, 23)], TEAL), ([(37, 15), (39, 18), (43, 13), (40, 14)], TEAL), ([(41, -1), (41, 4), (46, 5), (49, 8), (51, 11), (48, 4), (42, -1)], TEAL), ([(-17, 21), (-12, 28), (-8.7, 27.7), (-8.7, 26), (-12, 26), (-12, 21)], YELLOW)]), grid([row(raw(30, 30, f'<rect x="2" y="2" width="26" height="26" fill="{c}" stroke="#1f2430" stroke-width="2"/>'), T(n, 28), gap=6) for n, c in (('France', BLUE), ('Britain', RED), ('Germany', PURPLE), ('Belgium', ORANGE), ('Portugal', GREEN), ('Italy', TEAL), ('Spain', YELLOW), ('free', '#f4f1ea'))], 4, gap=10), gap=8)
# sphere of influence: a shaded zone on a coast
social-studies-9-imperialism/sphere-of-influence = raw(340, 260, '<rect x="0" y="0" width="340" height="260" rx="10" fill="#8fb8f0" stroke="#1f2430" stroke-width="5"/><path d="M0 0 H240 C230 60 260 120 240 180 C230 220 260 240 250 260 H0 Z" fill="#e9f3dc" stroke="#1f2430" stroke-width="4"/><path d="M120 60 H236 C226 100 248 130 238 160 H120 Z" fill="#e04848" opacity="0.6"/>')
# colonialism: arrows carrying goods to a distant country
social-studies-9-imperialism/colonialism = world_map(440, arrows_=[(20, 0, 0, 50), (80, 20, -2, 52)])
# separation of powers: three branches of government: one makes laws, one carries them out, one judges them
social-studies-9-revolutions-and-enlightenment/separation-of-powers = row(*[col(pillars(3, 150, color=c), T(a, 30, c), T(b, 24, GRAY), gap=2) for a, b, c in (('legislative', 'makes laws', BLUE), ('executive', 'carries out laws', ORANGE), ('judicial', 'judges laws', PURPLE))], gap=14, align='t')
# alliance: linked chain rings
social-studies-9-world-war-i/alliance = chain(3, 340)
# map: a simple map of a place: a river, roads and houses from above
social-studies-k-my-place-in-the-world/map = map_tile(320, roads=True, river=True, houses=[(30, 30), (222, 36), (40, 150), (232, 160)])
# water: a map with blue lakes and a river
social-studies-k-my-place-in-the-world/water = map_tile(340, roads=False, river=True, lakes=True)
# near: a house and a school close together on a map
social-studies-k-my-place-in-the-world/near = map_tile(340, roads=True, houses=((150, 60), (215, 60)))
# rule: a sign with a walking footprint
social-studies-k-rules-and-responsibilities/rule = col(box(footprint(110), color=GREEN, fill="#fff", p=26), raw(24, 90, '<rect x="6" y="0" width="12" height="90" fill="#8a8f9c"/>'), gap=0)
# fair: a balance scale that is level
social-studies-k-rules-and-responsibilities/fair = scale_icon(300)
# citizen: a star badge with a heart
social-studies-k-rules-and-responsibilities/citizen = over(star(260), heart(90, RED))
# kind: a heart with small sparkles
social-studies-k-rules-and-responsibilities/kind = raw(260, 240, '<path d="M130 220 C60 170 10 130 20 80 C30 30 90 20 130 70 C170 20 230 30 240 80 C250 130 200 170 130 220 Z" fill="#f08aa8" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<path d="M{x} {y - 14} L{x + 4} {y - 4} L{x + 14} {y} L{x + 4} {y + 4} L{x} {y + 14} L{x - 4} {y + 4} L{x - 14} {y} L{x - 4} {y - 4} Z" fill="#f5c524"/>' for x, y in ((30, 20), (236, 26), (240, 190), (24, 180))))
# country: a map outline of the United States
social-studies-k-symbols-and-holidays/country = us_map(440, color=BLUE, shade=())
# future: an arrow pointing forward to a star
social-studies-k-then-and-now/future = row(arrow(200, color=BLUE, sw=12), star(130), gap=10)
# topic-comment: two blocks, topic then comment, with an arrow
world-languages-6-12-asl-grammar-and-facial-expression/topic-comment = row(box(T('topic', 40), w=170, h=110, color=BLUE), arrow(70), box(T('comment', 40), w=210, h=110, color=ORANGE), gap=10)
# non-manual markers: a simple face outline with raised eyebrows
world-languages-6-12-asl-grammar-and-facial-expression/non-manual-markers = head_outline(280, brows='up')
# wh-question: a face outline with lowered eyebrows
world-languages-6-12-asl-grammar-and-facial-expression/wh-question = head_outline(280, brows='down')
# yes/no question: a face outline with raised eyebrows and a tilted head
world-languages-6-12-asl-grammar-and-facial-expression/yes-no-question = head_outline(280, brows='up', tilt=-12)
# fingerspelling: the hand shapes for C, A and B spell CAB
world-languages-6-12-asl-grammar-and-facial-expression/fingerspelling = row(*[col(hand(120, k), T(l, 44), gap=4) for k, l in (('c', 'C'), ('a', 'A'), ('flat', 'B'))], gap=16, align='b')
# gloss: the words ME GO STORE in capitals
world-languages-6-12-asl-grammar-and-facial-expression/gloss = T('ME GO STORE', 64)
# classifier: the CL:3 hand stands for a car and moves along its path
world-languages-6-12-classifiers-and-space/classifier = row(col(hand(130, '3'), T('CL:3', 30, BLUE), gap=4), raw(240, 140, '<path d="M10 120 C80 0 160 0 220 100" fill="none" stroke="#3a7bd5" stroke-width="8" stroke-dasharray="14 8"/><path d="M228 116 l-4 -28 l-22 14 z" fill="#3a7bd5"/>'), car(120), gap=4)
# signing space: a box in front of a simple torso outline
world-languages-6-12-classifiers-and-space/signing-space = torso(280, inner=None) if 0 else over(torso(280), raw(200, 120, '<rect x="5" y="5" width="190" height="110" rx="8" fill="#3a7bd5" fill-opacity="0.15" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="12 8"/>'), dy=40)
# referent: a dot in space with an arrow pointing to it
world-languages-6-12-classifiers-and-space/referent = raw(320, 200, '<circle cx="260" cy="70" r="22" fill="#e04848" stroke="#1f2430" stroke-width="4"/><path d="M20 170 L232 84" stroke="#1f2430" stroke-width="8"/><path d="M244 78 l-28 0 l10 24 z" fill="#1f2430"/>')
# location: a dot marked on a signing space box
world-languages-6-12-classifiers-and-space/location = raw(300, 220, '<rect x="5" y="5" width="290" height="210" rx="10" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="5" stroke-dasharray="14 8"/><circle cx="210" cy="80" r="22" fill="#e04848" stroke="#1f2430" stroke-width="4"/>')
# role shift: two arrows turning left and right
world-languages-6-12-classifiers-and-space/role-shift = row(curve_arrow(60, color=BLUE, start=200, end=330, cw=True), curve_arrow(60, color=ORANGE, start=-150, end=-30, cw=True), gap=20) if 0 else row(arrow(130, dir='left', color=BLUE, sw=10), head_outline(130), arrow(130, color=ORANGE, sw=10), gap=10)
# Spanish-speaking world: a world map with many countries shaded
world-languages-6-12-cultures-of-the-spanish-speaking-world/spanish-speaking-world = world_map(440, shade=[(-118, -55, -35, 32, ORANGE), (-10, 36, 3, 44, ORANGE)])
# dialect: one car, two words: coche in Spain, carro in Mexico
world-languages-6-12-cultures-of-the-spanish-speaking-world/dialect = col(car(130), row(col(bubble(T('coche', 38), 160, tail='left'), T('España', 26, GRAY), gap=2), col(bubble(T('carro', 38), 160, color=ORANGE, tail='right'), T('México', 26, GRAY), gap=2), gap=24), gap=8)
# Deaf culture: a hand outline in a spotlight
world-languages-6-12-deaf-culture-and-community/deaf-culture = raw(300, 300, '<path d="M150 0 L40 290 H260 Z" fill="#fff4b0" opacity="0.8"/><ellipse cx="150" cy="290" rx="110" ry="12" fill="#f5c524" opacity="0.6"/>') if 0 else over(raw(300, 320, '<path d="M150 0 L30 320 H270 Z" fill="#fff4b0"/>'), hand(180), dy=50)
# capital-D Deaf: a large capital D
world-languages-6-12-deaf-culture-and-community/capital-d-deaf = T('D', 240, color=BLUE)
# interpreter: two speech forms joined by a two-way arrow
world-languages-6-12-deaf-culture-and-community/interpreter = row(hand(130), arrow(100, double=True), bubble(None, 120), gap=14)
# audism: an unbalanced scale
world-languages-6-12-deaf-culture-and-community/audism = scale_icon(300, tilt=20)
# preterite: a timeline with a closed dot in the past
world-languages-6-12-past-tenses/preterite = timeline(3, 420, closed=0, now=2, labels=('ayer', '', 'hoy'))
# imperfect: a timeline with a wavy line in the past
world-languages-6-12-past-tenses/imperfect = timeline(3, 420, wavy=(0, 1), now=2, labels=('', '', 'hoy'))
# completed action: a timeline segment with a start and an end
world-languages-6-12-past-tenses/completed-action = timeline(4, 420, segment=(0, 2))
# habitual action: a timeline with repeated dots
world-languages-6-12-past-tenses/habitual-action = timeline(5, 420, repeated=True)
# time expression: a calendar with yesterday circled
world-languages-6-12-past-tenses/time-expression = calendar(280, circled=12)
# present tense: a timeline with a dot on now
world-languages-6-12-present-tense-verbs/present-tense = timeline(3, 420, now=1, labels=('', 'now', ''))
# conjugate: a verb stem with six different ending tiles
world-languages-6-12-present-tense-verbs/conjugate = row(tile('habl', BLUE, 90, w=150), col(*[tile(e, ORANGE, 44, w=110) for e in ('-o', '-as', '-a', '-amos', '-áis', '-an')], gap=6), gap=20)
# infinitive: a verb tile ending in -ir
world-languages-6-12-present-tense-verbs/infinitive = row(tile('viv', BLUE, 100, w=150), tile('-ir', ORANGE, 100, w=120), gap=6)
# stem-changing verb: o changing to ue inside a verb
world-languages-6-12-present-tense-verbs/stem-changing-verb = col(row(T('p', 64), tile('o', RED, 76), T('der', 64), gap=6), arrow(60, dir='down'), row(T('p', 64), tile('ue', RED, 76, w=100), T('do', 64), gap=6), gap=10)
# irregular verb: a verb tile with a zigzag arrow
world-languages-6-12-present-tense-verbs/irregular-verb = row(tile('ser', BLUE, 100, w=150), raw(120, 100, '<path d="M10 50 L40 20 L60 70 L85 20 L100 50" fill="none" stroke="#e04848" stroke-width="8" stroke-linejoin="round"/><path d="M112 54 l-20 -2 l10 -16 z" fill="#e04848"/>'), tile('soy', ORANGE, 100, w=150), gap=10)
# subject pronoun: tiles reading yo, tú, ella, nosotros
world-languages-6-12-present-tense-verbs/subject-pronoun = grid([tile(s, c, 90) for s, c in (('yo', BLUE), ('tú', ORANGE), ('ella', GREEN), ('nosotros', PURPLE))], 2, gap=14)
# turn left: an arrow turning left at a corner
world-languages-6-12-travel-and-directions/turn-left = raw(300, 300, '<rect x="110" y="0" width="80" height="300" fill="#b9b2a6"/><rect x="0" y="110" width="190" height="80" fill="#b9b2a6"/><path d="M150 280 V150 H50" fill="none" stroke="#e04848" stroke-width="12"/><path d="M26 150 l28 -18 v36 z" fill="#e04848"/>')
# straight ahead: an arrow pointing straight up a street
world-languages-6-12-travel-and-directions/straight-ahead = raw(260, 320, '<rect x="80" y="0" width="100" height="320" fill="#b9b2a6"/><path d="M130 0 V320" stroke="#fff" stroke-width="4" stroke-dasharray="16 12"/><path d="M130 300 V50" stroke="#e04848" stroke-width="12"/><path d="M130 20 l-18 30 h36 z" fill="#e04848"/>')
# block: a grid of streets with one block shaded
world-languages-6-12-travel-and-directions/block = raw(320, 320, '<rect x="0" y="0" width="320" height="320" fill="#b9b2a6"/>' + ''.join(f'<rect x="{20 + c * 100}" y="{20 + r * 100}" width="80" height="80" rx="6" fill="{"#f08a24" if (r, c) == (1, 1) else "#d3f0de"}" stroke="#1f2430" stroke-width="3"/>' for r in range(3) for c in range(3)))
# mother: a house with a heart
# family: a house outline with a heart
world-languages-k-12-family-home-and-school/family = house(280, inner=heart(80))
# home: a house
world-languages-k-12-family-home-and-school/home = house(280)
# school: a school building
world-languages-k-12-family-home-and-school/school = raw(320, 260, '<rect x="20" y="90" width="280" height="160" fill="#f6d27a" stroke="#1f2430" stroke-width="5"/><path d="M10 96 L160 20 L310 96 Z" fill="#e04848" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="135" y="180" width="50" height="70" fill="#c98b4f" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<rect x="{x}" y="120" width="40" height="40" fill="#d6e6fb" stroke="#1f2430" stroke-width="4"/>' for x in (45, 105, 175, 235)) + '<circle cx="160" cy="64" r="16" fill="#fff" stroke="#1f2430" stroke-width="4"/><line x1="160" y1="20" x2="160" y2="-10" stroke="#1f2430" stroke-width="4"/><path d="M160 -10 L190 -2 L160 6 Z" fill="#3a7bd5"/>')
# teacher: a chalkboard
world-languages-k-12-family-home-and-school/teacher = raw(360, 260, '<rect x="10" y="10" width="340" height="200" rx="8" fill="#2f5d3a" stroke="#8f6a4f" stroke-width="14"/><text x="180" y="130" font-family="Segoe UI" font-size="60" font-weight="700" text-anchor="middle" fill="#fff">2 + 2</text><rect x="250" y="216" width="50" height="14" rx="3" fill="#fff" stroke="#1f2430" stroke-width="3"/>')
# brother: two hand outlines side by side
# sister: two hand outlines side by side
# manual alphabet: four letters of the manual alphabet: A, B, C and L
world-languages-k-12-fingerspelling-and-the-manual-alphabet/manual-alphabet = row(*[col(hand(100, k), T(l, 40), gap=4) for k, l in (('a', 'A'), ('flat', 'B'), ('c', 'C'), ('l', 'L'))], gap=12, align='b')
# fingerspell: the hand shapes for L, A and B spell LAB
world-languages-k-12-fingerspelling-and-the-manual-alphabet/fingerspell = row(*[col(hand(120, k), T(l, 44), gap=4) for k, l in (('l', 'L'), ('a', 'A'), ('flat', 'B'))], gap=16, align='b')
# handshape: one hand shape: an open hand with the fingers spread
world-languages-k-12-fingerspelling-and-the-manual-alphabet/handshape = hand(260, 'open')
# dominant hand: one hand outline highlighted
world-languages-k-12-fingerspelling-and-the-manual-alphabet/dominant-hand = row(hand(150), hand(150, hl=True), gap=16)
# name sign: a gift box with a hand outline
world-languages-k-12-fingerspelling-and-the-manual-alphabet/name-sign = row(raw(200, 200, '<rect x="20" y="80" width="160" height="110" fill="#e04848" stroke="#1f2430" stroke-width="5"/><rect x="10" y="56" width="180" height="34" fill="#e04848" stroke="#1f2430" stroke-width="5"/><rect x="88" y="56" width="24" height="134" fill="#f5c524" stroke="#1f2430" stroke-width="4"/><path d="M100 56 C70 20 50 40 70 56 M100 56 C130 20 150 40 130 56" fill="none" stroke="#f5c524" stroke-width="8"/>'), hand(150), gap=16)
# letter: the letter A beside a fist outline
world-languages-k-12-fingerspelling-and-the-manual-alphabet/letter = row(T('A', 160, color=BLUE), hand(160, 'a'), gap=30)
# hello: a waving hand outline
world-languages-k-12-greetings-and-introductions/hello = wave_hand(260)
# goodbye: a door with an arrow out
world-languages-k-12-greetings-and-introductions/goodbye = row(door(200), arrow(90, color=BLUE), gap=10)
# please: a flat hand circling on the chest
world-languages-k-12-greetings-and-introductions/please = torso(280, inner=over(hand(110, 'flat'), curve_arrow(70, ORANGE, sw=6)))
# thank you: a heart
world-languages-k-12-greetings-and-introductions/thank-you = heart(260)
# my name is: a name tag
world-languages-k-12-greetings-and-introductions/my-name-is = raw(340, 220, '<rect x="10" y="10" width="320" height="200" rx="18" fill="#fff" stroke="#e04848" stroke-width="8"/><rect x="10" y="10" width="320" height="70" rx="18" fill="#e04848"/><rect x="10" y="56" width="320" height="24" fill="#e04848"/><text x="170" y="58" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#fff">HELLO</text><rect x="50" y="130" width="240" height="10" rx="5" fill="#b8bcc6"/>')
# how are you: a speech bubble with a question mark
world-languages-k-12-greetings-and-introductions/how-are-you = bubble(qmark(100), 260)
# hello: a hand outline moving out from the forehead
world-languages-k-12-greetings-and-introductions-in-asl/hello = row(head_outline(170, dot='forehead'), raw(120, 60, '<path d="M10 30 H90" stroke="#3a7bd5" stroke-width="8"/><path d="M110 30 l-24 -14 v28 z" fill="#3a7bd5"/>'), hand(110, 'flat'), gap=0)
# name: a name tag
world-languages-k-12-greetings-and-introductions-in-asl/name = raw(340, 220, '<rect x="10" y="10" width="320" height="200" rx="18" fill="#fff" stroke="#3a7bd5" stroke-width="8"/><rect x="10" y="10" width="320" height="70" rx="18" fill="#3a7bd5"/><rect x="10" y="56" width="320" height="24" fill="#3a7bd5"/><text x="170" y="58" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#fff">NAME</text><rect x="50" y="130" width="240" height="10" rx="5" fill="#b8bcc6"/>')
# nice to meet you: two index fingers moving together to meet
world-languages-k-12-greetings-and-introductions-in-asl/nice-to-meet-you = [row(h, arrow(40, ORANGE), arrow(40, ORANGE, 'left'), raw(h.w, h.h, f'<g transform="translate({h.w:.1f} 0) scale(-1 1)">{h.svg}</g>'), gap=4) for h in [hand(140, 'point')]][0]
# Deaf: a hand outline beside a heart
world-languages-k-12-greetings-and-introductions-in-asl/deaf = row(hand(160), heart(110), gap=20)
# get attention: a waving hand outline
world-languages-k-12-greetings-and-introductions-in-asl/get-attention = wave_hand(260)
# feeling: three simple faces: happy, sad, tired
world-languages-k-12-greetings-and-introductions-in-asl/feeling = faces('happy', 'sad', 'tired', size=110)
# number: number cards 1 to 5
world-languages-k-12-numbers-colors-and-calendar/number = tiles('1', '2', '3', '4', '5', colors=(BLUE, ORANGE, GREEN, PURPLE, RED), size=74)
# month: a calendar page
world-languages-k-12-numbers-colors-and-calendar/month = calendar(280)
# today: a calendar with one day circled
world-languages-k-12-numbers-colors-and-calendar/today = calendar(280, circled=9)
# number: an open hand outline
world-languages-k-12-numbers-colors-and-time/number = hand(260)
# color: crayons in a row
world-languages-k-12-numbers-colors-and-time/color = raw(400, 220, ''.join(f'<path d="M{20 + i * 62} 60 L{37 + i * 62} 20 L{54 + i * 62} 60 V200 H{20 + i * 62} Z" fill="{c}" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>' for i, c in enumerate(('#e04848', '#f08a24', '#f5c524', '#2f9e5b', '#3a7bd5', '#9b5de5'))))
# day: a week: one day picked out
world-languages-k-12-numbers-colors-and-time/day = col(row(*[tile(d, ORANGE if i == 3 else BLUE, 58, fill='#fde97a' if i == 3 else None) for i, d in enumerate('SMTWTFS')], gap=6), T('1 day', 36, ORANGE), gap=10)
# time: a wristwatch
world-languages-k-12-numbers-colors-and-time/time = raw(160, 300, '<rect x="45" y="0" width="70" height="300" rx="16" fill="#8f6a4f" stroke="#1f2430" stroke-width="5"/><circle cx="80" cy="150" r="66" fill="#fff" stroke="#1f2430" stroke-width="8"/><line x1="80" y1="150" x2="80" y2="104" stroke="#1f2430" stroke-width="7" stroke-linecap="round"/><line x1="80" y1="150" x2="112" y2="150" stroke="#1f2430" stroke-width="7" stroke-linecap="round"/>')
# palm orientation: a hand outline with an arrow showing palm direction
world-languages-k-12-numbers-colors-and-time/palm-orientation = row(hand(200), curve_arrow(50, color=ORANGE, start=-90, end=150), gap=10)
# week: seven boxes in a row
world-languages-k-12-numbers-colors-and-time/week = raw(440, 80, ''.join(f'<rect x="{5 + i * 62}" y="10" width="56" height="60" rx="6" fill="{"#d6e6fb" if i not in (0, 6) else "#fde3c8"}" stroke="#1f2430" stroke-width="4"/>' for i in range(7)))
# o'clock: a clock at 8:00 with the minute hand pointing at 12
world-languages-k-12-school-and-daily-routine/o-clock = clock(300, 8, 0, hl='m')
# every day: a week with all days checked
world-languages-k-12-school-and-daily-routine/every-day = raw(440, 80, ''.join(f'<rect x="{5 + i * 62}" y="10" width="56" height="60" rx="6" fill="#d3f0de" stroke="#1f2430" stroke-width="4"/><path d="M{17 + i * 62} 40 l10 12 l20 -24" fill="none" stroke="#2f9e5b" stroke-width="6" stroke-linecap="round"/>' for i in range(7)))
# parameter: five labeled boxes
world-languages-k-12-the-five-parameters-of-a-sign/parameter = grid([tile(s, c, 64) for s, c in (('hand', BLUE), ('place', ORANGE), ('move', GREEN), ('palm', PURPLE), ('face', RED))], 2, gap=12)
# location: a head outline with a dot at the chin
world-languages-k-12-the-five-parameters-of-a-sign/location = head_outline(280, dot='chin')
# movement: a hand moving from one place to another along an arc
world-languages-k-12-the-five-parameters-of-a-sign/movement = [row(raw(h.w, h.h, f'<g opacity="0.3">{h.svg}</g>'), curve_arrow(46, ORANGE, start=200, end=340), h, gap=0, align='b') for h in [hand(130, 'flat')]][0]
# handshape: a fist outline
world-languages-k-12-the-five-parameters-of-a-sign/handshape = hand(260, 'fist')
# non-manual marker: a face outline with motion lines
world-languages-k-12-the-five-parameters-of-a-sign/non-manual-marker = head_outline(280, motion=True)
# minimal pair: two head outlines with dots at chin and forehead
world-languages-k-12-the-five-parameters-of-a-sign/minimal-pair = row(over(pad(head_outline(190, dot='chin'), 24), hand(90, hl=True), dx=40, dy=32), raw(40, 60, '<path d="M8 22 H32 M8 38 H32" stroke="#8a8f9c" stroke-width="6" stroke-linecap="round"/><path d="M30 6 L10 54" stroke="#e04848" stroke-width="6" stroke-linecap="round"/>'), over(pad(head_outline(190, dot='forehead'), 24), hand(90, hl=True), dx=40, dy=-62), gap=14)

# ---------- 2026-10-27: the last 176 modules ----------
# pathway: a dotted zigzag path with a start dot and an end arrow
arts-3-5-dance-ideas-from-art-and-words/pathway = raw(420, 260, '<path d="M30 220 L130 50 L230 210 L330 50 L380 130" fill="none" stroke="#3a7bd5" stroke-width="12" stroke-dasharray="4 22" stroke-linecap="round"/><circle cx="30" cy="220" r="20" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M362 108 L402 160 L352 158 Z" fill="#e04848" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>')
# level: three steps, low, middle and high
arts-3-5-dance-ideas-from-art-and-words/level = row(col(star(70, YELLOW), box(w=110, h=60, color=DARK, fill=GREEN, rx=8), gap=8, align='c'), col(star(70, YELLOW), box(w=110, h=150, color=DARK, fill=ORANGE, rx=8), gap=8), col(star(70, YELLOW), box(w=110, h=240, color=DARK, fill=PURPLE, rx=8), gap=8), gap=18, align='b')
# warm colors: red, orange and yellow swatches
arts-3-5-mood-and-place-in-art/warm-colors = row(box(w=130, h=200, color=DARK, fill=RED, rx=18), box(w=130, h=200, color=DARK, fill=ORANGE, rx=18), box(w=130, h=200, color=DARK, fill=YELLOW, rx=18), gap=14)
# cool colors: blue, green and purple swatches
arts-3-5-mood-and-place-in-art/cool-colors = row(box(w=130, h=200, color=DARK, fill=BLUE, rx=18), box(w=130, h=200, color=DARK, fill=GREEN, rx=18), box(w=130, h=200, color=DARK, fill=PURPLE, rx=18), gap=14)
# frame: a film strip of five frames, a ball moving a little in each
arts-3-5-stop-motion-animation/frame = raw(460, 150, '<rect x="0" y="0" width="460" height="150" rx="10" fill="#1f2430"/>' + ''.join(f'<rect x="{12 + i * 34}" y="8" width="18" height="14" rx="3" fill="#fff"/><rect x="{12 + i * 34}" y="128" width="18" height="14" rx="3" fill="#fff"/>' for i in range(14)) + ''.join(f'<rect x="{12 + i * 88}" y="32" width="80" height="86" fill="#fdf0c4"/><circle cx="{30 + i * 88 + i * 9}" cy="{95 - i * 12}" r="13" fill="#e04848" stroke="#1f2430" stroke-width="3"/>' for i in range(5)))
# storyboard: six numbered boxes in two rows
arts-3-5-stop-motion-animation/storyboard = grid([box(T(str(i), 40, GRAY), w=120, h=95, color=DARK, fill='#fff', rx=6) for i in range(1, 7)], 3, gap=16)
# melody: a single line of notes on a staff
arts-6-8-arranging-a-song/melody = staff([2, 4, 5, 4, 6, 5, 3, 2], size=440)
# harmony: notes stacked as chords on a staff
arts-6-8-arranging-a-song/harmony = staff([(0, 2, 4), (1, 3, 5), (2, 4, 6), (0, 2, 4)], size=440)
# dynamics: a crescendo hairpin from p (soft) to f (loud)
arts-6-8-arranging-a-song/dynamics = raw(460, 200, '<path d="M70 100 L390 30 M70 100 L390 170" fill="none" stroke="#1f2430" stroke-width="12" stroke-linecap="round"/><text x="10" y="122" font-family="Georgia, serif" font-size="70" font-style="italic" font-weight="700" fill="#3a7bd5">p</text><text x="404" y="122" font-family="Georgia, serif" font-size="70" font-style="italic" font-weight="700" fill="#e04848">f</text>')
# phrasing: notes on a staff grouped by curved slurs
arts-6-8-listening-and-reviewing/phrasing = col(raw(440, 50, '<path d="M120 44 Q200 0 270 44" fill="none" stroke="#e04848" stroke-width="7" stroke-linecap="round"/><path d="M300 44 Q350 8 420 44" fill="none" stroke="#e04848" stroke-width="7" stroke-linecap="round"/>'), staff([4, 5, 6, 5, 3, 4, 2], size=440), gap=0)
# staging: a stage floor plan with two X marks far apart
arts-6-8-comparing-productions/staging = over(raw(440, 280, '<path d="M20 260 L80 20 H360 L420 260 Z" fill="#efdccb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M20 260 Q220 290 420 260" fill="none" stroke="#a0673a" stroke-width="6"/>'), row(cross(70, RED), raw(170, 10, ''), cross(70, BLUE), gap=0), dy=10)
# blocking: a stage floor plan with X marks joined by arrows
arts-6-8-devising-a-scene/blocking = raw(440, 280, '<path d="M20 260 L80 20 H360 L420 260 Z" fill="#efdccb" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><g stroke="#e04848" stroke-width="9" stroke-linecap="round"><path d="M95 195 l30 30 M125 195 l-30 30"/><path d="M205 75 l30 30 M235 75 l-30 30"/><path d="M315 195 l30 30 M345 195 l-30 30"/></g><g fill="none" stroke="#3a7bd5" stroke-width="6" stroke-dasharray="14 10"><path d="M130 190 L200 115"/><path d="M240 115 L310 190"/></g><path d="M208 106 l-18 4 l8 -16 z M318 196 l-2 -18 l14 10 z" fill="#3a7bd5"/>')
# spacing: two dancers with a double arrow showing the space between them
arts-6-8-performing-in-different-spaces/spacing = row(person(140, BLUE), arrow(130, ORANGE, double=True), person(140, PURPLE), gap=10, align='b')
# scale: a small gridded sketch, an arrow, a big gridded wall
arts-6-8-public-art-and-murals/scale = row(grid_shade(3, 3, shaded=0, size=90, cells=[(0, 0), (1, 1), (2, 2)]), arrow(70), grid_shade(3, 3, shaded=0, size=260, cells=[(0, 0), (1, 1), (2, 2)]), gap=18)
# variable: a box holding the number 0
computer-science-3-5-plan-it-before-you-code-it/variable = box(T('0', 140), w=220, h=200, color=ORANGE, fill=soft(ORANGE), rx=18)
# vary: three timer displays showing different times
computer-science-3-5-why-data-varies/vary = col(digital('12.4'), digital('11.9'), digital('12.7'), gap=14)
# granularity: a coarse grid beside a fine grid
computer-science-6-8-data-metadata-and-you/granularity = row(grid_shade(3, 3, size=200, shaded=4), grid_shade(12, 12, size=200, shaded=64), gap=30)
# contrast: dark text on white beside gray text on gray
computer-science-6-8-design-for-every-user/contrast = row(box(T('Aa', 90, DARK), w=180, h=180, color=DARK, fill='#fff', rx=16), box(T('Aa', 90, '#a4a8b2'), w=180, h=180, color=DARK, fill='#c4c7cf', rx=16), gap=24)
# data: a table of sun and cloud days with tally marks
computer-science-k-2-asking-with-data/data = col(row(sun(100), tally(4, 120), gap=40), row(cloud(110, '#e6e8ee'), tally(2, 120), gap=30), gap=30, align='l')
# value: a box holding the number 5
computer-science-k-2-signs-and-changing-values/value = box(T('5', 150), w=220, h=200, color=BLUE, fill=soft(BLUE), rx=18)
# omission: a sentence strip with a gap marked by three dots
ela-6-8-commas-dashes-and-ellipses/omission = row(box(w=170, h=80, color=BLUE, fill=soft(BLUE), rx=12), dots(3, cols=3, size=34, color=DARK), box(w=170, h=80, color=BLUE, fill=soft(BLUE), rx=12), gap=18)
# heading: a page with bold heading bars over text blocks
ela-6-8-structure-in-informative-writing/heading = page(260, lines=9, bold=(0, 4), indent=(), paras=None)
# practice: a calendar with a check on every day
health-pe-3-5-juggling-and-practice-habits/practice = calendar(300, checks=tuple(range(14)), cells=14)
# progress: three rising steps with a star on top
health-pe-3-5-juggling-and-practice-habits/progress = over(stairs(3, 320, color=GREEN), star(80), dx=110, dy=-110)
# common ground: two overlapping circles with the middle shaded
social-studies-7-panel-of-experts/common-ground = venn(2, shade='both')
# second: one person moves an idea and another says I second it
social-studies-8-motion-on-the-floor/second = col(bubble(T('I move that...', 34), 300, tail='left'), bubble(T('I second it!', 34), 300, color=GREEN, tail='right'), gap=16)
# pattern: a repeating row of clap, clap, stomp icons
arts-k-2-making-up-songs/pattern = col(*[row(hand(110), hand(110), footprint(100), gap=14) for _ in range(2)], gap=30)
# order: three boxes with arrows between them
arts-k-2-picture-and-sound-stories/order = boxes('1', '2', '3', colors=[GREEN, BLUE, ORANGE], size=60, w=110, h=110, arrows=True)
# timeline: a timeline of computing years
computer-science-3-5-computing-inventions-and-inventors/timeline = timeline(4, 440, labels=['1950', '1970', '1990', '2010'])
# organize: mixed-up shapes, then the same shapes sorted into rows
computer-science-3-5-fair-surveys/organize = row(raw(170, 170, g(shape('circle', 44, BLUE), 8, 10) + g(shape('triangle', 48, ORANGE), 70, 4) + g(shape('square', 40, GREEN), 124, 30) + g(shape('square', 40, GREEN), 20, 72) + g(shape('circle', 44, BLUE), 84, 62) + g(shape('triangle', 48, ORANGE), 116, 116) + g(shape('circle', 44, BLUE), 34, 122) + g(shape('square', 40, GREEN), 78, 124)), arrow(50), col(*[row(*[shape(k, 40, c) for _ in range(3)], gap=8) for k, c in (('circle', BLUE), ('square', GREEN), ('triangle', ORANGE))], gap=10, align='l'), gap=14)
# flowchart: a flowchart with an oval, two boxes, a diamond and arrows
computer-science-3-5-plan-it-before-you-code-it/flowchart = col(box(w=150, h=56, color=BLUE, rx=28), arrow(34, dir='down'), box(w=170, h=56, color=GREEN, rx=8), arrow(34, dir='down'), diamond(150, '?'), arrow(34, dir='down'), box(w=170, h=56, color=GREEN, rx=8), gap=2)
# loop: a circular arrow around a step box
computer-science-3-5-plan-it-before-you-code-it/loop = curve_arrow(110, BLUE, start=-70, end=230, inner=box(w=80, h=56, color=ORANGE, rx=8))
# condition: a diamond with yes and no arrows
computer-science-3-5-plan-it-before-you-code-it/condition = row(col(check(70), arrow(60, GREEN, dir='left'), gap=4), diamond(220, '?'), col(cross(70), arrow(60, RED), gap=4), gap=6)
# outlier: a dot plot with one dot far to the right
computer-science-3-5-why-data-varies/outlier = dotplot([3, 4, 4, 5, 5, 5, 6, 6, 7, 14], size=420, a=0, b=15)
# relationship: a scatter plot with dots rising left to right
computer-science-3-5-why-data-varies/relationship = scatter(14, trend=1.0, noise=0.6, size=320, line=True)
# missing value: a table with one empty cell circled
computer-science-6-8-cleaning-data-honestly/missing-value = over(table(cells=[['', 'A', 'B', 'C'], ['1', '12', '8', '15'], ['2', '9', '', '11'], ['3', '14', '10', '7']], size=340), raw(80, 80, '<circle cx="40" cy="40" r="34" fill="none" stroke="#e04848" stroke-width="7"/>'), dx=26, dy=22)
# count: five red cars in a row with tally marks
computer-science-k-2-asking-with-data/count = col(row(*[car(100) for _ in range(5)], gap=6), tally(5, 170), gap=30)
# tally: tally marks in groups of five
computer-science-k-2-asking-with-data/tally = tally(12, 380)
# steps: three numbered footprints in a row
computer-science-k-2-fair-rules-for-turns/steps = footprints(3, 100, numbered=True)
# program: a green flag starting a stack of labeled code blocks, with a check
computer-science-k-2-what-the-code-does/program = col(flag(80, GREEN), code_blocks(3, 230, labels=('move 10', 'turn right', 'say Hi')), check(60), gap=8)
# step: one arrow pointing right
computer-science-k-2-what-the-code-does/step = arrow(300, BLUE, sw=18)
# rate: a pie with 10 percent shaded: 10 out of 100
cte-6-8-economy-checkup/rate = row(pie(0.1, 240, ORANGE), col(M('10%', 80, color=ORANGE), T('10 out of 100', 30), gap=4), gap=20)
# compound interest: bars that grow faster each year: the start plus interest that earns interest
cte-6-8-interest-rate-dial/compound-interest = raw(420, 330, ''.join(f'<rect x="{24 + i * 66}" y="120" width="50" height="150" fill="#3a7bd5" stroke="#1f2430" stroke-width="3"/><rect x="{24 + i * 66}" y="{120 - v * 1.5:.0f}" width="50" height="{v * 1.5:.0f}" fill="#2f9e5b" stroke="#1f2430" stroke-width="3"/><text x="{49 + i * 66}" y="300" font-family="Segoe UI, Arial, sans-serif" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">{i}</text>' for i, v in enumerate((0, 10, 21, 33, 46, 61))) + '<line x1="10" y1="270" x2="410" y2="270" stroke="#1f2430" stroke-width="4"/><text x="210" y="328" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700" text-anchor="middle" fill="#5a5f6c">years</text><rect x="20" y="10" width="22" height="22" fill="#3a7bd5"/><text x="50" y="29" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700" fill="#1f2430">start</text><rect x="130" y="10" width="22" height="22" fill="#2f9e5b"/><text x="160" y="29" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700" fill="#1f2430">interest</text>')
# equilibrium price: supply and demand lines crossing at the equilibrium price
cte-6-8-snow-season-prices/equilibrium-price = col(T('price', 26, GRAY), plot(lambda x: x, lambda x: 8 - x, size=320, xr=(0, 8), yr=(0, 8), points=[(4, 4)], hlines=(4,), texts=[(5.6, 7.4, 'supply', BLUE), (1.4, 4.4, 'demand', ORANGE)]), row(Item(170, 1, ''), T('quantity', 26, GRAY), gap=0), gap=2, align='l')
# prefix: pre- plus view makes preview
ela-3-5-academic-and-subject-words/prefix = col(row(tile('pre-', ORANGE, 100), M('+', 60), tile('view', BLUE, 100), gap=12), arrow(50, dir='down'), T('preview', 90, hl={'pre': ORANGE, 'view': BLUE}), gap=8)
# structure: two boxes with an arrow from problem to solution icons
ela-3-5-comparing-texts-side-by-side/structure = row(box(warning(110), color=RED, fill=soft(RED)), arrow(80), box(bulb(110), color=GREEN, fill=soft(GREEN)), gap=14)
# Venn diagram: two overlapping circles
ela-3-5-comparing-texts-side-by-side/venn-diagram = venn(2)
# timeline: a horizontal line with four dots and tick marks
ela-3-5-diagrams-and-how-things-happen/timeline = timeline(4, 440)
# process: four steps in a circle with arrows
ela-3-5-diagrams-and-how-things-happen/process = cycle(['1', '2', '3', '4'], size=44)
# panel: a comic page with three panels in a row
ela-3-5-pictures-panels-and-performances/panel = row(box(sun(70), w=130, h=150, color=DARK, fill='#fff', rx=4), box(bubble(None, 80), w=130, h=150, color=DARK, fill='#fff', rx=4), box(star(70), w=130, h=150, color=DARK, fill='#fff', rx=4), gap=10)
# syllable: butterfly split into three syllable tiles, one clap dot each
ela-3-5-readers-theater-and-fluency/syllable = row(*[col(tile(s, c, 100), dot(30, DARK), gap=14) for s, c in (('but', BLUE), ('ter', ORANGE), ('fly', GREEN))], gap=14)
# comma: a large comma mark
ela-3-5-revising-and-editing/comma = raw(200, 300, '<circle cx="100" cy="110" r="62" fill="#1f2430"/><path d="M158 120 Q156 225 66 278 L54 260 Q108 214 104 160 Z" fill="#1f2430"/>')
# dash: a long horizontal punctuation line between two word blocks
ela-6-8-commas-dashes-and-ellipses/dash = row(box(w=140, h=60, color=BLUE, fill=soft(BLUE), rx=10), raw(110, 20, '<line x1="5" y1="10" x2="105" y2="10" stroke="#1f2430" stroke-width="10" stroke-linecap="round"/>'), box(w=140, h=60, color=BLUE, fill=soft(BLUE), rx=10), gap=12)
# ellipsis: three dots in a row
ela-6-8-commas-dashes-and-ellipses/ellipsis = dots(3, cols=3, size=70, color=DARK, gap=40)
# parenthetical: a sentence bar with a middle part set off by two curved marks
ela-6-8-commas-dashes-and-ellipses/parenthetical = row(box(w=110, h=60, color=BLUE, fill=soft(BLUE), rx=10), T('(', 90, font="Georgia, serif"), box(w=110, h=60, color=ORANGE, fill=soft(ORANGE), rx=10), T(')', 90, font="Georgia, serif"), box(w=80, h=60, color=BLUE, fill=soft(BLUE), rx=10), gap=6)
# delineate: an outline with three numbered lines
ela-6-8-listening-to-speakers-and-discussing/delineate = col(*[row(T(str(i), 54), box(w=260, h=46, color=BLUE, fill=soft(BLUE), rx=8), gap=18) for i in (1, 2, 3)], gap=20)
# chronological order: numbered boxes 1, 2, 3 joined by arrows
ela-6-8-narrative-point-of-view-and-structure/chronological-order = boxes('1', '2', '3', size=60, w=100, h=100, arrows=True)
# logical order: three steps rising left to right
ela-6-8-presenting-claims-and-findings/logical-order = stairs(3, 340, labels=['1', '2', '3'], color=BLUE)
# section: a page split into three blocks
ela-6-8-structure-in-informative-writing/section = page(260, paras=(3, 3, 3), bold=(0, 4, 8))
# sentence: a word strip starting with a big block and ending with a dot
ela-k-2-adding-details-and-fixing-sentences/sentence = row(box(w=70, h=90, color=RED, fill=soft(RED), rx=8), box(w=110, h=60, color=BLUE, fill=soft(BLUE), rx=8), box(w=90, h=60, color=BLUE, fill=soft(BLUE), rx=8), dot(30, DARK, fill=DARK), gap=10, align='b')
# capital: a large capital A beside a small a
ela-k-2-adding-details-and-fixing-sentences/capital = row(T('A', 260, RED), T('a', 150, GRAY), gap=30, align='b')
# period: a large black dot
ela-k-2-adding-details-and-fixing-sentences/period = dot(180, DARK, fill=DARK)
# complete sentence: a full word strip ending with a dot
ela-k-2-show-and-tell/complete-sentence = row(box(w=70, h=90, color=RED, fill=soft(RED), rx=8), box(w=100, h=60, color=BLUE, fill=soft(BLUE), rx=8), box(w=80, h=60, color=BLUE, fill=soft(BLUE), rx=8), box(w=100, h=60, color=BLUE, fill=soft(BLUE), rx=8), dot(30, DARK, fill=DARK), gap=8, align='b')
# sequence: three numbered boxes joined by arrows
eld-6-12-telling-stories-and-experiences/sequence = boxes('1', '2', '3', colors=[GREEN, BLUE, ORANGE], size=60, w=100, h=100, arrows=True)
# size: five circles growing from small to large
health-pe-3-5-worries-and-coping/size = row(*[dot(s, BLUE, fill=soft(BLUE)) for s in (30, 50, 75, 100, 130)], gap=14, align='b')
# steps: three numbered boxes joined by arrows
social-studies-1-teddy-bear-makers/steps = row(box(T('1', 50), w=95, h=95, color=GREEN), arrow(50), box(T('2', 50), w=95, h=95, color=BLUE), arrow(50), box(T('3', 50), w=95, h=95, color=ORANGE), gap=8)
# supply chain: a cocoa pod, a factory and a store joined by arrows
social-studies-5-cocoa-chain/supply-chain = flow(raw(90, 130, '<ellipse cx="45" cy="65" rx="38" ry="60" fill="#c9852f" stroke="#1f2430" stroke-width="5"/><path d="M45 8 V122 M22 20 Q12 65 22 110 M68 20 Q78 65 68 110" fill="none" stroke="#8a5a1f" stroke-width="4"/>'), raw(130, 120, '<path d="M8 112 V50 L45 70 V50 L82 70 V20 H104 V112 Z" fill="#c4c7cf" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="24" y="82" width="18" height="18" fill="#f5c33b"/><rect x="58" y="82" width="18" height="18" fill="#f5c33b"/>'), house(120, ORANGE), length=50)
# majority: a pie chart with more than half shaded
social-studies-8-motion-on-the-floor/majority = pie(0.62, 280, GREEN)
# ---------- converted from paintings (WORDWALL-PAINTINGS.md CODE rows) ----------
# steady: an evenly spaced row of beats (checked) above a row that bunches up as it speeds up (crossed)
arts-k-2-steady-beat-and-rhythm/steady = col(row(T('steady', 40, GREEN), check(56), gap=10), raw(440, 64, ''.join(g(heart(56), x, 4) for x in (0, 76, 152, 228, 304, 380))), Item(10, 10, ''), row(T('speeding up', 40, RED), cross(50), gap=10), raw(440, 64, ''.join(g(heart(56, '#f4a3a3'), x, 4) for x in (0, 130, 230, 300, 348, 384))), gap=10, align='l')
# long sound: a long held bar ("mooooo") above a short one ("pop")
arts-k-2-steady-beat-and-rhythm/long-sound = col(row(T('long', 44, ORANGE), over(raw(380, 80, '<rect x="4" y="4" width="372" height="72" rx="20" fill="#f08a24" stroke="#1f2430" stroke-width="5"/>'), T('moooooooo', 46, '#fff')), gap=18), row(T('short', 44, GRAY), raw(380, 80, '<rect x="4" y="4" width="80" height="72" rx="20" fill="#c9ced8" stroke="#1f2430" stroke-width="5"/>'), gap=18), gap=30, align='l')
# pitch: notes climbing stairs from low (a bear) to high (a bird)
arts-k-2-high-and-low-loud-and-soft/pitch = raw(460, 420, '<path d="M95 410 V360 H180 V295 H265 V230 H350 V165 H450" fill="none" stroke="#b4b8c2" stroke-width="6" stroke-dasharray="12 8"/>' + ''.join(g(note('q', 70), x, y) for x, y in ((112, 286), (197, 221), (282, 156), (367, 91))) + g(bear(84), 2, 290) + g(bird(84), 370, 0) + '<text x="44" y="412" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="middle" fill="#a0673a">low</text><text x="355" y="48" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#3a7bd5">high</text>')
# chord: three notes (G, B, D) stacked on a staff, played together
arts-6-8-harmony-and-chords/chord = col(over(row(staff([(2, 4, 6)], size=260, w=260, colors=[BLUE]), Item(60, 160, ''), gap=0), raw(320, 160, ''.join(f'<line x1="224" y1="{ny}" x2="266" y2="{ly - 9}" stroke="#3a7bd5" stroke-width="2.5"/><text x="272" y="{ly}" font-family="Segoe UI" font-size="30" font-weight="700" fill="#3a7bd5">{n}</text>' for n, ny, ly in (('G', 100, 150), ('B', 80, 100), ('D', 60, 50))))), T('G + B + D at the same time', 30), gap=8)
# polyrhythm: 3 even beats against 2 even beats in the same span, starting together
arts-6-8-music-around-the-world/polyrhythm = raw(470, 280, '<line x1="120" y1="10" x2="120" y2="250" stroke="#e04848" stroke-width="4" stroke-dasharray="10 7"/><line x1="460" y1="10" x2="460" y2="250" stroke="#e04848" stroke-width="4" stroke-dasharray="10 7"/>' + ''.join(f'<rect x="{120 + i * 340 / 6:.1f}" y="40" width="{340 / 6:.1f}" height="70" fill="{"#3a7bd5" if i % 2 == 0 else "#fff"}" stroke="#1f2430" stroke-width="3"/>' for i in range(6)) + ''.join(f'<rect x="{120 + i * 340 / 6:.1f}" y="150" width="{340 / 6:.1f}" height="70" fill="{"#f08a24" if i % 3 == 0 else "#fff"}" stroke="#1f2430" stroke-width="3"/>' for i in range(6)) + '<text x="100" y="88" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="end" fill="#3a7bd5">3 beats</text><text x="100" y="198" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="end" fill="#f08a24">2 beats</text><text x="290" y="272" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">same time</text>')
# timbre: the same note drawn as three wave shapes, flute (smooth), violin (sawtooth) and trumpet (bright)
arts-6-8-music-around-the-world/timbre = (lambda wv: col(*[row(T(n, 32, c), raw(330, 90, '<line x1="0" y1="45" x2="330" y2="45" stroke="#d9dbe2" stroke-width="2"/><path d="M' + ' L'.join(f'{i * 330 / 300:.1f} {45 - 36 * f(i / 300 * 4 * math.pi):.1f}' for i in range(301)) + f'" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/>'), gap=14) for n, c, f in (('flute', BLUE, lambda t: math.sin(t)), ('violin', ORANGE, lambda t: sum(math.sin(k * t) / k for k in range(1, 9)) / 1.7), ('trumpet', RED, lambda t: (math.sin(t) + 0.9 * math.sin(2 * t + 1) + 0.7 * math.sin(3 * t + 2) + 0.5 * math.sin(4 * t)) / 2.2))], T('same note, different sound color', 28, GRAY), gap=14, align='l'))(None)
# if-then: a diamond asks "Is it dark?"; yes turns the light on, no leaves it off
computer-science-3-if-this-then-that/if-then = col(raw(300, 180, '<path d="M150 6 L294 90 L150 174 L6 90 Z" fill="#fde3c8" stroke="#f08a24" stroke-width="6" stroke-linejoin="round"/><text x="150" y="80" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#1f2430">Is it</text><text x="150" y="122" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#1f2430">dark?</text>'), raw(360, 70, '<path d="M180 0 V20 M60 20 H300 M60 20 V58 M300 20 V58" fill="none" stroke="#1f2430" stroke-width="5"/><path d="M60 68 l-9 -14 h18 z M300 68 l-9 -14 h18 z" fill="#1f2430"/>'), row(col(T('yes', 34, GREEN), Item(10, 10, ''), lightbulb_on(100), T('light on', 28), gap=4), Item(70, 10, ''), col(T('no', 34, RED), Item(10, 10, ''), bulb(84, '#d9dbe2'), T('light off', 28), gap=4), gap=60, align='t'), gap=0)
# algorithm: four numbered steps (up, up, right, right) that move a robot along a grid to the cheese
computer-science-1-code-a-path/algorithm = row(col(*[row(box(T(str(i + 1), 30, '#fff'), w=50, h=50, color=BLUE, fill=BLUE, rx=10), box(arrow(46, ORANGE, d, sw=7), w=80, h=58, color=GRAY, fill='#fff', rx=10), gap=8) for i, d in enumerate(('up', 'up', 'right', 'right'))], gap=10), raw(270, 270, ''.join(f'<rect x="{c * 90}" y="{r * 90}" width="90" height="90" fill="#fff" stroke="#c4c8d0" stroke-width="3"/>' for r in range(3) for c in range(3)) + '<path d="M45 225 V45 H200" fill="none" stroke="#f08a24" stroke-width="7" stroke-dasharray="14 9"/><rect x="20" y="198" width="50" height="46" rx="8" fill="#8a8f9c" stroke="#1f2430" stroke-width="4"/><circle cx="35" cy="218" r="5" fill="#fff"/><circle cx="55" cy="218" r="5" fill="#fff"/><line x1="45" y1="198" x2="45" y2="186" stroke="#1f2430" stroke-width="4"/><circle cx="45" cy="184" r="5" fill="#e04848"/><path d="M190 72 L262 72 L262 22 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><circle cx="236" cy="58" r="6" fill="#d9a520"/><circle cx="252" cy="44" r="4" fill="#d9a520"/>'), gap=24)
# model: labeled photos (training data) go into the model, which then guesses about a new photo
computer-science-6-8-machine-learning-models/model = col(row(col(T('training data', 26, GRAY), grid([card(bird(46), 70, 70, BLUE), card(cat_icon(44), 70, 70, ORANGE), card(bird(46), 70, 70, BLUE), card(cat_icon(44), 70, 70, ORANGE)], 2, gap=8), gap=6), arrow(50), box(col(gear(70), T('model', 30), gap=4), color=PURPLE, p=16), gap=10), arrow(50, dir='down'), row(card(bird(56, ORANGE), 90, 90, GRAY), arrow(40), box(T('bird!', 36, DARK), color=GREEN, p=14), gap=10), T('new photo, prediction', 26, GRAY), gap=6)
# false positive: predicted yes, actually no (the model says "dog" but it is a cat)
computer-science-6-8-machine-learning-models/false-positive = grid2x2(('dog', 'cat'), ('"dog"', '"not dog"'), ('right', 'false\npositive', 'false\nnegative', 'right'), hl=1, title=('really is a...', 'model says'))
# main idea: the table top (main idea) held up by three legs (details)
ela-3-main-idea-and-key-details/main-idea = argue(top='main idea', mid='detail', bottom=None, n=3, hl='top', texts={'top': 'main idea: Bees help plants grow.'})
# key detail: the main idea held up by details, one key detail picked out
ela-3-main-idea-and-key-details/key-detail = argue(top='main idea', mid='detail', bottom=None, n=3, hl='mid', pick=0, texts={'top': 'Bees help plants grow.', 'mid': ['key detail', 'detail', 'detail']})
# topic sentence: a paragraph of bars with the first bar highlighted
ela-3-opinion-and-informative-writing/topic-sentence = col(T('topic sentence', 34, ORANGE), arrow(36, ORANGE, 'down', sw=6), raw(400, 230, '<rect x="40" y="6" width="350" height="34" rx="10" fill="#fde97a" stroke="#f08a24" stroke-width="5"/><rect x="50" y="15" width="330" height="16" rx="8" fill="#1f2430"/>' + ''.join(f'<rect x="10" y="{56 + i * 36}" width="{(380, 370, 385, 360, 250)[i]}" height="16" rx="8" fill="#b4b8c2"/>' for i in range(5))), gap=2)
# narrative: a camping trip told in order, beginning, middle and end
ela-3-narrative-writing/narrative = parts3([car(110, RED), raw(120, 100, '<path d="M10 92 L60 12 L110 92 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M60 92 L48 92 L60 50 L72 92 Z" fill="#1f2430"/>'), house(110, ORANGE)], numbers=True)
# beginning sound: a dog beside sound boxes d-o-g, the first box picked out
ela-k-rhymes-and-sounds/beginning-sound = col(dog_icon(150), row(tile('d', ORANGE, 120), tile('o', GRAY, 120, fill='#fff'), tile('g', GRAY, 120, fill='#fff'), gap=8), row(T('/d/', 52, ORANGE), Item(260, 10, ''), gap=0), gap=14)
# ending sound: a bus beside sound boxes b-u-s, the last box picked out
ela-k-rhymes-and-sounds/ending-sound = col(raw(220, 130, '<rect x="6" y="10" width="208" height="92" rx="16" fill="#f5c33b" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<rect x="{22 + i * 46}" y="24" width="34" height="30" rx="5" fill="#d6e6fb" stroke="#1f2430" stroke-width="3"/>' for i in range(4)) + '<rect x="6" y="70" width="208" height="8" fill="#1f2430"/><circle cx="54" cy="104" r="18" fill="#1f2430"/><circle cx="168" cy="104" r="18" fill="#1f2430"/><circle cx="54" cy="104" r="7" fill="#c9ccd1"/><circle cx="168" cy="104" r="7" fill="#c9ccd1"/>'), row(tile('b', GRAY, 120, fill='#fff'), tile('u', GRAY, 120, fill='#fff'), tile('s', ORANGE, 120), gap=8), row(Item(260, 10, ''), T('/s/', 52, ORANGE), gap=0), gap=14)
# blend: s and t slide together in "stop", and you hear both sounds
ela-1-phonics-blends-and-digraphs/blend = col(row(tile('s', BLUE, 120), T('+', 70), tile('t', ORANGE, 120), gap=12), arrow(50, dir='down'), row(raw(130, 130, '<polygon points="' + ' '.join(f'{65 + 60 * math.cos(math.radians(22.5 + 45 * k)):.1f},{65 + 60 * math.sin(math.radians(22.5 + 45 * k)):.1f}' for k in range(8)) + '" fill="#e04848" stroke="#1f2430" stroke-width="5"/>'), T('stop', 120, hl={'s': BLUE, 't': ORANGE}, under='st'), gap=24), T('/s/ + /t/, hear both', 36, GRAY), gap=10)
# next: three steps in a morning (wake up, breakfast, school), the second picked out
ela-1-writing-sentences-and-stories/next = parts3([sun(100), raw(130, 90, '<path d="M8 30 H122 C122 70 98 86 65 86 C32 86 8 70 8 30 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#f5c33b" stroke="#1f2430" stroke-width="2"/>' for x, y in ((40, 24), (60, 20), (80, 25), (100, 22), (50, 30)))), raw(130, 120, '<rect x="10" y="44" width="110" height="72" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M4 48 L65 12 L126 48 Z" fill="#a0673a" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="52" y="80" width="26" height="36" fill="#fff" stroke="#1f2430" stroke-width="4"/><rect x="22" y="58" width="20" height="18" fill="#d6e6fb" stroke="#1f2430" stroke-width="3"/><rect x="88" y="58" width="20" height="18" fill="#d6e6fb" stroke="#1f2430" stroke-width="3"/><line x1="65" y1="12" x2="65" y2="0" stroke="#1f2430" stroke-width="3"/>')], labels=('first', 'next', 'last'), hl=1)
# last: the same three steps, the final one picked out
ela-1-writing-sentences-and-stories/last = parts3([sun(100), raw(130, 90, '<path d="M8 30 H122 C122 70 98 86 65 86 C32 86 8 70 8 30 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#f5c33b" stroke="#1f2430" stroke-width="2"/>' for x, y in ((40, 24), (60, 20), (80, 25), (100, 22), (50, 30)))), raw(130, 120, '<rect x="10" y="44" width="110" height="72" fill="#e04848" stroke="#1f2430" stroke-width="5"/><path d="M4 48 L65 12 L126 48 Z" fill="#a0673a" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="52" y="80" width="26" height="36" fill="#fff" stroke="#1f2430" stroke-width="4"/><rect x="22" y="58" width="20" height="18" fill="#d6e6fb" stroke="#1f2430" stroke-width="3"/><rect x="88" y="58" width="20" height="18" fill="#d6e6fb" stroke="#1f2430" stroke-width="3"/><line x1="65" y1="12" x2="65" y2="0" stroke="#1f2430" stroke-width="3"/>')], labels=('first', 'next', 'last'), hl=2)
# meaning: the word card "tiny" points to what it tells you, very small
ela-1-word-meanings/meaning = row(tile('tiny', BLUE, 120), arrow(70), box(col(raw(220, 110, '<g opacity="0.3">' + g(bug(100), 110, 4) + '</g>' + g(bug(34), 30, 50) + '<circle cx="47" cy="67" r="30" fill="none" stroke="#e04848" stroke-width="5"/>'), T('very small', 34, ORANGE), gap=8), color=GREEN, fill='#fff', p=20), gap=10)
# vowel team: e and a share one tile in "seat" and make one sound
ela-2-long-vowels-and-two-syllable-words/vowel-team = col(row(tile('s', GRAY, 130, fill='#fff'), tile('ea', ORANGE, 130), tile('t', GRAY, 130, fill='#fff'), gap=8), T('two vowels, one sound: long e', 34, ORANGE), gap=16)
# syllable: rab and bit, one clap each
ela-2-long-vowels-and-two-syllable-words/syllable = col(row(*[col(raw(90, 60, '<path d="M14 50 L45 8 L76 50" fill="none" stroke="#f08a24" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'), T('clap', 28, ORANGE), gap=0) for _ in range(2)], gap=110), row(tile('rab', BLUE, 140), tile('bit', ORANGE, 140), gap=10), T('rabbit = 2 syllables', 40), gap=12)
# paragraph: sentence bars that all point to one idea, my dog
ela-2-paragraph-writing/paragraph = raw(470, 300, '<rect x="2" y="2" width="300" height="296" rx="14" fill="#fff" stroke="#c4c8d0" stroke-width="4"/>' + ''.join(f'<rect x="{50 if i == 0 else 22}" y="{30 + i * 52}" width="{(230, 258, 240, 255, 170)[i]}" height="18" rx="9" fill="#8a8f9c"/><line x1="{(280, 280, 262, 277, 192)[i] + 6}" y1="{39 + i * 52}" x2="356" y2="150" stroke="#f08a24" stroke-width="3"/>' for i in range(5)) + '<circle cx="404" cy="150" r="62" fill="#fde3c8" stroke="#f08a24" stroke-width="6"/>' + g(dog_icon(82), 363, 112) + '<text x="404" y="238" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#f08a24">one idea</text>')
# topic sentence: a paragraph of bars with the first bar highlighted
ela-2-paragraph-writing/topic-sentence = col(T('topic sentence', 34, ORANGE), arrow(36, ORANGE, 'down', sw=6), raw(400, 230, '<rect x="40" y="6" width="350" height="34" rx="10" fill="#fde97a" stroke="#f08a24" stroke-width="5"/><rect x="50" y="15" width="330" height="16" rx="8" fill="#1f2430"/>' + ''.join(f'<rect x="10" y="{56 + i * 36}" width="{(380, 370, 385, 360, 250)[i]}" height="16" rx="8" fill="#b4b8c2"/>' for i in range(5))), gap=2)
# compare and contrast: a Venn diagram of frogs and toads, shared traits in the middle
ela-4-text-structures/compare-and-contrast = raw(440, 360, '<circle cx="150" cy="200" r="135" fill="#d6e6fb" fill-opacity="0.85" stroke="#3a7bd5" stroke-width="6"/><circle cx="290" cy="200" r="135" fill="#fde3c8" fill-opacity="0.7" stroke="#f08a24" stroke-width="6"/><circle cx="150" cy="200" r="135" fill="none" stroke="#3a7bd5" stroke-width="6"/><text x="110" y="44" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#3a7bd5">frog</text><text x="330" y="44" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#f08a24">toad</text>' + ''.join(f'<text x="{x}" y="{y}" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#1f2430">{s}</text>' for x, y, s in ((85, 160, 'smooth,'), (85, 186, 'wet skin'), (85, 240, 'long legs'), (220, 160, 'lay eggs'), (220, 186, 'in water'), (220, 240, 'eat bugs'), (355, 160, 'bumpy,'), (355, 186, 'dry skin'), (355, 240, 'short legs'))))
# firsthand account: someone who was in the storm writes it in a diary
ela-4-firsthand-and-secondhand-accounts/firsthand-account = flow(col(raincloud(130), person(90, BLUE), T('was there', 30, BLUE), gap=4), col(book(130, BLUE, open_=False), T('diary', 30), gap=8), length=60)
# secondhand account: someone who was not there writes about the storm later, in a textbook
ela-4-firsthand-and-secondhand-accounts/secondhand-account = flow(col(raincloud(130), person(96, BLUE), T('was there', 30, BLUE), gap=4), col(row(person(96, ORANGE), book(100, ORANGE, open_=False), gap=8), T('was not there,', 30, ORANGE), T('wrote it later', 30, ORANGE), gap=4), length=50)
# claim: the claim on top, held up by reasons resting on evidence
ela-4-writing-with-evidence/claim = argue(hl='top', texts={'top': 'claim: Schools should have gardens.'})
# adjective order: describing words in the usual order, opinion, size, age, color, then the noun
ela-4-grammar-in-use/adjective-order = col(*[row(box(T(str(i + 1), 30, '#fff'), w=50, h=50, color=c, fill=c, rx=25), box(T(t, 26, c), w=130, h=50, color=c, fill='#fff', rx=10), T(w, 40), gap=12) for i, (t, w, c) in enumerate((('opinion', 'lovely', PURPLE), ('size', 'big', BLUE), ('age', 'old', TEAL), ('color', 'red', RED)))], T('a lovely big old red ball', 34, hl={'lovely': PURPLE, 'big': BLUE, 'old': TEAL, 'red': RED}), gap=10, align='l')
# reason: a point held up by reasons, the reasons picked out
ela-5-reasons-and-evidence/reason = argue(top='point', mid='reason', bottom=None, n=3, hl='mid', texts={'top': 'point: Save the bees.'})
# point: the main idea the author wants you to accept, held up by reasons
ela-5-reasons-and-evidence/point = argue(top='point', mid='reason', bottom=None, n=3, hl='top', texts={'top': 'point: Bees feed the world.'})
# thesis: an essay outline, the last sentence of the introduction is the thesis
ela-5-organized-essays/thesis = raw(470, 420, ''.join(f'<rect x="150" y="{y}" width="310" height="{h}" rx="12" fill="{c}" stroke="#1f2430" stroke-width="3"/><text x="136" y="{ty}" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="end" fill="#1f2430">{n}</text>' for y, h, c, n, ty in ((4, 112, "#d6e6fb", "introduction", 34), (128, 66, "#eceef2", "body", 170), (204, 66, "#eceef2", "body", 246), (280, 66, "#eceef2", "body", 322), (356, 60, "#d3f0de", "conclusion", 395))) + ''.join(f'<rect x="166" y="{y}" width="{w}" height="12" rx="6" fill="#8a8f9c"/>' for y, w in ((16, 270), (40, 250), (144, 270), (166, 210), (220, 260), (242, 200), (296, 270), (318, 230), (370, 260), (392, 180))) + '<rect x="160" y="60" width="292" height="44" rx="8" fill="#fde97a" stroke="#f08a24" stroke-width="5"/><rect x="170" y="76" width="262" height="12" rx="6" fill="#1f2430"/><text x="136" y="92" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="end" fill="#f08a24">thesis →</text>')
# exposition: the plot mountain with the opening picked out
ela-6-plot-and-character-development/exposition = plot_arc(0)
# rising action: the plot mountain with the climb picked out
ela-6-plot-and-character-development/rising-action = plot_arc(1)
# climax: the plot mountain with the peak picked out
ela-6-plot-and-character-development/climax = plot_arc(2)
# falling action: the plot mountain with the way down picked out
ela-6-plot-and-character-development/falling-action = plot_arc(3)
# resolution: the plot mountain with the ending picked out
ela-6-plot-and-character-development/resolution = plot_arc(4)
# central idea: the central idea in the middle, supporting details all around it
ela-6-central-idea-and-summary/central-idea = raw(460, 400, ''.join(f'<line x1="230" y1="200" x2="{x}" y2="{y}" stroke="#8a8f9c" stroke-width="6"/>' for x, y in ((80, 60), (380, 60), (80, 340), (380, 340))) + ''.join(f'<rect x="{x - 75}" y="{y - 32}" width="150" height="64" rx="14" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="5"/><text x="{x}" y="{y + 10}" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">detail</text>' for x, y in ((80, 60), (380, 60), (80, 340), (380, 340))) + '<circle cx="230" cy="200" r="98" fill="#fde3c8" stroke="#f08a24" stroke-width="7"/><text x="230" y="192" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="middle" fill="#1f2430">central</text><text x="230" y="230" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="middle" fill="#1f2430">idea</text>')
# argument: a claim held up by reasons, each resting on evidence
ela-6-tracing-an-argument/argument = argue(texts={'top': 'claim: School should start later.'})
# reason: the claim-reason-evidence diagram with the reasons picked out
ela-6-tracing-an-argument/reason = argue(hl='mid', texts={'top': 'School should start later.', 'mid': ['Teens need sleep.', 'reason']})
# antecedent: "Maria lost her pen." with an arrow from her back to Maria
ela-6-pronouns-and-sentence-variety/antecedent = tagged('In', ('Maria', BLUE, 'antecedent'), 'lost', ('her', ORANGE, 'pronoun'), 'pen.', links=[(3, 1, ORANGE)])
# agreement: a plural noun matched with a plural pronoun (checked) and with a singular one (crossed)
ela-6-pronouns-and-sentence-variety/agreement = col(row(tagged('The', ('birds', GREEN, 'plural'), 'built', ('their', GREEN, 'plural'), 'nest.', size=44, ts=0.66), check(64), gap=10), row(tagged('The', ('birds', RED, 'plural'), 'built', ('its', RED, 'singular'), 'nest.', size=44, ts=0.66), cross(56), gap=10), gap=36, align='l')
# context clues: the clue words around "arid" tell what it means
ela-6-connotation-and-context/context-clues = col(tagged('The', ('arid', ORANGE, '?'), 'land got', ('no rain', GREEN, 'clue'), size=42, ts=0.66), tagged('and the plants', ('dried up.', GREEN, 'clue'), size=42, ts=0.66), box(T('arid = very dry', 40, ORANGE), color=ORANGE, fill='#fff', p=30), gap=18)
# alliteration: "Silent snow sleeps," every word starting with the same s sound
ela-7-sound-and-form-in-poetry/alliteration = raw(420, 380, '<rect x="44" y="14" width="66" height="352" rx="20" fill="#f9d4d4"/>' + ''.join(f'<text x="50" y="{100 + i * 120}" font-family="Segoe UI" font-size="96" font-weight="700" fill="#1f2430"><tspan fill="#e04848">{w[0]}</tspan>{w[1:]}</text>' for i, w in enumerate(('Silent', 'snow', 'sleeps'))))
# sonnet: fourteen lines in four groups, rhyme letters ABAB CDCD EFEF GG down the side
ela-7-sound-and-form-in-poetry/sonnet = raw(470, 470, ''.join(f'<text x="30" y="{14 + i * 31 + (i // 4) * 12 + 18}" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="{c}">{l}</text><rect x="58" y="{14 + i * 31 + (i // 4) * 12 + 4}" width="{(300, 280, 296, 270, 290, 300, 276, 288, 300, 284, 292, 270, 300, 280)[i]}" height="14" rx="7" fill="{c}" opacity="0.75"/>' for i, (l, c) in enumerate(zip('ABABCDCDEFEFGG', ('#3a7bd5', '#f08a24') * 2 + ('#2f9e5b', '#8e5bc4') * 2 + ('#e04848', '#1d9a9a') * 2 + ('#a0673a', '#a0673a')))) + '<path d="M372 16 H386 V466 H372" fill="none" stroke="#1f2430" stroke-width="5"/><text x="400" y="232" font-family="Segoe UI" font-size="40" font-weight="700" fill="#1f2430">14</text><text x="400" y="266" font-family="Segoe UI" font-size="26" font-weight="700" fill="#1f2430">lines</text>')
# counterclaim: my claim and the opposing claim pushing against each other
ela-7-argument-with-counterclaims/counterclaim = col(box(col(T('my claim', 28, BLUE), T('Uniforms help', 34), T('students focus.', 34), gap=0), w=400, h=150, color=BLUE, fill='#fff'), row(arrow(60, BLUE, 'down', sw=9), arrow(60, ORANGE, 'up', sw=9), gap=20), box(col(T('counterclaim', 28, ORANGE), T('Uniforms limit', 34), T('self-expression.', 34), gap=0), w=400, h=150, color=ORANGE, fill=soft(ORANGE), sw=7), gap=6)
# position: a line between two sides of an issue with a pin placed toward one side
ela-7-argument-with-counterclaims/position = raw(470, 250, '<line x1="30" y1="150" x2="440" y2="150" stroke="#1f2430" stroke-width="7"/><circle cx="30" cy="150" r="12" fill="#3a7bd5"/><circle cx="440" cy="150" r="12" fill="#e04848"/><text x="40" y="200" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#3a7bd5">less</text><text x="40" y="230" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#3a7bd5">homework</text><text x="430" y="200" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">more</text><text x="430" y="230" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">homework</text>' + g(pin(90, ORANGE), 104, 64) + '<text x="150" y="44" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#f08a24">my position</text>')
# domain-specific vocabulary: three subjects, each with its own words
ela-7-informative-writing/domain-specific-vocabulary = row(*[col(box(T(s, 30, '#fff'), w=136, h=56, color=c, fill=c, rx=10), box(col(T(a, 28), T(b, 28), gap=6), w=136, h=110, color=c, fill='#fff', rx=10), gap=0) for s, c, a, b in (('science', GREEN, 'magma', 'cell'), ('math', BLUE, 'ratio', 'integer'), ('music', PURPLE, 'tempo', 'chord'))], gap=14)
# clause: "When the bell rang" has a subject and a verb
ela-7-phrases-clauses-and-sentence-types/clause = tagged('When', ('the bell', BLUE, 'subject'), ('rang', ORANGE, 'verb'), top=('clause', PURPLE), size=52)
# phrase: "After lunch" is a group of words with no subject and verb
ela-7-phrases-clauses-and-sentence-types/phrase = col(tagged('After', 'lunch', top=('phrase', PURPLE), size=64), row(T('subject?', 34, GRAY), cross(40), Item(30, 10, ''), T('verb?', 34, GRAY), cross(40), gap=8), gap=24)
# independent clause: "I ran home." has a subject and a verb and stands alone
ela-7-phrases-clauses-and-sentence-types/independent-clause = col(row(tagged(('I', BLUE, 'subject'), ('ran', ORANGE, 'verb'), 'home.', size=60), check(70), gap=16), T('stands alone as a sentence', 30, GREEN), gap=16)
# dependent clause: "Because it rained" cannot stand alone; it leans on a clause that can
ela-7-phrases-clauses-and-sentence-types/dependent-clause = col(row(tagged(('Because it rained', ORANGE), size=50), cross(56), gap=14), T('cannot stand alone', 32, RED), Item(10, 20, ''), row(col(tagged(('Because it rained,', ORANGE), size=44), tagged(('we stayed inside.', BLUE), size=44), gap=10, align='l'), check(64), gap=14), T('leans on a clause that can', 32, GREEN), gap=8, align='l')
# discrepancy: two sources give different dates for the same event, the mismatch circled
ela-8-conflicting-information/discrepancy = row(box(col(T('source 1', 26, GRAY), T('Bridge opened', 28), T('1932', 48, circle='1932'), gap=4), color=BLUE, fill='#fff', p=16), T('≠', 70, RED), box(col(T('source 2', 26, GRAY), T('Bridge opened', 28), T('1937', 48, circle='1937'), gap=4), color=BLUE, fill='#fff', p=16), gap=10)
# transition: two scenes joined by "Years later," a small tree, then a tall one
ela-8-narrative-techniques/transition = row(card(col(Item(10, 90, ''), tree(70), gap=0), 160, 200, BLUE), col(T('Years later,', 34, ORANGE), arrow(120, ORANGE), gap=0), card(tree(170), 160, 200, BLUE), gap=8)
# gerund: swim + ing becomes a noun, "Swimming is fun."
ela-8-verbals-and-voice/gerund = col(row(tile('swim', BLUE, 90), T('+', 50), tile('ing', ORANGE, 90), gap=8), arrow(40, dir='down'), tagged(('Swimming', PURPLE, 'noun'), 'is', 'fun.', size=56), gap=8)
# infinitive: to + win, "I want to win."
ela-8-verbals-and-voice/infinitive = col(row(tile('to', ORANGE, 100), T('+', 56), tile('win', BLUE, 100), gap=8), arrow(40, dir='down'), tagged('I', 'want', ('to win.', PURPLE, 'infinitive'), size=56), gap=8)
# active voice: the subject (the dog) does the chasing
ela-8-verbals-and-voice/active-voice = tagged('The', ('dog', BLUE, 'does it'), ('chased', ORANGE, 'action'), 'the', ('cat.', PURPLE, 'gets it'), size=46, links=[(1, 4, BLUE)], ts=0.7)
# passive voice: the subject (the cat) receives the chasing
ela-8-verbals-and-voice/passive-voice = tagged('The', ('cat', PURPLE, 'gets it'), ('was chased', ORANGE, 'action'), 'by the', ('dog.', BLUE, 'does it'), size=42, links=[(4, 1, BLUE)], ts=0.8, gap=8)
# beginning: three story panels, the first (the frog is lost) picked out
eld-k-2-retelling-stories/beginning = parts3([row(frog(80), T('?', 70, BLUE), gap=4), row(frog(70), raw(70, 60, '<rect x="4" y="4" width="62" height="52" fill="#fdf0c4" stroke="#1f2430" stroke-width="4"/><path d="M12 46 Q30 20 46 34 T60 14" fill="none" stroke="#e04848" stroke-width="3" stroke-dasharray="6 4"/>'), gap=4), row(frog(70), house(70, ORANGE), gap=4)], hl=0)
# middle: three story panels, the middle one (the frog finds a map) picked out
eld-k-2-retelling-stories/middle = parts3([row(frog(80), T('?', 70, BLUE), gap=4), row(frog(70), raw(70, 60, '<rect x="4" y="4" width="62" height="52" fill="#fdf0c4" stroke="#1f2430" stroke-width="4"/><path d="M12 46 Q30 20 46 34 T60 14" fill="none" stroke="#e04848" stroke-width="3" stroke-dasharray="6 4"/>'), gap=4), row(frog(70), house(70, ORANGE), gap=4)], hl=1)
# end: three story panels, the last one (the frog gets home) picked out
eld-k-2-retelling-stories/end = parts3([row(frog(80), T('?', 70, BLUE), gap=4), row(frog(70), raw(70, 60, '<rect x="4" y="4" width="62" height="52" fill="#fdf0c4" stroke="#1f2430" stroke-width="4"/><path d="M12 46 Q30 20 46 34 T60 14" fill="none" stroke="#e04848" stroke-width="3" stroke-dasharray="6 4"/>'), gap=4), row(frog(70), house(70, ORANGE), gap=4)], hl=2)
# because: an opinion joined to its reason by "because"
eld-3-5-opinions-with-reasons/because = col(T('opinion', 30, BLUE), box(T('I like winter', 40), w=400, h=100, color=BLUE), row(arrow(70, ORANGE, 'down', sw=9), T('because', 46, ORANGE), gap=16), T('reason', 30, GREEN), box(T('I can sled.', 40), w=400, h=100, color=GREEN), gap=6)
# for example: a point joined to a detail that supports it
eld-3-5-opinions-with-reasons/for-example = col(T('point', 30, BLUE), box(T('Dogs are smart;', 40), w=420, h=100, color=BLUE), row(arrow(70, ORANGE, 'down', sw=9), T('for example,', 44, ORANGE), gap=16), T('detail', 30, GREEN), box(T('they can learn tricks.', 38), w=420, h=100, color=GREEN), gap=6)
# so: a cause joined to its result by "so"
eld-3-5-cause-and-effect-language/so = col(T('cause', 30, BLUE), box(row(moon(60), T('It was dark,', 40), gap=16), w=460, h=110, color=BLUE), row(arrow(70, ORANGE, 'down', sw=9), T('so', 52, ORANGE), gap=16), T('result', 30, GREEN), box(row(lightbulb_on(64), T('we turned on the lamp.', 32), gap=12), w=460, h=110, color=GREEN), gap=6)
# therefore: a reason joined to what follows from it
eld-3-5-cause-and-effect-language/therefore = col(T('reason', 30, BLUE), box(row(sun(56), T('Plants need light;', 38), gap=14), w=440, h=110, color=BLUE), row(arrow(70, ORANGE, 'down', sw=9), T('therefore,', 48, ORANGE), gap=16), T('result', 30, GREEN), box(col(T('the plant grew', 36), T('toward the window.', 36), gap=0), w=440, h=120, color=GREEN), gap=6)
# century: a timeline from 1900 to 2000, ten decades, 100 years
eld-3-5-then-and-now-language/century = col(T('1 century = 100 years', 40, ORANGE), numberline(1900, 2000, 460, step=10, every=5, bracket=(1900, 2000, '100 years'), seg=(1900, 2000), color=ORANGE), T('10 decades', 30, GRAY), gap=6)
# per: three bags with 4 apples in each, 4 apples per bag
eld-6-8-word-problems-decoded/per = col(row(*[bag(150, inner=grid([apple(40)] * 4, 2, gap=4)) for _ in range(3)], gap=20), T('4 apples per bag', 44, ORANGE), T('(4 for each bag)', 32, GRAY), gap=12)
# total: 5 counters and 3 counters joined into one group of 8
eld-6-8-word-problems-decoded/total = col(row(dots(5, size=34, color=BLUE), T('+', 56), dots(3, size=34, color=ORANGE), gap=14), arrow(40, dir='down'), box(dots(8, size=34, colors=[BLUE] * 5 + [ORANGE] * 3), color=GREEN, fill='#fff', p=14), T('total = 8', 44, GREEN), gap=8)
# difference: a $70 bar and a $50 bar, the $20 gap marked
eld-6-8-word-problems-decoded/difference = raw(470, 260, '<rect x="80" y="30" width="350" height="64" rx="6" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><rect x="80" y="130" width="250" height="64" rx="6" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><rect x="330" y="130" width="100" height="64" rx="6" fill="#fde97a" stroke="#e04848" stroke-width="4" stroke-dasharray="10 6"/><text x="70" y="74" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#3a7bd5">$70</text><text x="70" y="174" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#f08a24">$50</text><text x="380" y="173" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#e04848">$20</text><text x="380" y="240" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#e04848">difference</text>')
# at most: a number line with a closed dot at 10 and everything below it shaded
eld-6-8-word-problems-decoded/at-most = col(T('at most 10', 44, ORANGE), numberline(0, 12, 460, closed=10, ray='left', color=ORANGE, hl=10), T('10 or fewer', 34, GRAY), gap=6)
# how many more: Ana's row of 7 lined up with Luis's row of 4, the 3 extra picked out
eld-6-8-word-problems-decoded/how-many-more = raw(470, 300, '<text x="80" y="78" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#1f2430">Ana</text><text x="80" y="168" font-family="Segoe UI" font-size="34" font-weight="700" text-anchor="end" fill="#1f2430">Luis</text>' + ''.join(f'<circle cx="{120 + i * 50}" cy="66" r="20" fill="{"#f08a24" if i > 3 else "#3a7bd5"}" stroke="#1f2430" stroke-width="3"/>' for i in range(7)) + ''.join(f'<circle cx="{120 + i * 50}" cy="156" r="20" fill="#3a7bd5" stroke="#1f2430" stroke-width="3"/><line x1="{120 + i * 50}" y1="90" x2="{120 + i * 50}" y2="132" stroke="#b4b8c2" stroke-width="3" stroke-dasharray="6 5"/>' for i in range(4)) + '<rect x="294" y="36" width="162" height="60" rx="30" fill="none" stroke="#f08a24" stroke-width="5"/><text x="375" y="160" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#8a8f9c">no match</text><text x="375" y="250" font-family="Segoe UI" font-size="52" font-weight="700" text-anchor="middle" fill="#f08a24">3 more</text>')
# claim: a question and the claim that answers it
eld-6-8-lab-reports-and-claims/claim = col(box(col(T('question', 26, BLUE), T('Does salt water', 30), T('freeze more slowly?', 30), gap=0), w=380, h=140, color=BLUE, fill='#fff'), arrow(50, dir='down'), box(col(T('claim', 26, ORANGE), T('Salt water freezes', 30), T('more slowly.', 30), gap=0), w=380, h=140, color=ORANGE, sw=7), gap=4)
# nutrition label: a cereal's Nutrition Facts label with the sugar line picked out
health-pe-3-5-nutrition-labels-and-choices/nutrition-label = nutrition_label('sugars', 360)
# serving size: the label's serving size line picked out beside one cup of cereal
health-pe-3-5-nutrition-labels-and-choices/serving-size = row(nutrition_label('serving', 300), col(raw(150, 150, '<path d="M14 30 H116 L106 140 H24 Z" fill="#d6e6fb" fill-opacity="0.6" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M116 50 C150 50 150 100 112 104" fill="none" stroke="#1f2430" stroke-width="7"/><path d="M20 62 H110 L106 140 H24 Z" fill="#f5c33b"/>' + ''.join(f'<circle cx="{30 + (i % 5) * 18}" cy="{70 + (i // 5) * 16}" r="7" fill="#e0a530" stroke="#a0673a" stroke-width="2"/>' for i in range(20)) + '<path d="M14 30 H116 L106 140 H24 Z" fill="none" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><line x1="20" y1="62" x2="44" y2="62" stroke="#1f2430" stroke-width="4"/>'), T('1 cup', 40, ORANGE), gap=6), gap=20)
# growth spurt: a height-by-age line that climbs slowly, then steeply for a few years (picked out), then levels off
health-pe-3-5-growing-up/growth-spurt = (lambda rate: (lambda f: row(raw(40, 300, '<text x="28" y="150" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 28 150)">height</text>'), col(plot(f, (f, 10.6, 13.6), size=320, xr=(-0.5, 18.5), yr=(-5, 185), colors=(BLUE, ORANGE), sw=7, texts=[(8.4, 150, 'growth spurt', ORANGE)]), T('age (years) →', 28), gap=0), gap=0))(lambda x: 50 + sum(rate(i * 0.1) * 0.1 for i in range(int(max(x, 0) / 0.1)))))(lambda t: (5.2 + 9 * math.exp(-((t - 12) / 1.1) ** 2)) / (1 + math.exp((t - 15.5) * 2)))
# pass: a field from above, a curved arrow carries the ball from one teammate to an open teammate
health-pe-3-5-game-strategies/pass = raw(460, 320, '<rect x="4" y="4" width="452" height="312" rx="10" fill="#7fc98f" stroke="#1f2430" stroke-width="5"/><line x1="230" y1="4" x2="230" y2="316" stroke="#fff" stroke-width="5"/><circle cx="230" cy="160" r="50" fill="none" stroke="#fff" stroke-width="5"/><path d="M116 214 Q240 70 352 112" fill="none" stroke="#f5c33b" stroke-width="8" stroke-dasharray="16 10"/><path d="M362 116 l-26 -14 l4 22 z" fill="#f5c33b" stroke="#1f2430" stroke-width="2"/><circle cx="100" cy="226" r="26" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><circle cx="380" cy="116" r="26" fill="#3a7bd5" stroke="#1f2430" stroke-width="5"/><circle cx="270" cy="236" r="26" fill="#e04848" stroke="#1f2430" stroke-width="5"/><circle cx="128" cy="204" r="12" fill="#fff" stroke="#1f2430" stroke-width="4"/><text x="380" y="70" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">open</text><text x="100" y="290" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">teammate</text><text x="270" y="296" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">other team</text>')
# intensity: a dial from light to moderate to vigorous, the needle in vigorous
health-pe-6-8-personal-fitness-plans/intensity = raw(460, 300, ''.join(f'<path d="M{230 + 190 * math.cos(math.radians(a0)):.1f} {250 - 190 * math.sin(math.radians(a0)):.1f} A190 190 0 0 1 {230 + 190 * math.cos(math.radians(a1)):.1f} {250 - 190 * math.sin(math.radians(a1)):.1f}" fill="none" stroke="{c}" stroke-width="60"/>' for a0, a1, c in ((180, 120, '#2f9e5b'), (120, 60, '#f5c33b'), (60, 0, '#e04848'))) + ''.join(f'<text x="{230 + 190 * math.cos(math.radians(a)):.1f}" y="{250 - 190 * math.sin(math.radians(a)) + 9:.1f}" font-family="Segoe UI" font-size="{fs}" font-weight="700" text-anchor="middle" fill="#fff" transform="rotate({90 - a} {230 + 190 * math.cos(math.radians(a)):.1f} {250 - 190 * math.sin(math.radians(a)):.1f})">{s}</text>' for a, s, fs in ((150, 'light', 28), (90, 'moderate', 28), (30, 'vigorous', 28))) + f'<line x1="230" y1="250" x2="{230 + 130 * math.cos(math.radians(38)):.1f}" y2="{250 - 130 * math.sin(math.radians(38)):.1f}" stroke="#1f2430" stroke-width="10" stroke-linecap="round"/><circle cx="230" cy="250" r="16" fill="#1f2430"/><text x="40" y="294" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#2f9e5b">easy</text><text x="420" y="294" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">hard</text>')
# square foot: a square 1 foot on each side, shaded
math-3-area/square-foot = raw(400, 390, '<rect x="40" y="20" width="280" height="280" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/><text x="180" y="150" font-family="Segoe UI" font-size="44" font-weight="700" text-anchor="middle" fill="#3a7bd5">1 square</text><text x="180" y="200" font-family="Segoe UI" font-size="44" font-weight="700" text-anchor="middle" fill="#3a7bd5">foot</text><text x="180" y="372" font-family="Segoe UI" font-size="38" font-weight="700" text-anchor="middle" fill="#e04848">1 ft</text><text x="384" y="160" font-family="Segoe UI" font-size="38" font-weight="700" text-anchor="middle" fill="#e04848" transform="rotate(90 384 160)">1 ft</text><path d="M40 316 V328 H320 V316 M336 20 H348 V300 H336" fill="none" stroke="#e04848" stroke-width="4"/>')
# measure: a pencil laid along a ruler from 0, reaching the 6
math-3-perimeter/measure = col(raw(460, 60, '<path d="M25 30 L60 12 H286 V48 H60 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><path d="M25 30 L60 12 V48 Z" fill="#efdccb" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><path d="M25 30 L38 23 V37 Z" fill="#1f2430"/><rect x="286" y="12" width="20" height="36" fill="#f28bb3" stroke="#1f2430" stroke-width="4"/><line x1="25" y1="56" x2="25" y2="60" stroke="#e04848" stroke-width="3"/><line x1="306" y1="52" x2="306" y2="60" stroke="#e04848" stroke-width="3"/>'), ruler(460, 8, 'in', inches=True), T('6 inches long', 44, RED), gap=4)
# square: four equal sides (tick marks) and four right angles (corner boxes)
math-3-quadrilaterals/square = raw(340, 340, '<rect x="40" y="40" width="260" height="260" fill="#d6e6fb" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<path d="{d}" fill="none" stroke="#f08a24" stroke-width="5"/>' for d in ('M40 70 H70 V40', 'M270 40 V70 H300', 'M300 270 H270 V300', 'M70 300 V270 H40')) + ''.join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#e04848" stroke-width="6"/>' for x1, y1, x2, y2 in ((170, 26, 170, 54), (170, 286, 170, 314), (26, 170, 54, 170), (286, 170, 314, 170))))
# rhombus: a tilted rhombus with four equal sides marked
math-3-quadrilaterals/rhombus = col(raw(400, 260, '<path d="M30 230 L130 30 L370 30 L270 230 Z" fill="#fde3c8" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/>' + ''.join(f'<line x1="{x - 12 * dx:.1f}" y1="{y - 12 * dy:.1f}" x2="{x + 12 * dx:.1f}" y2="{y + 12 * dy:.1f}" stroke="#e04848" stroke-width="6"/>' for x, y, dx, dy in ((80, 130, 0.894, 0.447), (250, 30, 0, 1), (320, 130, 0.894, 0.447), (150, 230, 0, 1)))), T('4 sides, all the same length', 32, RED), gap=10)
# shorter: a pencil and a ruler from the same starting line, the pencil picked out
math-k-longer-heavier-bigger/shorter = raw(460, 300, '<line x1="30" y1="10" x2="30" y2="290" stroke="#8a8f9c" stroke-width="5" stroke-dasharray="10 7"/><rect x="30" y="40" width="410" height="70" rx="6" fill="#f5c33b" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<line x1="{30 + i * 34}" y1="40" x2="{30 + i * 34}" y2="{64 if i % 2 else 72}" stroke="#1f2430" stroke-width="3"/>' for i in range(1, 12)) + '<rect x="24" y="168" width="230" height="84" rx="16" fill="#fde97a" stroke="#f08a24" stroke-width="5"/><path d="M36 210 L66 192 H210 V228 H66 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><path d="M36 210 L66 192 V228 Z" fill="#efdccb" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><rect x="210" y="192" width="22" height="36" fill="#f28bb3" stroke="#1f2430" stroke-width="4"/><text x="350" y="222" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="#f08a24">shorter</text>')
# heavier: a balance that tips down on the watermelon side, a grape up high
math-k-longer-heavier-bigger/heavier = col(scale_icon(400, left=raw(120, 80, '<ellipse cx="60" cy="40" rx="56" ry="36" fill="#2f9e5b" stroke="#1f2430" stroke-width="5"/><path d="M20 26 Q60 10 100 26 M14 44 Q60 30 106 44 M22 60 Q60 50 98 60" fill="none" stroke="#1d6b3c" stroke-width="5"/>'), right=grape(40), tilt=16), row(T('heavier', 40, ORANGE), Item(150, 10, ''), T('lighter', 32, GRAY), gap=0), gap=0)
# lighter: a balance with a rock down low and a feather up high, the feather side picked out
math-k-longer-heavier-bigger/lighter = col(scale_icon(400, left=raw(110, 76, '<path d="M8 70 L18 30 L48 8 L86 14 L104 46 L96 70 Z" fill="#8a8f9c" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/>'), right=raw(120, 50, '<path d="M8 42 C40 4 92 2 116 8 C96 26 56 46 8 42 Z" fill="#fff" stroke="#1f2430" stroke-width="4"/><path d="M4 46 L104 12" stroke="#1f2430" stroke-width="3"/>'), tilt=16), row(T('heavier', 32, GRAY), Item(150, 10, ''), T('lighter', 40, ORANGE), gap=0), gap=0)
# longest: three ribbons from the same start line, the red one longest
math-1-measuring-length/longest = raw(460, 300, '<line x1="30" y1="10" x2="30" y2="290" stroke="#8a8f9c" stroke-width="5" stroke-dasharray="10 7"/><rect x="30" y="34" width="250" height="56" rx="8" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><rect x="30" y="122" width="400" height="56" rx="8" fill="#e04848" stroke="#1f2430" stroke-width="4"/><rect x="30" y="210" width="160" height="56" rx="8" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><text x="230" y="162" font-family="Segoe UI" font-size="36" font-weight="700" text-anchor="middle" fill="#fff">longest</text>')
# inch: a ruler with its first inch bracketed and a paper clip about 1 inch long above it
math-2-rulers-and-units/inch = col(raw(460, 44, '<rect x="25" y="6" width="62" height="30" rx="15" fill="none" stroke="#6b707c" stroke-width="5"/><path d="M80 14 H40 A7 7 0 0 0 40 28 H74" fill="none" stroke="#6b707c" stroke-width="5"/>'), ruler(460, 6, 'in', inches=True, first='1 inch'), T('a paper clip is about 1 inch', 30, GRAY), gap=0)
# foot: a 12-inch ruler, 1 foot = 12 inches
math-2-rulers-and-units/foot = col(T('1 foot = 12 inches', 44, RED), raw(460, 30, '<path d="M25 26 V10 H400 V26" fill="none" stroke="#e04848" stroke-width="5"/>'), ruler(460, 12, 'in', inches=True), gap=0)
# penny: the penny, worth 1 cent, beside the other coins at their real sizes
math-2-time-and-money/penny = us_coins('penny')
# dime: the dime, worth 10 cents, smaller than the penny
math-2-time-and-money/dime = us_coins('dime')
# quarter: the quarter, worth 25 cents, beside the other coins
math-2-time-and-money/quarter = us_coins('quarter')
# dollar: a one-dollar bill is worth 100 cents (100 pennies)
math-2-time-and-money/dollar = col(raw(330, 150, '<rect x="4" y="4" width="322" height="142" rx="8" fill="#cfe3c4" stroke="#1f2430" stroke-width="5"/><rect x="16" y="16" width="298" height="118" rx="4" fill="none" stroke="#5d8a52" stroke-width="3"/><ellipse cx="165" cy="75" rx="44" ry="50" fill="#e8f1e2" stroke="#5d8a52" stroke-width="4"/><text x="165" y="94" font-family="Segoe UI" font-size="54" font-weight="700" text-anchor="middle" fill="#3d6b33">$1</text><text x="40" y="54" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#3d6b33">1</text><text x="290" y="54" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#3d6b33">1</text><text x="40" y="126" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#3d6b33">1</text><text x="290" y="126" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#3d6b33">1</text>'), T('= 100 cents', 50, RED), raw(300, 150, ''.join(f'<circle cx="{8 + (i % 20) * 14.5:.1f}" cy="{8 + (i // 20) * 30 + (i % 2) * 0:.1f}" r="6.5" fill="#c97a42" stroke="#1f2430" stroke-width="1.5"/>' for i in range(100))), T('100 pennies', 32, GRAY), gap=6)
# divide: 20 apples split into 4 equal groups of 5
math-4-multiplicative-comparison/divide = col(groups(4, 5, icon=apple, size=36, per_row=2, gap=16), M('20 ÷ 4 = 5', 64, color=ORANGE), T('4 equal groups of 5', 32, GRAY), gap=14)
# protractor: a half-circle protractor centered on the vertex, measuring a 60 degree angle
math-4-angles-and-line-plots/protractor = raw(460, 280, '<path d="M30 240 A200 200 0 0 1 430 240 Z" fill="#d6e6fb" fill-opacity="0.7" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<line x1="{230 + 200 * math.cos(math.radians(a)):.1f}" y1="{240 - 200 * math.sin(math.radians(a)):.1f}" x2="{230 + (176 if a % 30 == 0 else 186 if a % 10 == 0 else 192) * math.cos(math.radians(a)):.1f}" y2="{240 - (176 if a % 30 == 0 else 186 if a % 10 == 0 else 192) * math.sin(math.radians(a)):.1f}" stroke="#1f2430" stroke-width="{3 if a % 10 == 0 else 1.5}"/>' for a in range(0, 181, 5)) + f'<line x1="230" y1="240" x2="440" y2="240" stroke="#f08a24" stroke-width="8" stroke-linecap="round"/><line x1="230" y1="240" x2="{230 + 215 * math.cos(math.radians(60)):.1f}" y2="{240 - 215 * math.sin(math.radians(60)):.1f}" stroke="#f08a24" stroke-width="8" stroke-linecap="round"/>' + ''.join(f'<text x="{230 + 152 * math.cos(math.radians(a)):.1f}" y="{240 - 152 * math.sin(math.radians(a)) + 8 - (16 if a in (0, 180) else 0):.1f}" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="middle" fill="#1f2430" stroke="#fff" stroke-width="5" paint-order="stroke">{a}</text>' for a in range(0, 181, 30)) + f'<path d="M290 240 A60 60 0 0 0 {230 + 60 * math.cos(math.radians(60)):.1f} {240 - 60 * math.sin(math.radians(60)):.1f}" fill="none" stroke="#e04848" stroke-width="6"/><circle cx="230" cy="240" r="9" fill="#e04848" stroke="#1f2430" stroke-width="3"/><text x="300" y="214" font-family="Segoe UI" font-size="30" font-weight="700" fill="#e04848">60°</text><text x="230" y="276" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#e04848">vertex</text>')
# acute angle: an angle smaller than a right angle, shown beside a right angle
math-4-lines-angles-and-symmetry/acute-angle = row(col(angle(220, 40, ORANGE, label='40°'), T('acute', 40, ORANGE), T('less than 90°', 28, ORANGE), gap=2), col(angle(170, 90, GRAY, right=True), T('right angle', 30, GRAY), T('90°', 28, GRAY), gap=2), gap=20, align='b')
# obtuse angle: an angle bigger than a right angle, shown beside a right angle
math-4-lines-angles-and-symmetry/obtuse-angle = row(col(raw(260, 170, '<line x1="150" y1="150" x2="250" y2="150" stroke="#1f2430" stroke-width="6" stroke-linecap="round"/><path d="M258 150 l-16 -9 v18 z" fill="#1f2430"/><line x1="150" y1="150" x2="40" y2="30" stroke="#1f2430" stroke-width="6" stroke-linecap="round"/><path d="M34 23 l6 18 l12 -11 z" fill="#1f2430"/><path d="M200 150 A50 50 0 0 0 116 113" fill="none" stroke="#f08a24" stroke-width="6"/><text x="186" y="104" font-family="Segoe UI" font-size="28" font-weight="700" fill="#f08a24">132°</text>'), T('obtuse', 40, ORANGE), T('more than 90°', 28, ORANGE), gap=2), col(angle(150, 90, GRAY, right=True), T('right angle', 30, GRAY), T('90°', 28, GRAY), gap=2), gap=16, align='b')
# line of symmetry: a butterfly with a dashed fold line down the middle, two matching halves
math-4-lines-angles-and-symmetry/line-of-symmetry = (lambda wing: raw(400, 360, wing + f'<g transform="translate(400 0) scale(-1 1)">{wing}</g>' + '<ellipse cx="200" cy="190" rx="14" ry="110" fill="#1f2430"/><path d="M196 86 Q180 40 160 30 M204 86 Q220 40 240 30" fill="none" stroke="#1f2430" stroke-width="4"/><line x1="200" y1="6" x2="200" y2="354" stroke="#e04848" stroke-width="6" stroke-dasharray="16 10"/>'))('<path d="M196 150 C150 40 40 30 30 90 C22 140 80 180 196 190 Z" fill="#f08a24" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M196 200 C110 200 60 240 80 290 C100 330 170 300 196 230 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><circle cx="96" cy="100" r="22" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><circle cx="130" cy="262" r="16" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/>')
# metric system: a ladder of metric length units, km down to mm, each step 10 times smaller
math-5-units-and-line-plots/metric-system = raw(420, 470, ''.join(f'<rect x="20" y="{10 + i * 64}" width="100" height="48" rx="8" fill="{c}" stroke="#1f2430" stroke-width="3"/><text x="70" y="{44 + i * 64}" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#fff">{s}</text>' for i, (s, c) in enumerate(zip(('km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'), ('#8e5bc4', '#3a7bd5', '#1d9a9a', '#e04848', '#2f9e5b', '#f08a24', '#a0673a')))) + ''.join(f'<text x="140" y="{74 + i * 64}" font-family="Segoe UI" font-size="26" font-weight="700" fill="#1f2430">1 {a} = 10 {b}</text>' for i, (a, b) in enumerate(zip(('km', 'hm', 'dam', 'm', 'dm', 'cm'), ('hm', 'dam', 'm', 'dm', 'cm', 'mm')))) + '<path d="M380 30 V420" stroke="#e04848" stroke-width="6"/><path d="M380 436 l-12 -20 h24 z" fill="#e04848"/><text x="350" y="230" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#e04848" transform="rotate(90 350 230)">each step: 10 times smaller</text>')
# rectangular prism: a box shape, hidden edges dashed, six rectangle faces
math-5-volume/rectangular-prism = col(raw(400, 280, '<path d="M30 110 H270 V260 H30 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M30 110 L130 30 H370 L270 110 Z" fill="#d6e6fb" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M270 110 L370 30 V180 L270 260 Z" fill="#8fb4ea" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><path d="M30 260 L130 180 H370 M130 180 V30" fill="none" stroke="#1f2430" stroke-width="3" stroke-dasharray="10 8"/>'), T('6 rectangle faces', 36, BLUE), gap=8)
# quadrilateral: six shapes with four sides each, grouped under "4 sides"
math-5-classifying-2d-figures/quadrilateral = box(col(T('4 sides', 44, ORANGE), grid([shape('square', 100, BLUE), shape('rectangle', 120, GREEN), shape('rhombus', 100, PURPLE), shape('trapezoid', 120, ORANGE), shape('kite', 100, RED), shape('parallelogram', 120, TEAL)], 3, gap=22), gap=16), color=ORANGE, fill='#fff', p=24)
# rate: a double number line, 60 miles for every 1 hour
math-6-ratios-and-rates/rate = col(dnl((0, 60, 120, 180), (0, 1, 2, 3), names=('miles', 'hours'), hl=1), T('60 miles per hour', 40, ORANGE), gap=16)
# unit rate: a double number line, $2 for each 1 pound
math-6-ratios-and-rates/unit-rate = col(dnl(('$0', '$2', '$4', '$6'), (0, 1, 2, 3), names=('cost', 'pounds'), hl=1), T('$2 for 1 pound', 40, ORANGE), gap=16)
# markup: the store's cost plus a 30% markup makes the selling price
math-7-proportional-relationships/markup = raw(470, 300, '<rect x="20" y="40" width="300" height="70" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><rect x="320" y="40" width="90" height="70" fill="#f08a24" stroke="#1f2430" stroke-width="4"/><text x="170" y="86" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#fff">cost $20</text><text x="365" y="86" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#fff">$6</text><text x="365" y="28" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#f08a24">markup 30%</text><rect x="20" y="170" width="390" height="70" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><text x="215" y="216" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#fff">selling price $26</text><path d="M20 120 V134 H410 V120" fill="none" stroke="#1f2430" stroke-width="3"/><path d="M215 134 V160" stroke="#1f2430" stroke-width="4"/><path d="M215 166 l-9 -14 h18 z" fill="#1f2430"/><text x="235" y="286" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">$20 + 30% of $20 = $26</text>')
# tax: a price plus 8% sales tax makes the total
math-7-proportional-relationships/tax = raw(470, 300, '<rect x="20" y="40" width="360" height="70" fill="#3a7bd5" stroke="#1f2430" stroke-width="4"/><rect x="380" y="40" width="29" height="70" fill="#e04848" stroke="#1f2430" stroke-width="4"/><text x="200" y="86" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#fff">price $50</text><text x="420" y="28" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="end" fill="#e04848">tax 8% = $4</text><rect x="20" y="170" width="389" height="70" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><text x="215" y="216" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#fff">total $54</text><path d="M20 120 V134 H409 V120" fill="none" stroke="#1f2430" stroke-width="3"/><path d="M215 134 V160" stroke="#1f2430" stroke-width="4"/><path d="M215 166 l-9 -14 h18 z" fill="#1f2430"/><text x="235" y="286" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">$50 + 8% of $50 = $54</text>')
# inference: a random sample of students points to a conclusion about all students
math-7-sampling-and-inference/inference = (lambda R: col(row(col(T('all students', 26, GRAY), raw(250, 200, '<rect x="2" y="2" width="246" height="196" rx="14" fill="#fff" stroke="#8a8f9c" stroke-width="4"/>' + ''.join(f'<circle cx="{18 + (i % 12) * 19.5:.1f}" cy="{18 + (i // 12) * 20.5:.1f}" r="7" fill="{"#f08a24" if R.random() < 0.7 else "#3a7bd5"}"/>' for i in range(108)) + '<circle cx="128" cy="100" r="56" fill="none" stroke="#e04848" stroke-width="5"/>'), gap=4), arrow(40), col(T('sample', 26, RED), box(col(T('14 of 20', 32, ORANGE), T('like pizza', 28), gap=0), color=ORANGE, fill='#fff', p=12), gap=4), gap=8), arrow(40, dir='down'), box(T('Most students like pizza.', 32), color=GREEN, p=16), gap=6))(__import__('random').Random(7))
# biased sample: the sample only catches one group, the soccer team, so it does not match the whole school
math-7-sampling-and-inference/biased-sample = (lambda R: col(T('whole school', 28, GRAY), raw(420, 260, '<rect x="2" y="2" width="416" height="256" rx="14" fill="#fff" stroke="#8a8f9c" stroke-width="4"/>' + ''.join(f'<circle cx="{20 + (i % 20) * 20.5:.1f}" cy="{20 + (i // 20) * 22:.1f}" r="7" fill="{"#2f9e5b" if (i % 20 > 14 and i // 20 > 6) else R.choice(("#3a7bd5", "#f08a24", "#8e5bc4", "#8a8f9c"))}"/>' for i in range(220)) + '<rect x="318" y="164" width="96" height="88" rx="16" fill="none" stroke="#e04848" stroke-width="6"/>'), row(T('sample: only the soccer team', 30, RED), cross(40), gap=10), gap=6))(__import__('random').Random(3))
# probability: a 0 to 1 line from impossible to certain, a coin landing heads at 1/2
math-7-probability/probability = col(raw(480, 200, '<line x1="30" y1="80" x2="450" y2="80" stroke="#1f2430" stroke-width="6"/>' + ''.join(f'<line x1="{30 + i * 105}" y1="64" x2="{30 + i * 105}" y2="96" stroke="#1f2430" stroke-width="4"/><text x="{30 + i * 105}" y="50" font-family="Cambria Math" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">{v}</text><text x="{30 + i * 105}" y="{132 + (i % 2) * 32}" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="{c}">{s}</text>' for i, (v, s, c) in enumerate((('0', 'impossible', '#e04848'), ('1/4', 'unlikely', '#f08a24'), ('1/2', 'even chance', '#8e5bc4'), ('3/4', 'likely', '#1d9a9a'), ('1', 'certain', '#2f9e5b')))) + '<circle cx="240" cy="80" r="14" fill="#8e5bc4" stroke="#1f2430" stroke-width="3"/>'), row(coin(90, 'H'), T('heads: 1/2', 40, PURPLE), gap=14), gap=8)
# outcome: the six faces of a die, rolling a 4 is one of the six possible outcomes
math-7-probability/outcome = col(grid([mark(dice(k, 96), 'box', ORANGE) if k == 4 else pad(dice(k, 96), 14) for k in range(1, 7)], 3, gap=14), T('6 possible outcomes', 32, GRAY), T('rolling a 4 is one outcome', 32, ORANGE), gap=8)
# model: a rule and its graph stand for the ride cost, and predict the cost of 10 rides
math-8-modeling-with-functions/model = col(box(M('cost = 5 + 2 × rides', 44, color=BLUE), color=BLUE, fill='#fff', p=12), row(raw(40, 300, '<text x="26" y="150" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 150)">cost ($)</text>'), col(plot(lambda x: 5 + 2 * x, size=300, xr=(-0.6, 12), yr=(-1.5, 32), grid_=False, points=[(10, 25, ORANGE)], segs=[((10, 0), (10, 25), GRAY, True), ((0, 25), (10, 25), GRAY, True)], texts=[(8.4, 27.5, '$25', ORANGE)]), T('rides →', 26), gap=0), gap=0), T('10 rides: $25', 34, ORANGE), gap=6)
# initial value: a line graph with the starting amount (where x is 0) picked out
math-8-modeling-with-functions/initial-value = col(row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">total cost ($)</text>'), col(plot(lambda x: 10 + 4 * x, size=320, xr=(-0.4, 6), yr=(-2, 36), points=[(0, 10, RED)], texts=[(1.6, 9.2, '$10', RED)]), T('rides →', 26), gap=0), gap=0), T('initial value: $10 when x = 0', 32, RED), gap=6)
# Pythagorean theorem: a 3-4-5 right triangle with a square on each side, 9 + 16 = 25
math-8-the-pythagorean-theorem/pythagorean-theorem = (lambda u: col(raw(11 * u + 28, 10 * u + 28, f'<g transform="translate({4 * u + 14} {3 * u + 14})">' + ''.join(f'<rect x="{-4 * u + i * u}" y="{j * u}" width="{u}" height="{u}" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="2"/>' for i in range(4) for j in range(4)) + ''.join(f'<rect x="{i * u}" y="{4 * u + j * u}" width="{u}" height="{u}" fill="#fde3c8" stroke="#f08a24" stroke-width="2"/>' for i in range(3) for j in range(3)) + f'<g transform="rotate({math.degrees(math.atan2(4, 3)):.3f})">' + ''.join(f'<rect x="{i * u}" y="{-5 * u + j * u}" width="{u}" height="{u}" fill="#d3f0de" stroke="#2f9e5b" stroke-width="2"/>' for i in range(5) for j in range(5)) + f'</g><path d="M0 0 V{4 * u} H{3 * u} Z" fill="#fff" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="0" y="{4 * u - 18}" width="18" height="18" fill="none" stroke="#1f2430" stroke-width="3"/>' + ''.join(f'<text x="{x * u:.0f}" y="{y * u + 14:.0f}" font-family="Segoe UI" font-size="40" font-weight="700" text-anchor="middle" fill="{c}" stroke="#fff" stroke-width="6" paint-order="stroke">{t}</text>' for x, y, t, c in ((-2, 2, '16', '#3a7bd5'), (1.5, 5.5, '9', '#f08a24'), (3.5, 0.5, '25', '#2f9e5b'))) + '</g>'), M('9 + 16 = 25', 44), M('a² + b² = c²', 36, color=GRAY), gap=4))(32)
# bivariate data: a scatter plot of height and shoe size, one dot for each person
math-8-bivariate-data/bivariate-data = (lambda R: col(row(raw(40, 300, '<text x="26" y="150" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 150)">shoe size</text>'), col(plot(size=300, xr=(-0.3, 10), yr=(-0.3, 10), scatter=[(x, 0.8 * x + 1 + R.uniform(-1.3, 1.3)) for x in [R.uniform(0.6, 9.4) for _ in range(16)]]), T('height →', 26), gap=0), gap=0), T('1 dot = 1 person (2 numbers)', 30, BLUE), gap=8))(__import__('random').Random(5))
# precision: the same pencil on two rulers, one read to whole centimeters, one to tenths
math-9-units-and-quantities/precision = (lambda pen: col(T('whole cm: about 7 cm', 30, GRAY), pen, ruler(460, 9, 'cm', inches=False), Item(10, 14, ''), T('tenths: 7.3 cm', 32, ORANGE), pen, raw(460, 100, '<rect x="5" y="0" width="450" height="70" rx="6" fill="#f5c33b" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<line x1="{25 + i * 375 / 90:.1f}" y1="0" x2="{25 + i * 375 / 90:.1f}" y2="{32 if i % 10 == 0 else 20 if i % 5 == 0 else 12}" stroke="#1f2430" stroke-width="{3 if i % 10 == 0 else 1.5}"/>' for i in range(91)) + ''.join(f'<text x="{25 + i * 375 / 9:.1f}" y="58" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="middle" fill="#1f2430">{i}</text>' for i in range(10)) + '<text x="448" y="42" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="end" fill="#8a8f9c">cm</text>'), gap=0))(raw(460, 40, f'<path d="M25 20 L48 6 H{25 + 7.3 * 375 / 9 - 14:.1f} V34 H48 Z" fill="#3a7bd5" stroke="#1f2430" stroke-width="3" stroke-linejoin="round"/><path d="M25 20 L48 6 V34 Z" fill="#efdccb" stroke="#1f2430" stroke-width="3" stroke-linejoin="round"/><rect x="{25 + 7.3 * 375 / 9 - 14:.1f}" y="6" width="14" height="28" fill="#f28bb3" stroke="#1f2430" stroke-width="3"/>'))
# accuracy: darts near the center of the target (accurate) and darts bunched off to one side (not accurate)
math-9-units-and-quantities/accuracy = row(*[col(over(target(200, arrow_=False), raw(200, 200, ''.join(f'<circle cx="{100 + dx}" cy="{100 + dy}" r="8" fill="#1f2430" stroke="#fff" stroke-width="3"/>' for dx, dy in pts))), row(T(lab, 32, c), mk, gap=6), gap=10) for lab, c, mk, pts in (('accurate', GREEN, check(36), ((-6, 4), (5, -5), (2, 8), (-4, -6), (8, 2))), ('not accurate', RED, cross(30), ((52, -50), (60, -42), (46, -40), (58, -56), (64, -48))))], gap=30)
# rate: a double number line, 3 liters for every 1 minute
math-9-units-and-quantities/rate = col(dnl((0, 3, 6, 9), (0, 1, 2, 3), names=('liters', 'minutes'), hl=1), T('3 liters per minute', 40, ORANGE), gap=16)
# viable: tickets cost $5 each; whole numbers of tickets from 0 up make sense, negative ones do not
math-9-creating-equations/viable = col(M('C = 5t', 50, color=BLUE), row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">cost ($)</text>'), col(plot(lambda x: 5 * x, size=320, xr=(-4, 6.4), yr=(-22, 32), dashed=(0,), colors=(GRAY,), regions=[([(-4, -22), (0, -22), (0, 32), (-4, 32)], '#d9dbe2', 0.6)], points=[(t, 5 * t, GREEN) for t in range(0, 7)], open_points=[(t, 5 * t) for t in (-3, -2, -1)], texts=[(-2, 22, 'not', RED), (-2, 16, 'viable', RED)]), T('tickets (t) →', 26), gap=0), gap=0), T('viable: 0, 1, 2, 3 ... tickets', 30, GREEN), gap=4)
# model: the taxi fare rule C = 15 + 2m drawn as a line, a $15 base fee plus $2 a mile
math-9-creating-equations/model = col(box(M('C = 15 + 2m', 48, color=BLUE), color=BLUE, fill='#fff', p=12), row(raw(40, 300, '<text x="26" y="150" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 150)">fare C ($)</text>'), col(plot(lambda x: 15 + 2 * x, size=300, xr=(-0.6, 12), yr=(-2, 42), points=[(0, 15, RED)], tri=((4, 23), (5, 25)), texts=[(3.4, 9, '$15 base', RED), (7.6, 19, '+$2 a mile', ORANGE)]), T('miles (m) →', 26), gap=0), gap=0), gap=6)
# Cavalieri's principle: a straight and a slanted stack of the same coins, same height, same volume
math-10-volume-and-cross-sections/cavalieri-s-principle = col(row(*[raw(200, 300, ''.join(f'<rect x="{40 + off(i):.1f}" y="{270 - i * 24}" width="110" height="20" rx="9" fill="#c9ccd1" stroke="#1f2430" stroke-width="3"/>' for i in range(11)) + '<line x1="0" y1="292" x2="200" y2="292" stroke="#1f2430" stroke-width="4"/>') for off in (lambda i: 0, lambda i: i * 4.5)], raw(70, 300, '<path d="M10 30 H24 V290 H10" fill="none" stroke="#e04848" stroke-width="4"/><text x="58" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848" transform="rotate(-90 58 160)">same height</text>'), gap=10), T('same coins, same volume', 34, BLUE), gap=8)
# surface area: a box unfolded into its net, the six face areas added up
math-10-modeling-with-geometry/surface-area = col(raw(400, 300, ''.join(f'<rect x="{x * 30 + 20}" y="{y * 30 + 10}" width="{w * 30}" height="{h * 30}" fill="{c}" stroke="#1f2430" stroke-width="4"/><text x="{x * 30 + 20 + w * 15}" y="{y * 30 + 10 + h * 15 + 10}" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">{w * h}</text>' for x, y, w, h, c in ((2, 0, 3, 2, '#d6e6fb'), (0, 2, 2, 4, '#d3f0de'), (2, 2, 3, 4, '#fde3c8'), (5, 2, 2, 4, '#d3f0de'), (7, 2, 3, 4, '#fde3c8'), (2, 6, 3, 2, '#d6e6fb')))), M('6 + 6 + 12 + 12 + 8 + 8 = 52', 36), T('surface area = 52 square units', 30, ORANGE), gap=6)
# focus: a parabola, its focus and its directrix; a point on the curve is the same distance from both
math-12-conic-sections/focus = plot(lambda x: x * x / 4, size=360, xr=(-5, 5), yr=(-2.4, 6.6), hlines=(-1,), points=[(0, 1, RED), (3, 2.25, BLUE)], segs=[((3, 2.25), (0, 1), ORANGE, True), ((3, 2.25), (3, -1), ORANGE, True)], texts=[(-1.1, 1.9, 'focus', RED), (-3.1, -1.8, 'directrix', GRAY), (3.6, 1.5, 'P', BLUE)])
# instantaneous rate of change: a curve with a tangent line touching it at one point, its slope is the rate right there
math-12-limits-and-rates-of-change/instantaneous-rate-of-change = col(plot(lambda x: 0.25 * x * x + 0.5, lambda x: 1.0 * (x - 2) + 1.5, size=360, xr=(-1, 6), yr=(-1, 8), colors=(BLUE, ORANGE), points=[(2, 1.5, RED)], dashed=(1,), tri=((3, 2.5), (4, 3.5))), T('slope of the tangent = rate at that instant', 26, ORANGE), gap=6)
# quantitative variable: a table where height is numbers (quantitative) and eye color is categories
math-12-exploring-data/quantitative-variable = col(row(T('quantitative', 28, ORANGE), T('categorical', 28, GRAY), gap=50), table(cells=[['height (cm)', 'eye color'], ['152', 'brown'], ['160', 'blue'], ['148', 'green'], ['171', 'brown']], size=400, hl_col=0, fs=30), gap=6)
# binomial distribution: the chances of making 0 to 10 free throws out of 10 (70% shooter)
math-12-probability-and-random-variables/binomial-distribution = col(bars([math.comb(10, k) * 0.7 ** k * 0.3 ** (10 - k) for k in range(11)], labels=list(range(11)), size=420, w=420, color=BLUE, touch=False), T('shots made out of 10 (70% shooter)', 26), gap=4)
# geometric distribution: the chance that the first 6 comes on roll 1, 2, 3 ..., each bar smaller
math-12-probability-and-random-variables/geometric-distribution = col(bars([(5 / 6) ** (k - 1) / 6 for k in range(1, 11)], labels=list(range(1, 11)), size=420, w=420, color=PURPLE), T('roll number of the first 6', 28), gap=4)
# law of large numbers: the share of heads wobbles at first, then settles near 1/2 as flips pile up
math-12-probability-and-random-variables/law-of-large-numbers = (lambda R: (lambda fl: col(row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">share of heads</text>'), col(plot(size=320, xr=(-5, 400), yr=(-0.05, 1.05), hlines=(0.5,), curves=[(list(range(1, 401)), [sum(fl[:n]) / n for n in range(1, 401)])], colors=(BLUE,), sw=4, texts=[(330, 0.56, '1/2', RED)]), T('number of flips →', 26), gap=0), gap=0), T('more trials: closer to 1/2', 30, BLUE), gap=4))([R.random() < 0.5 for _ in range(400)]))(__import__('random').Random(11))
# Type I error: a table of truth against decision, rejecting a null hypothesis that is true
math-12-confidence-intervals-and-significance-tests/type-i-error = grid2x2(('H₀ true', 'H₀ false'), ('reject H₀', 'keep H₀'), ('Type I\nerror', 'correct', 'correct', 'Type II\nerror'), hl=0, title=('the truth', 'decision'))
# related rates: a 10 ft ladder slides; the top moves down while the bottom moves out, x² + y² = 10²
math-12-applications-of-derivatives/related-rates = raw(480, 400, '<rect x="80" y="10" width="26" height="340" fill="#c4c8d0" stroke="#1f2430" stroke-width="4"/><line x1="80" y1="350" x2="470" y2="350" stroke="#1f2430" stroke-width="6"/><line x1="106" y1="150" x2="350" y2="350" stroke="#a0673a" stroke-width="5" stroke-dasharray="10 8" opacity="0.5"/><line x1="106" y1="110" x2="306" y2="350" stroke="#a0673a" stroke-width="12" stroke-linecap="round"/><path d="M40 100 V176" stroke="#e04848" stroke-width="7"/><path d="M40 190 l-11 -18 h22 z" fill="#e04848"/><text x="40" y="224" font-family="Cambria Math" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">dy/dt</text><path d="M316 326 H390" stroke="#3a7bd5" stroke-width="7"/><path d="M402 326 l-18 -11 v22 z" fill="#3a7bd5"/><text x="360" y="308" font-family="Cambria Math" font-size="30" font-weight="700" text-anchor="middle" fill="#3a7bd5">dx/dt</text><path d="M120 110 V350" stroke="#1f2430" stroke-width="2" stroke-dasharray="6 5"/><text x="128" y="300" font-family="Cambria Math" font-size="30" font-weight="700" fill="#1f2430">y</text><text x="206" y="388" font-family="Cambria Math" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">x</text><text x="226" y="210" font-family="Cambria Math" font-size="30" font-weight="700" fill="#a0673a">10</text><text x="470" y="44" font-family="Cambria Math" font-size="34" font-weight="700" text-anchor="end" fill="#1f2430">x² + y² = 10²</text>')
# optimization: metal needed for a can of fixed volume, plotted against its radius; the lowest point is the best can
math-12-applications-of-derivatives/optimization = col(row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">metal used</text>'), col(plot(lambda r: 2 * math.pi * r * r + 2 * 355 / r, size=320, xr=(0, 8), yr=(0, 700), colors=(BLUE,), points=[((355 / (2 * math.pi)) ** (1 / 3), 2 * math.pi * (355 / (2 * math.pi)) ** (2 / 3) + 2 * 355 / (355 / (2 * math.pi)) ** (1 / 3), RED)], vlines=((355 / (2 * math.pi)) ** (1 / 3),)), T('radius of the can →', 26), gap=0), gap=0), T('minimum: the least metal', 32, RED), gap=4)
# accumulation function: the area under a rate curve from a fixed start a up to x, the total so far
math-12-the-integral/accumulation-function = col(plot(lambda x: 1.2 + 0.8 * math.sin(x * 0.9) + 0.15 * x, size=360, xr=(-0.3, 8), yr=(-0.5, 3.6), shade=(lambda x: 1.2 + 0.8 * math.sin(x * 0.9) + 0.15 * x, 1, 5.2, ORANGE), vlines=(1, 5.2), texts=[(1, -0.35, 'a', DARK), (5.2, -0.35, 'x', DARK), (3.1, 0.9, 'A(x)', ORANGE)]), M('A(x) = ∫ₐˣ f(t) dt', 40, color=ORANGE), gap=6)
# average value: a curve and a rectangle of the same area over the same interval; its height is the average value
math-12-applications-of-integrals/average-value = col(plot(lambda x: 0.3 * x * x + 1, size=360, xr=(-0.4, 3.6), yr=(-0.3, 4.6), shade=(lambda x: 0.3 * x * x + 1, 0, 3, BLUE), regions=[([(0, 0), (3, 0), (3, 1.9), (0, 1.9)], '#f08a24', 0.35)], segs=[((0, 1.9), (3, 1.9), RED, True)], vlines=(3,), texts=[(0.75, 3.0, 'average = 1.9', RED)]), T('same area under the curve and in the box', 26, GRAY), gap=6)
# metamorphosis: a frog life cycle, eggs, tadpole, froglet, adult frog
science-3-life-cycles/metamorphosis = cycle([col(raw(110, 80, ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="#e9f3e0" stroke="#1f2430" stroke-width="3"/><circle cx="{x}" cy="{y}" r="5" fill="#1f2430"/>' for x, y in ((24, 26), (52, 18), (80, 28), (36, 54), (66, 52), (92, 58)))), T('eggs', 30), gap=2), col(raw(120, 60, '<ellipse cx="34" cy="30" rx="26" ry="20" fill="#5b8c3a" stroke="#1f2430" stroke-width="4"/><path d="M58 30 C80 14 96 46 118 24" fill="none" stroke="#5b8c3a" stroke-width="10" stroke-linecap="round"/><circle cx="26" cy="24" r="4" fill="#1f2430"/>'), T('tadpole', 30), gap=2), col(raw(120, 80, '<path d="M60 42 C80 34 100 50 118 34" fill="none" stroke="#2f9e5b" stroke-width="8" stroke-linecap="round"/><ellipse cx="44" cy="44" rx="30" ry="22" fill="#2f9e5b" stroke="#1f2430" stroke-width="4"/><path d="M30 62 L18 76 M56 62 L68 76" stroke="#2f9e5b" stroke-width="7" stroke-linecap="round"/><circle cx="34" cy="36" r="4" fill="#1f2430"/>'), T('froglet', 30), gap=2), col(frog(110), T('frog', 30), gap=2)], r=150)
# scale model: Earth and the Moon drawn at true scale for both size and distance, about 30 Earths apart
science-6-gravity-and-the-solar-system/scale-model = raw(480, 300, ''.join(f'<circle cx="{30 + i * 14}" cy="150" r="7" fill="none" stroke="#c4c8d0" stroke-width="1.5"/>' for i in range(1, 31)) + '<circle cx="30" cy="150" r="7" fill="#3a7bd5" stroke="#1f2430" stroke-width="2"/><circle cx="453" cy="150" r="1.9" fill="#8a8f9c" stroke="#1f2430" stroke-width="1"/><path d="M30 190 V204 H453 V190" fill="none" stroke="#e04848" stroke-width="4"/><text x="240" y="240" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">about 30 Earths apart</text><text x="30" y="110" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="start" fill="#3a7bd5">Earth</text><text x="453" y="110" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="end" fill="#5a5f6c">Moon</text><line x1="30" y1="118" x2="30" y2="138" stroke="#3a7bd5" stroke-width="3"/><line x1="453" y1="118" x2="453" y2="142" stroke="#5a5f6c" stroke-width="3"/><text x="240" y="40" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">sizes and distance to scale</text>')
# air pressure: a tall column of air pressing down at sea level, a shorter one on a mountaintop
science-6-water-cycle-and-weather/air-pressure = raw(470, 440, '<rect x="0" y="0" width="470" height="440" fill="#eef6fc"/><path d="M0 400 H220 L340 170 L470 400 V440 H0 Z" fill="#a7c97f" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>' + ''.join(f'<path d="M{x} {y} v26" stroke="#3a7bd5" stroke-width="6"/><path d="M{x} {y + 34} l-9 -12 h18 z" fill="#3a7bd5"/>' for x in (70, 120) for y in range(30, 370, 42)) + ''.join(f'<path d="M{x} {y} v26" stroke="#3a7bd5" stroke-width="6"/><path d="M{x} {y + 34} l-9 -12 h18 z" fill="#3a7bd5"/>' for x in (318, 362) for y in range(30, 140, 42)) + '<rect x="40" y="20" width="110" height="380" fill="none" stroke="#3a7bd5" stroke-width="3" stroke-dasharray="8 6"/><rect x="288" y="20" width="104" height="150" fill="none" stroke="#3a7bd5" stroke-width="3" stroke-dasharray="8 6"/><text x="95" y="430" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">sea level: higher</text><text x="345" y="318" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">mountain:</text><text x="345" y="348" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">lower</text><text x="220" y="80" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#3a7bd5">air</text><text x="220" y="106" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#3a7bd5">pushing</text><text x="220" y="132" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#3a7bd5">down</text>')
# thermal energy: the same particles moving slowly (cold, less thermal energy) and fast (hot, more)
science-6-thermal-energy/thermal-energy = (lambda R: row(*[col(raw(210, 210, f'<rect x="3" y="3" width="204" height="204" rx="14" fill="{bg}" stroke="#1f2430" stroke-width="5"/>' + ''.join((lambda x, y, a: f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x + L * math.cos(a):.1f}" y2="{y + L * math.sin(a):.1f}" stroke="{c}" stroke-width="4"/><path d="M{x + (L + 8) * math.cos(a):.1f} {y + (L + 8) * math.sin(a):.1f} l{-12 * math.cos(a) - 6 * math.sin(a):.1f} {-12 * math.sin(a) + 6 * math.cos(a):.1f} l{12 * math.sin(a):.1f} {-12 * math.cos(a):.1f} z" fill="{c}"/><circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{c}" stroke="#1f2430" stroke-width="2.5"/>')(36 + (i % 4) * 46 + R.uniform(-6, 6), 36 + (i // 4) * 46 + R.uniform(-6, 6), R.uniform(0, 6.28)) for i in range(16))), T(t1, 32, c), T(t2, 24, c), gap=4) for bg, c, L, t1, t2 in (('#eaf2fb', BLUE, 14, 'cold: slow', 'less thermal energy'), ('#fdece0', RED, 34, 'hot: fast', 'more thermal energy'))], gap=24))(__import__('random').Random(2))
# reactant: baking soda and vinegar (reactants, picked out) go in; new substances come out
science-7-chemical-reactions/reactant = row(col(T('reactants', 32, ORANGE), box(col(T('baking soda', 30), T('+', 34), T('vinegar', 30), gap=6), w=200, color=ORANGE, sw=7, p=18), gap=6), arrow(60), col(T('products', 28, GRAY), box(col(T('carbon dioxide', 24, GRAY), T('water', 24, GRAY), T('sodium acetate', 24, GRAY), gap=6), w=200, color=GRAY, fill='#f3f4f7', p=18), gap=6), gap=6)
# photosynthesis: a leaf takes in light, water and carbon dioxide and gives out sugar and oxygen
science-7-photosynthesis-and-respiration/photosynthesis = raw(480, 420, '<path d="M240 340 C120 330 90 200 160 120 C210 70 300 60 350 60 C360 150 340 300 240 340 Z" fill="#2f9e5b" stroke="#1f2430" stroke-width="6" stroke-linejoin="round"/><path d="M240 340 C260 250 300 160 340 70 M240 340 L230 400" fill="none" stroke="#1d6b3c" stroke-width="6"/>' + g(sun(90), 10, 6) + '<path d="M90 70 L165 125" stroke="#f5c33b" stroke-width="8"/><path d="M176 133 l-22 -4 l10 -14 z" fill="#f5c33b"/><text x="60" y="122" font-family="Segoe UI" font-size="26" font-weight="700" fill="#d9a520">light</text><path d="M60 200 H150" stroke="#1d9a9a" stroke-width="8"/><path d="M162 200 l-18 -11 v22 z" fill="#1d9a9a"/><text x="10" y="186" font-family="Segoe UI" font-size="24" font-weight="700" fill="#1d9a9a">carbon</text><text x="10" y="236" font-family="Segoe UI" font-size="24" font-weight="700" fill="#1d9a9a">dioxide</text><path d="M180 410 L218 368" stroke="#3a7bd5" stroke-width="8"/><path d="M226 358 l-4 22 l-14 -10 z" fill="#3a7bd5"/><text x="100" y="400" font-family="Segoe UI" font-size="26" font-weight="700" fill="#3a7bd5">water</text><path d="M360 200 H430" stroke="#e04848" stroke-width="8"/><path d="M442 200 l-18 -11 v22 z" fill="#e04848"/><text x="476" y="180" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="end" fill="#e04848">oxygen</text><path d="M330 290 H420" stroke="#f08a24" stroke-width="8"/><path d="M432 290 l-18 -11 v22 z" fill="#f08a24"/><text x="476" y="330" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="end" fill="#f08a24">sugar</text>')
# joule: lifting a small apple (about 100 g) up 1 meter takes about 1 joule
science-8-kinetic-and-potential-energy/joule = raw(420, 420, '<line x1="20" y1="380" x2="400" y2="380" stroke="#1f2430" stroke-width="6"/><g opacity="0.35">' + g(apple(80), 120, 296) + '</g>' + g(apple(80), 120, 40) + '<path d="M160 290 V140" stroke="#f08a24" stroke-width="7" stroke-dasharray="14 9"/><path d="M160 128 l-12 20 h24 z" fill="#f08a24"/><path d="M260 80 H276 V336 H260" fill="none" stroke="#e04848" stroke-width="5"/><text x="292" y="218" font-family="Segoe UI" font-size="34" font-weight="700" fill="#e04848">1 m</text><text x="210" y="414" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">about 1 joule of energy</text>')
# wave: a wave with its crest, trough, wavelength and amplitude marked
science-8-waves/wave = raw(480, 330, '<line x1="10" y1="165" x2="470" y2="165" stroke="#8a8f9c" stroke-width="3" stroke-dasharray="10 7"/><path d="M' + ' L'.join(f'{10 + i * 2.3:.1f} {165 - 90 * math.sin(i * 2.3 / 200 * 2 * math.pi):.1f}' for i in range(201)) + '" fill="none" stroke="#3a7bd5" stroke-width="7"/><circle cx="60" cy="75" r="9" fill="#e04848"/><text x="60" y="58" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#e04848">crest</text><circle cx="160" cy="255" r="9" fill="#2f9e5b"/><text x="160" y="296" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#2f9e5b">trough</text><path d="M60 30 V20 H260 V30" fill="none" stroke="#8e5bc4" stroke-width="4"/><text x="160" y="16" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#8e5bc4">wavelength</text><path d="M290 165 V85 M260 75 H300" stroke="#f08a24" stroke-width="5"/><path d="M290 77 l-9 14 h18 z M290 163 l-9 -14 h18 z" fill="#f08a24"/><text x="304" y="120" font-family="Segoe UI" font-size="24" font-weight="700" fill="#f08a24">amplitude</text>')
# allele: a matching pair of chromosomes with the same gene spot in two forms, T (tall) and t (short)
science-8-reproduction-and-heredity/allele = raw(420, 400, ''.join(f'<rect x="{x}" y="20" width="56" height="300" rx="28" fill="#e8dcf5" stroke="#1f2430" stroke-width="5"/><rect x="{x}" y="70" width="56" height="16" fill="#c4b2de"/><rect x="{x}" y="230" width="56" height="20" fill="#c4b2de"/><rect x="{x}" y="140" width="56" height="44" fill="{c}" stroke="#1f2430" stroke-width="4"/><text x="{x + 28}" y="174" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#fff">{t}</text>' for x, c, t in ((110, "#2f9e5b", "T"), (254, "#f08a24", "t"))) + '<text x="98" y="160" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="end" fill="#2f9e5b">tall</text><text x="98" y="186" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="end" fill="#2f9e5b">allele</text><text x="322" y="160" font-family="Segoe UI" font-size="24" font-weight="700" fill="#f08a24">short</text><text x="322" y="186" font-family="Segoe UI" font-size="24" font-weight="700" fill="#f08a24">allele</text><path d="M166 162 H254" stroke="#1f2430" stroke-width="3" stroke-dasharray="6 5"/><text x="210" y="370" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">same gene, two forms</text>')
# climate change: global average temperature from 1880 to 2020, rising about 1 °C
science-8-natural-hazards-and-human-impact/climate-change = (lambda yrs, t: col(T('global average temperature', 28), row(raw(56, 300, ''.join(f'<text x="50" y="{10 + (1.5 - v) / 2.5 * 280 + 7:.0f}" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="end" fill="#1f2430">{s}</text>' for v, s in ((-0.5, '-0.5'), (0, '0'), (0.5, '+0.5'), (1, '+1 °C')))), plot(size=300, xr=(1870, 2030), yr=(-1, 1.5), hlines=(0,), curves=[(yrs, t)], colors=(RED,), axes=False, box_=True, sw=6), gap=0), raw(356, 30, ''.join(f'<text x="{56 + 10 + (y - 1870) / 160 * 280:.0f}" y="22" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="middle" fill="#1f2430">{y}</text>' for y in (1880, 1920, 1960, 2000))), T('compared with the 1951-1980 average', 22, GRAY), gap=4))([1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], [-0.17, -0.35, -0.08, -0.43, -0.27, -0.14, 0.12, -0.17, -0.03, 0.03, 0.26, 0.45, 0.40, 0.72, 1.01])
# constraints: our straw tower design, boxed in by its limits
science-8-engineering-design/constraints = raw(460, 420, '<rect x="130" y="110" width="200" height="200" rx="16" fill="#fff" stroke="#8a8f9c" stroke-width="5" stroke-dasharray="12 8"/><path d="M180 290 L230 140 L280 290 M195 245 H265 M210 200 H250 M180 290 H280" fill="none" stroke="#f5c33b" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><text x="230" y="134" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#8a8f9c">our design</text>' + ''.join(f'<rect x="{x - w / 2}" y="{y - 30}" width="{w}" height="60" rx="12" fill="#f9d4d4" stroke="#e04848" stroke-width="5"/><text x="{x}" y="{y + 10}" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#1f2430">{s}</text>' for x, y, w, s in ((230, 50, 260, 'only 20 straws'), (230, 370, 230, 'only tape'), (70, 210, 130, '1 hour'), (390, 210, 130, '$0 cost'))))
# trade-off: a seesaw, lighter up on one side and stronger down on the other; more of one means less of the other
science-8-engineering-design/trade-off = col(seesaw(440, left=box(T('lighter', 40), color=BLUE, p=14), right=box(T('stronger', 40), color=ORANGE, p=14), tilt=14), T('gain one, give up some of the other', 30, GRAY), gap=8)
# set point: body temperature wobbles above and below a dashed 37 °C target and is pulled back each time
science-9-homeostasis/set-point = col(plot(lambda x: 37 + 0.9 * math.sin(x * 1.3) * math.exp(-0.05 * x), size=380, xr=(0, 14), yr=(35.0, 39.0), axes=False, box_=True, hlines=(37,), colors=(RED,), texts=[(5.2, 38.55, 'too hot: sweat', RED), (7.4, 35.3, 'too cold: shiver', BLUE)]), T('set point: about 37 °C', 34, DARK), gap=6)
# speciation: one species split by a river; over time the two groups become two species
science-9-evolution/speciation = raw(440, 430, '<path d="M200 10 C240 90 190 170 230 250 C260 310 210 370 240 430 H280 C250 370 300 310 270 250 C230 170 280 90 240 10 Z" fill="#7ab8e8"/><path d="M240 410 V310 M240 310 C240 270 120 250 110 170 V120 M240 310 C240 270 360 250 370 170 V120" fill="none" stroke="#1f2430" stroke-width="8" stroke-linecap="round"/>' + g(bug(80, '#8e5bc4'), 200, 330) + g(bug(80, '#3a7bd5'), 70, 40) + g(bug(80, '#e04848'), 330, 40) + '<text x="290" y="400" font-family="Segoe UI" font-size="24" font-weight="700" fill="#1f2430">one species</text><text x="110" y="28" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#3a7bd5">species A</text><text x="370" y="28" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#e04848">species B</text><text x="250" y="210" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#1f5f8f" transform="rotate(-80 250 210)">river</text>')
# nuclear fusion: two light hydrogen nuclei join into one heavier helium nucleus, giving off energy
science-9-stars-and-the-big-bang/nuclear-fusion = (lambda nuc: col(row(col(nuc(((-17, 0, 1), (17, 0, 0))), T('hydrogen', 28), gap=4), T('+', 60), col(nuc(((0, -15, 1), (-17, 13, 0), (17, 13, 0))), T('hydrogen', 28), gap=4), gap=16), arrow(50, DARK, 'down', sw=7), row(over(star(210, '#fde97a'), nuc(((-17, -17, 1), (17, -17, 0), (-17, 17, 0), (17, 17, 1)))), col(T('helium', 36), T('+ energy', 44, ORANGE), T('+ a neutron', 26, GRAY), gap=4, align='l'), gap=10), row(dot(26, RED, fill=RED), T('proton', 26), dot(26, GRAY, fill=GRAY), T('neutron', 26), gap=8), gap=8))(lambda bs: raw(150, 150, ''.join(f'<circle cx="{75 + x * 1.35:.0f}" cy="{75 + y * 1.35:.0f}" r="27" fill="{"#e04848" if p else "#8a8f9c"}" stroke="#1f2430" stroke-width="3"/>' + (f'<text x="{75 + x * 1.35:.0f}" y="{86 + y * 1.35:.0f}" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#fff">+</text>' if p else '') for x, y, p in bs)))
# albedo: snow reflects most sunlight back up; a dark forest soaks most of it up
science-9-earth-s-systems-and-feedback/albedo = row(*[col(raw(210, 280, f'<rect x="0" y="210" width="210" height="70" fill="{gr}" stroke="#1f2430" stroke-width="4"/>' + ''.join(f'<path d="M{x} 20 L{x + 50} 200" stroke="#f5c33b" stroke-width="8"/><path d="M{x + 54} 212 l-16 -14 l14 -6 z" fill="#f5c33b"/>' for x in (20, 70, 120)) + ''.join(f'<path d="M{x + 60} 200 L{x + 110} 30" stroke="#f08a24" stroke-width="{w}" stroke-dasharray="12 7"/><path d="M{x + 114} 18 l-14 14 l13 5 z" fill="#f08a24"/>' for x, w in pts) + extra), T(t1, 36, DARK), T(t2, 28, ORANGE), T(t3, 24, ORANGE), gap=2) for gr, pts, extra, t1, t2, t3 in (('#fff', ((20, 7), (70, 7), (120, 5)), '', 'snow', 'high albedo', '80 to 90% reflected'), ('#2f6b3a', ((70, 3),), ''.join(f'<path d="M{x} 210 l16 -40 l16 40 z" fill="#1d4d29" stroke="#1f2430" stroke-width="2"/>' for x in range(4, 200, 30)), 'forest', 'low albedo', 'about 10% reflected'))], gap=26)
# synthesis reaction: A + B snap together into one new substance, AB (iron + oxygen makes rust)
science-10-chemical-reactions-and-equations/synthesis-reaction = col(row(dot(90, BLUE, fill=BLUE), T('+', 64), dot(90, ORANGE, fill=ORANGE), arrow(70), row(dot(90, BLUE, fill=BLUE), dot(90, ORANGE, fill=ORANGE), gap=-14), gap=14), row(T('A', 44, BLUE), T('+', 44), T('B', 44, ORANGE), T('→', 44), T('AB', 44, PURPLE), gap=60), T('iron + oxygen → rust', 34, BROWN), gap=14)
# catalyst: an energy hill; with a catalyst the hump is lower, so the reaction goes faster
science-10-reaction-rates-and-equilibrium/catalyst = col(plot(lambda x: 2.4 - 1.2 / (1 + math.exp(-(x - 5) * 2)) + 4.2 * math.exp(-((x - 5) / 1.1) ** 2), lambda x: 2.4 - 1.2 / (1 + math.exp(-(x - 5) * 2)) + 2.0 * math.exp(-((x - 5) / 1.1) ** 2), size=380, xr=(0, 10), yr=(0, 7.4), axes=False, box_=False, colors=(GRAY, ORANGE), dashed=(1,), texts=[(5, 7, 'without catalyst', GRAY), (8.5, 4.4, 'with catalyst', ORANGE), (1.6, 1.6, 'reactants', DARK), (8.6, 0.5, 'products', DARK)]), T('lower energy hill: faster reaction', 30, ORANGE), gap=4)
# pressure: the same push on a small area (sinks in, high pressure) and on a big area (stays on top, low pressure)
science-10-gases-and-kinetic-theory/pressure = col(M('P = F ÷ A', 50, color=BLUE), row(*[col(raw(200, 260, f'<rect x="0" y="170" width="200" height="90" fill="#eef4fb" stroke="#8a8f9c" stroke-width="3"/><rect x="50" y="{20 + dy}" width="100" height="70" rx="8" fill="#8a8f9c" stroke="#1f2430" stroke-width="4"/><text x="100" y="{64 + dy}" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#fff">500 N</text><rect x="{100 - w / 2}" y="{90 + dy}" width="{w}" height="{80}" fill="#a0673a" stroke="#1f2430" stroke-width="4"/>'), T(t1, 28, c), T(t2, 26, c), gap=2) for w, dy, t1, t2, c in ((16, 50, 'small area', 'high pressure', RED), (190, -6, 'large area', 'low pressure', GREEN))], gap=30), gap=6)
# Boyle's law: at the same temperature, squeezing a gas into a smaller volume raises its pressure
science-10-gases-and-kinetic-theory/boyle-s-law = col(row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">volume</text>'), col(plot(lambda p: 6 / p, size=320, xr=(-0.2, 6.5), yr=(-0.2, 6.5), colors=(BLUE,), points=[(1.2, 5, ORANGE), (4, 1.5, RED)]), T('pressure →', 26), gap=0), gap=0), M('P × V stays the same', 34, color=BLUE), gap=4)
# Charles's law: at the same pressure, gas volume grows in step with temperature (in kelvin); a small cold balloon and a big warm one
science-10-gases-and-kinetic-theory/charles-s-law = col(row(raw(40, 320, '<text x="26" y="160" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430" transform="rotate(-90 26 160)">volume</text>'), col(plot(lambda t: t / 80, size=320, xr=(-10, 420), yr=(-0.2, 5.6), colors=(GRAY,), points=[(250, 250 / 80, BLUE), (360, 360 / 80, RED)]), T('temperature (K) →', 26), gap=0), gap=0), row(col(balloon(50, BLUE), T('cold', 28, BLUE), gap=2), col(balloon(90, RED), T('warm', 28, RED), gap=2), gap=50, align='b'), gap=4)
# neutralization: an acid plus a base makes water plus a salt, and the pH moves to 7
science-10-acids-bases-and-solutions/neutralization = col(row(box(col(T('acid', 32, RED), M('HCl', 38), gap=2), color=RED, p=16), T('+', 54), box(col(T('base', 32, BLUE), M('NaOH', 38), gap=2), color=BLUE, p=16), gap=10), arrow(46, DARK, 'down', sw=7), row(box(col(T('water', 32, TEAL), M('H₂O', 38), gap=2), color=TEAL, p=16), T('+', 54), box(col(T('salt', 32, GRAY), M('NaCl', 38), gap=2), color=GRAY, p=16), gap=10), raw(460, 116, ''.join(f'<rect x="{10 + i * 31}" y="10" width="31" height="44" fill="{c}"/>' for i, c in enumerate(('#e04848', '#e8603c', '#f08a24', '#f5a623', '#f5c33b', '#c9d43a', '#7cc04a', '#2f9e5b', '#1d9a9a', '#2c8bc9', '#3a7bd5', '#4f63c4', '#6b51c0', '#8e5bc4'))) + '<rect x="10" y="10" width="434" height="44" fill="none" stroke="#1f2430" stroke-width="3"/><path d="M227 62 l-12 20 h24 z" fill="#1f2430"/><text x="227" y="110" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">pH 7</text><text x="10" y="86" font-family="Segoe UI" font-size="22" font-weight="700" fill="#e04848">acid</text><text x="444" y="86" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="end" fill="#8e5bc4">base</text>'), gap=10)
# newton: a small apple hanging from a spring scale that reads 1 newton
science-11-newton-s-laws/newton = raw(360, 440, '<line x1="180" y1="0" x2="180" y2="30" stroke="#1f2430" stroke-width="5"/><rect x="130" y="30" width="100" height="220" rx="14" fill="#d6e6fb" stroke="#1f2430" stroke-width="5"/>' + ''.join(f'<line x1="150" y1="{60 + i * 18}" x2="{180 if i % 5 else 196}" y2="{60 + i * 18}" stroke="#1f2430" stroke-width="3"/>' for i in range(11)) + '<text x="244" y="68" font-family="Segoe UI" font-size="24" font-weight="700" fill="#1f2430">0</text><text x="244" y="158" font-family="Segoe UI" font-size="26" font-weight="700" fill="#e04848">1 N</text><path d="M140 150 H210" stroke="#e04848" stroke-width="7"/><line x1="180" y1="250" x2="180" y2="300" stroke="#1f2430" stroke-width="5"/>' + g(apple(80), 140, 296) + '<text x="180" y="420" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">about 1 newton</text><text x="270" y="350" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#8a8f9c">100 g</text>')
# efficiency: energy in splits into useful light and wasted heat; an LED wastes much less than an old bulb
science-11-energy-and-work/efficiency = col(*[col(T(name, 28), raw(440, 110, f'<rect x="0" y="10" width="100" height="90" fill="#8a8f9c"/><text x="50" y="64" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#fff">100 J in</text><path d="M100 10 H150 C200 10 200 0 250 0 H320 V{90 * u / 100:.0f} H250 C200 {90 * u / 100:.0f} 200 {10 + 90 * u / 100:.0f} 150 {10 + 90 * u / 100:.0f} H100 Z" fill="#f5c33b"/><path d="M100 {10 + 90 * u / 100:.0f} H150 C200 {10 + 90 * u / 100:.0f} 200 {20 + 90 * u / 100:.0f} 250 {20 + 90 * u / 100:.0f} H320 V110 H250 C200 110 200 100 150 100 H100 Z" fill="#e04848" opacity="0.8"/><text x="328" y="{max(18, 90 * u / 200 + 8):.0f}" font-family="Segoe UI" font-size="22" font-weight="700" fill="#d9a520">{u} J light</text><text x="328" y="{70 + 90 * u / 200:.0f}" font-family="Segoe UI" font-size="22" font-weight="700" fill="#e04848">{100 - u} J heat</text>'), T(f'efficiency = {u}%', 30, ORANGE), gap=4) for name, u in (('LED bulb', 40), ('old bulb', 5))], gap=18)
# watt: 1 watt is 1 joule of energy every second
science-11-energy-and-work/watt = col(M('1 watt = 1 joule per second', 38, color=BLUE), row(*[col(raw(70, 70, f'<circle cx="35" cy="35" r="30" fill="#fff" stroke="#1f2430" stroke-width="5"/><line x1="35" y1="35" x2="{35 + 22 * math.sin(i * 2.1):.1f}" y2="{35 - 22 * math.cos(i * 2.1):.1f}" stroke="#e04848" stroke-width="4"/>'), T(f'second {i + 1}', 20, GRAY), box(T('1 J', 30, '#fff'), color=ORANGE, fill=ORANGE, p=10), gap=4) for i in range(3)], arrow(50), lightbulb_on(90), gap=14), T('a 500 W motor uses 500 J each second', 26, GRAY), gap=14)
# Doppler effect: sound rings bunch up in front of a moving siren (higher pitch) and spread out behind it (lower pitch)
science-11-waves-and-sound/doppler-effect = raw(480, 390, ''.join(f'<circle cx="{150 + k * 34}" cy="170" r="{150 - k * 30}" fill="none" stroke="#3a7bd5" stroke-width="4"/>' for k in range(5)) + '<rect x="268" y="150" width="56" height="40" rx="8" fill="#e04848" stroke="#1f2430" stroke-width="4"/><path d="M332 170 H400" stroke="#1f2430" stroke-width="6"/><path d="M414 170 l-18 -11 v22 z" fill="#1f2430"/>' + g(person(70, ORANGE), 420, 230) + g(person(70, PURPLE), -6, 230) + '<text x="476" y="370" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="end" fill="#f08a24">higher pitch</text><text x="4" y="370" font-family="Segoe UI" font-size="26" font-weight="700" fill="#8e5bc4">lower pitch</text>')
# interference: two waves in step add into a bigger wave; two waves out of step cancel out
science-11-waves-and-sound/interference = (lambda wv: col(*[row(col(wv(a, 0, BLUE, 200), wv(a, s, ORANGE, 200), gap=0), arrow(44, DARK), col(wv(r, 0, PURPLE, 200), T(lab, 26, PURPLE), gap=0), gap=10) for a, s, r, lab in ((1, 0, 2, 'add up: bigger'), (1, math.pi, 0, 'cancel: flat'))], gap=20))(lambda a, s, c, w: raw(w, 100, '<line x1="0" y1="50" x2="200" y2="50" stroke="#d9dbe2" stroke-width="2"/><path d="M' + ' L'.join(f'{i * 2} {50 - 22 * a * math.sin(i / 100 * 4 * math.pi + s):.1f}' for i in range(101)) + f'" fill="none" stroke="{c}" stroke-width="5"/>'))
# photoelectric effect: light shines on a metal plate and knocks electrons off it
science-11-light-and-the-electromagnetic-spectrum/photoelectric-effect = raw(460, 400, '<rect x="40" y="300" width="380" height="50" fill="#c4c8d0" stroke="#1f2430" stroke-width="5"/><text x="230" y="335" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">metal</text>' + ''.join('<path d="M' + ' L'.join(f'{x0 + t * 1.2 + 10 * math.sin(t / 6):.1f} {20 + t * 2.4:.1f}' for t in range(0, 106)) + f'" fill="none" stroke="#8e5bc4" stroke-width="5"/><path d="M{x0 + 128} {294} l-14 -18 l18 -4 z" fill="#8e5bc4"/>' for x0 in (30, 110, 190)) + ''.join(f'<path d="M{x} 296 L{x + dx} {296 - dy}" stroke="#3a7bd5" stroke-width="4" stroke-dasharray="8 6"/><circle cx="{x + dx}" cy="{296 - dy}" r="14" fill="#3a7bd5" stroke="#1f2430" stroke-width="3"/><text x="{x + dx}" y="{296 - dy + 7}" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#fff">−</text>' for x, dx, dy in ((170, 120, 140), (250, 140, 70), (330, 70, 180))) + '<text x="60" y="390" font-family="Segoe UI" font-size="24" font-weight="700" fill="#8e5bc4">light</text><text x="440" y="390" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="end" fill="#3a7bd5">electrons fly off</text>')
# bioaccumulation: a tuna keeps taking in a little mercury, which stays in its body, so older fish hold more
science-12-pollution-and-solutions/bioaccumulation = (lambda R: col(row(*[col(over(fish(s, '#6f8fb0'), raw(s, s * 0.7, ''.join(f'<circle cx="{s * 0.3 + R.uniform(0, s * 0.35):.1f}" cy="{s * 0.2 + R.uniform(0, s * 0.3):.1f}" r="3.5" fill="#e04848"/>' for _ in range(n)))), T(t, 26), gap=4) for s, n, t in ((90, 3, '1 year'), (130, 10, '5 years'), (170, 26, '10 years'))], gap=14, align='b'), arrow(400, GRAY, sw=6, text='time'), row(dot(18, RED, fill=RED), T('mercury stays and builds up', 26, RED), gap=8), gap=10))(__import__('random').Random(4))
# stakeholder: a water plan in the middle with arrows to the groups it affects
science-12-engineering-for-global-challenges/stakeholder = raw(470, 420, ''.join(f'<line x1="235" y1="210" x2="{x}" y2="{y}" stroke="#8a8f9c" stroke-width="5"/>' for x, y in ((90, 80), (380, 80), (90, 340), (380, 340))) + '<rect x="160" y="170" width="150" height="80" rx="14" fill="#d6e6fb" stroke="#3a7bd5" stroke-width="6"/><text x="235" y="203" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">water</text><text x="235" y="233" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">plan</text>' + ''.join(f'<circle cx="{x}" cy="{y}" r="58" fill="#fff" stroke="#f08a24" stroke-width="5"/>' + g(ic, x - 36, y - 46) + f'<text x="{x}" y="{y + (82 if y > 200 else -66)}" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for x, y, ic, t in ((90, 90, raw(72, 72, '<path d="M8 66 V30 L36 8 L64 30 V66 Z" fill="#e04848" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/><rect x="26" y="40" width="20" height="26" fill="#fff" stroke="#1f2430" stroke-width="3"/>'), 'farmers'), (380, 90, raw(72, 72, '<path d="M4 68 V34 L24 46 V34 L44 46 V14 H60 V68 Z" fill="#8a8f9c" stroke="#1f2430" stroke-width="4" stroke-linejoin="round"/>'), 'factory'), (90, 330, house(72, BLUE), 'families'), (380, 330, fish(72, TEAL), 'wildlife'))))
# interdependence: the farmer sells wheat to the baker, the baker sells bread to the farmer; each needs the other
social-studies-3-business-and-specialization/interdependence = raw(470, 330, '<path d="M8 150 V80 L70 30 L132 80 V150 Z" fill="#e04848" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="50" y="92" width="40" height="58" fill="#fff" stroke="#1f2430" stroke-width="4"/><path d="M338 150 V70 H462 V150 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="5"/><path d="M330 74 Q400 20 470 74 Z" fill="#a0673a" stroke="#1f2430" stroke-width="5" stroke-linejoin="round"/><rect x="384" y="100" width="34" height="50" fill="#fff" stroke="#1f2430" stroke-width="4"/><text x="70" y="190" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">farmer</text><text x="400" y="190" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">baker</text><path d="M150 70 Q235 20 318 70" fill="none" stroke="#f08a24" stroke-width="8"/><path d="M328 78 l-22 -2 l10 -16 z" fill="#f08a24"/><text x="235" y="30" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#a0673a">wheat</text><path d="M318 140 Q235 200 150 140" fill="none" stroke="#3a7bd5" stroke-width="8"/><path d="M140 132 l22 0 l-8 18 z" fill="#3a7bd5"/><text x="235" y="214" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#3a7bd5">bread</text><text x="235" y="300" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">each needs the other</text>')
# statehood: a US map with Colorado shaded, the 38th state, admitted in 1876
social-studies-4-state-history/statehood = col(us_map(440, shade=('CO',), color=ORANGE), T('Colorado became the 38th state in 1876', 28, ORANGE), gap=8)
# colony: Virginia, a colony across the ocean, ruled by faraway England
social-studies-5-exploration-and-colonization/colony = col(T('Virginia: an English colony', 32, RED), world_map(440, view=(-95, 22, 15, 62), pins=[(-77, 37.5)], arrows_=[(-2, 52, -74, 38)], shade=[(-6, 50, 2, 56, ORANGE)], labels=[(-84, 32, 'Virginia', RED, 24), (-4, 60, 'England', ORANGE, 26)]), T('ruled by England, far across the ocean', 26, GRAY), gap=6)
# dynasty: a line of rulers from the same family, the crown passing from parent to child
social-studies-6-ancient-india-and-china/dynasty = col(T('one family, ruler after ruler', 30), raw(460, 200, ''.join(g(person(90, c), 20 + i * 115, 70) + f'<path d="M{28 + i * 115} 64 L{34 + i * 115} 36 L{50 + i * 115} 52 L{65 + i * 115} 30 L{80 + i * 115} 52 L{96 + i * 115} 36 L{102 + i * 115} 64 Z" fill="#f5c33b" stroke="#1f2430" stroke-width="3" stroke-linejoin="round"/>' + (f'<path d="M{100 + i * 115} 130 H{122 + i * 115}" stroke="#1f2430" stroke-width="5"/><path d="M{132 + i * 115} 130 l-14 -9 v18 z" fill="#1f2430"/>' if i < 3 else '') for i, c in enumerate((PURPLE, PURPLE, PURPLE, PURPLE)))), raw(460, 40, '<rect x="10" y="4" width="440" height="32" rx="16" fill="#e8dcf5" stroke="#8e5bc4" stroke-width="3"/><text x="230" y="29" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#8e5bc4">parent → child → grandchild → ...</text>'), gap=4)
# feudalism: a pyramid of king, lords, knights and peasants; land goes down, loyalty and service go up
social-studies-7-medieval-europe/feudalism = row(raw(60, 300, '<path d="M30 20 V260" stroke="#2f9e5b" stroke-width="8"/><path d="M30 274 l-12 -20 h24 z" fill="#2f9e5b"/><text x="18" y="140" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#2f9e5b" transform="rotate(-90 18 140)">land</text>'), pyramid_levels(4, 320, labels=['peasants', 'knights', 'lords', 'king'], colors=(BROWN, BLUE, PURPLE, YELLOW), blocks=True), raw(60, 300, '<path d="M30 280 V40" stroke="#e04848" stroke-width="8"/><path d="M30 26 l-12 20 h24 z" fill="#e04848"/><text x="46" y="150" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#e04848" transform="rotate(90 46 150)">loyalty, service</text>'), gap=4)
# taxation without representation: Parliament taxes the colonies, but the colonies have no vote in Parliament
social-studies-8-road-to-revolution/taxation-without-representation = raw(470, 330, '<rect x="0" y="0" width="470" height="330" fill="#fff"/><rect x="150" y="10" width="170" height="310" fill="#d6e8f5"/><text x="235" y="314" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="middle" fill="#3a7bd5">Atlantic Ocean</text><rect x="4" y="100" width="140" height="120" rx="14" fill="#fde3c8" stroke="#f08a24" stroke-width="5"/><text x="74" y="152" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">13</text><text x="74" y="184" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#1f2430">colonies</text><rect x="326" y="100" width="140" height="120" rx="14" fill="#f9d4d4" stroke="#e04848" stroke-width="5"/><text x="396" y="152" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#1f2430">Parliament</text><text x="396" y="184" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#1f2430">in London</text><path d="M320 120 Q235 60 156 120" fill="none" stroke="#e04848" stroke-width="8"/><path d="M146 126 l20 -2 l-8 -18 z" fill="#e04848"/><text x="235" y="60" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#e04848">taxes</text><path d="M150 200 Q235 260 316 200" fill="none" stroke="#3a7bd5" stroke-width="8" stroke-dasharray="14 9"/><path d="M326 194 l-20 2 l8 18 z" fill="#3a7bd5"/>' + g(cross(50), 210, 205) + '<text x="235" y="284" font-family="Segoe UI" font-size="28" font-weight="700" text-anchor="middle" fill="#3a7bd5">no vote</text>')
# precedent: Washington served two terms, and the next presidents followed his example
social-studies-8-the-early-republic/precedent = raw(470, 330, ''.join((f'<rect x="{i * 118 - 2}" y="6" width="116" height="250" rx="16" fill="#fde97a" stroke="#f08a24" stroke-width="5"/>' if i == 0 else '') + g(person(84, BLUE if i else ORANGE), 16 + i * 118, 30) + f'<text x="{58 + i * 118}" y="170" font-family="Segoe UI" font-size="{20 if len(n) > 8 else 22}" font-weight="700" text-anchor="middle" fill="#1f2430">{n}</text><rect x="{20 + i * 118}" y="190" width="34" height="34" rx="6" fill="#3a7bd5" stroke="#1f2430" stroke-width="3"/><rect x="{62 + i * 118}" y="190" width="34" height="34" rx="6" fill="#3a7bd5" stroke="#1f2430" stroke-width="3"/><text x="{58 + i * 118}" y="248" font-family="Segoe UI" font-size="20" font-weight="700" text-anchor="middle" fill="#1f2430">2 terms</text>' for i, n in enumerate(('Washington', 'Jefferson', 'Madison', 'Monroe'))) + '<text x="58" y="290" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#f08a24">sets the</text><text x="58" y="316" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#f08a24">example</text><path d="M130 300 H440" stroke="#1f2430" stroke-width="5"/><path d="M452 300 l-16 -9 v18 z" fill="#1f2430"/><text x="290" y="288" font-family="Segoe UI" font-size="22" font-weight="700" text-anchor="middle" fill="#1f2430">later presidents follow it</text>')
# natural rights: life, liberty and property, rights a person has from birth
social-studies-9-revolutions-and-enlightenment/natural-rights = raw(440, 420, ''.join(f'<circle cx="{x}" cy="{y}" r="86" fill="{c}" fill-opacity="0.35" stroke="{c}" stroke-width="6"/><text x="{x + dx}" y="{y + dy}" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">{t}</text>' for x, y, c, t, dx, dy in ((220, 130, '#3a7bd5', 'life', 0, -40), (140, 270, '#f08a24', 'liberty', -30, 40), (300, 270, '#2f9e5b', 'property', 30, 40))) + g(person(100, PURPLE), 186, 166) + '<text x="220" y="410" font-family="Segoe UI" font-size="24" font-weight="700" text-anchor="middle" fill="#8e5bc4">everyone, from birth</text>')
# social contract: the people give up some freedom to a government, which gives them protection in return
social-studies-9-revolutions-and-enlightenment/social-contract = raw(470, 330, g(person(70, BLUE), 20, 100) + g(person(70, ORANGE), 70, 120) + g(person(70, GREEN), 40, 160) + '<text x="80" y="290" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">the people</text>' + g(pillars(3, 150), 300, 100) + '<text x="375" y="290" font-family="Segoe UI" font-size="30" font-weight="700" text-anchor="middle" fill="#1f2430">government</text><path d="M160 110 Q235 50 300 110" fill="none" stroke="#f08a24" stroke-width="8"/><path d="M310 118 l-22 -2 l10 -16 z" fill="#f08a24"/><text x="235" y="44" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#f08a24">some freedom</text><path d="M300 230 Q235 290 160 230" fill="none" stroke="#3a7bd5" stroke-width="8"/><path d="M150 222 l22 0 l-8 18 z" fill="#3a7bd5"/><text x="235" y="325" font-family="Segoe UI" font-size="26" font-weight="700" text-anchor="middle" fill="#3a7bd5">protection</text>')
# elasticity: the same price rise on a steep demand curve (small drop in quantity) and a flat one (big drop)
social-studies-12-supply-and-demand/elasticity = row(*[col(T(t, 28, c), plot(f, size=210, xr=(0, 10), yr=(0, 10), colors=(c,), segs=[((0, 6), (f_inv(6), 6), GRAY, True), ((0, 4), (f_inv(4), 4), GRAY, True), ((f_inv(6), 0), (f_inv(6), 6), GRAY, True), ((f_inv(4), 0), (f_inv(4), 4), GRAY, True), ((f_inv(4), 0.6), (f_inv(6), 0.6), RED)], points=[(f_inv(6), 6, RED), (f_inv(4), 4, RED)]), T(t2, 22, GRAY), gap=4) for t, c, f, f_inv, t2 in (('inelastic', BLUE, lambda q: 25 - 4 * q, lambda p: (25 - p) / 4, 'like gasoline'), ('elastic', ORANGE, lambda q: 7.5 - 0.6 * q, lambda p: (7.5 - p) / 0.6, 'quantity drops a lot'))], gap=20)
# Indigenous languages: a map of Mexico, Central and South America with places where some Indigenous languages are spoken today
world-languages-6-12-cultures-of-the-spanish-speaking-world/indigenous-languages = world_map(440, view=(-118, -56, -34, 33), pins=[(-99, 19.4), (-89.5, 17), (-73, -13.5), (-68.5, -16.5), (-57, -24.5), (-72.6, -38.7)], labels=[(-104, 26, 'Nahuatl', RED, 24), (-77, 13, 'Maya', RED, 24), (-88, -12, 'Quechua', RED, 24), (-56, -15, 'Aymara', RED, 24), (-46, -27, 'Guaraní', RED, 24), (-86, -40, 'Mapudungun', RED, 22)])
# father: a family tree with the father picked out
world-languages-k-12-family-and-home/father = family_tree('father')
# grandmother: a family tree with the grandmother (a parent's mother) picked out
world-languages-k-12-family-and-home/grandmother = family_tree('grandmother')
# fusion: two light hydrogen nuclei join into one heavier helium nucleus, giving off energy
science-10-nuclear-chemistry/fusion = (lambda nuc: col(row(col(nuc(((-17, 0, 1), (17, 0, 0))), T('hydrogen', 28), gap=4), T('+', 60), col(nuc(((0, -15, 1), (-17, 13, 0), (17, 13, 0))), T('hydrogen', 28), gap=4), gap=16), arrow(50, DARK, 'down', sw=7), row(over(star(210, '#fde97a'), nuc(((-17, -17, 1), (17, -17, 0), (-17, 17, 0), (17, 17, 1)))), col(T('helium', 36), T('+ energy', 44, ORANGE), T('+ a neutron', 26, GRAY), gap=4, align='l'), gap=10), row(dot(26, RED, fill=RED), T('proton', 26), dot(26, GRAY, fill=GRAY), T('neutron', 26), gap=8), gap=8))(lambda bs: raw(150, 150, ''.join(f'<circle cx="{75 + x * 1.35:.0f}" cy="{75 + y * 1.35:.0f}" r="27" fill="{"#e04848" if p else "#8a8f9c"}" stroke="#1f2430" stroke-width="3"/>' + (f'<text x="{75 + x * 1.35:.0f}" y="{86 + y * 1.35:.0f}" font-family="Segoe UI" font-size="32" font-weight="700" text-anchor="middle" fill="#fff">+</text>' if p else '') for x, y, p in bs)))
