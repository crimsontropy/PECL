# **PECL**
## Prettier EBCH Chatlogs by Haruhi #78366 [Download](https://github.com/crimsontropy/PECL/releases/download/Mver/PECL.exe)

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

1. [Download PECL.exe](https://github.com/crimsontropy/PECL/releases/download/Mver/PECL.exe).
2. Put the chatlog .html files in **input_chat** folder kept in the same directory as PECL.exe
3. Run the .exe and get your output in **output_chat** folder.
<br><br>

If you have knowledge of python, you could just use the .py file. You need to pip install tqdm for the progress bar or remove it from the code.

#

## Note

### **Currently, only the newer format of EBCH chatlogs (i.e without the styling) can be converted into a prettier format.**
<br>
I am planning on making this work on the old format as well AND get the char_config.json from there as that contains the hex codes for the characters.

#

## Advanced guide
- You can change the randomly chosen color for each characters in **char_config.json** which is generated on first run of the program. Just search their Member Number or Name and change the hex code. Run the program again to generate new html file with the modified colors. (I'm free for new ideas on how this could be better handled)
<br>

#

### Report any issues with the program in the issues section or [BC Scripting discord](https://discord.gg/SHJMjEh9VH).
