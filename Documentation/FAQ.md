![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.png)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
  FAQ |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/ADDONS.md">ADDONS</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

# Contents

- [Contents](#contents)
  - [FAQ](#faq)
    - [Q: Do I have to read this?](#q-do-i-have-to-read-this)
    - [Q: Can I uncap the FPS?](#q-can-i-uncap-the-fps)
    - [Q: What mod is it that makes favorited items/potions/quest items show on my character?](#q-what-mod-is-it-that-makes-favorited-itemspotionsquest-items-show-on-my-character)
    - [Q: How do I reposition my weapons? / Can I have swords on my back?](#q-how-do-i-reposition-my-weapons--can-i-have-swords-on-my-back)
    - [Q: My character is really skinny and the weight sliders only adjust the neck and wrist, how do I change my character's body appearance?](#q-my-character-is-really-skinny-and-the-weight-sliders-only-adjust-the-neck-and-wrist-how-do-i-change-my-characters-body-appearance)
    - [Q: How do I start the main questline?](#q-how-do-i-start-the-main-questline)
    - [Q: I can't find Altano in the Windpeak Inn. / How do I start VIGILANT?](#q-i-cant-find-altano-in-the-windpeak-inn--how-do-i-start-vigilant)
    - [Q: How do I start UNSLAAD?](#q-how-do-i-start-unslaad)
    - [Q: What is the Pilgrim skill? / How do I access the Pilgrim skill tree?](#q-what-is-the-pilgrim-skill--how-do-i-access-the-pilgrim-skill-tree)
    - [Q: How do I set up the quick wheel?](#q-how-do-i-set-up-the-quick-wheel)
    - [Q: I can't add a weapon/armor to the wheel.](#q-i-cant-add-a-weaponarmor-to-the-wheel)
    - [Q: Can I still use the vanilla favorites menu? I do not like the wheel.](#q-can-i-still-use-the-vanilla-favorites-menu-i-do-not-like-the-wheel)
    - [Q: Can I add/remove \[insert mod\] to the list?](#q-can-i-addremove-insert-mod-to-the-list)
    - [Q: Will you add \[insert mod\] to the list?](#q-will-you-add-insert-mod-to-the-list)
    - [Q: Will you add OStim/SexLab to the list?](#q-will-you-add-ostimsexlab-to-the-list)
  - [Known Issues](#known-issues)
    - [When leveling up skills, new perk nodes do not get highlighted until exiting and re-entering the perk menu!](#when-leveling-up-skills-new-perk-nodes-do-not-get-highlighted-until-exiting-and-re-entering-the-perk-menu)
    - [Dark Brotherhood abducted me when trying to start the Helgen Intro!](#dark-brotherhood-abducted-me-when-trying-to-start-the-helgen-intro)
    - [Wicked Game Quest (Val Serano) bugged out because of the Dark Brotherhood trying to abduct me!](#wicked-game-quest-val-serano-bugged-out-because-of-the-dark-brotherhood-trying-to-abduct-me)
    - [Carriage Horse in Solitude is partially in the wall!](#carriage-horse-in-solitude-is-partially-in-the-wall)
    - [Not receiving Courier Letter from Dark Brotherhood!](#not-receiving-courier-letter-from-dark-brotherhood)
    - [Being randomly attacked or arrested by NPCs!](#being-randomly-attacked-or-arrested-by-npcs)
    - [\[Insert Male NPC\] looks like he has tits / has a really big chest and arms!](#insert-male-npc-looks-like-he-has-tits--has-a-really-big-chest-and-arms)
    - [Can't attack with Left Hand in First Person (Dual Wield or Unarmed)!](#cant-attack-with-left-hand-in-first-person-dual-wield-or-unarmed)
    - [Widgets overlap TrueHUD Attributes Widget!](#widgets-overlap-truehud-attributes-widget)
    - [Stuck in slow motion!](#stuck-in-slow-motion)
  - [Known Crashes](#known-crashes)
    - [Wheeler.dll Crash!](#wheelerdll-crash)
    - [Crashing when talking to Azura/Peryite/Augur of Dunlain/\[Insert Talking Head Activator\]!](#crashing-when-talking-to-azuraperyiteaugur-of-dunlaininsert-talking-head-activator)
    - [Crashing after loading a save! / Crashing after dying!](#crashing-after-loading-a-save--crashing-after-dying)
      - [Experimental fix for crash on load (after dying, after fast travel, from a carriage ride, or just reloading a save game)](#experimental-fix-for-crash-on-load-after-dying-after-fast-travel-from-a-carriage-ride-or-just-reloading-a-save-game)

## FAQ

### Q: Do I have to read this?
A: No, but if you ask me any question on this document, I will refer you back to here.

### Q: Can I uncap the FPS?
A: The list is capped to 61 FPS by default. While [SSE Display Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/34705) adjusts timing values based on framerate to prevent physics from spazzing out at high framerates, some mods may use havok code that still rely on a ~60 FPS cap to prevent physics-based issues. If you wish to uncap the FPS, then you can do so in the ENB menu **AND** in the `SSEDisplayTweaks.ini` file in the `[Performance] SSE Display Tweaks - Modified` mod.

### Q: What mod is it that makes favorited items/potions/quest items show on my character?
A: [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001). You can open the menu with `Left Shift+Backspace` to customize what you want to show and what you don't want to show.

### Q: How do I reposition my weapons? / Can I have swords on my back?
A: Open the [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001) GUI with `Left Shift+Backspace` and reposition your equipment.

### Q: My character is really skinny and the weight sliders only adjust the neck and wrist, how do I change my character's body appearance?
A: Open the OBody menu with `;` (check or change the keybind in the MCM if you do not have a QWERTY keyboard).

### Q: How do I start the main questline?  
A: Go to the Helgen Inn, speak to Matlara, and select the dialogue option `"Give me your best room. (X gold) (Start Intro)"` in order to start the intro sequence.

### Q: I can't find Altano in the Windpeak Inn. / How do I start VIGILANT?  
A: VIGILANT requires the player be level 25, completion of House of Horrors, and completion of Kindred Judgement (the final quest of Dawnguard DLC). 

### Q: How do I start UNSLAAD?
A: UNSLAAD requires the completion of Dragonslayer (the final quest of the Main Quest).

### Q: What is the Pilgrim skill? / How do I access the Pilgrim skill tree?
A: The Pilgrim skill is added by [Pilgrim - Custom Skills Framework Addon](https://www.nexusmods.com/skyrimspecialedition/mods/93913) and acts as the way to progress the religion mechanic in the list. You can access the skill tree by using the **Pray** power while sneaking.

### Q: How do I set up the quick wheel?
A: There is extensive documentation on the [mod page](https://www.nexusmods.com/skyrimspecialedition/mods/97345).

### Q: I can't add a weapon/armor to the wheel.
A: This is usually caused by an alternate start mod that adds random items to your inventory. This only happens to the set of starting items you have. To fix this issue, simply drop the item onto the ground and pick it again.

### Q: Can I still use the vanilla favorites menu? I do not like the wheel.
A: If you're on keyboard press `G` to open up the vanilla favorites menu.

### Q: Can I add/remove [insert mod] to the list?
A: Yes, but if you have to ask, no. Also adding or removing a mod would void any official support.

### Q: Will you add [insert mod] to the list?
A: No, probably not. We'll see.

### Q: Will you add OStim/SexLab to the list?
A: If you want to commission me to do so, then maybe. Otherwise, no.

## Known Issues

### When leveling up skills, new perk nodes do not get highlighted until exiting and re-entering the perk menu!
Solution(s)
 1. This is a bug with advancing skills while inside of an active menu. I won't fix this, it's a minor visual bug, the perks can still be selected even if you don't exit and re-enter menu.

### Dark Brotherhood abducted me when trying to start the Helgen Intro!
Solution(s)
 1. Don't be stupid. Reload a save before starting the intro and make sure that you have been abducted BEFORE trying to start the Helgen Intro. 

### Wicked Game Quest (Val Serano) bugged out because of the Dark Brotherhood trying to abduct me!
Solution(s)
 1. See above.

### Carriage Horse in Solitude is partially in the wall!
Solution(s)
 1. This bug isn't worthy of my time and I have already tried to fix it. For some reason that is beyond my current comprehension, he does not move after being moved in the CK. I will not waste more brain power and time trying to figure out the cause of this very very minor issue.

### Not receiving Courier Letter from Dark Brotherhood!
Solution(s)
 1. This appears to happen sometimes but from my testing as long as you sleep in a bed they should still abduct you as intended. Not sure what is causing this as of yet.

### Being randomly attacked or arrested by NPCs!
Solution(s)
 1. open the console, select one of the NPCs, and type `paycrimegold 0 0`

### [Insert Male NPC] looks like he has tits / has a really big chest and arms!
Solution(s)
 1. Change their OBody preset, do not report this as an issue to me, I'm tired of hearing about it.

### Can't attack with Left Hand in First Person (Dual Wield or Unarmed)!
Solution(s)
 1. It works fine if you attack with right-hand first, otherwise right click (left-hand) will be treated as a "Block" input.

### Widgets overlap TrueHUD Attributes Widget!
Solution(s)
 1. Seems to be a rare bug and it's fixed on game restart, not sure of cause.

### Stuck in slow motion!
Solution(s)
 1. Bug with Wheeler, just reopen and close the wheel.

## Known Crashes

### Wheeler.dll Crash!
**Cause**: Wheeler typically crashes for one of two reasons: 
1. You slotted player-made potions in Wheeler and ran out of them.  
   **Fix**: Do not put player-made potions in Wheeler.  
2. You no longer have an item in your inventory that Wheeler is trying to reference.  
   **Fix**: Open dMenu (Default: `Home`). Navigate to Wheeler Controls --> Reset All Wheels. **This will reset your current Wheeler configuration**.

### Crashing when talking to Azura/Peryite/Augur of Dunlain/[Insert Talking Head Activator]!
**Cause**: Bug with the [Katana follower](https://www.nexusmods.com/skyrimspecialedition/mods/69622) mod if you are on the quest `Chasing the Current` with the quest stage `Talk to Katana another time`.  
**Fix**: Talk to Katana to progress to the next stage (`Head to the Drunken Huntsman`) in order to fix the crash.

### Crashing after loading a save! / Crashing after dying!
**Cause** Skyrim has a multitude of issues when it comes to loading back game data without restarting the game. There are a few culprits that could be the main driver of these crashes, but I have yet to collect enough information or consistently reproducible crashes to report it to the relevant authors.  
**Fix**: Please post logs in in the [discord](https://discord.gg/4WwqfK5yHg) channel `#apostasy-support` if you suffer from these crashes, but realize that I have very little ability to fix them at this current time.

#### Experimental fix for crash on load (after dying, after fast travel, from a carriage ride, or just reloading a save game)
<Details>

  
  1.  Navigate to `[Your Apostasy Install Location]\profiles\Apostasy\SkyrimPrefs.ini`  
  2.  Change `uLargeRefLODGridSize =9`  
  3.  to `uLargeRefLODGridSize =5`  
  4.  save changes (CTRL+S)  

This will reduce quality of some large objects at far away distance. **The difference is very minor you're unlikely to even notice it.** Might improve performance as well.
</Details>
