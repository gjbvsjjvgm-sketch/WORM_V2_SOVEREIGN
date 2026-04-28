#!/bin/bash
# YOUSEF SHTIWE (WORM V2) - Sovereign Entry Point
export YOUSEF_SHTIWE_MODE="true"
export HERMES_HOME=$(pwd)/hermes_sovereign_data
export PYTHONPATH=$(pwd)/hermes-agent:$(pwd)
python3 -m yousef_shtiwe_cli.main "$@"
