![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.png)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  Gameplay Guide |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/apostasy">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md">FAQ</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/ADDONS.md">ADDONS</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

- [Initial Setup](#initial-setup)
- [Overview](#overview)
  - [Core Overhauls](#core-overhauls)
  - [Combat Foundations](#combat-foundations)
- [Leveling and Progression](#leveling-and-progression)
  - [Changes to leveling](#changes-to-leveling)
  - [Perks](#perks)
- [Difficulty](#difficulty)
  - [New Mechanics](#new-mechanics)
- [Quests Changes](#quests-changes)
- [New Armors and Weapons](#new-armors-and-weapons)
- [New Content](#new-content)
  - [New Quests](#new-quests)
  - [Vanilla Quest Expansions and Edits](#vanilla-quest-expansions-and-edits)
  - [Followers](#followers)
  - [Player Homes](#player-homes)

## Initial Setup

Before reading this guide, please follow the [Installation Guide](https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md) as it will answer the vast majority of technical questions related to getting the list setup and running. Be sure to check out the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md) page to learn more about the controller support, optional tweaks, addons, MCM options, and more.

## Overview

This section will cover the absolute basics of the list. I suggest reading, or skimming all of the linked mod pages in this section if you are unfamiliar with the preceding mods.

Before reading this section, I suggest looking over the [load order](https://loadorderlibrary.com/lists/Apostasy) and [keybinds](https://github.com/Oghma-Infinium/Apostasy/blob/main/images/Keybinds.png).

### Core Overhauls

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/GameplayHeader.png)

 - Apostasy uses a custom Perk Overhaul for all Warrior and Thief skills and Custom-made perks for Alteration and Enchanting. The rest of the perks are covered by a custom mashup and overhaul of other perk mods.
 - Apostasy uses a custom encounter zone and level scaling mod to **delevel** the world, instituting minimum and maximum level caps for every dungeon.
 - [Nirn's Chosen](https://www.nexusmods.com/skyrimspecialedition/mods/121427) and [Stones of Sacrifice](https://www.nexusmods.com/skyrimspecialedition/mods/121629) cover the Race and Standing Stones overhauls within the list.
 - [Pilgrim - A Religion Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/54099) and the [Custom Skills Framework Addon](https://www.nexusmods.com/skyrimspecialedition/mods/93913) flesh out the Religion system for the list.

### Combat Foundations

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720691484-471070989.png)

The following mods are considered the "foundations" of the combat and gameplay for Apostasy:
 - [Stances NG](https://www.nexusmods.com/skyrimspecialedition/mods/117986) provides the ability to swap between multiple stances. By default, stances only contribute to what animations are used, but some perks provide benefits to specific stances!
   - Default keybinds: `X` for Wolf Stance, `Ctrl+X` for Hawk Stance, `Shift+X` for Bear Stance.
   - Stances affect first and third person.
 - [TK Dodge RE](https://www.nexusmods.com/skyrimspecialedition/mods/56956) adds Dodging to the game.
   - Dodges are based on Armor Type. Heavy Armor and Cloth users gets a shorter step dodge with shortened iframes, Light Armor gets a longer roll dodge with longer iframes.
   - In First person, Dodges are always roll dodges.
 - The list has custom Timed Block mechanic. Enter block just before enemy hit for increased block efficiency with a chance to stagger the attacker.
   - The Block skill tree has multiple perks to upgrade Timed Block with additional effects.
 - [Maxsu Poise](https://github.com/max-su-2019/MaxsuPoise/blob/master/docs/en/Mechanics%20Manual.md) and [Modern Stagger Lock](https://github.com/max-su-2019/ModernStaggerLock) implement a Poise system, which has been fine tuned for the list. Poise Health can be seen on the Special Bar of TrueHUD (the yellow bar above Health on player and target widgets). The Poise system is discussed in more depth in the [New Mechanics](#new-mechanics) section.

## Leveling and Progression

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720520004-1902455222.png)

Apostasy modifies the vanilla leveling experience in a way to reward the player for engaging in the world in sensible ways. While perks can be obtained through leveling, the perks gained from leveling alone are unlikely to be sufficient for sustaining a full character build in late game. Below is a general breakdown of what to expect with the leveling and progression system in Apostasy.

### Changes to leveling

Apostasy uses [Experience](https://www.nexusmods.com/skyrimspecialedition/mods/17751) and [Static Skill Leveling Rewritten](https://www.nexusmods.com/skyrimspecialedition/mods/89940) to handle leveling and progression.

My custom settings are explained below:
<Details>
<summary>XP Breakpoints</summary>

 Apostasy modifies the vanilla XP per level requirements.

 `requiredXP = 290 + (playerlevel * 20)`

| Level | XP Required |  
|     :---:    |     :---:     |  
| 1  | 310  |  
| 10  | 4,000  | 
| 20 | 10,000  | 
| 30 | 18,000  | 
| 40 | 28,000  | 
| 50 | 40,000  |
| 100 | 130,000 | 

</Details>

<Details>
<summary>Static Skill Leveling Settings</summary>

 - Gain skill points equal to 10 + (1 * playerlevel) for each level up, up to 50 points per level (this cap will be hit at level 40+).
 - You can only store a maximum of 50 skill points per level, therefore **after level 40, you must spend all your skill points at level up or you will waste some points.**
 - You can increase skills up to 25 times per level (permitting you have enough points and the skills are adequately below the current skill cap).

Skill Point Costs are as follows:

| Skill Level | Skill Point Cost |  
|     :---:    |     :---:     |  
| 0-25  | 1  |  
| 26-50  | 2  | 
| 51-75 | 4  | 
| 76-100 | 6  | 

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

### Perks

Apostasy takes a mixed approach to the acquisition of perks and skills. Providing the player with 60 Perks from level 1-50 (no perks are granted from leveling after level 50) and up to an additional 34 perks from Quests.

<Details>
<summary>Additional Perk Sources</summary>

The following is a list of the additional perk sources in Apostasy.

**Main Quest** (8 perks total)

 - [Bleak Falls Barrow](https://en.uesp.net/wiki/Skyrim:Bleak_Falls_Barrow_(quest))
 - [Dragon Rising](https://en.uesp.net/wiki/Skyrim:Dragon_Rising)
 - [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller)
 - [Diplomatic Immunity](https://en.uesp.net/wiki/Skyrim:Diplomatic_Immunity)
 - [Alduin's Wall](https://en.uesp.net/wiki/Skyrim:Alduin%27s_Wall)
 - [Elder Knowledge](https://en.uesp.net/wiki/Skyrim:Elder_Knowledge)
 - [The Fallen](https://en.uesp.net/wiki/Skyrim:The_Fallen)
 - [Dragonslayer](https://en.uesp.net/wiki/Skyrim:Dragonslayer)

**Guilds** (12 perks total)

 - [The Silver Hand](https://en.uesp.net/wiki/Skyrim:The_Silver_Hand)
 - [Glory of the Dead](https://en.uesp.net/wiki/Skyrim:Glory_of_the_Dead)
 - [Revealing the Unseen](https://en.uesp.net/wiki/Skyrim:Revealing_the_Unseen)
 - [The Eye of Magnus](https://en.uesp.net/wiki/Skyrim:The_Eye_of_Magnus)
 - [Darkness Returns](https://en.uesp.net/wiki/Skyrim:Darkness_Returns)
 - [Under New Management](https://en.uesp.net/wiki/Skyrim:Under_New_Management)
 - [Bound Until Death](https://en.uesp.net/wiki/Skyrim:Bound_Until_Death)
 - [Hail Sithis!](https://en.uesp.net/wiki/Skyrim:Hail_Sithis!)
 - [Destroy the Dark Brotherhood!](https://en.uesp.net/wiki/Skyrim:Destroy_the_Dark_Brotherhood!)
 - [Tending the Flames](https://en.uesp.net/wiki/Skyrim:Tending_the_Flames)
 - Battle for Whiterun ([Imperial](https://en.uesp.net/wiki/Skyrim:Battle_for_Whiterun_(Imperial)) / [Stormcloak](https://en.uesp.net/wiki/Skyrim:Battle_for_Whiterun_(Stormcloaks)))
 - [Liberation of Skyrim](https://en.uesp.net/wiki/Skyrim:Liberation_of_Skyrim) / [Reunification of Skyrim](https://en.uesp.net/wiki/Skyrim:Reunification_of_Skyrim)

**Side Quests** (6 perks total)

 - [Kyne's Sacred Trials](https://en.uesp.net/wiki/Skyrim:Kyne%27s_Sacred_Trials)
 - [The Blessings of Nature](https://en.uesp.net/wiki/Skyrim:The_Blessings_of_Nature)
 - [Blood on the Ice](https://en.uesp.net/wiki/Skyrim:Blood_on_the_Ice)
 - [The Book of Love](https://en.uesp.net/wiki/Skyrim:The_Book_of_Love)
 - [The Heart of Dibella](https://en.uesp.net/wiki/Skyrim:The_Heart_of_Dibella)
 - [No One Escapes Cidhna Mine](https://en.uesp.net/wiki/Skyrim:No_One_Escapes_Cidhna_Mine)

**DLC Quests** (6 perks total)

 - [Beyond Death](https://en.uesp.net/wiki/Skyrim:Beyond_Death)
 - [Kindred Judgment](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment)
 - [Lost to the Ages](https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages)
 - [The Temple of Miraak](https://en.uesp.net/wiki/Skyrim:The_Temple_of_Miraak)
 - [The Path of Knowledge](https://en.uesp.net/wiki/Skyrim:The_Path_of_Knowledge)
 - [At the Summit of Apocrypha](https://en.uesp.net/wiki/Skyrim:At_the_Summit_of_Apocrypha)

**Other Sources** (2 perks total)

 - [Oghma Infinium](https://elderscrolls.fandom.com/wiki/Oghma_Infinium_(Skyrim))

</Details>

## Difficulty

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720419196-1191687929.png)

Rather than Skyrim's vanilla difficulty system of only scaling up or down damage based on difficulty, Apostasy introduces some additional mechanics based on difficulty. You can read more about these mechanics below.

<Details>
<summary>Difficulty Sliders</summary>

| Difficulty | Damage Done | Damage Taken |
|     :---:    |     :---:     |     :---:     | 
| **Novice**    | 1.50x | 0.5x | 
| **Apprentice** | 1.25x | 0.75x | 
| **Adept** | 1.00x |  1.00x | 
| **Expert** | 1.00x | 1.50x | 
| **Master** | 0.75x | 2.00x | 
| **Legendary** | 0.75x | 2.00x | 

Additionally, on Legendary difficulty your spells cost 10% more Magicka, you receive 25% more Poise damage, and your Sneak Attacks are 50% less effective.

</Details>

<Details>
<summary>Harsher Health Regeneration</summary>

On Adept difficulty and higher, the Harsher Health Regeneration mechanic is introduced. This mechanic reduces your character's natural Health Regeneration by 100%. When you fall below 50% Health, your Health Regeneration is increased by 100%, allowing your Health to naturally regenerate without any additional buffs. Below 25% Health, your Health Regeneration is increased by an additional amount based on the difficulty.

Harsher Health Regeneration is done to make Health Regeneration a more valuable stat and more desirable. All effects that grant Health Regeneration (food, shrines, enchantments, alchemy, perks, etc.) will continue to function as intended.

| Difficulty | Base Health Regeneration >50% | Base Health Regeneration <50% | Base Health Regeneration <25% |
|     :---:    |     :---:     |     :---:     |      :---:     | 
| **Novice**    | 100%* | 100%* | 100%* | 
| **Apprentice** | 100%* | 100%* | 100%* |
| **Adept** | 0% | 100% |  200% | 
| **Expert** | 0% | 100% | 200% | 
| **Master** | 0% | 100% | 100% | 
| **Legendary** | 0% | 100% | 100% | 

 **On Novice and Apprentice, this mechanic is disabled.*

</Details>

<Details>
<summary>Carry Weight and Encumbrance</summary>

On Novice difficulty, your character's natural Carry Weight is increased by 100, making your base Carry Weight 400.

On Expert difficulty and higher, the new Carry Weight and Encumbrance mechanics are introduced. These mechanics reduce your character's natural Carry Weight by 100, making your base Carry Weight 200. Additionally, when over-encumbered, you take 4 Stamina damage per second.

These changes to carry weight seek to make Carry Weight a more interesting stat, while still allowing people to easily opt out of the system if they decide they do not like it.

| Difficulty | Base Carry Weight | 
|     :---:    |     :---:     | 
| **Novice**    | 400 | 
| **Apprentice** | 300 | 
| **Adept** | 300 | 
| **Expert** | 200 | 
| **Master** | 200 | 
| **Legendary** | 200 | 

</Details>

### New Mechanics

Apostasy overhauls or adds additional mechanics, reminiscent of modern Action RPGs to further enhance the gameplay. Check out the sections below to learn more!

<Details>
<summary>Poise and Stagger</summary>

On Apprentice and Novice difficulty, the player can not be inflicted with Heavy Stagger, unless facing a Massive Target.

On Novice difficulty, incoming Poise damage is reduced by 20% for the player. This results in the player being much more difficult to stagger.

</Details>

<Details>
<summary>Massive Targets</summary>

Apostasy also introduces a "Massive Target" feature for specific enemy types, such as Giants and Dragons. Massive Targets take reduced damage from Attacks of Opportunity and can not be backstabbed. 

Additionally, Massive Targets have a higher likelihood of inflicting Heavy Staggers.

</Details>

<Details>
<summary>Attacks of Opportunity</summary>

Apostasy introduces a unique Attacks of Opportunity system to the game. This system is designed for the list and can not be found anywhere else. Attacks of Opportunity scale with difficulty and provide advantages to tactical positioning and timing in combat. So how does it work?

When you attack an enemy who is power attacking, drawing a bow, casting a spell, staggered, knocked down, or paralyzed, you will deal 50% more damage and Poise damage. When you attack an enemy from behind (a backstab), you will deal an additional 50% extra damage on top of any other Attack of Opportunity modifier(s) that may be active.

The player is also susceptible to Attacks of Opportunity, however their lethality scales based on difficulty. 

| Difficulty | Player Damage Taken | NPC Damage Taken | Massive Target Damage Taken
|     :---:    |     :---:     |     :---:    |     :---:     | 
| **Novice**    | +0% | +50% | +25% |
| **Apprentice** | +0% | +50% | +25% |
| **Adept** | +25% | +50% | +25% |
| **Expert** | +50% | +50% | +0% |
| **Master** | +50% | +50% | +0% |
| **Legendary** | +50% | +50% | +0% |

Ward spells protect the user from Attacks of Opportunities (player and any NPC).

</Details>

<Details>
<summary>Bloodied</summary>

Apostasy introduces a new mechanic referred to as Bloodied. Bloodied targets take more damage from Power Attacks while they are below half Health.

The player can not be affected by Bloodied on any difficulty.

</Details>

<Details>
<summary>Confusion</summary>

Apostasy introduces a new mechanic referred to as Confusion. Confusion affects mages when they receive a melee attack while casting a spell.

The player can be affected by Confusion on Expert or higher difficulties.

</Details>

## Quests Changes

Apostasy changes a significant amount of vanilla quests in one way or another in order to offer a more complete roleplaying exprience. The following list is non-exhaustive.

<Details>
<summary>Vanilla Quests</summary>

 - [Awakening](https://en.uesp.net/wiki/Skyrim:Awakening) Requires level 20, however this can be started at any point by going to [Dayspring Canyon](https://en.uesp.net/wiki/Skyrim:Dayspring_Canyon).
 - [Hearthfire](https://en.uesp.net/wiki/Skyrim:Hearthfire) Letter Requires level 15.
 - [Dragonborn](https://en.uesp.net/wiki/Skyrim:Dragonborn_(quest)) Requires level 30 and completion of [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller).
 - [A Chance Arrangement](https://en.uesp.net/wiki/Skyrim:A_Chance_Arrangement) Requires the player to have a Sneak Skill >=25, have picked >=10 pockets, and stolen >=100 items.
 - [Loud and Clear](https://en.uesp.net/wiki/Skyrim:Loud_and_Clear) Requires the player to complete a minimum of 4 radiant jobs for the Thieves Guild.
 - [Dampened Spirits](https://en.uesp.net/wiki/Skyrim:Dampened_Spirits) Requires the player to complete a minimum of 6 jobs for the Thieves Guild.

</Details>

<Details>
<summary>Level Locked Quests</summary>

  - **Level 15+**
    - [Dungeon Delving](https://en.uesp.net/wiki/Skyrim:Dungeon_Delving_(Jarl_-_Hagravens))
    - [Kill the Giant](https://en.uesp.net/wiki/Skyrim:Kill_the_Giant_(Jarl))
    - [Missing in Action](https://en.uesp.net/wiki/Skyrim:Missing_In_Action)
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

  - **Wyrmstooth**: Requires level 15+ and completion of [The Way of the Voice](https://en.uesp.net/wiki/Skyrim:The_Way_of_the_Voice).
  - **Vigilant**: Requires level 25+ and the completion of [Kindred Judgement](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment) and [House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).
  - **Unslaad**: Requires completion of [Dragonslayer](https://en.uesp.net/wiki/Skyrim:Dragonslayer).

</Details>

## New Armors and Weapons

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720811383-481712445.png)

Apostasy adds a significant amount of new Armors and Weapons to the game, all of which have been hand tuned and modified to fit within the balance of the list. While most can be accessed through [Skyrim Outfit System](https://www.nexusmods.com/skyrimspecialedition/mods/42162) if you want to use them purely for cosmetics, many have been re-integrated into the world as potential loot (or equipment that is unique to specific NPCs) and/or has been made obtainable through **Crafting Motifs**. 

Below is an (incomplete) list of new armors and weapons that are added and obtainable by the player:

<Details>
<summary>New Equipment</summary>

  - [Bone Cultist Armor](https://www.nexusmods.com/skyrimspecialedition/mods/111224): Can be found on Solstheim Bandits and has the same crafting requirements as Bonemold.
  - [Colovian Prince Set](https://www.nexusmods.com/skyrimspecialedition/mods/79894): See **Motifs**. Can be found on select NPCs.
  - [Crown Plate Set](https://www.nexusmods.com/skyrimspecialedition/mods/114751): See **Motifs**. Can also be found on [Kematu](https://en.uesp.net/wiki/Skyrim:Kematu) and his men.
  - [Dark Brotherhood Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/57539): Replacer for Dark Brotherhood Armor.
  - [Dark Witch Armor](https://www.nexusmods.com/skyrimspecialedition/mods/112260): See **Motifs**. Worn by [Illia](https://en.uesp.net/wiki/Skyrim:Illia).
  - [Dwemer Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/81043): Craftable with Dwemer Smithing.
  - [Eclipse Mage Outfit](https://www.nexusmods.com/skyrimspecialedition/mods/77244):
  - [Elmlock Armor and Blade](https://www.nexusmods.com/skyrimspecialedition/mods/105930): 
  - [Fleet Knight Set](https://www.nexusmods.com/skyrimspecialedition/mods/95009): See **Motifs**.
  - [Fluted Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/106381): Craftable with Ebony Smithing. Can also be found on select NPCs.
  - [Glasses Pack](https://www.nexusmods.com/skyrimspecialedition/mods/115653): See **Motifs**.
  - [Gryphonknight Regalia](https://www.nexusmods.com/skyrimspecialedition/mods/107437): Can be looted off of [Sabine Nytte](https://en.uesp.net/wiki/Skyrim:Sabine_Nytte).
  - [Illusive Infiltrator Armor](https://www.nexusmods.com/skyrimspecialedition/mods/105659): Craftable with Steel Smithing.
  - [Infantry Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/88099): Can be crafted with Steel Smithing. Can also be found on select NPCs.
  - [Kellan Armor](https://www.nexusmods.com/skyrimspecialedition/mods/68199): Craftable with Steel Smithing. Worn by select NPCs. 
  - [Kvetchi Mercenary Set](https://www.nexusmods.com/skyrimspecialedition/mods/79226): See **Motifs**.
  - [Lunar Guard Armor](https://www.nexusmods.com/skyrimspecialedition/mods/75349): See **Motifs**.
  - [MAGECORE](https://www.nexusmods.com/skyrimspecialedition/mods/113540): See **Motifs**.
  - [Maormer Seascale Set](https://www.nexusmods.com/skyrimspecialedition/mods/91506): Can be looted from [Haldyn](https://en.uesp.net/wiki/Skyrim:Haldyn).
  - [Obi's HeadHunter Armor](https://www.nexusmods.com/skyrimspecialedition/mods/113990): Can be looted from [Captain Hargar](https://en.uesp.net/wiki/Skyrim:Captain_Hargar).
  - [Orcish Armor Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/110280): Craftable with Orcish Smithing, can also be seen as variant armors for Stronghold Orcs. 
  - [Raven HDT-SMP Armor](https://www.nexusmods.com/skyrimspecialedition/mods/87655): Can be looted from the boss in [Bloodlet Throne](https://en.uesp.net/wiki/Skyrim:Bloodlet_Throne).
  - [Rihad Swordsman Set](https://www.nexusmods.com/skyrimspecialedition/mods/120576): See **Motifs**. Can also be found on [Kematu](https://en.uesp.net/wiki/Skyrim:Kematu) and his men.
  - [Silver Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/79088): Craftable with Advanced Armors Smithing. Worn by select NPCs. 
  - [Squire's Plate](https://www.nexusmods.com/skyrimspecialedition/mods/120370): See **Motifs**.
  - [Stormhold Warrior Armor](https://www.nexusmods.com/skyrimspecialedition/mods/96559): Can be crafted with Steel Smithing. Variants can also be looted off [Deeja](https://en.uesp.net/wiki/Skyrim:Deeja) and [Jaree-Ra](https://en.uesp.net/wiki/Skyrim:Jaree-Ra).
  - [Travelling Priest Robes](https://www.nexusmods.com/skyrimspecialedition/mods/118327): Can be found on several Priest-type NPCs and crafted.
  - [Twilight Princess Armor](https://www.nexusmods.com/skyrimspecialedition/mods/71182): Can be crafted after completion of [Kindred Judgement](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment) with Steel Smithing. Worn by [Serana](https://en.uesp.net/wiki/Skyrim:Serana).
  - [Vey Alaxon](https://www.nexusmods.com/skyrimspecialedition/mods/104572): Fully integrated into Gilded Elven tier, craftable with Elven Smithing.
  - [Wayward Knight Set](https://www.nexusmods.com/skyrimspecialedition/mods/112793): See **Motifs**.
  - [Wild Witch Outfit](https://www.nexusmods.com/skyrimspecialedition/mods/81085): See **Motifs**. A variant can also be looted off [The Caller](https://en.uesp.net/wiki/Skyrim:The_Caller).
  - [Wind Ruler Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/60842): Can be looted from the [Butcher](https://en.uesp.net/wiki/Skyrim:Butcher) and [Umana](https://en.uesp.net/wiki/Skyrim:Umana). Also found on select NPCs.
  - [Ysmir Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/112454): Replaces the appearance of [Ahzidal's relics](https://en.uesp.net/wiki/Lore:Relics_of_Ahzidal), and can be crafted after completion of [Glory of the Dead](https://en.uesp.net/wiki/Skyrim:Glory_of_the_Dead).

</Details>

Crafting Motifs are consumed (like spell tomes) and are not required to be held in inventory in order to craft their respective equipment. Below is a list of Crafting Motifs, their requirements, and where to find them:

<Details>
<summary>Style Motifs</summary>

Armors and weapons crafted from Motifs may or may not require the equivalent Smithing perk in addition to the manual knowledge requirement.

 - **Clothes and Jewelry**
   - [Glasses](https://www.nexusmods.com/skyrimspecialedition/mods/115653): Purchasable from Jewelers and Radiant Raiments. (**FEMALE ONLY**).
   - **Earrings**: Purchasable from Jewelers and Radiant Raiments. (Covers [Goam's Earrings](https://www.nexusmods.com/skyrimspecialedition/mods/112173) and [Pierced Ears - Earrings SE](https://www.nexusmods.com/skyrimspecialedition/mods/13571).)
     - WARNING: Earrings and Ear meshes are complicated and they may not align perfectly with all ear shapes.
   - [Magecore](https://www.nexusmods.com/skyrimspecialedition/mods/113540): Purchasable from Radiant Raiments. (**FEMALE ONLY**, Armored variants can be crafted with Ebony Smithing + Manual). More NSFW/Lewd variants can be toggled in the Apostasy MCM.
   - [Wild Witch](https://www.nexusmods.com/skyrimspecialedition/mods/81085): Purchasable from Radiant Raiments.
 - **Armor and Weapons**
   - **Alik'r Style**: Purchasable from Blacksmiths with level 40+ Smithing skill. (Covers [Crown Plate](https://www.nexusmods.com/skyrimspecialedition/mods/114751) and [Rihad Swordsman](https://www.nexusmods.com/skyrimspecialedition/mods/120576).)
   - **Bretonic Style**: Purchaseable from Blacksmiths with level 60+ Smithing skill. (Covers [Fleet Knight](https://www.nexusmods.com/skyrimspecialedition/mods/95009), [Gryphonknight](https://www.nexusmods.com/skyrimspecialedition/mods/107437), [Wayward Knight](https://www.nexusmods.com/skyrimspecialedition/mods/112793), [Squire's Plate](https://www.nexusmods.com/skyrimspecialedition/mods/120370), and [Dark Witch Armor](https://www.nexusmods.com/skyrimspecialedition/mods/112260).)
     - More NSFW/lewd versions of some sets can be toggled in the Apostasy MCM.
   - **Cyrodilic Style**: Purchasable from Blacksmiths with level 40+ Smithing skill. (Covers [Colovian Prince](https://www.nexusmods.com/skyrimspecialedition/mods/79894) and [Kvetchi Mercenary](https://www.nexusmods.com/skyrimspecialedition/mods/79226).)
   - **Khajiit Style**: Purchasable from Blacksmiths with level 80+ Smithing skill. (Covers [Lunar Guard](https://www.nexusmods.com/skyrimspecialedition/mods/75349) and [Moon Monk's Robes](https://www.nexusmods.com/skyrimspecialedition/mods/82495).)

</Details>

## New Content

This section will try to list the new content focused mods added to the list, and if necessary, describe any major changes to them.

### New Quests

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720525985-188255669.png)

 - [A Conversation - Quest Mod](https://www.nexusmods.com/skyrimspecialedition/mods/124431)
 - [Artifacts - The Breton Paladin](https://www.nexusmods.com/skyrimspecialedition/mods/16199)
 - [Artifacts - The Ice Blade of the Monarch](https://www.nexusmods.com/skyrimspecialedition/mods/13972)
 - [Artifacts - The Tournament of the ten Bloods](https://www.nexusmods.com/skyrimspecialedition/mods/15264)
 - [Belethor's Sister](https://www.nexusmods.com/skyrimspecialedition/mods/92381)
 - [Demon of Dream](https://www.nexusmods.com/skyrimspecialedition/mods/118719)
 - [Dragon Hunting](https://www.nexusmods.com/skyrimspecialedition/mods/99193)
 - [Final Farewell - Quest Mod](https://www.nexusmods.com/skyrimspecialedition/mods/127894?)
 - [Missives](https://www.nexusmods.com/skyrimspecialedition/mods/17576) + [Headhunter - Bounties Redone](https://www.nexusmods.com/skyrimspecialedition/mods/51847)
 - [Final Farewell - Quest Mod](https://www.nexusmods.com/skyrimspecialedition/mods/127894)
 - [Mysteries of the Dwemer](https://www.nexusmods.com/skyrimspecialedition/mods/114863)
 - [Penitus Oculatus](https://www.nexusmods.com/skyrimspecialedition/mods/21061)
 - [SIRENROOT - Deluge of Deceit](https://www.nexusmods.com/skyrimspecialedition/mods/70917)
 - [Skyrim Extended Cut - Saints and Seducers](https://www.nexusmods.com/skyrimspecialedition/mods/72772)
 - [Tales of Skyrim - Berserkyr](https://www.nexusmods.com/skyrimspecialedition/mods/103559)
 - [Unslaad](https://www.nexusmods.com/skyrimspecialedition/mods/11789)
 - [VIGILANT](https://www.nexusmods.com/skyrimspecialedition/mods/11849)
 - [Wyrmstooth](https://www.nexusmods.com/skyrimspecialedition/mods/45565)

### Vanilla Quest Expansions and Edits

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720526384-1494096468.png)

 - [A Lovely Letter Alternate Routes](https://www.nexusmods.com/skyrimspecialedition/mods/21916)
 - [Blood and Silver - Cidhna Mine Expanded](https://www.nexusmods.com/skyrimspecialedition/mods/20269)
 - [Blood on the Ice Redux](https://www.nexusmods.com/skyrimspecialedition/mods/6126)
 - [Boethiah's Calling - Alternate Questline](https://www.nexusmods.com/skyrimspecialedition/mods/121499)
 - [Caught Red Handed - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/65708)
 - [Defeat the Dragon Cult](https://www.nexusmods.com/skyrimspecialedition/mods/86625)
 - [Finding Susanna Alive](https://www.nexusmods.com/skyrimspecialedition/mods/32512)
 - [House of Horrors - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57285)
 - [Improved College Entry - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22184)
 - [Improved Companions - Questline Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/22300)
 - [In the Shadow of the Crown](https://www.nexusmods.com/skyrimspecialedition/mods/79600)
 - [Infiltration - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/114054)
 - [Innocence Lost - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/80974)
 - [Jiub's Opus](https://www.nexusmods.com/skyrimspecialedition/mods/17056)
 - [Mehrunes Dagon's Shrine Unlocked - Pieces of the Past Alternate Ending](https://www.nexusmods.com/skyrimspecialedition/mods/119502)
 - [Muiri's Revenge](https://www.nexusmods.com/skyrimspecialedition/mods/24312)
 - [Nilheim - Misc Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/53792)
 - [Paarthurnax - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/51711)
 - [Search and Seizure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/67066)
 - [Serana Cure Quest Plus](https://www.nexusmods.com/skyrimspecialedition/mods/105091)
 - [Simple Fishing Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/103440)
 - [Stones of Barenziah Quest Markers](https://www.nexusmods.com/skyrimspecialedition/mods/684)
 - [The Heart of Dibella - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/94863)
 - [The Taste of Death - Quest Addon](https://www.nexusmods.com/skyrimspecialedition/mods/123173)
 - [The Only Cure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57683)
 - [The Whispering Door - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/76606)
 - [Thieves Guild Alternative Endings](https://www.nexusmods.com/skyrimspecialedition/mods/114558)
 - [Thieves Guild Requirements](https://www.nexusmods.com/skyrimspecialedition/mods/33256)
 - [Unmasking Sybille](https://www.nexusmods.com/skyrimspecialedition/mods/109265)

### Followers

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1724960630-647828967.png)

 - [Feris - Custom Voiced Female Follower](https://www.nexusmods.com/skyrimspecialedition/mods/90032)
 - [Follower Dialogue Expansion Series](https://next.nexusmods.com/profile/anbeegod/mods?gameId=1704)
 - [Gore - A Companion Mod](https://www.nexusmods.com/skyrimspecialedition/mods/85298)
 - [INDIGO](https://www.nexusmods.com/skyrimspecialedition/mods/88240)
 - [Kaidan 2](https://www.nexusmods.com/skyrimspecialedition/mods/19075)
 - [Katana - Journey in the Shadows](https://www.nexusmods.com/skyrimspecialedition/mods/69622)
 - [Khajiit Will Follow](https://www.nexusmods.com/skyrimspecialedition/mods/2227)
 - [Remiel-Custom Voiced Dwemer Specialist and Companion](https://www.nexusmods.com/skyrimspecialedition/mods/51874)
 - [Serana Dialogue Add-On](https://www.nexusmods.com/skyrimspecialedition/mods/32161)
 - [Song of the Green (Auri Follower)](https://www.nexusmods.com/skyrimspecialedition/mods/11278)
 - [Val Serano - Pirate Custom Voiced Follower and Quest Adventure](https://www.nexusmods.com/skyrimspecialedition/mods/103669)

### Player Homes

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720691342-1079637258.png)

 - [Elianora's Breezehome Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/2829)
 - [Mirele Bismath Reborn](https://www.nexusmods.com/skyrimspecialedition/mods/93817)
 - [Tel Jerdein - Telvanni Sorcerer Tower](https://www.nexusmods.com/skyrimspecialedition/mods/33539)
