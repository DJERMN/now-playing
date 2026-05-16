#!/usr/bin/env python3
"""
DJERMN Now Playing Daemon
Reads current track from Rekordbox master.db, commits now-playing.json to GitHub.
Display: https://djermn.github.io/now-playing/
"""

import sys, io, logging, json, time, re, os, subprocess, urllib.request, urllib.parse, threading

logging.disable(logging.WARNING)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pyrekordbox.db6 import Rekordbox6Database

REPO_PATH  = '/Users/bariser/Documents/DJERMN.github.io'
JSON_FILE  = os.path.join(REPO_PATH, 'now-playing.json')
POLL_INTERVAL = 2


def get_current_track():
    try:
        db = Rekordbox6Database()
        histories = sorted(db.get_history(), key=lambda h: str(h.created_at), reverse=True)
        if not histories:
            return None
        latest = histories[0]
        songs = [s for s in db.get_history_songs() if s.HistoryID == latest.ID]
        if not songs:
            return None
        songs.sort(key=lambda s: s.TrackNo or 0, reverse=True)
        c = songs[0].Content
        if not c:
            return None
        return {
            'id': c.ID,
            'title': c.Title or '',
            'artist': c.Artist.Name if c.Artist else '',
            'bpm': round(c.BPM / 100, 1) if c.BPM else None,
            'key': c.Key.ScaleName if c.Key else None,
        }
    except Exception as e:
        print(f"  DB-Fehler: {e}")
        return None


def clean_title(t):
    t = re.sub(r'\s*[-–]\s*[^-–]*?(remix|edit|mix|version|instrumental|radio|extended|original|bootleg|flip|rework|vip|dub|mashup|medley|clean|dirty|intro|outro)[\s\S]*', '', t, flags=re.I)
    t = re.sub(r'\s*\([^)]*?(clean|dirty|intro|outro|radio|explicit|instrumental|remix|edit|mix|version|extended|original|live|acoustic)[^)]*\)', '', t, flags=re.I)
    return t.strip()


def clean_artist(a):
    return re.split(r'\s+(?:ft\.?|feat\.?|&|vs\.?)\s+', a, flags=re.I)[0].strip()


def get_artwork(title, artist):
    ct = clean_title(title)
    ca = clean_artist(artist)
    for q in list(dict.fromkeys([f"{ca} {ct}", f"{artist} {ct}", f"{ca} {title}"])):
        if not q.strip():
            continue
        url = 'https://itunes.apple.com/search?term=' + urllib.parse.quote(q) + '&media=music&limit=5'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=8) as r:
                d = json.loads(r.read())
            for res in d.get('results', []):
                art = res.get('artworkUrl100')
                if art:
                    return art.replace('100x100bb', '600x600bb')
        except Exception:
            pass
        time.sleep(0.5)
    return None


FIREBASE_BASE = 'https://now-playing-75593-default-rtdb.europe-west1.firebasedatabase.app'
_secret_path  = os.path.expanduser('~/Library/Application Support/djermn/firebase_secret.txt')
_secret       = open(_secret_path).read().strip() if os.path.exists(_secret_path) else ''
FIREBASE_URL  = f'{FIREBASE_BASE}/now-playing.json?auth={_secret}'


def push_to_firebase(data):
    req = urllib.request.Request(
        FIREBASE_URL,
        data=json.dumps(data, ensure_ascii=False).encode(),
        method='PUT',
        headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
    )
    urllib.request.urlopen(req, timeout=8)


def push_to_github(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    subprocess.run(['git', '-C', REPO_PATH, 'add', 'now-playing.json'],
                   check=True, capture_output=True)
    subprocess.run(['git', '-C', REPO_PATH, 'commit', '-m',
                    f"Now playing: {data.get('title', '')}"],
                   check=True, capture_output=True)
    subprocess.run(['git', '-C', REPO_PATH, 'push'],
                   check=True, capture_output=True)


def main():
    print("DJERMN Now Playing Daemon")
    print(f"Display:  https://djermn.github.io/now-playing/")
    print(f"Polling alle {POLL_INTERVAL}s — Strg+C zum Beenden\n")

    last_id = None

    def enrich_and_push(data):
        artwork = get_artwork(data['title'], data['artist'])
        print(f"  Artwork: {'OK' if artwork else 'nicht gefunden'}")
        data['artwork'] = artwork
        try:
            push_to_firebase(data)
            print(f"  Firebase: OK (mit Artwork)")
        except Exception as e:
            print(f"  Firebase-Fehler: {e}")
        try:
            push_to_github(data)
            print(f"  GitHub: OK\n")
        except Exception as e:
            print(f"  GitHub-Fehler: {e}\n")

    while True:
        track = get_current_track()

        if track and track['id'] != last_id:
            last_id = track['id']
            print(f"Jetzt: {track['title']} — {track['artist']}")

            data = {
                'title': track['title'],
                'artist': track['artist'],
                'bpm': track['bpm'],
                'key': track['key'],
                'artwork': None,
                'updated': time.strftime('%Y-%m-%dT%H:%M:%S'),
            }

            # Phase 1: sofort — Browser aktualisiert in <1s
            try:
                push_to_firebase(data)
                print(f"  Firebase: OK (sofort)")
            except Exception as e:
                print(f"  Firebase-Fehler: {e}")

            # Phase 2: Artwork + GitHub im Hintergrund
            threading.Thread(target=enrich_and_push, args=(data.copy(),), daemon=True).start()

        time.sleep(POLL_INTERVAL)


if __name__ == '__main__':
    main()
