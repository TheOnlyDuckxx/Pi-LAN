"""Utilite: helpers iperf; fonctionnement: documente usage basique si client dispo."""


def iperf_hint() -> str:
    return "iperf3 -s sur le host, iperf3 -c <host> sur le client"
