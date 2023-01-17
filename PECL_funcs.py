import random
from bs4 import NavigableString
# from tqdm import tqdm
import sys

def new_format_content_distributer(chatlog):
    chatby = []
    index = -1
    for doer in chatlog:
        doer = str(doer).strip()
        if len(doer) != 0 and doer[0] == "[" and doer[-1] == "]":
            index += 1
            chatby.append([doer])
        else:
            if len(chatby[index]) == 1:
                chatby[index].append(doer)
            else:
                chatby[index][1] = chatby[index][1] + " <br> " + doer
    return chatby

def old_format_content_distributer(chatlog):
    chatparsed = []
    index = -1
    previous_tag = ""
    for tag in chatlog:
        if isinstance(tag,NavigableString): #type(tag) == type(NavigableString("")):
            if not isinstance(previous_tag,NavigableString):
                chatparsed.append([tag])
                index += 1
            else:
                doer = str(tag).strip()
                # print(doer,len(doer),doer[0],doer[-1])
                # sys.exit()
                if not (len(doer) != 0 and doer[0] == "[" and doer[-1] == "]"):
                    # print(doer)
                    # sys.exit()
                    chatparsed[index].append(tag)
        else:
            chatparsed[index].append(tag)
        previous_tag = tag
    return chatparsed

r = lambda: random.randint(0,255)

# def get_div_member_number(chat_data):
#     return chat_data["data-sender"]

def get_div_rgba_color(chat_data = None):
    if chat_data is None:
        return (r(),r(),r(),0.1)
    # if chat_data.has_attr("style"):
    back_style = chat_data["style"]
    back_style = back_style.replace("background-color:rgba(","").strip()[:-2]
    back_style = back_style.split(",")
    try:
        red = int(back_style[0])
    except:
        red = r()
    try:
        green = int(back_style[1])
    except:
        green = r()
    try:
        blue = int(back_style[2])
    except:
        blue = r()
    try:
        alpha = float(back_style[3])
    except:
        alpha = 0.1
    
    return (red,green,blue,alpha)

def general_chat_detail_set(chat_details,char_config,chat_data = None):
    # chat_details = x[0].split(" - ")
    # print(chat_details)
    try:
        # print(type(chat_data))
        if len(chat_details) == 3:
            chat_date = chat_details[0][1:]
            chat_time = chat_details[1]
            chat_room = chat_details[2].replace("]","")
            # print(isinstance(chat_data,NavigableString),chat_data)
            if chat_data.has_attr("data-sender"):
                chat_member_number = chat_data["data-sender"]
            else:
                chat_member_number = ""
            # print(chat_member_number)
            chat_char = "-"
            # print(len(chat_member_number),chat_data["data-sender"])
            if len(chat_member_number) > 0 and chat_member_number not in char_config and chat_data.has_attr("style"):
                char_config[chat_member_number] = {}
                char_config[chat_member_number]["player_name"] = chat_char
                rgbacolor = get_div_rgba_color(chat_data)
                player_rgbacolor = "{}".format(rgbacolor)
                player_color = "#%02X%02X%02X" % rgbacolor[:-1]
                char_config[chat_member_number]["player_color"] = player_color
                char_config[chat_member_number]["player_rgbacolor"] = player_rgbacolor
                # print(char_config[chat_member_number])
        elif len(chat_details) == 5:
            chat_date = chat_details[0][1:]
            chat_time = chat_details[1]
            chat_room = chat_details[2].replace("Room: ","")
            chat_char = chat_details[3].replace("AccName: ","")
            chat_member_number = chat_details[4].replace("AccNum: ","")[:-1]
            if chat_member_number not in char_config:
                char_config[chat_member_number] = {}
                char_config[chat_member_number]["player_name"] = chat_char
                rgbacolor = get_div_rgba_color()
                player_rgbacolor = "{}".format(rgbacolor)
                player_color = "#%02X%02X%02X" % rgbacolor[:-1]
                char_config[chat_member_number]["player_color"] = player_color
                char_config[chat_member_number]["player_rgbacolor"] = player_rgbacolor
            elif char_config[chat_member_number]["player_name"] == "-":
                char_config[chat_member_number]["player_name"] = chat_char
        else:
            print(chat_details)
            sys.exit()
    except Exception as err:
        print(chat_data)
        print(f"Unexpected {err=}, {type(err)=}")
        sys.exit()
    return (chat_date,chat_time,chat_room,chat_char,chat_member_number)
