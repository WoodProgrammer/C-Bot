import pytest
from bot import slackConnect, slackRtmRead, parseInputMessage

input = {'type': 'message', 'channel': 'DABDFD8GP', 'user': 'UA9LVEY64', 'text': 'ananasdads', 'ts': '1524232547.000489', 'source_team': 'TAABY7WCS', 'team': 'TAABY7WCS'}

def test_slackConnection():
    assert slackConnect() == True

@pytest.mark.skip(reason="Not accually finished.")
def test_slackRtmRead():
    print(slackRtmRead())


def test_parsetInputMessage():
    assert parseInputMessage(input) == ['UA9LVEY64','ananasdads']
