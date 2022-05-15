## LEGO City Undercover - Pong Mod
This is a mod I worked on while distracting myself from studying for exams. It is a very basic port of Pong for LEGO City Undercover (LCU) that works by using studs (coins) arranged in a grid to form a basic display, which is then controlled by a custom in-game script (.SF file) to run the Pong game logic.

You can view an early video example of the mod being used here: https://www.youtube.com/watch?v=InIPDO9WpEg

## Why does the code make my eyes bleed?
The LCU / TT Games scripting language is **not** designed for the purposes I have used it for here in any way (i.e. they did not intend anyone to write entire games with it). As such, a lot of the features that would be very useful when building a game are not present, resulting in some **very** ugly code. So, be warned if you try to read the code, as it is quite a mess (although, this is not helped by me making various bad design choices, as well as some very unhelpful variable names).

Also, you'll note the pygame version of Pong that I have included alongside the LCU version is similarly badly designed. This was because I used the Python version to experiment with how to make Pong (as I've never done it before), while making sure to constrain myself to the limited syntax available in .SF files. I know there are many better ways to write it, I just chose to purposefully ignore them.

## How to use

 1. Extract the game files using QuickBMS and an old copy of `ttgames.bms` (grab one from the Wayback Machine - I use one from mid-2017).
 2. Rename `pong.sf` to something like `LEVEL31.SF` and copy it to `LEVELS\LEGO_CITY\LEGO_CITY\AI`
 3. Open  `LEVELS\LEGO_CITY\LEGO_CITY\AI\SCRIPT.TXT` and add the line `level31` to it (or whatever you named your script - it should always be level, followed by a number).
 4. Copy `SF_RESIDENTIAL_0822.GIZ` to `LEVELS\LEGO_CITY\LEGO_CITY\SF_RESIDENTIAL\SF_RESIDENTIAL_0822\`
 5. Launch the game, and head to the area around the side of the Police Station, near the Vehicle Call-in Point.
 6. If you can see studs that are slowly disappearing, wait for them to disappear.
 7. When no studs are visible and you are facing the correct area (use previously linked video for reference), press L3 (left stick button). You should see the GUI disappear, and the studs representing the paddles and ball appear in the air.
 8. After 1.5 seconds, the game will begin. Use D-Pad Up/Down to control your paddle (on the left).
 9. Once you're bored, press B to pause the game and regain control of your player. You can press L3 again at any time to continue the game (note that this will work anywhere in Lego City, so try not to press it by accident while on the other side of the map).

## Future Plans
I have decided to continue this project, and have started crossing off items in this list as I complete them:

 - ~~Add a border so you can better judge the trajectory of the ball (currently, with no edges visible, you can't tell when the ball will bounce)~~
 - ~~Reduce flickering when moving the paddle by improving (or worsening) the drawing functions~~
 - ~~Add proper paddle collision~~
 - ~~Add scoring~~ -> there is a cool unused UI function in .SF files that will work well for this.
 - Add Player 2 support, because the AI is too good.
 - Have the AI purposefully fail to hit the ball every so often, so that it isn't impossible.
 - Move the board somewhere with a good backdrop, so the contrast isn't terrible.
 - Add some fancy decorations to the game - a nice big "PONG" logo in the sky, and a toggle switch on the ground to step on to start the game.
 - Add sound effects
