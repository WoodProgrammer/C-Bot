from slackclient import SlackClient
from config import API_KEY
from bot_helper import run_payload
import time, json

slack_client = SlackClient(API_KEY)


def slackConnect():
    print(API_KEY)
    return slack_client.rtm_connect()

def slackRtmRead():
    while True:
        data = slack_client.rtm_read()
        try:
            if data[0]['type'] == 'message':
                print(run_payload(data[0]['text']))
        except Exception as exp:
            print(exp)
        time.sleep(1)


def parseInputMessage(input):
    return [input['user'],input['text']]

def sendMessageToSlack(channel_name,input):
    try:
        slack_client.api_call('chat.postMessage',channel=channel_name, text=input, as_user=True)
        return True
    except:
        return False
