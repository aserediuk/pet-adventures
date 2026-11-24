# Pet Adventures

**[▶ PLAY NOW](https://aserediuk.github.io/pet-adventures/pet-adventures.html)**: plays right in your browser, on a computer, iPad or iPhone.

A top-down, turn-based pet-collecting adventure for kids, in one self-contained HTML file.
It needs no install, libraries, or internet connection.

Its soundtrack is the showpiece: a complete music engine, written from scratch inside that same file, that synthesizes every note live in the browser. There are no audio files at all. See [The music engine](#the-music-engine).

## Look

The whole world is drawn in code, with no image files: a lush pixel diorama of mottled grass, soft dirt paths, layered forests, sparkling water and cosy buildings, lit by warm afternoon sun. Every map has its own mood, from fireflies in Whisker Woods to snowfall on Frosty Peak. The 33 pets keep their original hand-drawn look, with added light and shade.

## Play

**On a PC or Mac:** double-click `pet-adventures.html`. It opens in your browser (Chrome, Edge or Safari) and plays with the keyboard. Nothing to install, and it works offline.

**On iPad or iPhone:** open [the game's web address](https://aserediuk.github.io/pet-adventures/pet-adventures.html) in Safari. Touch controls appear automatically: a D-pad on the left, **A** (talk, confirm, hold for faster text) and **B** (back, menu) on the right, plus small Emote, Home, Music and Sound buttons. You can also tap menu choices, battle buttons and dialog boxes, and names are typed on an on-screen keyboard. Landscape gives the biggest screen. On iPhone, use Share, then **Add to Home Screen**, to play full screen. An iPhone or iPad needs the game served from a web address; opening the file from the Files app won't work.

Press **Space** to begin. A short intro from *When Pets Attack Studio Productions* introduces the story and the evil Dr. Gizmo: **Space** skips it, **Enter** goes to the next scene.

| Key | What it does |
| --- | --- |
| Arrows / WASD | Walk, move the cursor |
| Enter / Space / E | Talk, open chests, confirm, next text (hold to speed text up) |
| Q / Esc | Back, open the menu (in fullscreen use Q, since the browser keeps Esc) |
| V | Emote! Heart, star, music note or happy face (in battle your pet celebrates) |
| H | Go home to your house (asks first) |
| M | Mute everything |
| N | Music on/off (sound effects stay on) |
| F | Fullscreen on/off |

**Super Hamster:** once Dr. Gizmo is beaten, he rewires his Mega-Zapper into the Super Growth Machine. Bring a Nugget (a grown-up Alvin), face the machine and press A to turn it into a Super Hamster, the strongest pet in the game.

**Tasks:** characters with a yellow **?** over their head need help: find a lost item, bring home a lost pet, or befriend a certain kind of pet to show them. Accept with Yes, check progress under **Tasks** in the menu, and come back (green **!**) for a reward.

**Helpful characters** in every area give tips: what to do next (who to beat, where, and how strong your team should be) and how to battle better. You can leave any battle with Run; trainers stay unbeaten so you can come back stronger.

**The road:** Pawsville → Meadow Path → Pebble Canyon → Whisker Woods → Misty Marsh → Frosty Peak → Gizmo's Lab. Gatekeepers block the canyon pass, the marsh bridge and the mountain pass until you beat them, and Champion Maple only battles trainers with all 4 **Trail Ribbons** (won from the guardians of Sunny Farm, Splash Lake, Sunny Dunes and Parrot Jungle).

**The story:** pets are going missing from Pawsville, and someone in a white lab coat was seen sneaking into Whisker Woods. Choose your first pet, a puppy (Buddy) or a kitten (Mittens), then explore. Befriend wild pets with Treats and find the 8 treasure chests. Beat the Pet Champion to learn the truth, then get into Dr. Gizmo's lab and stop him from experimenting on the pets.

**Places to explore.** Each pet lives where it would in real life:

| Area | Where | Pets |
| --- | --- | --- |
| Pawsville | your town | ducks, frogs, turtles and goldfish in the pond reeds |
| Sunny Farm | east of town | puppies, kittens, ponies, bunnies and mice in the wheat; piglets in the mud; ducklings by the pond |
| Splash Lake | west of town | turtles, goldfish, frogs and ducks in the reeds |
| Meadow Path | north of town | bunnies, mice, hedgehogs (and water pets by the stream) |
| Sunny Dunes | east of Meadow Path | gerbils, hamsters, lizards and desert hedgehogs in the dry brush |
| Pebble Canyon | north of Meadow Path | lizards, hedgehogs, ferrets, mice, gerbils |
| Whisker Woods | north of Pebble Canyon | ferrets, hedgehogs, mice, bunnies and frogs |
| Misty Marsh | north of Whisker Woods | frogs, ducks, turtles, goldfish in the reeds; piglets in the mud |
| Frosty Peak | north of Misty Marsh | snow bunnies, mice, ferrets, dogs and cats, plus the Champion at the summit |
| Parrot Jungle | east of Whisker Woods | parrots, lizards and frogs |

**33 pets**: the Super Hamster, plus 16 babies that each grow up at Lv 10: Buddy (dog), Mittens (cat), Alvin (hamster), Cookie (gerbil), Ziggy (lizard), Kiwi (parrot), Clover (rabbit), Nibbles (mouse), Noodle (ferret), Prickle (hedgehog), Shelly (turtle), Bubbles (goldfish), Ribbit (frog), Daisy (pony), Puddles (duckling) and Truffle (piglet). Water pets hide in the reeds by the pond and the stream.

**Names and dress-up:** you type your name when you start a new game (change it any time in Menu, Your Name). Give pets nicknames, and dress them up with a bow, top hat, crown, flower or party hat in 6 colors (Menu, Pets, pick a pet).

**Making friends:** offer a tired wild pet a treat it really likes. Pets eat what they like in real life:

| Treat | Loved by |
| --- | --- |
| Bone | dogs, ferrets |
| Fish | cats |
| Seeds | hamsters, gerbils, mice, parrots, ducks |
| Bugs | lizards, hedgehogs, turtles, frogs |
| Carrot | rabbits, ponies, pigs |
| Apple | parrots, ponies, pigs |
| Lettuce | rabbits, turtles, ducks |
| Fish Flakes | fish |

Offer the wrong snack and the pet usually turns up its nose. In battle, the Bag marks the wild pet's favorites with a red ♥.

Types come in loops (1.5× damage forward, 0.67× backward): **Dog > Cat > Hamster > Gerbil > Dog**, **Cat > Parrot > Lizard > Cat**, **Cat > Mouse**, **Ferret > Mouse > Pony > Pig > Hedgehog > Ferret** and **Duck > Frog > Fish > Turtle > Rabbit > Duck**. A pet's Summary shows what it's strong and weak against.

## The music engine

Every sound in Pet Adventures is made on the spot by a tracker-style synthesizer built into the game file. There are no audio files, samples or libraries: just song data (a few lines of text per song) and a Web Audio engine that plays it.

**The style** is "math-rock chiptune": odd meters, polyrhythms and tapping arpeggios on retro sound chips.

- **19 songs**, from a 3/4 music box in the Pet Clinic to a 9/8 + 8/8 + 7/8 battle theme.
- **Polymeter built in.** Each instrument loops at its own length, so a 5-step riff drifts against an 8-step drum beat and locks back in on schedule.
- **Three sound styles**, switchable any time in the Jukebox:

  | Style | Sound |
  | --- | --- |
  | **8-bit** | Pulse-wave lead and arpeggios, triangle bass, noise drums. Mono, like a real chip. |
  | **Mix** | The punchy 8-bit lead, arps and drums with a fuller FM bass and a light echo. |
  | **16-bit** (default) | An emulated FM sound chip: FM lead, glassy FM bell arps, growly FM bass, a soft pad on calm songs, gated drums, stereo and ping-pong echo. |

- **Two main themes.** A main theme is a title track plus a five-note melody that every other song quotes. Switch between them in the pause menu (**Music Theme**) or with **T** in the Jukebox, and the whole soundtrack changes its quotes at once with a smooth crossfade.
  - **Theme 1** (default) is a 70-second piece in klezmer mode on D. A choppy 7/8 riff with quarter-tone "snap" bends and tremolo locks in with the drums, stretches over a 14-beat cycle, then settles into a danceable 4/4 groove. There the layers stack like a looper pedal, the 7-beat riff slides against the 8-beat bars (lining up again every 7 bars), and little pet chirps (yip, mew, squeak) answer the melody.
  - **Theme 2** is the original: E G D A G, in a 7/8 title track.
  - Under Theme 1, every other song carries its signature sounds: a bell doubles the melody quote an octave up with snap bends, a pet chirp answers it, and the quote returns in the song's other sections where it fits the harmony.
  - Add `?theme=theme2` or `?theme=theme1` to the address to pick one directly.
- **Expressive notes:** accents, held notes, vibrato, tracker arpeggios, quarter-tones, three kinds of pitch bend, tremolo, tom fills and FM pet voices.
- **Studio-style output:**
  - Every note fades in and out over at least 5 ms, so there are no clicks.
  - Every song is loudness-matched in every style (measured by rendering each one offline).
  - The music ducks under sound effects.
  - A soft clipper and limiter keep it from ever distorting.
- **Rock-solid timing:** notes are scheduled ahead on the audio clock, songs crossfade over 400 ms between areas, and a hidden browser tab resumes cleanly instead of bursting.

**Listen:** open the **Jukebox** from the pause menu, or open `pet-adventures.html#music` for the Music Room.

| Key | Jukebox action |
| --- | --- |
| W / S | Choose a song |
| Enter | Play it |
| A / D | Switch sound style (on "Main Theme - Theme 1": jump between its sections A–F) |
| T | Switch the main theme and hear every song change its quotes |
| N | Music on/off |

The Jukebox shows each instrument's step pattern as it plays, so you can watch the polyrhythms line up. For Theme 1 it also shows the section, bar number and meter.

## Tests

- `python3 tools/check_golden.py` checks that Theme 2 still plays exactly the notes saved in `tests/golden/theme2-events.json` (it needs Chrome).
- `pet-adventures.html#test` runs the self-test. It checks sprites, data, all 3 maps (shape, reachability, exits), 500 random battles, and that UI text fits.
- `pet-adventures.html#view=smoke` plays through automatically with simulated key presses. It covers starting a game, walking, the clinic, a map exit, winning, catching, the refused Treat, losing, a chest, evolving, and beating the Champion. Results appear in the browser console.
- `#view=<screen>` opens a preview of one screen, for checking layout. Screens: `intro0`–`intro5`, `title`, `starter`, `map_pawsville`, `map_meadow`, `map_woods`, `map_lab`, `map_farm`, `map_lake`, `map_dunes`, `map_jungle`, `labtop`, `boss`, `battle`, `moves`, `party`, `summary`, `pen`, `shop`, `clinic`, `win`, `evolve`, `pets` (all 32 pets), `newpets`, `bag`, `emote`, `emotebattle`.

## License

© 2026 When Pets Attack Studio Productions. Pet Adventures is free for noncommercial use under the [PolyForm Noncommercial License 1.0.0](LICENSE).
