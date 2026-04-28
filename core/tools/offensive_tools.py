# -*- coding: utf-8 -*-
import subprocess
import os
from pathlib import Path
from typing import Optional, Dict, Any

HERMES_HOME = Path.cwd()
WORM_CMD = "python3 scripts/worm_engine.py"

def _run_worm_command(subcommand: str, args: list = None) -> Dict[str, Any]:
    cmd = f"{WORM_CMD} {subcommand}"
    if args:
        cmd += " " + " ".join(str(a) for a in args)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def offensive_recon(target: str, recon_type: str = "basic"):
    return _run_worm_command("recon", [target, recon_type])

def offensive_exploit(target: str, exploit: str = "auto"):
    return _run_worm_command("exploit", [target, exploit])

def offensive_payload(lhost: str, lport: int, payload_type: str = "reverse_shell"):
    return _run_worm_command("payload", [lhost, str(lport), payload_type])

def offensive_zerotrace():
    return _run_worm_command("zero-trace", [])

TOOLS = {
    "offensive_recon": offensive_recon,
    "offensive_exploit": offensive_exploit,
    "offensive_payload": offensive_payload,
    "offensive_zerotrace": offensive_zerotrace,
}
