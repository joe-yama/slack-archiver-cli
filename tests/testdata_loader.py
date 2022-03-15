import json
import os
from pathlib import Path
from typing import Dict

from slack_sdk.web import SlackResponse
from slack_sdk import WebClient

TEST_ROOT: Path = Path(os.path.dirname(__file__))

with open(str(TEST_ROOT/"data/response_conversations_list.json")) as f:
    response_conversations_list: Dict = json.load(f)

with open(str(TEST_ROOT/"data/response_conversations_join.json")) as f:
    response_conversations_join: Dict = json.load(f)

with open(str(TEST_ROOT/"data/response_conversations_archive.json")) as f:
    response_conversations_archive: Dict = json.load(f)

def get_slackresponse(data: Dict) -> SlackResponse:
    return SlackResponse(
        client=WebClient("dummy"),
        http_verb="GET",
        api_url="http://localhost:8000",
        req_args=dict(),
        data=data,
        headers=dict(),
        status_code=200
    )
