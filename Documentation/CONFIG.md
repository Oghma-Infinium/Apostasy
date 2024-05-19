![](https://raw.githubusercontent.com/Oghma-Infinium/Fahluaan/main/images/Banner.webp)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/87820">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/fahluaan">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/Documentation/FAQ.md">FAQ</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Fahluaan/blob/main/ADDONS.md">Addons</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

- [Optional Addons](#optional-addons)
  - [Performance Options](#performance-options)
  - [Insects Begone](#insects-begone)
  - [Optional Tweaks](#optional-tweaks)
  - [Gamepad Support](#gamepad-support)
    - [Changing Keybinds](#changing-keybinds)
  - [Ultrawide Patches](#ultrawide-patches)
  - [Changing Resolution](#changing-resolution)
  - [Skyrim Upscaler](#skyrim-upscaler)
  - [In-Game MCM options](#in-game-mcm-options)
  - [Wheeler](#wheeler)
    - [Wheel Editing](#wheel-editing)
      - [Creation](#creation)
      - [Insertion](#insertion)
      - [Ordering](#ordering)
      - [Deletion](#deletion)


# Optional Addons

The following sections detail the **supported** modifications to the list. Any other modifications should be discussed in the `#fahluaan-modifications` channel of the [Waking Dreams](https://discord.gg/4WwqfK5yHg) support server.

## Performance Options

This section will cover the `Performance Options` section of the modlist. Due to Fahluaan's relatively good performance, at least in the data that has been collected, the performance options are not extremely robust to keep users from having to download additional LOD Outputs.

Based on user feedback, the performance options should provide a 20-40% net performance gain, depending on hardware and area (interior vs exterior), with minimal loss in the visual fidelity of the list. In order to use these Performance tweaks, activate the `Performance Mode` mod under the `Performance Options` separator in MO2 and disable the following mods above it:
 - `Tamrielic Grass For ENB Complex Grass`
 - `Veydosebrom Regions - Complex Grass`
 - `Folkvangr for ENB Complex Grass`
 - `Folkvangr Summer Tundra for ENB Complex Grass`
 - `Origins of forest for ENB Complex Grass`
 - `Cathedral - 3D Pine Grass for ENB Complex Grass`

In order to gain some additional performance, you can also deactivate `Enhanced Volumetric Lighting and Shadows (EVLaS)` under the performance Options tab.

## Insects Begone

For those with arachnophobia and/or entomophobia, the `Insects Begone` Separator contains some mods to remove most of the spider and insect adjacent models and enemies from the list. Some aspects of the list's vision are compromised to support these tweaks.

## Optional Tweaks

This section will cover the following Optional Tweaks that are included as a part of the modlist. Please note that if you do any of these tweaks, it is in your best interest to share this information when reporting any potential bugs that you encounter when playing the modlist.
 1. **Yet Another Music Merge - Content Creator Version**: Read more [here](#note-for-content-creators).
 2. **Content Creator Music Patches**: Read more [here](#note-for-content-creators).
 3. **QuickLoot RE - Disable in Combat**: An edited `.toml` file for QuickLoot RE to disable the loot box from appearing while in combat.
 4. **Show Compass Markers**: Makes it so compass markers are shown before they are discovered.
 5. **No ENB Lens Effect**: Disables ENB Lens effect (the frost and rain overlays).
 6. **No Survival Camera Effects**: Removes the image space effects added by CC Survival Mode.
 7. **Vigilant - No Enemy Blur**: Removes the image space blur effects that some enemies produce in Act 3 of Vigilant.
 8. **Lux - Brighter Templates**: Overwrites Lux's base lighting templates with brighter ones, for those who find interiors to be too dark.
 9. **V's Blursed RaceMenu Presets**: Brings back some classic meme presets seen in older versions of the list. Optional to enable.
 10. **NeverNude**: (Enabled by default), Removes Female nudity from the list, the list does not support male nudity without modifications.
 11. **Khajiit Speak Patch**: Patches all Dialogue in the list to act like [Khajiit Speak](https://www.nexusmods.com/skyrimspecialedition/mods/441).
 12. **Capture Warmer (Dynamic Cubemaps)**: Enable if using Dynamic Cubemap setting in ENB. **WARNING** Can cause camera glitches when changing cells.
 13. **Journeyman - A Fast Travel Overhaul**: Redesigns fast travel, read the [modpage](https://www.nexusmods.com/skyrimspecialedition/mods/92220) for more info.
 14. **Arena - Harder Easy Spawns**: Easy spawns are always any number between X and 1, where X is 0.75 of the level set by the Encounter Zone, Easy actors are often quite low level. This mod makes it so once you hit level 10, the level range of Easy actor spawns are extended, so they will more often spawn at higher levels.
 15. **Blade and Blunt - Dynamic Difficulty**: Level Based Difficulty Scaling makes incremental changes to your game’s difficulty in the background when you reach levels 10, 20, 30, and 40, to simulate increasing the difficulty of your game by one tier (Adept to Expert; Expert to Master, etc) over the course of your game. You can read more about specific numbers on the [Blade and Blunt modpage](https://www.nexusmods.com/skyrimspecialedition/mods/34549). Note that Dynamic Difficulty **does not** affect Novice or Legendary difficulties.
 16. **Fahluaan - Cloak Integration**: Adds cloaks to outfit records of some NPCs so cloaks can be seen in the world. Enable or Disable **BEFORE** making a new game.
 17. **Fahluaan - No Killmoves**: Disables Killmoves. Enabled by default.


## Gamepad Support

Fahluaan offers some mods to provide support for individuals who wish to play with a controller or gamepad. Refer to the [Changing Keybinds](#changing-keybinds) section for gamepad binds that need to be changed ***outside of the game***. 

In order to set up Fahluaan's gamepad support correctly, please follow these steps:
 1. Under the **Gamepad Support** Separator in MO2, activate the `Fahluaan - Controller Support` mod.
 2. Once in game, open the Settings > Controls and Reset Controls to default with the `Y` button (or equivalent) on your controller.
 3. Refer to the controlmap and set up your binds in the in-game Mod Configuration Menus as some of these can not be set in advanced.

![](https://raw.githubusercontent.com/Oghma-Infinium/Fahluaan/main/images/Keybinds.png)

 4. The [Wheeler](https://www.nexusmods.com/skyrimspecialedition/mods/97345) will likely need some additional configuration to play nicely with controller. To do some open the dMenu using `Home` on your keyboard and change the keybind(s) in the **Mod Config** tab.

If you wish to swap back to keyboard and mouse afterwards, just activate the `Backup Default Control Map` mod in MO2, and deactivate it if you wish to swap back to gamepad.

*****NOTE**: I (aljo) do not own a controller. The gamepad config is provided as-is by other users and helpers and may not be perfect.***

### Changing Keybinds

This section is going to be short and basic and only cover keybinds that must be changed ***outside of the game***. Please refer the [this](https://ck.uesp.net/wiki/Input_Script) page for the DXScanCodes used by most mods.

1. **Dual Wield Blocking**: Open the mod `Dual Wield Parrying - Settings` and locate the `DualWieldParryingSKSE.ini` file.
2. **Dodging**: Open the mod `TK Dodge - Settings` and locate the `TK Dodge RE.ini` file.

## Ultrawide Patches

Fahluaan offers some mods to provide Ultrawide and Widescreen Support. Under the **Ultrawide Patches** Separator in MO2 you will find some mods that you will want to activate if you are playing on Ultrawide or Widescreen resolutions (21:9 or 32:9).

Please note that I (aljo) do not own a widescreen monitor. The ultrawide settings and additional mods are what have been said to work based on user input and may not be perfect.

## Changing Resolution

By default, Wabbajack will set the resolution in your `Skyrimprefs.ini` to match the native resolution of your monitor. However, Skyrim scales very poorly at resolutions above 1080p (`1920x1080`) and depending on your hardware, it might be difficult to achieve consistent FPS on higher resolutions.

The preferable way to change your resolution is to find the `SSEDisplayTweaks.ini` located in the `SSE Display Tweaks` mod. Open the file and navigate to the `[Render]` section and find the lines `#Resolution=1920x1080` and `#ResolutionScale=0.75`. Here you can change the resolution here to your desired resolution. After changing the resolution, remove the `#` in order for the settings to take affect when launching the game.

Example for how the .ini line should look:
Before: `#Resolution=1920x1080`  
After: `Resolution=2560x1440`  

## Skyrim Upscaler

While [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) is an unsupported addition, it is asked about often enough that I felt I should put this here. In order to make sure your Upscaler works, you must change some lines in the `SSEDisplayTweaks.ini`.  

In the `SSEDisplayTweaks.ini` make sure that `Fullscreen = false`, `Borderless = true`, and `BorderlessUpscale = false` under the `[Render]` section.  

All other installation concerns for Skyrim Upscaler (DLSS) should be discussed in the modifications channel in the discord.  

## In-Game MCM options

Most MCMs will come pre-configured, the following is a list of Mod Configuration Menus that I have deemed may be beneficial to play around with as a user.
 - **Skyrim Unbound**: Choose your Standing Stone, starting location, starting equipment, starting wealth, etc. By default, the player is set to become Dragonborn, so if you do not want that for some reason, turn it off. **I highly suggest against choosing to not become Dragonborn, as it will lock you out of a lot of content within the list.**
 - **Improved Alternate Conversation Camera**: Edit the dialogue view. Can also be done through the `.ini` file in Mod Organizer.
 - **OBody Standalone**: Set OBody menu key here. (Default: `;`).
 - **Skyrim Outfit System**: This mod can be used to essentially acheive armor [transmogrification](https://www.merriam-webster.com/dictionary/transmogrify) in Skyrim, read more on the usage on the [modpage](https://www.nexusmods.com/skyrimspecialedition/mods/42162).
 - **SmoothCam**: Default preset is a slightly modified version of Vanilla Enhanced 2.0.
 - **Ultimate Immersion Toggle**: Hide UI Keybind. (Default: `X`).

## Wheeler

I am only writing this section because it is commonly asked enough that I feel I need to write it down on the list's documentation to have an easy place to point people. Almost this entire section is copy-pasted from the [Wheeler mod page](https://www.nexusmods.com/skyrimspecialedition/mods/97345).

### Wheel Editing

Changes to the wheel can be made when you open the wheel in either the inventory or magic menu. When you open the wheel in these two menus, the background will grey out, suggesting that you're now in **edit mode**.

#### Creation

By default, create an empty wheel using the "N" key and an empty slot using the "M" key. You can create as many wheels and as many slots in a single wheel as you'd like.

#### Insertion

To insert an item or magic into the slot, hover on the item you desire in the inventory, open the wheel, and left-click (right shoulder) on the entry you wish to insert the item into.

#### Ordering

To change a slot's order in a wheel, press the up/down arrow to swap its position with neighboring slots.

To change a wheel's ordering among all wheels, press the left/right arrow to swap its position with neighboring wheels.

#### Deletion

To delete an item from a slot, simply right-click on the item you wish to delete.

Right-clicking on an empty slot deletes the slot.

Right-clicking on an empty wheel deletes the wheel (you can't delete the last wheel).