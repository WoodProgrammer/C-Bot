import pytest
from bot import slackConnect, slackRtmRead


def test_slackConnection():
    assert slackConnect() == True

@pytest.mark.skip(reason="Not accually finished.")
def test_slackRtmRead():
    print(slackRtmRead())
