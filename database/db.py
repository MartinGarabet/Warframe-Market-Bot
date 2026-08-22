"""
This module will handle storing and reading price alerts using SQLite.

Each alert says: "this Discord user wants to know when this item
drops to or below this price."
"""

import sqlite3

DB_PATH = "alerts.db"


def init_db() -> None:
    """
    Create the alerts table if it doesn't already exist.
    Safe to call every time the bot starts up.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            item_slug TEXT NOT NULL,
            target_price INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_alert(user_id: str, item_slug: str, target_price: int) -> None:
    """
    Save a new alert: notify user_id when item_slug drops to
    target_price platinum or below.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO alerts (user_id, item_slug, target_price) VALUES (?, ?, ?)",
        (user_id, item_slug, target_price)
    )

    connection.commit()
    connection.close()


def get_all_alerts() -> list[dict]:
    """
    Return every alert currently stored, as a list of dicts,
    example [{"id": 1, "user_id": "123", "item_slug": "mesa_prime_set", "target_price": 60}, ...]
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT id, user_id, item_slug, target_price FROM alerts")
    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


def remove_alert(alert_id: int) -> None:
    """
    Delete an alert by its id.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM alerts WHERE id = ?", (alert_id,))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
    add_alert(user_id="test_user_123", item_slug="mesa_prime_set", target_price=60)

    print("Current alerts:")
    for alert in get_all_alerts():
        print(alert)