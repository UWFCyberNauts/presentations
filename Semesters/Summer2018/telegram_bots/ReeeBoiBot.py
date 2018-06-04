#!/usr/bin/env python3.6

from http.client import HTTPSConnection
from urllib.parse import urlencode
from json import dumps, loads
from sys import argv, exit

def processJsonForMessageAndNewOffset(json):
    jsonResult = json['result']
    if len(jsonResult) < 1:
        print("No message!")
        return (None, None)
    else:
        messages = list()
        update_id = 0
        for update in jsonResult:
            message = update['message'] # I will always get these
            update_id = update['update_id'] # I will always get these
            try:
                messages.append(message['text']) # I may not get this
            except KeyError:
                print("Got a key error")
                return (None, None)

        return (messages, update_id)

botExt = "/bot"
getMe = "/getMe"
getUpdates = "/getUpdates"
offset = 0

if len(argv) == 3 and argv[1] == '-a' and len(argv[2]) == 45:
    botExt += argv[2]
else:
    print(f"Usage: {argv[0]} -a API_KEY")
    exit(1)

headers = {'Content-type': 'application/json'}
getUpdatesJson = dumps({'offset': offset, 'limit': 100, 'timeout': 30, 'allowed_updates': ['message']})

print(f"Calling POST: {botExt + getUpdates}")
tAPIConnection = HTTPSConnection("api.telegram.org", 443)

tAPIConnection.request("POST", botExt+getUpdates, getUpdatesJson, headers)
response = tAPIConnection.getresponse()

print(response.status, response.reason)
data = response.read().decode("UTF-8")
print(dumps(loads(data), sort_keys=True, indent=4))

messages, update_id = processJsonForMessageAndNewOffset(loads(data))

if not (messages == None) and not (update_id == None):
    print(messages)
    print(f"Next offset: {update_id}")
    offset = update_id
