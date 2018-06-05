#!/usr/bin/env python3.6

from http.client import HTTPSConnection
from json import dumps, loads
from sys import argv, exit
from datetime import datetime
from os.path import exists
from os import stat
import re # How fitting ^o^

def verboseSay(string):
    if verbose:
        print(string)

def processJsonForChatID(result_array, channel):
    chat_id = 0

    for update in result_array:
        chat = (update['message'])['chat']
        verboseSay(chat['title'])
        if chat['title'] == channel:
            chat_id = chat['id'] # I will always get these
            return chat_id

def processJsonForOffset(result_array):
    update_id = 0

    for update in result_array:
        update_id = update['update_id'] # I will always get these

    return update_id

def processJsonForMessage(result_array):
    messages = list()
    for update in result_array:
        message = update['message'] # I will always get these
        caught = False

        try:
            messages.append((message['text'], message['date'])) # I may not get this
        except KeyError:
            caught = True
            verboseSay("Got a key error")

            if caught:
                try:
                    messages.append((message['caption'], message['date']))
                except KeyError:
                    verboseSay("Not even a picture!")
                    return None

        return messages

headers = {'Content-type': 'application/json'}
botExt = "/bot"
getMe = "/getMe"
getUpdates = "/getUpdates"
sendMessage = "/sendMessage"
channelToListen = None
channelToListenID = None
verbose = False
file_logging = False
reee_file = None
regular_expression = re.compile(r"reee", re.IGNORECASE)
reee_count = 0
offset = 0

if len(argv) > 1:
    count = 0
    for arg in argv:
        count += 1
        if count <= len(argv):
            if arg == '-a':
                botExt += argv[count]
            elif arg == '-v':
                verbose = True
            elif arg == '-f':
                file_logging = True
                if exists(argv[count]):
                    if stat(argv[count]).st_size > 0:
                        reee_file = open(argv[count], 'r')
                        reee_count = int(reee_file.readline().rstrip())

                reee_file = open(argv[count], 'w')
            elif arg == '-c':
                channelToListen = argv[count]
        else:
            print(f"Usage: {argv[0]} [-v{{erbose}}] -a API_KEY -c CHANNEL_TO_LISTEN_TO -f COUNT_FILE\n\t\tWhere COUNT_FILE is the file that stores the REEE count\n\t\twhere CHANNEL_TO_LISTEN_TO is the channel that the bot will pay attention to")
            exit(1)

if not channelToListen:
    print(f"Usage: {argv[0]} [-v{{erbose}}] -a API_KEY -c CHANNEL_TO_LISTEN_TO -f COUNT_FILE\n\t\tWhere COUNT_FILE is the file that stores the REEE count\n\t\twhere CHANNEL_TO_LISTEN_TO is the channel that the bot will pay attention to")
    exit(1)

tAPIConnection = HTTPSConnection("api.telegram.org", 443)

while True:
    getUpdatesJson = dumps({'offset': offset, 'limit': 100, 'timeout': 30, 'allowed_updates': ['message']})

    verboseSay(f"Calling POST: {botExt + getUpdates}")

    tAPIConnection.request("POST", botExt + getUpdates, getUpdatesJson, headers)
    response = tAPIConnection.getresponse()

    verboseSay(f"Got: {response.status}, {response.reason}")

    data = loads(response.read().decode("UTF-8"))
    verboseSay(dumps(data, sort_keys=True, indent=4))

    results = data['result']

    if len(results) < 1:
        verboseSay("No message!")
        continue

    messages = processJsonForMessage(results)
    offset = processJsonForOffset(results) + 1

    if channelToListenID is None:
        channelToListenID = processJsonForChatID(results, channelToListen)
        verboseSay(f"Channel ID: {channelToListenID}")

    verboseSay(f"Offset: {offset}")

    if messages is not None: 
        unix_time = int(datetime.now().timestamp())
        verboseSay(f"Unix_Time: {unix_time}")

        for message, timestamp in messages:
            if re.search(regular_expression, message):
                verboseSay("Matched REEE")

                reee_count += 1
                if file_logging:
                    reee_file.seek(0)
                    reee_file.truncate()
                    reee_file.write(str(reee_count))
                    reee_file.flush()

                if (unix_time - timestamp) < 60 and (unix_time - timestamp) > -60:
                    verboseSay("Send REEE COUNT")

                    sendMessageJson = dumps({'chat_id': channelToListenID, 'text': f'Reee count: {reee_count}'})

                    verboseSay(f"Calling POST: {botExt + sendMessage}")
                    tAPIConnection.request("POST", botExt + sendMessage, sendMessageJson, headers)
                    response = tAPIConnection.getresponse()
                    verboseSay(f"After Speaking Got: {response.status}, {response.reason}")
                    verboseSay(dumps(loads(response.read().decode("UTF-8")), sort_keys=True, indent=4))

            else:
                verboseSay("Not a REEE match!")
            
