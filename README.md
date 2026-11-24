# Pet Adventures

A top-down, turn-based pet-collecting adventure for kids, in one self-contained HTML file.
It needs no install, libraries, or internet connection.

## Play

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

**The story:** pets are going missing from Pawsville, and someone in a white lab coat was seen sneaking into Whisker Woods. Choose your first pet, a puppy (Buddy) or a kitten (Mittens), then explore. Befriend wild pets with Treats and find the 8 treasure chests. Beat the Pet Champion to learn the truth, then get into Dr. Gizmo's lab and stop him from experimenting on the pets.

**Places to explore.** Each pet lives where it would in real life:

| Area | Where | Pets |
| --- | --- | --- |
| Pawsville | your town | ducks, frogs, turtles and goldfish in the pond reeds |
| Sunny Farm | east of town | puppies, kittens, ponies, bunnies and mice in the wheat; piglets in the mud; ducklings by the pond |
| Splash Lake | west of town | turtles, goldfish, frogs and ducks in the reeds |
| Meadow Path | north of town | bunnies, mice, hedgehogs (and water pets by the stream) |
| Sunny Dunes | east of Meadow Path | gerbils, hamsters, lizards and desert hedgehogs in the dry brush |
| Whisker Woods | north of Meadow Path | ferrets, hedgehogs, mice, bunnies and frogs |
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

The soundtrack is "math-rock chiptune": four chip voices (two pulse waves, a triangle bass and noise drums), odd meters, polyrhythms, and a shared five-note theme quoted in every song. Listen to any song from the pause menu's **Jukebox**, or open `pet-adventures.html#music` for the Music Room: W/S to choose, Enter to play. It shows each layer's step pattern, so you can see the polyrhythms.

## Tests

- `pet-adventures.html#test` runs the self-test. It checks sprites, data, all 3 maps (shape, reachability, exits), 500 random battles, and that UI text fits.
- `pet-adventures.html#view=smoke` plays through automatically with simulated key presses. It covers starting a game, walking, the clinic, a map exit, winning, catching, the refused Treat, losing, a chest, evolving, and beating the Champion. Results appear in the browser console.
- `#view=<screen>` opens a preview of one screen, for checking layout. Screens: `intro0`–`intro5`, `title`, `starter`, `map_pawsville`, `map_meadow`, `map_woods`, `map_lab`, `map_farm`, `map_lake`, `map_dunes`, `map_jungle`, `labtop`, `boss`, `battle`, `moves`, `party`, `summary`, `pen`, `shop`, `clinic`, `win`, `evolve`, `pets` (all 32 pets), `newpets`, `bag`, `emote`, `emotebattle`.
