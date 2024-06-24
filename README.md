![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.webp)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  Installation |
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

# Attention

## ! ! ! THIS DOCUMENTATION IS UNFINISHED ! ! !

**Modlist Support: [Waking Dreams](https://discord.gg/4WwqfK5yHg)**

>[!IMPORTANT]
>Apostasy requires the four free AE mods (Fishing, Rare Curios, Survival Mode, and Saints and Seducers) included in the Skyrim Anniversary Edition update from November 2021.

>[!WARNING]
>You must update Skyrim to the latest version (1.6.1170) on Steam to install this list.

# Contents
- [Attention](#attention)
  - [! ! ! THIS DOCUMENTATION IS UNFINISHED ! ! !](#---this-documentation-is-unfinished---)
- [Contents](#contents)
  - [Introduction](#introduction)
    - [System Requirements](#system-requirements)
  - [Installation](#installation)
    - [Pre-Installation](#pre-installation)
      - [Installing Microsoft Visual C++ Redistribution Package](#installing-microsoft-visual-c-redistribution-package)
      - [Pagefile and crash prevention](#pagefile-and-crash-prevention)
      - [Setting Shader Cache Size](#setting-shader-cache-size)
      - [Steam Setup](#steam-setup)
      - [Game Language](#game-language)
      - [Installing Creation Club Content](#installing-creation-club-content)
    - [Wabbajack Installation](#wabbajack-installation)
      - [Installing Wabbajack](#installing-wabbajack)
      - [Downloading and Installing Apostasy](#downloading-and-installing-apostasy)
    - [Problems with installation](#problems-with-installation)
      - [Problematic Files](#problematic-files)
  - [Post-Installation and Optional Setup](#post-installation-and-optional-setup)
    - [Game Folder](#game-folder)
    - [Antivirus Exceptions](#antivirus-exceptions)
    - [Post-Installation Issues and Troubleshooting](#post-installation-issues-and-troubleshooting)
    - [Keyboard Keybinds](#keyboard-keybinds)
    - [Gamepad Keybinds](#gamepad-keybinds)
  - [Playing the List](#playing-the-list)
    - [Starting the Game](#starting-the-game)
  - [Updating the modlist](#updating-the-modlist)
  - [Removing the Modlist](#removing-the-modlist)
  - [Issues](#issues)
  - [Credits and Thanks](#credits-and-thanks)

## Introduction

Apostasy is a Wabbajack modlist for Skyrim SE that offers a modern, action-oriented combat system, custom tailored gameplay, and a consistent, high-fidelity graphics overhaul. Apostasy aims to deliver a cohesive and refined experience, enhancing both visuals and mechanics.

The full modlist can be viewed [here](https://loadorderlibrary.com/lists/Apostasy).

You can find a summary of all relevant changes on the [Gameplay Guide](https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md).

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### System Requirements

>[!NOTE]
>The listed specs are the best idea of a baseline that I can provide at the current moment, based on feedback I have gotten from testers and my own experiences. In the future this will be updated depending on feedback received. Your PC may run the list better or worse due a variety of reasons, I will not provide troubleshooting or support for hardware related issues.

>[!CAUTION]
>An SSD is required to the play the list.   
>Only Windows 10 or 11 operating systems are supported. Windows LTSC, special variants, lightened editions or any other modified variant **WILL NOT WORK.** Lunix installations also **WILL NOT WORK**.

| Spec Category | Minimum | Recommended |
|     :---:    |     :---:     |     :---:     | 
| **OS**    | 64-bit Windows 10 | 64-bit Windows 10 | 
| **Resolution** | 1920 x 1080 | 2560 x 1440 |
| **Processor** | R7 5800X or equivalent |  R7 7800X3D or equivalent | 
| **Memory** | 16gb RAM + 40gb Pagefile | 32gb RAM + 40gb Pagefile | 
| **Graphics** | RTX 3060Ti or equivalent | RTX 4070 or equivalent | 
| **Storage** | SATA SSD | M.2 SSD | 

Please note that the below numbers are current estimates and the actual may be larger or smaller depending on version.

Downloads: ~150 GB  
Install: ~190 GB  
Temp Files: ~40 GB (on OS drive)  
**TOTAL:** ~340 GB  

<Details>
<summary>Temporary Files</summary>

Wabbajack typically requires around 30-40 GB of space on your main OS drive for temporary and working files during the installation, this space is not counted towards the total install space of the list for sake of this guide, however Wabbajack roughly accounts for it in the UI.

</Details>

<Details>
<summary>BSA Warning</summary>

Apostasy heavily employs [BSA](https://en.uesp.net/wiki/Skyrim_Mod:Archive_File_Format)s in order to keep the list's size down and improve performance. However, this means that the installation process may take longer than some other lists and you may run into issues with Wabbajack crashing if you allocate too many system resources to it. It also can potentially inflate the amount of temporary file space required by Wabbajack but this still needs to be tested and confirmed.

If you are struggling with issues of Wabbajack crashing during the installation process, please read the [Problems with Installation](#problems-with-installation) section of this ReadMe.

</Details>

## Installation

Installing Apostasy is relatively easy and, if you have Nexus Premium, will be a simple waiting game. If you are updating the modlist, you can safely skip to the [updating section](#updating-the-modlist).

### Pre-Installation

These steps are only required for installing the Modlist for the first time. Additionally, many of these steps may be covered in other modlist installs, for new users I suggest reading through here regardless.

#### Installing Microsoft Visual C++ Redistribution Package

 1. Install [Visual C++ x64](https://aka.ms/vs/17/release/vc_redist.x64.exe), [.Net Runtime 8.X.X desktop x64](https://dotnet.microsoft.com/en-us/download/dotnet/8.0), and [.Net 6.0 Runtime desktop x64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.30-windows-x64-installer).
 2. Change Skyrim so it does not [automatically update](https://help.steampowered.com/en/faqs/view/71AB-698D-57EB-178C#disable).
 3. Right click on Skyrim SE and click on properties, untick the `Enable Steam Overlay while in-game.`
 4. You also need to start the games to the main menu in order to download all the creations. **DO NOT SKIP THIS STEP, IF YOU DO SO WABBAJACK WILL FAIL**

#### Pagefile and crash prevention

>[!WARNING]
>Larger Skyrim modlists require a significant amount of memory, running out of memory **will** result in crashes and other potential issues. Due to Apostasy's size and number of files required to be handled for the list, this step is **NOT** optional, I do not care how much RAM or VRAM you have, please do this step.

Setting up a pagefile:

 1. Press `Win Key + R`.
 2. Type `sysdm.cpl ,3` and hit `ENTER`.
 3. Navigate to *Performance* and click the box `Settings...`.
 4. Click the *Advanced* tab at the top.
 5. Under *Virtual Memory* click the box `Change...`.
 6. **Uncheck** *Automatically manage* if it is checked.
 7. Select your disk drive, ideally your fastest solid state drive.
 8. Click `Custom size:`.
 9. In the box next to `Initial Size (MB)` type `40960`.
 10. In the box next to `Maximum Size (MB)` type `40960`.
 11. Click `Set`.
 12. Click `OK`.
 13. Click `Apply`.
 14. Click `OK`.
 15. **Restart your computer**.
  
> Your pagefile does not need to be on the same drive as your Wabbajack install or Steam install.

<Details>
<summary>BONUS READING: Why do we need a pagefile?</summary>

Skyrim is a very old game (originally released in 2011) that is built on the [Creation Engine](https://en.wikipedia.org/wiki/Creation_Engine), a engine based off of the [Gamebryo](https://en.wikipedia.org/wiki/Gamebryo) engine that was originally used for Morrowind (released in 2002).

Through lots of experience and trial-and-error, we have discovered that increasing the window's pagefile can fix certain types of Skyrim crashes, the two most common examples being `Unhandled native exception occurred at 0x7FF6ADC8DDDA` and `Unhandled native exception occurred at 0x0`.

But why is this? Skyrim appears to use system memory in very unexpected ways, for example it will frequently dip into the pagefile memory despite there being available RAM. Skyrim heavily favors high speed, low latency RAM (the best you can get as of writing this is 6000MHz and CL30 for DDR5).

</Details>

#### Setting Shader Cache Size

>[!WARNING]
>For Nvidia users, it is also recommended to boost the size of the shader cache. These settings have been shown to improve stability, while it may not be entirely necessary, it is still recommended.

Changing the shader cache size:

 1. Right-click on your desktop and select `NVIDIA Control Panel`,.
 2. Navigate and click on `Manage 3D settings`. It is the 2nd one to the top.
 3. Scroll down in Global Settings until you see **Shader Cache Size**.
 4. Double Click **Driver Default** to the right of Shader Cache Size and select **10 GB**
 5. Click `Apply` in the bottom right hand corner. 
 6. You may exit out of the application.
![](https://raw.githubusercontent.com/iAmMe27/Tahrovin/main/img/ShaderCache.png)

#### Steam Setup

>[!IMPORTANT]
>If you have your Steam Library in Program Files, read [this article](https://github.com/LostDragonist/steam-library-setup-tool/wiki/Usage-Guide) by LostDragonist. Locations such as Desktop, Documents, Downloads, OneDrive, etc. *will* cause issues with installing and playing the list.

#### Game Language

>[!WARNING]
>The English Steam version of Skyrim is the only supported version. I understand that this may be frustrating for non-English speaking users or users with the GOG/Bethesda.net versions, but due to the core file differences between the different versions, I am only able to support one game version.

Setting the Game Language:

 1. Right click on your Skyrim in Steam.
 2. Click `Properties`.
 3. Click `Language`.
 4. Set the Language to `English`.

#### Installing Creation Club Content

>[!WARNING]
>Due to some issues with the 1.6.1130 update and onwards, Steam now ships Skyrim with its own version of some CC files. However these files do not have the same hashes as the files that are downloaded from the in-game Creation Club menu for AE users. In order to work around this issue and make the list as accessible as possible, the list is compiled using the file hashes from the in-game CC downloads.

Installing Creation Club Content:

 1. Navigate to your Skyrim SE's Steam data folder. (example: `D:\SteamLibrary\steamapps\common\Skyrim Special Edition\data`).
 2. Within your data folder, delete *both* the `ccbgssse037-curios.bsa` and `ccbgssse037-curios.esl` files.
 3. Launch Skyrim SE through Steam and click the `Creations` button on the main menu.
 4. Press `O` on your keyboard to open the options menu and click `Download all owned Creation Club content` (The Rare Curios CC should now be installing).
 5. Exit out of the Creations menu, say yes to Bethesda's load order shit, and exit the game.
 6. **VERY IMPORTANT**, from this step onwards, **DO NOT** verify your game files unless told to as it will revert the "correct" file hashes to the ones that are included in the base-game install.

### Wabbajack Installation

#### Installing Wabbajack

Once you have completed pre-installation, download the [latest version of Wabbajack](https://github.com/wabbajack-tools/wabbajack/releases) on this github and place it in a folder such as `C:\Wabbajack`. **DO NOT place it in Program Files, User folders (such as Desktop, Documents, Downloads, OneDrive, etc.), in your Skyrim's Steam folder, or in any folders related to the modlist itself (the downloads or install folder).**. I recommend placing it on an SSD as it will work quicker on there.

>[!IMPORTANT]
>The list requires Wabbajack version **3.6.1.0 or later**, installing on older versions of Wabbajack will prevent the installation from being completed.

#### Downloading and Installing Apostasy

>[!CAUTION]
>A legal copy of Skyrim Special Edition is required. Pirated copies of the game will cause the installation to fail and even if you manage to somehow get around Wabbajack's built-in piracy prevention measures, SKSE does not work with the cracked exes.  
**Buy the game.**

Downloading and installing Apostasy can take a while depending on your internet connection and computer. To install Apostasy, complete the following steps.

 1. Open Wabbajack and click `Browse Modlists`
 2. Press the download button on Apostasy and wait for it to download.
 3. Set the installation folder to be somewhere like `C:\Games\Apostasy` or `C:\Apostasy`. **DO NOT place it in the Wabbajack root folder, Program Files, User folders (such as Desktop, Documents, Downloads, etc.), or in your Skyrim's Steam folder**
    > The download location does not need to be on a SSD, but it makes installing faster.
 1. Press the play button to begin.
 2. Turn on your favorite show or a nice long video essay Wabbajack does its thing. Alternatively read through this readme again.
 3. If the installation is successful, then rejoice and move onto [post installation](#post-installation-and-optional-setup). If the installation is unsuccessful, follow what is below or join the [discord server](https://discord.gg/4WwqfK5yHg) for support.

### Problems with installation

It is possible that you may encounter an error with Wabbajack when installing. Some common issues are listed below.

<Details>
<summary>Trouble downloading a specific file:</summary>

Big files can fail to download due to connection issues. You can either run wabbajack again or download the file manually. If you decide to manually download it, make sure to place it in the same place as the other downloads. 

> This issue can also occur with files sources from Google Drive, MEGA, Patreon, and other sites. If you are failing on a non-nexus file, then read the [Problematic Files](#problematic-files) section.

</Details>

<Details>
<summary>X is not a whitelisted download:</summary>

This may happen when I update the modlist. Please check if there is a new update or wait until you see a release ping.  

</Details>

<Details>
<summary>Wabbajack could not find my game folder:</summary>

Either buy the game or re-read the [Pre-Installation](#pre-installation) section.  

</Details>  

<Details>
<summary>Antivirus reports a virus:</summary>

Windows 10/11 may automatically quarantine a key file which is needed for Mod Organizer. You can fix this by [adding an exclusion for Mod Organizer in windows defender](#antivirus-exceptions).  

</Details>

<Details>
<summary>Unable to download Data_ccXXXXX - *.bsa or *.esp:</summary>

This error means that there is an issue where Wabbajack is unable to hash your Creation Club Content. If you have followed the steps outlined under [Pre-Installation](#installing-creation-club-content), are not on a pirated copy of the game, and have verified your steam files, then it is very likely that Wabbajack or Bethesda has messed up the hashing for these files. If this is the case, please wait for it to be resolved before continuing to download the list.  

</Details>  

<Details>
<summary>Unable to download Skyrim_Default.ini:</summary>

This error means you failed to follow the readme. Go back to the [game language](#game-language) section and set your game language to English.  

</Details>  

<Details>
<summary>Sanity check error extracting file:</summary>

Wabbajack will sometimes have issues extracting some files if they use special characters. If you encounter this issue in a wabbajack log, please try the steps down below:

 1. Press `Win Key + R`.
 2. Type `intl.cpl` and hit `ENTER`.
 3. Navigate to *Administrative* and click `Change system locale...`.
 4. Change the *Current system locale:* to `English (United Kingdom)`.
 5. **Uncheck** `Beta: Use Unicode UTF-8 for worldwide language support`
 6. Click `OK`
 7. **Restart your computer** and rerun the Wabbajack installer.

> It is suggested to have a program installed on your PC that can open `.json` files, like [Notepad++](https://notepad-plus-plus.org/) or [Visual Studio Code](https://code.visualstudio.com/).  

</Details>  

<Details>
<summary>Wabbajack Crashing during the installation:</summary>

If you find yourself struggling to run Wabbajack without it crashing, freezing up, or blue-screening your PC, please try lowering Wabbajack's resource usage using these steps:

 1. Open Wabbajack.
 2. Click the gear icon in the top-right corner of the Wabbajack window.
 3. Click the `Edit Resource Usage Settings and Close Wabbajack` button.
 4. Lower the `MaxTasks` number for each category to half of what it is currently set to.
 5. Press `Ctrl+S` on your keyboard to save the file.
 6. Open Wabbajack and continue the installation process.

> It is suggested to have a program installed on your PC that can open `.json` files, like [Notepad++](https://notepad-plus-plus.org/) or [Visual Studio Code](https://code.visualstudio.com/).  

</Details>  

#### Problematic Files

>[!NOTE]
>Wabbajack frequently has trouble downloading mods hosted on sites other than Nexus. These files are listed below for your convenience.  
>You will need to manually download these files and place them in the `Resource Download Location` that is made in the [Downloading and Installing Apostasy](#downloading-and-installing-apostasy) section.

Google Drive Files:
- [High Poly Head v1.4 (SE)](https://drive.google.com/uc?id=15_0njBUjHKidNnJPmLXEygzGVWsA3Zbq&export=download)
- [Dint's BDOR Hairs](https://drive.usercontent.google.com/download?id=1tpY3bDs-LR6rptf8oPUfraKs1CkxJJB3&export=download&authuser=0)
- [Dint's HairPack 02](https://drive.usercontent.google.com/download?id=1Ts0sQz3hDxhCeS_LUnXJQFuws_qbw9YQ&authuser=0)
- [Dint's Face Part mod](https://drive.usercontent.google.com/u/0/uc?id=1RQl8ki73fgLnzBZn6EWjneuW4Dk8TUO_&export=download)
- [Olivier Kenjutsu Battleaxe and Warhammer](https://drive.google.com/file/d/1rX4INfO3ieWp25gPh0NiLPl1ktLoegZ9)

MEGA Files:
- [High Poly Head - EFA - Male Eyebrow fix](https://mega.nz/file/WZt0BDCL#JNUTn_5P2sEPuHm3znSdrrqN28tPnxvmVzeFOw67FAU)

Patreon Files: (These are free to download)
- [ESkyrim MCO Installer](https://www.patreon.com/file?h=68233071&i=11449877)

## Post-Installation and Optional Setup

### Game Folder

Apostasy uses a Wabbajack feature called Stock Game to keep your Skyrim installation clean. All the files that you need to run the list are in a folder called `Stock Game`. You don’t need to copy anything at all.

### Antivirus Exceptions

>[!CAUTION]
>Antivirus programs are notorious for false flagging [MO2's Virtual File System](https://stepmodifications.org/wiki/Guide:Mod_Organizer/Advanced), which can and will cause crashes and other problems. Antivirus programs like BitDefender, Norton, and Webroot are especially aggressive, and you will very likely need to fully remove them from your PC in order to actually launch the game through MO2. It is 2024, Windows Defender and being smart online is more than adequate to protect yourself from malicious software.

If you use Windows Defender, it is advised that you set up an Exception for the modlist.

<Details>
<summary>Setting up Windows Defender Exceptions:</summary>

 1. Press the Windows Key.
 2. Type "Windows Defender" in the search bar and select "Windows Security".
 3. Click on "Virus & threat protection" in the left pane.
 4. Click the "Manage settings" option under "Virus & threat protection settings".
 5. Scroll down to "Exclusions" and click "Add or remove exclusions".
 6. Windows Defender will prompt you with a run as administrator screen, just hit yes.
 7. Click the "Add an exclusion" button at the top and choose "Folder".
 8. Navigate to your Install folder for the list and click "Select Folder".
 9. **(OPTIONAL)** You can repeat these steps for the other executables:
    - ModOrganizer.exe (`[Path to Modlist]\ModOrganizer.exe`)
    - Nemesis Unlimited Behavior Engine.exe (`[Path to Modlist]\mods\Project New Reign - Nemesis Unlimited Behavior Engine\Nemesis_Engine\Nemesis Unlimited Behavior Engine.exe`)
    - Synthesis.exe (`[Path to Modlist]\tools\Synthesis\Synthesis.exe`)

</Details>  

### Post-Installation Issues and Troubleshooting

<Details>
<summary>Game is zoomed into the top left corner!</summary>

Windows Scaling can prevent games from displaying correctly, and will often result in the game appearing "zoomed in". To fix this, find the `SkyrimSE.exe` located in your `[Path to Modlist]\Stock Game` and follow the steps in the images below:

![](https://cdn.discordapp.com/attachments/694254949944655953/847772081030299648/skyrim-scaling.png?ex=66774586&is=6675f406&hm=812e1240d8de4ecc213055242067caddb1df617907c677a426b7f8c23dac4e8b&)

</Details>

<Details>
<summary>Form 43 Error in MO2. / A DLL plugin has failed to load correctly.</summary>

Your installation did not complete. Rerun Wabbajack and make sure to tick the **Overwrite Installation** box.  
If the error persists after a reinstall, then delete the `[Path to Modlist]\mods` folder, and rerun Wabbajack again.

</Details>  

<Details>
<summary>Crashes</summary>

Skyrim is a notoriously buggy game and cramming thousands of mods into it is not gauranteed to always produce the most stable experience possible. Especially in heavier lists where you may be pushing the limitations of your hardware as a result of Skyrim's old and unoptimized rendering pipeline.

If you find yourself crashing, then please share your crashlogs in the appropriate #support channel on the [discord server](https://discord.gg/4WwqfK5yHg).

In order to get the best possible response please ensure that:
 1. Your crash is reproducible. 
 2. You include all relevant crashlogs (if you do not know where to find them then use the `!crashlog` command in chat).
 3. Provide details about the crash (what you were doing, where it took place, if there was an associated quest, etc). Details are necessary in order to quickly diagnose crashes.

</Details>  

### Keyboard Keybinds

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Keybinds.png)

### Gamepad Keybinds

>[!WARNING]
>Gamepads may need additional setup in order to work as intended. Please refer to the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md#gamepad-support) page.

![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/controlmap.png)

>[!TIP]
>You can review default keybinds in game by pressing `F11`!

## Playing the List

>[!TIP]
>Before starting the list, read over the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md), [FAQ](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md), and [Gameplay](https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md) pages.

### Starting the Game

 1. Head over to your modlist installation folder (e.g. `C:\Apostasy`), locate an executable named `ModOrganizer.exe`, and launch it.
 2. Launch the "Play" Executable in MO2.
    > The game may take several minutes to load on your first launch. Please be patient and at no point should you click the `Unlock` button in MO2.
 3. Click "New Game".
 4. Create your character.
 5. Wait about a minute or so before leaving the start room for the game to fully initialize and MCM Recorder to finish processing.
    > The MCM Recorder should start automatically and will pop-up a message box when finished.
 6. **(OPTIONAL)** Refer to the MCM options listed on the [Configuration](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md#in-game-mcm-options) to adjust your settings.
 7. Talk to the dragon to choose your start.
    > If no start is chosen then you will have a default start in the Helgen Inn.
 8. Leave the room.

## Updating the modlist

Versioning for the list will adhere to the following format: `MAJOR.MINOR.PATCH`.
 - `MAJOR`: Any release with a number change here will be considered a major update as at least 1 area of the list was massively overhauled. These updates with **NEVER** be save safe.
 - `MINOR`: Any release with a number change here will be considered a minor update, these updates will usually not be save safe, unless otherwise specified.
 - `PATCH`: Any release with a number change here will be considered a patch, these updates should be save safe and will be used primarily for bugfixes.
 - In some rare cases you may see a fourth slot be used, which I will refer to as `HOTFIX`. These list "updates" will be used if the list needs to be recompiled for any reason. There will be no changes in these "updates" as they are purely for maintenance.
Updating is like installing the list. Simply make sure your paths are the same and tick the `overwrite existing modlist` button. **Note**: Any mods you have added will be deleted when updating. To make sure that Wabbajack does not delete your added mods upon updating, prefix your mods with `[NoDelete]`.

>[!IMPORTANT]
>Saves can be continued across **Save-Safe** updates. Updates will be indicated whether or not they are **Save-Safe** on the [Changelog](https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md). It is suggested that you backup your saves before updating if you plan on continuing them.

>[!TIP]
>RaceMenu presets can be placed in the `[NoDelete] RaceMenu Presets` mod under the `Stock List [NoDelete]'s` Seperator of MO2 if you want to ensure they are saved after an update.

## Removing the Modlist
Simply delete the folder. Congratulations, you have uninstalled Apostasy.

## Issues

Please check the [FAQ](https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/FAQ.md) first if you have any issues. 

>[!TIP]
>If you encounter any bugs or issues while playing the list, the [Waking Dreams](https://discord.gg/4WwqfK5yHg) support server is preferred and will have the fastest turn around time for support.  Alternatively, you can leave an issue report on the Github [Issues Page](https://github.com/Oghma-Infinium/Apostasy/issues) or leave a bug report on the [Nexus Page](https://www.nexusmods.com/skyrimspecialedition/mods/118893?tab=bugs)


## Credits and Thanks

- _YOU_ for reading this.
- [Bingus](https://ko-fi.com/beangas) for [Ascensio](https://github.com/Oghma-Infinium/Ascensio), ENB tweaking, asset editing, and much, much more.
- Curly for the original iteration of Ascensio that got me started with my first modlist.
- [Ylikollikas](https://next.nexusmods.com/profile/Ylikollikas) for a lot, I can not even begin to list what he has contributed.
- [iAmMe27](https://ko-fi.com/iamme27) for general modding, documentation, and WJ assistance.
- Discord helpers for their time and effort playtesting, providing feedback, and support assistance.
- [Jolly Co-Operators](https://discord.gg/jolly-coop) and [Cacophony](https://www.patreon.com/cacophony1979) for their wonderful community that inspired me to start modding more.
- JustThatKing, jdsmith2816, and Total for their feedback and assistance when I started modding.
- Bethesda Game Studios for Skyrim and the Creation Kit.
- [ElminsterAU](https://www.patreon.com/ElminsterAU) and the xEdit team for SSEEdit.
- [Noggog](https://www.nexusmods.com/skyrim/users/862590) for Mutagen and Synthesis.
- [Halgari](https://www.nexusmods.com/skyrimspecialedition/users/17252164) and the WJ Team for the amazing platform that is Wabbajack.
- [LivelyDismay](https://github.com/LivelyDismay) and [The Animonculory](https://github.com/The-Animonculory) for their modding guides.
- [Sheson](https://ko-fi.com/sheson) for DynDOLOD.
- [Styyx](https://github.com/Styyx1) for assisting heavily in creating DLLs for the custom mods made for the list.
- [Aelarr](https://www.nexusmods.com/skyrim/users/6843757) and Anreme for permissions to use some custom mods from The Owl Archives server.
- Mgde12, D1Z4STR, 半蔵 内倉, Kepler, Hencoat, Matty, EnragedHamster, Scott, snowpeachcherry, Charlie Kriech, Durgenage, Pacifist Fist, Don Maker, Russell Collins, Oresh, Danimals, Monko, Anehum, Valeria, The Unattested Wombat, Ola Nordman, Regista433, Jaron Scotland, King_Sheogorath, TheRyge, and Shakes for support on [patreon](https://www.patreon.com/aljoxo).
- adorion1981, aexilkv, AlphaGhost47, Ananta, Blade, Bubborus, derkaenaz, DevZan, doombot117, E2J, FalseRealism, Felivath, FutureWorld, Gous, Gremlin, hedich, Jeremy, JoeyFlow, JollyTheRancher, JXEYES, Kathie Murphy, Lunaros, Maelstrom, Paulo Giovanni, Psylence, rezthe0one on Discord, Roxiie, SaddestNoddles, skylion, Soloist, Steve, Tom Curran, Won Pham, WoWZaton, and Zhijia for their support via [Ko-fi](https://ko-fi.com/aljoxo).
