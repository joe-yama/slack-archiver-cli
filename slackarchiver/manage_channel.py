from dataclasses import dataclass
import sys

from typing import List, Dict

from slack_sdk.errors import SlackApiError
from slack_sdk import WebClient


from slackarchiver.settings import SLACK_BOT_TOKEN
from slackarchiver.utils import confirm_user_input


client: WebClient = WebClient(token=SLACK_BOT_TOKEN)


@dataclass
class Channel:
    id: int
    name: str

    def __str__(self):
        return self.name


def list_channels(
    channel_prefix: str = "",
    exclude_archived: bool = True,
    include_private_channels: bool = False
    ) -> List[Channel]:
    next_cursor: str = "" # for pagenation
    hit_channels: List[Channel] = []
    while True:
        response: Dict = client.conversations_list(
            exclude_archived=exclude_archived,
            types="public_channel,private_channel" if include_private_channels else "public_channel",
            limit=200,
            cursor=next_cursor
            )
        if not response["ok"] or not response:
            raise SlackApiError(f"Response of conversations_list api finished in fail. response: {response}")
        for channel in response["channels"]:
            if (channel_name:=channel["name_normalized"]).startswith(channel_prefix):
                # sys.stdout.write(channel_name+"\n")
                hit_channels.append(Channel(channel["id"], channel_name))
        next_cursor = response["response_metadata"]["next_cursor"]
        if not next_cursor:
            break
    return hit_channels


def archive_channels(
    channel_prefix: str,
    include_private_channels: bool = False
    ):
    target_channels: List[Channel] = list_channels(
        channel_prefix=channel_prefix,
        include_private_channels=include_private_channels)
    for channel in target_channels:
        sys.stdout.write(str(channel)+"\n")
    sys.stdout.write(f"{len(target_channels):,d} channels found (prefix: {channel_prefix})"+"\n")
    if not target_channels:
        # hit no channels
        return 

    if confirm_user_input(f"Do you want to archive {len(target_channels):,d} channels?"):
        raise NotImplementedError
        for channel in target_channels:
            # archive channel
            sys.stdout.write(f"Archived channel: {channel}"+"\n")
    return 
