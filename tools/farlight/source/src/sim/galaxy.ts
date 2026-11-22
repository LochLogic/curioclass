import { createRng, hashCoords } from './prng.ts';
import type { Vec3 } from './math.ts';

export type StarKind = 'warm-sun' | 'amber-dwarf' | 'sky-giant' | 'pulsar' | 'black-hole';

export type BiomeKind =
  | 'meadow-world'
  | 'coral-ocean'
  | 'golden-dunes'
  | 'aurora-ice'
  | 'crystal-garden'
  | 'cloud-giant'
  | 'amber-canyons'
  | 'volcanic-ember'
  | 'mist-forest'
  | 'crater-moon';

export interface StarRef {
  id: string;
  name: string;
  sectorX: number;
  sectorY: number;
  sectorZ: number;
  x: number; // light-years in galaxy space
  y: number;
  z: number;
  starKind: StarKind;
  isHome?: boolean;
}

export interface PlanetData {
  id: number;
  name: string;
  biome: BiomeKind;
  radius: number;
  orbitRadius: number;
  orbitAngle: number;
  position: Vec3;
  colorA: [number, number, number];
  colorB: [number, number, number];
  atmosphereColor: [number, number, number];
  hasRings: boolean;
  ringInner: number;
  ringOuter: number;
  ringTilt: number;
  ringColor: [number, number, number];
  landable: boolean;
  funFact: string;
}

export interface StarSystem {
  ref: StarRef;
  seed: number;
  name: string;
  starKind: StarKind;
  starRadius: number;
  starColor: [number, number, number];
  nebulaPrimary: [number, number, number];
  nebulaSecondary: [number, number, number];
  planets: PlanetData[];
  tagline: string;
}

export const SECTOR_SIZE_LY = 40;
export const GALAXY_RADIUS_LY = 3200;

const PREFIXES = [
  'Sun', 'Luma', 'Aure', 'Vela', 'Kora', 'Bree', 'Milo', 'Tala',
  'Sora', 'Novi', 'Peb', 'Caly', 'Opal', 'Zeph', 'Wisp', 'Hali',
  'Cora', 'Fenn', 'Liri', 'Rumi', 'Tavi', 'Yara', 'Orin', 'Mira',
];
const SUFFIXES = [
  'crest', 'bloom', 'haven', 'drift', 'spark', 'reach', 'vale', 'gleam',
  'spire', 'brook', 'glow', 'mere', 'song', 'wing', 'field', 'port',
  'light', 'bell', 'star', 'mist', 'dell', 'cove', 'rise', 'beam',
];

const BIOME_PALETTES: Record<
  BiomeKind,
  {
    a: [number, number, number];
    b: [number, number, number];
    atmo: [number, number, number];
    landable: boolean;
    fact: string;
  }
> = {
  'meadow-world': {
    a: [0.24, 0.72, 0.45],
    b: [0.16, 0.48, 0.78],
    atmo: [0.42, 0.78, 1.0],
    landable: true,
    fact: 'Rolling green hills and sunny oceans, full of curious critters!',
  },
  'coral-ocean': {
    a: [0.10, 0.65, 0.78],
    b: [0.95, 0.56, 0.46],
    atmo: [0.35, 0.88, 0.96],
    landable: true,
    fact: 'A warm archipelago world where coral reefs glow at twilight.',
  },
  'golden-dunes': {
    a: [0.93, 0.73, 0.42],
    b: [0.78, 0.45, 0.28],
    atmo: [0.98, 0.78, 0.52],
    landable: true,
    fact: 'Singing sand dunes shaped by gentle golden trade winds.',
  },
  'aurora-ice': {
    a: [0.78, 0.92, 0.98],
    b: [0.38, 0.68, 0.92],
    atmo: [0.45, 0.95, 0.85],
    landable: true,
    fact: 'Shimmering glaciers beneath dancing green and teal auroras.',
  },
  'crystal-garden': {
    a: [0.64, 0.48, 0.92],
    b: [0.32, 0.84, 0.82],
    atmo: [0.75, 0.62, 1.0],
    landable: true,
    fact: 'Giant quartz spires chime softly whenever a breeze passes by.',
  },
  'cloud-giant': {
    a: [0.94, 0.78, 0.56],
    b: [0.72, 0.46, 0.36],
    atmo: [0.96, 0.84, 0.66],
    landable: false,
    fact: 'A swirling giant made of colorful clouds and icy ring pebbles!',
  },
  'amber-canyons': {
    a: [0.88, 0.48, 0.30],
    b: [0.58, 0.32, 0.24],
    atmo: [0.96, 0.66, 0.44],
    landable: true,
    fact: 'Towering red-rock arches carved by ancient rivers.',
  },
  'volcanic-ember': {
    a: [0.28, 0.24, 0.26],
    b: [0.98, 0.44, 0.16],
    atmo: [0.95, 0.52, 0.30],
    landable: true,
    fact: 'Warm basalt valleys lit by slow-flowing glowing magma streams.',
  },
  'mist-forest': {
    a: [0.18, 0.58, 0.52],
    b: [0.46, 0.76, 0.42],
    atmo: [0.55, 0.88, 0.78],
    landable: true,
    fact: 'Lantern-trees light up the misty canopy every evening.',
  },
  'crater-moon': {
    a: [0.68, 0.67, 0.64],
    b: [0.46, 0.45, 0.48],
    atmo: [0.55, 0.62, 0.72],
    landable: true,
    fact: 'Low gravity lets you take huge bouncy moon-hops!',
  },
};

export const SOL_STAR_REF: StarRef = {
  id: 'sol',
  name: 'Sol (Home)',
  sectorX: 0,
  sectorY: 0,
  sectorZ: 0,
  x: 0,
  y: 0,
  z: 0,
  starKind: 'warm-sun',
  isHome: true,
};

export function starId(sx: number, sy: number, sz: number, index: number): string {
  return `${sx},${sy},${sz}:${index}`;
}

export function starDistanceLY(a: { x: number; y: number; z: number }, b: { x: number; y: number; z: number }): number {
  return Math.hypot(a.x - b.x, a.y - b.y, a.z - b.z);
}

function pickStarKind(rng: ReturnType<typeof createRng>): StarKind {
  const r = rng.next();
  if (r < 0.44) return 'warm-sun';
  if (r < 0.68) return 'amber-dwarf';
  if (r < 0.83) return 'sky-giant';
  if (r < 0.93) return 'pulsar';
  return 'black-hole';
}

/** Deterministically lists all stars inside a 3D galaxy sector */
export function getStarsInSector(galaxySeed: number, sx: number, sy: number, sz: number): StarRef[] {
  if (Math.abs(sy) > 2) return []; // Thin galactic disk

  const cx = (sx + 0.5) * SECTOR_SIZE_LY;
  const cz = (sz + 0.5) * SECTOR_SIZE_LY;
  const distFromCore = Math.hypot(cx, cz);
  if (distFromCore > GALAXY_RADIUS_LY) return [];

  const stars: StarRef[] = [];
  if (sx === 0 && sy === 0 && sz === 0) {
    stars.push(SOL_STAR_REF);
  }

  const seed = hashCoords(galaxySeed, sx, sy, sz);
  const rng = createRng(seed);

  // Denser near spiral arms, sparser at outer rim
  const angle = Math.atan2(cz, cx);
  const armWave = Math.cos(angle * 2 - distFromCore * 0.0045);
  const density = 0.55 + 0.35 * armWave + (1 - distFromCore / GALAXY_RADIUS_LY) * 0.4;
  const count = rng.chance(Math.min(0.95, density)) ? rng.int(1, 3) : 0;

  for (let i = 0; i < count; i++) {
    const x = (sx + rng.range(0.12, 0.88)) * SECTOR_SIZE_LY;
    const y = (sy + rng.range(-0.4, 0.4)) * SECTOR_SIZE_LY * 0.45;
    const z = (sz + rng.range(0.12, 0.88)) * SECTOR_SIZE_LY;
    if (sx === 0 && sy === 0 && sz === 0 && Math.hypot(x, y, z) < 18) continue;

    const name = `${rng.pick(PREFIXES)}${rng.pick(SUFFIXES)}`;
    stars.push({
      id: starId(sx, sy, sz, i),
      name,
      sectorX: sx,
      sectorY: sy,
      sectorZ: sz,
      x,
      y,
      z,
      starKind: pickStarKind(rng),
    });
  }
  return stars;
}

/** Queries all stars within `radiusLY` of a 3D galactic coordinate */
export function getNearbyStars(
  galaxySeed: number,
  center: { x: number; y: number; z: number },
  radiusLY: number,
): StarRef[] {
  const minSx = Math.floor((center.x - radiusLY) / SECTOR_SIZE_LY);
  const maxSx = Math.floor((center.x + radiusLY) / SECTOR_SIZE_LY);
  const minSy = Math.max(-2, Math.floor((center.y - radiusLY) / SECTOR_SIZE_LY));
  const maxSy = Math.min(2, Math.floor((center.y + radiusLY) / SECTOR_SIZE_LY));
  const minSz = Math.floor((center.z - radiusLY) / SECTOR_SIZE_LY);
  const maxSz = Math.floor((center.z + radiusLY) / SECTOR_SIZE_LY);

  const result: StarRef[] = [];
  for (let sx = minSx; sx <= maxSx; sx++) {
    for (let sy = minSy; sy <= maxSy; sy++) {
      for (let sz = minSz; sz <= maxSz; sz++) {
        const list = getStarsInSector(galaxySeed, sx, sy, sz);
        for (const st of list) {
          if (starDistanceLY(center, st) <= radiusLY) {
            result.push(st);
          }
        }
      }
    }
  }
  result.sort((a, b) => starDistanceLY(center, a) - starDistanceLY(center, b));
  return result;
}

/** Finds a welcoming starting Golden Sun system ~620 LY from Sol so kids can actually reach Home! */
export function getStartingStar(galaxySeed: number): StarRef {
  const candidates = getNearbyStars(galaxySeed, { x: 460, y: 0, z: 420 }, 160);
  const warm = candidates.find((s) => s.starKind === 'warm-sun' && !s.isHome);
  if (warm) return warm;
  return {
    id: 'start-haven',
    name: 'Sunbloom',
    sectorX: 11,
    sectorY: 0,
    sectorZ: 10,
    x: 455,
    y: 4,
    z: 418,
    starKind: 'warm-sun',
  };
}

function buildSolSystem(): StarSystem {
  const mkPlanet = (
    id: number,
    name: string,
    biome: BiomeKind,
    radius: number,
    orbitRadius: number,
    orbitAngle: number,
    colorA: [number, number, number],
    colorB: [number, number, number],
    atmosphereColor: [number, number, number],
    funFact: string,
    hasRings = false,
  ): PlanetData => ({
    id,
    name,
    biome,
    radius,
    orbitRadius,
    orbitAngle,
    position: {
      x: Math.cos(orbitAngle) * orbitRadius,
      y: 0,
      z: Math.sin(orbitAngle) * orbitRadius,
    },
    colorA,
    colorB,
    atmosphereColor,
    hasRings,
    ringInner: radius * 1.38,
    ringOuter: radius * 2.45,
    ringTilt: 0.42,
    ringColor: [0.94, 0.88, 0.74],
    landable: biome !== 'cloud-giant',
    funFact,
  });

  return {
    ref: SOL_STAR_REF,
    seed: 1,
    name: 'Sol (Home)',
    starKind: 'warm-sun',
    starRadius: 185,
    starColor: [1.0, 0.92, 0.72],
    nebulaPrimary: [0.16, 0.45, 0.78],
    nebulaSecondary: [0.85, 0.56, 0.36],
    tagline: 'Welcome home! Our Solar System: blue Earth, rusty Mars, and ringed Saturn.',
    planets: [
      mkPlanet(0, 'Mercury', 'crater-moon', 18, 380, 0.4, [0.66, 0.63, 0.60], [0.46, 0.44, 0.44], [0.4, 0.42, 0.48], 'The fastest planet around the Sun. A year here is just 88 Earth days!'),
      mkPlanet(1, 'Venus', 'golden-dunes', 28, 560, 1.8, [0.96, 0.82, 0.54], [0.84, 0.62, 0.34], [0.98, 0.86, 0.62], 'Wrapped in bright golden clouds, making it the brightest planet in our sky.'),
      mkPlanet(2, 'Earth', 'meadow-world', 32, 780, 3.1, [0.22, 0.66, 0.36], [0.12, 0.42, 0.82], [0.38, 0.74, 1.0], 'Home sweet home! Sparkling blue oceans, green continents, and cozy cities.'),
      mkPlanet(3, 'Mars', 'amber-canyons', 24, 1020, 4.4, [0.86, 0.42, 0.24], [0.62, 0.28, 0.18], [0.92, 0.56, 0.38], 'Home to Olympus Mons, the tallest volcano in the entire Solar System!'),
      mkPlanet(4, 'Jupiter', 'cloud-giant', 82, 1380, 5.5, [0.92, 0.78, 0.62], [0.76, 0.44, 0.30], [0.92, 0.80, 0.66], 'So huge that over 1,300 Earths could fit inside its swirling cloud bands!'),
      mkPlanet(5, 'Saturn', 'cloud-giant', 70, 1780, 0.9, [0.95, 0.86, 0.64], [0.78, 0.68, 0.48], [0.96, 0.88, 0.70], 'Famous for its sparkling rings made of billions of ice crystals!', true),
    ],
  };
}

export function generateStarSystemFromRef(galaxySeed: number, ref: StarRef): StarSystem {
  if (ref.isHome || ref.id === 'sol') {
    return buildSolSystem();
  }
  const seed = hashCoords(
    galaxySeed,
    Math.round(ref.x * 10),
    Math.round(ref.y * 10),
    Math.round(ref.z * 10),
  );
  const rng = createRng(seed);
  const starKind = ref.starKind;

  const starConfig: Record<
    StarKind,
    {
      radius: number;
      color: [number, number, number];
      nebA: [number, number, number];
      nebB: [number, number, number];
      tagline: string;
    }
  > = {
    'warm-sun': {
      radius: 180,
      color: [1.0, 0.88, 0.65],
      nebA: [0.16, 0.52, 0.74],
      nebB: [0.88, 0.46, 0.38],
      tagline: 'A bright golden star with friendly, sunlit worlds.',
    },
    'amber-dwarf': {
      radius: 135,
      color: [1.0, 0.62, 0.34],
      nebA: [0.78, 0.34, 0.42],
      nebB: [0.96, 0.68, 0.36],
      tagline: 'A cozy orange star casting perpetual sunset light.',
    },
    'sky-giant': {
      radius: 230,
      color: [0.62, 0.84, 1.0],
      nebA: [0.18, 0.48, 0.92],
      nebB: [0.36, 0.86, 0.82],
      tagline: 'A dazzling blue-white giant lighting up turquoise nebulae.',
    },
    pulsar: {
      radius: 95,
      color: [0.55, 0.92, 1.0],
      nebA: [0.14, 0.68, 0.86],
      nebB: [0.58, 0.36, 0.92],
      tagline: 'A spinning lighthouse star with twin beams of glowing light!',
    },
    'black-hole': {
      radius: 145,
      color: [1.0, 0.74, 0.42],
      nebA: [0.64, 0.36, 0.78],
      nebB: [0.95, 0.56, 0.28],
      tagline: 'A cosmic whirlpool that bends starlight into a golden halo.',
    },
  };

  const cfg = starConfig[starKind];
  const allBiomes = Object.keys(BIOME_PALETTES) as BiomeKind[];
  const planetCount = starKind === 'black-hole' ? 2 : rng.int(3, 5);
  const planets: PlanetData[] = [];

  for (let i = 0; i < planetCount; i++) {
    const biome: BiomeKind =
      i === 0 && starKind === 'warm-sun'
        ? 'meadow-world'
        : i === 1 && rng.chance(0.55)
          ? 'cloud-giant'
          : rng.pick(allBiomes);

    const pal = BIOME_PALETTES[biome];
    const isGiant = biome === 'cloud-giant';
    const radius = isGiant ? rng.range(58, 86) : rng.range(22, 42);
    const orbitRadius = 460 + i * 320 + rng.range(-30, 50);
    const orbitAngle = (i * 1.45 + rng.range(0.1, 0.6)) % (Math.PI * 2);

    const hasRings = isGiant ? rng.chance(0.85) : rng.chance(0.22);
    const ringInner = radius * 1.38;
    const ringOuter = radius * (isGiant ? 2.45 : 1.95);

    planets.push({
      id: i,
      name: `${ref.name} ${['I', 'II', 'III', 'IV', 'V', 'VI'][i] ?? i + 1}`,
      biome,
      radius,
      orbitRadius,
      orbitAngle,
      position: {
        x: Math.cos(orbitAngle) * orbitRadius,
        y: rng.range(-35, 35),
        z: Math.sin(orbitAngle) * orbitRadius,
      },
      colorA: pal.a,
      colorB: pal.b,
      atmosphereColor: pal.atmo,
      hasRings,
      ringInner,
      ringOuter,
      ringTilt: rng.range(0.22, 0.52),
      ringColor: isGiant ? [0.92, 0.85, 0.72] : [0.76, 0.86, 0.95],
      landable: pal.landable,
      funFact: pal.fact,
    });
  }

  return {
    ref,
    seed,
    name: ref.name,
    starKind,
    starRadius: cfg.radius,
    starColor: cfg.color,
    nebulaPrimary: cfg.nebA,
    nebulaSecondary: cfg.nebB,
    planets,
    tagline: cfg.tagline,
  };
}

/** Backwards-compatible sector helper used by tests & quick previews */
export function generateStarSystem(
  galaxySeed: number,
  sectorX: number,
  sectorY: number,
  sectorZ: number,
  forcedStarKind?: StarKind,
): StarSystem {
  const seed = hashCoords(galaxySeed, sectorX, sectorY, sectorZ);
  const rng = createRng(seed);
  const ref: StarRef = {
    id: starId(sectorX, sectorY, sectorZ, 0),
    name: `${rng.pick(PREFIXES)}${rng.pick(SUFFIXES)}`,
    sectorX,
    sectorY,
    sectorZ,
    x: sectorX * SECTOR_SIZE_LY,
    y: sectorY * SECTOR_SIZE_LY,
    z: sectorZ * SECTOR_SIZE_LY,
    starKind: forcedStarKind ?? pickStarKind(rng),
  };
  return generateStarSystemFromRef(galaxySeed, ref);
}

export function getShowcaseSystems(galaxySeed = 202604): StarSystem[] {
  return [
    generateStarSystem(galaxySeed, 0, 0, 0, 'warm-sun'),
    generateStarSystem(galaxySeed, 3, 1, -2, 'sky-giant'),
    generateStarSystem(galaxySeed, -4, 2, 5, 'pulsar'),
    generateStarSystem(galaxySeed, 8, -3, 7, 'black-hole'),
    generateStarSystem(galaxySeed, -2, -5, -3, 'amber-dwarf'),
  ];
}
