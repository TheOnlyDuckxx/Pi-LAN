#!/usr/bin/env bash
# Utilite: installer sur Pi; fonctionnement: deps, venv, systemd.
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .

sudo mkdir -p /var/lib/lanhub
sudo cp systemd/lanhub.service /etc/systemd/system/lanhub.service
sudo systemctl daemon-reload
sudo systemctl enable lanhub
sudo systemctl restart lanhub
