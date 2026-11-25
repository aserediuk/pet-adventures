# Pet Adventures

A top-down, turn-based pet-collecting RPG for kids. The whole game is **one self-contained file**, `pet-adventures.html` (about 6,600 lines of HTML, CSS and vanilla JS). **To play on a PC or Mac:** double-click the file; it opens in Chrome, Edge or Safari and uses the keyboard. **On iPad or iPhone:** open it from a web address in Safari (touch controls appear; a local file won't run there). `README.md` is the player-facing guide; keep it in step with features.

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
  | T | Switch main theme (Jukebox only) |

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

- **Maps:** `rows` of tile characters, which must be rectangular. Maps are **written at their original size and stretched to 1.5× at startup** (`growMaps`, section 7d; the user asked for areas 50% bigger). Written size is at most 48×32, which becomes 72×48. `growMaps` doubles evenly spaced rows and columns, never one that runs through a building, an exit or a gatekeeper's post, and moves every position in `MAPS` and `QUESTS`. Positions inside the map data are in written coordinates; code elsewhere that names a written position must convert it with `gx(map, x)` / `gy(map, y)`. The lab is not stretched (`NO_GROW`). Old saves are moved to the same spot (`G.big`). Reed beds count as "by the water" within 2 tiles (`nearWater`). Tile legend:

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
- **Treats:** `TREAT_LIKES[type]` lists the treats each type likes (real-life diets). A wrong treat is usually refused (`WRONG_TREAT_REFUSE`). Treats are **not sold** (`SHOP_ORDER` leaves them out): they come from chests.
- **Chests:** each chest gives its own prize the first time (`G.chests[id]`, which also counts for the win screen). Every opening also has a 67% chance (`CHEST_TREAT_CHANCE`) of 2 treats that the area's pets like (`chestTreat`). An opened chest is in `G.chestOpen`; `refillChests()` empties that list on a nap at home, a heal at the Clinic and a blackout, so treats can never run out for good.
- **Shop prices:** Bandage 150, Big Bandage 500, Fishing Rod 350 (user's numbers).
- **Bosses:** an NPC with `boss: '<species>'`, `hp: <multiplier>` and a one-pet `trainer.team` is a big wild pet, drawn with the 32 px sprite. It stands two tiles beyond a gatekeeper in a one-tile corridor, fights as a trainer battle (no treats, running works, it stays put), has its HP multiplied (`maxHp` uses `pet.boss`), and steps aside with `moveTo` when beaten. Levels are the user's (raised once to make the game harder): Bramble (Pebble Canyon) Lv 12, Gloop (Misty Marsh) Lv 15, Blizzard (Frosty Peak) Lv 20; Dr. Gizmo's team is Lv 28. Champion Maple's four pets and Lab Helper Bolt's two are Lv 22 (also the user's numbers); the difficulty-curve self-test assumes four pets at Lv 21 for Maple. Tune a boss with its `hp`, not its level; the difficulty-curve self-test includes them.
- **Fishing Rod:** fish take no treats (`TREAT_LIKES.Fish` is empty, `needsRod`). `ITEMS.rod` costs 350 coins at the Pet Shop, is bought once (`G.bag.rod` is 0 or 1) and is never used up. In a wild battle with a fish, Bag → Fishing Rod runs `castRod` with `rodChance` (the same odds as a favourite treat). Offering a fish a treat is refused without using the treat or the turn. Old saves get 20 coins back per Fish Flakes.

## Graphics system (sections 3b–3j, marked `// >>> GFX:name` … `// <<< GFX:name`)

All art is generated in code at startup. `tests/graphics-report.md` has the scorecard, performance numbers and known gaps.

- **Palette (`RAMPS`, `PI`, `PALETTE`):** 56 colours in hue-shifted ramps, light to dark. `DARKER[]`/`LIGHTER[]` step any colour along its ramp. Never add plain grays or black; the self-test rejects them. Use `PI.<ramp>[i]` in generators, never hex strings.
- **`Pix`:** a palette-indexed pixel map. `ell()` draws a blob lit from the upper left with clustered texture; `poly`, `line`, `rect`, `blit`; `outline()` for characters and pets; `selfEdge()` for environment art (no dark outlines). `toCanvas()` keeps `.pix` on the canvas.
- **Noise:** `hash2`, `vnoise`, `speckle` are deterministic, so nothing flickers.
- **Ground (`paintGround`, `groundOf`):** each map's ground is painted once per pixel and cached (about 190–230 ms for the biggest maps, on first entry). Terrain is looked up through a noise wobble, which makes the organic borders; a distance map `D` drives rims, shallows and foam; a fringe pass hangs grass blades over paths and banks; then per-tile details are stamped. Tall grass (`tallBlades`) is a 20×22 picture drawn at `-TALL_OX, -TALL_OY`, so it overhangs its tile. `TERRAIN` maps tile characters to terrain; `BIOME[mapKey]` sets the grass tones and details. Map data, tile ids and walkability are never changed by graphics code.
- **Tall things (`worldObjects`):** trees (`treePix(kind, variant, B, tone)`, 36×52, `TREE_VARIANTS` shapes; tone 1 is the darker tree inside a forest), boulders, cacti and fences are baked into one strip per map row (`STRIP_RE`); buildings are separate pictures. `drawWorld` sorts strips, buildings and characters by row. A character just north of a tree or roof is drawn again from the waist up, so it stays visible.
- **Characters (`LOOK2`, `personPix`):** 16×24, frames 0 stand, 1 step A, 2 mid, 3 step B, 4 idle. Draw with `drawChar` (feet on the tile's bottom).
- **Pets (`petPolish`, `PET_BIG`, `PET_SPR`, `PET16`):** the user rejected generated pets as too cute and not animal-like (the hamster looked like a bear), tried three samples and chose "the original, shaded". So pet shapes come only from the original hand-drawn 32×32 string-array sprites in section 3 (`PET_OLD`). `petPolish` doubles each with Scale2x for battles (64×64), maps it onto the master palette (`petColour`) and adds upper-left shading; menus use the 32 px drawing with lighter shading; the overworld uses a 16 px reduction (`petTiny`). Your own pet in battle is the mirrored front, as in the original game. `drawPetSprite(sp, x, y, s)`: `s = 1` is 32 px, `s = 2` is 64 px, `s = 4` is 128 px. To change a pet's look, edit its string-array art; never redraw pets procedurally without asking.
- **Battle (`battleBackdrop`, `SCENE`):** one painted backdrop per biome. `HORIZON` is 82 so the far pet's patch sits on the ground. Particles (`fxSpawn`) use their own random generator (`fxRand`), so effects never shift gameplay dice rolls.
- **Light (`MOOD`, `drawMood`):** pre-rendered sunbeams, vignette, mist and glows, drawn as whole overlays. No per-pixel work happens during play.
- **Exits must be easy to see** (user feedback): trees whose crowns would hang over an exit or the few steps leading to it are drawn as low bushes (`low` in `worldObjects`), and `drawExitArrow` bounces a yellow arrow on every exit.
- **No overlaps:** the user asked that panels and text never cover the art. The title and win screens are laid out around `DIO_HZ`; check screenshots after moving anything there.
- **Scenes:** `drawDiorama` (title and win), `roomBackdrop` (Clinic and Shop), `menuBackdrop`, `evolveRays`.
- **Previews:** `#view=palette`, `people`, `people2`, `petsheet&0`–`5`, `petzoom&a,b,c,d` (each shows the original beside the shaded sprite), `battlein&<map>&<your pet>&<other pet>[&hit|super|caught]`, `perf&<map>`.
- **Editing the graphics code:** while it was built, each chunk lived in its own file and was injected between its markers. Edit in place now, keeping the markers.
- **Still to do:** the old string-array art for tiles and people is unused on screen but still in the file (the pet art is in use); treat icons, emotes and accessories were not redrawn.

## Machine evolution

Some grown-up pets have `machineEvo` (a species marked `machineOnly`) instead of `evo`. So far that's Nugget → Super Hamster (`superham`). Battles never trigger it. The player faces Dr. Gizmo's Mega-Zapper (`Z` tiles in the lab) and presses A (`useMachine`). It's locked until `G.flags.gizmo`, and Gizmo's `final` lines explain it. `evolveScene(p, to, intro)` handles both kinds of evolution. The Super Hamster sprite is built from Nugget's art: a mask and cape sides are painted onto the half rows, and a cape canvas (`pet_superham_cape`) is drawn behind the body. The difficulty-curve self-test leaves `machineOnly` pets out of a "usual" team.

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
  - HP = ⌊base·L/20⌋ + L + 10. Other stats = ⌊base·L/25⌋ + 5. The level cap is 30 (`MAX_LV`; the user chose to raise it from 20 so a Lv 28 Dr. Gizmo can be beaten). Trainer pets may be up to `FOE_MAX_LV`. The difficulty-curve self-test assumes six pets at Lv 24 for Dr. Gizmo.
  - XP to the next level = 12·L² (`toNext`; raised 20% from 10·L² at the user's request). The difficulty-curve self-test assumes fixed team levels, so it does not notice slower levelling.
- **Rewards:** XP per win = (5·L² + 10) × 1.5 (trainers only) × `XP_BONUS` 1.25. Benched pets get half.
- **Damage:** ⌊((2L/5+2)·Pow·Atk/Def)/50 + 2⌋ × type multiplier × random 0.85–1. Enemies hit at `ENEMY_DAMAGE` (0.85).
- **Catching:**
  - Catch chance = clamp(0.25 + 0.6·(1 − hp/max), 0.05, 0.95).
  - A favorite treat multiplies it by 1.2. A wrong treat multiplies it by 0.3, after a 75% chance of refusal.
- **Main road:** Pawsville → Meadow Path → Pebble Canyon (gatekeeper Rex, then boss Bramble) → Whisker Woods → Misty Marsh (Fen, then boss Gloop) → Frosty Peak (Bo, then boss Blizzard, then Champion Maple at the summit) → Gizmo's Lab (Bolt, then Dr. Gizmo, then the win screen).
- **Side areas:** Sunny Farm, Splash Lake, Sunny Dunes and Parrot Jungle each have a ribbon guardian. Maple needs all 4 **Trail Ribbons**.
- **Starters:** a puppy (Buddy) or a kitten (Mittens) only.
- **Difficulty curve:** a self-test simulates a typical team at the level a player usually has for each big fight. Win rates must stay between **45% and 92%**. Retune trainer levels, not the formulas, if it fails.

## Audio system (section 4)

Everything is synthesized with Web Audio; there are no audio files. The pieces, in file order: SFX → `MainThemes` → `SONGS` → compiler → scheduler → voices → Jukebox.

### Song data

- A song is `{ title, bpm, spb, barSteps, meter, form, parts }`. `form` is a list of part names; each part is `{ bars, layers, barSteps?, meter?, echo?, solo? }` of at most 8 bars. All layers restart together at each part.
- A layer is `L(voice, steps, loopLength, opts)`. Each layer loops at its own length, which is what makes the polymeter.
- **Voices:** `p1` (lead), `p2` (arp), `tri` (bass), `noise` (drums), `pad`, `chirp` (pet voices). One layer per voice in a part.
- **Step tokens:**

  | Token | Meaning |
  | --- | --- |
  | `C4`, `F#5`, `Bb3` | a note |
  | `.` | rest (a held note keeps ringing through it) |
  | `_` | rest that also ends a held note |
  | `-` suffix | hold |
  | `+` | quarter-tone sharp |
  | `/` | slide up from a quarter-tone flat (90 ms) |
  | `^` | snap bend: from a quarter-tone flat to pitch within 60 ms |
  | `%` | wobble bend: dips a quarter-tone and returns, ending in tune |
  | `~` | vibrato |
  | `>` prefix | accent |
  | `:xy` | tracker arpeggio on p1/p2 (32nd notes), or chord tones on pad |
  | `T1`–`T5`, `U1`–`U5` | the active theme's notes (see Main themes) |
  | `\|` | visual bar line, ignored |

- **Drum tokens:** `k` kick, `s` snare, `h` hat, `g` ghost, `r` rimshot, `x` kick + snare, `t`/`m`/`l` high/mid/low tom.
- **Chirp tokens:** `y` yip, `m` mew, `q` squeak (pitch curves in `MainThemes.theme1.chirps`).
- **Layer options:** `duty` (pulse width), `tr` (transpose in semitones), `gate` (note length as a fraction of a step), `trem` (route through the tremolo bus), `off` (start offset in steps, to carry a loop's position across parts), `q` (theme quotes).
- `compileSong(name)` caches per theme (`name|theme`). `songEventDump()` lists every scheduled event.

### Main themes

- **Naming:** **Theme 1** (key `theme1`, the default) is the newer klezmer-mode theme; **Theme 2** (key `theme2`) is the original soundtrack. They were first built the other way round and renamed at the user's request, so the golden file for the original is `theme2-events.json`. Theme 1's own songs have ids ending in `K`: `titleK`, `winK`, `championK`, `victoryK`.
- `MainThemes.theme2` and `.theme1` each hold `name`, `theme` (5 notes), `intervals`, `sting`, `songs` and `title` (the title track's data). theme1 also has `riff`, `hook`, `groove`, `chirps` and a `minor` variant of its intervals.
- **Theme 2 must never change musically.** `tests/golden/theme2-events.json` holds every song's events for 2 loops as they were before Theme 1 existed, and `python3 tools/check_golden.py` must pass. Run it after any change to song data, the compiler or the scheduler.
- **Quotes:** songs quote the active theme with `T1`–`T5`. The layer's `q: [Q(root1, root2, iv1, iv2)]` gives the root note per theme and optional interval variants (Theme 2's lydian or major variants; `MINOR2` for Theme 1 in minor keys). `U1`–`U5` use the second entry of `q`.
- **Signature sounds (`addSignature`, themes with `signature: true`, so Theme 1 only):** the user found that changing 5 notes per song was too subtle to hear, and chose this over reworking grooves. At compile time, with no change to song data: quote notes get an accent on the 1st and snap bends on the 2nd and 4th (`quoteToken`); a bell (`p2` timbre, labelled THEME) doubles the quote an octave up; a pet chirp answers it; and in parts without a quote the bell plays it once at the first bar where every note is consonant with the bass and lead (it stays out if no bar fits). Added layers are marked `sig`. `#view=signature` lists what each song gets. Theme 2 must get none of this (self-test and golden check).
- **Selection:** `activeThemeKey` (default `theme1`). Order of precedence at startup: `?theme=theme2|theme1` in the address, then the stored setting (`petAdventures.settings.v1`, with the sound style), then the default. A save also stores `musicTheme`; it applies only when the browser has no stored choice (`applySavedTheme`). `setMusicTheme(k)` switches at once with a 400 ms crossfade (`rethemeAt`).
- **Song swaps:** `themeSong(name)` maps a requested song to the active theme's version. Theme 1 swaps `title` → `titleK`, `win` → `winK` (section E of the title), `champion` → `championK` (last 8 bars: the riff in 7/8, then the 4/4 groove) and `victory` → `victoryK` (last five notes are the theme). `switchSong(name, now, { raw: true })` skips the swap; the Jukebox uses it for its two "Main Theme" rows. Each player remembers what was asked for in `pl.req`.
- **Theme 1's title (`titleK`)** is 40 bars, about 70 s at 128 BPM, with a constant eighth note:

  | Section | Parts | Bars | What happens |
  | --- | --- | --- | --- |
  | A | `A` | 4 of 7/8 | riff alone, tremolo, echo |
  | B | `B` | 8 of 7/8 | drums and bass hit the riff's rhythm; pet chirps |
  | C | `C1 C2 C3` | 8 of 7/8 | lead sings the theme in a 14-eighth cycle; hats, then a rising arp |
  | D | `D1 D2` | 7/8 + 4/4 | riff alone, then a tom fill |
  | E | `E1`–`E6` | 16 of 4/4 | looper build, then the hook twice (second time an octave up) and a tag |
  | F | `F` | 2 of 7/8 | riff alone, back into A |

  Parts whose names share a first letter form one section (`songSections`). The self-test checks these lengths, the riff's `off` continuity through E, and that it realigns 7 bars after it enters.
- The spec that asked for Theme 1 mentioned an "RNG ?theme= parameter"; the game has no RNG or seed parameter, so there was nothing to preserve.

### Sound styles (`STYLES`)

Default `16bit` (the user's choice; Mix was the default before). Players switch with A/D in the Jukebox, and the choice is stored.

| Data voice | 8-bit | Mix | 16-bit |
| --- | --- | --- | --- |
| `p1` | pulse | pulse | FM lead |
| `p2` | pulse | pulse | FM bell arp (ratio 3.5 or 7, or 2 if `duty: 0.5`) |
| `tri` | triangle | FM bass | FM bass |
| `noise` | noise bursts, triangle kick | noise bursts, sine kick | gated kick/snare/hat |
| `pad` | off | off | detuned saws (only in `PAD_SONGS`) |
| `chirp` | square blip | square blip | FM blip |
| echo | off | 0.6× | full, ping-pong |
| stereo width | 0 (mono) | 0.6 | 1 |

Sound effects (`SFX`, `tone`, `noise`) always stay 8-bit.

### Signal path

- Music: voice → (tremolo bus or stereo bus) → player gain (the song's loudness trim) → `musicIn` → 11 kHz lowpass → compressor (ratio 3, 8 ms attack) → `musicBus` (0.18; N toggles it) → `duck` (dips under each SFX) → master.
- Echo: a send from the player gain, 1/8-note delay, feedback 0.3, lowpassed. Songs opt in with `SONGS.x.echo`; a part can switch it on or off with `echo: 1|0` (`pl.onPart`).
- Master (`makeMasterChain`): mute gain (M) → 28 Hz highpass → 4× oversampled soft clip (clean below 0.6) → limiter → speakers.
- `makeMusicChain` is shared by live playback and the offline probes.

### Quality rules (don't remove without re-measuring)

- **No clicks:** every note and SFX fades in and out over at least 5 ms (`envelope`, `gateEnv`, `tone`, `noise` mark their gain `isEnv`, and the self-test checks each one). M and N fade with `smoothSet`.
- **Pitch shapes** go through `pitchShape()`, and every shape ends exactly in tune.
- **Loudness trims:** `SONG_TRIM[style][song]` sets each song's player gain. Trims close 60% of each song's gap to the median, so calm songs stay a little quieter on purpose. After changing voices, styles or song data, re-measure with `python3 tools/cdp_probe.py "$F#view=loudness&raw" 90` (raw) and `#view=loudness` (with trims). The compressor absorbs part of a trim, so refine against the measured result. Theme-2-only songs are measured over their whole loop; the others over 24 s.
- **Node budget:** about 40 live note nodes (`NODES`, `roomFor`; low-priority notes are skipped first). Fixed routing per player (panners, pad filters, ping-pong echo, tremolo) is kept in `pl.fixed` and not counted. A song that is fading out stops starting pad, arp, chirp and hi-hat notes. In 16-bit the real-audio probe can still skip about 1 quiet arp note while a new song fades in.
- **Stereo:** `PAN` values times the style's width. Bass, kick and snare stay centred.
- Noise hits start at a random offset in a 2 s buffer.

### Scheduler

`setInterval` every 25 ms schedules 120 ms ahead on the audio clock (`pumpPlayer`). A hidden tab skips missed steps instead of bursting. `switchSong` crossfades over 400 ms (`cut` and `sting` stop the old song at once), and never leaves two songs playing. Battles start with the active theme's 3-note sting; the victory jingle is a one-shot. Music starts only after the first key press or tap (`audioUnlock`).

### Rules the self-test enforces

- Every note parses, and every `loopLength` matches its step count.
- Under each theme, every song that theme plays quotes that theme.
- Quarter-tones (`+`, `/`) appear only in `QUARTER_TONE_SONGS`, are never held, and at most 1 per bar in Woods.
- Every part has a kick or bass, unless it's marked `solo`.
- Songs are 16–32 bars (unless `long`), with at most 7 voices and no repeated voice in a part.

### Jukebox (`MusicRoomScreen`)

Rows: "Main Theme - Theme 2", "Main Theme - Theme 1" (both always as written), then every other song as the active theme plays it. A/D switches sound style, or jumps between sections when Theme 1's row is selected. T (or tapping the Theme label) switches the theme.

### User preferences

- **Parrot Jungle is the user's favorite.** Its groove is the reference for the other songs, so don't change its patterns without asking.
- The user wants originality: Theme 1 uses techniques from microtonal math rock, but no existing song's melody, riff or rhythm.

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
- **Golden check:** `python3 tools/check_golden.py` (Theme 2's notes must match `tests/golden/theme2-events.json`).
- **Graphics:** `python3 tools/cdp_probe.py "$F#view=perf&woods" 14` reports frame times; screenshots of the main screens are in `tests/screenshots/graphics`.
- **Real audio:** headless virtual time freezes the audio clock, so use `"$F#view=themeprobe" 232` (Theme 1 in all three styles, section jump, theme switching), or `python3 tools/cdp_probe.py "$F#view=audioprobe" 22` (switching, crossfades, N/M, node peak), `"$F#view=clicktest&tri" 25` (offline render, measuring sudden sample jumps), or `"$F#view=jukebox" 4 shot.png`.
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

- GitHub: `aserediuk/pet-adventures` (private), branch `main`, tags `v0.1`–`v0.3`. Commits use the user's real name and email. End commit messages with the `Co-Authored-By` line the current session specifies.
- Only commit or push when the user asks.
- **License:** PolyForm Noncommercial 1.0.0 (`LICENSE`), © 2026 When Pets Attack Studio Productions. The game file has a header comment and the title screen shows `CREDIT_LINE`.
- **Live build:** GitHub Pages serves `main` at https://aserediuk.github.io/pet-adventures/pet-adventures.html (the README's PLAY NOW link). iOS needs the game served from a URL like this; a pushed commit is what players get.
