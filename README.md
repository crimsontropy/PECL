# **PECL**
## Prettier EBCH Chatlogs by Haruhi #78366 [Download](https://github.com/crimsontropy/PECL/releases/download/allF/PECL.exe)

A quick and easy way to get some styling on [EBCH chatlogs](https://e2466.gitlab.io/ebch/).
Thanks to Elicia #10831 for the logger! 
<br><br>
Sample Image:
<br>
<img src="https://cdn.discordapp.com/attachments/1034819975522828352/1059154395973025912/image.png" width="60%" height="60%">
<!-- ![image1](https://cdn.discordapp.com/attachments/1034819975522828352/1059154395973025912/image.png =250x250) -->

#

## How to use: 

- ## The Standard Way (Windows only)

1. [Download PECL.exe](https://github.com/crimsontropy/PECL/releases/download/allF/PECL.exe).
2. Create a **input_chat** folder in tne same directory as the exe. 
3. Put the chatlog .html files in **input_chat** folder.
4. Run the .exe and get your output in **output_chat** folder.
<br><br>

If you have knowledge of python, you could just use the .py file. You need to pip install tqdm for the progress bar or remove it from the code.

#

## Advanced guide
- The newer chatlogs don't have character color information present, so its best if you keep older chatlogs in the folder if you have them, which would be picked up by PECL to color the rest of the places the character shows up. 
- You can change the randomly chosen color for each characters in **char_config.json** which is generated on first run of the program. Just search their Member Number or Name and change the hex code. Run the program again to generate new html file with the modified colors. (I'm free for new ideas on how this could be better handled)
<br>

#

### Report any issues with the program in the issues section or [BC Scripting discord](https://discord.gg/SHJMjEh9VH) to @crimsonfox#9325.
