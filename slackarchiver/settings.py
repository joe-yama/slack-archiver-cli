import os

import dotenv


dotenv.load_dotenv(verbose=True)

if "SLACK_BOT_TOKEN" not in os.environ:
    raise KeyError("Environment variable `SLACK_BOT_TOKEN` was not found.")

SLACK_BOT_TOKEN: str = os.environ.get("SLACK_BOT_TOKEN")