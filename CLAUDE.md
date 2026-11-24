# Pet Adventures

A top-down, turn-based pet-collecting RPG for kids. The whole game is **one self-contained file**, `pet-adventures.html` (about 5,700 lines of HTML, CSS and vanilla JS). It runs by double-clicking it in Chrome or Safari on a Mac, or from a web address on iPad or iPhone. `README.md` is the player-facing guide; keep it in step with features.

## Hard rules

- **One file, nothing external.** No libraries, images, fonts, audio files or network requests. Art is string-array sprites, text is a built-in pixel font, and sound is synthesized with Web Audio.
- **Original content only.** Don't use names, terms, moves, sprites or catching devices from existing commercial creature-collecting games. Wild pets are befriended with **treats**. Beaten pets are "tired out", never "fainted" or "died". Watch for accidental borrowings: an early "Nurse Joy-Bell" and the trainer classes "Camper" and "Ranger" were renamed for this reason.
- **Kid-friendly.** Short, friendly, encouraging text. Dr. Gizmo is a cartoon villain who turns good, and nothing is scary or violent.
- **No soft-locks.** Every screen must always have a valid input. The player can never end up inside a wall. Running away always works, in trainer battles too, and the trainer then stays unbeaten. If every pet is tired out, the player wakes at the Clinic, healed, minus 25% of coins. The forced "who's next?" pet picker starts on a healthy pet. Treats can't be given to a trainer's pets, and that refusal doesn't use up the turn.
- **Text must fit at 432×240.** Measure with `textW()`; the self-test checks every string, including `{name}` (the player's name) filled in at its 10-character maximum.

## Display, input and devices

- **Canvas:** the internal resolution is 432×240, with 16 px tiles.
  - **Desktop:** scales by the largest whole number that fits the window.
  - **Touch (`touchUI`):** fits the screen with a fractional scale, leaving room for the controls (whole-number scale when there's room, as on iPad).
  - The **hint bar** is the bottom 10 px (`HINT_Y = 230`), and dialog boxes sit above it.
- **Pixel font:** `FONT` uses 5×7 glyphs on a 6 px advance, 8 px tall, with descenders. Any new character used in text needs a glyph. `wrapText()` wraps by pixel width.
- **Keys (`KeyboardEvent.code`):**

  | Keys | Action |
  | --- | --- |
  | WASD / arrows | Move, menus |
  | Enter / Space / E | ok |
  | Esc / Q | back / menu |
  | M | Mute all |
  | N | Music on/off |
  | F | Fullscreen |
  | V | Emote |
  | H | Go home (asks first) |

  - Keys are ignored while Cmd, Ctrl or Alt is held.
  - Space also pushes a `'space'` token, which the intro uses to skip.
  - `NameEntryScreen` grabs all key presses while it's open, so letters type text.
- **Touch (section 9b):**
  - On-screen D-pad, A/B buttons and small Emote, Home, Music, Sound and Full buttons. These are DOM elements using Pointer Events.
  - Screens may define `tap(x, y)` in game coordinates, or `tapOk = true`.
  - `touchHint()` rewrites hint text into D-pad/A/B wording.
  - iOS specifics: audio unlocks on `touchend`/`pointerup`; zoom and scroll are blocked with `touch-action:none` plus `preventDefault`; the Fullscreen API exists on iPad only, so iPhone uses Add to Home Screen; safe areas are read through `#safe`.

## Code map (numbered sections in the file)

1. Constants and display (`fitCanvas`, fullscreen). 2. Pixel font. 3. Sprites:
   - Tiles, chests, people (palette-swapped).
   - The 12 original pets, drawn as hand-made mirrored half-sprites with tail overlays.
   - The 20 newer pets, made by the shape painter (`ANIMALS`, `NEW_PETS`, `paintPet`).
   - Accessories (`ACC_*`).
4. Audio: 8-bit SFX (`tone`, `noise`, `SFX`), then the music system (see below). 5. Game data: `TYPES`, `BEATS`, `MOVES`, `LEARNSETS`, `SPECIES`, `ITEMS`, treats. 6. Pet rules, as pure functions (`petStats`, `calcDamage`, `gainXP`, `catchChance`, `treatChance`). 7. World data (`MAPS`). 7b. Story (`STORY`, `goalText`). 8. Save and load. 9. Input. 9b. Touch. 10. Screen stack, timers, `runScript`, fade. 11. UI helpers. 12. Message and choice screens. 13. Overworld (`talkTo`, `STORY_SCRIPTS`, tips, chests, doors). 14. Pause menu, pets, bag, summary. 15. Clinic, Pet Pen, shop. 16+. Title, intro, starter, win, battle, evolution, main loop, self-test, developer previews, boot.

**How the flow works:**
- **Screen stack:** a stack of screen objects, each with `update(inp)`, `draw()` and `hint()`. Opaque screens hide whatever is below them.
- **Async scripts:** game flow is written as async scripts (`runScript`) that `await say()`, `await choose()`, `await startBattle()`, and so on.
- **`busy` flag:** blocks overworld input while a script runs.
- **Error recovery:** an unexpected error falls back to the overworld (`recoverFromError`).
- **Save data:** the game state `G` is the save file, kept in `localStorage` (`petAdventures.save.v1`, wrapped in try/catch). `loadGame()` cleans it up and migrates old fields.

## Data formats

- **Maps:** `rows` of tile characters, which must be rectangular and at most 48×32. Tile legend:

  | Characters | Meaning |
  | --- | --- |
  | `. , = f b D ~ T R B K H W` | town and grass tiles |
  | `L P M X Z C` | lab |
  | `_ ; c r` | desert |
  | `w m \|` | farm |
  | `J j` | jungle |
  | `* ^ Y q` | snow |

  - Grass tiles (`, ; w m j ^`) trigger encounters.
  - Encounter tables: `wild`, then `pond` (used when a water tile `~` is next to the grass tile), then `byTile` (per tile character).
  - Other fields: `exits` (rectangle → `to`, `tx`/`ty`; wider exits keep your sideways position), `doors`, `labels`, `npcs`, `chests`.
- **NPCs:**
  - Every NPC: `id`, `look` (a key in `LOOKS`), `name`, `x`, `y`, `dir` and `lines`, plus optional `after` (after being beaten) and `final` (after Dr. Gizmo is beaten).
  - Trainers: `trainer.team`, plus optional `moveTo` (steps aside when beaten, used for gatekeepers), `onWin` (a `STORY_SCRIPTS` key, such as `ribbon`, `champion` or `gizmo`), `ribbon`, `needsRibbons` and `music`.
  - Non-trainers say their lines the first time, then always give a tip (`progressTip`, `BATTLE_TIPS`).
- **Pets:** `SPECIES[id] = { name, type, fam, base: {hp, atk, def, spd}, evo, evoLv }`. Adult forms have about 1.3× the baby's stats. Learnsets give 6 moves at Lv 1, 1, 7, 9 (a move against the pet's weakness), 13 and 17. A pet object is `{ sp, lv, xp, hp, moves, pending, nick?, acc? }`.
- **Treats:** `TREAT_LIKES[type]` lists the treats each type likes (real-life diets). A wrong treat is usually refused (`WRONG_TREAT_REFUSE`).

## Tasks (section 7c)

`QUESTS` lists 12 tasks, one per helpful character (`giver`). Kinds: `item` (a sparkle on `map` at `x,y`), `pet` (a lost pet sprite there) and `show` (have one of `show` in the party or Pet Pen). State lives in `G.quests[id]`: `new` → `active` → (`found`) → `done`. Lost items and pets only exist on the map while the task is active (`questObjAt` blocks the tile and `interact` picks them up). Givers show a yellow ? (task offered) or green ! (ready to hand in). The self-test checks every object tile is open and reachable and never blocks a path.

## Game design numbers

- **Types:** 16 types in loops.

  | Loop | Order |
  | --- | --- |
  | Original | Dog > Cat > Hamster > Gerbil > Dog |
  | Second | Cat > Parrot > Lizard > Cat (Cat also beats Mouse) |
  | Land | Ferret > Mouse > Pony > Pig > Hedgehog > Ferret |
  | Water | Duck > Frog > Fish > Turtle > Rabbit > Duck |

  Damage is ×1.5 forward and ×0.67 backward. Normal moves are always ×1.
- **Stats:**
  - HP = ⌊base·L/20⌋ + L + 10. Other stats = ⌊base·L/25⌋ + 5. The level cap is 20.
  - XP to the next level = 10·L².
- **Rewards:** XP per win = (5·L² + 10) × 1.5 (trainers only) × `XP_BONUS` 1.25. Benched pets get half.
- **Damage:** ⌊((2L/5+2)·Pow·Atk/Def)/50 + 2⌋ × type multiplier × random 0.85–1. Enemies hit at `ENEMY_DAMAGE` (0.85).
- **Catching:**
  - Catch chance = clamp(0.25 + 0.6·(1 − hp/max), 0.05, 0.95).
  - A favorite treat multiplies it by 1.2. A wrong treat multiplies it by 0.3, after a 75% chance of refusal.
- **Main road:** Pawsville → Meadow Path → Pebble Canyon (gatekeeper Rex) → Whisker Woods → Misty Marsh (Fen) → Frosty Peak (Bo, then Champion Maple at the summit) → Gizmo's Lab (Bolt, then Dr. Gizmo, then the win screen).
- **Side areas:** Sunny Farm, Splash Lake, Sunny Dunes and Parrot Jungle each have a ribbon guardian. Maple needs all 4 **Trail Ribbons**.
- **Starters:** a puppy (Buddy) or a kitten (Mittens) only.
- **Difficulty curve:** a self-test simulates a typical team at the level a player usually has for each big fight. Win rates must stay between **45% and 92%**. Retune trainer levels, not the formulas, if it fails.

## Music (section 4)

- **Sound styles (`STYLES`, default `mix`):** 8-bit (pulse lead and arps, triangle bass, noise drums), **Mix** (8-bit pulse lead and tapping arps plus snappy noise drums, with an FM bass, a sine kick and a light echo, no pad) and 16-bit (all FM, gated drums, pad, full echo). The user found pure 16-bit lost the punch and fun of 8-bit, so Mix is the default. Players switch styles with Left/Right in the Jukebox; the choice is saved in `localStorage` (`petAdventures.settings.v1`). The compressor is set gently (ratio 3, 8 ms attack) so attacks punch through.

- **The 16-bit voices.** Songs are data in `SONGS`; in 16-bit style the voices map as follows:

  | Data voice | Sound |
  | --- | --- |
  | `p1` | FM LEAD |
  | `p2` | FM ARP (bell; ratio 3.5 or 7, or 2 if `duty: 0.5`) |
  | `tri` | FM BASS |
  | `noise` | gated kick/snare/hat, plus `g` (ghost) and `r` (rimshot) |
  | `pad` | detuned saws; only allowed in Title, Pawsville, Clinic/Shop and Win (`PAD_SONGS`) |

  Sound effects stay 8-bit.
- **Audio chain:**
  - Music: voices → 11 kHz lowpass → compressor → `musicBus` (0.18, N toggles it) → `duck` (dips under each SFX) → `master` (M mutes) → speakers.
  - Echo: one 1/8-note feedback echo, only on Title, Whisker Woods and Clinic/Shop (`SONGS.x.echo`).
- **Step strings:** each layer is `L(voice, steps, loopLength, opts)`.

  | Token | Meaning |
  | --- | --- |
  | `C4` | a note |
  | `.` | rest |
  | `-` suffix | hold |
  | `+` | quarter-tone sharp |
  | `/` | bend into the note |
  | `~` | vibrato |
  | `>` prefix | accent |
  | `:xy` | tracker arpeggio on p1/p2 (32nd notes), or chord tones on pad |
  | `\|` | visual bar line, ignored |

  Each layer loops at its own length (polymeter). Songs are made of parts of at most 8 bars, and all layers restart together at each part.
- **Rules the tests enforce:**
  - Every note parses, and every `loopLength` matches its step count.
  - Every song quotes the 5-note motif (up a minor 3rd, down a 4th, up a 5th, down a step; E G D A G in C).
  - Quarter-tones appear only in `woods` and `champion`, are never held, and are at most 1 per bar in Woods.
  - Every part has a steady pulse (kick or bass).
  - Songs are 16–32 bars, at most 7 voices.
  - Every note and SFX fades in and out over at least 5 ms (`envelope`, `gateEnv`, `tone`, `noise` set `isEnv`).
  - Live audio nodes stay at about 40 at most (`NODES`, `roomFor` skips low-priority notes).
- **Engine quality layer (don't remove without re-measuring):**
  - **Loudness trims:** `SONG_TRIM[style][song]` sets each song's player gain so songs and styles match in level. The trims close 60% of each song's gap to the median, so calm songs stay a little quieter on purpose. After changing voices, styles or song data, re-measure with `python3 tools/cdp_probe.py "$F#view=loudness&raw" 45` (raw levels) and `#view=loudness` (with trims). The compressor absorbs part of a trim, so refine the trims against the measured result.
  - **Stereo:** `PAN` values times the style's `width` (8-bit is 0, so it stays mono; Mix 0.6; 16-bit 1). Each song player gets 5 fixed panner nodes (`makeBuses`), which are not counted in the ~40-node note budget. The echo is ping-pong when width > 0.
  - **Master stage (`makeMasterChain`):** mute gain → 28 Hz highpass → 4× oversampled soft clip (clean below 0.6) → limiter. `makeMusicChain` is shared by live playback and the offline probes.
  - **M and N** fade with `smoothSet` (no clicks). Noise hits start at a random offset in a 2 s buffer.
- **Scheduler:** `setInterval` every 25 ms schedules 120 ms ahead on the audio clock. A hidden tab skips missed steps instead of bursting. Songs crossfade over 400 ms between areas, battles start with a sting, and the victory jingle is a one-shot.
- **Parrot Jungle is the user's favorite.** Its groove is the reference for the other songs, so don't change its patterns without asking.

## Testing (run both before every commit)

```sh
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
F="file://$PWD/pet-adventures.html"
# Self-test: data, sprites, all maps, 500 battles, text fit, treats, difficulty curve, music data, FM envelopes, scheduler
"$CH" --headless=new --disable-gpu --virtual-time-budget=30000 --dump-dom "$F#test" | python3 -c "import re,sys,html;print(html.unescape(re.search(r'<pre id=\"testout\">(.*?)</pre>',sys.stdin.read(),re.S).group(1)))"
# Automated play-through with simulated keys and touches (takes a minute or two)
"$CH" --headless=new --disable-gpu --virtual-time-budget=3000000 --dump-dom "$F#view=smoke" | python3 -c "import re,sys,html;print(html.unescape(re.search(r'<pre id=\"testout\">(.*?)</pre>',sys.stdin.read(),re.S).group(1)))"
```

- **Screenshots:** `--screenshot=out.png --window-size=1366,640 --virtual-time-budget=400` on `#view=<name>`. Previews include `title`, `starter`, `map_<id>`, `battle`, `moves`, `bag`, `party`, `summary`, `pen`, `shop`, `clinic`, `win`, `evolve`, `pets`, `newpets`, `intro0`–`intro5`, `name`, `nick`, `dressup`, `outfits`, `emote`, `labtop` and `boss`. Add `&touch` to force the touch layout, and use a phone-sized `--window-size` such as 844,390.
- **Real audio:** headless virtual time freezes the audio clock, so use `python3 tools/cdp_probe.py "$F#view=audioprobe" 22` (switching, crossfades, N/M, node peak), `"$F#view=clicktest&tri" 25` (offline render, measuring sudden sample jumps), or `"$F#view=jukebox" 4 shot.png`.
- **Music Room:** `pet-adventures.html#music` is the Music Room jukebox; the in-game one is Menu → Jukebox.
- **New features need new checks** in `runSelfTest()` (pure logic) or `runSmoke()` (flows). In smoke tests:
  - Save and restore anything you change on `G`, such as the party or flags.
  - Remember the battle menu remembers its last choice.
  - Remember that Enter on a name box with nothing typed only works for pet names.

## Gotchas

- Don't name a global `top`; it clashes with `window.top`. The stack helper is `topScreen()`.
- Headless Chrome barely runs `requestAnimationFrame`, so `#view=smoke` steps the game with a timer instead.
- **NPC positions:** where a trainer stands depends on story flags, so use `npcPos()` and `npcAt()`, never `n.x`/`n.y`, when checking the map.
- **Changing `MAPS`:** the self-test flood-fills each map, beating trainers in any order a player could. Arrival tiles must be walkable, and must not be grass, an exit or a door. Every edge opening must be an exit.
- **Large edits:** for big changes, write a Python patch script that asserts each anchor string appears exactly the expected number of times. Back up the file first, then run both test suites.

## Repo and workflow

- GitHub: `aserediuk/pet-adventures` (private), branch `main`, tag `v0.1`. Commits use the user's real name and email. End commit messages with the `Co-Authored-By` line the current session specifies.
- Only commit or push when the user asks.
- iOS needs the game served from a URL. A private repo can't use GitHub Pages without making the repo public or a paid plan.
