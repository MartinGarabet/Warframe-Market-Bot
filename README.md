# Warframe Market Price Tracker Bot

A Discord bot that tracks item prices on [Warframe Market](https://warframe.market)
and notifies users when an item they're watching drops to (or below) their target price.

## Why I built this

I play Warframe regularly and wanted a way to know when Prime parts or other
tradeable items hit a good price, without manually refreshing the market site.
This project also let me practice working with a real public API, persistent
storage, and building something people can actually use daily.

## Status

Work still in progress. 

## Tech stack

- Python
- [Warframe Market API](https://warframe.market/api_docs) (public, no key needed)
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

# 3. Run the placeholder entry point
python main.py

# 4. Run tests
pytest
```

## Project structure

```
warframe-market-bot/
├── bot/
│   ├── config.py         # loads settings/secrets
│   └── market_client.py  # talks to the Warframe Market API
├── database/
│   └── db.py             # stores user price alerts
├── tests/
│   └── test_placeholder.py
├── main.py                # entry point
├── requirements.txt
└── README.md
```
