# Graphics upgrade report

Branch `v0.4-graphics`. Every graphic in `pet-adventures.html` is now generated in code at startup, in a "modern GBA-style" pixel diorama look. Gameplay, maps, collision, music, controls and save data are unchanged.

## Results

| Check | Result |
| --- | --- |
| Self-test (`#test`) | Pass, 33 checks (2 new graphics checks) |
| Playthrough (`#view=smoke`) | Pass, 77 checks |
| Music golden snapshot | Pass, 15 songs, 11,605 note events |
| Map reachability | Unchanged (the self-test's flood fill passes on all 11 maps) |
| Text fit at 432×240 | Pass (font metrics unchanged; type tags re-checked with icons) |
| Crisp pixels | All 38 screenshots have uniform 2×2 or 3×3 pixel blocks |
| Frame time, Whisker Woods, all effects on | 0.6 ms average, 1.0 ms at the 95th percentile, 4.3 ms worst of 600 frames |
| Startup (all art built) | About 180 ms |
| Painting a map's ground on entry | 36–58 ms, once per map, then cached |

Frame times were measured in headless Chrome on this Mac with `#view=perf` (update + render + a forced flush per frame). I could not run Safari or a real MacBook Air from here, so those are not measured.

There are no unit or monkey test suites in this project; "all tests" means the self-test, the playthrough and the golden snapshot.

## Style guide scorecard

Scores are my own reading of the screenshots, 1–5.

| Section | Score | Notes |
| --- | --- | --- |
| Overall diorama feel | 4 | Dense, warm and readable. Characters are about 1.5 tiles tall. |
| Colour | 5 | 56-colour master palette; every ramp shifts hue; no plain gray or black (self-test checks this). |
| Texture | 4 | Clustered noise on grass, paths, canopies, sand and snow, with no visible tile repeats. Tall grass still shows faint rows. |
| Light and shadow | 4 | Upper-left light on every shape, contact shadows baked into the ground and under characters, sunbeams and vignette. |
| Outlines | 5 | Environment uses its own darker shades; characters and pets get a thin dark-brown outline. |
| Props | 4 | All listed props exist. The mailbox, picket fence and garden beds are part of the building pictures, because the maps could not change. |
| Buildings | 5 | Blue-roof cottage with flower boxes, mint clinic with a heart-and-paw sign, shop with striped awning and bone sign, plus a barn. |
| Characters | 4 | 15 looks, 4 directions, 4-frame walk, 2-frame idle. Player wears a green hoodie and backpack. |
| Pets | 4 | 33 pets, front and back at 48×48, plus 32 and 16 px. Back views are plainer than the fronts. |
| Animation | 4 | Water sparkles, swaying tall grass and flower beds, chest, evolution rays, idle pets. |
| Biome moods | 4 | Every map has a mood. Whisker Woods has no stream in its map, so the stepping stones are in Meadow Path. |
| Battle scenes | 4 | A backdrop per biome, impact sparks, flash and shake, treat toss, hearts. |
| UI | 4 | 9-slice cream panels, shiny bars, type icons. The existing pixel font was kept (see below). |
| Title and win | 5 | Pawsville diorama with pixel-lettered logo; festive golden version for the win. |

### The three weakest areas, and what I did

1. **Evolution scene** was a flat dark screen. It now has turning rays of light, a pulsing glow, the white silhouette flicker and a star burst on reveal.
2. **Menu backgrounds** (party, Pet Pen, summary, dress-up) were flat old colours. They now use a striped paw-print backdrop from the master palette.
3. **Flower beds** did not sway. They are now a two-frame overlay.

## Departures from the brief

- **Screenshots** were taken with headless Chrome, not Playwright, which is not installed here.
- **Auto-tiling** is done per pixel, not with edge and corner tile pieces: each pixel looks up its terrain through a noise wobble, so borders are organic and nothing repeats.
- **Font:** the game already had a procedurally drawn pixel bitmap font. I kept its glyphs and metrics so every text-fit check still holds.
- **Battle sprites** are 48×48 as asked. They are smaller on screen than the old 64-pixel (doubled) sprites.
- **Intro close-ups** still draw characters at 2×–4×. They are whole-pixel crisp, but their pixel density differs from the scene.
- **Not redrawn:** treat icons, emote bubbles and pet accessories (bows, hats) keep their earlier pixel art.
- **Old art data** (the earlier string-array tiles, people and pets) is still in the file and is still built at startup before being replaced. It is unused on screen and could be removed in a follow-up.

## Originality check

- No image, sprite sheet, logo or screenshot was downloaded, traced or embedded. There is no base64 or external asset in the file.
- Every graphic comes from generator functions over palette-indexed pixel maps (`Pix`), using shapes, ramps and deterministic noise written for this game.
- Pets are ordinary animals (dog, cat, hamster, gerbil, rabbit, mouse, ferret, hedgehog, pony, pig, lizard, parrot, duck, turtle, fish, frog) built from shaded ellipses. I reviewed all 33 sheets and found nothing that resembles a character or creature from an existing game, show or franchise.
- There are no ball-shaped emblems or catch devices. Wild pets are befriended with treats. The clinic sign is a heart with a paw print; the shop sign is a bone.
- There are no signatures or watermarks. The only credit is the title-screen licence line.

## Screenshots

In `tests/screenshots/graphics/`, each at 2× (1024×600 window) and 3× (1366×768 window), 38 files:

`title`, `pawsville`, `meadow`, `woods`, `interior-clinic`, `shop`, `dialog`, `win`, and a battle in each of the 11 areas: `battle-pawsville`, `battle-meadow`, `battle-woods`, `battle-farm`, `battle-lake`, `battle-dunes`, `battle-canyon`, `battle-jungle`, `battle-marsh`, `battle-peak`, `battle-lab`.

## Commits

One per stage: palette and shading helpers; font and UI; ground and auto-tiling; trees, forest borders, buildings and depth sorting; props; characters; pets; battle scenes; lighting, sunbeams and particles; title and win screens; then this quality pass.
