#!/usr/bin/env python3.6

from http.client import HTTPSConnection
from json import dumps, loads
from sys import argv, exit
from datetime import datetime
import re

def processJsonForChatID(json, channel):
    jsonResult = json['result']
    if len(jsonResult) < 1:
        print("No message!")
        return None

    else:
        chat_id = 0

        for update in jsonResult:
            chat = (update['message'])['chat']
            print(chat['title'])
            if chat['title'] == channel:
                chat_id = chat['id'] # I will always get these
                return chat_id

def processJsonForOffset(json):
    jsonResult = json['result']
    if len(jsonResult) < 1:
        print("No message!")
        return None

    else:
        update_id = 0

        for update in jsonResult:
            update_id = update['update_id'] # I will always get these

        return update_id

def processJsonForMessage(json):
    jsonResult = json['result']
    if len(jsonResult) < 1:
        print("No message!")
        return None
    else:
        messages = list()
        for update in jsonResult:
            message = update['message'] # I will always get these
            caught = False

            try:
                messages.append((message['text'], message['date'])) # I may not get this
            except KeyError:
                caught = True
                print("Got a key error")

            if caught:
                try:
                    messages.append((message['caption'], message['date']))
                except KeyError:
                    print("Not even a picture!")
                    return None

        return messages

headers = {'Content-type': 'application/json'}
botExt = "/bot"
getMe = "/getMe"
getUpdates = "/getUpdates"
sendMessage = "/sendMessage"
channelToListen = "ReeeBoiTesting"
channelToListenID = None
regular_expression = re.compile(r"reee", re.IGNORECASE)
reee_count = 0
offset = 0

if len(argv) == 3 and argv[1] == '-a' and len(argv[2]) == 45:
    botExt += argv[2]
else:
    print(f"Usage: {argv[0]} -a API_KEY")
    exit(1)


tAPIConnection = HTTPSConnection("api.telegram.org", 443)

while True:
    getUpdatesJson = dumps({'offset': offset, 'limit': 100, 'timeout': 30, 'allowed_updates': ['message']})

    print(f"Calling POST: {botExt + getUpdates}")
    tAPIConnection.request("POST", botExt + getUpdates, getUpdatesJson, headers)
    response = tAPIConnection.getresponse()

    print(f"Got: {response.status}, {response.reason}")
    data = loads(response.read().decode("UTF-8"))

    print(dumps(data, sort_keys=True, indent=4))
    messages = processJsonForMessage(data)
    update = processJsonForOffset(data)

    if channelToListenID is None:
        channelToListenID = processJsonForChatID(data, channelToListen)
        print(f"Channel ID: {channelToListenID}")

    if update is not None:
        offset = update + 1

    print(f"Offset: {offset}")

    if messages is not None: 
        unix_time = int(datetime.now().timestamp())
        print(f"Unix_Time: {unix_time}")

        for message, timestamp in messages:
            if re.search(regular_expression, message):
                print("Matched REEE")
                reee_count += 1

                if (unix_time - timestamp) < 60 and (unix_time - timestamp) > -60:
                    print("Send REEE COUNT")
                    sendMessageJson = dumps({'chat_id': channelToListenID, 'text': f'Reee count: {reee_count}'})
                    tAPIConnection.request("POST", botExt + sendMessage, sendMessageJson, headers)
                    response = tAPIConnection.getresponse()
                    print(dumps(loads(response.read().decode("UTF-8")), sort_keys=True, indent=4))
                    print(f"After Speaking Got: {response.status}, {response.reason}")

            else:
                print("Not a REEE match!")
            
