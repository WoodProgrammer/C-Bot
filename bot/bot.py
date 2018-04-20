from slackclient import SlackClient
from config import API_KEY
slack_client = SlackClient(API_KEY)


def slackConnect():
    print(API_KEY)
    return slack_client.rtm_connect()

def slackRtmRead():
    return slack_client.rtm_read()
