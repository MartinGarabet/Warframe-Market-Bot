"""
The Discord bot itself.

Provides two slash commands:
- /track <item> <price>   -> saves an alert
- /untrack <alert_id>     -> removes an alert
"""

import discord
from discord import app_commands

from bot.config import DISCORD_TOKEN
from bot.market_client import get_lowest_active_price
from database.db import init_db, add_alert, get_all_alerts, remove_alert

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    init_db()
    await tree.sync()
    print(f"Logged in as {client.user}. Slash commands synced.")


@tree.command(name="track", description="Get notified when an item drops to a target price")
@app_commands.describe(item="Item slug, e.g. mesa_prime_set", price="Target price in platinum")
async def track(interaction: discord.Interaction, item: str, price: int):
    add_alert(user_id=str(interaction.user.id), item_slug=item, target_price=price)
    await interaction.response.send_message(
        f"Got it! I'll let you know when **{item}** drops to **{price}** platinum or below."
    )


@tree.command(name="untrack", description="Stop tracking an alert by its ID")
async def untrack(interaction: discord.Interaction, alert_id: int):
    remove_alert(alert_id)
    await interaction.response.send_message(f"Removed alert #{alert_id}.")


@tree.command(name="myalerts", description="List your active price alerts")
async def myalerts(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    all_alerts = get_all_alerts()
    my_alerts = [alert for alert in all_alerts if alert["user_id"] == user_id]

    if not my_alerts:
        await interaction.response.send_message("You have no active alerts.")
        return

    lines = [
        f"#{alert['id']}: {alert['item_slug']} at {alert['target_price']} platinum"
        for alert in my_alerts
    ]
    await interaction.response.send_message("\n".join(lines))


@tree.command(name="price", description="Check the current lowest active price of an item")
async def price(interaction: discord.Interaction, item: str):
    await interaction.response.defer()
    lowest_price = get_lowest_active_price(item)

    if lowest_price is None:
        await interaction.followup.send(f"No active sellers found for **{item}** right now.")
    else:
        await interaction.followup.send(f"Lowest active price for **{item}**: {lowest_price} platinum")


def run():
    client.run(DISCORD_TOKEN)