"""
Configuration loading for the bot.

"""

import os

# Example of how this will look once we add python-dotenv:
# from dotenv import load_dotenv
# load_dotenv()
# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
