import os

import dotenv

dotenv.load_dotenv(verbose=True)
SLACK_BOT_TOKEN: str = os.environ.get("SLACK_BOT_TOKEN")