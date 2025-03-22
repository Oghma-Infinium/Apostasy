![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.png)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/apostasy">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md">FAQ</a> |
  Configuration |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/ADDONS.md">ADDONS</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

- [Optional Addons](#optional-addons)
  - [Keybinds and Gamepad](#keybinds-and-gamepad)
    - [Controller and Gamepad Support](#controller-and-gamepad-support)
  - [Performance Optimizations](#performance-optimizations)
  - [Optional Visual Tweaks](#optional-visual-tweaks)
  - [Optional Gameplay Tweaks](#optional-gameplay-tweaks)
  - [Ultrawide Support](#ultrawide-support)
- [Changing FPS Limit](#changing-fps-limit)
- [Changing Resolution](#changing-resolution)
- [Upscalers and FrameGen](#upscalers-and-framegen)
  - [ENB Frame Generation](#enb-frame-generation)
  - [Skyrim Upscaler](#skyrim-upscaler)
  - [Lossless Scaling](#lossless-scaling)
- [In-Game MCM Options](#in-game-mcm-options)
- [Wheeler](#wheeler)
  - [Wheel Editing](#wheel-editing)
    - [Creation](#creation)
    - [Insertion](#insertion)
    - [Ordering](#ordering)
    - [Deletion](#deletion)


# Optional Addons

The following sections detail the **supported** modifications to the list. Any other modifications should be discussed in the `#Apostasy-modified` channel of the [Waking Dreams](https://discord.gg/4WwqfK5yHg) support server.

## Keybinds and Gamepad

This section is going to be short and basic and only cover keybinds that must be changed ***outside of the game***. Please refer the [this](https://ck.uesp.net/wiki/Input_Script) page for the DXScanCodes used by most mods.

 - **Dual Wield Blocking**: 
   1. Open the mod `Apostasy - Dual Block Parry Keybinds`. 
   2. In the mod open the `DualWieldParryingSKSE.ini` and the `BlockCancel.json` files and change the keybind(s). 
     - **MAKE SURE THE KEYBIND YOU CHANGE TO IN THE `DualWieldParryingSKSE.ini` MATCHES THE KEYBIND FOR `"BlockCancel2"` IN THE `BlockCancel.json`**.
   3. **In game**, edit the dual block keybind in the `Paragon Perks` MCM, or dual block will not be able to trigger timed blocks.
 - **Cycle Stances**: If you would prefer Stances cycle on a single key press instead of having 3 separate keybinds then you can do the following.
   1. Open the mod `Stances NG`.
   2. In the mod open the `StancesNG.ini`.
   3. Change `bUseCycling` from `false` to `true`.

### Controller and Gamepad Support

Apostasy ships with a premade controller configuration, designed for the list. In order to activate the controller config, please follow the steps below:

 1. Navigate to the `Keybinds and Gamepad` separator under the Optional Addons section in the **left pane** of MO2.
 2. Deactivate the `Apostasy - Default Controlmap` mod.
 3. Activate the `Wait Menu Redirected` mod.
 4. Activate the `Apostasy - Controller Configuration` mod.
 5. ???
 6. Profit!

Please note that by default, the controller config does not support blocking with a weapon+spell. If you want to add this feature then you can change the **Dual Wield Blocking** keybind, however there isn't really an available bind for it.

## Performance Optimizations

>[!IMPORTANT]
>Make sure to set your CPU Affinity before experimenting with other Performance Optimizations below!
<Details>
<summary>Setting CPU Affinity</summary>

 1. Click the `Puzzle Piece` button at the top of MO2 and select `Set CPU Affinity` and press `OK` on the pop-up box.
    ![](https://raw.githubusercontent.com/Oghma-Infinium/Vagabond/main/images/cpu%20affinity%20example.png)
 2. That's it, it's really that simple. **Please, please, please** do this before launching the game and whenever you update the modlist.

</Details>


Below are the list of mods you will find under the `Performance Optimizations` separator in MO2.
 1. `ENB Frame Generation`: This mod requires a GPU that supports DirectX 12 and a 120hz+ monitor.
 2. `Faster HDT-SMP - AVX512 Optimization`: This mod contains the AVX512 version of the [Faster HDT-SMP](https://www.nexusmods.com/skyrimspecialedition/mods/57339) `.dll` file compatible with the list. It is ***highly*** suggested that you try out this addon if you have a CPU that supports AVX-512 instruction. If you do not know if your CPU supports AVX-512, then google it or use a tool like HWinfo. **ENABLING THIS MOD WITH AN INCOMPATIBLE CPU WILL EITHER CRASH YOUR GAME OR BREAK ALL SMP**.
 3. `Apostasy - Performance DynDOLOD Output`: ***Strongly suggested*** for PCs that are barely meeting the [system requirements](https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md#system-requirements) for the list, or for those who are experiencing performance-related issues.  
 If you plan on swapping to this version of DynDOLOD then read the steps below. **FAILING TO FOLLOW THESE STEPS WILL RESULT IN A CORRUPTED GAME.**
    1. **If swapping on an existing save game**, Make a [clean save](https://dyndolod.info/Help/Clean-Save) (follow steps 1-4).
    2. Activate the `[Performance] Apostasy - Performance DynDOLOD Output` mod under the **Perfomance Optimizations** separator in the left pane of MO2.
    3. Deactivate the `Apostasy - DynDOLOD Output` mod under the **LOD Outputs** separator in the left pane of MO2.

Beyond what I can easily offer, you may want to consider reducing the `iShadowMapResolution` from `4096` to `1024` or `512` in the `skyrimprefs.ini`.   

>[!CAUTION]
>**DO NOT** use tools such as [Bethini](https://www.nexusmods.com/site/mods/631)! The `.ini` files have already been extensively tweaked, and many of the preconfigured settings set by these tools are not optimized for the list. 

**DISCLAIMER:** I will not provide troubleshooting or support for performance as everyones' PC is different and I can only know for certain how performance is on my own machine. In addition to this, I (aljo) am not some massive computer hardware nerd and I am not qualified to make definitive statements about hardware performance when I have not personally tested it, if that hardware is borderline / similar to the hardware that I **expect** to work best for the list.

## Optional Visual Tweaks

This separator contains a series of visual-only mods that can be easily disabled/enabled based on user preference. They will be discussed below.
 1. `Apostasy - Bodyslides - Nevernude`: Replaced the nude Male and Female default bodies with Nevernude variants. May not cover some unique bodies such as burnt Astrid.
 2. `Camera Noise`: Adds some camera motion/shake effects to both 1st and 3rd person. Can be tweaked via the ENB Menu (must Load Config first in ENB menu for it to show up in Shaders window). Can be disabled if it does not suit the users preference and should be disabled by people prone to motion sickness.
 3. `Capture Warmer (Dynamic Cubemaps)`: Improves the reflection quality of Dynamic Cubemaps, however has an annoying bug which causes the camera to spin when entering/exiting some cells. Disabled by default since the list does not make heavy use of Dynamic Cubemaps.
 4. `Dynamic Cubemaps - Metals`: Replaces the majority of cubemaps used by Armors and Weapons in the list with the 1px cubemap required to make use of the Dynamic Cubemap feature in ENB. It is strongly suggested that if you want to use Dynamic cubemaps you use this feature instead of the "Replace All Cubemaps" feature in the ENB GUI as that feature can cause some visuals bugs (e.g. issues with eye reflections due to replacing the Eye cubemap).
 5. `Enhanced Volumetric Lighting and Shadows`: EVLaS "improves" Skyrim's Volumetric lighting at the cost of performance. Disabling this mod can cause some oddities with moon lighting.
 6. `No Armor Spell Shader`: Removes the shader effect from spells like [Oakflesh](https://en.uesp.net/wiki/Skyrim:Armor_(spells)#Oakflesh), etc.
 7. `Precision Trail Magic Replacer - Chaos`: Edit of the precision weapon trail for enchanted and some unique weapons. Can be disabled if it does not suit user preferences.
 8. `Precision Trail Magic Replacer - Edit`: Disable if disabling the mod above.
 9.  `Precision magic trails`: Disable if disabling the mods above.
 10. `Precision Trail Replacer - Simple`: Replacer for the default Precision weapon trail. 
 11. `Visualized Critical Hits - MIF`: Adds some additional visual feedback on critical strikes. Can be disabled if it does not suit user preferences.

## Optional Gameplay Tweaks

This separator contains a series of gameplay-related tweaks that should be enabled or disabled **BEFORE** starting a new game. They will be discussed below.
 1. `Apostasy - Khajiit Speak`: Patches all Dialogue in the list to act like [Khajiit Speak](https://www.nexusmods.com/skyrimspecialedition/mods/441).
 2. `Apostasy - Arachnophobia and Entomophobia Support`: Removes some enemies that may trigger Arachnophobia or Entomophobia in some users.

## Ultrawide Support

Apostasy offers some mods to provide Ultrawide and Widescreen Support. Under the **Ultrawide Support** Separator in MO2 you will find some mods that you will want to activate if you are playing on Ultrawide or Widescreen resolutions (21:9 or 32:9).

Please note that I (aljo) do not own a widescreen monitor. The ultrawide settings and additional mods are what have been said to work based on user input and may not be perfect.

Ultrawide testing was done by TheRyge (21:9), Mgde12 (21:9), echo (21:9), and Kannon (32:9). If anyone would like to contribute to improvements for Ultrawide support, please reach out.

# Changing FPS Limit

By default, Apostasy is capped to 61 FPS and has several settings that will target 61 FPS. If you wish to increase your FPS Limit then these are changes that are recommended.

The following `.ini` files must be edited **while out of game**. After tweaking these `.ini` files, you can uncap FPS or change the FPS cap in the in-game ENB GUI (`Shift+Enter` to open).

<Details>
<summary>Shadow Boost</summary>

 1. Open the `Shadow Boost` mod under the `Performance Optimizations` separator.
 2. Under the `[Settings]` Header, edit `fTargetFPS = 61.000000` (line 2) to your new Target FPS.

</Details>

<Details>
<summary>SSE FPS Stabilizer</summary>

 1. Open the `SSE FPS Stabilizer` mod under the `Performance Optimizations` separator.
 2. Under the `[Settings]` Header, edit `TargetFps = 61` (line 13) to your new Target FPS.

</Details>

# Changing Resolution

By default, Wabbajack will set the resolution in the list's `Skyrimprefs.ini` to match the native resolution of your monitor. However, Skyrim scales very poorly at resolutions above 1080p (`1920x1080`) and depending on your hardware, it might be difficult to achieve consistent FPS on higher resolutions.

The preferable way to change your resolution is to find the `SSEDisplayTweaks.ini` located in the `[Performance] SSE Display Tweaks - Modified` mod. Open the file and navigate to the `[Render]` section and find the lines `#Resolution=1920x1080` and `#ResolutionScale=0.75`. Here you can change the resolution here to your desired resolution. After changing the resolution, remove the `#` in order for the settings to take affect when launching the game.

Example for how the .ini line should look:  
Before: `#Resolution=1920x1080`  
After: `Resolution=2560x1440`  

# Upscalers and FrameGen

## ENB Frame Generation

The list includes the [ENB Frame Generation](https://www.nexusmods.com/skyrimspecialedition/mods/144507) mod as an optional file under [Performance Optimizations](#performance-optimizations). While this mod is disabled by default, it can be enabled for potentially large performance gains at minimal quality loss. This mod is not considered a list modification. 

The Waking Dreams staff and I (aljo) do not endorse any other potential alternative to this mod, however there are other 3rd party software that can be utilized to achieve a similar effect.

## Skyrim Upscaler

While [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) is an unsupported addition, it is asked about often enough that I felt I should put this here. In order to make sure your Upscaler works, you must change some lines in the `SSEDisplayTweaks.ini`.

In the `SSEDisplayTweaks.ini` make sure that `Fullscreen = false` (line 39), `Borderless = true` (line 48), and `BorderlessUpscale = false` (line 58) under the `[Render]` section.  

Additionally, if you intend on using the FrameGen features of the newer [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) builds, go in the `SSEDisplayTweaks.ini` and set `FramerateLimit` (line 206) equal to **half** of your monitor's refresh rate.

All other installation concerns for Skyrim Upscaler (DLSS) should be discussed in the modifications channel in the discord.  

## Lossless Scaling

[Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) is also an unsupported addition to the list. In order to make sure your Upscaler works optimally, you must change some lines in the `SSEDisplayTweaks.ini`.

In the `SSEDisplayTweaks.ini` make sure that `Fullscreen = false` (line 39), `Borderless = true` (line 48), and `BorderlessUpscale = false` (line 58) under the `[Render]` section.  

Additionally, if you intend on using the FrameGen features of the newer [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) builds, go in the `SSEDisplayTweaks.ini` and set `FramerateLimit` (line 206) equal to **half** of your monitor's refresh rate.

All other configuration concerns for Lossless Scaling should be discussed in the modifications channel in the discord.

# In-Game MCM Options

Thanks to Wabbajack, MCMs will come pre-configured with the intended settings. The following is a list of MCMs that contain keybind or preference related settings.

>[!WARNING]
>Changing MCM Settings in any MCM that is not listed below is considered a list modification!

 1. `Apostasy`: This is a custom MCM made for the list.
    > **NSFW Armors Toggle**: Determines whether some lewd-er versions of some armors will be craftable or not. Has no effect on the armors that NPCs wear or the armors that can be looted. (Default: Disabled)
    > **Killmove Mode**: Choose to enable or disable killmoves: Disabled or Vanilla Style. (Default: Vanilla Style)
    > **Skin Animals**: Determines whether [Simple Hunting Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/95943) skins animals. (Default: Disabled)
 2. `Better Third Person Selection`: ???
 3. `CollisionReset`: Change the keybind for resetting SMP physics (Default: `F10`). 
 4. `Compass Controls`: Change the Toggle key for the Compass (Default: `'`).
 5. `Dialogue History`: Change the keybind to bring up the Dialogue History menu (Default: `LAlt + Y`).
 6. `Dismembering Framework`: Disable the mod if you do not like the added gore (Default: `ENABLED` - click **Mod Status** at the very top to toggle Enabled or Disabled state.)
 7. `Dynamic Activation Key`: Change the keybind modifier for Dynamic Activation (Default: `LShift`).
 8. `Dynamic Crafting`: Can enable and disable the features of the mod.
 9. `Dynamic Looting`: Can enable and disable different interaction animations. Note that animations do not play when weapon is drawn. 
 10. `Eld Beri II`: **(DEBUG ONLY)** Can clear stuck lantern effects on the player or other actors. 
 11. `EVG CLAMBER`: Change the EVG Clamber settings (Default: `Balanced`). This isn't recommended to be tampered with but you can.
 12. `Horse Whistle Key`: Change the Hotkey for Horse Call (Default: `H`). Optionally add a lesser power to perform the function of the hotkey.
 13. `LOD Reload Bug Fix`: **(DEBUG ONLY)** Can fix unloaded LODs.
 14. `moreHUD`: Can adjust certain widgets on the HUD.
 15. `OBody NG`: Change the keybind for the OBody morphs menu (Default: `;`). **DO NOT ENABLE PERFORMANCE MODE!**
 16. `One Click Power Attack`: Change the keybind for Power Attacks (Default: `V`).
 17. `Paragon Perks`: Change Dual Wield Block key here if you changed it previously.
 18. `Photo Mode`: Adjust the keybinds and settings for [po3's Photo Mode](https://www.nexusmods.com/skyrimspecialedition/mods/91701).
 19. `Precision`: Can enable or disable Hitstop (Default: `Enabled`).
 20. `Quest Journal Limit Bug Fixer`: **(DEBUG ONLY)** Refreshes all active quest objectives.
 21. `QuickLoot IE`: Configure QuickLoot's settings and controls.
 22. `Settling of Squad`: See followers managed by [Settling of Squad](https://www.nexusmods.com/skyrimspecialedition/mods/125471).
 23. `Skyrim Outfit System`: Transmog system, read more on the [mod page](https://www.nexusmods.com/skyrimspecialedition/mods/42162) or in the [discord](https://discord.gg/4WwqfK5yHg).
 24. `SmoothCam`: Change the SmoothCam Camera preset (Default: `Apostate Preset`).
 25. `Sneak Vignette`: Adjust the opacity of the Vignette that appears while sneaking. Set `Vignette Opacity` to `0` in order to disable (Default: `67`).
 26. `Swift Potion`: Change the hotkey for quick potion binds.  
     - Restore Health = `F`  
     - Restore Stamina = `Shift+F`  
     - Restore Magicka = `Ctrl+F`  
 27. `TK Dodge`: Change the hotkey for Dodging (Default: `LAlt`).
 28. `True Directional Movement`: Change the target lock hotkey (Default: `M3`).
 29. `TrueHUD`: Adjust core components of the HUD.

# Wheeler

Wheeler is utilized as an alternative to the vanila favorites menu (which can still be accessed with `G` on keyboard). For configuration help, please refer to the below documentation. Also please note that almost this entire section is copy-pasted from the [Wheeler mod page](https://www.nexusmods.com/skyrimspecialedition/mods/97345), and the mod page may provide more assistance with certain configuration help.

## Wheel Editing

Changes to the wheel can be made when you open the wheel in either the **inventory or magic menu**. When you open the wheel in these two menus, the background will grey out, suggesting that you're now in **edit mode**.

### Creation

By default, create an empty wheel using the `N` key and an empty slot using the `M` key. You can create as many wheels and as many slots in a single wheel as you'd like.

### Insertion

To insert an item or magic into the slot, hover on the item you desire in the inventory, open the wheel, and **left-click** (right shoulder) on the entry you wish to insert the item into.

### Ordering

To change a slot's order in a wheel, press the up/down arrow to swap its position with neighboring slots.  

To change a wheel's ordering among all wheels, press the left/right arrow to swap its position with neighboring wheels.

### Deletion

To delete an item from a slot, simply **right-click** on the item you wish to delete.
 - Right-clicking on an empty slot deletes the slot.
 - Right-clicking on an empty wheel deletes the wheel (you can't delete the last wheel).
