"""
This module will talk to the Warframe Market API (v2).

It knows how to fetch current sell orders for a given item and figure out
the lowest price currently available from an online or in-game seller.
"""

import requests

BASE_URL = "https://api.warframe.market/v2"


def get_sell_orders(item_slug: str) -> list[dict]:
    """
    Fetch all sell orders for a given item from warframe market.

    item_slug: the item's URL-friendly name, example "mesa_prime_set"
    Returns a list of order dicts as given by the API.
    """
    url = f"{BASE_URL}/orders/item/{item_slug}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    all_orders = data["data"]

    return [order for order in all_orders if order["type"] == "sell"]


def get_lowest_active_price(item_slug: str) -> int | None:
    """
    Return the lowest sell price currently offered by a seller who is
    actively in-game right now for the given item.

    Returns None if there are no in-game sellers right now.
    """
    sell_orders = get_sell_orders(item_slug)

    active_orders = [
        order for order in sell_orders
        if order["user"]["status"] == "ingame"
    ]

    if not active_orders:
        return None

    lowest_order = min(active_orders, key=lambda order: order["platinum"])
    return lowest_order["platinum"]


if __name__ == "__main__":
    test_slug = "mesa_prime_set"
    price = get_lowest_active_price(test_slug)

    if price is None:
        print(f"No active sellers found for {test_slug} right now.")
    else:
        print(f"Lowest active price for {test_slug}: {price} platinum")