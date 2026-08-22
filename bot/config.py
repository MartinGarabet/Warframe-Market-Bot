"""
Configuration loading for the bot.

"""

import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")

if not DISCORD_TOKEN:
    raise ValueError(
        "DISCORD_TOKEN is missing. Make sure you have a .env file "
        "with DISCORD_TOKEN=your_token_here in the project root."
    )