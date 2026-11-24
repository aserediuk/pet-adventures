# Pet Adventures

A top-down, turn-based pet-collecting adventure for kids, in one self-contained HTML file.
It needs no install, libraries, or internet connection.

## Play

**On iPad or iPhone:** open the game in Safari. Touch controls appear automatically: a D-pad on the left, **A** (talk, confirm, hold for faster text) and **B** (back, menu) on the right, plus small Emote, Home, Music and Sound buttons. You can also tap menu choices, battle buttons and dialog boxes, and names are typed on an on-screen keyboard. Landscape gives the biggest screen. On iPhone, use Share, then **Add to Home Screen**, to play full screen. The game needs a web address to run on an iPhone or iPad (see below); opening the file from the Files app won't work.

Double-click `pet-adventures.html`. It runs in Chrome or Safari.

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

**32 pets**, each a baby that grows up at Lv 10: Buddy (dog), Mittens (cat), Alvin (hamster), Cookie (gerbil), Ziggy (lizard), Kiwi (parrot), Clover (rabbit), Nibbles (mouse), Noodle (ferret), Prickle (hedgehog), Shelly (turtle), Bubbles (goldfish), Ribbit (frog), Daisy (pony), Puddles (duckling) and Truffle (piglet). Water pets hide in the reeds by the pond and the stream.

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

## Music

The soundtrack is "math-rock chiptune" with three sound styles you can switch in the Jukebox (Left/Right): **8-bit**, **Mix** (the default: punchy 8-bit lead, arps and drums with a fuller FM bass) and **16-bit**, an emulated FM sound chip with an FM lead, a glassy FM arp/bell, a growly FM bass, a soft detuned-saw pad for calm songs, gated kick/snare/hat, and a 1/8-note echo on the Title, Whisker Woods and Clinic/Shop songs (sound effects stay 8-bit), odd meters, polyrhythms, and a shared five-note theme quoted in every song. Listen to any song from the pause menu's **Jukebox**, or open `pet-adventures.html#music` for the Music Room: W/S to choose, Enter to play. It shows each layer's step pattern, so you can see the polyrhythms.

## Tests

- `pet-adventures.html#test` runs the self-test. It checks sprites, data, all 3 maps (shape, reachability, exits), 500 random battles, and that UI text fits.
- `pet-adventures.html#view=smoke` plays through automatically with simulated key presses. It covers starting a game, walking, the clinic, a map exit, winning, catching, the refused Treat, losing, a chest, evolving, and beating the Champion. Results appear in the browser console.
- `#view=<screen>` opens a preview of one screen, for checking layout. Screens: `intro0`–`intro5`, `title`, `starter`, `map_pawsville`, `map_meadow`, `map_woods`, `map_lab`, `map_farm`, `map_lake`, `map_dunes`, `map_jungle`, `labtop`, `boss`, `battle`, `moves`, `party`, `summary`, `pen`, `shop`, `clinic`, `win`, `evolve`, `pets` (all 32 pets), `newpets`, `bag`, `emote`, `emotebattle`.
