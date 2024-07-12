![](https://raw.githubusercontent.com/Oghma-Infinium/Apostasy/main/images/Banner.png)

<p align="center">
  [ <a href="https://www.nexusmods.com/skyrimspecialedition/mods/118893">Nexus</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/README.md">Installation</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/GAMEPLAY.md">Gameplay Guide</a> |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/CHANGELOG.md">Changelog</a> |
  <a href="https://loadorderlibrary.com/lists/Apostasy">Modlist</a> |
  FAQ |
  <a href="https://github.com/Oghma-Infinium/Apostasy/blob/main/Documentation/CONFIG.md">Configuration</a> |
  <a href="https://ko-fi.com/aljoxo">Ko-fi</a> | 
  <a href="https://www.patreon.com/aljoxo">Patreon</a> ]
</p>

---

## FAQ

### Q: Do I have to read this?
A: No, but if you ask me any question on this document, I will refer you back to here.

### Q: Can I uncap the FPS?
A: The list is capped to 61 FPS by default. While [SSE Display Tweaks](https://www.nexusmods.com/skyrimspecialedition/mods/34705) adjusts timing values based on framerate to prevent physics from spazzing out at high framerates, some mods may use havok code that still rely on a ~60 FPS cap to prevent physics-based issues. If you wish to uncap the FPS, then you can do so in the ENB menu **AND** in the `SSEDisplayTweaks.ini` file in the `[Performance] SSE Display Tweaks - Modified` mod.

### Q: What mod is it that makes favorited items/potions/quest items show on my character?
A: [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001). You can open the menu with `Left Shift+Backspace` to customize what you want to show and what you don't want to show.

### Q: How do I reposition my weapons? / Can I have swords on my back?
A: Open the [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001) GUI with `Left Shift+Backspace` and reposition your equipment.

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

### HUD / UI Disappears during Helgen Intro!
Solution(s)
 1. This seems to be an issue that will sometimes occur with [TrueHUD](https://www.nexusmods.com/skyrimspecialedition/mods/62775) when the `SetCartHUD` function is used in papyrus. I have removed this function (as it's not necessary to the functionality of the Helgen Intro with [Alternate Perspective](https://www.nexusmods.com/skyrimspecialedition/mods/50307)), however if it still occurs then **restarting your game** will return your HUD / UI to normal.

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

### Naked when in Vampire Lord form!
Solution(s)
 1. Skyrim Outfit System overrides the Armor that is "worn" in Vampire Lord form, but since only the Non-playable armor worn in Vampire Lord form works with Vampire Lord race, the armor that Outfit System visually equips is invisible. Minor issue that is not fixable unless the author of the mod adds some type of smart toggle if you are detected in a VL/WW transformation.

### Not receiving Courier Letter from Dark Brotherhood!
Solution(s)
 1. This appears to happen sometimes but from my testing as long as you sleep in a bed they should still abduct you as intended. Not sure what is causing this as of yet.

### Being randomly attacked or arrested by NPCs!
Solution(s)
 1. open the console, select one of the NPCs, and type `paycrimegold 0 0`

### Having issues controlling NPCs in Sirenroot!
Solution(s)
 1. The issue is caused by a bad script interaction between Immersive Camera and Sirenroot. You can disable Immersive Camera (and its script patches) in the left hand pane of MO2 for the duration of Sirenroot.

### Body type won't change when trying to apply a new body through OBody.
Solution(s)
 1. This issue should be fixed with versions 4.2.0+ of [OBody NG](https://www.nexusmods.com/skyrimspecialedition/mods/77016), however if you still encounter this issue then you should check the [Troubleshooting Guide](https://www.nexusmods.com/skyrimspecialedition/articles/4868).

### [Insert Male NPC] looks like he has tits / has a really big chest and arms!
Solution(s)
 1. Change their OBody preset, do not report this as an issue to me, I'm tired of hearing about it.

### Can't attack with Left Hand in First Person (Dual Wield or Unarmed)!
Solution(s)
 1. I am currently looking for an elegant solution to this issue, but the list is first and foremost focused on third person. If you wish to play a DW or Unarmed-based build in first person, I would suggest rethinking your build or playing a list that is more suitable for this.

### Widgets overlap TrueHUD Attributes Widget!
Solution(s)
 1. Seems to be a rare bug and it's fixed on game restart, not sure of cause.

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

### Consistently crashing in the same cell!
**Cause**: There are several potential causes of a crash, one of the more common ones being lighting related.
**Fix**: Post your crashlogs in the [discord](https://discord.gg/4WwqfK5yHg) channel `#apostasy-support`.

### Crashing after loading a save! / Crashing after dying!
**Cause** Skyrim has a multitude of issues when it comes to loading back game data without restarting the game. There are a few culprits that could be the main driver of these crashes, but I have yet to collect enough information or consistently reproducible crashes to report it to the relevant authors.
**Fix**: Please post logs in in the [discord](https://discord.gg/4WwqfK5yHg) channel `#apostasy-support` if you suffer from these crashes, but realize that I have very little ability to fix them at this current time.