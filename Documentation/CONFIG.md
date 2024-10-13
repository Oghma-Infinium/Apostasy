![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.png)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
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
  - [Skyrim Upscaler](#skyrim-upscaler)
  - [Lossless Scaling](#lossless-scaling)
- [In-Game MCM options](#in-game-mcm-options)
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
   - Open the mod `Apostasy - Dual Block Parry Keybinds`. 
   - In the mod open the `DualWieldParryingSKSE.ini` and the `BlockCancel.json` files and change the keybind(s). 
     - **MAKE SURE THE KEYBIND YOU CHANGE TO IN THE `DualWieldParryingSKSE.ini` MATCHES THE KEYBIND FOR `"BlockCancel2"` IN THE `BlockCancel.json`**.
   - **In game**, edit the dual block keybind in the `Valor Perks` MCM, or dual block will not be able to trigger timed blocks.

### Controller and Gamepad Support

Apostasy ships with a premade controller configuration, designed for the list. In order to activate the controller config, please follow the steps below:

 1. Navigate to the `Keybinds and Gamepad` separator under the Optional Addons section in the **left pane** of MO2.
 2. Deactivate the `Apostasy - Default Controlmap` mod.
 3. Activate the `Wait Menu Redirected Mod`.
 4. Activate the `Apostasy - Controller Configuration` mod.
 5. ???
 6. Profit!

Please note that by default, the controller config does not support blocking with a weapon+spell. If you want to add this feature then you can change the **Dual Wield Blocking** keybind, however there isn't really an available bind for it.

## Performance Optimizations

It is suggested that the majority of this section is left untouched unless you are an experienced modder.

The mods prefixed as `[Performance]` will be discussed below.
 1. `SSE Display Tweaks - Modified`: This is the version of Display Tweaks that is suggested to be edited for ease of use. Right clicking on the mod --> Information --> Notes provides instructions on the necessary Display Tweaks changes necessary if you plan on using some type of 3rd party FrameGen tool.
 2. `Faster HDT-SMP - AVX512 Optimization`: This mod contains the AVX512 version of the [Faster HDT-SMP](https://www.nexusmods.com/skyrimspecialedition/mods/57339) `.dll` file compatible with the list. It is ***highly*** suggested that you try out this addon if you have a CPU that supports AVX-512 instruction. If you do not know if your CPU supports AVX-512, then google it or use a tool like HWinfo. **ENABLING THIS MOD WITH AN INCOMPATIBLE CPU WILL EITHER CRASH YOUR GAME OR BREAK ALL SMP**.
 3. `CPU affinity`: To adjust CPU affinity for your setup, click the `Puzzle Piece` button at the top of MO2 and select `Set CPU Affinity` and press ok on the pop-up box.
       > Example of the options you need to press are provided [here](https://raw.githubusercontent.com/Oghma-Infinium/Vagabond/main/images/cpu%20affinity%20example.png).  
       > May give small performance improvement.
 4. `Apostasy - Performance DynDOLOD Output`: **Strongly suggested** for PCs that are barely meeting the [system requirements](https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md#system-requirements) of the list or for those who are experiencing performance-related issues. If you plan on swapping to this version of DynDOLOD then read the steps below. **FAILING TO FOLLOW THESE STEPS WILL RESULT IN A CORRUPTED GAME.**
    1. **If swapping on an existing save game**, Make a [clean save](https://dyndolod.info/Help/Clean-Save) (follow steps 1-4).
    2. Activate the `[Performance] Apostasy - Performance DynDOLOD Output` mod under the **Perfomance Optimizations** separator in the left pane of MO2.
    3. Deactivate the `Apostasy - DynDOLOD Output` mod under the **LOD Outputs** separator in the left pane of MO2.

Beyond what I can easily offer, you may want to consider reducing the `iShadowMapResolution` from 1024 to 512 in the `skyrimprefs.ini`.   
Please **DO NOT** run tools such as Bethini, the ini files have already been configured extensively and many changes made by Bethini are frankly terrible. 

**DISCLAIMER:** I will not provide troubleshooting or support for performance as everyones' PC is different and I can only know for certain how performance is on my own machine. In addition to this, I (aljo) am not some massive computer hardware nerd and I am not qualified to make definitive statements about hardware performance when I have not personally tested it, if that hardware is borderline / similar to the hardware that I **expect** to work best for the list.

## Optional Visual Tweaks

This separator contains a series of visual-only mods that can be easily disabled/enabled based on user preference. They will be discussed below.
 1. `Apostasy - Bodyslides - Nevernude`: Replaced the nude Male and Female default bodies with Nevernude variants. May not cover some unique bodies such as burnt Astrid.
 2. `Camera Noise`: Adds some camera motion/shake effects to both 1st and 3rd person. Can be tweaked via the ENB Menu (must Load Config first in ENB menu for it to show up in Shaders window). Can be disabled if it does not suit the users preference and should be disabled by people prone to motion sickness.
 3. `Capture Warmer (Dynamic Cubemaps)`: Improves the reflection quality of Dynamic Cubemaps, however has an annoying bug which causes the camera to spin when entering/exiting some cells. Disabled by default since the list does not make heavy use of Dynamic Cubemaps.
 4. `Dynamic Cubemaps - Metals`: Replaces the majority of cubemaps used by Armors and Weapons in the list with the 1px cubemap required to make use of the Dynamic Cubemap feature in ENB. It is strongly suggested that if you want to use Dynamic cubemaps you use this feature instead of the "Replace All Cubemaps" feature in the ENB GUI as that feature can cause some visuals bugs (e.g. issues with eye reflections due to replacing the Eye cubemap).
 5. `Dynamic Impact Slash Effects X`: Adds new particle effects on weapon hits. Can be disabled if it does not suit user preferences. Can also be reinstalled with a different Impact VFX choice. Make sure to keep the other FOMOD choices the same if you reinstall the mod (check the Mod's note for full FOMOD breakdown).
 6. `Enhanced Volumetric Lighting and Shadows`: EVLaS "improves" Skyrim's Volumetric lighting at the cost of performance. Disabling this mod can cause some oddities with moon lighting.
 7. `Precision Trail Magic Replacer - Chaos`: Edit of the precision weapon trail for enchanted and some unique weapons. Can be disabled if it does not suit user preferences.
 8. `Precision Trail Magic Replacer - Edit`: Disable if disabling the mod above.
 9. `Precision magic trails`: Disable if disabling the mods above.
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

By default, Apostasy is capped to 61 FPS and has several settings that will target 61 FPS. If you wish to increase your FPS Limit then **while out of game** you must make changes to the following `.ini` files in order to not experience increased stuttering while at your new FPS cap. After tweaking these `.ini` files, you can uncap FPS or change the FPS cap in the in-game ENB GUI (`Shift+Enter` to open).

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

## Skyrim Upscaler

While [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) is an unsupported addition, it is asked about often enough that I felt I should put this here. In order to make sure your Upscaler works, you must change some lines in the `SSEDisplayTweaks.ini` located in the `[Performance] SSE Display Tweaks - Modified` mod.

In the `SSEDisplayTweaks.ini` make sure that `Fullscreen = false` (line 39), `Borderless = true` (line 48), and `BorderlessUpscale = false` (line 58) under the `[Render]` section.  

Additionally, if you intend on using the FrameGen features of the newer [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) builds, go in the `SSEDisplayTweaks.ini` and set `FramerateLimit` (line 206) equal to **half** of your monitor's refresh rate.

All other installation concerns for Skyrim Upscaler (DLSS) should be discussed in the modifications channel in the discord.  

## Lossless Scaling

[Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) is also an unsupported addition to the list. If you plan on using it, follow the instructions above for Skyrim Upscaler, they should be applicable here as well. 

All other configuration concerns for Lossless Scaling should be discussed in the modifications channel in the discord.

# In-Game MCM options

Most MCMs will come pre-configured, the following is a list of Mod Configuration Menus that I have deemed may be beneficial to play around with as a user. Default hotkeys listed are for Keyboard and may differ if using the controller config.

Changing MCM Settings in any MCM that is under the `> Apostasy MCM Hider <` tab is considered a list modification.

 1. `Apostasy`: This is a custom MCM made for the list.
    > **NSFW Armors Toggle**: Determines whether some lewd-er versions of some armors will be craftable or not. Has no effect on the armors that NPCs wear or the armors that can be looted. (Default: Disabled)
    > **Killmove Mode**: Choose between three different styles of Killmoves: Disabled, Vanilla Style, or Cinematic. (Default: Vanilla Style)
    > **Skin Animals**: Determines whether [Simple Hunting Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/95943) skins animals. (Default: Disabled)
 2. `CollisionReset`: Change the keybind for resetting SMP physics (Default: `F10`). 
 3. `Compass Controls`: Change the Toggle key for the Compass (Default: `'`).
 4. `Dialogue History`: Change the keybind to bring up the Dialogue History menu (Default: `LAlt + Y`).
 5. `Dismembering Framework`: Disable the mod if you do not like the added gore (Default: `ENABLED` - click `Mod Status` at the very top to toggle Enabled or Disabled state.)
 6. `Dynamic Activation Key`: Change the keybind modifier for Dynamic Activation (Default: `LShift`).
 7. `Edryu's Widget`: Enable/Disable or reposition the equipment widgets (the ones **above** the Health, Magicka, and Stamina bars). By default, Edryu's is configured for 1440p, dropdown below has recommended settings for other 16:9 resolutions.

<Details>
<summary>Edryu's Widget Settings</summary>

**1080p:**

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/EDRYU1080p.png)

**1440p:**

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/EDRYU1440p.png)

**4k:**

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/EDRYU4K.png)

</Details>

 8. `EVG CLAMBER`: Change the EVG Clamber settings (Default: `Balanced`). This isn't recommended to be tampered with but you can.
 9. `Horse Whistle Key`: Change the Hotkey for Horse Call (Default: `H`). Optionally add a lesser power to perform the function of the hotkey.
 10.  `OBody NG`: Change the keybind for the OBody morphs menu (Default: `;`).
 11. `One Click Power Attack`: Change the keybind for Power Attacks (Default: `V`).
 12. `QuickLoot EE`: Optionally disable QuickLoot from popping up during combat.
 13. `SmoothCam`: Change the SmoothCam Camera preset (Default: `Apostate Preset`).
 14. `STB_ResistsWidget`: Enable/Disable or reposition the resist widgets (the ones to the **left** of the Health, Magicka, and Stamina bars).

<Details>
<summary>STB_ResistsWidget Settings</summary>

**16:9**

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/ResistWidgets.png)

</Details>

 15.  `Swift Potion`: Change the hotkey for quick potion binds.  
     - Restore Health = `F`  
     - Restore Stamina = `Shift+F`  
     - Restore Magicka = `Ctrl+F`  
 16.  `TK Dodge`: Change the hotkey for Dodging (Default: `LAlt`).
 17.  `True Directional Movement`: Change the target lock hotkey (Default: `M3`).
 18.  `Valor Perks`: Change Dual Wield Block key here if you changed it previously.
 19.  `Widget Mod`: Enable/Disable or reposition the miscellaneous widgets (the ones **below** the Health, Magicka, and Stamina bars).  
     - Please note that only the widgets used are appropriately skinned for the UI, so enabling additional widgets may be undesirable.
  
<Details>
<summary>Widget Mod Settings</summary>

**16:9**

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod1-1.png)  
![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod1-2.png)  
![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod1-3.png)  
![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod1-4.png)  
![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod2-1.png)  
![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/MCM%20Configs/WidgetMod2-2.png)  

**21:9**

May need Tweaks

</Details>

# Wheeler

I am only writing this section because it is commonly asked enough that I feel I need to write it down on the list's documentation to have an easy place to point people. Almost this entire section is copy-pasted from the [Wheeler mod page](https://www.nexusmods.com/skyrimspecialedition/mods/97345).

## Wheel Editing

Changes to the wheel can be made when you open the wheel in either the inventory or magic menu. When you open the wheel in these two menus, the background will grey out, suggesting that you're now in **edit mode**.

### Creation

By default, create an empty wheel using the `N` key and an empty slot using the `M` key. You can create as many wheels and as many slots in a single wheel as you'd like.

### Insertion

To insert an item or magic into the slot, hover on the item you desire in the inventory, open the wheel, and left-click (right shoulder) on the entry you wish to insert the item into.

### Ordering

To change a slot's order in a wheel, press the up/down arrow to swap its position with neighboring slots.

To change a wheel's ordering among all wheels, press the left/right arrow to swap its position with neighboring wheels.

### Deletion

To delete an item from a slot, simply right-click on the item you wish to delete.

Right-clicking on an empty slot deletes the slot.

Right-clicking on an empty wheel deletes the wheel (you can't delete the last wheel).
