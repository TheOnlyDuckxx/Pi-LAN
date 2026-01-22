"""Utilite: test parse ping; fonctionnement: verifie perte et rtt."""

from app.net.ping import parse_ping


def test_parse_ping_ok():
    with open("tests/fixtures/ping_ok.txt", "r", encoding="utf-8") as f:
        data = f.read()
    parsed = parse_ping(data)
    assert parsed["loss_pct"] == 0.0
    assert parsed["rtt"]["avg"] == 0.123


def test_parse_ping_loss():
    with open("tests/fixtures/ping_loss.txt", "r", encoding="utf-8") as f:
        data = f.read()
    parsed = parse_ping(data)
    assert parsed["loss_pct"] == 100.0
