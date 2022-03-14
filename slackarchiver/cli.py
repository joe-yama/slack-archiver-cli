from dataclasses import dataclass
import os
import sys
import fire
from typing import Dict, Any, List

from slackarchiver.manage_channel import list_channels, archive_channels

def cli_list_channels() -> int:
    fire.Fire(list_channels)
    return 0


def cli_archive_channels() -> int:
    fire.Fire(archive_channels)
    return 0
