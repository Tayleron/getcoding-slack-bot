import os
import time
from slackclient import SlackClient
from dotenv import load_dotenv

load_dotenv('.env')

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)



rpgUser = {
    "user": None,
    "start": None,
    "total": None
} #dictionary name, start time, end time, total time

def handle_channel_join(event):
    print("Status change for ", event['user'])
    rpgUser ["user"] = event ["user"]
    rpgUser ["start"] = event ["ts"]
        if start != None:
            rpgUser ["total"] = ( event ["ts"] - rpgUser ["start"] ) + rpgUser ["total"]
            rpgUser["start"] = None




if sc.rtm_connect():
    while True:
        events = sc.rtm_read()

        for event in events:
            if event ["type"] == "message":
                if event ["text"] == "list users":
                    sc.api_call(
                        "chat.postMessage",
                        channel=event ["channel"], 
                        text="hello"
                    )
            elif event ["type"] == "presence_change":
                handle_channel_join(event)        



#if text is hello, then reply hi!

# if event.
#   time.sleep(1)

# else:
#      print("Connection Failed")