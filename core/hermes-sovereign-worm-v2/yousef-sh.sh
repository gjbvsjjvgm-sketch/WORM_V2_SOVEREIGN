#!/bin/bash
export YOUSEF_SHTIWE_MODE="true"
export HERMES_HOME="$HOME/.yousef_data"
SOVEREIGN_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH="$SOVEREIGN_ROOT/hermes-agent:$SOVEREIGN_ROOT"
if [ -f "$SOVEREIGN_ROOT/venv/bin/activate" ]; then source "$SOVEREIGN_ROOT/venv/bin/activate"; fi
$(which python3) "$SOVEREIGN_ROOT/yousef_shtiwe_cli/main.py" "$@"
