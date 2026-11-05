-- Curio Class messages (home page banner, 2026-11-05). No IP address, no device details.
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TEXT NOT NULL,
  kind TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT '',
  message TEXT NOT NULL,
  email TEXT NOT NULL DEFAULT '',
  page TEXT NOT NULL DEFAULT '',
  read INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS messages_read ON messages (read, created);
