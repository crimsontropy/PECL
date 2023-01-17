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

endhtml = """</div>
</body>
</html>
"""

roomname_begin = """<div style=\"font-size: 2.5vw; background-color: navy; font-family: cursive; color: ghostwhite; text-align: center;\"><span style=\"color: red\"> Room Name:     </span>"""

roomname_mid = "<span style=\"float: right; font-size: 1.4vw\">"

roomname_end = "</span></div>"