# import random
import json
import os
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup as BSoup
from bs4 import NavigableString
from PECL_vars import beginhtml,endhtml,roomname_begin,roomname_mid,roomname_end
from PECL_funcs import new_format_content_distributer,old_format_content_distributer,general_chat_detail_set

print("\n========================== Prettier EBCH Chatlogs by Haruhi#78366 ==========================\n")


if not os.path.isdir("input_chat"):
    print("input_chat folder is missing.\n\nAdd your chatlogs in input_chat folder made in the same directory as this program for conversion.")
    input("\nPress enter to close...")
    sys.exit()

files = [f for f in os.listdir("input_chat") if os.path.isfile(os.path.join("input_chat", f))]
print("Files found in input_chat: ",files,end="\n\n")

def save_html(finalhtml):
    if not os.path.isdir("output_chat"):
        print("Creating output_chat folder...")
        os.mkdir("output_chat")
    print("\nSaving converted file in output_chat...")
    with open("output_chat\\-converted-"+file,"w") as createhtml:
        createhtml.write(finalhtml)
    print("Done!\n")

def new_parse_method(chatlog):
    chatby = new_format_content_distributer(chatlog)

    print("No of chats: ",len(chatby))
    
    boilerplate = "<div class=\"ChatMessage "
    boilerend = " </div>"
    new_format = ""

    current_date = ""
    current_room = ""

    for x in tqdm(chatby):
        chat_details = x[0].split(" - ")
        (chat_date,chat_time,chat_room,chat_char,chat_member_number) = general_chat_detail_set(chat_details,char_config)
        ischat = False
        iswhisp = False

        if current_room != chat_room or current_date != chat_date:
            new_format += roomname_begin + chat_room + roomname_mid + chat_date + roomname_end
            current_room = chat_room
            current_date = chat_date
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

        if ischat:
            new_format += ">"
        else:
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
    return new_format

def old_format_parser(chathtml,char_config):
    soup = BSoup(chathtml,"html.parser")
    for tag in soup.select(".lds-ellipsis"):
        tag.decompose()
    for tag in soup.select("div.bce-pending.ChatMessageEmote"):
        tag.decompose()
    chatlog = list(soup)

    am_new = []
    am_len = 0
    for i in chatlog[::-1]:
        if isinstance(i,NavigableString) or i.name == "br":
            # print(i)
            am_len += 1
            if isinstance(i,NavigableString):
                am_new.append(str(i))
        else:
            break
    new_format = ""
    if len(am_new) > 0:
        new_format = new_parse_method(am_new[::-1])
        chatparsed = old_format_content_distributer(chatlog[:-am_len])
    else:
        chatparsed = old_format_content_distributer(chatlog)

    current_date = ""
    current_room = ""
    old_format = ""
    print("No of chats:",len(chatparsed))

    for x in tqdm(chatparsed):
        # try: 
        chat_details = x[0].split(" - ")
        chat_data = x[1]

        (chat_date,chat_time,chat_room,chat_char,chat_member_number) = general_chat_detail_set(chat_details,char_config,chat_data)

        if current_room != chat_room or current_date != chat_date:
            old_format += roomname_begin + chat_room + roomname_mid + chat_date + roomname_end
            current_room = chat_room
            current_date = chat_date
            continue
        
        # if len(x) == 2:
        old_format += str(chat_data)
        # except:
        #     print(x)
    return old_format + new_format

# r = lambda: random.randint(0,255)

def new_format_parser(chathtml,char_config):
    chatlog = chathtml.readline().split("<br>")

    new_format = new_parse_method(chatlog)
    return new_format

old_chathtml = []
new_chathtml = []

char_config = {}
if os.path.isfile('char_config.json'):
    with open('char_config.json', 'r') as fp:
        char_config = json.load(fp)

for file in files:
    filename, file_extension = os.path.splitext(file)
    if file_extension != ".html":
        print("Ignoring",file,"as file extension isn't .html")
        continue
    print("Checking file: ",file)

    with open("input_chat\\" + file,"r") as chathtml:
        first_tag = chathtml.readline()
        first_tag = first_tag[first_tag.find("[")+1:first_tag.find("]")]
        # soup = BSoup(chathtml,"html.parser")
        # for tag in soup:
        #     if isinstance(tag,NavigableString):
        # first_tag = str(tag)
        if len(first_tag.split(" - ")) == 3:
            old_chathtml.append(file)
        elif len(first_tag.split(" - ")) == 5:
            new_chathtml.append(file)
        else:
            print("Format not detected, skipping.. ", file, end="\n\n")
print("File checks done.",end="\n\n")

for file in old_chathtml:
    print("Working on: ",file,end="\n\n")
    with open("input_chat\\" + file,"r") as chathtml:
        finalhtml = beginhtml + old_format_parser(chathtml,char_config) + endhtml
        save_html(finalhtml)
for file in new_chathtml:
    print("Working on: ",file,end="\n\n")
    with open("input_chat\\" + file,"r") as chathtml:
        finalhtml = beginhtml + new_format_parser(chathtml,char_config) + endhtml
        save_html(finalhtml)

with open('char_config.json', 'w') as fp:
    json.dump(char_config, fp, sort_keys=True, indent=4)
input("\nPress enter to close...")