## LEGO City Undercover - Pong Mod
This is a mod I worked on while distracting myself from studying for exams. It is a very basic port of Pong for LEGO City Undercover (LCU) that works by using studs (coins) arranged in a grid to form a basic display, which is then controlled by a custom in-game script (.SF file) to run the Pong game logic.

You can view a video example of the mod being used here: https://www.youtube.com/watch?v=tNTxwAIV-iQ
You can also find an older version of the mod being demonstrated here: https://www.youtube.com/watch?v=InIPDO9WpEg (spoiler: it's bad)

## Why does the code make my eyes bleed?
The LCU / TT Games scripting language is **not** designed for the purposes I have used it for here in any way (i.e. they did not intend anyone to write entire games with it). As such, a lot of the features that would be very useful when building a game are not present, resulting in some **very** ugly code. So, be warned if you try to read the code, as it is quite a mess (although, this is not helped by me making various bad design choices, as well as some very unhelpful variable names) It should also be noted that I have made zero effort to clean the code up, despite knowing that it's a mess, so I humbly ask that you don't judge me for the trash I have created.

Also, you'll note the pygame version of Pong that I have included alongside the LCU version is similarly badly designed. This was because I used the Python version to experiment with how to make Pong (as I've never done it before), while making sure to constrain myself to the limited syntax available in .SF files. I know there are many better ways to write it, I just chose to purposefully ignore them.

## How to install/use
Installation and usage instructions are included in the release package, which you can download here: https://github.com/NodeTG/LCU-Pong/releases