import type { BiomeKind } from '../sim/galaxy.ts';
import { createRng, hashCoords } from '../sim/prng.ts';
import { sampleTerrainHeight } from '../sim/planet-flight.ts';
import type { ProceduralMesh } from './ship-gen.ts';

export interface SurfaceSpecies {
  floraName: string;
  floraFact: string;
  critterName: string;
  critterFact: string;
  flierName: string;
  flierFact: string;
}

export interface WorldInstanceSet {
  /** Each instance: pos(3), scale(1), rotY(1), kind(1), phase(1), tintMix(1) = 8 floats */
  treeData: Float32Array<ArrayBuffer>;
  treeCount: number;
  lanternData: Float32Array<ArrayBuffer>;
  lanternCount: number;
  spireData: Float32Array<ArrayBuffer>;
  spireCount: number;
  critterData: Float32Array<ArrayBuffer>;
  critterCount: number;
  flierData: Float32Array<ArrayBuffer>;
  flierCount: number;
  grassData: Float32Array<ArrayBuffer>;
  grassCount: number;
  fishData: Float32Array<ArrayBuffer>;
  fishCount: number;
  ruinData: Float32Array<ArrayBuffer>;
  ruinCount: number;
  cityData: Float32Array<ArrayBuffer>;
  cityCount: number;
  centerX: number;
  centerZ: number;
}

const FLORA_NAMES: Record<BiomeKind, [string, string]> = {
  'meadow-world': ['Sunburst Umbrella Tree', 'Its wide leaves catch morning dew and shade wandering critters.'],
  'coral-ocean': ['Tidebloom Palm', 'Sways with salty sea breezes and drops buoyant coconuts.'],
  'golden-dunes': ['Singing Cactus Spire', 'Hums a gentle musical note when desert wind blows past!'],
  'aurora-ice': ['Frost-Bell Pine', 'Its icy needles sparkle like tiny prisms under the aurora.'],
  'crystal-garden': ['Chime-Quartz Cluster', 'Resonates with warm glowing light whenever the sun sets.'],
  'cloud-giant': ['Sky-Wisp', 'Floating atmospheric droplets.'],
  'amber-canyons': ['Redwood Arch Bush', 'Roots grip sandstone cliffs to drink deep canyon mist.'],
  'volcanic-ember': ['Ember-Cap Fern', 'Thrives near warm basalt vents with glowing orange tips.'],
  'mist-forest': ['Lantern-Pod Tree', 'Hangs glowing lavender fruit that lights up the forest at night!'],
  'crater-moon': ['Moon-Glass Monolith', 'Ancient crystalline rock formed by tiny micrometeorites.'],
};

const CRITTER_NAMES: Record<BiomeKind, [string, string]> = {
  'meadow-world': ['Bouncy Meadow-Hopper', 'Loves leaping over daisies and chirping at visiting explorers!'],
  'coral-ocean': ['Pebble-Shell Crab', 'Collects shiny seashells and dances along the sandy shore.'],
  'golden-dunes': ['Sand-Glider Fox', 'Has huge fluffy ears that keep it cool under the desert sun.'],
  'aurora-ice': ['Snow-Puff Penguin', 'Slides belly-first down snowy slopes just for fun!'],
  'crystal-garden': ['Prism-Beetle', 'Its shimmering shell flashes rainbow colors as it hops along.'],
  'cloud-giant': ['Cloud-Manta', 'Glides effortlessly on high-altitude jet streams.'],
  'amber-canyons': ['Canyon-Strider', 'Long springy legs let it bound from boulder to boulder.'],
  'volcanic-ember': ['Magma-Snail', 'Carries a cozy heat-proof shell that glows like a campfire.'],
  'mist-forest': ['Glow-Moth Critter', 'Follows lantern trees and leaves tiny trails of sparkles!'],
  'crater-moon': ['Star-Tardigrade', 'A friendly space-bear that bounces joyfully in low gravity!'],
};

const FLIER_NAMES: Record<BiomeKind, [string, string]> = {
  'meadow-world': ['Sunwing Sky-Manta', 'Glides in peaceful circles over sunny meadows, flashing golden wingtips!'],
  'coral-ocean': ['Coral Kite-Ray', 'Skims the turquoise ocean spray and rides warm coastal updrafts.'],
  'golden-dunes': ['Dune-Swallow', 'Soars effortlessly high above singing sand dunes on wide amber wings.'],
  'aurora-ice': ['Aurora Owl-Glider', 'Its shimmering translucent wings reflect green northern lights!'],
  'crystal-garden': ['Prism Dragonfly', 'Flutters between quartz spires with chiming, crystalline wings.'],
  'cloud-giant': ['Jetstream Manta', 'Surfs swirling high-altitude cloud bands.'],
  'amber-canyons': ['Canyon Condor-Ray', 'Rides warm red-rock thermals high above the mesa arches.'],
  'volcanic-ember': ['Ember Phoenix-Moth', 'Glows like a floating lantern as it circles warm volcanic vents.'],
  'mist-forest': ['Moonlight Sky-Jellie', 'Drifts softly through misty tree canopies, trailing lavender sparkles!'],
  'crater-moon': ['Solar-Sail Sprite', 'A rare tiny space-glider that rides beams of pure sunlight!'],
};

export function getPlanetSpecies(biome: BiomeKind): SurfaceSpecies {
  const [floraName, floraFact] = FLORA_NAMES[biome];
  const [critterName, critterFact] = CRITTER_NAMES[biome];
  const [flierName, flierFact] = FLIER_NAMES[biome];
  return { floraName, floraFact, critterName, critterFact, flierName, flierFact };
}

class PropMeshBuilder {
  private verts: number[] = [];
  private idx: number[] = [];

  addPrism(
    cx: number, cy: number, cz: number,
    rxBot: number, rxTop: number, height: number,
    sides: number,
    color: [number, number, number],
    roughness: number,
    emissive = 0,
  ): void {
    const y0 = cy;
    const y1 = cy + height;
    for (let i = 0; i < sides; i++) {
      const a0 = (i / sides) * Math.PI * 2;
      const a1 = ((i + 1) / sides) * Math.PI * 2;
      const c0 = Math.cos(a0), s0 = Math.sin(a0);
      const c1 = Math.cos(a1), s1 = Math.sin(a1);
      const am = (a0 + a1) * 0.5;
      const nx = Math.cos(am), nz = Math.sin(am);
      const ny = rxBot > rxTop ? 0.32 : rxBot < rxTop ? -0.25 : 0;
      const nLen = Math.hypot(nx, ny, nz) || 1;

      const base = this.verts.length / 11;
      const pts: [number, number, number][] = [
        [cx + c0 * rxBot, y0, cz + s0 * rxBot],
        [cx + c1 * rxBot, y0, cz + s1 * rxBot],
        [cx + c1 * rxTop, y1, cz + s1 * rxTop],
        [cx + c0 * rxTop, y1, cz + s0 * rxTop],
      ];
      for (const p of pts) {
        this.verts.push(
          p[0], p[1], p[2],
          nx / nLen, ny / nLen, nz / nLen,
          color[0], color[1], color[2],
          roughness, emissive,
        );
      }
      this.idx.push(base, base + 1, base + 2, base, base + 2, base + 3);
    }

    // Top cap if rxTop > 0.01
    if (rxTop > 0.01) {
      const centerIdx = this.verts.length / 11;
      this.verts.push(cx, y1 + rxTop * 0.12, cz, 0, 1, 0, color[0], color[1], color[2], roughness, emissive);
      for (let i = 0; i < sides; i++) {
        const a = (i / sides) * Math.PI * 2;
        this.verts.push(
          cx + Math.cos(a) * rxTop, y1, cz + Math.sin(a) * rxTop,
          0, 1, 0,
          color[0], color[1], color[2],
          roughness, emissive,
        );
      }
      for (let i = 0; i < sides; i++) {
        this.idx.push(centerIdx, centerIdx + 1 + ((i + 1) % sides), centerIdx + 1 + i);
      }
    }
  }

  build(): ProceduralMesh {
    return {
      vertices: new Float32Array(this.verts),
      indices: new Uint16Array(this.idx),
    };
  }
}

export function buildTreeMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const trunk: [number, number, number] = [0.38, 0.25, 0.17];
  const leafA: [number, number, number] = [0.22, 0.72, 0.42];
  const leafB: [number, number, number] = [0.32, 0.84, 0.50];
  b.addPrism(0, 0, 0, 0.48, 0.26, 4.4, 6, trunk, 0.85, 0);
  b.addPrism(0, 3.6, 0, 2.5, 1.5, 1.6, 7, leafA, 0.72, 0);
  b.addPrism(0, 4.9, 0, 1.75, 0.35, 1.5, 7, leafB, 0.68, 0);
  return b.build();
}

export function buildLanternMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const stem: [number, number, number] = [0.24, 0.18, 0.28];
  const cap: [number, number, number] = [0.76, 0.32, 0.62];
  const pod: [number, number, number] = [0.72, 0.56, 1.0];
  b.addPrism(0, 0, 0, 0.38, 0.22, 4.0, 6, stem, 0.8, 0);
  b.addPrism(0, 3.7, 0, 2.1, 0.45, 1.2, 8, cap, 0.55, 0.15);
  // Glowing lantern fruit pods hanging beneath cap
  b.addPrism(1.15, 2.8, 0.3, 0.35, 0.25, 0.75, 6, pod, 0.2, 1.4);
  b.addPrism(-1.05, 2.6, -0.45, 0.32, 0.22, 0.7, 6, pod, 0.2, 1.4);
  b.addPrism(0.1, 2.7, -1.1, 0.34, 0.24, 0.72, 6, pod, 0.2, 1.4);
  return b.build();
}

export function buildSpireMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const main: [number, number, number] = [0.58, 0.82, 0.96];
  const side: [number, number, number] = [0.76, 0.55, 0.98];
  b.addPrism(0, 0, 0, 0.95, 0.06, 5.2, 5, main, 0.18, 0.55);
  b.addPrism(0.85, 0, 0.35, 0.55, 0.04, 3.1, 5, side, 0.2, 0.7);
  b.addPrism(-0.75, 0, -0.4, 0.48, 0.04, 2.5, 5, main, 0.2, 0.5);
  return b.build();
}

export function buildCritterMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const body: [number, number, number] = [0.98, 0.64, 0.38];
  const belly: [number, number, number] = [1.0, 0.92, 0.78];
  const accent: [number, number, number] = [0.35, 0.94, 0.96];
  // Cute rounded body + head + bouncy legs + glowing ears/crest
  b.addPrism(0, 0.55, 0, 0.72, 0.62, 0.92, 7, body, 0.6, 0);
  b.addPrism(0, 1.25, -0.48, 0.48, 0.36, 0.68, 7, belly, 0.55, 0);
  // Glowing cute ears / antennae
  b.addPrism(-0.26, 1.85, -0.52, 0.12, 0.06, 0.55, 5, accent, 0.2, 0.9);
  b.addPrism(0.26, 1.85, -0.52, 0.12, 0.06, 0.55, 5, accent, 0.2, 0.9);
  // 4 little legs
  b.addPrism(-0.38, 0, -0.32, 0.14, 0.12, 0.65, 5, body, 0.7, 0);
  b.addPrism(0.38, 0, -0.32, 0.14, 0.12, 0.65, 5, body, 0.7, 0);
  b.addPrism(-0.38, 0, 0.32, 0.14, 0.12, 0.65, 5, body, 0.7, 0);
  b.addPrism(0.38, 0, 0.32, 0.14, 0.12, 0.65, 5, body, 0.7, 0);
  return b.build();
}

/** Cozy 3D Research Camp: warm geodesic dome, glowing window band, beacon spire */
export function buildCampMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const baseCol: [number, number, number] = [0.88, 0.86, 0.82];
  const domeCol: [number, number, number] = [0.96, 0.56, 0.34];
  const windowGlow: [number, number, number] = [1.0, 0.86, 0.48];
  const beaconGlow: [number, number, number] = [0.38, 0.96, 1.0];
  const mast: [number, number, number] = [0.32, 0.38, 0.48];

  b.addPrism(0, 0, 0, 3.2, 3.0, 0.8, 8, baseCol, 0.55, 0);
  b.addPrism(0, 0.8, 0, 2.85, 2.75, 0.85, 8, windowGlow, 0.15, 0.95);
  b.addPrism(0, 1.65, 0, 2.75, 1.15, 1.55, 8, domeCol, 0.42, 0.08);
  // Tall glowing science beacon mast
  b.addPrism(2.3, 0, -1.2, 0.24, 0.12, 5.4, 6, mast, 0.45, 0);
  b.addPrism(2.3, 5.4, -1.2, 0.42, 0.18, 0.75, 6, beaconGlow, 0.1, 1.8);
  return b.build();
}

/** Graceful soaring Sky-Glider / Cloud-Manta (wings flap smoothly in world-props.wgsl!) */
export function buildFlierMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const bodyCol: [number, number, number] = [0.96, 0.94, 0.88];
  const wingCol: [number, number, number] = [0.34, 0.84, 0.96];
  const tipGlow: [number, number, number] = [1.0, 0.74, 0.36];

  // Sleek tapered body & tail
  b.addPrism(0, 0, -0.5, 0.36, 0.12, 0.55, 6, bodyCol, 0.42, 0.08);
  b.addPrism(0, 0.05, 0.65, 0.22, 0.06, 0.42, 5, wingCol, 0.4, 0.15);
  // Wide soaring wings (extended along +/- X so vertex shader flaps them smoothly!)
  b.addPrism(-1.35, 0.12, 0.0, 1.15, 0.95, 0.14, 5, wingCol, 0.35, 0.12);
  b.addPrism(1.35, 0.12, 0.0, 1.15, 0.95, 0.14, 5, wingCol, 0.35, 0.12);
  // Glowing golden wingtips
  b.addPrism(-2.45, 0.14, 0.15, 0.55, 0.15, 0.12, 5, tipGlow, 0.2, 0.85);
  b.addPrism(2.45, 0.14, 0.15, 0.55, 0.15, 0.12, 5, tipGlow, 0.2, 0.85);
  return b.build();
}

/** Lush wind-swaying grass tuft with a colorful wildflower blossom */
export function buildGrassMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const blade: [number, number, number] = [0.24, 0.76, 0.36];
  const flower: [number, number, number] = [1.0, 0.78, 0.42];
  b.addPrism(0, 0, 0, 0.32, 0.04, 1.35, 4, blade, 0.78, 0);
  b.addPrism(0.45, 0, 0.25, 0.28, 0.04, 1.05, 4, blade, 0.78, 0);
  b.addPrism(-0.4, 0, -0.2, 0.26, 0.04, 1.15, 4, blade, 0.78, 0);
  b.addPrism(0.15, 1.05, 0.1, 0.16, 0.22, 0.28, 5, flower, 0.45, 0.28);
  return b.build();
}

/** Swimming shallow-ocean ray / fish */
export function buildFishMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const body: [number, number, number] = [0.26, 0.86, 0.94];
  const fin: [number, number, number] = [1.0, 0.62, 0.38];
  b.addPrism(0, 0, 0, 0.45, 0.15, 0.32, 6, body, 0.25, 0.35);
  b.addPrism(-0.65, 0.05, 0.1, 0.42, 0.08, 0.12, 4, fin, 0.3, 0.4);
  b.addPrism(0.65, 0.05, 0.1, 0.42, 0.08, 0.12, 4, fin, 0.3, 0.4);
  return b.build();
}

/** Ancient Glowing Star-Arch Ruin (discoverable landmark on planets!) */
export function buildRuinMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const stone: [number, number, number] = [0.64, 0.62, 0.68];
  const rune: [number, number, number] = [0.42, 0.94, 1.0];
  const gold: [number, number, number] = [1.0, 0.82, 0.38];
  // Twin carved monolith pillars + bridge lintel + floating glowing star-crystal
  b.addPrism(-3.2, 0, 0, 1.2, 0.9, 8.2, 6, stone, 0.75, 0);
  b.addPrism(3.2, 0, 0, 1.2, 0.9, 8.2, 6, stone, 0.75, 0);
  b.addPrism(0, 7.6, 0, 4.4, 3.8, 1.35, 6, stone, 0.72, 0);
  b.addPrism(0, 4.2, 0, 0.75, 0.05, 1.6, 6, rune, 0.1, 1.75);
  b.addPrism(0, 2.6, 0, 0.05, 0.75, 1.6, 6, gold, 0.1, 1.55);
  return b.build();
}

/** Eco-Futuristic Coastal City Tower for Earth (Sol III) */
export function buildCityTowerMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const tower: [number, number, number] = [0.84, 0.88, 0.94];
  const winGlow: [number, number, number] = [1.0, 0.88, 0.56];
  const roof: [number, number, number] = [0.28, 0.76, 0.52];
  b.addPrism(0, 0, 0, 3.8, 3.2, 16.0, 8, tower, 0.35, 0);
  b.addPrism(0, 4.0, 0, 3.65, 3.55, 1.2, 8, winGlow, 0.15, 0.85);
  b.addPrism(0, 9.5, 0, 3.45, 3.35, 1.2, 8, winGlow, 0.15, 0.85);
  b.addPrism(0, 16.0, 0, 3.1, 1.2, 1.8, 8, roof, 0.55, 0.08);
  return b.build();
}

/** 6-Wheeled Bouncy Explorer Rover (rendered ahead of camera in Rover mode!) */
export function buildRoverMesh(): ProceduralMesh {
  const b = new PropMeshBuilder();
  const body: [number, number, number] = [0.98, 0.76, 0.30];
  const trim: [number, number, number] = [0.95, 0.94, 0.90];
  const tire: [number, number, number] = [0.18, 0.20, 0.26];
  const head: [number, number, number] = [0.88, 0.98, 1.0];
  // Cozy chassis + rollbar + headlights + 6 big chunky moon wheels
  b.addPrism(0, 0.55, 0, 1.15, 0.95, 0.72, 6, body, 0.38, 0);
  b.addPrism(0, 1.25, 0.15, 0.75, 0.55, 0.55, 6, trim, 0.28, 0.06);
  // Headlights
  b.addPrism(-0.55, 0.92, -0.95, 0.18, 0.16, 0.22, 6, head, 0.1, 1.8);
  b.addPrism(0.55, 0.92, -0.95, 0.18, 0.16, 0.22, 6, head, 0.1, 1.8);
  // 6 wheels
  for (const wz of [-0.85, 0.0, 0.85]) {
    b.addPrism(-1.05, 0.0, wz, 0.38, 0.38, 0.52, 8, tire, 0.85, 0);
    b.addPrism(1.05, 0.0, wz, 0.38, 0.38, 0.52, 8, tire, 0.85, 0);
  }
  return b.build();
}

/** Deterministically populates trees, grass, fish, ruins, Earth cities & critters around (cx, cz) */
export function spawnSurfaceInstances(
  centerX: number,
  centerZ: number,
  seed: number,
  biome: BiomeKind,
  seaLevel: number,
  isEarth = false,
): WorldInstanceSet {
  const cellSize = 36;
  const gridRadius = 8;
  const baseGx = Math.floor(centerX / cellSize);
  const baseGz = Math.floor(centerZ / cellSize);

  const trees: number[] = [];
  const lanterns: number[] = [];
  const spires: number[] = [];
  const critters: number[] = [];
  const fliers: number[] = [];
  const grass: number[] = [];
  const fish: number[] = [];
  const ruins: number[] = [];
  const cities: number[] = [];

  for (let gx = baseGx - gridRadius; gx <= baseGx + gridRadius; gx++) {
    for (let gz = baseGz - gridRadius; gz <= baseGz + gridRadius; gz++) {
      const h = hashCoords(seed, gx, 17, gz);
      const rng = createRng(h);

      const propsInCell = biome === 'crater-moon' ? 1 : 2;
      for (let k = 0; k < propsInCell; k++) {
        const px = (gx + rng.range(0.08, 0.92)) * cellSize;
        const pz = (gz + rng.range(0.08, 0.92)) * cellSize;
        const py = sampleTerrainHeight(px, pz, seed, biome);
        if (py < seaLevel + 1.8) continue;

        // Avoid steep cliff faces
        const slopeX = Math.abs(sampleTerrainHeight(px + 2, pz, seed, biome) - py);
        const slopeZ = Math.abs(sampleTerrainHeight(px, pz + 2, seed, biome) - py);
        if (slopeX > 2.2 || slopeZ > 2.2) continue;

        const rotY = rng.range(0, Math.PI * 2);
        const phase = rng.range(0, Math.PI * 2);
        const tintMix = rng.next();

        if (biome === 'crystal-garden' || biome === 'crater-moon' || biome === 'volcanic-ember') {
          if (rng.chance(0.75)) {
            spires.push(px, py - 0.3, pz, rng.range(0.9, 2.2), rotY, 2, phase, tintMix);
          } else {
            lanterns.push(px, py - 0.2, pz, rng.range(0.8, 1.5), rotY, 1, phase, tintMix);
          }
        } else if (biome === 'mist-forest') {
          if (rng.chance(0.62)) {
            lanterns.push(px, py - 0.2, pz, rng.range(1.0, 2.0), rotY, 1, phase, tintMix);
          } else {
            trees.push(px, py - 0.2, pz, rng.range(1.0, 2.1), rotY, 0, phase, tintMix);
          }
        } else if (biome === 'golden-dunes' || biome === 'amber-canyons') {
          if (rng.chance(0.45)) {
            spires.push(px, py - 0.3, pz, rng.range(0.7, 1.6), rotY, 2, phase, tintMix);
          } else if (rng.chance(0.35)) {
            trees.push(px, py - 0.2, pz, rng.range(0.8, 1.4), rotY, 0, phase, tintMix);
          }
        } else {
          // meadow-world, coral-ocean, aurora-ice
          if (rng.chance(0.76)) {
            trees.push(px, py - 0.2, pz, rng.range(0.95, 2.15), rotY, 0, phase, tintMix);
          } else if (rng.chance(0.6)) {
            lanterns.push(px, py - 0.2, pz, rng.range(0.75, 1.35), rotY, 1, phase, tintMix);
          } else {
            spires.push(px, py - 0.3, pz, rng.range(0.7, 1.4), rotY, 2, phase, tintMix);
          }
        }
      }

      // Friendly wandering critters
      if (rng.chance(0.24)) {
        const cx = (gx + rng.range(0.15, 0.85)) * cellSize;
        const cz = (gz + rng.range(0.15, 0.85)) * cellSize;
        const cy = sampleTerrainHeight(cx, cz, seed, biome);
        if (cy > seaLevel + 2.0) {
          critters.push(cx, cy, cz, rng.range(0.85, 1.45), rng.range(0, Math.PI * 2), 3, rng.range(0, 6.28), rng.next());
        }
      }

      // Soaring Sky-Glider flocks overhead!
      if (rng.chance(biome === 'crater-moon' ? 0.05 : 0.18)) {
        const fx = (gx + rng.range(0.1, 0.9)) * cellSize;
        const fz = (gz + rng.range(0.1, 0.9)) * cellSize;
        const ground = Math.max(seaLevel, sampleTerrainHeight(fx, fz, seed, biome));
        const fy = ground + rng.range(24, 78);
        fliers.push(fx, fy, fz, rng.range(0.95, 1.85), rng.range(0, Math.PI * 2), 5, rng.range(0, 6.28), rng.next());
      }

      // Lush instanced grass & wildflowers near the player (inner 9x9 cells)
      if (
        Math.abs(gx - baseGx) <= 4 &&
        Math.abs(gz - baseGz) <= 4 &&
        (biome === 'meadow-world' || biome === 'coral-ocean' || biome === 'mist-forest')
      ) {
        for (let g = 0; g < 6; g++) {
          const ux = (gx + rng.range(0.05, 0.95)) * cellSize;
          const uz = (gz + rng.range(0.05, 0.95)) * cellSize;
          const uy = sampleTerrainHeight(ux, uz, seed, biome);
          if (uy > seaLevel + 2.2 && uy < 42) {
            grass.push(ux, uy - 0.1, uz, rng.range(0.7, 1.4), rng.range(0, 6.28), 7, rng.range(0, 6.28), rng.next());
          }
        }
      }

      // Swimming shallow-ocean fish / rays in clear turquoise coves!
      if (seaLevel > -500 && biome !== 'volcanic-ember' && rng.chance(0.32)) {
        const sx = (gx + rng.range(0.15, 0.85)) * cellSize;
        const sz = (gz + rng.range(0.15, 0.85)) * cellSize;
        const bed = sampleTerrainHeight(sx, sz, seed, biome);
        if (bed < seaLevel - 1.5 && bed > seaLevel - 18) {
          fish.push(sx, seaLevel - 1.0, sz, rng.range(1.1, 2.0), rng.range(0, 6.28), 6, rng.range(0, 6.28), rng.next());
        }
      }

      // Rare Ancient Glowing Star-Arch Ruins (~1-2 visible per region)
      if (rng.chance(0.03)) {
        const rx = (gx + 0.5) * cellSize;
        const rz = (gz + 0.5) * cellSize;
        const ry = sampleTerrainHeight(rx, rz, seed, biome);
        if (ry > seaLevel + 3.0) {
          ruins.push(rx, ry - 0.25, rz, rng.range(1.0, 1.45), rng.range(0, 6.28), 4, 0, rng.next());
        }
      }

      // Sparkling Procedural Coastal Cities when exploring Earth (Sol III)!
      if (isEarth && rng.chance(0.14)) {
        const bx = (gx + rng.range(0.2, 0.8)) * cellSize;
        const bz = (gz + rng.range(0.2, 0.8)) * cellSize;
        const by = sampleTerrainHeight(bx, bz, seed, biome);
        if (by > seaLevel + 2.5 && by < 24) {
          cities.push(bx, by - 0.4, bz, rng.range(0.8, 1.9), rng.range(0, 6.28), 4, 0, rng.next());
        }
      }
    }
  }

  return {
    treeData: new Float32Array(trees),
    treeCount: trees.length / 8,
    lanternData: new Float32Array(lanterns),
    lanternCount: lanterns.length / 8,
    spireData: new Float32Array(spires),
    spireCount: spires.length / 8,
    critterData: new Float32Array(critters),
    critterCount: critters.length / 8,
    flierData: new Float32Array(fliers),
    flierCount: fliers.length / 8,
    grassData: new Float32Array(grass),
    grassCount: grass.length / 8,
    fishData: new Float32Array(fish),
    fishCount: fish.length / 8,
    ruinData: new Float32Array(ruins),
    ruinCount: ruins.length / 8,
    cityData: new Float32Array(cities),
    cityCount: cities.length / 8,
    centerX: baseGx * cellSize,
    centerZ: baseGz * cellSize,
  };
}
