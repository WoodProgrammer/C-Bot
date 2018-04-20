import pytest
from bot import slackConnect, slackRtmRead


def test_slackConnection():
    assert slackConnect() == True


def test_slackRtmRead():
    print(slackRtmRead())
