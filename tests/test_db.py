"""
Tests for database/db.py.

Each test points DB_PATH at a temporary file (via monkeypatch) instead of
the real alerts.db, so tests never touch or depend on your actual data.
"""

import database.db as db


def test_add_and_get_alert(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", str(tmp_path / "test_alerts.db"))
    db.init_db()

    db.add_alert(user_id="123", channel_id="456", item_slug="mesa_prime_set", target_price=60)

    alerts = db.get_all_alerts()
    assert len(alerts) == 1
    assert alerts[0]["item_slug"] == "mesa_prime_set"
    assert alerts[0]["target_price"] == 60


def test_remove_alert(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", str(tmp_path / "test_alerts.db"))
    db.init_db()

    db.add_alert(user_id="123", channel_id="456", item_slug="mesa_prime_set", target_price=60)
    alert_id = db.get_all_alerts()[0]["id"]

    db.remove_alert(alert_id)

    assert db.get_all_alerts() == []