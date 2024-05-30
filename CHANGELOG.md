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

- [0.1.1](#011) Release Date: May 30, 2024
- [0.1.0](#001) Release Date: May 29, 2024

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