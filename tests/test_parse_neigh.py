"""Utilite: test parse ip neigh; fonctionnement: verifie extraction IP/MAC/etat."""

from app.net.neigh import parse_ip_neigh


def test_parse_ip_neigh():
    with open("tests/fixtures/ip_neigh.txt", "r", encoding="utf-8") as f:
        data = f.read()
    entries = parse_ip_neigh(data)
    assert entries[0]["ip"] == "192.168.1.10"
    assert entries[0]["mac"] == "aa:bb:cc:dd:ee:ff"
