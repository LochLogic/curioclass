// Science Calculations generator, grades 6-12.
// One topic (or a mix) of physical science formulas. F = m × a starts at grade 8 (MS-PS2-2 is qualitative, so
// quantitative use waits for grade 8); Ohm's law, momentum and kinetic energy start at grade 9 (high school physics). Each problem gives two values and asks for the third. Grades 6-8
// get values that come out even (at most two decimal places); grades 9-12 get lab-style values and round to three
// significant figures. The key shows the formula, the substitution and the answer with units in each problem box.
// Wave speed (v = f × λ) starts at grade 8; conservation of momentum (carts that stick, or two things pushing apart)
// and series and parallel circuits (total resistance, then current) are high school. A second topic can be chosen;
// the sheet then alternates between the two.
(() => {
const { part, example, lines, keyline, esc } = Gen.h;
const { fmt } = Gen.m;

const GRADES = [['6', 'Grade 6'], ['7', 'Grade 7'], ['8', 'Grade 8'], ['9', 'Grade 9'], ['10', 'Grade 10'], ['11', 'Grade 11'], ['12', 'Grade 12']];
const hs = g => +g >= 9;
const sf3 = x => Number(Number(x).toPrecision(3));
const r2 = x => Math.round((x + Number.EPSILON) * 100) / 100;
const show = x => fmt(x, 6);
// three significant figures keeping trailing zeros: 1.30, 0.430, 24,200
const show3 = x => Math.abs(x) >= 100 ? fmt(x, 0) : Number(x).toPrecision(3);
// "a" before a consonant sound, "an" before a vowel sound (an 8 kg cart, an 11 Ω resistor, an elevator)
const art = t => t.replace(/(?<![\w.,])([Aa]) (?=8|1[18](?![\d,])|1[18],\d{3}(?![\d,])|[aeiouAEIOU])/g, (m, a) => a + 'n ');
// a value with one decimal place, a half step, two decimals: all exact
const tenth = (r, lo, hi) => r.int(lo * 10, hi * 10) / 10;
const half = (r, lo, hi) => r.int(lo * 2, hi * 2) / 2;

// prod: [X, Y, Z] means X = Y x Z. forms: the solved form for each unknown, symbols in braces.
const TOPICS = {
  density: {
    label: 'Density', prod: ['m', 'D', 'V'],
    sym: { D: 'D', m: 'm', V: 'V' }, name: { D: 'density', m: 'mass', V: 'volume' }, unit: { D: 'g/cm³', m: 'g', V: 'cm³' },
    formula: 'D = m ÷ V', also: 'm = D × V and V = m ÷ D', units: 'D in g/cm³, m in g, V in cm³',
    forms: { D: '{m} ÷ {V}', m: '{D} × {V}', V: '{m} ÷ {D}' },
    ctx: [
      // densities of pure metals and ice at room temperature (ice near 0 °C), in g/cm³
      ...[['aluminum', 2.7], ['copper', 8.96], ['iron', 7.87], ['lead', 11.3], ['gold', 19.3], ['silver', 10.5], ['zinc', 7.14]].map(([mat, D]) => ({
        gen: (r, H) => ({ D, V: H ? tenth(r, 4, 60) : r.int(4, 40) }),
        q: { D: f => `A block of ${mat} has a mass of ${f('m')} and a volume of ${f('V')}. What is its density?`,
          m: f => `A block of ${mat} has a volume of ${f('V')}. The density of ${mat} is ${f('D')}. What is the block's mass?`,
          V: f => `A piece of ${mat} has a mass of ${f('m')}. The density of ${mat} is ${f('D')}. What is its volume?` } })),
      { gen: (r, H) => ({ D: 0.92, V: H ? tenth(r, 8, 40) : r.int(8, 30) }),
        q: { D: f => `An ice cube has a mass of ${f('m')} and a volume of ${f('V')}. What is the density of the ice?`,
          m: f => `An ice cube has a volume of ${f('V')}. Ice has a density of ${f('D')}. What is the ice cube's mass?`,
          V: f => `An ice cube has a mass of ${f('m')}. Ice has a density of ${f('D')}. What is its volume?` } },
      ...[['rock sample', 2.5, 3.0, 10, 60], ['wooden block', 0.4, 0.9, 20, 300], ['plastic cube', 0.9, 1.4, 8, 64], ['sample of a mystery liquid', 0.7, 1.3, 20, 250]].map(([what, lo, hi, vlo, vhi]) => ({
        gen: (r, H, E) => ({ D: E ? r.int(lo * 10, hi * 10) / 10 : r.int(lo * 100, hi * 100) / 100, V: H ? tenth(r, vlo, vhi) : E ? r.int(Math.ceil(vlo / 5), Math.min(60, vhi) / 5) * 5 : r.int(vlo, vhi) }),
        q: { D: f => `A ${what} has a mass of ${f('m')} and a volume of ${f('V')}. What is its density?`,
          m: f => `A ${what} has a volume of ${f('V')} and a density of ${f('D')}. What is its mass?`,
          V: f => `A ${what} has a mass of ${f('m')} and a density of ${f('D')}. What is its volume?` } })),
    ],
  },
  speed: {
    label: 'Speed', prod: ['d', 'v', 't'],
    sym: { v: 'v', d: 'd', t: 't' }, name: { v: 'speed', d: 'distance', t: 'time' }, unit: { v: 'm/s', d: 'm', t: 's' },
    formula: 'v = d ÷ t', also: 'd = v × t and t = d ÷ v', units: 'v in m/s, d in m, t in s',
    forms: { v: '{d} ÷ {t}', d: '{v} × {t}', t: '{d} ÷ {v}' },
    ctx: [['walker', 1, 2, 30, 600], ['runner', 3, 7, 20, 300], ['cyclist', 4, 10, 30, 600], ['car', 10, 30, 5, 120], ['train', 20, 50, 30, 600], ['skateboarder', 2, 6, 10, 120]].map(([who, lo, hi, tlo, thi]) => ({
      gen: (r, H) => ({ v: H ? tenth(r, lo, hi) : (hi <= 10 ? half(r, lo, hi) : r.int(lo, hi)), t: H ? tenth(r, tlo, thi) : r.int(tlo / 5, thi / 5) * 5 }),
      q: { v: f => `A ${who} travels ${f('d')} in ${f('t')}. What is the ${who}'s average speed?`,
        d: f => `A ${who} moves at an average speed of ${f('v')} for ${f('t')}. How far does the ${who} travel?`,
        t: f => `A ${who} moves at an average speed of ${f('v')}. How long does it take the ${who} to travel ${f('d')}?` } })),
  },
  accel: {
    label: 'Acceleration', special: 'accel',
    sym: { a: 'a', vf: 'v<sub>f</sub>', vi: 'v<sub>i</sub>', t: 't' }, name: { a: 'acceleration', vf: 'final speed', vi: 'starting speed', t: 'time' },
    unit: { a: 'm/s²', vf: 'm/s', vi: 'm/s', t: 's' },
    formula: 'a = (v<sub>f</sub> − v<sub>i</sub>) ÷ t', also: 'v<sub>f</sub> = v<sub>i</sub> + a × t and t = (v<sub>f</sub> − v<sub>i</sub>) ÷ a',
    units: 'a in m/s², v<sub>f</sub> (final speed) and v<sub>i</sub> (starting speed) in m/s, t in s',
    forms: { a: '({vf} − {vi}) ÷ {t}', t: '({vf} − {vi}) ÷ {a}', vf: '{vi} + {a} × {t}' },
    // last value: a realistic top final speed in m/s (car 35 is about 78 mph, a sprinter tops out near 12, a cyclist near 12)
    ctx: [['car', 1, 5, 2, 8, 15, 35], ['cyclist', 0.5, 2, 2, 8, 4, 12], ['sprinter', 2, 5, 1, 3, 0, 11], ['train', 0.2, 1, 20, 50, 10, 40], ['skateboarder', 0.5, 2, 2, 5, 2, 8]].map(([who, alo, ahi, tlo, thi, vimax, vmax]) => ({
      vmax,
      gen: (r, H) => ({ a: H ? r.int(alo * 100, ahi * 100) / 100 : (ahi <= 2 ? half(r, Math.max(.5, alo), ahi) : r.int(alo, ahi)), t: H ? tenth(r, tlo, thi) : r.int(tlo, thi),
        vi: H && vimax && r.chance(.6) ? r.int(1, vimax) : 0 }),
      q: { a: f => `A ${who} speeds up from ${f('vi', 'rest')} to ${f('vf')} in ${f('t')}. What is the ${who}'s acceleration?`,
        t: f => `A ${who} speeds up from ${f('vi', 'rest')} to ${f('vf')} with an acceleration of ${f('a')}. How long does this take?`,
        vf: f => `A ${who} starts ${f('vi', 'from rest', 'at ')} and speeds up with an acceleration of ${f('a')} for ${f('t')}. What is the ${who}'s final speed?` } })),
  },
  force: {
    label: 'Force', prod: ['F', 'm', 'a'],
    sym: { F: 'F', m: 'm', a: 'a' }, name: { F: 'net force', m: 'mass', a: 'acceleration' }, unit: { F: 'N', m: 'kg', a: 'm/s²' },
    formula: 'F = m × a', also: 'm = F ÷ a and a = F ÷ m', units: 'F in newtons (N), m in kg, a in m/s²',
    forms: { F: '{m} × {a}', m: '{F} ÷ {a}', a: '{F} ÷ {m}' },
    ctx: [['shopping cart', 10, 40, 1, 0.5, 3], ['sled with its rider', 30, 90, 1, 0.5, 3], ['car', 900, 2000, 50, 1, 4], ['bowling ball', 4, 7, 1, 1, 5], ['wagon', 5, 30, 1, 0.5, 2]].map(([obj, lo, hi, step, alo, ahi]) => ({
      gen: (r, H) => ({ m: H && step === 1 ? tenth(r, lo, hi) : r.int(lo / step, hi / step) * step, a: H ? r.int(alo * 100, ahi * 100) / 100 : half(r, alo, ahi) }),
      q: { F: f => `A ${f('m')} ${obj} speeds up with an acceleration of ${f('a')}. What net force acts on it?`,
        m: f => `A net force of ${f('F')} gives a ${obj} an acceleration of ${f('a')}. What is the mass of the ${obj}?`,
        a: f => `A net force of ${f('F')} acts on a ${f('m')} ${obj}. What is its acceleration?` } })),
  },
  weight: {
    label: 'Weight', prod: ['W', 'm', 'g'],
    sym: { W: 'W', m: 'm', g: 'g' }, name: { W: 'weight', m: 'mass', g: 'acceleration due to gravity' }, unit: { W: 'N', m: 'kg', g: 'm/s²' },
    formula: 'W = m × g', also: 'm = W ÷ g', units: 'W in newtons (N), m in kg, g = 9.8 m/s² on Earth',
    forms: { W: '{m} × {g}', m: '{W} ÷ {g}', g: '{W} ÷ {m}' },
    ctx: [
      ...[['backpack', 2, 10], ['dog', 5, 40], ['bicycle', 8, 15], ['student', 30, 70], ['bag of rice', 1, 10], ['car', 900, 2000]].map(([obj, lo, hi]) => ({
        gen: (r, H) => ({ m: hi > 100 ? r.int(lo / 50, hi / 50) * 50 : H ? tenth(r, lo, hi) : half(r, lo, hi), g: 9.8 }),
        q: { W: f => `A ${obj} has a mass of ${f('m')}. What is the ${obj}'s weight on Earth?`,
          m: f => `A ${obj} weighs ${f('W')} on Earth. What is the ${obj}'s mass?` } })),
      // surface gravity: Moon 1.62 m/s², Mars 3.71 m/s² (NASA planetary fact sheets)
      ...[['the Moon', 1.62], ['Mars', 3.71]].map(([where, g]) => ({
        hsOnly: true, only: 'g',
        gen: r => ({ m: r.int(20, 140), g }),
        q: { g: f => `A space rover part with a mass of ${f('m')} weighs ${f('W')} on ${where}. What is the acceleration due to gravity on ${where}?` } })),
    ],
  },
  work: {
    label: 'Work', prod: ['W', 'F', 'd'],
    sym: { W: 'W', F: 'F', d: 'd' }, name: { W: 'work', F: 'force', d: 'distance' }, unit: { W: 'J', F: 'N', d: 'm' },
    formula: 'W = F × d', also: 'F = W ÷ d and d = W ÷ F', units: 'W in joules (J), F in newtons (N), d in m',
    forms: { W: '{F} × {d}', F: '{W} ÷ {d}', d: '{W} ÷ {F}' },
    ctx: [['push a box across the floor', 'pushing a box across the floor', 20, 200, 1, 20], ['pull a wagon along a path', 'pulling a wagon along a path', 10, 80, 5, 50],
      ['lift a box straight up onto a shelf', 'lifting a box straight up onto a shelf', 50, 300, 1, 2], ['push a stalled car along a flat road', 'pushing a stalled car along a flat road', 200, 600, 5, 30]].map(([verb, ing, flo, fhi, dlo, dhi]) => ({
      gen: (r, H) => ({ F: H ? r.int(flo, fhi) : r.int(flo / 5, fhi / 5) * 5, d: H ? tenth(r, dlo, dhi) : (dhi <= 2 ? half(r, dlo, dhi) : r.int(dlo, dhi)) }),
      q: { W: f => `You ${verb} with a force of ${f('F')} over a distance of ${f('d')}. How much work do you do?`,
        F: f => `You do ${f('W')} of work by ${ing} over a distance of ${f('d')}. How much force do you use?`,
        d: f => `You ${verb} with a force of ${f('F')} and do ${f('W')} of work. How far does it move?` } })),
  },
  power: {
    label: 'Power', prod: ['W', 'P', 't'],
    sym: { P: 'P', W: 'W', t: 't' }, name: { P: 'power', W: 'work', t: 'time' }, unit: { P: 'W', W: 'J', t: 's' },
    formula: 'P = W ÷ t', also: 'W = P × t and t = W ÷ P', units: 'P in watts (W), W (work) in joules (J), t in s',
    forms: { P: '{W} ÷ {t}', W: '{P} × {t}', t: '{W} ÷ {P}' },
    ctx: [['student running up the stairs', 200, 600, 3, 8], ['elevator motor lifting a car of people', 5000, 20000, 5, 20], ['crane lifting a steel beam', 10000, 50000, 10, 40], ['winch pulling a boat onto a trailer', 500, 2000, 10, 60]].map(([who, plo, phi, tlo, thi]) => ({
      gen: (r, H) => ({ P: H ? r.int(plo / 10, phi / 10) * 10 : r.int(plo / 50, phi / 50) * 50, t: H ? tenth(r, tlo, thi) : r.int(tlo, thi) }),
      q: { P: f => `A ${who} does ${f('W')} of work in ${f('t')}. What is the power?`,
        W: f => `A ${who} works with a power of ${f('P')} for ${f('t')}. How much work is done?`,
        t: f => `A ${who} does ${f('W')} of work with a power of ${f('P')}. How long does it take?` } })),
  },
  ohm: {
    label: "Ohm's law", prod: ['V', 'I', 'R'],
    sym: { V: 'V', I: 'I', R: 'R' }, name: { V: 'voltage', I: 'current', R: 'resistance' }, unit: { V: 'V', I: 'A', R: 'Ω' },
    formula: 'V = I × R', also: 'I = V ÷ R and R = V ÷ I', units: 'V in volts (V), I in amperes (A), R in ohms (Ω)',
    forms: { V: '{I} × {R}', I: '{V} ÷ {R}', R: '{V} ÷ {I}' },
    ctx: [{ gen: (r, H) => {
      if (H) { const R = r.pick([10, 22, 33, 47, 68, 100, 150, 220, 330, 470, 680, 1000]); const V = tenth(r, 1.5, 24); return { V, R, I: sf3(V / R) }; }
      for (let k = 0; k < 50; k++) { const V = r.pick([1.5, 3, 4.5, 6, 9, 12]), I = r.pick([0.1, 0.2, 0.25, 0.3, 0.5, 0.75, 1, 1.5, 2, 3]), R = V / I;
        if (Math.abs(R - Math.round(R)) < 1e-9 && R >= 2 && R <= 120) return { I, R: Math.round(R) }; }
      return { I: 0.5, R: 12 }; },
    q: { I: f => `A ${f('R')} resistor is connected to ${src(f('V'))}. What current flows through the resistor?`,
      V: f => `A current of ${f('I')} flows through a ${f('R')} resistor. What is the voltage across the resistor?`,
      R: f => `${src(f('V'), 1)} pushes a current of ${f('I')} through a resistor. What is the resistance?` } }],
  },
  momentum: {
    label: 'Momentum', prod: ['p', 'm', 'v'], hsOnly: true,
    sym: { p: 'p', m: 'm', v: 'v' }, name: { p: 'momentum', m: 'mass', v: 'speed' }, unit: { p: 'kg·m/s', m: 'kg', v: 'm/s' },
    formula: 'p = m × v', also: 'm = p ÷ v and v = p ÷ m', units: 'p in kg·m/s, m in kg, v in m/s',
    forms: { p: '{m} × {v}', m: '{p} ÷ {v}', v: '{p} ÷ {m}' },
    ctx: [],
  },
  ke: {
    label: 'Kinetic energy', special: 'ke', hsOnly: true,
    sym: { KE: 'KE', m: 'm', v: 'v' }, name: { KE: 'kinetic energy', m: 'mass', v: 'speed' }, unit: { KE: 'J', m: 'kg', v: 'm/s' },
    formula: 'KE = ½ × m × v²', also: 'm = 2 × KE ÷ v² and v = √(2 × KE ÷ m)', units: 'KE in joules (J), m in kg, v in m/s',
    forms: { KE: '0.5 × {m} × {v}²', m: '2 × {KE} ÷ {v}²', v: '√(2 × {KE} ÷ {m})' },
    ctx: [],
  },
  wave: {
    label: 'Wave speed', prod: ['v', 'f', 'lam'],
    sym: { v: 'v', f: 'f', lam: 'λ' }, name: { v: 'wave speed', f: 'frequency', lam: 'wavelength' }, unit: { v: 'm/s', f: 'Hz', lam: 'm' },
    formula: 'v = f × λ', also: 'f = v ÷ λ and λ = v ÷ f', units: 'v in m/s, f in hertz (Hz), λ (wavelength) in m',
    forms: { v: '{f} × {lam}', f: '{v} ÷ {lam}', lam: '{v} ÷ {f}' },
    ctx: [
      // f and λ in half steps (grade 8) so the speed comes out even; tenths in high school
      ...[['wave on a rope', 1, 5, 0.5, 3], ['wave on a long spring', 1, 4, 0.5, 2.5], ['water wave in a pool', 0.5, 2, 0.5, 4]].map(([who, flo, fhi, llo, lhi]) => ({
        gen: (r, H) => ({ f: H ? tenth(r, flo, fhi) : half(r, flo, fhi), lam: H ? tenth(r, llo, lhi) : half(r, llo, lhi) }),
        q: { v: f => `A ${who} has a frequency of ${f('f')} and a wavelength of ${f('lam')}. What is the speed of the wave?`,
          f: f => `A ${who} travels at ${f('v')} and has a wavelength of ${f('lam')}. What is its frequency?`,
          lam: f => `A ${who} travels at ${f('v')} with a frequency of ${f('f')}. What is its wavelength?` } })),
      { gen: r => ({ f: tenth(r, 0.1, 0.5), lam: r.int(5, 40) }),
        q: { v: f => `An ocean wave has a frequency of ${f('f')} and a wavelength of ${f('lam')}. What is the speed of the wave?`,
          f: f => `An ocean wave travels at ${f('v')} and has a wavelength of ${f('lam')}. What is its frequency?`,
          lam: f => `An ocean wave travels at ${f('v')} with a frequency of ${f('f')}. What is its wavelength?` } },
      // sound in air at 20 °C is about 343 m/s
      { hsOnly: true, gen: r => { const f = r.int(2, 40) * 50; return { f, lam: sf3(343 / f) }; },
        q: { v: f => `A sound wave in air has a frequency of ${f('f')} and a wavelength of ${f('lam')}. What is the speed of sound in the air?`,
          f: f => `Sound travels through air at ${f('v')}. A note has a wavelength of ${f('lam')}. What is its frequency?`,
          lam: f => `Sound travels through air at ${f('v')}. What is the wavelength of a ${f('f')} note?` } },
    ],
  },
  momcons: {
    label: 'Conservation of momentum', special: 'momcons', hsOnly: true,
    sym: { m1: 'm<sub>1</sub>', v1: 'v<sub>1</sub>', m2: 'm<sub>2</sub>', v2: 'v<sub>2</sub>', vf: 'v′', u: 'v<sub>2</sub>' },
    name: { m1: 'mass', v1: 'speed', m2: 'mass', v2: 'speed', vf: 'speed after a collision', u: 'recoil speed' },
    unit: { m1: 'kg', v1: 'm/s', m2: 'kg', v2: 'm/s', vf: 'm/s', u: 'm/s' },
    formula: 'm₁v₁ + m₂v₂ = (m₁ + m₂)v′ (they stick together) &nbsp; 0 = m₁v₁ − m₂v₂ (they push apart from rest)',
    also: 'total momentum before = total momentum after', units: 'm in kg, v in m/s, momentum in kg·m/s; v′ is the shared speed after the collision',
    forms: { vf: '({m1} × {v1} + {m2} × {v2}) ÷ ({m1} + {m2})', u: '{m1} × {v1} ÷ {m2}' },
    ctx: [
      // sticking together: the second object is at rest or moving the same way more slowly
      ...[['cart', 'cart', 0.5, 3, 1, 4], ['train car', 'train car', 10, 30, 1, 4], ['clay ball', 'wooden block', 0.1, 0.5, 2, 8], ['football player', 'player', 70, 110, 2, 7]].map(([a, b, mlo, mhi, vlo, vhi]) => ({
        gen: r => { const m1 = a === 'train car' ? r.int(mlo, mhi) * 1000 : a === 'clay ball' ? tenth(r, mlo, mhi) : a === 'cart' ? tenth(r, mlo, mhi) : r.int(mlo, mhi);
          const m2 = a === 'train car' ? r.int(mlo, mhi) * 1000 : a === 'clay ball' ? tenth(r, 0.5, 2) : a === 'cart' ? tenth(r, mlo, mhi) : r.int(mlo, mhi);
          const v1 = tenth(r, vlo, vhi), v2 = r.chance(.6) ? 0 : tenth(r, 0.5, Math.max(0.5, v1 - 0.5));
          return v2 >= v1 ? null : { m1, v1, m2, v2 }; },
        q: { vf: f => `A ${f('m1')} ${a} moving at ${f('v1')} ${a === 'football player' ? 'tackles' : 'runs into'} a ${f('m2')} ${b} ${f('v2', 'at rest', 'moving the same way at ')}. They ${a === 'football player' ? 'hold on to each other' : 'stick together'}. What is their speed right after?` } })),
      // pushing apart from rest
      { gen: r => ({ m1: r.int(40, 70), v1: tenth(r, 1, 4), m2: r.int(50, 90) }),
        q: { u: f => `Two skaters stand still on the ice and push off each other. The ${f('m1')} skater moves away at ${f('v1')}. How fast does the ${f('m2')} skater move in the other direction?` } },
      { gen: r => ({ m1: r.int(2, 10), v1: tenth(r, 2, 8), m2: r.int(80, 120) }),
        q: { u: f => `An astronaut floating at rest throws a ${f('m1')} tool at ${f('v1')}. The astronaut and suit have a mass of ${f('m2')}. How fast does the astronaut drift the other way?` } },
      { gen: r => ({ m1: r.int(2, 10), v1: r.int(10, 30) * 10, m2: r.int(5, 15) * 100 }),
        q: { u: f => `A ${f('m2')} cannon at rest on wheels fires a ${f('m1')} ball at ${f('v1')}. How fast does the cannon roll backward?` } },
    ],
  },
  circuit: {
    label: 'Series and parallel circuits', special: 'circuit', hsOnly: true,
    sym: { V: 'V', R1: 'R<sub>1</sub>', R2: 'R<sub>2</sub>', R3: 'R<sub>3</sub>', Rt: 'R<sub>T</sub>', I: 'I' },
    name: { V: 'voltage', R1: 'resistance', R2: 'resistance', R3: 'resistance', Rt: 'total resistance', I: 'current' },
    unit: { V: 'V', R1: 'Ω', R2: 'Ω', R3: 'Ω', Rt: 'Ω', I: 'A' },
    formula: 'Series: R<sub>T</sub> = R₁ + R₂ + … &nbsp; Parallel: 1 ÷ R<sub>T</sub> = 1 ÷ R₁ + 1 ÷ R₂ + … &nbsp; then I = V ÷ R<sub>T</sub>',
    also: 'I = V ÷ R', units: 'R in ohms (Ω), V in volts (V), I in amperes (A)',
    forms: { Rt: '{R1} + {R2}', I: '{V} ÷ {Rt}' },
    ctx: [{ gen: r => { const ser = r.chance(.5) ? 'series' : 'parallel', n = r.chance(.35) ? 3 : 2;
        const Rs = r.distinct(n, () => r.pick([10, 20, 30, 40, 50, 60, 100, 120, 150, 200, 300])).sort((a, b) => a - b);
        if (Rs.length < n) return null;
        const g = { V: r.pick([6, 9, 12, 24]), R1: Rs[0], R2: Rs[1], ser }; if (n === 3) g.R3 = Rs[2];
        return g; },
      q: { Rt: f => `${rlist(f)} are connected in ${f.g.ser}. What is the total resistance of the circuit?`,
        I: f => `${rlist(f)} are connected in ${f.g.ser} to ${src(f('V'))}. Find the total resistance, then the current from the battery.` } }],
  },
};
// "A 10 Ω resistor and a 20 Ω resistor" or "10 Ω, 20 Ω and 30 Ω resistors"
const rlist = f => f.g.R3 != null ? `${f('R1')}, ${f('R2')} and ${f('R3')} resistors` : `A ${f('R1')} resistor and a ${f('R2')} resistor`;
const totalR = g => { const Rs = [g.R1, g.R2, g.R3].filter(x => x != null); return g.ser === 'series' ? Rs.reduce((a, b) => a + b, 0) : 1 / Rs.reduce((a, b) => a + 1 / b, 0); };
// moving objects shared by momentum and kinetic energy (a baseball is about 0.145 kg, a size 5 soccer ball about 0.43 kg)
const MOVERS = [['baseball', () => 0.145, 20, 45], ['soccer ball', () => 0.43, 5, 30], ['bowling ball', r => tenth(r, 4, 7), 2, 8],
  ['runner', r => r.int(50, 90), 3, 9], ['car', r => r.int(18, 40) * 50, 5, 30], ['cyclist and bike', r => r.int(60, 100), 4, 12]];
TOPICS.momentum.ctx = MOVERS.map(([obj, m, lo, hi]) => ({
  gen: r => ({ m: m(r), v: tenth(r, lo, hi) }),
  q: { p: f => `A ${f('m')} ${obj} moves at ${f('v')}. What is the momentum of the ${obj}?`,
    m: f => `A ${obj} moving at ${f('v')} has a momentum of ${f('p')}. What is the mass of the ${obj}?`,
    v: f => `A ${f('m')} ${obj} has a momentum of ${f('p')}. How fast is the ${obj} moving?` } }));
TOPICS.ke.ctx = MOVERS.map(([obj, m, lo, hi]) => ({
  gen: r => ({ m: m(r), v: tenth(r, lo, hi) }),
  q: { KE: f => `A ${f('m')} ${obj} moves at ${f('v')}. What is the kinetic energy of the ${obj}?`,
    m: f => `A ${obj} moving at ${f('v')} has ${f('KE')} of kinetic energy. What is the mass of the ${obj}?`,
    v: f => `A ${f('m')} ${obj} has ${f('KE')} of kinetic energy. How fast is the ${obj} moving?` } }));

// a battery for the usual cell voltages, a lab power supply otherwise
function src(V, cap) { const t = /^(1\.5|3|4\.5|6|9|12) V$/.test(V) ? `a ${V} battery` : `a power supply set to ${V}`; return cap ? t[0].toUpperCase() + t.slice(1) : t; }
// F = m × a and wave speed from grade 8; Ohm's law, momentum, kinetic energy, conservation of momentum and circuits from grade 9
const topicsFor = g => ['density', 'speed', 'accel'].concat(+g >= 8 ? ['force'] : [], ['weight', 'work', 'power'], hs(g) ? ['ohm', 'momentum', 'ke'] : [], +g >= 8 ? ['wave'] : [], hs(g) ? ['momcons', 'circuit'] : []);

// solve one unknown from the other values (the make side; verify checks with the forward relation instead)
function solve(tp, unk, g) {
  const T = TOPICS[tp];
  if (T.special === 'accel') return { a: () => (g.vf - g.vi) / g.t, t: () => (g.vf - g.vi) / g.a, vf: () => g.vi + g.a * g.t }[unk]();
  if (T.special === 'ke') return { KE: () => 0.5 * g.m * g.v * g.v, m: () => 2 * g.KE / (g.v * g.v), v: () => Math.sqrt(2 * g.KE / g.m) }[unk]();
  if (T.special === 'momcons') return { vf: () => (g.m1 * g.v1 + g.m2 * g.v2) / (g.m1 + g.m2), u: () => g.m1 * g.v1 / g.m2 }[unk]();
  if (T.special === 'circuit') return { Rt: () => totalR(g), I: () => g.V / totalR(g) }[unk]();
  const [X, Y, Z] = T.prod;
  return unk === X ? g[Y] * g[Z] : unk === Y ? g[X] / g[Z] : g[X] / g[Y];
}
const derivedKey = (tp, base) => { const sp = TOPICS[tp].special;
  return sp === 'accel' ? 'vf' : sp === 'ke' ? 'KE' : sp === 'momcons' ? ('v2' in base ? 'vf' : 'u') : sp === 'circuit' ? ('V' in base ? 'I' : 'Rt') : TOPICS[tp].prod[0]; };

// one problem: values for every variable, an unknown, the question text
function problem(r, tp, H, grade) {
  const T = TOPICS[tp];
  const ctxs = T.ctx.filter(c => H || !c.hsOnly);
  const c = r.pick(ctxs);
  const base = c.gen(r, H, !H && +grade <= 7);
  if (!base) return null;
  const dk = derivedKey(tp, base);
  const all = { ...base };
  if (!(dk in base)) all[dk] = H ? sf3(solve(tp, dk, base)) : r2(solve(tp, dk, base));
  const unks = c.only ? [c.only] : Object.keys(c.q);
  let unk = r.pick(unks);
  if (tp === 'circuit') { unk = r.chance(.3) ? 'Rt' : 'I'; if (unk === 'Rt') { delete all.V; delete all.I; } }
  if (!H && Math.abs(all[dk] - solve(tp, dk, all)) > 1e-9) return null;   // grades 6-8 stay exact
  const g = { ...all }; delete g[unk];
  if (tp === 'accel' && unk !== 'vf' && all.vf <= all.vi) return null;
  const raw = solve(tp, unk, g);
  const ans = H ? sf3(raw) : r2(raw);
  if (!(ans > 0)) return null;
  // high school: skip a value that sits right on a rounding boundary (33.65 -> 33.7), where float noise could flip the key
  if (H && Math.abs(raw - ans) > 0.45 * 10 ** (Math.floor(Math.log10(ans)) - 2)) return null;
  if (tp === 'accel' && all.vf > (c.vmax || 45)) return null;
  const f = (k, zero, pre = '') => ((k === 'vi' || k === 'v2') && !g[k]) ? zero : pre + `${show(g[k])} ${T.unit[k]}`;
  f.g = g;
  return { kind: 'calc', topic: tp, unk, g, ans, H, q: art(c.q[unk](f)), a: `${H ? show3(ans) : show(ans)} ${T.unit[unk]}` };
}

const symH = (tp, k) => `<i>${TOPICS[tp].sym[k]}</i>`.replace(/<i>([^<]*)<sub>/, '<i>$1</i><sub>').replace(/<\/sub><\/i>$/, '</sub>');
const formHtml = (tp, unk, vals) => {
  const T = TOPICS[tp];
  const body = T.forms[unk].replace(/\{(\w+)\}/g, (_, k) => vals ? show(vals[k]) : symH(tp, k));
  return `${symH(tp, unk)} = ${body}`;
};
const solution = it => {
  if (it.topic === 'circuit') {
    const Rs = [it.g.R1, it.g.R2, it.g.R3].filter(x => x != null), ser = it.g.ser === 'series', RT = symH('circuit', 'Rt');
    const rsum = ser ? `${RT} = ${Rs.map(show).join(' + ')}` : `1 ÷ ${RT} = ${Rs.map(x => `1 ÷ ${show(x)}`).join(' + ')}`;
    const Rt = show3(sf3(totalR(it.g)));
    const formula = ser ? `${RT} = <i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>${Rs.length > 2 ? ' + <i>R</i><sub>3</sub>' : ''}` : `1 ÷ ${RT} = 1 ÷ <i>R</i><sub>1</sub> + 1 ÷ <i>R</i><sub>2</sub>${Rs.length > 2 ? ' + 1 ÷ <i>R</i><sub>3</sub>' : ''}`;
    const eq = ser ? '=' : '≈';
    if (it.unk === 'Rt') return { formula, sub: rsum, ans: `${RT} ${eq} ${esc(it.a)}` };
    return { formula: `${formula}; <i>I</i> = <i>V</i> ÷ ${RT}`, sub: `${rsum}, so ${RT} ${eq} ${Rt} Ω; <i>I</i> = ${show(it.g.V)} ÷ ${Rt}`, ans: `<i>I</i> ≈ ${esc(it.a)}` };
  }
  return { formula: formHtml(it.topic, it.unk), sub: formHtml(it.topic, it.unk, it.g), ans: `${symH(it.topic, it.unk)} = ${it.H ? '≈ ' : ''}${esc(it.a)}`.replace('= ≈', '≈') };
};

// one reasoning question per sheet, on the sheet's first topic
function reasoning(r, tp, H) {
  const nm = H ? (x => sf3(x)) : r2;
  switch (tp) {
    case 'density': {
      for (let k = 0; k < 80; k++) {
        const objs = 'ABCD'.split('').map(L => { const D = r.int(H ? 30 : 3, H ? 250 : 25) / (H ? 100 : 10), V = r.int(H ? 5 : 2, H ? 60 : 12) * (H ? 1 : 5); return { L, m: r2(D * V), V, D }; });
        const fl = objs.filter(o => o.m / o.V < 1);
        if (objs.some(o => Math.abs(o.D - 1) < 0.05) || !fl.length || fl.length === 4) continue;
        return { kind: 'float', objs, q: 'Water has a density of 1.0 g/cm³. An object floats in water when its density is less than 1.0 g/cm³. Find the density of each object. Which objects float?',
          a: fl.map(o => o.L).join(', ') };
      }
      return null;
    }
    case 'speed': {
      if (r.chance(.35)) { const v = r.int(10, 30); return { kind: 'velocity', v, q: `Two cars both drive at ${v} m/s. One drives north and the other drives south. Do they have the same speed? Do they have the same velocity? Explain.`,
        a: `Same speed (${v} m/s), different velocities, because velocity includes direction (north or south).` }; }
      const a = { t: r.int(10, 30) }, b = { t: r.int(10, 30) };
      a.v = H ? tenth(r, 3, 8) : r.int(3, 8); b.v = H ? tenth(r, 3, 8) : r.int(3, 8);
      if (a.v === b.v) return null;
      a.d = r2(a.v * a.t); b.d = r2(b.v * b.t);
      return { kind: 'faster', A: a, B: b, q: `Runner A runs ${show(a.d)} m in ${a.t} s. Runner B runs ${show(b.d)} m in ${b.t} s. Who is faster? Show both speeds.`,
        a: `Runner ${a.v > b.v ? 'A' : 'B'} (A: ${show(a.v)} m/s, B: ${show(b.v)} m/s)` };
    }
    case 'accel': {
      const A = { t: r.int(2, 6), a: r.int(2, 6) }, B = { t: r.int(5, 12), a: r.int(1, 3) };
      if (A.a === B.a) return null;
      A.vf = A.a * A.t; B.vf = B.a * B.t;
      return { kind: 'accel2', A, B, q: `Car A speeds up from rest to ${A.vf} m/s in ${A.t} s. Car B speeds up from rest to ${B.vf} m/s in ${B.t} s. Which car has the greater acceleration? Show both.`,
        a: `Car ${A.a > B.a ? 'A' : 'B'} (A: ${A.a} m/s², B: ${B.a} m/s²)` };
    }
    case 'force': {
      const m1 = r.int(4, 15), k = r.int(2, 4), F = r.int(2, 10) * 10;
      return { kind: 'samef', m1, m2: m1 * k, F, q: `The same net force of ${F} N pushes a ${m1} kg cart and a ${m1 * k} kg cart. Which cart has the greater acceleration, and how many times greater is it?`,
        a: `The ${m1} kg cart, ${k} times greater (${show(r2(F / m1))} m/s² compared with ${show(r2(F / (m1 * k)))} m/s²)` };
    }
    case 'weight': {
      const m = r.int(50, 90);
      return { kind: 'moon', m, q: `An astronaut has a mass of ${m} kg on Earth. She travels to the Moon, where gravity is weaker. Does her mass change? Does her weight change? Explain.`,
        a: `Her mass stays ${m} kg because the amount of matter is the same. Her weight gets smaller because the Moon's g is smaller than Earth's.` };
    }
    case 'work': {
      const F = r.int(10, 60) * 10;
      return { kind: 'wall', F, q: `You push on a brick wall with a force of ${F} N for a whole minute, but the wall does not move. How much work do you do on the wall? Explain.`,
        a: '0 J, because the wall moves 0 m and work = force × distance.' };
    }
    case 'power': {
      const W = r.int(8, 20) * 150, t1 = r.int(4, 8), t2 = t1 + r.int(1, 4);
      return { kind: 'pow2', W, t1, t2, q: `Two students each do ${show(W)} J of work carrying boxes up the stairs. Student A takes ${t1} s and student B takes ${t2} s. Who has more power? Show both.`,
        a: `Student A (A: ${show(nm(W / t1))} W, B: ${show(nm(W / t2))} W)` };
    }
    case 'ohm': {
      const V = r.pick([6, 9, 12]), R = r.pick([2, 3, 4, 6]);
      return { kind: 'ohm2', V, R, q: `A ${V} V battery is connected to a ${R} Ω resistor. The resistor is swapped for a ${2 * R} Ω resistor and the battery stays the same. What happens to the current? Give both currents.`,
        a: `The current is cut in half: ${show(r2(V / R))} A becomes ${show(r2(V / (2 * R)))} A.` };
    }
    case 'momentum': {
      const v1 = tenth(r, 25, 45), m2 = tenth(r, 4, 7), v2 = tenth(r, 2, 6);
      const p1 = sf3(0.145 * v1), p2 = sf3(m2 * v2);
      if (Math.abs(p1 - p2) < 0.5) return null;
      return { kind: 'mom2', v1, m2, v2, q: `Which has more momentum: a 0.145 kg baseball thrown at ${show(v1)} m/s, or a ${show(m2)} kg bowling ball rolling at ${show(v2)} m/s? Show both.`,
        a: `The ${p1 > p2 ? 'baseball' : 'bowling ball'} (baseball ${show(p1)} kg·m/s, bowling ball ${show(p2)} kg·m/s)` };
    }
    case 'wave': {
      const fA = r.int(1, 3), v = 2 * fA * r.int(1, 4), lamB = v / (2 * fA), lamA = 2 * lamB;
      return { kind: 'wave2', fA, v, q: `Two waves travel along the same rope at the same speed, ${v} m/s. Wave A has a frequency of ${fA} Hz and wave B has a frequency of ${2 * fA} Hz. Which wave has the longer wavelength, and how many times longer? Show both.`,
        a: `Wave A, 2 times longer (A: ${show(lamA)} m, B: ${show(lamB)} m)` };
    }
    case 'momcons': {
      const m1 = r.int(40, 60), m2 = m1 + r.int(10, 40);
      return { kind: 'push2', m1, m2, q: `A ${m1} kg skater and a ${m2} kg skater stand still, then push off each other. Which skater moves away faster? Explain using momentum.`,
        a: `The ${m1} kg skater. Total momentum stays 0, so the two momenta are equal and opposite, and the smaller mass needs the larger speed.` };
    }
    case 'circuit': {
      const R = r.pick([10, 20, 30, 40, 60]), V = r.pick([6, 12, 24]);
      return { kind: 'circ2', R, V, q: `Two ${R} Ω resistors are connected to a ${V} V battery, first in series and then in parallel. Which arrangement draws more current from the battery? Give both currents.`,
        a: `Parallel (series: ${show(nm(V / (2 * R)))} A, parallel: ${show(nm(V / (R / 2)))} A)` };
    }
    case 'ke': {
      const m = r.int(50, 90), v = r.int(2, 5);
      const k1 = 0.5 * m * v * v, k2 = 0.5 * m * 4 * v * v;
      return { kind: 'ke2', m, v, q: `A ${m} kg runner speeds up from ${v} m/s to ${2 * v} m/s. Find the kinetic energy at each speed. How many times larger is it?`,
        a: `${show(k1)} J becomes ${show(k2)} J, 4 times larger, because KE depends on v².` };
    }
  }
  return null;
}

Gen.add('science-calc', {
  title: 'Science Calculations', type: 'Apply',
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '8' },
    { id: 'topic', label: 'Topic', type: 'select', def: 'density',
      options: v => topicsFor(v.grade).map(t => [t, TOPICS[t].label]).concat([['mix', 'Mixed review']]) },
    { id: 'count', label: 'Problems', type: 'select', options: [['4', '4'], ['6', '6'], ['8', '8']], def: '6' },
    { id: 'topic2', label: 'Second topic (the sheet alternates between the two)', type: 'select', def: 'none', show: v => v.topic !== 'mix',
      options: v => [['none', 'No second topic']].concat(topicsFor(v.grade).filter(t => t !== v.topic).map(t => [t, TOPICS[t].label])) },
  ],
  css: `
.sc-box { border: 1.5px solid #333; border-radius: 6px; padding: 6px 12px; margin: 6px 0 8px; }
.sc-box p { margin: 2px 0; }
.sc-box .sc-f { font: 600 16px/1.4 var(--sans); }
.sc-box .sc-u { font-size: 13px; color: #333; }
.sc-ps { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 14px; }
.sc-p { border: 1px solid #888; border-radius: 6px; padding: 6px 10px 8px; break-inside: avoid; }
.sc-p > p { margin: 0 0 4px; font-size: 14px; line-height: 1.35; }
.sc-l { display: flex; align-items: flex-end; gap: 6px; height: 0.34in; }
.sc-l > span { font: 600 11px var(--sans); text-transform: uppercase; letter-spacing: .06em; width: 6.4em; color: #444; padding-bottom: 2px; }
.sc-l > b { flex: 1; border-bottom: 1px solid #555; font-weight: 400; font-size: 14px; padding-bottom: 1px; }
.sc-tab td, .sc-tab th { padding: 2px 8px; height: auto; }
.sc-top { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; align-items: stretch; }
.sc-top > div { margin: 0; }
.sc-flt { display: flex; gap: 18px; align-items: flex-end; flex-wrap: wrap; }
@media (max-width: 700px) { .sc-top, .sc-ps { grid-template-columns: 1fr; } }
@media print { .sc-p > p { font-size: 9.5pt; } .sc-l { height: 0.24in; } .sc-tab td, .sc-tab th { padding: 1px 8px; } .sc-p > p { margin-bottom: 2px; } .sc-p { padding: 4px 8px 6px; } .sc-ps { gap: 7px 12px; } }
`,
  make(v, r) {
    const g = v.grade, H = hs(g), n = +v.count;
    const two = v.topic !== 'mix' && v.topic2 !== 'none' && v.topic2 !== v.topic && topicsFor(g).includes(v.topic2) ? v.topic2 : null;
    const pool = v.topic === 'mix' ? r.sample(topicsFor(g), n > 6 ? 4 : 3) : two ? [v.topic, two] : [v.topic];
    let i = 0;
    const items = r.distinct(n, () => problem(r, pool[(i++) % pool.length], H, g), p => p.q);
    const used = pool.filter(t => items.some(it => it.topic === t));
    const ex = r.distinct(1, () => { const e = problem(r, used[0], H, g); return e && !items.some(it => it.q === e.q) ? e : null; }, p => p.q)[0] || items[0];
    let rq = null;
    // a mixed sheet saves room by using a short written question rather than the density table
    const rt = used.length > 1 && used.some(t => t !== 'density') ? used.filter(t => t !== 'density') : used;
    for (let k = 0; k < 20 && !rq; k++) rq = reasoning(r, rt[k % rt.length], H);
    const rule = H ? 'Round each answer to three significant figures.' : 'Every answer comes out even, with two decimal places at most.';
    const fbox = `<div class="sc-box"><p class="ws-tag">Formulas</p>${used.map(t => { const T = TOPICS[t];
      return `<p><span class="sc-f">${T.label}: ${T.formula.replace(/\b([A-Za-z]{1,2})\b(?![^<]*>)/g, '<i>$1</i>')}</span>${+g <= 7 && used.length === 1 ? ` <span class="sc-u">(also ${T.also})</span>` : ''}${used.length > 1 ? ' ' : '<br>'}<span class="sc-u">${T.units}</span></p>`; }).join('')}<p class="sc-u"><b>Rounding:</b> ${rule}</p></div>`;
    const exs = solution(ex);
    const exHtml = example(`<b>${esc(ex.q)}</b>`, `Formula: ${exs.formula} &nbsp; Substitute: ${exs.sub} &nbsp; Answer: <b>${exs.ans}</b>`);
    const box = (it, k) => { const s = solution(it);
      return `<div class="sc-p"><p><span class="ws-num">${k}.</span> ${esc(it.q)}</p>` +
        `<div class="sc-l"><span>Formula</span><b><span class="ws-ans">${s.formula}</span></b></div>` +
        `<div class="sc-l"><span>Substitute</span><b><span class="ws-ans">${s.sub}</span></b></div>` +
        `<div class="sc-l"><span>Answer</span><b><span class="ws-ans">${s.ans}</span></b></div></div>`; };
    const parts = [part('', `<div class="sc-top">${fbox}${exHtml}</div>`), part('Problems: write the formula, put in the numbers, then give the answer with its unit', `<div class="sc-ps">${items.map((it, k) => box(it, k + 1)).join('')}</div>`)];
    const all = items.slice();
    if (rq) {
      let html = `<div class="ws-q"><p><span class="ws-num">${n + 1}.</span> ${esc(rq.q)}</p>`;
      if (rq.kind === 'float') html += `<div class="sc-flt"><table class="ws-table sc-tab" style="width:auto"><thead><tr><th>Object</th><th>Mass (g)</th><th>Volume (cm³)</th><th>Density (g/cm³)</th><th>Floats?</th></tr></thead><tbody>${rq.objs.map(o =>
        `<tr><td>${o.L}</td><td>${show(o.m)}</td><td>${show(o.V)}</td><td><span class="ws-ans">${show(r2(o.m / o.V))}</span></td><td><span class="ws-ans">${o.m / o.V < 1 ? 'yes' : 'no'}</span></td></tr>`).join('')}</tbody></table>` +
        `<p>Objects that float: <span class="ws-blank" style="min-width:8em"><span class="ws-ans">${esc(rq.a)}</span></span></p></div>`;
      else html += lines(2) + keyline(esc(rq.a));
      html += '</div>';
      parts.push(part('', html));
      rq.q = art(rq.q);
      all.push(rq);
    }
    const label = v.topic === 'mix' ? 'Mixed review' : two ? `${TOPICS[v.topic].label} and ${TOPICS[two].label.toLowerCase()}` : TOPICS[v.topic].label;
    const gl = GRADES.find(x => x[0] === g)[1];
    return {
      title: `${label}: ${gl}`, level: `${gl}, ${H ? 'three significant figures' : 'answers come out even'}`,
      ican: `I can use a formula to find ${v.topic === 'mix' || two ? 'a missing quantity' : 'the ' + Object.keys(TOPICS[v.topic].forms).filter(k => H || k !== 'g').map(k => TOPICS[v.topic].name[k]).join(', ')} and give my answer with the right unit.`.replace(/, ([^,]*) and give/, ' or $1 and give'),
      directions: 'For each problem, write the formula you need, write it again with the numbers put in, and solve. Write the answer with its unit on the Answer line.',
      minutes: n > 6 ? 35 : 25, materials: 'pencil, calculator',
      parts, items: all,
      mistakes: 'Dividing the wrong way round when solving for a value that is not on the left of the formula (for example V = D ÷ m instead of m ÷ D), dropping the unit or writing the unit of a different quantity, and in mixed sheets mixing up the two meanings of W (weight in N, work in J).' + (H ? ' For kinetic energy, squaring only after multiplying by the mass, or forgetting the ½.' : ''),
      notes: `Every value is realistic for its object. ${H ? 'Grades 9 to 12 use lab-style values; the key rounds to three significant figures, so an answer that differs only in the last digit from rounding along the way should get credit.' : 'Grades 6 to 8 are built so every answer comes out even or to two decimal places.'} Earth's g is 9.8 m/s² throughout. Press New sheet for new numbers at the same level.`,
    };
  },
  verify(s, v) {
    const out = [];
    const H = +v.grade >= 9;
    // forward relations, written independently of the solved forms in make: each returns left - right
    const FWD = { density: x => x.m - x.D * x.V, speed: x => x.d - x.v * x.t, accel: x => (x.vf - x.vi) - x.a * x.t, force: x => x.F - x.m * x.a,
      weight: x => x.W - x.m * x.g, work: x => x.W - x.F * x.d, power: x => x.W - x.P * x.t, ohm: x => x.V - x.I * x.R,
      momentum: x => x.p - x.m * x.v, ke: x => x.KE - 0.5 * x.m * x.v * x.v, wave: x => x.v - x.f * x.lam,
      // momentum before = momentum after; a push-off from rest gives equal and opposite momenta
      momcons: x => 'u' in x ? x.m1 * x.v1 - x.m2 * x.u : x.m1 * x.v1 + x.m2 * x.v2 - (x.m1 + x.m2) * x.vf,
      // series adds resistances; parallel adds conductances (1/R)
      circuit: x => { const Rs = [x.R1, x.R2, x.R3].filter(y => y != null); const tot = x.ser === 'series' ? Rs.reduce((a, b) => a + b, 0) : 1 / Rs.reduce((a, b) => a + 1 / b, 0);
        return 'I' in x ? x.I * tot - x.V : x.Rt - tot; } };
    const UNIT = { density: { D: 'g/cm³', m: 'g', V: 'cm³' }, speed: { v: 'm/s', d: 'm', t: 's' }, accel: { a: 'm/s²', vf: 'm/s', t: 's' }, force: { F: 'N', m: 'kg', a: 'm/s²' },
      weight: { W: 'N', m: 'kg', g: 'm/s²' }, work: { W: 'J', F: 'N', d: 'm' }, power: { P: 'W', W: 'J', t: 's' }, ohm: { V: 'V', I: 'A', R: 'Ω' },
      momentum: { p: 'kg·m/s', m: 'kg', v: 'm/s' }, ke: { KE: 'J', m: 'kg', v: 'm/s' }, wave: { v: 'm/s', f: 'Hz', lam: 'm' },
      momcons: { vf: 'm/s', u: 'm/s' }, circuit: { Rt: 'Ω', I: 'A' } };
    const num = a => parseFloat(String(a).replace(/,/g, ''));
    for (const it of s.items) {
      if (it.kind === 'calc') {
        const x = { ...it.g }, f = val => { x[it.unk] = val; return FWD[it.topic](x); };
        const a = num(it.a);
        if (!(a > 0)) { out.push(`${it.q}: answer ${it.a} is not positive`); continue; }
        if (!String(it.a).endsWith(' ' + UNIT[it.topic][it.unk])) out.push(`${it.q}: wrong unit in ${it.a}`);
        if (!H) {
          const scale = Math.max(1, ...Object.values(x).map(Math.abs));
          if (Math.abs(f(a)) > 1e-7 * scale) out.push(`${it.q}: ${it.a} does not satisfy the formula (off by ${f(a)})`);
          if (Math.round(a * 100) / 100 !== a) out.push(`${it.q}: ${it.a} has more than two decimals`);
        } else {
          const h = 0.5 * 10 ** (Math.floor(Math.log10(a)) - 2);
          if (f(a - h) * f(a + h) > 0) out.push(`${it.q}: ${it.a} is not the three-figure answer`);
          if (Number(a.toPrecision(3)) !== a) out.push(`${it.q}: ${it.a} has more than three significant figures`);
        }
        // the question must state every given value
        for (const [k, val] of Object.entries(it.g)) if (typeof val === 'number' && !(it.topic === 'weight' && k === 'g' && it.unk !== 'g') && !(it.topic === 'accel' && k === 'vi' && !val) && !(it.topic === 'momcons' && k === 'v2' && !val) && !it.q.includes(fmt(val, 6) + ' ')) out.push(`${it.q}: does not state ${k}`);
        if (it.topic === 'circuit' && !it.q.includes(' in ' + it.g.ser)) out.push(`${it.q}: does not say ${it.g.ser}`);
        continue;
      }
      if (it.kind === 'float') {
        const want = it.objs.filter(o => o.m < o.V).map(o => o.L).join(', ');
        if (want !== it.a) out.push(`float: key ${it.a}, should be ${want}`);
        if (it.objs.some(o => o.m === o.V)) out.push('float: an object with density exactly 1');
      } else if (it.kind === 'faster') {
        const va = it.A.d / it.A.t, vb = it.B.d / it.B.t;
        if (!it.a.startsWith(`Runner ${va > vb ? 'A' : 'B'}`)) out.push(`faster: key ${it.a}`);
      } else if (it.kind === 'accel2') {
        if (!it.a.startsWith(`Car ${it.A.vf / it.A.t > it.B.vf / it.B.t ? 'A' : 'B'}`)) out.push(`accel2: key ${it.a}`);
      } else if (it.kind === 'samef') {
        if (!it.a.startsWith(`The ${it.m1} kg cart, ${it.m2 / it.m1} times`)) out.push(`samef: key ${it.a}`);
      } else if (it.kind === 'wall') {
        if (!it.a.startsWith('0 J')) out.push('wall: key is not 0 J');
      } else if (it.kind === 'pow2') {
        if (!it.a.startsWith(it.t1 < it.t2 ? 'Student A' : 'Student B')) out.push(`pow2: key ${it.a}`);
      } else if (it.kind === 'ohm2') {
        if (!it.a.includes(`${fmt(it.V / it.R, 2)} A becomes ${fmt(it.V / it.R / 2, 2)} A`)) out.push(`ohm2: key ${it.a}`);
      } else if (it.kind === 'mom2') {
        if (!it.a.startsWith(`The ${0.145 * it.v1 > it.m2 * it.v2 ? 'baseball' : 'bowling ball'}`)) out.push(`mom2: key ${it.a}`);
      } else if (it.kind === 'wave2') {
        const lamA = it.v / it.fA, lamB = it.v / (2 * it.fA);
        if (lamA !== 2 * lamB || !it.a.startsWith(`Wave A, 2 times longer (A: ${fmt(lamA, 2)} m, B: ${fmt(lamB, 2)} m)`)) out.push(`wave2: key ${it.a}`);
      } else if (it.kind === 'push2') {
        if (!it.a.startsWith(`The ${Math.min(it.m1, it.m2)} kg skater`)) out.push(`push2: key ${it.a}`);
      } else if (it.kind === 'circ2') {
        const Is = it.V / (2 * it.R), Ip = it.V / (it.R / 2);
        if (!(Ip > Is) || !it.a.includes(`series: ${fmt(Number(Is.toPrecision(3)), 6)} A, parallel: ${fmt(Number(Ip.toPrecision(3)), 6)} A`)) out.push(`circ2: key ${it.a}`);
      } else if (it.kind === 'ke2') {
        if (!it.a.startsWith(`${fmt(it.m * it.v * it.v / 2, 2)} J becomes ${fmt(2 * it.m * it.v * it.v, 2)} J, 4 times`)) out.push(`ke2: key ${it.a}`);
      }
    }
    return out;
  },
});
})();
