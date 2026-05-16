# DJERMN Now Playing

Zeigt den aktuell in Rekordbox geladenen Track live auf einer öffentlichen Webseite.

**Display:** https://djermn.github.io/now-playing/

## Architektur

```
Rekordbox (spielt Song)
  → master.db DjmdSongHistory (~30s Delay, Pioneer-Design)
  → now_playing_daemon.py (pollt alle 2s)
  → Firebase Realtime Database (sofort, <1s)
  → Browser (Firebase WebSocket Push, kein Polling)
  → GitHub (git commit + push, für Backup-Archiv)
```

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `now_playing_daemon.py` | Haupt-Daemon |
| `de.djermn.now-playing.plist` | macOS LaunchAgent (Autostart) |

## Installation

### 1. Abhängigkeiten

```bash
pip3 install pyrekordbox
```

### 2. Daemon installieren

```bash
cp now_playing_daemon.py ~/Library/Application\ Support/djermn/
cp de.djermn.now-playing.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/de.djermn.now-playing.plist
```

### 3. Status prüfen

```bash
launchctl list | grep djermn
tail -f ~/Library/Logs/djermn-now-playing.log
```

### Daemon stoppen / starten

```bash
launchctl unload ~/Library/LaunchAgents/de.djermn.now-playing.plist
launchctl load   ~/Library/LaunchAgents/de.djermn.now-playing.plist
```

## Konfiguration (in now_playing_daemon.py)

| Variable | Wert | Beschreibung |
|----------|------|-------------|
| `REPO_PATH` | `~/Documents/DJERMN.github.io` | Lokales GitHub-Pages-Repo |
| `FIREBASE_URL` | Firebase REST URL | Realtime Database Endpunkt |
| `POLL_INTERVAL` | `2` | Sekunden zwischen DB-Abfragen |

## Bekannte Einschränkungen

- **~30–60s Delay** vom Songwechsel bis zur Anzeige — Rekordbox schreibt erst nach Mindest-Spielzeit in die History (Pioneer-Design, nicht änderbar ohne Pro DJ Link)
- **Artwork ~65–70% Trefferquote** — DJ-Edits oft nicht in iTunes
- Nur auf dem Mac mit laufendem Rekordbox nutzbar
