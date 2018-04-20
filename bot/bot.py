from slackclient import SlackClient
from config import API_KEY
import time

slack_client = SlackClient(API_KEY)


def slackConnect():
    print(API_KEY)
    return slack_client.rtm_connect()

def slackRtmRead():
    while True:
        print(slack_client.rtm_read())
        time.sleep(1)


def parseInputMessage(input):
    return [input['user'],input['text']]
