![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.webp)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md">FAQ</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/ADDONS.md">Addons</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

- [Optional Addons](#optional-addons)
  - [Gamepad Support](#gamepad-support)
  - [Performance Optimizations](#performance-optimizations)
  - [Optional Visual Tweaks](#optional-visual-tweaks)
  - [Optional Gameplay Tweaks](#optional-gameplay-tweaks)
  - [Ultrawide Support](#ultrawide-support)
  - [Changing Keybinds](#changing-keybinds)
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

The following sections detail the **supported** modifications to the list. Any other modifications should be discussed in the `#Apostasy-modifications` channel of the [Waking Dreams](https://discord.gg/4WwqfK5yHg) support server.

## Gamepad Support

Gamepad/Controller support for the list.

## Performance Optimizations

It is suggested that the majority of this section is left untouched unless you are an experienced modder.

The mods prefixed as `[Performance]` will be discussed below.
 1. `SSE Display Tweaks - Modified`: This is the version of Display Tweaks that is suggested to be edited for ease of use. Right clicking on the mod --> Information --> Notes provides instructions on the necessary Display Tweaks changes necessary if you plan on using some type of 3rd party FrameGen tool.
 2. `Faster HDT-SMP - AVX512 Optimization`: This mod contains the AVX512 version of the [Faster HDT-SMP](https://www.nexusmods.com/skyrimspecialedition/mods/57339) `.dll` file compatible with the list. It is ***highly*** suggested that you try out this addon if you have a CPU that supports AVX-512 instruction. If you do not know if your CPU supports AVX-512, then google it or use a tool like HWinfo. **ENABLING THIS MOD WITH AN INCOMPATIBLE CPU WILL CRASH YOUR GAME**.

## Optional Visual Tweaks

This separator contains a series of visual-only mods that can be easily disabled/enabled based on user preference. They will be discussed below.
 1. `Apostasy - Bodyslides - Nevernude`: Replaced the nude Male and Female default bodies with Nevernude variants. May not cover some unique bodies such as burnt Astrid.
 2. `Capture Warmer (Dynamic Cubemaps)`: Improves the reflection quality of Dynamic Cubemaps, however has an annoying bug which causes the camera to spin when entering/exiting some cells. Disabled by default since the list does not make heavy use of Dynamic Cubemaps.
 3. `Dynamic Cubemaps - Metals`: Replaces the majority of cubemaps used by Armors and Weapons in the list with the 1px cubemap required to make use of the Dynamic Cubemap feature in ENB. It is strongly suggested that if you want to use Dynamic cubemaps you use this feature instead of the "Replace All Cubemaps" feature in the ENB GUI as that feature can cause some visuals bugs (e.g. issues with eye reflections due to replacing the Eye cubemap).
 4. `Dynamic Impact Slash Effects X`: Adds new particle effects on weapon hits. Can be disabled if it does not suit user preferences. Can also be reinstalled with a different Impact VFX choice. Make sure to keep the other FOMOD choices the same if you reinstall the mod (check the Mod's note for full FOMOD breakdown).
 5. `Enhanced Volumetric Lighting and Shadows`: EVLaS "improves" Skyrim's Volumetric lighting at the cost of performance and potentially worse visuals at most times of day outside of Dawn/Dusk. Disabled by default due to author preference.
 6. `Precision Trail Magic Replacer - Chaos`: Edit of the precision weapon trail for enchanted and some unique weapons. Can be disabled if it does not suit user preferences.
 7. `Precision Trail Magic Replacer - Edit`: Disable if disabling the mod above.
 8. `Precision Default Weapon Trail Replacer - Smoother`: Replacer for the default Precision weapon trail. 
 9. `Visualized Critical Hits - MIF`: Adds some additional visual feedback on critical strikes. Can be disabled if it does not suit user preferences.

## Optional Gameplay Tweaks

This separator contains a series of gameplay-related tweaks that should be enabled or disabled **BEFORE** starting a new game. They will be discussed below.
 1. `Apostasy - Khajiit Speak`: Patches all Dialogue in the list to act like [Khajiit Speak](https://www.nexusmods.com/skyrimspecialedition/mods/441).
 2. `Apostasy - Arachnophobia and Entomophobia Support`: Removes some enemies that may trigger Arachnophobia or Entomophobia in some users.

## Ultrawide Support

Apostasy offers some mods to provide Ultrawide and Widescreen Support. Under the **Ultrawide Support** Separator in MO2 you will find some mods that you will want to activate if you are playing on Ultrawide or Widescreen resolutions (21:9 or 32:9).

Please note that I (aljo) do not own a widescreen monitor. The ultrawide settings and additional mods are what have been said to work based on user input and may not be perfect.

## Changing Keybinds

This section is going to be short and basic and only cover keybinds that must be changed ***outside of the game***. Please refer the [this](https://ck.uesp.net/wiki/Input_Script) page for the DXScanCodes used by most mods.

1. **Dual Wield Blocking**: Open the mod `Dual Wield Parrying - Settings` and locate the `DualWieldParryingSKSE.ini` file.
2. **Dodging**: Open the mod `TK Dodge - Settings` and locate the `TK Dodge RE.ini` file.

## Changing Resolution

By default, Wabbajack will set the resolution in the list's `Skyrimprefs.ini` to match the native resolution of your monitor. However, Skyrim scales very poorly at resolutions above 1080p (`1920x1080`) and depending on your hardware, it might be difficult to achieve consistent FPS on higher resolutions.

The preferable way to change your resolution is to find the `SSEDisplayTweaks.ini` located in the `[Performance] SSE Display Tweaks - Modified` mod. Open the file and navigate to the `[Render]` section and find the lines `#Resolution=1920x1080` and `#ResolutionScale=0.75`. Here you can change the resolution here to your desired resolution. After changing the resolution, remove the `#` in order for the settings to take affect when launching the game.

Example for how the .ini line should look:
Before: `#Resolution=1920x1080`  
After: `Resolution=2560x1440`  

## Skyrim Upscaler

While [Skyrim Upscaler](https://www.nexusmods.com/skyrimspecialedition/mods/80343) is an unsupported addition, it is asked about often enough that I felt I should put this here. In order to make sure your Upscaler works, you must change some lines in the `SSEDisplayTweaks.ini`.  

In the `SSEDisplayTweaks.ini` make sure that `Fullscreen = false`, `Borderless = true`, and `BorderlessUpscale = false` under the `[Render]` section.  

All other installation concerns for Skyrim Upscaler (DLSS) should be discussed in the modifications channel in the discord.  

## In-Game MCM options

Most MCMs will come pre-configured, the following is a list of Mod Configuration Menus that I have deemed may be beneficial to play around with as a user.


## Wheeler

I am only writing this section because it is commonly asked enough that I feel I need to write it down on the list's documentation to have an easy place to point people. Almost this entire section is copy-pasted from the [Wheeler mod page](https://www.nexusmods.com/skyrimspecialedition/mods/97345).

### Wheel Editing

Changes to the wheel can be made when you open the wheel in either the inventory or magic menu. When you open the wheel in these two menus, the background will grey out, suggesting that you're now in **edit mode**.

#### Creation

By default, create an empty wheel using the `N` key and an empty slot using the `M` key. You can create as many wheels and as many slots in a single wheel as you'd like.

#### Insertion

To insert an item or magic into the slot, hover on the item you desire in the inventory, open the wheel, and left-click (right shoulder) on the entry you wish to insert the item into.

#### Ordering

To change a slot's order in a wheel, press the up/down arrow to swap its position with neighboring slots.

To change a wheel's ordering among all wheels, press the left/right arrow to swap its position with neighboring wheels.

#### Deletion

To delete an item from a slot, simply right-click on the item you wish to delete.

Right-clicking on an empty slot deletes the slot.

Right-clicking on an empty wheel deletes the wheel (you can't delete the last wheel).