"""
Tests for bot/market_client.py.

We fake ("mock") the Warframe Market API responses instead of making
real network calls, so these tests are fast and always predictable.
"""

from unittest.mock import patch, Mock

from bot.market_client import get_sell_orders, get_lowest_active_price


def make_fake_order(order_type: str, platinum: int, status: str) -> dict:
    """Helper to build a fake order dict shaped like the real API response."""
    return {
        "type": order_type,
        "platinum": platinum,
        "user": {"status": status},
    }


@patch("bot.market_client.requests.get")
def test_get_sell_orders_filters_out_buy_orders(mock_get):
    fake_orders = [
        make_fake_order("sell", 100, "ingame"),
        make_fake_order("buy", 50, "ingame"),
    ]
    mock_get.return_value = Mock(json=lambda: {"data": fake_orders})

    result = get_sell_orders("some_item")

    assert len(result) == 1
    assert result[0]["type"] == "sell"


@patch("bot.market_client.requests.get")
def test_get_lowest_active_price_picks_cheapest_ingame_seller(mock_get):
    fake_orders = [
        make_fake_order("sell", 100, "ingame"),
        make_fake_order("sell", 70, "ingame"),
        make_fake_order("sell", 50, "offline"),
    ]
    mock_get.return_value = Mock(json=lambda: {"data": fake_orders})

    price = get_lowest_active_price("some_item")

    assert price == 70


@patch("bot.market_client.requests.get")
def test_get_lowest_active_price_returns_none_when_no_one_ingame(mock_get):
    fake_orders = [
        make_fake_order("sell", 100, "offline"),
        make_fake_order("sell", 90, "online"),
    ]
    mock_get.return_value = Mock(json=lambda: {"data": fake_orders})

    price = get_lowest_active_price("some_item")

    assert price is None