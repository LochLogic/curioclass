r"""A small QR code encoder for the Sub Day cover (docs/SUPPLY-CLOSET-PLAN.md, Phase B).

    python scripts/qr.py https://curioclass.org/tools/fraction-trail/     print the SVG

Byte mode, error correction level M, versions 1 to 9 (up to 180 bytes, plenty for a tool URL; version 10 and up need a 16-bit length). build_site.py calls
svg() at build time, so the code is inline in the page and nothing loads when it is viewed. The steps follow the QR
standard (ISO/IEC 18004): encode, Reed-Solomon, interleave, place, mask, add format and version bits.
"""
import sys

ECC_PER_BLOCK = [0, 10, 16, 26, 18, 24, 16, 18, 22, 22, 26]  # level M, by version
BLOCKS = [0, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5]
MASKS = [
    lambda x, y: (x + y) % 2 == 0,
    lambda x, y: y % 2 == 0,
    lambda x, y: x % 3 == 0,
    lambda x, y: (x + y) % 3 == 0,
    lambda x, y: (x // 3 + y // 2) % 2 == 0,
    lambda x, y: x * y % 2 + x * y % 3 == 0,
    lambda x, y: (x * y % 2 + x * y % 3) % 2 == 0,
    lambda x, y: ((x + y) % 2 + x * y % 3) % 2 == 0,
]


def raw_modules(ver):
    """Modules left for data and error correction after the function patterns."""
    n = (16 * ver + 128) * ver + 64
    if ver >= 2:
        k = ver // 7 + 2
        n -= (25 * k - 10) * k - 55
        if ver >= 7:
            n -= 36
    return n


def data_codewords(ver):
    return raw_modules(ver) // 8 - ECC_PER_BLOCK[ver] * BLOCKS[ver]


def align_positions(ver):
    if ver == 1:
        return []
    k = ver // 7 + 2
    step = (ver * 4 + k * 2 + 1) // (2 * k - 2) * 2
    size = ver * 4 + 17
    return [6] + sorted(size - 7 - i * step for i in range(k - 1))


def gf_mul(x, y):
    z = 0
    for i in reversed(range(8)):
        z = (z << 1) ^ ((z >> 7) * 0x11D)
        z ^= ((y >> i) & 1) * x
    return z


def rs_divisor(degree):
    out = [0] * (degree - 1) + [1]
    root = 1
    for _ in range(degree):
        for j in range(degree):
            out[j] = gf_mul(out[j], root)
            if j + 1 < degree:
                out[j] ^= out[j + 1]
        root = gf_mul(root, 2)
    return out


def rs_remainder(data, divisor):
    out = [0] * len(divisor)
    for b in data:
        factor = b ^ out.pop(0)
        out.append(0)
        for i, c in enumerate(divisor):
            out[i] ^= gf_mul(c, factor)
    return out


def codewords(text):
    """(version, the final interleaved codewords) for the text."""
    data = text.encode('utf-8')
    for ver in range(1, 10):
        if 4 + 8 + len(data) * 8 <= data_codewords(ver) * 8:
            break
    else:
        raise ValueError(f'{len(data)} bytes is too long for a version 9 QR code')
    cap = data_codewords(ver) * 8
    bits = [0, 1, 0, 0] + [(len(data) >> i) & 1 for i in reversed(range(8))]
    for b in data:
        bits += [(b >> i) & 1 for i in reversed(range(8))]
    bits += [0] * min(4, cap - len(bits))
    bits += [0] * (-len(bits) % 8)
    words = [int(''.join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]
    pad = 0xEC
    while len(words) < cap // 8:
        words.append(pad)
        pad ^= 0xEC ^ 0x11
    nblocks, ecc = BLOCKS[ver], ECC_PER_BLOCK[ver]
    raw = raw_modules(ver) // 8
    nshort, short_len = nblocks - raw % nblocks, raw // nblocks
    div = rs_divisor(ecc)
    blocks, k = [], 0
    for i in range(nblocks):
        dat = words[k:k + short_len - ecc + (0 if i < nshort else 1)]
        k += len(dat)
        rem = rs_remainder(dat, div)
        if i < nshort:
            dat = dat + [0]  # a placeholder so the blocks line up; skipped below
        blocks.append(dat + rem)
    out = []
    for i in range(len(blocks[0])):
        for j, blk in enumerate(blocks):
            if i != short_len - ecc or j >= nshort:
                out.append(blk[i])
    return ver, out


class Grid:
    def __init__(self, ver):
        self.ver, self.size = ver, ver * 4 + 17
        self.dark = [[False] * self.size for _ in range(self.size)]
        self.func = [[False] * self.size for _ in range(self.size)]

    def put(self, x, y, dark):
        self.dark[y][x] = dark
        self.func[y][x] = True

    def functions(self):
        n = self.size
        for i in range(n):
            self.put(6, i, i % 2 == 0)
            self.put(i, 6, i % 2 == 0)
        for cx, cy in ((3, 3), (n - 4, 3), (3, n - 4)):
            for dy in range(-4, 5):
                for dx in range(-4, 5):
                    x, y = cx + dx, cy + dy
                    if 0 <= x < n and 0 <= y < n:
                        self.put(x, y, max(abs(dx), abs(dy)) not in (2, 4))
        pos = align_positions(self.ver)
        last = len(pos) - 1
        for i, ay in enumerate(pos):
            for j, ax in enumerate(pos):
                if (i, j) in ((0, 0), (0, last), (last, 0)):
                    continue
                for dy in range(-2, 3):
                    for dx in range(-2, 3):
                        self.put(ax + dx, ay + dy, max(abs(dx), abs(dy)) != 1)
        self.format_bits(0)
        if self.ver >= 7:
            rem = self.ver
            for _ in range(12):
                rem = (rem << 1) ^ ((rem >> 11) * 0x1F25)
            bits = self.ver << 12 | rem
            for i in range(18):
                b = (bits >> i) & 1 == 1
                a, c = n - 11 + i % 3, i // 3
                self.put(a, c, b)
                self.put(c, a, b)

    def format_bits(self, mask):
        data = (0 << 3) | mask  # level M's format bits are 00
        rem = data
        for _ in range(10):
            rem = (rem << 1) ^ ((rem >> 9) * 0x537)
        bits = (data << 10 | rem) ^ 0x5412
        bit = lambda i: (bits >> i) & 1 == 1
        n = self.size
        for i in range(6):
            self.put(8, i, bit(i))
        self.put(8, 7, bit(6))
        self.put(8, 8, bit(7))
        self.put(7, 8, bit(8))
        for i in range(9, 15):
            self.put(14 - i, 8, bit(i))
        for i in range(8):
            self.put(n - 1 - i, 8, bit(i))
        for i in range(8, 15):
            self.put(8, n - 15 + i, bit(i))
        self.put(8, n - 8, True)

    def place(self, words):
        n, i, right = self.size, 0, self.size - 1
        while right >= 1:
            if right == 6:
                right = 5
            for vert in range(n):
                for j in range(2):
                    x = right - j
                    y = n - 1 - vert if ((right + 1) & 2) == 0 else vert
                    if not self.func[y][x] and i < len(words) * 8:
                        self.dark[y][x] = (words[i >> 3] >> (7 - (i & 7))) & 1 == 1
                        i += 1
            right -= 2

    def apply_mask(self, mask):
        f = MASKS[mask]
        for y in range(self.size):
            for x in range(self.size):
                if not self.func[y][x] and f(x, y):
                    self.dark[y][x] = not self.dark[y][x]

    def penalty(self):
        n, g, score = self.size, self.dark, 0
        lines = [row for row in g] + [[g[y][x] for y in range(n)] for x in range(n)]
        finder = [True, False, True, True, True, False, True]
        for line in lines:
            run, prev = 0, None
            for v in line:
                run = run + 1 if v == prev else 1
                prev = v
                if run == 5:
                    score += 3
                elif run > 5:
                    score += 1
            padded = [False] * 4 + line + [False] * 4
            for i in range(len(padded) - 6):
                if padded[i:i + 7] == finder and (not any(padded[max(0, i - 4):i]) or not any(padded[i + 7:i + 11])):
                    score += 40
        for y in range(n - 1):
            for x in range(n - 1):
                if g[y][x] == g[y][x + 1] == g[y + 1][x] == g[y + 1][x + 1]:
                    score += 3
        dark = sum(map(sum, g))
        total = n * n
        score += ((abs(dark * 20 - total * 10) + total - 1) // total - 1) * 10
        return score


def matrix(text):
    """The QR code as rows of booleans (True is dark), without the quiet zone."""
    ver, words = codewords(text)
    best = None
    for mask in range(8):
        g = Grid(ver)
        g.functions()
        g.place(words)
        g.apply_mask(mask)
        g.format_bits(mask)
        p = g.penalty()
        if best is None or p < best[0]:
            best = (p, g)
    return best[1].dark


def svg(text, label=None):
    """An inline SVG with a 4-module quiet zone; size it with CSS."""
    m = matrix(text)
    n = len(m) + 8
    d = ''.join(f'M{x + 4} {y + 4}h1v1h-1z' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    title = f'<title>{label}</title>' if label else ''
    return (f'<svg class="qr" viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" role="img" shape-rendering="crispEdges">'
            f'{title}<rect width="{n}" height="{n}" fill="#fff"/><path d="{d}" fill="#000"/></svg>')


if __name__ == '__main__':
    print(svg(sys.argv[1] if len(sys.argv) > 1 else 'https://curioclass.org/'))
