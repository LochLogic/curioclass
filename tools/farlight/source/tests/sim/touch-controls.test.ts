import { describe, expect, it } from 'vitest';
import { computeStickAxes } from '../../src/ui/touch-controls.ts';

describe('Phone & Tablet Touch Controls Math', () => {
  it('returns zero axes inside the deadzone', () => {
    const res = computeStickAxes(2, -3, 46, 0.12);
    expect(res.forward).toBe(0);
    expect(res.strafe).toBe(0);
  });

  it('maps upward thumb drag to +1 forward and clamps beyond maxRadius', () => {
    const res = computeStickAxes(0, -90, 46, 0.12);
    expect(res.forward).toBeCloseTo(1, 4);
    expect(res.strafe).toBeCloseTo(0, 4);
    expect(res.knobY).toBeCloseTo(-46, 4);
  });

  it('normalizes diagonal thumb movement smoothly without exceeding unit magnitude', () => {
    const res = computeStickAxes(46, -46, 46, 0.12);
    expect(Math.hypot(res.strafe, res.forward)).toBeCloseTo(1, 4);
    expect(res.strafe).toBeGreaterThan(0.65);
    expect(res.forward).toBeGreaterThan(0.65);
  });
});
