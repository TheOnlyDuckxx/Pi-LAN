"""Utilite: wrapper subprocess; fonctionnement: capture stdout/stderr avec timeout."""

import subprocess


def run_command(cmd: list[str], timeout: int = 5) -> dict:
    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return {"stdout": completed.stdout, "stderr": completed.stderr, "code": completed.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "timeout", "code": 124}
