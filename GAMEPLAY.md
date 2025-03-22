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
- [Overview and Basics](#overview-and-basics)
  - [Core Overhauls](#core-overhauls)
    - [Archon - Faiths of Tamriel](#archon---faiths-of-tamriel)
    - [Paragon - A Modern Perk Overhaul](#paragon---a-modern-perk-overhaul)
    - [Additional Edits](#additional-edits)
  - [Combat Foundations](#combat-foundations)
- [Leveling and Progression](#leveling-and-progression)
  - [Changes to Leveling](#changes-to-leveling)
  - [Perk Point Acquisition](#perk-point-acquisition)
- [Difficulty and Mechanics](#difficulty-and-mechanics)
  - [Difficulty-based Mechanics](#difficulty-based-mechanics)
  - [New and Notable Mechanics](#new-and-notable-mechanics)
- [Quests Changes](#quests-changes)
- [New Armors and Weapons](#new-armors-and-weapons)
- [Content Additions and Improvements](#content-additions-and-improvements)
  - [Followers](#followers)
  - [New Quests](#new-quests)
  - [Vanilla Quest Expansions and Edits](#vanilla-quest-expansions-and-edits)
  - [Player Homes](#player-homes)

## Initial Setup

Before reading this guide, please follow the [Installation Guide](https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md) as it will answer the vast majority of technical questions related to getting the list setup and running. Be sure to check out the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md) page to learn more about the controller support, optional tweaks, addons, MCM options, and more.

## Overview and Basics

This section will cover the absolute basics of the list. I suggest reading, or skimming all of the linked mod pages in this section if you are unfamiliar with the preceding mods.

Before reading this section, I suggest looking over the [load order](https://loadorderlibrary.com/lists/Apostasy) and [keybinds](https://github.com/Oghma-Infinium/Apostasy/blob/main/images/Keybinds.png).

### Core Overhauls

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/GameplayHeader.png)

 - Apostasy uses a custom Perk Overhaul for all Warrior and Thief skills and Custom-made perks for Alteration and Enchanting. Read more about it [here](#paragon---a-modern-perk-overhaul)!
 - Apostasy uses a custom encounter zone and level scaling mod to **delevel** the world, instituting minimum and maximum level caps for every dungeon.
 - [Nirn's Chosen](https://www.nexusmods.com/skyrimspecialedition/mods/121427) and [Stones of Sacrifice](https://www.nexusmods.com/skyrimspecialedition/mods/121629) cover the Race and Standing Stones overhauls within the list.
 - Apostasy uses a custom Religion Overhaul to cover the Nine Divines, the Seventeen Daedric Princes, Auriel, and Magnus. Read more about it [here](#archon---faiths-of-tamriel)!
   - "Faith" is broken down into three "tiers".
     - Tier 1: The Shrine Blessing.
     - Tier 2: A scaling bonus that gets stronger by completing certain tasks relevant to the deity.
     - Tier 3: A capstone bonus granted for completing a specific quest or feat.
 - [Sacrilege](https://www.nexusmods.com/skyrimspecialedition/mods/42408/) and [Growl](https://www.nexusmods.com/skyrimspecialedition/mods/31245) overhaul the Vampire and Werewolf systems.
   - Both have been heavily customized to fit better within the balance of the list, specific changes are discussed [here](#additional-edits).
 - [Apothecary](https://www.nexusmods.com/skyrimspecialedition/mods/52130) and [Thaumaturgy](https://www.nexusmods.com/skyrimspecialedition/mods/57138) cover Alchemy and Enchanting respectively.
 - [Artificer](https://www.nexusmods.com/skyrimspecialedition/mods/99619), [Artifacts of the Ancestors](https://www.nexusmods.com/skyrimspecialedition/mods/92389), and [Mysterious Mementos](https://www.nexusmods.com/skyrimspecialedition/mods/118342) overhaul unique artifacts and add several new ones.
   - Some tweaks have been made for items to fit into the list better, specific changes are discussed [here](#additional-edits).
 - [Stormcrown](https://www.nexusmods.com/skyrimspecialedition/mods/90659) overhauls the vanilla shout system, improving the vanilla shouts, adding new ones, and completely overhauling the meditation system.
   - Some shouts have been tweaked to function better within the list.
 - [Gourmet](https://www.nexusmods.com/skyrimspecialedition/mods/96876) overhauls food and drink, transforming the traditional "eat 30 cheese wheels mid combat" into a more complex buff system.
 - [Starfrost](https://www.nexusmods.com/skyrimspecialedition/mods/97536) manages the Survival changes, such as Exhaustion, Hunger, and Warmth.

#### Archon - Faiths of Tamriel

Archon is an overhaul of Skyrim's religion system that focuses on enhancing and adding deities native to Skyrim's world. Archon is heavily inspired by [Pilgrim](https://www.nexusmods.com/skyrimspecialedition/mods/54099) and [3Tweaks](https://sites.google.com/view/3bftweaksrequiem/character/divine)' implementation of Religion.  

Deity buffs are granted by praying at a shrine associated with that deity. New shrines are added around Skyrim to find and receive blessings from. Buffs are broken up into three major categories: (1) Blessings - these are the base benefits you get by praying at a shrine; (2) Acolyte - these are scaling bonuses that are unlocked and become stronger by performing activities associated with a given deity; (3) Champion - these are capstone bonuses that are unlocked by completing specific quests or feats of strength, in some cases capstones include additional restrictions.

<Details>
<summary>The Divines</summary>

**Akatosh**
 1. **Blessing of Akatosh**: You have a 10% chance to absorb the Magicka from incoming spells. 
 2. **Acolyte of Akatosh**: Your Shouts recover 10-25% faster after completing 5-40 quests.
 3. **Champion of Akatosh**: Your Health, Magicka, and Stamina is increased by 25 after completing [Dragonslayer](https://en.uesp.net/wiki/Skyrim:Dragonslayer).

**Arkay**
 1. **Blessing of Arkay**: Your Health is increased by 50.
 2. **Acolyte of Arkay**: Your Armor Rating is increased by 25-100 after slaying 10-250 undead.
 3. **Champion of Arkay**: Your Health recovers up to 100% faster based on your missing Health after completing [The Wolf Queen Awakened](https://en.uesp.net/wiki/Skyrim:The_Wolf_Queen_Awakened), additionally you can not be a Vampire, possess the [Necromancer's Amulet](https://en.uesp.net/wiki/Skyrim:Necromancer_Amulet), or complete [The Taste of Death](https://en.uesp.net/wiki/Skyrim:The_Taste_of_Death).

**Dibella**
 1. **Blessing of Dibella**: Your Stamina Regeneration is increased by 50%.
 2. **Acolyte of Dibella**: Your Poise Resistance is increased by 5-20% after passing 3-25 persuasion checks.
 3. **Champion of Dibella**: Your Stamina recovers up to 100% faster based on your missing Stamina after completing [The Heart of Dibella](https://en.uesp.net/wiki/Skyrim:The_Heart_of_Dibella) and [Caught Red Handed](https://en.uesp.net/wiki/Skyrim:Caught_Red_Handed), additionally can not join The Dark Brotherhood.

**Julianos**
 1. **Blessing of Julianos**: Your Magicka is increased by 50.
 2. **Acolyte of Julianos**: Your spells and enchantments cost 4-10% less after learning 5-40 spells.
 3. **Champion of Julianos**: Your Magicka recovers up to 100% faster based on your missing Magicka after completing a [Ritual Quest](https://en.uesp.net/wiki/Category:Skyrim-Quests-College_of_Winterhold-Spell_Rituals), additionally can not join The Thieves Guild.

**Kynareth**
 1. **Blessing of Kynareth**: Your Stamina is increased by 50.
 2. **Acolyte of Kynareth**: Your Stamina Regeneration is increased by 20-50% after discovering 25-150 locations.
 3. **Champion of Kynareth**: You move 20% faster after bringing the Gildergreen sapling back to Whiterun during [The Blessings of Nature](https://en.uesp.net/wiki/Skyrim:The_Blessings_of_Nature).

**Mara**
 1. **Blessing of Mara**: Your Magicka Regeneration is increased by 50%.
 2. **Acolyte of Mara**: Your Magic Resistance is increased by 10-25% after clearing 5-40 dungeons.
 3. **Champion of Mara**: You restore 20 Health per second to nearby allies after completing [The Book of Love](https://en.uesp.net/wiki/Skyrim:The_Book_of_Love) and [Waking Nightmare](https://en.uesp.net/wiki/Skyrim:Waking_Nightmare), additionally can not join The Dark Brotherhood.

**Stendarr**
 1. **Blessing of Stendarr**: Your Health Regeneration is increased by 50%.
 2. **Acolyte of Stendarr**: You are 10-25% better at blocking and bashing after slaying 2-20 daedra.
 3. **Champion of Stendarr**: Your attacks deal additional Sun damage after completing [Laid to Rest](https://en.uesp.net/wiki/Skyrim:Laid_to_Rest), additionally you can not be a Vampire, Werewolf, or side with Molag Bal in [The House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).

**Talos**
 1. **Blessing of Talos**: Your Shouts recover 25% faster.
 2. **Acolyte of Talos**: You deal 10-25% extra Poise damage after absorbing 2-15 dragon souls.
 3. **Champion of Talos**: Your Shouts are 25% stronger and last 50% longer after completing the Civil War, additionally you can not side with Ondolemar in [Search and Seizure](https://en.uesp.net/wiki/Skyrim:Search_and_Seizure).

**Zenithar**
 1. **Blessing of Zenithar**: Your Carry Weight is increased by 50.
 2. **Acolyte of Zenithar**: You receive 5-20% better prices after bartering* 50-500 times.
 3. **Champion of Zenithar**: You can temper all items by two additional tiers after completing [Lost to the Ages](https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages) and [Unfathomable Depths](https://en.uesp.net/wiki/Skyrim:Unfathomable_Depths), additionally can not join The Thieves Guild.

*Buying or selling a single item is considered "Bartering".

</Details>

<Details>
<summary>The Daedra</summary>

**Azura**
 1. **Blessing of Azura**: Your Magicka is increased by 50.
 2. **Acolyte of Azura**: Your weapon enchantments are 20-50% stronger after using 25-175 soul gems.
 3. **Champion of Azura**: You have a 20% chance to absorb the Magicka from incoming spells after cleansing Azura's Star during [The Black Star](https://en.uesp.net/wiki/Skyrim:The_Black_Star).

**Boethiah**
 1. **Blessing of Boethiah**: Your Stamina is increased by 50.
 2. **Acolyte of Boethiah**: You spend 5-20% less Stamina when power attacking or drawing a bow after slaying* 40-350 people.
 3. **Champion of Boethiah**: Killing an enemy with a melee or ranged weapon restores 100 Health after completing [Boethiah's Calling](https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling), additionally you can not be a Vampire, complete [The Cursed Tribe](https://en.uesp.net/wiki/Skyrim:The_Cursed_Tribe), or side with Molag Bal in [The House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).

**Clavicus Vile**
 1. **Blessing of Clavicus Vile**: You receive 10% better prices.
 2. **Acolyte of Clavicus Vile**: Your Conjuration spells cost 10-25% less Magicka after passing 3-25 persuasion checks.
 3. **Champion of Clavicus**: You can summon or reanimate one additional minion after completing [A Daedra's Best Friend](https://en.uesp.net/wiki/Skyrim:A_Daedra%27s_Best_Friend), additionally you can not be a Werewolf.

**Hermaeus Mora**
 1. **Blessing of Hermaeus Mora**: You have a 10% chance to absorb the Magicka from incoming spells.
 2. **Acolyte of Hermaeus Mora**: You cast spells 5-20% faster after reading 5-75 books.
 3. **Champion of Hermaeus Mora**: Your spells cost 25% less Magicka after reading the [Oghma Infinium](https://en.uesp.net/wiki/Skyrim:Oghma_Infinium) and completing at least one [Black Book](https://en.uesp.net/wiki/Lore:Black_Books).

**Hircine**
 1. **Blessing of Hircine**: Your Movement Speed is increased by 10%.
 2. **Acolyte of Hircine**: Your Stamina Regeneration is increased by 20-50% after slaying 25-300 creatures.
 3. **Champion of Hircine**: Your attacks deal additional Sun damage after completing [Ill Met By Moonlight](https://en.uesp.net/wiki/Skyrim:Ill_Met_By_Moonlight), additionally you must be a Werewolf.

**Jyggalag**
 1. **Blessing of Jyggalag**: Your Armor Rating is increased by 100.
 2. **Acolyte of Jyggalag**: Your Magic Resistance is increased by 10-25% after slaying 2-20 daedra.
 3. **Champion of Jyggalag**: You resist 25% of incoming weapon and spell damage when below half Health after completing [The Mind of Madness](https://en.uesp.net/wiki/Skyrim:The_Mind_of_Madness), additionally you can not be a Vampire, Werewolf, or possess the [Wabbajack](https://en.uesp.net/wiki/Skyrim:Wabbajack).

**Malacath**
 1. **Blessing of Malacath**: Your Stamina is increased by 50.
 2. **Acolyte of Malacath**: You deal 20-50% more damage with power attacks after slaying 40-350 people.
 3. **Champion of Malacath**: Killing an enemy with a melee or ranged weapon restores 100 Stamina after completing [The Cursed Tribe](https://en.uesp.net/wiki/Skyrim:The_Cursed_Tribe), additionally you can not complete [Boethiah's Calling](https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling).

**Mehrunes Dagon**
 1. **Blessing of Mehrunes Dagon**: Your Magicka Regeneration is increased by 50%.
 2. **Acolyte of Mehrunes Dagon**: Your Destruction spells cost 10-25% less Magicka after slaying 40-350 people.
 3. **Champion of Mehrunes Dagon**: You reduce the Fire, Frost, and Shock Resistance of all nearby enemies by 25% after siding with Mehrunes Dagon in [Pieces of the Past](https://en.uesp.net/wiki/Skyrim:Pieces_of_the_Past).

**Mephala**
 1. **Blessing of Mephala**: Your Health is increased by 50.
 2. **Acolyte of Mephala**: Your Health Regeneration is increased by 20-50% after committing 2-20 murders.
 3. **Champion of Mephala**: You deal 50% extra damage against targets who are attacking or when striking targets from behind after siding with Mephala in [The Whispering Door](https://en.uesp.net/wiki/Skyrim:The_Whispering_Door).

**Meridia**
 1. **Blessing of Meridia**: Your Magicka Regeneration is increased by 50%.
 2. **Acolyte of Meridia**: Your Restoration spells cost 10-25% less Magicka after slaying 10-250 undead.
 3. **Champion of Meridia**: Your Magic Resistance is increased by 25% after completing [The Break of Dawn](https://en.uesp.net/wiki/Skyrim:The_Break_of_Dawn), additionally you can not be a Vampire, or side with Molag Bal in [The House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).

**Molag Bal**
 1. **Blessing of Molag Bal**: Your Magicka is increased by 50.
 2. **Acolyte of Molag Bal**: Your Magicka Regeneration is increased by 20-50% after trapping 20-100 souls.
 3. **Champion of Molag Bal**: As a vampire, you deal 50% extra damage to enemies who fall below half Health after siding with Molag Bal in [The House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors), additionally you can not complete [Boethiah's Calling](https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling).

**Namira**
 1. **Blessing of Namira**: Your Health Regeneration is increased by 50%.
 2. **Acolyte of Namira**: You reflect 20-50% of incoming melee damage back at your attacker after committing 2-20 murders.
 3. **Champion of Namira**: After consuming a corpse, you reduce the Armor Rating of all nearby enemies by 150, after completing [The Taste of Death](https://en.uesp.net/wiki/Skyrim:The_Taste_of_Death), additionally as Namira's Champion you are able to feed on corpses without wearing the [Ring of Namira](https://en.uesp.net/wiki/Skyrim:Ring_of_Namira).

**Nocturnal**
 1. **Blessing of Nocturnal**: You are 20% harder to detect while sneaking.
 2. **Acolyte of Nocturnal**: Your Carry Weight is increased by 20-50 after picking 10-100 pockets.
 3. **Champion of Nocturnal**: You move 20% faster while sneaking after returning the [Skeleton Key](https://en.uesp.net/wiki/Skyrim:Skeleton_Key) to Nocturnal.

**Peryite**
 1. **Blessing of Peryite**: Your Stamina Regeneration is increased by 50%.
 2. **Acolyte of Peryite**: Your poisons last for 20-50% more hits after slaying 20-200 automatons.
 3. **Champion of Peryite**: You reduce the Poison Resistance of all nearby enemies by 50% after siding with Peryite during [The Only Cure](https://en.uesp.net/wiki/Skyrim:The_Only_Cure).

**Sanguine**
 1. **Blessing of Sanguine**: Your Stamina Regeneration is increased by 50%.
 2. **Acolyte of Sanguine**: You deal 10-25% extra unarmed damage after winning 1-9 brawls.
 3. **Champion of Sanguine**: Your potions last 100% longer after completing [A Night to Remember](https://en.uesp.net/wiki/Skyrim:A_Night_To_Remember).

**Sheogorath**
 1. **Blessing of Sheogorath**: Your Health is increased by 50.
 2. **Acolyte of Sheogorath**: Your potions last 20-50% longer after plucking 6-72 butterfly wings.
 3. **Champion of Sheogorath**: Your attacks and spells randomly deal between 3% and 3,200% of their total damage after completing [The Mind of Madness](https://en.uesp.net/wiki/Skyrim:The_Mind_of_Madness).

**Vaermina**
 1. **Blessing of Vaermina**: Your Magicka Regeneration is increased by 50%.
 2. **Acolyte of Vaermina**: Your Illusion spells cost 10-25% less Magicka after using 25-175 soul gems.
 3. **Champion of Vaermina**: You absorb 20 points of Magicka per second from nearby enemies affected by an Illusion spell after completing [Waking Nightmare](https://en.uesp.net/wiki/Skyrim:Waking_Nightmare), additionally you can not be a Werewolf.

*Slaying People is not the same as Murder, killing Bandits would be considered "slaying people".

</Details>

<Details>
<summary>Miscellaneous Deities</summary>

**Auriel**
 1. **Blessing of Auriel**: Your Magicka is increased by 50.
 2. **Acolyte of Auriel**: Your Restoration spells cost 10-25% less Magicka after learning 5-40 spells.
 3. **Champion of Auriel**: 

**Magnus**
 1. **Blessing of Magnus**: You have a 10% chance to absorb the Magicka from incoming spells. 
 2. **Acolyte of Magnus**: Your Alteration spells cost 10-25% less Magicka after learning 5-40 spells.
 3. **Champion of Magnus**: Your Magic Resistance is increased by 25% after completing [The Eye of Magnus](https://en.uesp.net/wiki/Skyrim:The_Eye_of_Magnus).

**Sithis**
 1. **Blessing of Sithis**: You are 20% harder to detect while sneaking.
 2. **Acolyte of Sithis**: You deal 10-25% more damage with sneak attacks after 20-150 successful sneak attacks.
 3. **Champion of Sithis**: You spend 50% less Stamina while sneaking after completing [Hail Sithis!](https://en.uesp.net/wiki/Skyrim:Hail_Sithis!).

</Details>

#### Paragon - A Modern Perk Overhaul

Paragon is an overhaul of Skyrim’s Combat and Stealth perk trees with the aim of redesigning and balancing skills and perks around a Modern Combat setup. Paragon was built from the ground up with Apostasy in mind and currently covers 14 out of the 18 trees, the remaining 4 trees are covered under [Additional Edits](#additional-edits). In addition to perks, Paragon also controls a large majority of Apostasy's Stamina system.

<Details>
<summary>Alchemy</summary>

**Alchemist (10/50)**: Crafted potions and poisons are 50/100% stronger.

**Experimenter (20)**: Eating an ingredient reveals all of its effects.  
**Green Thumb (40/70)**: You gather one/two extra ingredient/s from plants.  
**Purity (80)**: All negative effects are removed from crafted potions, and all positive effects are removed from crafted poisons.

**Intensity (30)**: Poisons last for up to 10 additional hits based on your Alchemy skill.  
**Solvency (60)**: Crafted poisons are 25% stronger.  
**Overdose (90)**: Your attacks against Poisoned targets deal additional Poison damage to all nearby enemies.

**Concentration (30)**: Potions last up to 100% longer based on your Alchemy skill.  
**Potency (60)**: Crafted potions are 25% stronger.  
**Philosopher's Stone (90)**: Consuming a beneficial potion or ingredient gives a chance to receive an additional side effect.

**Chemist (100)**: You create twice as many potions and poisons from the same number of ingredients.

</Details>

<Details>
<summary>Alteration</summary>

**Evoker (10/50)**: Alteration spells cost 25/50% less Magicka.

**Meditation (20/60)**: Your Magicka Regeneration is increased by 50/100% while wearing robes.  
**Mage Armor (40)**: While wearing robes, armor spells are twice as strong and allow you to resist 50% of incoming Poise damage.  
**Arcane Attunement (70)**: You cast spells 20% faster while wearing robes.  
**Arcane Awakening (100)**: Your Magicka Regenerates 50% faster for 10 seconds after casting a spell.

**Balance (30/70)**: Alteration spells last 50/100% longer.

**Ocato's Recital (40)**: Entering combat automatically activates the most effective armor spell you know. This effect can only occur once every 5 minutes.  
**Distortion (60)**: While under the effects of an armor spell, your dodges are enhanced and jumping costs 20% less Stamina.  
**Streak (70)**: While under the effects of an armor spell, your dodges deal Shock damage to nearby enemies.  
**Arcane Warding (80)**: While under the effect of an armor spell, your Magic Resistance is increased by 25%.  
**Golem (90)**: While under the effect of an armor spell, you have a 20% chance to absorb the Magicka from incoming spells.

</Details>

<Details>
<summary>Archery</summary>

**Marksman (10/50)**: Bows and Crossbows deal 25/50% more damage.

**Cheap Shot (30)**: While wielding a bow or crossbow, bashing reduces the target's movement speed for 30 seconds.  
**Pocket Sand (90)**: Cheap Shot has a chance to immobilize the target for 10 seconds.

**Piercing Shot (30/70)**: Bows and crossbows apply Gaping Wounds, dealing additional bleeding damage over 5/10 seconds.  
**Overdraw (40/80)**: Bows and crossbows deal 25/50% more Poise damage.

**Ranger (20/70)**: You draw your bow and reload your crossbow much faster. / and you move much faster while drawing a bow or wielding a crossbow.  
**Steady Hand (60)**: Zooming in with a bow or crossbow slows down time by up to 50% and costs 25% less Stamina.  
**Beast Master (100)**: Hitting a target with a bow or crossbow has a chance to summon a random Spirit Summon for 30 seconds. This effect can only occur once every 30 seconds.

</Details>

<Details>
<summary>Block</summary>

**Gladiator (10/50)**: Blocking and bashing are 25/50% more effective.

**Frontline Tactics (30/70)**: Blocking with a shield reduces incoming arrow/and spell damage by 50%. Successful timed blocks with a shield negate incoming arrow/and spell damage.  
**Second Wind (60)**: Successful timed blocks with a shield restores 20 Stamina.  
**Bloodbath (90)**: Successful timed blocks with a shield deal bleeding damage over 10 seconds to nearby enemies and restores 20 Health.

**Blocking Expertise (40)**: Blocking and bashing cost 50% less Stamina.  
**Defensive Maneuvers (60)**: Blocking no longer slows your movement and you can now sprint while blocking.

**Victimize (20)**: Successfully timed blocking a target below half Stamina causes them to become stunned.  
**Punishment (40)**: Bashing deals five times more damage and power bashing deals Stamina damage over 10 seconds.  
**Deliverance (80)**: Power attacks cost 20% less Stamina after a successful timed block for 3 seconds.  
**Death Blow (100)**: Power attacks deal 50% more damage after a successful timed block for 3 seconds. This bonus is doubled against stunned targets.

</Details>

<Details>
<summary>Enchanting</summary>

**Artificer (10/50)**: Crafted enchantments are 50/100% stronger and soul gems restore 50/100% more charge.

**Jewelry Enchanter (20)**: Crafted jewelry enchantments are 50% stronger.  
**Armor Enchanter (40/80)**: Crafted armor and clothing enchantments are 25/50% stronger.  
**Weapon Enchanter (40/80)**: Crafted weapon enchantments are 25/50% stronger.  
**Twin Secrets (100)**: You can place two enchantments on a single item.

**Resonance (20)**: Weapon enchantments cost 50% less charge.  
**Power Surge (60)**: Weapon enchantments are 50% stronger when delivered by a power attack.

**Sage (20/60)**: Scrolls last twice/four times as long.  
**Scribe (30/70)**: Scrolls are 50/100% stronger.

**Channeler (30/70)**: Equipped staves slowly/quickly regenerate charge outside of combat.  
**Arcane Infusion (90)**: While in combat, your equipped staff drains 5 Magicka per second. While you have Magicka remaining, your staves are twice as effective.

</Details>

<Details>
<summary>Hand to Hand</summary>

**Pugilist (10/50)**: Unarmed strikes deal 25/50% more damage.

**Heavy Blows (30/70)**: While in Wolf Stance, unarmed strikes apply Concussion, dealing Stamina damage over 5/10 seconds and preventing regeneration.  
**Debilitating Strikes (40/80)**: Concussion deals more/significantly more Stamina damage.  
**Switch-Hitter (100)**: While in Wolf Stance, unarmed power attacks deal up to double damage based on the target's missing Stamina.

**Ferocious Assault (30/70)**: While in Hawk Stance, unarmed strikes are 10/20% more likely to deal critical damage.  
**Overwhelm (40/80)**: Critical strikes with unarmed strikes deal more/significantly more damage.  
**Haymaker (100)**: While in Hawk Stance, unarmed power attacks are guaranteed to deal critical damage if the target is staggered or when striking from behind.  

**Underhanded Strike (30/70)**: While in Bear Stance, unarmed strikes apply Daze, reducing the target's movement speed and casting speed by 10/20% for 10 seconds.  
**Pressure Fighter (40/80)**: While in Bear Stance, unarmed strikes deal 25/50% more Poise damage to Dazed targets.  
**Finisher (100)**: While in Bear Stance, unarmed power attacks have a chance to knock an enemy down.

**Brawler (20)**: Power attacks while unarmed cost 20% less Stamina.  
**Knockout (40)**: Power attacks while unarmed deal 50% more damage.

**Brace (60/90)**: You resist 10/20% of incoming weapon and spell damage while unarmed.

</Details>

<Details>
<summary>Heavy Armor</summary>

**Defender (10/50)**: Heavy Armor is 50/100% more effective and its encumbrance penalty is reduced by 50/100%.

**Juggernaut (30)**: Your Armor Rating is increased by 100 while wearing a Heavy Armor chest piece.

**Unstoppable (40)**: You resist 20% of incoming Poise damage while wearing a Heavy Armor chest piece.  
**Constitution (60)**: You resist 50% of incoming bleeding and critical damage while wearing a Heavy Armor chest piece.  
**Infernal Armor (90)**: Incoming spell damage is reduced by up to 40%, based on Armor Rating while wearing a heavy armor chest piece.

**Unyielding (20/70)**: Your Health Regeneration is increased by 50/100% while wearing a Heavy Armor chest piece.  
**Defiance (40/90)**: You resist 25/50% of incoming weapon and spell damage when power attacking, drawing a bow, or casting a spell while wearing a Heavy armor chest piece.  
**Resolve (80)**: When you are struck by a hostile attack or spell, your Health regenerates 50% faster for 10 seconds.  
**Imposing Presence (100)**: You reduce the damage of nearby enemies by 20%, when you fall below half Health you absorb Health from nearby enemies.

</Details>

<Details>
<summary>Light Armor</summary>

**Scout (10/50)**: Light Armor is 50/100% more effective and its encumbrance penalty is reduced by 50/100%.

**Specialist (30)**: Your Armor Rating is increased by 100 while wearing a Light Armor chest piece.

**Acrobat (40)**: Dodging costs 25% less Stamina while wearing a Light Armor chest piece.  
**Edgerunner (90)**: Successful dodges briefly slow time while wearing a Light Armor chest piece.

**Agility (20/70)**: Your Stamina Regeneration is increased by 50/100% while wearing a Light Armor chest piece.  
**Endurance (60)**: You resist 50% of all incoming Stamina damage and Slow effects while wearing a light armor chest piece.

**Windrunner (40/90)**: Your move 10/20% faster and sprinting costs 25/50% less Stamina while weaing a Light Armor chest piece.  
**Momentum (80)**: When you cast a spell or attack an enemy, your Stamina regenerates 50% faster for 10 seconds.

**Pit Fighter (100)**: You deal up to 50% more damage based on the number of nearby enemies.

</Details>

<Details>
<summary>One-Handed</summary>

**Skirmisher (10/50)**: One-handed weapons deal 25/50% more damage.

**Grievous Wounds (30/70)**: While in Wolf Stance, attacks with One-Handed weapons apply Grievous Wounds, dealing additional bleeding damage over 5/10 seconds.  
**Carve and Spit (40/80)**: Grievous Wounds deal more/significantly more damage.  
**Veinripper (100)**: While in Wolf Stance, power attacks with One-Handed weapons against targets affected by Grievous Wounds have a chance to cause them to rupture and restore Health.

**Overbearing Assault (30/70)**: While in Hawk Stance, attacks with One-Handed weapons are 10/20% more likely to deal critical damage.  
**Ravage (40/80)**: Critical strikes with One-Handed weapons deal more/significantly more damage.  
**Focused Strike (100)**: While in Hawk Stance, power attacks with One-Handed weapons increase your critical strike damage by 50% for 10 seconds.

**Shattering Strikes (30/70)**: While in Bear Stance, attacks with One-Handed weapons apply Rend, reducing Armor Rating by 150/300 for 10 seconds.  
**Furious Fighter (40/80)**: While in Bear Stance, One-Handed weapons deal 25/50% more Poise damage to Rended targets.  
**Bonebreaker (100)**: While in Bear Stance, power attacks with One-Handed weapons reduce the target's movement speed and weapon damage by 25% for 10 seconds.

**Veteran (20)**: Power Attacks with One-Handed weapons cost 20% less Stamina.  
**Overrun (40)**: Power Attacks with One-Handed weapons deal 50% more damage.

**Ambush (60/90)**: Attacks with One-Handed weapons deal 25/50% more damage against targets who are attacking or when striking targets from behind while your left hand is empty.  
**Overwhelming Rage (60/90)**: While dual wielding, consecutive attacks against the same target deal up to 25/50% more damage.  
**Corrupted Catalyst (60/90)**: Attacks with a One-Handed weapon deal additional damage / and proc additional effects based on the damage-dealing spell in your off-hand.

</Details>

<Details>
<summary>Security</summary>

**Cutpurse (10/50)**: You are 50/100% more likely to succeed at lockpicking and pickpocketing.

**Icepick (30/70)**: You can lockpick basic/advanced automatons to shut them down.

**Deep Pockets (20/60)**: Your Carry Weight is increased by 50/100.

**Fatal Concoction (30/70)**: You can harm enemies by placing poisons in their pockets. / Poisons that you place in enemy pockets deal 100% more damage.  

**Nimble Fingers (40)**: Your maximum chance to succeed at pickpocketing is increased to 100%.  
**Misdirection (80)**: You can pickpocket equipped weapons.  
**Perfect Touch (100)**: You can pickpocket equipped armor and jewelry.

**Locksmith (40)**: You are much more likely to succeed at picking Expert and Master locks and your lockpick starts closer to the opening position.  
**Treasure Hunter (60)**: You find more rare loot in dungeons.  
**Dungeon Master (90)**: You have a chance to find more valuable equipment in any chest.

</Details>

<Details>
<summary>Smithing</summary>

**Craftsman (10/50)**: You can temper all items by one/two additional tiers.

**Blacksmith (30)**: You can temper all items by one additional tier.  
**Armorer (70)**: You can temper all items by one additional tier.  
**Forgemaster (90)**: You can temper all items by one additional tier.

**Sculptor (40)**: You can create unique Talismans at any forge that provide additional bonuses when equipped.  
**Runecarver (70)**: You can upgrade Talismans at any forge, gaining an additional special effect.

**Basic Smithing (20)**: You can create Steel and Leather items at any forge.  
**Journeyman Smithing (40)**: You can create Dwarven, Scaled, and Steel Plate items at any forge.  
**Intermediate Smithing (60)**: You can create Nordic, Orcish, and Elven items at any forge.  
**Advanced Smithing (80)**: You can create Ebony, Glass, and Stalhrim items at any forge.  
**Mythic Smithing (100)**: You can create Daedric and Dragon items at any forge.

</Details>

<Details>
<summary>Sneak</summary>

**Agent (10/50)**: You are 25/50% harder to detect and consume 25/50% less Stamina while sneaking.

**Silent Casting (30)**: Your spells are silent to others.  
**Shadowcaster (40/80)**: Sneak attacks with spells deal 50/100% more damage.

**Focused Aim (30)**: You spend 50% less Stamina when drawing a bow while sneaking.  
**Deadly Aim (40/80)**: Sneak attacks with bows deal 50/100% more damage.

**Merciless (20/70)**: Sneak attacks with melee weapons deal 50/100% more damage.  
**Backstab (30)**: Sneak attacks with one-handed weapons deal 50% more damage when striking targets from behind.  
**Master Assassin (60/90)**: Sneak attacks with daggers deal 50/100% more damage.

**Trespasser (20)**: You can execute a silent roll while sneaking, increasing your movement speed by 20% for 10 seconds.  
**Infiltrator (40)**: You no longer trigger traps and make 50% less noise while moving.  
**Cloak of Shadows (60)**: Sneaking in combat restores 10 Health per second for 10 seconds and causes enemies to stop searching for you. This effect can occur once every 60 seconds.  
**Subterfuge (80)**: Performing a silent roll grants you invisibility for 10 seconds. This effect can occur once every 30 seconds.  
**Lingering Shadow (100)**: Your sneak attacks deal 100% more damage while under the effects of Subterfuge and for an additional 3 seconds after it ends.

</Details>

<Details>
<summary>Speech</summary>

**Merchant (10/50)**: You receive 10/20% better prices.

**Silver Tongue (30)**: You are much more likely to succeed at persuasion and intimidation, and you can bribe guards to ignore crimes.

**Supply and Demand (20/70)**: Merchants have extra gold / even more gold available for bartering.  
**Investor (80)**: You can invest in a merchant’s business to increase their available gold.  
**Good for Business (100)**: Merchants you have invested in sell additional high quality goods.

**Profiteer (40/70)**: You can sell any item /, including stolen items, to any merchant in Tamriel.

**Kinship (30)**: Your Companions' Health is increased by 100.  
**Legion (40)**: Your Companions' Armor Rating is increased by 150, and they receive 25% less incoming spell damage.  
**Inspiring Leader (90)**: Your Companions regenerate Health, Magicka, and Stamina while you are above half for the respective attribute.

</Details>

<Details>
<summary>Two-Handed</summary>

**Champion (10/50)**: Two-handed weapons deal 25/50% more damage.

**Mortal Wounds (30/70)**: While in Wolf Stance, attacks with Two-Handed weapons apply Mortal Wounds, dealing additional bleeding damage over 5/10 seconds.  
**Rip and Tear (40/80)**: Mortal Wounds deal more/significantly more damage.  
**Death Strike (100)**: While in Wolf Stance, power attacks with Two-Handed weapons against targets affected by Mortal Wounds leech Health. This effect can only occur once every 10 seconds per target.

**Savage Assault (30/70)**: While in Hawk Stance, attacks with Two-Handed weapons are 10/20% more likely to deal critical damage.  
**Devastate (40/80)**: Critical strikes with Two-Handed weapons deal more/significantly more damage.  
**Sudden Death (100)**: While in Hawk Stance, power attacks with Two-Handed weapons are up to five times as likely to deal critical damage based on the target's missing Health.

**Crushing Blow (30/70)**: While in Bear Stance, attacks with Two-Handed weapons apply Sunder, reducing Armor Rating by 150/300 for 10 seconds.  
**Brutal Fighter (40/80)**: While in Bear Stance, Two-Handed weapons deal 25/50% more Poise damage to Sundered targets.  
**Skullcrusher (100)**: While in Bear Stance, power attacks with Two-Handed weapons smash through enemy block, interrupt spellcasting, and interrupt targets drawing a bow. Successful block breaks and interrupts restore 20 Stamina.

**Battlemaster (20)**: Power attacks with Two-Handed weapons cost 20% less Stamina.  
**Overpower (40)**: Power attacks with Two-Handed weapons deal 50% more damage.

**Doom Winds (60)**: After performing 5 or more light attacks with Two-Handed weapons, your next power attack releases a gust of wind, staggering nearby enemies. This effect can only occur once every 15 seconds.  
**Heroism (90)**: After unleashing Doom Winds, you restore 100 Stamina.

</Details>

#### Additional Edits

The list includes a multitude of changes to core mods, below I will attempt to list out the important ones.

<Details>
<summary>Additional Perk Changes</summary>

Apostasy uses Adamant to be the main overhaul for perk trees that are untouched by Paragon. However, the list makes several edits to these perk trees to make the progression more in line with the other trees handled by Paragon and to incorporate modded content better. Below is the list of notable changes to these trees.

**Conjuration**
 - Removed the Cultist perks.

**Destruction**
 - Changed the skill requirements for several perks.
   - **Spell Surge** now requires 30 skill (was 20).
   - **Spell Surge** now reduces dual casting costs by 20% (was 25%).
   - **Augment [X]` perks now require 20 skill (was 30).
   - Tier 1 specialization perks (e.g., **Firebrand`, **North Wind`, etc.) now require 40/90 skill (was 60/90).
   - **Impact** now requires 70 skill (was 40).
 - Incorporated [Ascension](https://www.nexusmods.com/skyrimspecialedition/mods/89223) to give perk bonuses to non-elemental Destruction skills.
   - Unaspected spells include Destruction school spells from [Desecration](https://www.nexusmods.com/skyrimspecialedition/mods/90832) and [Natura](https://www.nexusmods.com/skyrimspecialedition/mods/77826).
   - Unaspected spells do not include Vampire or Drain spells, those scale with perks in the Vampire Lord tree.
   - **Execution** perk now requires 40/90 skill and **Raw Power** (was 80/100 skill and **Aspection`).
   - **Aspection** perk now requires 100 skill and **Execution** (was 60 skill and **Raw Power`).
   - **Magic Mantle** removed.
   - **Destructive Barrier** now requires **Spell Surge** (was **Magic Mantle`).
   - New Perk, **Fevered Incantation**, added.
     - Requires 60 skill and **Destructive Barrier**. Doubles the damage dealt by *elemental* cloaks (e.g., Flame Cloak).

**Restoration** 
 - Changed the skill requirements for several perks.
   - **Dawn's Wrath** now requires 30/70 skill (was 40/80).
   - **Empowered Ward** now requires 30 skill (was 20).
   - **Affliction** and **Divine Glory** now require 20/60 skill (was 30/70).
   - **Plague** and **Power of the Light** now require 40/90 skill (was 60/90).
   - New Perk, **Enduring Ideal**, added.
     - Requires 80 skill and **Power of the Light**. Allows Sun spells to affect living, Daedra, and Dwarven automatons.
   - New Perk, **Sanctification**, added.
     - Requires 100 skill and **Enduring Ideal**. Provides Sun spells an execute proc similar to Destruction capstones (e.g., **Wildfire**).

</Details>

<Details>
<summary>Alchemy Changes</summary>

By default, [Apothecary](https://www.nexusmods.com/skyrimspecialedition/mods/52130)'s Restore potions (e.g., Minor Potion of Healing) last for 10 seconds. Due to the changes to potion drinking in Apostasy, keenly the animation, the duration of these potions has been reduced to 4 seconds, and their magnitude has been appropriately buffed.

</Details>

<Details>
<summary>Artifact Changes</summary>

Apostasy makes a multitude of changes to Artifacts in the list so that they better suit the balance and mechanics of the list. I'm not going to list them all because that would be too much work, but here are the most notable changes:

 - **Cicero's Gloves**: Fortifies Potion Duration by 50% instead of increasing Attack Speed by 10%.
 - **Gauntlets of the Horny Fist**: Additionally makes unarmed attacks deal additional fire damage.
 - **Severin Family Ring**: Fortifies Poison Use by 20% instead of increasing Attack Speed by 10%.
 - **Silver-Blood Family Ring**: Increases Poison Resist by 50% instead of increasing Attack Speed by 10%.

Technically not artifacts but these are going to be listed here:

 - **Agent of Mara**: Healing spells cost 10% less Magicka.
 - **Sailor's Repose**: While under the effects of alcohol, your Health Regeneration is increased by 50%.

</Details>

<Details>
<summary>Shout Changes</summary>

Apostasy utilizes [Stormcrown](https://www.nexusmods.com/skyrimspecialedition/mods/90659) to overhaul and add new shouts to the world. However, due to some design differences between Apostasy's combat and vanilla-style combat, certain shouts have been tweaked to be more suitable to the list.

Elemental Fury grants your weapons a chance to deal additional elemental damage (similar to Chaos Damage enchantment).
 - Each word adds an additional element (1 word = Fire, 2 words = Fire + Frost, 3 words = Fire + Frost + Shock).
 - The meditation for Elemental Fury doubles the damage of the elemental damage procs. 
 - This shout's duration can be increased by Fortify Shout Duration effects, the damage is unaffected by Fortify Shout Power effects. 

Battle Fury now restores the attributes for yourself and nearby allies.
 - Each word increases the strength of the restore effect.
   - First Word: Stamina
   - Second Word: Magicka
   - Third Word: Health
 - The meditation increases regen of associated attribute(s).
 - The shout's magnitude can be increased by Fortify Shout Power effects and is unaffected by Fortify Shout Duration effects.

Additionally, the two words of Lightning Breath and one word of Poison Breath have been moved to [Icemoth](https://www.nexusmods.com/skyrimspecialedition/mods/109541) in order to replace the word walls added by that mod and improve compatibility in the main worldspace. The walls moved were the two word walls added to Solstheim by [Stormcrown](https://www.nexusmods.com/skyrimspecialedition/mods/90659) and the Lightning Breath word wall east of [Dunshnikh Yal](https://en.uesp.net/wiki/Skyrim:Dushnikh_Yal).

</Details>

<Details>
<summary>Standing Stone Changes</summary>

In an effort to create some more interesting effects that can leverage the unique gameplay components of the list, ~~and because I can never make up my mind regarding certain effects~~, certain Standing Stones are changed compared to the default effect in [Stones of Sacrifice](https://www.nexusmods.com/skyrimspecialedition/mods/121629).

Apostasy's Ritual Stone Effect:
> Spells cast via scrolls and staves are 50% stronger and last twice as long, however regular spells are half as strong and last half as long.

Apostasy's Shadow Stone Effect:
> You move 20% faster, and performing a dodge marks nearby enemies for 3 seconds. Melee attacks against marked enemies restore Stamina. However, your blocking and bashing are 50% less effective.

</Details>

<Details>
<summary>Vampire and Werewolf Changes</summary>

Several changes have been made to [Sacrilege](https://www.nexusmods.com/skyrimspecialedition/mods/42408/) and [Growl](https://www.nexusmods.com/skyrimspecialedition/mods/31245) to better integrate them with the balance of the list. Here is an incomplete list of the changes made.

Vampires: 
 - **Blood from a Stone** perk now allows absorb spells to affect all non-living targets. 
 - **Champion of the Night** passive was removed.
 - **Dark Scion** passive now provides a 25% sneak attack damage bonus instead of a sneak bonus that scales with Vampiric age.
 - **Forsaken** passive halves the effectiveness of Shrine bonuses from the Divines, Auriel, and Magnus.
 - **Hemomancer** perk now has two ranks and buffs all absorb (drain) spells by 25/50%.
 - **Unnatural Strength** passive no longer gives a scaling attack damage bonus based on Vampiric age.
 - Stage 1 Vampirism grants 100% Frost Resist, reducing down to 25% at Stage 4.
 - Stage 1 Vampirism grants 25% Weakness to Fire, increasing to 100% at Stage 4.
 - Rebalanced spells added by [Sacrilege](https://www.nexusmods.com/skyrimspecialedition/mods/42408/).

Werewolves:
 - **Beastblood** passive now grants 100% Weakness to Poison, instead of 25% Weakness to Fire.
 - **Bestial Strength** perk is now 2 ranks instead of 5.
 - **Feral Instincts** perk no longer increases werewolf power attack damage.
 - **Golden Mane** passive (High Elves) now grants 25% Magic Resist while in Beast Form.
 - **Lycanthropic Regen** perk no longer increases base recovery of Health and Stamina, instead it increases Regeneration multiplier.
 - **Swipe** perk now increases werewolf power attack damage instead of providing sweep attack bonus (this bonus is inherent).

</Details>

### Combat Foundations

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720691484-471070989.png)

The following mods are considered the "foundations" of the combat and gameplay for Apostasy:
 - [Stances NG](https://www.nexusmods.com/skyrimspecialedition/mods/117986) provides the ability to swap between multiple stances. By default, stances only contribute to what animations are used, but some perks provide benefits to specific stances!
   - Default keybinds: `X` for Wolf Stance, `Ctrl+X` for Hawk Stance, `Shift+X` for Bear Stance.
   - Stances affect first and third person.
 - [TK Dodge RE](https://www.nexusmods.com/skyrimspecialedition/mods/56956) adds Dodging to the game.
   - Dodges are based on Armor Type. Heavy Armor and Cloth users gets a shorter step dodge with shortened iframes, Light Armor gets a longer roll dodge with longer iframes.
   - The Light Armor skill tree has multiple perks to upgrade your Dodge efficiency.
   - In First person, Dodges are always roll dodges.
 - **Custom Timed Blocking**, if you block just before enemy hit, gain increased block efficiency with a chance to stagger the attacker.
   - The Block skill tree has multiple perks to upgrade Timed Block with additional effects and bonuses.
 - [Maxsu Poise](https://github.com/max-su-2019/MaxsuPoise/blob/master/docs/en/Mechanics%20Manual.md) and [Modern Stagger Lock](https://github.com/max-su-2019/ModernStaggerLock) implement a Poise system, which has been fine tuned for the list. Poise Health can be seen on the Special Bar of TrueHUD (the yellow bar above Health on player and target widgets). The Poise system is discussed in more depth in the [Difficulty and Mechanics](#difficulty-and-mechanics) section.

## Leveling and Progression

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720520004-1902455222.png)

Apostasy modifies the vanilla leveling experience in a way to reward the player for engaging in the world in sensible ways. While perks can be obtained through leveling, the perks gained from leveling alone are unlikely to be sufficient for sustaining a full character build in late game. Below is a general breakdown of what to expect with the leveling and progression system in Apostasy.

### Changes to Leveling

Apostasy uses [Experience](https://www.nexusmods.com/skyrimspecialedition/mods/17751) and [Static Skill Leveling Rewritten](https://www.nexusmods.com/skyrimspecialedition/mods/89940) to handle leveling and progression.

My custom settings are explained below:
<Details>
<summary>XP Breakpoints</summary>

Apostasy modifies the vanilla XP per level requirements.

`requiredXP = 240 + (playerlevel * 20)`

| Level | Cumulative XP Required |  
|     :---:    |     :---:     |  
| 1  | 260  |  
| 10  | 3,500  | 
| 20 | 9,000  | 
| 30 | 16,500  | 
| 40 | 26,000  | 
| 50 | 37,500  | 
| 100 | 125,000 | 

</Details>

<Details>
<summary>Static Skill Leveling Settings</summary>

 - Gain skill points equal to 15 + (1 * playerlevel) for each level up, up to 50 points per level (this cap will be hit at level 40+).
 - You can only store a maximum of 60 skill points per level, therefore **after level 40, you must spend all your skill points at level up or you will waste some points.**
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

### Perk Point Acquisition

Apostasy takes a mixed approach to the acquisition of perks and skills. Providing the player with 60 Perks from level 1-50 (no perks are granted from leveling after level 50) and up to an additional 31 perks from Quests.

<Details>
<summary>Additional Perk Sources</summary>

The following is a list of the additional perk sources in Apostasy.

**Main Quest** (5 perks total)

 - [Dragon Rising](https://en.uesp.net/wiki/Skyrim:Dragon_Rising)
 - [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller)
 - [Alduin's Wall](https://en.uesp.net/wiki/Skyrim:Alduin%27s_Wall)
 - [Elder Knowledge](https://en.uesp.net/wiki/Skyrim:Elder_Knowledge)
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

## Difficulty and Mechanics

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

### Difficulty-based Mechanics

Apostasy overhauls or adds additional mechanics, reminiscent of modern Action RPGs to further enhance the gameplay. Check out the sections below to learn more!

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
<summary>Carry Weight and Encumbrance</summary>

Unlike in the Vanilla game, Carry Weight is no longer increases when you distribute level ups into Stamina. Carry Weight can be increased through alchemy, enchantments and equipment, spells, and some other sources.  

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
<summary>Massive Targets</summary>

Apostasy also introduces a "Massive Target" feature for specific enemy types, such as Giants and Dragons. Massive Targets take reduced damage from Attacks of Opportunity and can not be backstabbed. 

Additionally, Massive Targets have a higher likelihood of inflicting Heavy Staggers.

</Details>

<Details>
<summary>Poise and Stagger</summary>

On Apprentice and Novice difficulty, the player can not be inflicted with Heavy Stagger, unless facing a Massive Target.

On Novice difficulty, incoming Poise damage is reduced by 20% for the player. This results in the player being much more difficult to stagger.

</Details>

### New and Notable Mechanics

<Details>
<summary>Bloodied</summary>

Apostasy introduces a new mechanic referred to as Bloodied. Bloodied targets take more damage from Power Attacks while they are below half Health. The player is not affected by Bloodied on any difficulty.

</Details>

<Details>
<summary>Confusion</summary>

Apostasy introduces a new mechanic referred to as Confusion. Confusion affects mages when they receive a melee attack while casting a spell.

The player can be affected by Confusion on **Expert or higher** difficulties.

</Details>

<Details>
<summary>Item Degradation</summary>

Apostasy utilizes [Simple Degradation](https://www.nexusmods.com/skyrimspecialedition/mods/74790), which makes armor and weapons lose their tempering durability over time. Weapons will never degrade below +0 tempering (read: they can never become worse than the base item).  

To help manage item degradation, the player can find or craft hammers and whetstones to temper their gear while away from town.

</Details>

<Details>
<summary>Resistance Scaling</summary>

Apostasy changes the way in which resists are calculated. I am adding this section here solely for the min-maxers and for those who care and/or want something to reference. 

 - Armor has a *soft cap* of 75% Physical Resist @ 500 Armor Rating and a *hard cap* of 90% Physical Resist @ 1000 Armor Rating.  
 - Magic and Elemental Resistances have a *soft cap* of 75% Resistance @ 75% Resistance (enchanting, alchemy, etc), however they have a *hard cap* of 90% Resistance @ 150% Resistance. 
   - This sounds convoluted so here is an example of how it actually works in practice: you equip a pair of boots with 50% Frost Resistance as a non-Nord, you will resist 50% of incoming Frost damage, as a Nord you would resist 80% of incoming Frost damage (50% base resist + 50% resist on armor = 100% Frost Resist, however scaling is reduced >75%).

There are effects that exist outside of raw Armor Rating and raw Resistance values that act as multipliers on top of your base resistances, these will usually be worded as "weapon" and "spell" damage (e.g., "You resist 50% of incoming weapon and spell damage").
 - If you have 500 Armor Rating and 75% Magic Resist with the **Defiance** perk in the Heavy Armor tree, then you would have the equivalent of 87.5% Physical and Magic Resistance while power attacking (the required condition to proc Defiance's bonus).

This section is very technical and not necessary to know to play the game normally, however understanding additive vs multiplicative bonuses can better inform decisions made while playing the list. Keep in mind that it is impossible to become *fully immune* to damage.

</Details>

## Quests Changes

Apostasy changes a significant amount of vanilla quests in one way or another in order to offer a more complete roleplaying exprience. The following list is non-exhaustive.

<Details>
<summary>Vanilla Quests</summary>

 - [Awakening](https://en.uesp.net/wiki/Skyrim:Awakening) Requires level 20, however this can be started at any point by going to [Dayspring Canyon](https://en.uesp.net/wiki/Skyrim:Dayspring_Canyon).
 - [Hearthfire](https://en.uesp.net/wiki/Skyrim:Hearthfire) Letter Requires level 15.
 - [Dragonborn](https://en.uesp.net/wiki/Skyrim:Dragonborn_(quest)) Requires level 30 and completion of [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller).
 - [A Chance Arrangement](https://en.uesp.net/wiki/Skyrim:A_Chance_Arrangement) Requires the player to have an apprentice level Sneak skill (25 or higher), have picked at least 10 pockets, and stolen at least 100 items.
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

 - **DAc0da**: Requires level 20+ and the completion of [Arniel's Endeavor](https://en.uesp.net/wiki/Skyrim:Arniel%27s_Endeavor), [The Eye of Magnus](https://en.uesp.net/wiki/Skyrim:The_Eye_of_Magnus), and [The Horn of Jurgen Windcaller](https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller).
 - **Wyrmstooth**: Requires level 15+ and completion of [The Way of the Voice](https://en.uesp.net/wiki/Skyrim:The_Way_of_the_Voice).
 - **Vigilant**: Requires level 25+ and the completion of [Kindred Judgement](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment) and [House of Horrors](https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors).
 - **Unslaad**: Requires completion of [Dragonslayer](https://en.uesp.net/wiki/Skyrim:Dragonslayer).

*It is recommended to play [Vicn](https://next.nexusmods.com/profile/Vicn)'s quest mods in the following order: DAc0da -> Vigilant -> Unslaad.*

</Details>

## New Armors and Weapons

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720811383-481712445.png)

Apostasy adds a significant amount of new Armors and Weapons to the game, all of which have been hand tuned and modified to fit within the balance of the list. While most can be accessed through [Skyrim Outfit System](https://www.nexusmods.com/skyrimspecialedition/mods/42162) if you want to use them purely for cosmetics, many have been re-integrated into the world as potential loot (or equipment that is unique to specific NPCs) and/or has been made obtainable through **Crafting Motifs**. 

Below is an (incomplete) list of new armors and weapons that are added and obtainable* by the player:

<Details>
<summary>New Equipment</summary>

 - [Ancient Imperial Armor](https://www.nexusmods.com/skyrimspecialedition/mods/142655): Can be found on certain enemies in [Vigilant](https://www.nexusmods.com/skyrimspecialedition/mods/11849).
 - [Armor of Mehrunes Dagon](https://www.nexusmods.com/skyrimspecialedition/mods/113809): ???
 - [Bocksten Cloak](https://www.nexusmods.com/skyrimspecialedition/mods/138180): Can be crafted at tanning racks.
 - [Bone Cultist Armor](https://www.nexusmods.com/skyrimspecialedition/mods/111224): Can be found on Solstheim Bandits and has the same crafting requirements as Bonemold.
 - [Casual Pirate Outfit](https://www.nexusmods.com/skyrimspecialedition/mods/133795): Worn by some NPCs from the [Val Serano](https://www.nexusmods.com/skyrimspecialedition/mods/103669) mod.
 - [Colovian Prince Set](https://www.nexusmods.com/skyrimspecialedition/mods/79894): See **Motifs**. Can be found on select NPCs.
 - [Crown Plate Set](https://www.nexusmods.com/skyrimspecialedition/mods/114751): See **Motifs**. Worn by [Kematu](https://en.uesp.net/wiki/Skyrim:Kematu) and other Alik'r.
 - [Dark Brotherhood Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/57539): Replacer for Dark Brotherhood Armor.
 - [Dark Witch Armor](https://www.nexusmods.com/skyrimspecialedition/mods/112260): See **Motifs**. Worn by [Illia](https://en.uesp.net/wiki/Skyrim:Illia).
 - [Dwemer Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/81043): Can be crafted with Journeyman Smithing.
 - [Eclipse Mage Outfit](https://www.nexusmods.com/skyrimspecialedition/mods/77244): Can be crafted with Basic Smithing.
 - [Elmlock Armor and Blade](https://www.nexusmods.com/skyrimspecialedition/mods/105930): Can be crafted with Advanced Smithing.
 - [Fleet Knight Set](https://www.nexusmods.com/skyrimspecialedition/mods/95009): See **Motifs**.
 - [Fluted Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/106381): Can be crafted with Advanced Smithing. Can also be found on select NPCs.
 - [Fuse Melony Armor](https://www.patreon.com/posts/hdt-smp-melony-67711235): Can be crafted with Basic Smithing. Worn by [Annekke Crag-Jumper](https://en.uesp.net/wiki/Skyrim:Annekke_Crag-Jumper).
 - [Fuse Sona Armor](https://www.patreon.com/posts/hdt-smp-sona-68902488): Worn by [Auri](https://www.nexusmods.com/skyrimspecialedition/mods/11278).
 - [Fuse Highlander Armor](https://www.patreon.com/posts/highlander-armor-79874952): Light Armor worn by [Astrid](https://www.nexusmods.com/skyrimspecialedition/mods/132350), can be crafted with Journeyman Smithing.
 - [Fuse Spriggan Armor](https://www.patreon.com/posts/spriggan-armor-115658146): Used for a custom set that can be found piece by piece from various Spriggan dens.
 - [Glasses Pack](https://www.nexusmods.com/skyrimspecialedition/mods/115653): See **Motifs**.
 - [Gryphonknight Regalia](https://www.nexusmods.com/skyrimspecialedition/mods/107437): Can be looted off of [Sabine Nytte](https://en.uesp.net/wiki/Skyrim:Sabine_Nytte).
 - [Illusive Infiltrator Armor](https://www.nexusmods.com/skyrimspecialedition/mods/105659): Can be crafted with Basic Smithing.
 - [Infantry Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/88099): Can be crafted with Basic Smithing. Can also be found on select NPCs.
 - [Kellan Armor](https://www.nexusmods.com/skyrimspecialedition/mods/68199): Can be crafted with Basic Smithing. Worn by select NPCs. 
 - [Kvetchi Mercenary Set](https://www.nexusmods.com/skyrimspecialedition/mods/79226): See **Motifs**.
 - [Lifesworn Vestiges](https://www.nexusmods.com/skyrimspecialedition/mods/136837): Can be crafted with Basic Smithing.
 - [Lunar Guard Armor](https://www.nexusmods.com/skyrimspecialedition/mods/75349): See **Motifs**.
 - [MAGECORE](https://www.nexusmods.com/skyrimspecialedition/mods/113540): See **Motifs**.
 - [Master Thief Armor](https://www.nexusmods.com/skyrimspecialedition/mods/141700): Replacer for Thieves Guild (and associated) Armor.
 - [Maormer Seascale Set](https://www.nexusmods.com/skyrimspecialedition/mods/91506): Can be looted from [Haldyn](https://en.uesp.net/wiki/Skyrim:Haldyn).
 - [Moon Monk Robes](https://www.nexusmods.com/skyrimspecialedition/mods/82495): See **Motifs**.
 - [Northern God Armor](https://www.nexusmods.com/skyrimspecialedition/mods/63772): Can be crafted with Journeyman Smithing.
 - [Obi's HeadHunter Armor](https://www.nexusmods.com/skyrimspecialedition/mods/113990): Can be looted from [Captain Hargar](https://en.uesp.net/wiki/Skyrim:Captain_Hargar).
 - [Orcish Armor Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/110280): can be crafted with Intermediate Smithing, can also be seen as variant armors for Stronghold Orcs. 
 - [Raven HDT-SMP Armor](https://www.nexusmods.com/skyrimspecialedition/mods/87655): Can be looted from the boss in [Bloodlet Throne](https://en.uesp.net/wiki/Skyrim:Bloodlet_Throne).
 - [Rihad Swordsman Set](https://www.nexusmods.com/skyrimspecialedition/mods/120576): See **Motifs**. Worn by [Kematu](https://en.uesp.net/wiki/Skyrim:Kematu) and other Alik'r.
 - [Silver Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/79088): Can be crafted with Journeyman Smithing. Worn by select NPCs. 
 - [Squire's Plate](https://www.nexusmods.com/skyrimspecialedition/mods/120370): See **Motifs**.
 - [Stormhold Warrior Armor](https://www.nexusmods.com/skyrimspecialedition/mods/96559): Can be crafted with Basic Smithing. Variants can also be looted off [Deeja](https://en.uesp.net/wiki/Skyrim:Deeja) and [Jaree-Ra](https://en.uesp.net/wiki/Skyrim:Jaree-Ra).
 - [Thalmor Ceykynd Armors](https://www.nexusmods.com/skyrimspecialedition/mods/136041): Can be crafted with Advanced Smithing after completion of [Diplomatic Immunity](https://en.uesp.net/wiki/Skyrim:Diplomatic_Immunity). Worn by certain Thalmor enemies.
 - [Thalmor Emissary Clothes](https://www.nexusmods.com/skyrimspecialedition/mods/101086): Worn by [Ancano](https://en.uesp.net/wiki/Skyrim:Ancano), [Ancarion](https://en.uesp.net/wiki/Skyrim:Ancarion), [Elenwen](https://en.uesp.net/wiki/Skyrim:Elenwen), and [Rulindil](https://en.uesp.net/wiki/Skyrim:Rulindil).
 - [Travelling Priest Robes](https://www.nexusmods.com/skyrimspecialedition/mods/118327): Can be found on several Priest-type NPCs and crafted.
 - [Twilight Princess Armor](https://www.nexusmods.com/skyrimspecialedition/mods/71182): Can be crafted after completion of [Kindred Judgement](https://en.uesp.net/wiki/Skyrim:Kindred_Judgment) with Basic Smithing. Worn by [Serana](https://en.uesp.net/wiki/Skyrim:Serana).
 - [Vey Alaxon](https://www.nexusmods.com/skyrimspecialedition/mods/104572): Fully integrated into Gilded Elven tier, can be crafted with Intermediate Smithing.
 - [Wayward Knight Set](https://www.nexusmods.com/skyrimspecialedition/mods/112793): See **Motifs**.
 - [Wild Witch Outfit](https://www.nexusmods.com/skyrimspecialedition/mods/81085): See **Motifs**. A variant can also be looted off [The Caller](https://en.uesp.net/wiki/Skyrim:The_Caller).
 - [Wind Ruler Armor SE](https://www.nexusmods.com/skyrimspecialedition/mods/60842): Can be looted from the [Butcher](https://en.uesp.net/wiki/Skyrim:Butcher) and [Umana](https://en.uesp.net/wiki/Skyrim:Umana). Also found on select NPCs.
 - [Yaldabaoth Armor](https://www.nexusmods.com/skyrimspecialedition/mods/104528): Can be crafted with Advanced Smithing. Worn by Laza.
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

## Content Additions and Improvements

Apostasy comes with several new quest mods and expansions for several vanilla quests or quest lines. These content additions and improvements will expand on the game, offering new adventures, routes, and companions to explore and engage with!

### Followers

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1724960630-647828967.png)

 - [Feris - Custom Voiced Female Follower](https://www.nexusmods.com/skyrimspecialedition/mods/142226): A wandering rogue who can be met in Whiterun's Bannered Mare!
 - [Follower Dialogue Expansion Series](https://next.nexusmods.com/profile/anbeegod/mods?gameId=1704): Greatly expands the dialogue and adds new short character quests for many vanilla followers.
 - [Gore - A Companion Mod](https://www.nexusmods.com/skyrimspecialedition/mods/85298): A former mercenary with a dark past and extensive personality, he can be found in the Falkreath wilds after being caught in a rather unfortunate situation!
 - [Heart of Ice - Astrid](https://www.nexusmods.com/skyrimspecialedition/mods/132350): A warrior from Roscrea who has traveled to Skyrim for a village artifact, she can be found in Bluewater cave near Rorikstead.
 - [INDIGO](https://www.nexusmods.com/skyrimspecialedition/mods/88240): A Khajiit with a complex needs system who can be found imprisoned over a simple misunderstanding in Riften Jail.
 - [Kaidan 2](https://www.nexusmods.com/skyrimspecialedition/mods/19075): A mercenary who is hunter by the Thalmor, he can be found in the Abandoned Prison.
 - [Katana - Journey in the Shadows](https://www.nexusmods.com/skyrimspecialedition/mods/69622): An *otherworldly* individual with a few friends, she can be found in Solitude's Winking Skeever.
 - [Khajiit Will Follow](https://www.nexusmods.com/skyrimspecialedition/mods/2227): Four new Kahjiit followers with their own unique quests, backstories, and personalities. 
 - [Remiel-Custom Voiced Dwemer Specialist and Companion](https://www.nexusmods.com/skyrimspecialedition/mods/51874): A Breton engineer from Wayrest who has traveled to Skyrim in hopes of exploring the province's various Dwemer ruins, she can be found in Markarth's Silver Blood Inn.
 - [Serana Dialogue Add-On](https://www.nexusmods.com/skyrimspecialedition/mods/32161): A massive expansion and overhaul to Skyrim's most beloved follower.
 - [Song of the Green (Auri Follower)](https://www.nexusmods.com/skyrimspecialedition/mods/11278): A Bosmer traditionalist who has ended up in Skyrim, she can be found in her secluded hut in the forests of Falkreath.
 - [Val Serano - Pirate Custom Voiced Follower and Quest Adventure](https://www.nexusmods.com/skyrimspecialedition/mods/103669): A sea-faring rogue with an extensive questline, in order to find Val Serano you must first go to White River Watch in Whiterun and find the note in a bottle.

### New Quests

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720525985-188255669.png)

 - [A Conversation](https://www.nexusmods.com/skyrimspecialedition/mods/124431): Atop the The Seven Thousand Steps, you will encounter a hooded stranger who will openly discuss his beliefs about life and the world.
 - [Artifacts - The Ice Blade of the Monarch](https://www.nexusmods.com/skyrimspecialedition/mods/13972): Adventure out to Pilgrim's Trench and begin a short quest to collect some of Tamriel's most ancient artifacts.
 - [Artifacts - The Tournament of the ten Bloods](https://www.nexusmods.com/skyrimspecialedition/mods/15264): Travel to Attribution's Share and earn Boethiah's favor by taking on her Champions, gaining some powerful artifacts along the way.
 - [Belethor's Sister](https://www.nexusmods.com/skyrimspecialedition/mods/92381): What if Belethor actually sold his sister?
 - [DAc0da](https://www.nexusmods.com/skyrimspecialedition/mods/134405): Work with the Psijic order to uncover the secrets of the destroyed Numidium that suddenly appears off the coast of Solitude.
 - [Demon of Dream](https://www.nexusmods.com/skyrimspecialedition/mods/118719): While wandering Skyrim, you may come across three ex-cultists of Vaermina. Enter their nightmares and uncover the secrets within!
 - [Dragon Hunting](https://www.nexusmods.com/skyrimspecialedition/mods/99193): Adds new ingredients and rewards to dragons and a repeatable Dragon Hunting quest to make the act of killing dragons more engaging.
 - [Final Farewell](https://www.nexusmods.com/skyrimspecialedition/mods/127894?): Come across a ghost who searches for vengeance, and help him come to terms with the afterlife.
 - [Missives](https://www.nexusmods.com/skyrimspecialedition/mods/17576) + [Headhunter - Bounties Redone](https://www.nexusmods.com/skyrimspecialedition/mods/51847): New Notice Board type system, reminiscent of The Witcher and other classic RPG titles.
 - [More to do in the Soul Cairn](https://www.nexusmods.com/skyrimspecialedition/mods/115962): Three new inhabitants have been added to the Soul Cairn, help them settle their affairs before they face the judgement of the Ideal Masters.
 - [Mysteries of the Dwemer](https://www.nexusmods.com/skyrimspecialedition/mods/114863): Maro, a researcger of the Dwemer, will appear outside of multiple Dwarven ruins, providing exposition and lore about the Deep Folk's history and theories on their downfall. 
 - [Penitus Oculatus](https://www.nexusmods.com/skyrimspecialedition/mods/21061): Expands upon the Destroy the Dark Brotherhood quest, adding an entire Penitus Oculatus questline for "good guy" playthroughs!
 - [Redeeming Fultheim](https://www.nexusmods.com/skyrimspecialedition/mods/136788): Convince Fultheim to rejoin the Blades.
 - [Siege at Icemoth](https://www.nexusmods.com/skyrimspecialedition/mods/109541): Travel to Icemoth, an island hidden in the Sea of Ghosts, and uncover the secrets that lay buried there. 
 - [SIRENROOT - Deluge of Deceit](https://www.nexusmods.com/skyrimspecialedition/mods/70917): Scour the Aedric ruins at the bottom of Lake Honrich in a Tomb Raider and Dragon Age inspired quest.
 - [Skyrim Extended Cut - Saints and Seducers](https://www.nexusmods.com/skyrimspecialedition/mods/72772): Travel to the Shivering Isles in a fully-voiced overhaul of Skyrim's CC Saints and Seducers Addon!
 - [Unslaad](https://www.nexusmods.com/skyrimspecialedition/mods/11789): What happens to the Hero when the adventure is over?
 - [VIGILANT](https://www.nexusmods.com/skyrimspecialedition/mods/11849): Join the remnants of the Vigilant of Stendarr and embark on an epic journey through the lore of the Elder Scrolls.
 - [Whispers of the Depths - Quest Mod](https://www.nexusmods.com/skyrimspecialedition/mods/127087): Encounter Slays-Manys-Beasts and hear him regale his tales of the sea.
 - [Wyrmstooth](https://www.nexusmods.com/skyrimspecialedition/mods/45565): Travel to the island of Wyrmstooth to assist the East Empire Company take on an ancient and powerful dragon. 

### Vanilla Quest Expansions and Edits

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720526384-1494096468.png)

 - [A Lovely Letter Alternate Routes](https://www.nexusmods.com/skyrimspecialedition/mods/21916): No longer must you involve yourself in Scen and Faendal's quarrel, alternatively you can expose both of them to Camilla.
 - [Blood and Silver - Cidhna Mine Expanded](https://www.nexusmods.com/skyrimspecialedition/mods/20269): Expands upon Cidhna Mine, adding new NPCs, potential escape routes, and secrets to explore.
 - [Bring Meeko to Lod](https://www.nexusmods.com/skyrimspecialedition/mods/25246): "Lod wants a dog and Meeko wants an owner. Seems like a perfect pair."
 - [Boethiah's Calling - Alternate Questline](https://www.nexusmods.com/skyrimspecialedition/mods/121499): Adds a new quest that allows you to obtain the Ebony Mail without ever siding with Boethiah.
 - [Caught Red Handed - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/65708): Adds some new dialogue to the infamous quest involving Svana and Haelga in Riften!
 - [Collecting the Edda](https://www.nexusmods.com/skyrimspecialedition/mods/52081): Restores an unfinished vanilla quest for the Bards College, allowing you to collect the Edda for Giraud Gemane.
 - [Defeat the Dragon Cult](https://www.nexusmods.com/skyrimspecialedition/mods/86625): Adds a new quest to help direct the Dragonborn to the location of Alduin's most loyal servants.
 - [Destroy the Dark Brotherhood - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/118229): Introduces new, lore-friendly ways to get kidnapped by Astrid and expands upon the vanilla Destroy the Dark Brotherhood questline!
 - [Finding Susanna Alive](https://www.nexusmods.com/skyrimspecialedition/mods/32512): Did you ever find it weird that you could never meet the tavern maid who is butchered in Blood on Ice? No? Well now you can anyways!
 - [House of Horrors - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57285): Greatly expands upon Molag Bal's daedric quest, providing new "good guy" routes and more!
 - [In the Shadow of the Crown](https://www.nexusmods.com/skyrimspecialedition/mods/79600): Provides an alternative route to completing the Stones of Barenziah, without ever dealing with the Thieves Guild.
 - [Infiltration - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/114054): Turns one of vanilla's most underwhelming quests into an epic adventure with real decisions to be made!
 - [Innocence Lost - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/80974): Have you ever wanted to give consequences to Grelod the Kind without acting like the average murder-hobo? Well look no further!
 - [Jarl Balgruuf Dilemma](https://www.nexusmods.com/skyrimspecialedition/mods/41132): Jarl Balgruuf can now be convinced to join the Stormcloaks!
 - [Jiub's Opus](https://www.nexusmods.com/skyrimspecialedition/mods/17056): Adds quest markers to one of the most annoying quests in the vanilla game. 
 - [Mehrunes Dagon's Shrine Unlocked - Pieces of the Past Alternate Ending](https://www.nexusmods.com/skyrimspecialedition/mods/119502): Adds new choices to Mehrunes Dagon's daedric quest, providing some additional potential outcomes to be experienced.
 - [Muiri's Revenge](https://www.nexusmods.com/skyrimspecialedition/mods/24312): Provides a way to obtain Muiri's Ring without joining the Dark Brotherhood. 
 - [Nilheim - Misc Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/53792): Provides some more roleplaying choice and flexibility to a beloved vanilla encounter.
 - [Paarthurnax - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/51711): Greatly expands upon the reasons for the Paarthurnax Dilemma and provides the Dragonborn with some new choices. 
 - [Revealing Rune](https://www.nexusmods.com/skyrimspecialedition/mods/120935): Adds a short quest to expand upon Rune's backstory and dialogue.
 - [Search and Seizure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/67066): Gives the player more options and choices when dealing with the Thalmor in Markarth.
 - [Serana Cure Quest Plus](https://www.nexusmods.com/skyrimspecialedition/mods/105091): Improves Serana's Cure quest.
 - [Serious Civil War Consequences for Jarl Balgruuf](https://www.nexusmods.com/skyrimspecialedition/mods/81554): Expands upon Balgruuf's decision to side with the Stormcloaks or the Imperials and the consequences for both actions.
 - [Simple Fishing Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/103440): Improves Skyrim's CC Fishing addon.
 - [The Heart of Dibella - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/94863): Offers new roleplay opportunities, dialogue, and choice for Dibella's quest.
 - [The Taste of Death - Quest Addon](https://www.nexusmods.com/skyrimspecialedition/mods/123173): Have you ever wanted to bring Markarth's Cult of Namira to justice? Offers new routes for "good guy" players when dealing with Namira and her Cult.
 - [The Only Cure - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/57683): Greatly expands upon Peryite's daedric quest, providing new "good guy" routes and more!
 - [The Whispering Door - Quest Expansion](https://www.nexusmods.com/skyrimspecialedition/mods/76606): Greatly expands upon Mephala's daedric quest, providing new "good guy" routes and more!
 - [Thieves Guild Alternative Endings](https://www.nexusmods.com/skyrimspecialedition/mods/114558): Greatly expands upon the ending of the Thieves Guild questline, allowing the player to defy or betray Nocturnal or refuse the mantle of Nightingale.
 - [Unmasking Sybille](https://www.nexusmods.com/skyrimspecialedition/mods/109265): Investigate and reveal the dark secret of one of the most powerful Court Wizards of the province.

### Player Homes

![](https://staticdelivery.nexusmods.com/mods/1704/images/118893/118893-1720691342-1079637258.png)

 - [Elianora's Breezehome Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/2829): A massive overhaul to the beloved starter home.
 - [Tel Jerdein - Telvanni Sorcerer Tower](https://www.nexusmods.com/skyrimspecialedition/mods/33539): A new Dunmer-themed player home in the mountains of the Rift.
