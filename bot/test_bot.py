import pytest
from bot import slackConnect, slackRtmRead, parseInputMessage, sendMessageToSlack

input = {'type': 'message', 'channel': 'CHANNEL', 'user': 'USER', 'text': 'ananasdads', 'ts': '||||', 'source_team': '|||', 'team': '|||'}

def test_slackConnection():
    assert slackConnect() == True

@pytest.mark.skip(reason="Not accually finished.")
def test_slackRtmRead():
    print(slackRtmRead())


def test_parsetInputMessage():
    assert parseInputMessage(input) == ['UA9LVEY64','ananasdads']


def test_sendMessageToSlack():
    assert sendMessageToSlack('CHAT_ID','testing message') == True
