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

## FAQ

### Q: Do I have to read this?
A: No, but if you ask me any question on this document, I will refer you back to here.

### Q: Why does my game freeze after every load transition?
A: It's not freezing, the list has a [mod](https://www.nexusmods.com/skyrimspecialedition/mods/60958) that pauses the game after cell transitions.

### Q: What mod is it that makes favorited items/potions/quest items show on my character?
A: [Immersive Equipment Displays](https://www.nexusmods.com/skyrimspecialedition/mods/62001). You can open the menu with `Left Shift+Backspace` to customize what you want to show and what you don't want to show. You can also use IED to determine weapon positioning (if you want weapons to be sheathed on back for example).

### Q: I can't level up, what do I do?  
A: You need to sleep in a bed in order to level up. If you do not want to be forced to sleep in a bed, then you may change this option in the Survival Mode Control Panel MCM or disable Survival Mode.

### Q: How do I start the main questline?  
A: If you have chosen to be Dragonborn in the Skyrim Unbound MCM, then upon killing your first dragon, you will be summoned by the Greybeards. If you have chosen to not be the Dragonborn, then you can not proceed with the main questline, doing so will also lock you out of a fair amount of content in the list due to the way quest progression is setup.

### Q: When do dragons start spawning?  
A: By default, dragons are set to begin spawning once the player reaches level 10. Dragons will spawn at word walls before you encounter them in the wild.

### Q: How do I become the Thane of Whiterun?   
A: You must complete [The Blessings of Nature](https://en.uesp.net/wiki/Skyrim:The_Blessings_of_Nature) quest and talk to Jarl Balgruuf when the Gildergreen tree is repaired/the sappling blooms. He'll thank you and allow you to buy the Breezehome, and the standard thaneship quest (help people of the hold and buy a house to become a thane) will be available. Additionally, as of version 0.9.0+, you also need to complete the [Bleak Falls Barrow](https://en.uesp.net/wiki/Skyrim:Bleak_Falls_Barrow_(quest)) quest which can be started by asking Jarl Balgruuf for work. Please note that BFB is not required as part of the main questline.

### Q: I finished The Blessing of Nature, how long does the tree take to bloom?
A: It can take a few in-game days to a few in-game weeks. You can wait these out if you'd like, but make sure to do so away from Whiterun.

### Q: I can't find Altano in the Windpeak Inn. / How do I start VIGILANT?  
A: VIGILANT requires the player be level 25, completion of House of Horrors, and completion of Kindred Judgement (the final quest of Dawnguard DLC). 
> Similarly, GLENMORIL and UNSLAAD require certain quests to be completed in order to be played. GLENMORIL requires Vigilant, At the Summit of Apocrypha (the final quest of the Dragonborn DLC), and Sacred Anatomancer (a quest from Vigilant that can be started in the Ratway) to be completed. 
> UNSLAAD requires the completion of GLENMORIL and Dragonslayer (the final quest of the Main Questline).

### Q: How do I get rid of the black bars? How to disable letterbox.
A: Open the ENB Menu (Default `Shift+Enter`), Open `ENBPOSTPASS.FX`, Scroll down until you see "letterbox" and untick it, Press the "Save Configuration" button, Close the ENB Menu.

### Q: What is the Pilgrim skill / How do I access the Pilgrim skill tree?
A: The Pilgrim skill is added by [Pilgrim - Custom Skills Framework Addon](https://www.nexusmods.com/skyrimspecialedition/mods/93913) and acts as the way to progress the religion mechanic in the list. You can access the skill tree by using the **Pray** power while sneaking.

### Q: Issue with wrist/hand when weilding Warhammers or Battleaxes in first person without gauntlets.
A: This is an issue with in the vanilla game but becomes more apparent when using [CFPAO's](https://www.nexusmods.com/skyrimspecialedition/mods/87169) animations. The author said they will not fix it and I can not fix it. Just wear some gauntlets.

### Q: How do I set up the quick wheel?
A: There is extensive documentation on the mod page [here](https://www.nexusmods.com/skyrimspecialedition/mods/97345).

### Q: I can't add a weapon/armor to the wheel.
A: This is usually caused by an alternate start mod that adds random items to your inventory. This only happens to the set of starting items you have. To fix this issue, simply drop the item onto the ground and pick it again.

### Q: Can I still use the vanilla favorites menu? I do not like the wheel.
A: If you're on keyboard press `G` to open up the vanilla favorites menu.

### Q: Sex?
A: No.

## Known Issues

### Naked when in Vampire Lord form!
Solution(s)
 1. Skyrim Outfit System overrides the Armor that is "worn" in Vampire Lord form, but since only the Non-playable armor worn in Vampire Lord form works with Vampire Lord race, the armor that Outfit System visually equips is invisible. Minor issue that is not fixable unless the author of the mod adds some type of smart toggle if you are detected in a VL/WW transformation.

### Being randomly attacked or arrested by NPCs!
Solution(s)
 1. open the console, select one of the NPCs, and type `paycrimegold 0 0`

### Awakening Quest does not start!
Soultion(s)
 1. The quest will pop up in your journal when you free Serana from the tomb. Currently it does not start prior to this point because of something At Your Own Pace - Dawnguard does. 

### Having issues controlling NPCs in Sirenroot!
Solution(s)
 1. The issue is caused by a bad script interaction between Immersive Camera and Sirenroot. You can disable Immersive Camera (and its script patches) in the left hand pane of MO2 for the duration of Sirenroot.

### Crashing when talking to Azura/Peryite/Augur of Dunlain/[Insert Talking Head Activator]!
Solution(s)
 1. If you are using the Katana follower mod and you have the quest `Chasing the Current` with the quest stage `Talk to Katana another time`, then talk to Katana to progress to the next stage (`Head to the Drunken Huntsman`) in order to fix the crash.

### Map is very bright!
Solution(s)
 1. This is a conflict between Flat World Map Frameworks and Seasons of Skyrim. It only occurs during specific weather events and I have spoken to both authors about this. It will not be resolved.

### Body type won't change when trying to apply a new body through OBody.
Solution(s)
 1. This issue should be fixed with versions 4.2.0+ of [OBody NG](https://www.nexusmods.com/skyrimspecialedition/mods/77016), however if you still encounter this issue then you should check the [Troubleshooting Guide](https://www.nexusmods.com/skyrimspecialedition/articles/4868).

### [Insert Male NPC] looks like he has tits / has a really big chest and arms!
Solution(s)
 1. Change their OBody preset, do not report this as an issue to me, I'm tired of hearing about it.