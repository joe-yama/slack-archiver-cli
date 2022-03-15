from typing import List

from slack_sdk import WebClient
from slackarchiver.manage_channel import (
    ArchiveResult,
    Channel,
    archive_channels,
    list_channels,
)


def test_list_channels(slack_webclient_mock: WebClient) -> None:
    channels: List[Channel] = list_channels(client=slack_webclient_mock)
    assert len(channels) == 2


def test_archive_channels(slack_webclient_mock: WebClient) -> None:
    archiveresult: ArchiveResult = archive_channels(
        channel_prefix="test-channel-", yes=True, client=slack_webclient_mock
    )
    assert archiveresult.success is True
    assert len(archiveresult.listed_channels) == 2
    assert len(archiveresult.archived_channels) == 2
