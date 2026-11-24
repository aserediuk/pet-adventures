#!/usr/bin/env python3
"""Check that Theme 2 still plays exactly the notes in tests/golden/theme2-events.json.

Runs the game's #view=events dump with ?theme=theme2 in headless Chrome and compares every song's
scheduled note events (2 full loops each), the encounter sting and the five theme notes.

Usage: python3 tools/check_golden.py
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
url = 'file://' + os.path.join(ROOT, 'pet-adventures.html') + '?theme=theme2#view=events'
out = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'cdp_probe.py'), url, '3'], capture_output=True, text=True).stdout.strip()
if not out.startswith('EVENTS '):
    sys.exit('could not read the event dump: ' + out[:200])
now = json.loads(out[7:])
gold = json.load(open(os.path.join(ROOT, 'tests', 'golden', 'theme2-events.json')))
bad = []
for key in ('sting', 'theme'):
    if now.get(key) != gold.get(key):
        bad.append(key)
for name, song in gold['songs'].items():
    got = now['songs'].get(name)
    if got is None:
        bad.append(name + ' (missing)')
    elif got != song:
        diff = next((i for i, (a, b) in enumerate(zip(got['events'], song['events'])) if a != b), None)
        bad.append('%s (first different event: %s)' % (name, diff))
extra = [n for n in now['songs'] if n not in gold['songs']]
if extra:
    bad.append('unexpected songs: ' + ', '.join(extra))
total = sum(len(s['events']) for s in gold['songs'].values())
if bad:
    sys.exit('GOLDEN FAIL: ' + '; '.join(bad))
print('GOLDEN PASS: Theme 2 matches all %d songs, %d note events' % (len(gold['songs']), total))
