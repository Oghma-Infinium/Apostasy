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

- [0.2.0](#012) Release Date: June 4, 2024
- [0.1.1](#011) Release Date: May 30, 2024
- [0.1.0](#001) Release Date: May 29, 2024

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
 - Private Beta