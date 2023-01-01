import random
import json
import os
import sys
from tqdm import tqdm

print("\n========================== Prettier EBCH Chatlogs by Haruhi#78366 ==========================\n")


if not os.path.isdir("input_chat"):
    print("input_chat folder is missing.\n\nAdd your chatlogs in input_chat folder made in the same directory as this program for conversion.")
    input("\nPress enter to close...")
    sys.exit()

files = [f for f in os.listdir("input_chat") if os.path.isfile(os.path.join("input_chat", f))]
print("Files found in input_chat: ",files,end="\n\n")

beginhtml = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        canvas {
            padding: 0;
            margin: auto;
            outline: none;
            display: block;
            top:0;
            bottom: 0;
            left: 0;
            right: 0;
            position: absolute;
            width: 100%;
        }
        @media (min-aspect-ratio: 2/1) {
        canvas {
            width: unset;
            height: 100%;
        }
        }
        input {
            background: white;
        }
        textarea {
            background: white;
            resize: none;
        }
        * { -webkit-tap-highlight-color:rgba(0,0,0,0); }
        #TextAreaChatLog {
            background-color: white;
            border: 1px solid black;
            overflow: auto;
            word-wrap: break-word;
            padding: 0 !important;
        }
        .ChatMessage {
            position: relative;
            padding-left: 0.4em;
            overflow: hidden;
        }
        .ChatMessage::before {
            content: attr(data-time);
            float: right;
            color: gray;
            font-style: italic;
            font-size: 0.4em;
            margin-right: 0.2em;
        }
        .ChatMessage::after {
            content: attr(data-sender);
            position: absolute;
            color: gray;
            font-size: 0.3em;
            top: 1.6em;
            right: 0.2em;
        }
        .ChatMessageName {
            text-shadow: 0.05em 0.05em black;
        }
        .ChatMessageAction, .ChatMessageActivity{
            color: gray;
        }
        .ChatMessageEmote {
            color: gray;
            font-style: italic;
        }
        .ChatMessageWhisper {
            font-style: italic;
            color: silver;
        }
        #TextAreaChatLog[data-shrinknondialogue=true] .ChatMessageEmote {
            font-size: 0.75em;
        }
        #TextAreaChatLog[data-colortheme=dark], #TextAreaChatLog[data-colortheme="dark2"] {
        background-color: #111;
        color: #eee;
        }
        #TextAreaChatLog[data-colortheme=dark] .ChatMessageName {
        text-shadow: 0.05em 0.05em #eee;
        }
        #TextAreaChatLog[data-colortheme=dark] .ChatMessageWhisper, #TextAreaChatLog[data-colortheme="dark2"] .ChatMessageWhisper {
        color: #555;
        }

        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage, #TextAreaChatLog[data-colortheme="light2"] .ChatMessage {
        line-height: 1.4em;
        padding: 0.1em;
        padding-right: 2em;
        }
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessage {
        border-bottom: 1px solid rgba(0, 0, 0, 0.25);
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage {
        border-bottom: 1px solid rgba(255, 255, 255, 0.4);
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessageEmote,
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessageAction,
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessageActivity,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessageEmote,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessageAction,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessageActivity {
        font-size: 0.8em;
        }
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessageName {
        text-shadow: 0 0 0.12em rgba(0, 0, 0, .5);
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessageName {
        text-shadow: 0 0 0.12em rgba(255, 255, 255, .4);
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage::before,
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage::after,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessage::before,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessage::after {
        position: absolute;
        float: none;
        line-height: 1;
        font-size: 0.5em;
        right: 0.2em;
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage::before,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessage::before {
        top: 0.4em;
        }
        #TextAreaChatLog[data-colortheme="dark2"] .ChatMessage::after,
        #TextAreaChatLog[data-colortheme="light2"] .ChatMessage::after {
        top: 1.6em;
        }
        #TextAreaChatLog[data-enterleave=smaller] .ChatMessageEnterLeave {
            font-size: 0.5em;
            text-align: center;
        }
        #TextAreaChatLog[data-shrinknondialogue=true] .ChatMessageNonDialogue {
            font-size: 0.5em;
            text-align: center;
        }
        #TextAreaChatLog[data-enterleave=hidden] .ChatMessageEnterLeave {
            display: none;
        }
        #TextAreaChatLog[data-membernumbers=never] .ChatMessage::after,
        #TextAreaChatLog[data-membernumbers=onmouseover] .ChatMessage::after {
            display: none;
        }
        #TextAreaChatLog[data-membernumbers=onmouseover] .ChatMessage:hover::after {
            display: block;
        }
        #TextAreaChatLog[data-displaytimestamps=false] .ChatMessage::before {
            display: none;
        }
        #TextAreaChatLog[data-displaytimestamps=false] .ChatMessage::after {
            top: 0;
        }
        #TextAreaChatLog[data-colornames=false] .ChatMessageName {
            color: inherit !important;
            text-shadow: none;
            font-weight: bold;
        }
        #TextAreaChatLog[data-coloractions=false] .ChatMessageAction,
        #TextAreaChatLog[data-coloremotes=false] .ChatMessageEmote,
        #TextAreaChatLog[data-coloractivities=false] .ChatMessageActivity {
            background-color: transparent !important;
        }
        #TextAreaChatLog[data-whitespace=preserve] {
            white-space: pre-wrap;
            overflow-wrap: break-word;
        }
        </style>
        <title>Chat History</title>
    </head>
    <body style="margin: auto;">
        <div id="TextAreaChatLog" name="TextAreaChatLog" screen-generated="ChatRoom" 
            class="HideOnPopup" style="font-size: 2vw; font-family: &quot;Arial&quot;, 
            sans-serif; position: fixed;
            width: 100vw; height: 100vh; display: inline;" data-coloractions="true" data-coloractivities="true" data-coloremotes="true"
            data-colornames="true" data-colortheme="dark" data-displaytimestamps="true" data-enterleave="normal" data-fontsize="medium"
            data-membernumbers="always" data-mustyleposes="false" data-showactivities="true" data-showautomaticmessages="false"
            data-showbeepchat="true" data-showchathelp="true" data-shrinknondialogue="false" data-whitespace="preserve" data-censoredwordslist=""
            data-censoredwordslevel="0">"""

endhtml = """
    </div>
</body>
</html>
"""

r = lambda: random.randint(0,255)

for file in files:
    filename, file_extension = os.path.splitext(file)
    if file_extension != ".html":
        print("Ignoring",file,"as file extension isn't .html")
        continue
    print("Working on: ",file,end="\n\n")
    chatlog = []
    with open("input_chat\\" + file,"r") as chathtml:
        chatlog = chathtml.readline().split("<br>")

    # print(len(chatlog))
    chatby = []
    index = -1
    skipfile = False
    for doer in chatlog:
        try:
            if doer != "" and doer[0] == "[" and doer[-1] == "]":
                index += 1
                chatby.append([doer])
            else:
                if len(chatby[index]) == 1:
                    chatby[index].append(doer)
                else:
                    chatby[index][1] = chatby[index][1] + " <br> " + doer
        except:
            # print(doer,len(doer))
            print("Error parsing file. This may indicate that the file is in the old EBCH format.\n")
            skipfile = True
            break
            # input("Press Enter to close...")
            # sys.exit()
    if skipfile: continue
    print("No of chats: ",len(chatby))
    
    boilerplate = "<div class=\"ChatMessage "
    boilerend = " </div>"
    new_format = ""

    # player_rgbacolor = "255,0,138,0.1"
    # player_color = "#9d41bc"
    # player_rgbconv = "{}".format( tuple([int(player_color[i+1:i+3], 16) for i in (0, 2, 4)] + [0.1]))

    char_config = {}
    if os.path.isfile('char_config.json'):
        with open('char_config.json', 'r') as fp:
            char_config = json.load(fp)

    current_date = ""
    current_room = ""

    for x in tqdm(chatby):
        chat_details = x[0].split(" - ")
        # print(chat_details)
        chat_date = chat_details[0][1:]
        chat_time = chat_details[1]
        chat_room = chat_details[2].replace("Room: ","")
        chat_char = chat_details[3].replace("AccName: ","")
        chat_member_number = chat_details[4].replace("AccNum: ","")[:-1]
        # print(chat_char,chat_date,chat_member_number,chat_room)
        ischat = False
        iswhisp = False

        if current_room != chat_room or current_date != chat_date:
            new_format += "<div style=\"font-size: 2.5vw; background-color: navy; font-family: cursive; color: ghostwhite; text-align: center;\">" + "<span style=\"color: red\"> Room Name:     </span>" + chat_room + "<span style=\"float: right; font-size: 1.4vw\">" + chat_date +"</span></div>"
            current_room = chat_room
            current_date = chat_date

        if chat_member_number not in char_config:
            char_config[chat_member_number] = {}
            char_config[chat_member_number]["player_name"] = chat_char
            rgbacolor = (r(),r(),r(),0.1)
            player_rgbacolor = "{}".format(rgbacolor)
            player_color = "#%02X%02X%02X" % rgbacolor[:-1]
            char_config[chat_member_number]["player_color"] = player_color
            char_config[chat_member_number]["player_rgbacolor"] = player_rgbacolor

        new_format += boilerplate

        if x[1][0] == "(" and x[1][-1] == ")":
            new_format += "ChatMessageActivity ChatMessageNonDialogue\" "
        elif x[1][0] == "*" and x[1][-1] == "*":
            new_format += "ChatMessageEmote\" "
        elif x[1].startswith("Whisper"):
            new_format += "ChatMessageWhisper\" "
            iswhisp = True
        else:
            new_format += "ChatMessageChat\" "
            ischat = True
        
        new_format += "data-time=\"" + chat_time + "\" "
        new_format += "data-sender=\"" + chat_member_number + "\" "

        new_format += "style=\"background-color:rgba" + char_config[chat_member_number]["player_rgbacolor"] + ";\">"
        # new_format += "\n"

        if ischat or iswhisp:
            new_format += "<span class=\"ChatMessageName\" style=\"color:" + char_config[chat_member_number]["player_color"]
            c_loc = x[1].find(":")
            chat_from = x[1][:c_loc+1]
            chat_content = x[1][c_loc+1:]
            
            if ischat:
                new_format += ";\">" + chat_from + "</span>"
            else:
                new_format += "; font-style: italic;\">" + chat_from+ "</span>"
            new_format += chat_content
        else:
            new_format += x[1]

        new_format += boilerend

        # print(new_format)
        # break

    final_html = beginhtml + new_format + endhtml

    if not os.path.isdir("output_chat"):
        print("Creating output_chat folder...")
        os.mkdir("output_chat")
    print("\nSaving converted file in output_chat...")
    with open("output_chat\\-converted-"+file,"w") as createhtml:
        createhtml.write(final_html)
    print("Done!\n")

with open('char_config.json', 'w') as fp:
    json.dump(char_config, fp, sort_keys=True, indent=4)
input("\nPress enter to close...")