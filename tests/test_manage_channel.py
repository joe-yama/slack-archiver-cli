from typing import List

from slackarchiver.manage_channel import Channel, list_channels


def test_list_channels() -> None:
    channels: List[Channel] = list_channels()
    assert len(channels) > 0
