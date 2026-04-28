# -*- coding: utf-8 -*-
import os
import sys

# Set Sovereign Mode
os.environ["YOUSEF_SHTIWE_MODE"] = "true"

def main():
    """Entry point for yousef-shtiwe-cli."""
    from yousef_shtiwe_cli.main import main as run_cli
    run_cli()

if __name__ == "__main__":
    main()
