# Warframe Market Price Tracker Bot

A Discord bot that tracks item prices on [Warframe Market](https://warframe.market)
and notifies users when an item they're watching drops to (or below) their target price.

<img width="607" height="86" alt="warframee" src="https://github.com/user-attachments/assets/5da6a192-e631-4c25-81e4-8852cb5d4894" />

## Why I built this

I play Warframe regularly and wanted a way to know when Prime parts or other
tradeable items hit a good price, without manually refreshing the market site.
This project also let me practice working with a real public API, persistent
storage, and building something people can actually use day-to-day.

# Warframe Market Price Tracker Bot

A Discord bot that tracks item prices on [Warframe Market](https://warframe.market)
and notifies users, in the channel they used the command in, when an item
they're watching drops to (or below) their target price — based only on
sellers who are actively in-game right now.

## Why I built this

I play Warframe regularly and wanted a way to know when Prime parts or other
tradeable items hit a good price, without manually refreshing the market site.
This project also let me practice working with a real public API, persistent
storage, background scheduling, and building something people can actually
use day to day, inspired by hearing about a similar market tracking project
built for World of Warcraft.

## Features

- `/track <item> <price>` — get notified when an item drops to your target price
- `/untrack <alert_id>` — stop tracking an alert
- `/myalerts` — list your active alerts
- `/price <item>` — check the current lowest active price on demand
- A background job checks all saved alerts every few minutes automatically
- Only considers sellers who are currently **in-game**, for realistic, up-to-date prices

## Tech stack

- Python
- [Warframe Market API v2](https://docs.warframe.market) (public, no key needed)
- discord.py
- SQLite

## Getting started (development)

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file (see .env.example) with your own Discord bot token
DISCORD_TOKEN=your_token_here

# 4. Run the bot
python main.py

# 5. Run tests
pytest
```

## Project structure

```
warframe-market-bot/
├── bot/
│   ├── config.py          # loads settings/secrets from .env
│   ├── market_client.py   # talks to the Warframe Market API
│   └── discord_bot.py     # Discord slash commands + background price checker
├── database/
│   └── db.py               # stores user price alerts (SQLite)
├── tests/
│   ├── test_market_client.py
│   └── test_db.py
├── main.py                 # entry point
├── requirements.txt
├── .env.example
└── README.md
```

## What I'd add with more time

- A `/list_items` autocomplete so users don't need to know exact item slugs
- Rate-limit handling for the Warframe Market API
- Deployment to a free always-on host instead of running locally
