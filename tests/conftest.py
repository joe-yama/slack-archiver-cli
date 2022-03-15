from unittest.mock import MagicMock

import pytest
from pytest_mock.plugin import MockerFixture
from slack_sdk import WebClient
from testdata_loader import (
    get_slackresponse,
    response_conversations_archive,
    response_conversations_join,
    response_conversations_list,
)


@pytest.fixture
def slack_webclient_mock(mocker: MockerFixture) -> WebClient:
    # Mocking conversations list
    conversations_list_mock: MagicMock = mocker.patch.object(
        WebClient, "conversations_list"
    )
    conversations_list_mock.return_value = get_slackresponse(
        data=response_conversations_list
    )

    # Mocking conversartions join
    conversations_join_mock: MagicMock = mocker.patch.object(
        WebClient, "conversations_join"
    )
    conversations_join_mock.return_value = get_slackresponse(
        data=response_conversations_join
    )

    # Mocking conversartions archive
    conversations_archive_mock: MagicMock = mocker.patch.object(
        WebClient, "conversations_archive"
    )
    conversations_archive_mock.return_value = get_slackresponse(
        data=response_conversations_archive
    )
    return WebClient("mytoken")
