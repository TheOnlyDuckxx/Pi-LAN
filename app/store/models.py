"""Utilite: schema conceptuel; fonctionnement: reference des tables SQLite attendues."""

# Tables:
# clients(id, ip, mac, alias, last_seen, first_seen)
# ping_results(id, client_id, ts, avg_ms, jitter_ms, loss_pct)
# port_scans(id, client_id, ts, open_ports_json)
# events(id, ts, type, payload_json)
