![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.webp)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  Gameplay Guide |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md">FAQ</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/ADDONS.md">Addons</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

## Initial Setup

Before reading this guide, please follow the [Installation Guide](https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md) as it will answer the vast majority of technical questions related to getting the list setup and running. Be sure to check out the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md) page to learn more about the optional tweaks and addons and MCM options.

## Basics

This section will cover the absolute basics of the list. I suggest reading, or skimming all of the linked mod pages in this section if you are unfamiliar with the preceding mods.

Before reading this section, I suggest looking over the [load order](https://loadorderlibrary.com/lists/Apostasy) and [keybinds](https://github.com/Oghma-Infinium/Apostasy/blob/main/images/Keybinds.png).

### Core Mods

 - TBA

### Leveling and Progression

Apostasy modifies the vanilla leveling experience in a way to reward the player for engaging in the world in sensible ways. While perks can be obtained through leveling, the perks gained from leveling alone are unlikely to be sufficient for sustaining a full character build in late game. Below is a general breakdown of what to expect with the leveling and progression system in Apostasy.

#### Changes to leveling

Apostasy uses [Experience](https://www.nexusmods.com/skyrimspecialedition/mods/17751) and [Static Skill Leveling Rewritten](https://www.nexusmods.com/skyrimspecialedition/mods/89940) to handle leveling and progression.

My custom settings are explained below:
<Details>
<summary>Static Skill Leveling Settings</summary>

 - Gain skill points equal to 5 + (0.5 * playerlevel) for each level up, up to 30 points at level 50.
 - You can only store a maximum of 30 skill points per level, therefore **after level 50, you must spend all your skill points at level up or you will waste some points.**
 - You can increase skills up to 25 times per level (permitting you have enough points).

Skills Costs are as follows:

 > 0  to 25 : 1  
 > 26 to 50 : 2  
 > 51 to 75 : 4  
 > 76 to 100: 6  

</Details>

<Details>
<summary>Experience Skill Caps</summary>

 Experience allows the implementation of level-based skill caps.

 `skillCap = 18 + (playerlevel * 2.75)`

| Level | Skill Cap |  
|     :---:    |     :---:     |  
| 1  | 20  |  
| 5  | 31  | 
| 10 | 45  | 
| 15 | 59  | 
| 20 | 73  | 
| 25 | 86  |
| 30 | 100 | 

</Details>

### Difficulty

Apostasy uses [Difficulty Global Variable](https://www.nexusmods.com/skyrimspecialedition/mods/120521) allows for some additional tweaks to difficulty settings. A large advantage to using this mod is that difficulty setting will reflect in item and spell tooltips.

<Details>
<summary>Difficulty Sliders</summary>

| Difficulty | Damage Done | Damage Taken |
|     :---:    |     :---:     |     :---:     | 
| **Novice**    | 1.50x | 1.00x | 
| **Apprentice** | 1.25x | 1.25x |
| **Adept** | 1.00x |  1.50x | 
| **Expert** | 0.80x | 2.00x | 
| **Master** | 0.70x | 2.50x | 
| **Legendary** | 0.60x | 3.00x | 

</Details>

Apostasy introduces some additional mechanics based on difficulty. You can read more about these mechanics below.

<Details>
<summary>Harsher Health Regeneration</summary>

On Adept difficulty and higher, the Harsher Health Regeneration mechanic is introduced. This mechanic reduces your character's natural Health Regeneration by 100%. When you fall below 50% Health, your Health Regeneration is increased by 100%, allowing your Health to naturally regenerate without any additional buffs. Below 25% Health, your Health Regeneration is increased by an additional amount based on the difficulty.

Harsher Health Regeneration is done to make Health Regeneration a more valuable stat and more desirable. All effects that grant Health Regeneration (food, shrines, enchantments, alchemy, perks, etc.) will continue to function as intended.

| Difficulty | Health Regeneration >50% | Health Regeneration <50% | Health Regeneration <25% |
|     :---:    |     :---:     |     :---:     |      :---:     | 
| **Novice**    | 100%* |100%* | 100%* | 
| **Apprentice** | 100%* | 100%* | 100%* |
| **Adept** | 0% | 100% |  250% | 
| **Expert** | 0% | 100% | 200% | 
| **Master** | 0% | 100% | 150% | 
| **Legendary** | 0% | 0% | 0% | 
 **On Novice and Apprentice, this mechanic is disabled.*

**Legendary difficulty disables the Fortify Health Regeneration bonuses from falling below 50% and 25% Health.** This is done to ensure Legendary difficulty remains a challenge at all stages of the game, and to discourage players from playing on Legendary in general.

</Details>

<Details>
<summary>Carry Weight and Encumbrance</summary>

On Novice and Apprentice difficulty, your character's natural Carry Weight is increased by 200, making your base Carry Weight 500.

On Expert difficulty and higher, the new Carry Weight and Encumbrance mechanics are introduced. These mechanics reduce your character's natural Carry Weight by 100, making your base Carry Weight 200. Additionally, when over-encumbered, you take 4 Stamina damage per second.

These changes to carry weight seek to make Carry Weight a more interesting stat, while still allowing people to easily opt out of the system if they decide they do not like it.

| Difficulty | Base Carry Weight | 
|     :---:    |     :---:     | 
| **Novice**    | 500 | 
| **Apprentice** | 500 | 
| **Adept** | 300 | 
| **Expert** | 200 | 
| **Master** | 200 | 
| **Legendary** | 200 | 

</Details>

#### Attacks of Opportunity

Apostasy introduces a unique Attacks of Opportunity system to the game. This system is designed for the list and can not be found anywhere else. Attacks of Opportunity scale with difficulty and provide advantages to tactical positioning and timing in combat. So how does it work?

When you attack an enemy who is power attacking, drawing a bow, casting a spell, staggered, knocked down, or paralyzed, you will deal 50% more damage and poise damage. When you attack an enemy from behind, you will deal an additional 50% extra damage on top of any other Attack of Opportunity modifier(s) that may be active.

The player is also susceptible to Attacks of Opportunity, however their lethality scales based on difficulty. On Adept difficulty, Attacks of Opportunity deal 25% more damage to the player. On Expert+ difficulties, Attacks of Opportunity deal 50% more damage to the player. On Novice and Apprentice difficulties, the player can not suffer an Attack of Opportunity.

Ward spells protect the user from Attacks of Opportunities (player and any NPC).

Apostasy also introduces a "Massive Target" feature for specific enemy types. Massive Targets take 50% less damage from Attacks of Opportunity on Adept difficulty or lower (they take 25% more damage rather than 50% more damage) and can not be backstabbed. On Expert+ difficulties, Massive Targets can not suffer from Attacks of Opportunity.

### Quests Changes

Apostasy changes a significant amount of vanilla quests in one way or another in order to offer a more complete roleplaying exprience. The following list is non-exhaustive. Please note that not all MCM Options from Timing is Everything may work as intended in the list.

<Details>
<summary>DLC Quests</summary>

 - [Awakening](https://en.uesp.net/wiki/Skyrim:Awakening) Requires level 20, however this can be started at any point by going to [Dayspring Canyon](https://en.uesp.net/wiki/Skyrim:Dayspring_Canyon).
 - [Hearthfire](https://en.uesp.net/wiki/Skyrim:Hearthfire) Letter Requires level 15.
 - [Dragonborn](https://en.uesp.net/wiki/Skyrim:Dragonborn_(quest)) Requires level 20 and completion of [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller).

</Details>

<Details>
<summary>Level Locked Quests</summary>

  - **Level 15+**
    - [Dungeon Delving](https://en.uesp.net/wiki/Skyrim:Dungeon_Delving_(Jarl_-_Hagravens))
    - [Kill the Giant](https://en.uesp.net/wiki/Skyrim:Kill_the_Giant_(Jarl))
    - [The Forsworn Conspiracy](https://en.uesp.net/wiki/Skyrim:The_Forsworn_Conspiracy)
  - **Level 20+**
    - [A Night To Remember](https://en.uesp.net/wiki/Skyrim:A_Night_To_Remember)
    - [Ill Met By Moonlight](https://en.uesp.net/wiki/Skyrim:Ill_Met_By_Moonlight)
    - [Kill the Vampire](https://en.uesp.net/wiki/Skyrim:Kill_the_Vampire)
    - [The Black Star](https://en.uesp.net/wiki/Skyrim:The_Black_Star)
    - [The Break of Dawn](https://en.uesp.net/wiki/Skyrim:The_Break_of_Dawn)
    - [The Mind of Madness](https://en.uesp.net/wiki/Skyrim:The_Mind_of_Madness)
    - [Unfathomable Depths](https://en.uesp.net/wiki/Skyrim:Unfathomable_Depths)
  - **Level 25+**
    - [A Daedra's Best Friend](https://en.uesp.net/wiki/Skyrim:A_Daedra%27s_Best_Friend)
    - [The Cursed Tribe](https://en.uesp.net/wiki/Skyrim:The_Cursed_Tribe)
    - [The House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors)
    - [The Taste of Death](https://en.uesp.net/wiki/Skyrim:The_Taste_of_Death)
    - [The Wolf Queen Awakened](https://en.uesp.net/wiki/Skyrim:The_Wolf_Queen_Awakened)
    - [Waking Nightmare](https://en.uesp.net/wiki/Skyrim:Waking_Nightmare)
  - **Level 30+**
    - [Boethiah's Calling](https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling)
    - [Deathbrand](https://en.uesp.net/wiki/Skyrim:Deathbrand_(quest))
    - [Discerning the Transmundane](https://en.uesp.net/wiki/Skyrim:Discerning_the_Transmundane)
    - [Pieces of the Past](https://en.uesp.net/wiki/Skyrim:Pieces_of_the_Past)
    - [The Only Cure](https://en.uesp.net/wiki/Skyrim:The_Only_Cure)
    - [The Whispering Door](https://en.uesp.net/wiki/Skyrim:The_Whispering_Door)
  - **Level 40+**
    - [The Ebony Warrior](https://en.uesp.net/wiki/Skyrim:The_Ebony_Warrior)

</Details>

<Details>
<summary>Modded Quests</summary>

   - **Vigilant**: Requires level 25+ and the completion of [Kindred Judgement](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment) and [House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).
   - **Unslaad**: Requires completion of [Dragonslayer](https://en.uesp.net/wiki/Skyrim:Dragonslayer).

</Details>


## New Content

This section will try to list the new content focused mods added to the list, and if necessary, describe any major changes to them.

### New Quests

 - [Artifacts - The Breton Paladin](https://www.nexusmods.com/skyrimspecialedition/mods/16199)
 - [Artifacts - The Ice Blade of the Monarch](https://www.nexusmods.com/skyrimspecialedition/mods/13972)
 - [Artifacts - The Tournament of the ten Bloods](https://www.nexusmods.com/skyrimspecialedition/mods/15264)
 - [Belethor's Sister](https://www.nexusmods.com/skyrimspecialedition/mods/92381)
 - [Dragon Hunting](https://www.nexusmods.com/skyrimspecialedition/mods/99193)
 - [Missives](https://www.nexusmods.com/skyrimspecialedition/mods/17576) + [Headhunter - Bounties Redone](https://www.nexusmods.com/skyrimspecialedition/mods/51847)
 - [Mysteries of the Dwemer](https://www.nexusmods.com/skyrimspecialedition/mods/114863)
 - [Penitus Oculatus](https://www.nexusmods.com/skyrimspecialedition/mods/21061)
 - [SIRENROOT - Deluge of Deceit](https://www.nexusmods.com/skyrimspecialedition/mods/70917)
 - [Skyrim Extended Cut - Saints and Seducers](https://www.nexusmods.com/skyrimspecialedition/mods/72772)
 - [Unslaad](https://www.nexusmods.com/skyrimspecialedition/mods/11789)
 - [VIGILANT](https://www.nexusmods.com/skyrimspecialedition/mods/11849)

### Vanilla Quest Expansions and Edits

 - [A Lovely Letter Alternate Routes](https://www.nexusmods.com/skyrimspecialedition/mods/21916)
 - [Blood and Silver - Cidhna Mine Expanded](https://www.nexusmods.com/skyrimspecialedition/mods/20269)
 - [Blood on the Ice Redux](https://www.nexusmods.com/skyrimspecialedition/mods/6126)
 - [Caught Red Handed - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/65708)
 - [Defeat the Dragon Cult](https://www.nexusmods.com/skyrimspecialedition/mods/86625)
 - [Finding Susanna Alive](https://www.nexusmods.com/skyrimspecialedition/mods/32512)
 - [House of Horrors - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57285)
 - [Improved College Entry - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22184)
 - [Improved Companions - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22300)
 - [In the Shadow of the Crown](https://www.nexusmods.com/skyrimspecialedition/mods/79600)
 - [Infiltration - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/114054)
 - [Jiub's Opus](https://www.nexusmods.com/skyrimspecialedition/mods/17056)
 - [Muiri's Revenge](https://www.nexusmods.com/skyrimspecialedition/mods/24312)
 - [Nilheim - Misc Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/53792)
 - [Paarthurnax - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/51711)
 - [Search and Seizure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/67066)
 - [Serana Cure Quest Plus](https://www.nexusmods.com/skyrimspecialedition/mods/105091)
 - [Simple Fishing Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/103440)
 - [Stones of Barenziah Quest Markers](https://www.nexusmods.com/skyrimspecialedition/mods/684)
 - [The Heart of Dibella - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/94863)
 - [Innocence Lost - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/80974)
 - [The Only Cure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57683)
 - [The Whispering Door - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/76606)
 - [Thieves Guild Alternative Endings](https://www.nexusmods.com/skyrimspecialedition/mods/114558)
 - [Thieves Guild Requirements](https://www.nexusmods.com/skyrimspecialedition/mods/33256)
 - [Unmasking Sybille](https://www.nexusmods.com/skyrimspecialedition/mods/109265)

### Followers

 - [Bjorn - Fully Voiced Follower](https://www.nexusmods.com/skyrimspecialedition/mods/91652)
 - [Feris - Custom Voiced Female Follower](https://www.nexusmods.com/skyrimspecialedition/mods/90032)
 - [Follower Dialogue Expansion - Aela the Huntress](https://www.nexusmods.com/skyrimspecialedition/mods/114801)
 - [Follower Dialogue Expansion - Brelyna Maryon](https://www.nexusmods.com/skyrimspecialedition/mods/113359)
 - [Follower Dialogue Expansion - Erik the Slayer](https://www.nexusmods.com/skyrimspecialedition/mods/116719)
 - [Follower Dialogue Expansion - Jordis the Sword-Maiden](https://www.nexusmods.com/skyrimspecialedition/mods/117930)
 - [Follower Dialogue Expansion - Mjoll the Lioness](https://www.nexusmods.com/skyrimspecialedition/mods/116025)
 - [Gore - A Companion Mod](https://www.nexusmods.com/skyrimspecialedition/mods/85298)
 - [INDIGO](https://www.nexusmods.com/skyrimspecialedition/mods/88240)
 - [Kaidan 2](https://www.nexusmods.com/skyrimspecialedition/mods/19075)
 - [Katana - Journey in the Shadows](https://www.nexusmods.com/skyrimspecialedition/mods/69622)
 - [Light and Shade](https://www.nexusmods.com/skyrimspecialedition/mods/77993)
 - [Remiel-Custom Voiced Dwemer Specialist and Companion](https://www.nexusmods.com/skyrimspecialedition/mods/51874)
 - [Song of the Green (Auri Follower)](https://www.nexusmods.com/skyrimspecialedition/mods/11278)
 - [Val Serano - Pirate Custom Voiced Follower and Quest Adventure](https://www.nexusmods.com/skyrimspecialedition/mods/103669)

### Player Homes

 - [Elianora's Breezehome Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/2829)
 - [Mirele Bismath Reborn](https://www.nexusmods.com/skyrimspecialedition/mods/93817)
 - [Ruska - Riften Player Home](https://www.nexusmods.com/skyrimspecialedition/mods/16177)
 - [Tel Jerdein - Telvanni Sorcerer Tower](https://www.nexusmods.com/skyrimspecialedition/mods/33539)
 - [Wuth Rein - An ancient nordic hideout](https://www.nexusmods.com/skyrimspecialedition/mods/52995)
