"""A small WebSocket client for Chrome's DevTools port, standard library only.

drive.py and audit_tool.py use the `websockets` package when it is installed and fall back to this when it is not
(a sandboxed Python, such as the Codex builder's, may not see the user's site-packages). It covers only what those
scripts use: `await connect(url)` or `async with connect(url) as ws`, `await ws.send(text)`, `async for msg in ws`,
`await ws.recv()` and `await ws.close()`. Client frames are masked; ping, close and continuation frames are handled.
"""
import asyncio, base64, os, struct, urllib.parse


class Connection:
    def __init__(self, reader, writer):
        self.r, self.w = reader, writer

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return await self.recv()
        except (asyncio.IncompleteReadError, ConnectionError):
            raise StopAsyncIteration

    async def recv(self):
        parts = []
        while True:
            a, b = await self.r.readexactly(2)
            op, n = a & 15, b & 127
            if n == 126:
                n = struct.unpack('!H', await self.r.readexactly(2))[0]
            elif n == 127:
                n = struct.unpack('!Q', await self.r.readexactly(8))[0]
            mask = await self.r.readexactly(4) if b & 128 else None
            data = await self.r.readexactly(n)
            if mask:
                data = bytes(v ^ mask[i % 4] for i, v in enumerate(data))
            if op == 8:
                raise asyncio.IncompleteReadError(b'', None)
            if op == 9:
                await self._frame(data, 10); continue
            if op in (0, 1, 2):
                parts.append(data)
                if a & 128:
                    return b''.join(parts).decode()

    async def _frame(self, data, op=1):
        m, n = os.urandom(4), len(data)
        head = bytes([128 | op]) + (bytes([128 | n]) if n < 126 else bytes([128 | 126]) + struct.pack('!H', n) if n < 65536
                                    else bytes([128 | 127]) + struct.pack('!Q', n))
        self.w.write(head + m + bytes(v ^ m[i % 4] for i, v in enumerate(data)))
        await self.w.drain()

    async def send(self, text):
        await self._frame(text.encode())

    async def close(self):
        self.w.close()
        try:
            await self.w.wait_closed()
        except Exception:
            pass


class connect:
    def __init__(self, url, **kwargs):  # kwargs (max_size and the like) are accepted and ignored
        self.url, self.c = url, None

    async def _open(self):
        u = urllib.parse.urlparse(self.url)
        r, w = await asyncio.open_connection(u.hostname, u.port or 80, limit=2**28)
        key = base64.b64encode(os.urandom(16)).decode()
        path = u.path + ('?' + u.query if u.query else '')
        w.write(f'GET {path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n'
                f'Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n'.encode())
        await w.drain()
        head = await r.readuntil(b'\r\n\r\n')
        if b' 101 ' not in head.split(b'\r\n')[0] + b' ':
            raise ConnectionError(head[:200])
        self.c = Connection(r, w)
        return self.c

    def __await__(self):
        return self._open().__await__()

    async def __aenter__(self):
        return await self._open()

    async def __aexit__(self, *exc):
        await self.c.close()
