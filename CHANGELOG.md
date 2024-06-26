![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.webp)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  Changelog |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md">FAQ</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/ADDONS.md">Addons</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> |
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

# Changelog
- [0.4.2](#042) Release Date: June 24, 2024
- [0.4.1](#041) Release Date: June 22, 2024
- [0.4.0](#040) Release Date: Not released.
- [0.3.1](#031) Release Date: June 12, 2024
- [0.3.0](#030) Release Date: June 9, 2024
- [0.2.0](#020) Release Date: June 4, 2024
- [0.1.1](#011) Release Date: May 30, 2024
- [0.1.0](#001) Release Date: May 29, 2024

## 0.4.2

Key Info

 - Save-safe with previous version (I think). Ignore missing plugin(s), they shouldn't matter.
 - Added cloaks. Will do more for integration later.
 - Bug fixes.
 - Balance Tweaks.

<Details>
<summary>Changes</summary>

### Updated

 - [Cities of the North Optimized Meshes](https://www.nexusmods.com/skyrimspecialedition/mods/85242)
 - [Blue Palace Terrace Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/107752)
 - [Bjorn - Fully Voiced Follower](https://www.nexusmods.com/skyrimspecialedition/mods/91652)
 - [Atlantean Landscape -Complete- Complex Terrain Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/89542)
 - [Ultimate NPC Dodging](https://www.nexusmods.com/skyrimspecialedition/mods/120738)
 - [Skyking Signs](https://www.nexusmods.com/skyrimspecialedition/mods/112902)
 - [Simple Hunting Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/95943)
 - [Modern first-person animation overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/115525)
 - [Rihad Swordsman Set](https://www.nexusmods.com/skyrimspecialedition/mods/120576)
 - [Cities of the North - Dawnstar Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/30885)

### Added

 - [Rihad Swordsman 3BA](https://www.nexusmods.com/skyrimspecialedition/mods/122484)
 - [Follower Dialogue Expansion - Uthgerd the Unbroken](https://www.nexusmods.com/skyrimspecialedition/mods/122487)
 - [Smooth Random Jump Animation - Rework](https://www.nexusmods.com/skyrimspecialedition/mods/59633)
 - [Smooth Weapon Jump Animation](https://www.nexusmods.com/skyrimspecialedition/mods/74748)
 - [Male Argonian Shouts - Revoiced](https://www.nexusmods.com/skyrimspecialedition/mods/44124)
 - [Untarnished UI - Oxygen Meter 2 Patch](https://www.nexusmods.com/skyrimspecialedition/mods/111978)
 - [Apostate Camera Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/122440)
 - [GORE - Fishing (CC) Patch](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=444005&nmm=1&game_id=1704)
 - [MCO-ADXP Rapier moveset](https://www.nexusmods.com/skyrimspecialedition/mods/115295)
 - [Eastern Brassplate 3BA HDT-SMP](https://www.nexusmods.com/skyrimspecialedition/mods/122488)
 - [Fahluaan - Character Presets](https://www.nexusmods.com/skyrimspecialedition/mods/96793)
 - [Just Bite - Sacrilege Dynamic Activation Key Patch](https://www.nexusmods.com/skyrimspecialedition/mods/122597)

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Reduced number of dragon souls needed to progress Stormcrown perk tree. Won't take affect on existing save games unless you use the console commands below.
   - `set MAG_DragonbornNextPerk to 1`
   - `set MAG_DragonbornRequiredSouls01 to 2`
   - `set MAG_DragonbornRequiredSouls02 to 3`
   - `set MAG_DragonbornRequiredSouls03 to 4`
 - Apprentice Carry Weight reduced to 300 (was 500). Not sure if this would take effect on an existing save-game?
   - I felt like Apprentice and Novice weren't meaningfully different, so I am aiming to try and rebalance Apprentice a little bit.
   - Legendary difficulty will be receiving a minor overhaul in some update soon.
 - Reworked NPC Movesets.
 - Dark Magic Talisman nerfed by 20%. Now restores 80 Magicka over 10 seconds instead of 100 Magicka over 10 seconds.
 - Removed some spiders in Bleak Falls Barrow.
 - Adjusted background speech scaling.

### Bug Fixes
 
 - Fixed some incorrect pathing in landscape texturesets.
 - Fixed missing textures on fall forest landscapes.
 - Fixed shader material issue on several ice objects that had parallax.
 - Should have fixed issue with footstep sounds in first person for some stances.
 - Redrew landscape near Mara's Eye Pond.
   - `26 2`
 - Fixed missing textures on Maro's armor.
 - Fixed incorrect water cubemap being used in Goldenglow Estate Sewer.
 - Fixed incorrect water cubemap being used in Soljund's Sinkhole.
 - Fixed incorrect water cubemap being used in the Red Wave.
 - Fixed incorrect Acoustic Space in Volkihar Undercroft.
 - Fixed incorrect Acoustic Space in Volkihar Ruins.
 - Fixed incorrect Acoustic Space in Fort Dawnguard.
 - Fixed incorrect Acoustic Space in House of Clan Battle-Born.
 - Fixed incorrect Acoustic Space in House Gray-Mane.
 - Fixed incorrect Acoustic Space in Radiant Raiment.
 - Fixed incorrect Acoustic Space in Elgrim's Elixirs.
 - Fixed incorrect cell Ownership for the Nightgate Inn.
 - Fixed incorrect cell Ownership for Hollyfrost Farm.
 - Fixed incorrect cell Ownership for Hlaalu Farm.
 - Adjusted floating tree (kinda) near Boethiah's Shrine.
   - `98E78`

### Misc. Changes

 - Jump Animations.
 - Reworked NPC Animations.
   - Separated "Common" and "Boss" NPCs.
   - Added some folders for certain followers to have unique movesets while using their weapon of choice. I will expand this over time when necessary.
   - So what is left?
     - Some more in-depth, faction-specific animations.
     - Some unique bosses.
     - Vigilant and Unslaad bosses aren't quite completed yet.
 - Tweaked Bow Aiming interpolation for default SmoothCam preset.
 - Gave Umana a set of Armor that wasn't just Steel Plate.
 - Gave Salma a set of Armor that wasn't just Steel Plate.
 - Added a new visual for Rallying Standard's buff.
 - Slightly adjusted the positioning of Widgets so there was more spacing between them and the enchantment bar.
 - Changed Magicka bar to be a light blue instead of a dark grey to better differentiate it from Stamina.
   - Old Magicka bar color was `#909090` if you wish to change back.
 - Actually compiled the script to potentially fix the HUD issues during the intro.

</Details>

## 0.4.1

Key Info

 - Not save safe with previous beta versions.
 - This update combines [0.4.0](#040) and [0.4.1](#041). I broke it up like this for easier keeping track of specific changes to the list.
 - Reworked Landscapes, Mountains, Terrain, and graphics setup in order to acheive more consistent blending and attempt to fix snow shader-related issues.
 - Read changelogs for 0.4 and 0.4.1 (recommended).
 - Did HUD customization.

<Details>
<summary>Changes</summary>

### Updated

 - [Cathedral 3D Mountain Flowers - Base Object Swapper](https://www.nexusmods.com/skyrimspecialedition/mods/60756)
 - [Snowy Carts for Snowy Regions](https://www.nexusmods.com/skyrimspecialedition/mods/111575)
 - [Snowy Ships for Snowy Regions](https://www.nexusmods.com/skyrimspecialedition/mods/111827)
 - [Mysterious Mementos - Assorted Artifact Rebalances](https://www.nexusmods.com/skyrimspecialedition/mods/118342)
 - [Vanilla Complex Parallax - Dungeons](https://www.nexusmods.com/skyrimspecialedition/mods/88828)
 - [Vanilla Complex Parallax - Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/88295)
 - [Vanilla Complex Parallax - Clutter and Furniture](https://www.nexusmods.com/skyrimspecialedition/mods/89791)
 - [Skyking Signs](https://www.nexusmods.com/skyrimspecialedition/mods/112902)
 - [Vigilant - Daedroth Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/78704)
 - [I4 Armor Icons Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/119824)
 - [Alternate Perspective - Voiced Addon](https://www.nexusmods.com/skyrimspecialedition/mods/96865)
 - [Static Mesh Improvement Mod Improvement Mod](https://www.nexusmods.com/skyrimspecialedition/mods/55543)
 - [GG's Complex Silverware](https://www.nexusmods.com/skyrimspecialedition/mods/121232)
 - [DynDOLOD DLL NG](https://www.nexusmods.com/skyrimspecialedition/mods/97720)

### Added

 - [Seranade - A(nother) Serana Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/112513)
 - [Setting on Sulphur](https://www.nexusmods.com/skyrimspecialedition/mods/86906)
 - [Atlantean Landscape -Complete- Complex Terrain Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/89542)
 - [Tomato's Complex Landscapes Parallax AIO](https://www.nexusmods.com/skyrimspecialedition/mods/110981)
 - [Riton Landscape](https://www.nexusmods.com/skyrimspecialedition/mods/121614)
 - [Terrain Parallax Blending Fix](https://www.nexusmods.com/skyrimspecialedition/mods/88261)
 - [Tomato's Whiterun - Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/122064)
 - [Static Mesh Improvement Mod - SMIM - Complex Parallax Addon](https://www.nexusmods.com/skyrimspecialedition/mods/117921)
 - [Vanilla Complex Parallax - Dragonborn](https://www.nexusmods.com/skyrimspecialedition/mods/116129)
 - [Vanilla Complex Parallax - Dawnguard](https://www.nexusmods.com/skyrimspecialedition/mods/115474)
 - [Vanilla Complex Parallax - Minor Architecture](https://www.nexusmods.com/skyrimspecialedition/mods/114426)
 - [DynDOLOD The Little Things](https://www.nexusmods.com/skyrimspecialedition/mods/122201)
 - [HD Textures for Solitude and Temple Frescoes](https://www.nexusmods.com/skyrimspecialedition/mods/56341)
 - [Shep's Tattoo Collection SE](https://www.nexusmods.com/skyrimspecialedition/mods/22636)
 - [The Royal Seat - Modular - Solitude Throne](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=499332&nmm=1&game_id=1704)
 - [Dark Brotherhood Sanctuary Decor - The Blood Door](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=237548&nmm=1&game_id=1704)
 - [Valtheim](https://www.nexusmods.com/skyrimspecialedition/mods/94539)
 - Dint999's Face Part mod
 - [Proper Mod-Added Torch Support](https://www.nexusmods.com/skyrimspecialedition/mods/104521)
 - [Customizable Companions Questline Progression Requirements](https://www.nexusmods.com/skyrimspecialedition/mods/78308)
 - [Roggvir's Execution Scene Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/74652)
 - [Thalmor Don't Report To Stormcloaks](https://www.nexusmods.com/skyrimspecialedition/mods/73890)
 - [More Sensible Quartermasters](https://www.nexusmods.com/skyrimspecialedition/mods/73887)
 - [Dynamic injured creature animations - Falmer](https://www.nexusmods.com/skyrimspecialedition/mods/117258)
 - [HelpExtender](https://www.nexusmods.com/skyrimspecialedition/mods/74376)
 - [Fix For Invisible Hud After Helgen Intro with TrueHUD and Alternate Perspective](https://www.nexusmods.com/skyrimspecialedition/mods/79479)
 - [Better Combat Escape - NG](https://www.nexusmods.com/skyrimspecialedition/mods/72901)
 - [TMD Epic Waterfalls](https://www.nexusmods.com/skyrimspecialedition/mods/106210)
 - [Cave Rocks Improved](https://www.nexusmods.com/skyrimspecialedition/mods/120229)
 - [Thuldor's Ivarstead - Farmhouse Roofs](https://www.nexusmods.com/skyrimspecialedition/mods/99624)
 - [Simple Nail Polish](https://www.nexusmods.com/skyrimspecialedition/mods/108077)
 - [BnP - Female Skin](https://www.nexusmods.com/skyrimspecialedition/mods/65274)
 - [BnP - Male Skin](https://www.nexusmods.com/skyrimspecialedition/mods/65402)
 - [DVA - Dynamic Vampire Appearance](https://www.nexusmods.com/skyrimspecialedition/mods/96817)
 - [Wet Function Redux SE](https://www.nexusmods.com/skyrimspecialedition/mods/78804)
 - [Rihad Swordsman Set - HIMBO](https://www.nexusmods.com/skyrimspecialedition/mods/122376)
 - [3D Dwemer Sun - Subterranean Object SMIMed - Blackreach - Forgotten Seasons - Myrwatch](https://www.nexusmods.com/skyrimspecialedition/mods/121858)
 - [3D Dwemer Sun - Subterranean Object SMIMed - Blackreach - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/121906)
 - [Colovian Prince Set](https://www.nexusmods.com/skyrimspecialedition/mods/79894)
 - [Colovian Prince Set - My patches and tweaks SE by Xtudo](https://www.nexusmods.com/skyrimspecialedition/mods/110812)
 - [Colovian Prince Set - HIMBO](https://www.nexusmods.com/skyrimspecialedition/mods/86504)
 - [3BA Colovian Prince](https://www.nexusmods.com/skyrimspecialedition/mods/84230)
 - [Kvetchi Mercenary Set](https://www.nexusmods.com/skyrimspecialedition/mods/79226)
 - [Kvetchi Mercenary Set - My patches and tweaks SE by Xtudo](https://www.nexusmods.com/skyrimspecialedition/mods/110632)
 - [Kvetchi Mercenary Set - HIMBO](https://www.nexusmods.com/skyrimspecialedition/mods/86564)
 - [Kvetchi Mercenary Armour 3BA with HDT-SMP Cloth Physics](https://www.nexusmods.com/skyrimspecialedition/mods/83171)
 - [TMD Epic Waterfalls](https://www.nexusmods.com/skyrimspecialedition/mods/106210)
 - [Rally's Water Foam](https://www.nexusmods.com/skyrimspecialedition/mods/28922)
 - [Beef Unending - A Civil War Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/121332)
 - [ECE Sliders Addon for Racemenu](https://www.nexusmods.com/skyrimspecialedition/mods/75686)
 - [Dovahzul Overlays](https://www.nexusmods.com/skyrimspecialedition/mods/120405)
 - [Overlay Collection](https://www.nexusmods.com/skyrimspecialedition/mods/120581)
 - [moreHUD SE - Legacy Settings Loader](https://www.nexusmods.com/skyrimspecialedition/mods/55503)
 - [Widget Mod](https://www.nexusmods.com/skyrimspecialedition/mods/32387)
 - [Widget Mod - Legacy Settings Loader](https://www.nexusmods.com/skyrimspecialedition/mods/55629)
 - [Elden Ring HUD](https://www.nexusmods.com/skyrimspecialedition/mods/65855)

### Removed

 - [HD Remastered Landscapes - Complex Terrain Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/94835)
   - Stopped using MM/ML.
 - [Atlantean Landscape -Majestic Edition-](https://www.nexusmods.com/skyrimspecialedition/mods/102170)
   - Stopped using MM/ML.
 - [Majestic Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/41857)
   - Bad blending in some spots.
 - [Majestic Mountains Complex Material](https://www.nexusmods.com/skyrimspecialedition/mods/87547)
   - Bad blending in some spots.
 - [Vanaheimr - Mountains](https://www.nexusmods.com/skyrimspecialedition/mods/115471)
   - Stopped using MM/ML.
 - [Complex Markarth Fixed AF](https://www.nexusmods.com/skyrimspecialedition/mods/120316)
   - Stopped using MM/ML.
 - [Stones of Solitude - Majestic Mountains Rocks](https://www.nexusmods.com/skyrimspecialedition/mods/68007)
   - Stopped using MM/ML.
 - [Majestic Landscapes - Patch for Praedy's Soul Cairn Bone Piles](https://www.nexusmods.com/skyrimspecialedition/mods/96933)
   - Stopped using MM/ML.
 - [Better Dynamic Snow 2.11 - Definitive Edition](https://www.nexusmods.com/skyrimspecialedition/mods/112386)
   - Stopped using MM/ML.
 - [Better Dynamic Snow - Definitive Edition Patches](https://www.nexusmods.com/skyrimspecialedition/mods/117954)
   - Stopped using BDS DE.
 - [Pfuscher's Wet Mud Texture](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=396091&nmm=1&game_id=1704)
   - Stopped using MM/ML.
 - [Skyland Whiterun](https://www.nexusmods.com/skyrimspecialedition/mods/13015)
   - Whiterun now uses a mashup of Tomato's and winedave's textures, Skyland isn't needed anymore as a "base coat".
 - [Whiterun City Stone Walls - Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/103239)
   - Tomato's new Whiterun retexture has better walls.
 - [Vanilla Complex Parallax - Whiterun](https://www.nexusmods.com/skyrimspecialedition/mods/88553)
   - Meshes are no longer needed.
 - [PB's 4k or 8k Silky Skin for CBBE](https://www.nexusmods.com/skyrimspecialedition/mods/95818)
   - Swapped skin mod. I am indecisive.
 - [LOVERBOY Male Skin - HD Complexion for Men](https://www.nexusmods.com/skyrimspecialedition/mods/81831)
   - Swapped skin mod. I am indecisive.
 - [Real Dwemer Pipes](https://www.nexusmods.com/skyrimspecialedition/mods/86055)
   - Unneeded.

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Removed Uncommon Taste, Olava's Token, Wedding Dress, Wedding Sandals, Wedding Wreath, Emperor's Robes, Muiri's Ring, and Gilded Wristguards from the reward chest after completing the Penitus Oculatus questline.
 - Increased Companions radiant requirements to progress questline.
 - Standardized Bow Draw Speed.
 - Improved Shadow Stone and Rogue Class proc chance (again).
 - Atronach Stone now allows Magicka regeneration outside of combat.
 - Juggernaut (Heavy Armor) and Specialist (Light Armor) nerfed to +50/100 Armor Rating (was +100/200).
 - Adjusted background Armor scaling.

### Bug Fixes
 
 - Dark Brotherhood Remnant will no longer spawn in the wrong Morthal Inn. (Not tested, should work).
 - Killing Cicero via the Penitus Oculatus questline or in the Dawnstar Sanctuary should now appropriately reward his hat.
 - Actually fixed the offering basket placement in Morthal near the Missive board.
 - Fixed Nirnroots having no sound.
 - NPCs who use bows will no longer have two bows equipped on their back before drawing their weapon.
 - Fixed issue where giant boss of Cradlecrush Rock was flagged to Start Dead, rendering any bounty or radiant quests for the location unfinishable.
 - Fixed Werewolf's Beastblood tooltip to appropriately reflect the changes the list makes.
 - Potentially fixed issue with HUD disappearing and not returning during the intro.
 - Fixed Stonehills occlusion.
 - Fixed subsurface scattering mismatch on male genitals.
 - Fixed a floating Lantern on the Dainty Sload.

### Misc. Changes

 - Made a custom replacer for Serana based off of [Serana Re-imagined](https://www.nexusmods.com/skyrimspecialedition/mods/43430) and using the Hair from [Seranade - A(nother) Serana Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/112513).
 - So much work done on landscapes and mountains...complete overhaul of a lot of environmental textures and assets.
 - Dark Brotherhood Torture Victims now wear Bloody Rags...instead of nothing.
 - Removed ugly Thickets from Dawnstar.
 - Added parallax to the Whiterun dirt roads.
 - Disabled some trees in Whiterun that were prone to clipping.
 - Increased speed for Power Attack 2 for Greatsword Bear by 10% (1.1x speedmult --> 1.2x speedmult).
 - Adjusted racial tooltips for Werewolves.
 - Gave The Caller a unique outfit.
 - Added Armored variants of Magecore equipment.
   - Stalhrim Tier, requires appropriate crafting perks and manual.
 - Adjusted Marsh (Morthal) and Tundra (Whiterun) grass.
 - Combined Wayward Knight and Fleet Knight crafting (and added Gryphonknight) into a single crafting manual - **Bretonic Style**.
   - Renamed "Gryphonknight" to "Gryphon Knight".
 - Did a ton of new outfit distribution.
 - Swapped up some NPC replacers.
 - Built SMP Hair collisions.
 - HUD setup, feel free to give feedback if you have any.

</Details>

## 0.4.0

Key Info

 - Jesus christ I want to be finished with this beta cycle.
 - Redesigned the Alteration perk tree.
 - This version was not released.

<Details>
<summary>Changes</summary>

### Updated

 - [Solstheim Exterior Soundscapes](https://www.nexusmods.com/skyrimspecialedition/mods/121361)
 - [Mehrunes Dagon's Shrine Unlocked - Pieces of the Past Alternate Ending](https://www.nexusmods.com/skyrimspecialedition/mods/119502)
 - [Boethiah's Calling - Alternate Questline](https://www.nexusmods.com/skyrimspecialedition/mods/121499)
 - [Ultimate NPC Dodging](https://www.nexusmods.com/skyrimspecialedition/mods/120738)
 - [GG's Complex Silverware](https://www.nexusmods.com/skyrimspecialedition/mods/121232)
 - [Feris - Custom Voiced Female Follower](https://www.nexusmods.com/skyrimspecialedition/mods/90032)
 - [Vanaheimr - Mountains](https://www.nexusmods.com/skyrimspecialedition/mods/115471)\
 - [KR2's Kaidan NPC Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/103472)
 - [Female Player Animations (OAR)](https://www.nexusmods.com/skyrimspecialedition/mods/85073)
 - [Male Player Animations (OAR)](https://www.nexusmods.com/skyrimspecialedition/mods/89225)
 - [Lux](https://www.nexusmods.com/skyrimspecialedition/mods/43158?)
 - [Lux - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/113002)
 - [Lux Orbis](https://www.nexusmods.com/skyrimspecialedition/mods/56095)
 - [Lux Orbis - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/114169)
 - [AMON ENB REBORN for NAT 3](https://www.nexusmods.com/skyrimspecialedition/mods/99786)
 - [Windhelm Bridge Revived](https://www.nexusmods.com/skyrimspecialedition/mods/84686)
 - [DynDOLOD Resources SE 3](https://www.nexusmods.com/skyrimspecialedition/mods/52897)
 - [Snowy Surfaces Sound Collision and Aesthetics](https://www.nexusmods.com/skyrimspecialedition/mods/76257)
 - [Diverse Witcher Missives Boards - Base Object Swapper](https://www.nexusmods.com/skyrimspecialedition/mods/111770)
 - [Base Object Swapper](https://www.nexusmods.com/skyrimspecialedition/mods/60805)
 - [SmoothCam - SynErgy Preset](https://www.nexusmods.com/skyrimspecialedition/mods/46655)
 - [Maxsu Poise Revise](https://www.nexusmods.com/skyrimspecialedition/mods/117988)
 - [Follower Dialogue Expansion - Lydia](https://www.nexusmods.com/skyrimspecialedition/mods/119226)
 - [Animated Ice Floes](https://www.nexusmods.com/skyrimspecialedition/mods/90634)
 - [JS Dwarven Oil SE](https://www.nexusmods.com/skyrimspecialedition/mods/66770)

### Added

 - [Beast Race Bodypaints SE](https://www.nexusmods.com/skyrimspecialedition/mods/20446)
 - [Skyrim Outfit System SE Revived - Beast Race Disabler](https://www.nexusmods.com/skyrimspecialedition/mods/105841)
 - [Particle Patch - Magic Hand FX](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=511536&nmm=1&game_id=1704)
 - [The Handy Icon Collection Collective](https://www.nexusmods.com/skyrimspecialedition/mods/90508)
 - [ADXP I MCO MGRR Greatsword Moveset for NPC](https://www.nexusmods.com/skyrimspecialedition/mods/107048)
 - [ADXP I MCO MGRR Machete Moveset for NPC](https://www.nexusmods.com/skyrimspecialedition/mods/112802)
 - [ADXP I MCO MGRR Warhammer Moveset for NPC](https://www.nexusmods.com/skyrimspecialedition/mods/112803)
 - [Rihad Swordsman Set](https://www.nexusmods.com/skyrimspecialedition/mods/120576)
 - [Rihad Swordsman Set - My patches SE by Xtudo](https://www.nexusmods.com/skyrimspecialedition/mods/122125)
 - [Look Around - Searching Animations For NPCs](https://www.nexusmods.com/skyrimspecialedition/mods/79958)
 - [Smooth Staff Animation](https://www.nexusmods.com/skyrimspecialedition/mods/54883)
 - [Dragon Breath VFX Edit](https://www.nexusmods.com/skyrimspecialedition/mods/118431)
 - [Dwemer Pipework Reworked](https://www.nexusmods.com/skyrimspecialedition/mods/46507)
 - [Golden Dwemer Pipeworks Redone](https://www.nexusmods.com/skyrimspecialedition/mods/67114)
 - [Lux - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/91312)
 - [Golden Dwemer Pipeworks Redone - Unofficial Update](https://www.nexusmods.com/skyrimspecialedition/mods/94440)
 - [Golden Dwemer Pipeworks - Patches](https://www.nexusmods.com/skyrimspecialedition/mods/78424)
 - [Markarth Fixed AF - Golden Dwemer Pipeworks Redone FULL Patch](https://www.nexusmods.com/skyrimspecialedition/mods/85536)
 - [Dwemer Armor SE - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/87080)
 - [Vanilla Dwarven Armour and Weapon - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/87332)
 - [Katana Crafting - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/87588)
 - [Dwemer Automatons - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/87692)
 - [Spear of Skyrim - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/90625)
 - [Aetherial Crown SE - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/91404)
 - [Sconces of Solstheim - Improved DLC2 Braziers - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/95240)
 - [Goblins and Riekrs- Mihail Monsters and Animals (SE-AE version) - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/95254)
 - [Sharpen Other Swords II - AnimObject Swapper2 - GDPR Patch](https://www.nexusmods.com/skyrimspecialedition/mods/96336)
 - [ENB Particle Lights - Dwemer Lanterns - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/97141)
 - [Sons of Skyrim 2.0 - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/104366)
 - [Splendid Mechanized Dwemer Door from GDOS - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/107793)
 - [Markarth Silver Blood Inn Door - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/107796)
 - [Eastern Brassplate Set - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/109628)
 - [My Aching Back - Mattresses for Dwemer Beds - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/113724)
 - [Security Overhaul SKSE - Lock Variations - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/113901)
 - [Security Overhaul SKSE - Regional Locks - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/113900)
 - [Unique Markarth Doors - Security Overhaul SKSE - Base Object Swapper - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/115844)
 - [Praedy's Staves - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/118824)
 - [ElSopa - Quivers Redone - Golden Dwemer Pipeworks Redone Patch](https://www.nexusmods.com/skyrimspecialedition/mods/120408)
 - [Nightgate Inn Revived](https://www.nexusmods.com/skyrimspecialedition/mods/121244)
 - [Alternate Perspective - Solstheim Start Fix](https://www.nexusmods.com/skyrimspecialedition/mods/112709)
 - [Serana Dialogue Add-On](https://www.nexusmods.com/skyrimspecialedition/mods/32161)
 - [Serana Dialogue Add-On Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/70782)
 - [Serana Dialogue Add-On - Pilgrim Patch](https://www.nexusmods.com/skyrimspecialedition/mods/73135)
 - [Daedric Shrines - Mehrunes Dagon - Vanaheimr](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=511743&nmm=1&game_id=1704)
 - [Jarl Balgruuf Dilemma SSE](https://www.nexusmods.com/skyrimspecialedition/mods/41132)
 - [Serious Civil War Consequences for Jarl Balgruuf](https://www.nexusmods.com/skyrimspecialedition/mods/81554)
 - [Hotkey Reminder](https://www.nexusmods.com/skyrimspecialedition/mods/115853)
 - [aljo's Sorcerer Patches](https://www.nexusmods.com/skyrimspecialedition/mods/95219)

### Removed

 - [Improved Alternate Conversation Camera](https://www.nexusmods.com/skyrimspecialedition/mods/68210)
   - Buggy.
 - [Golden Ship Model Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/91221)
   - Redundant.
 - [Ancient Automatons](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=1000213503&nmm=1&game_id=110)
   - Changed Dwemer Metal retexture.
 - [Ancient Dwemer Metal](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=1000213510&nmm=1&game_id=110)
   - Changed Dwemer Metal retexture.
 - [Ancient Dwemer Metal - My patches](https://www.nexusmods.com/skyrimspecialedition/mods/38845)
   - Changed Dwemer Metal retexture.
   - Removed several patches from this mod page I will not be listing out for sanity.
 - [Goblins and Riekrs - ADM patch](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=404289&nmm=1&game_id=1704)
   - Changed Dwemer Metal retexture.
 - [SOS V2.0 - SE by Xtudo - ADM Desaturated](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=440443&nmm=1&game_id=1704)
   - Changed Dwemer Metal retexture.
 - [Spaghetti's Towns - Nightgate Inn](https://www.nexusmods.com/skyrimspecialedition/mods/89287)
   - New overhaul for the area.

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Redesigned the Alteration perk tree.
 - Nerfed Mimic level scaling.
 - Nerfed Mimic damage.
 - Mimics are now weak to Poison (50%).
 - Disabled Draugrs spawning from static draugr corpses.
 - Attacks now hit up to 3 targets (was 5).
 - Power Attacks now cleave up to 5 targets.
 - Dropped the chance that NPCs have potions from 40% to 30%.
 - Improved Shadow Stone conditional proc chance.
 - Patched Gore for Gourmet and Apothecary.
 - Bound Weapons are now Apprentice-level. Bound Dagger remains as Novice.
 - Completely reintegrated Rare Curios.
 - Revamped Bandit level lists.
 - Tier 1 Talismans now require 8 refined essences to create (was 10).
 - Tier 2 Talismans now require 10 refined essences to create, in addition to their previous requirements.

### Bug Fixes
 
 - Fixed Atronach Stone's tooltip.
 - Disabled two vanilla road chunks near Solitude and Dragon Bridge that were missed by Northern Roads.
   - `68854` and `C3933`.
 - Re-enabled RoadSignPost near Dragon Bridge Kynareth Statue.
 - Correct erroneous **OR** check on some crafting recipes that caused them to be available prematurely (e.g. Lunar Guard).
 - Repainted cells near Morthal.
   - `-9 13` and `-9 14`
 - Patched landscape gap near Whiterun.
   - `4 -2` and `4 -1`
 - Repainted cells near Loreius Farm.
   - `8 2`, `8 3`, `9 2`, `9 3`
 - Fixed Level-Up menu still saying "Lockpicking" and "Pickpocket" instead of "Hand to Hand" and "Security", respectively.
 - Apprentice Stone now correctly "randomly" reduces spell cost.
 - Potentially fixed issue where NPCs would drop "NPC Fear Potion".
 - Fixed horrible z-fighting and texture flickering issues in Windhelm.
 - Moved Well of the Void near Winterhold so it wasn't *slightly* floating off the ground anymore at some angles.
 - Adjusted the scale of a snow pine tree in Hob's Fall Cave that was clipping into the draw bridge.
 - Removed XP exploit for finding NPCs in the College.
 - Fixed Landscape issue in Morthal.
   - `-11 16`, `-11 15`, `-10 16`
 - Fixed Eclipse Mage SMP on female actors.
 - I think I finally fixed the issue where you can get stuck in the block animation?
 - Fixed tempering suffixes being wrong.
 - Arcane Enchanter in Wuth Rein player home no longer clips into shelf.
 - You can no longer swap between Stances in Werewolf or Vampire Lord form (not that it did anything anyways).
 - Fixed Steel Plate Boots missing GND and Inventory model.
 - Clearspring Tarn is now clearable.
 - Fixed bounds issue in White River Watch that caused some Cave Statics to become invisible. (Thanks Feli for reporting this and thanks GG for fixing it).
 - Added a NavCut near `POITundra05` to prevent enemies getting stuck on rocks in the area.
   - `1,2` for ref `c9d04`.
 - Removed some floating crows near the Abandoned Shack. I would've repositioned them but my CK crashed when loading the meshes so idk.
 - Adjusted a Thistle (`A1857`) and repainted border of cells `1, -16` and `0, -16`.
 - Honey no longer includes the fact that it cures Poisons and Diseases on the tooltip. I will eventually rework the Werebear perk that adds this feature.
 - Killmove Toggle in Apostasy MCM should now appropriately disable Ranged killmoves (Magic and Bows). **Not tested**.
 - Fixed Candle and Magelight being useless (thanks Anehum for confirming my fix).
 - Tarek Serano will no longer bug out after being defeated in the `But You Have Heard of Me` quest.
 - Fixed double staves inventory bug.
 - Repainted landscape to cover up seam near Anga's Mill and Windhelm.
   - `26 7` and `26 6`
 - Disabled tree near Raldbthar `3B62B`.
 - Disabled tree near Dark Brotherhood Sanctuary `0x44FEAC~Nature of the Wild Lands.esp`.
 - Fixed bodies not being draggable.
 - Adjusted placements of items in Mehrunes Dagon Shrine so stuff wasn't floating in mid air.
 - Missive Boards should now be properly swapped with their regional variants.
   - Reverted Base Object Swapper to [version 2.6.1](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=421727&nmm=1&game_id=1704).

### Misc. Changes

 - Removed Fleet Knight Variants test chest.
 - Reverted NotWL's change to `TreeDriftWood01` as it looked out of place in many areas.
 - Improved Shadow Stone visual FX.
 - Changed default Nord F Preset to not look ugly.
 - Started distributing some movesets to Vigilant NPCs.
 - Removed some environmental clutter added by Auri near Riften Docks.
   - `41 -25` and `40 -25`.
 - Added I4 Icons for Racial Bonuses and Standing Stone Bonuses.
 - Created a custom SmoothCam preset for the list and fixed the dialogue camera. Please give feedback.
 - Tweaks to ENB, including custom interior inis.
 - Tweaked Thieves Guild Quest Requirements and added Documentation for them under the [Quest Changes](https://github.com/Oghma-Infinium/apostasy/blob/main/GAMEPLAY.md#quests-changes) section of the Gameplay Guide.
 - Changed the wording on Unhindered (Light Armor), Unstoppable (Heavy Armor), and the Tower Stone to be more consistent with other buffs that reduce incoming poise damage.
 - Reduced the weight of Dragon Scales to 3 (was 10) and the weight of Dragon Bones to 6 (was 15).
 - Persistentified `Taarengrav.esp` and `MorthalBarrow.esp`.
 - Attempts have been made to appeal to the straight male audience in the same way I have appealed to the gay woman audience.
 - Removed start room markers.
 - Added keybinds for Restore Stamina and Restore Magicka Potions (`Shift+F` and `Ctrl+F` respectively).
 - Shrine of Mehrunes Dagon is properly Lux patched now.
 - Patched Val Serano's Warm Candlelight spell to be more similar to other variants.

</Details>

## 0.3.1

Key Info

 - Save-Safe. Just remove and re-get your Standing Stones so they update appropriately.
 - Revamped Standing Stones.
 - Im too tired to write the rest of this changelog, just read the notes below.

<Details>
<summary>Changes</summary>

### Updated

 - Boethiah's Calling - Alternate Questline
 - Tales of Skyrim - Berserkyr
 - Tales of Skyrim - Berserkyr Patch Collection
 - Animated Ice Bergs
 - Vanilla hair remake
 - Animated Ice Floes
 - Revenant Spirits of the Soul Cairn
 - Falkreath Gravestone Diversity - Base Object Swapper
 - powerofthree's Tweaks
 - Alternate Perspective - Alternate Start

### Added

 - Papyrus Ini Manipulator
 - JS Shout Apart Skeletons SE
 - Falmer Servant Lines Expansion
 - Magic Casting Utilities
 - Shout Recovery Utilities
 - Safety of Skuldafn - Railing and Small Fixes
 - Solstheim Exterior Soundscapes
 - Sonorum Arcana - The Magic Sound Compendium
 - Sorcerer Combat Animation* (NYI)
 - QuickLoot EE - Settings Loader
 - Player Name Randomizer
 - Player Name Randomizer - Show in UI
 - Patrons Menu* (NYI)

### Removed

 - Paper UI Sounds for Skyrim
 - Servitor - Atronach SFX Replacer

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Revamped Standing Stones.
 - Gave the player 25% resistance to incoming Stagger during power attacks.
 - Increased base poise Health by 50%.
 - Decreased base poise damage of melee weapons by 50%.
 - Decreased base poise damage of ranged weapons by 25%.
 - Removed Tree in front of Embershard Mine that bandits were constantly getting stuck on.
 - You can no longer jump when you do not have enough Stamina (10).
 - Did some background adjustments to the damage formula for the Ravage, Devastate, Overwhelm, Rip and Tear, and Carve and Spit perks.

### Bug Fixes
 
 - Fixed One With the Pack (Speech) having an incorrect tooltip based on an earlier design of the perk.
 - Martyrdom (Heavy Armor) now actually works (previously only worked == 50% Health and not <= 50% Health>). 
 - Nerfed Martyrdom from 250% Reflect to 200% Reflect.
 - Untouchable (Light Armor) received the same fix as Martyrdom.
 - Fixed compile issue that caused the Vigilant Rebalance to be missing from the list.
 - Removed Rim Lighting from Companion Armor 2.
 - Fixed inconsistent map marker coloration.
 - Fixed issue with unknown locations on compass appearing as quest markers.
 - Improper WeapType sorting in inventory (i.e. Katanas being classified as War Axes) will be fixed in a future version. The issue was addressed with the relevant authors.
 - Scarves and Mufflers should have gnd and inventory models now. ~~I did not test this fix.~~ Fix confirmed by Anehum.
 - Added vertex coloring to `bridgerowboat02anim.nif` and `bridgerowboat03anim.nif`, hopefully this fixes broken parallax. ~~(Did not test).~~ Fix confirmed by Anehum.

### Misc. Changes

 - Added a SkyUI MCM config that *may* improve item positioning in inventory for ultrawide (21:9) users. Let me know if things are better.
 - Adjusted the shape of the Light Armor and Smithing trees.
 - Increased Precision Capsule length for first person.
 - Tweaked Extended Encounters MCM.
 - Changed sourcing for certain files, should reduce Wabbajack file size.
 - Added MenuMain to ScriptClassExclusions of PapyrusTweaks.
 - Swapped to Papyrus version of [Dynamic Activation Key](https://www.nexusmods.com/skyrimspecialedition/mods/96273) since some crashes appeared to be linked to the DLL version.
 - Added some mods I will implement in the future.
 - Swapped some tree models.
 - Travelling Priest gear is now crafted at a forge instead of a tanning rack.
 - I think I fixed map markers being inconsistently colored.

</Details>

## 0.3.0

Key Info

 - This update was going to be save safe, but I decided to implement more stuff than just fixes.
 - Recovery Annotations now work (I'm stupid).
 - Added missing Timed Block sound.
 - Implemented advanced difficulty edits. Read more [here](https://github.com/Oghma-Infinium/apostasy/blob/main/GAMEPLAY.md#difficulty).
 - Implemented Attacks of Opportunity. Read more [here](https://github.com/Oghma-Infinium/apostasy/blob/main/GAMEPLAY.md#attacks-of-opportunity).
 - Implemented Massive Targets. Read more [here](https://github.com/Oghma-Infinium/apostasy/blob/main/GAMEPLAY.md#massive-targets)
 - Enemies now have a chance to spawn with potions and use them.
 - NPCs are now able to dodge. Please give feedback on this mechanic.
 - Added Controller Configuration (thanks ylik).
 - Reworked Stagger system.
 - You can no longer be staggered during a timed block (unless hit by an attack that does so much Poise Damage it goes through 99% Stagger Resistance lol).
 - Poise Health can now be seen with TrueHUD's special bars.
 - Greatly increased skill point gains per level.
 - Fixed Bloodskal Blade.

<Details>
<summary>Changes</summary>

### Updated

 - Fleet Knight Set
 - Stances NG
 - Foamimi's Orlando Visual Overhaul
 - Snazzy Interiors Patch Collection
 - Revealing Rune
 - DynDOLOD 3.00
 - MaxsuPoiseRevise
 - Dynamic Activation Key
 - Rally's Mods - Shibui Skyrim Recolor
 - NPCs Learn to Aim (Skill-Based Aiming)
 - powerofthree's Tweaks
 - Vanaheimr - Mountains
 - Follower Dialogue Expansion - Jenassa
 - Follower Dialogue Expansion - Jordis the Sword-Maiden
 - Follower Dialogue Expansion - Brelyna Maryon
 - Follower Dialogue Expansion - Mjoll the Lioness
 - Animated Ice Floes
 - DynDOLOD output
 - TexGen output
 - Grass output
 - Bodyslide output
 - CDN Output

### Added

 - Vanilla Eating Animation Fixes
 - Immersive Carcass Carrying
 - Better Two-Handed Axe Position - IED-OAR
 - Immersive Better Bow Positioning - IED-OAR
 - Grass Cache Helper NG
 - MCO Universal Support
 - Skyrim Outfit System SE Revived
 - Smart NPC Potions - Enemies Use Potions and Poisons
 - Smart NPC Potions - Enemies Use Potions and Poisons - Settings Loader
 - Ultimate NPC Dodging
 - lrh9's Fixes and Patches
 - Universal (SKSE) Rim Lighting Fix
 - Snazzy Honningbrew Meadery
 - Snazzy Interiors - Morvayn Manor
 - Silver Objects SMIMed - Silver - Sovngarde - Thieves Guild - Vampire
 - H.I.T.S. - Hands Itch To Steal - A Silverware Worthy Of The Nords
 - GG's Complex Silverware
 - Better AltTab
 - Bloodskal Weapon art - MCO fix and Artifact remake
 - Extended Encounters
 - Wandering Merchants - Skyrim and Solstheim
 - Animated Ice Bergs
 - RS Children - Gore - A Companion Mod
 - Tales of Skyrim - Berserkyr
 - Tales of Skyrim - Berserkyr Patch Collection
 - Tales Of Skyrim - Berserkyr - 3BA Conversion
 - Tales of Skyrim - Berserkyr Armor (HIMBO V5 Refits)
 - Hand placed enemies - Light
 - Boethiah's Calling - Alternate Questline
 - Mehrunes Dagon's Shrine Unlocked - Pieces of the Past Alternate Ending - Voiced

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Alchemist now increases potion and poison strength by 50/100%. (was 25/50%).
 - Solvency now increases poison strength by 25%. (was 50%).
 - Potency now increases potion strength by 25%. (was 50%).
 - Removed two Nord Hero Sword spawn from Bleak Falls Barrow. Replaced with Ancient Nord Sword spawns.
 - Removed a Nord Hero Battleaxe spawn from Bleak Falls Inner Sanctum. Replaced with a Honed Ancient Nord Battleaxe spawn.
 - Reworked Poise Health formula.
 - Heavy Staggers can only be inflicted by power attacks and power bashes now.
 - Rebalanced some item stats from NordWarr's Sons of Skyrim mod.
 - Adjusted Background Armor Scaling. 
   - A full set of (untempered) Daedric Armor (without a shield) will now give 500 Armor @ 100 Heavy Armor and all relevant Armor boosting perks (excluding Rallying Standard).
   - A full set of (untempered) Dragonscale Armor (without a shield) will now give 400 Armor @ 100 Light Armor and all relevant Armor boosting perks. 
 - Edgerunner now slows time by 50% for 5 seconds. (Was 20% slow time for 3 seconds with a 20% movement speed buff).
 - Scaling changes for lockpicking (will only take effect on a new game).
 - Starting skill level bumped to 10. (was 5).
 - Class Changes:
   - Prisoner now starts with Flames and Healing.
   - Witch Hunter moved to Stealth classes.
   - Witch Hunter now has Sneak as a minor skill. (was Light Armor).
   - Witch Hunters now start with robes, instead of Light Armor.
   - Witch Hunters now start with Conjure Familiar spell.
   - Bandit has been replaced with Barbarian. Barbarians gain Berserker's Frenzy ability, causing them to spend 20% less Stamina when power attacking, drawing a bow, jumping, or sprinting.
   - Soldiers now has Heavy Armor as a minor skill. (was Light Armor).
   - Soldiers now start with Heavy Armor and an Iron Shield, instead of Light Armor and a Hide shield.
   - Battlemage now gains Magicka Battery. Magicka Battery causes melee attacks to restore Magicka while under the effects of an armor spell.
   - Hero now gains Himmel's Resolve. Himmel's Resolve grants resistance to incoming poise damage and causes you to deal additional poise damage to enemies.
   - Rogue now gains Opportunist. Opportunist provides a chance to become intangible (ethereal) during incoming melee attacks, you deal more damage while intangible.
   - Monk now gains Attenuation. Attenuation gives your unarmed attacks a chance to deal additional elemental damage, scaling with your elemental resistance.
   - Mage's Arcane Affinity no longer reduces enchantment cost.
   - Sorcerer's Pact Binding no longer debuffs you when you do not have an active summon.
   - Pact Binding renamed to Binding Vow.
 - Increased skill point gains per level after I did the math and realized that my skill gains were ~50% of Fahluaan's.
 - Nerfed Serana and Valerica.
 - Argonians now increase Armor Rating by 100 instead of 50% Faster Health Regeneration. This change was made primarily due to the Heal Rate buff being too strong but also too weak due to the Health Scaling difficulty changes.
 - Increased enemy density.

### Bug Fixes

 - `bingus hates spiders.esp` no longer incorrectly masters The Contest CC. (Thanks Mgde12).
 - Fixed mipmaps on several grass types. Thinner grasses should no longer visually disappear at a distance.
 - Spears will now correctly use Polearm animations instead of mistakenly using Battleaxe animations.
 - Cleaned up minor landscape seam outside of Riverwood, cell border `5,-11` and `6,-11`.
 - Cleaned up minor landscape seam outside of Whiterun, cell border `4,-1` and `3,-1`.
 - Adjusted Navcuts and Collision boxes near Honningbrew Meadery, cell `7,-5`.
 - Timed Blocks will now have their intended sound effect.
 - Reinstalled `Rally's Candlelight and Magelight Fix` with Mysticism patch.
   - Kinda sorta fixed Magelight putting off no light.
 - Ma'zaka's face is no longer devoid of all his features.
 - Disabled floating static in Blue Palace kitchen.
 - Fixed missing Barkeeper shirt mesh.
 - Disabled some trees clipping into the Shrine of Magus in Falkreath.
 - Fixed floating basket in Morthal that should've been near the Missive board.
 - Removed a clipping Juniper tree near Old Hroldan, cell `-29,-2`.
 - Fixed Face Sculptor interaction.
 - Fixed rogue master on arachnophobia addon.
 - Adjusted positioning on Gourmet Tables in The Frozen Hearth, Braidwood Inn, and Windpeak Inn.

### Misc. Changes

 - Disabled Movement during unpaused menus. May change in the future.
 - Preconfigured IED.
 - Replaced more `_sk.dds` files with proper maps for the ENB.
 - Recovery Annotations should work properly now, oops.
 - Added crafting recipes for all new Fleet Knight pieces and variants.
 - Removed "Left Hand Toggle" from Apostasy MCM since it didn't do anything.
 - Assigned Saadia a bodyslide preset.
 - Removed some clipping flora in Whiterun.
 - Disabled notification that occured when drinking potions.
 - Spell tomes are no longer automatically consumed when interacting with them for the first time.
 - Unknown locations are now shown with a "?" marker on the compass before discovery. Previously, unknown locations did not appear on compass.
 - Units on compass are now in metric standard. Previously, was imperial.
 - Reran SynHPH patcher because it was still built off an old version of the list and caused some issues with Races. oops.
 - Wheeler now uses the same font as the rest of the UI.
 - New armor distributions to some named stronghold orcs. Standardized Orc Chief gear.
   - Will not take affect on existing saves if the NPCs have already been met.
 - Included edited version of OneClickPowerAttack.dll to make Power Bashes work more reliably. (Thanks Styyx).
 - Removed Clover and Fern grass from Pine Forest grass. This change will not be visible in game until I regenerate the list's Grass Cache.
 - Yeeted low quality snow grass. This change will not be visible in game until I regenerate the list's Grass Cache.
 - Actually patched FleshFX.
 - Re-did the downscale on some folkvangr grass because ylik complained about my downscale being bad.
 - Removed unspecified entity Statue near Riverwood.
 - Difficulty will no longer correctly scale tooltips (this is how it works in Vanilla). It was incredibly difficult to maintain and I realized that I had multiple exceptions that I was not happy about. I may bring this back in the future, but not now.
 - Changed Reach Shrub and Reach Bush meshes.
 - Reduced Ice cracking sound near ice floes and icebergs.
 - Reduced Standing Stone ambient sounds.
 - Regenerated Grass Cache, TexGen, and DynDOLOD.
 - Rewrote flavor text for all Races in RaceMenu.
 - Fleet Knight and Wayward Knight color variants are now appropriately named.

</Details>

## 0.2.0

Key Info

 - Not save-safe (probably).
 - Mostly just caught up on first round of bug reports from beta cycle.
 - Recleaned several plugins to fix UDRs.
 - ESL flagged mods that could be.
 - Added first-person stance support.
 - Added NPC Obscurity and Generic Naming.
 - Overhauled Solstheim landscape textures (some LOD might mismatch now, I will regen later into the beta cycle after more NG testings).
 - **EXPERIMENTAL** Disabled OBody Performance Mode as it was seemingly causing FPS issues and crashes when loading a high number of NPCs.
 - Next update I will work on UI and HUD.

<Details>
<summary>Changes</summary>

### Updated

 - Grab And Throw
 - Static Mesh Improvement Mod Improvement Mod
 - Destroy The Dark Brotherhood - Quest Expansion
 - Innocence Lost - Quest Expansion
 - Better Third Person Selection - BTPS
 - Spriggans SE
 - Draugr Unarmed Attack Animation
 - Toggle UI (SKSE Plugin)
 - CBBE 3BA Vanilla Outfits Redone
 - Feris - Custom Voiced Female Follower
 - Open Animation Replacer
 - Actor Value Generator
 - Poisoner's Aid
 - Silver Armor and Weapons Retexture SE
 - Dragon Priests Retexture SE
 - NPCs Learn to Aim (Skill-Based Aiming)
 - BFCO-MCO Pickaxe moveset
 - Particle Patch
 - Stances NG
 - Animated Ice Floes
 - hdt smp female amulets and necklaces vanilla replacer
 - Dragon War - A Dragon Overhaul
 - Bjorn - Fully Voiced Follower

### Added

 - Crafting Camera Fix
 - EVG CLAMBER - Slope Animations
 - New Game Sound on Continue (SKSE)
 - Clean KillCam
 - Wait Menu Redirected
 - HDT - Khajiit Alfiq Patch
 - Revealing Rune
 - Female Bosmer Normal Map Fix
 - PB's 4k or 8k Silky Skin for CBBE
 - Bijin Skin UNP and CBBE SE
   - Used for tint masks.
 - Icy Windhelm - Lux Orbis Patch
 - NPCs Names Distributor
 - Daedric Names
 - Reachmen Tribes Names
 - Tamrielic Names
 - Dovah Names
 - Alternate Obscuring Names for NPCs Names Distributor
 - Comprehensive First Person Animation Overhaul - CFPAO
 - Modern first-person animation overhaul
 - KG Animations - Two-handers
 - Stances based animations for 1st person combat
 - First Person Combat Animations Overhaul 2.0 -SIZE MATTERS
 - Skyrim Souls RE - Updated
 - Skyrim Souls RE for Skyrim 1.5
 - Blurbs of Skyrim
 - Main Menu Customizer
 - Feminine Khajiit Textures
 - Masculine Khajiit Textures
 - CBBE Unholy Tattoos
 - Remove Ash Pebbles
 - GG's Temple of Kynareth

### Removed

 - Bows Don't Creak SE - Bow Draw Sound Replacement ISC Edition
   - Redundant
 - Apothecary - Vanilla Potion Restore
   - Redundant.
 - LOVERGIRL Skin - HD Complexion for Women
 - Stones of Barenziah Quest Markers
   - Redundant.

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - None.

### Bug Fixes

 - Fixed Stance issue for Player.
 - Fixed alchemy scaling for Restore Health/Magicka/Stamina potions.
 - Fixed candles clipping into Arcadia's Cauldron's Alchemy table.
 - Potentially fixed getting stuck in block after some key combinations due to BlockStop never being sent.
 - Removed floating Brazier in cell `-24,-6`.
 - Fixed landscape seam near Ivarstead, in cell `19,-17`.
 - Fixed landscape seam in Morthal, in cell `-9,15`.
 - Fixed invisible M'aiq.
 - Removed parallax from a section of the `NorCatHallSm3way01.nif` mesh to reduce warping.
 - Potion of Ultimate Stamina now properly restores health over time.
 - Corrected ownership of crops for Cowflop Farm.
 - Corrected ownership of crops for Lemkil's Farm.
 - Corrected ownership of crops for Corpselight Farm.
 - Fixed missing textures on `DLC1TreeWinterAspenSnow01`, `DLC1TreeWinterAspenSnow03`, and `DLC1TreeWinterAspenSnow05`.
 - Fixed incorrect models on most soul gems.
 - Removed partially floating tree in cell `-4,-21`.
 - Shrine of Jyggalag near Shriekwind Bastion is now interactible.
 - Fixed hole in Shriekwind Bastion.
 - Should have fixed invalid font issue with some apostrophes (blame Google Docs).
 - Silver necklace should now be silver. (I don't know if this was actually a bug but it appears to be silver in my game so idk.)

### Misc. Changes

 - Re-organized Audio section of MO2.
 - Re-organized the User Interface section of MO2.
 - Patched new Security and Hand to Hand skill books for BCS.
 - Removed redundant Cultist and Pilgrim perks from the Conjuration and Restoration skill trees.
 - Adjusted tooltip of "Cheap Shot" to sound more natural.
 - Redid NPC Attack Animations again.
 - Removed Shrine of Nocturnal from Breezehome.
 - Changed skin mod due to bad blending with the previous skin.
 - Removed Winter Aspens from Raven Rock.
 - Removed some drift wood clutter from Raven Rock.
 - Started work on the OBody Config.
 - Disabled OBody performance mode, hopefully this doesn't have any long term repercussions. 
 - Edited subsurface texture for goam's elven ears.
 - Adjusted `pickaxe mco npc` OAR priority to remove meaningless warning in OAR menu.
 - Added support for first person stances.
 - Adjusted several invalid cell editor ids.
 - Removed some candles clipping into the Alchemy Station in the Temple of Kynareth.
 - Adjusted some previously floating plants in Falkreath. 
 - ESL flagged the following mods:
   - `FastTravelSpeedMultiplier.esp`
   - `Subtler Nirnroot.esp`
   - `aptrgangr.esp`
   - `VanillaArgoniansRedux.esp`
   - `Lion's Mane.esp`
   - `HornsAreForever.esp`
   - `ArgonianWeightSliderAffectedTails.esp`
   - `VWA_VanillaWarpaintsAbsolution.esp`
   - `slordars_body_freckles.esp`
   - `FMS_FemaleMakeupSuite.esp`
   - `Wolfpaint_Face.esp`
   - `AK_RM_PubicStyles_All_In_One.esp`
   - `SFO_SkinFeatureOverlays.esp`
   - `BarbarianPaints.esp`
   - `CommunityOverlays1_0T30.esp`
   - `CommunityOverlays2_31T50.esp`
   - `CommunityOverlays3.esp`
   - `Lupine_YyvengarBodypaints.esp`
   - `Lupine_ZiovendianBodypaints.esp`
   - `Hellish Hounds.esp`
   - `Realistic Treeline.esp`
   - `JiubQuestMarkers.esp`
   - `GQJ_DG_vampireamuletfix.esp`
   - `ATIB.esp`
   - `Sacrilege - Fishing Compatibility Patch.esp`
   - `Skyking Signs - RedBags Falkreath Patch.esp`
   - `USSEP - The Great City of Solitude Patch.esp`

</Details>

## 0.1.1

Key Info

 - Fixed compilation issue that made the modlist require Ghost of the Tribunal CC.
 - Fixed compilation issue which caused Wabbajack to ignore specific list outputs that I had disabled for previous test compiles.
 - Moved my control map out of overwrite so Wabbajack would actually include it in the compile (oops).
 - Changed file sourcing for Valor's DLL so it should no longer require a github account to download the list.
 - Distributed Magecore and Wild Witch crafting manuals to Radiant Raiments.
 - Fixed NPC t-posing issues.
 - Enabled the Stagger animations that I forgot to include in the previous version.
 - **EXPERIMENTAL** Disabled Cell Buffer. Hopefully this fixes some crashes.
 - **EXPERIMENTAL** Tweaked the stagger system as staggers felt too weak and inconsistent. Please give me feedback on this.

<Details>
<summary>Changes</summary>

### Updated

 - Dragon War - A Dragon Overhaul
 - Lurking Menace - A Mimic Mod
 - Follower Dialogue Expansion - Jenassa
 - Open Animation Replacer - Detection Plugin

### Added

 - Amon - SK Fix All in One
 - Maxsu Poise Revise
 - SpellSword Moveset
 - Precision Trail Replacer - Simple

### Removed

 - Precision Default Weapon Trail Replacer - Smoother and Elden Ring Style

</Details>

<Details>
<summary>Patch Notes</summary>

### Balance

 - Changed Restore-type Potions to restore over 4 seconds (instead of instant), this should allow Potions to still feel good when being used while allowing them to still scale with Potion Duration effects.
 - Mimics should now spawn less and should spawn more intelligently based on location.
   - Mimics may be nerfed in the future depending on feedback.

### Bug Fixes

 - Fixed alpha blending issue with blood decals.
 - Rebuilt NPC combat folders to fix t-posing issues when enemies wielded certain weapon types and combos.
 - Fixed Crushing Blow and Shattering Strikes not mentioning the relevant Stance in tooltip.
 - Fixed Mortal Wounds improperly mentioning "One-Handed" in the tooltip when it should have been "Two-Handed".
 - Adjusted z-axis of reference `C2CAC` in Helgen.
 - Actors should no longer be roleplaying the hunchback of notre dame while riding a horse.
 - Potentially fixed issue where player could get stuck in block animation after block canceling.
 - Fixed some improper idle animation conditions.
 - Corrected Embers fire in Breezehome that was using vanilla location.
 - Fixed gap between stairs and terrain in Tamriel world cell `-17, -4`.
   - Repainted that entire cell and neighboring cells as well.
 - Removed incorrect alpha property on `rockpilel03moss.nif`. (Thanks ylik)

### Misc. Changes

 - Disabled Auto-Potion system (Health potions can still be quick accessed with the `F` key).
 - Swapped SmoothCam shoulder Toggle to `M5` since it was conflicting with the Crouch bind (`C`).
 - Added a temporary subsurface scattering "fix" until Bingus and I have time to adjust ENB SSS more.
 - Swapped Precision trail mesh to make Ylik happy.

</Details>

## 0.1.0

Key Info

 - Initial Release.
 - Closed Beta.