/**
 * Deterministic PRNG and coordinate hashing for the procedural galaxy.
 * Same seed + coordinates always generate the exact same star system.
 */

export function hash32(x: number): number {
  let h = x | 0;
  h = Math.imul(h ^ (h >>> 16), 0x85ebca6b);
  h = Math.imul(h ^ (h >>> 13), 0xc2b2ae35);
  return (h ^ (h >>> 16)) >>> 0;
}

export function hashCoords(seed: number, x: number, y: number, z: number): number {
  let h = hash32(seed ^ 0x9e3779b9);
  h = hash32(h ^ Math.imul(x | 0, 374761393));
  h = hash32(h ^ Math.imul(y | 0, 668265263));
  h = hash32(h ^ Math.imul(z | 0, 2147483647));
  return h >>> 0;
}

export interface Rng {
  next(): number;
  range(min: number, max: number): number;
  int(min: number, maxInclusive: number): number;
  pick<T>(items: readonly T[]): T;
  chance(probability: number): boolean;
}

export function createRng(seed: number): Rng {
  let a = seed >>> 0;
  const next = (): number => {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  return {
    next,
    range: (min, max) => min + next() * (max - min),
    int: (min, maxInclusive) => min + Math.floor(next() * (maxInclusive - min + 1)),
    pick: <T>(items: readonly T[]): T => {
      const idx = Math.floor(next() * items.length);
      return items[idx] as T;
    },
    chance: (p) => next() < p,
  };
}
