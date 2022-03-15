import pytest
from unittest.mock import MagicMock

from pytest_mock.plugin import MockerFixture
from slack_sdk import WebClient

from testdata_loader import get_slackresponse
from testdata_loader import response_conversations_list
from testdata_loader import response_conversations_join
from testdata_loader import response_conversations_archive


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
