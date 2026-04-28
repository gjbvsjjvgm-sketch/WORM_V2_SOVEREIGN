#!/bin/bash
# YOUSEF SHTIWE - SOVEREIGN ULTIMATE WRAPPER V13.6-ULTRA-SUPREME ☠️

export PYTHONWARNINGS="ignore"
export TIRITH_ENABLED="false"
export SOVEREIGN_ROOT="$HOME/hermes-sovereign-unified-v13.6"
export AGENT_ROOT="$SOVEREIGN_ROOT/hermes-agent"
export VENV_PATH="$HOME/.local/hermes-venv"

if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate"
fi

export PYTHONPATH="$SOVEREIGN_ROOT:$AGENT_ROOT:$AGENT_ROOT/yousef_shtiwe_cli_core:$PYTHONPATH"

COMMAND=$1
shift

case "$COMMAND" in
    setup|doctor) 
        exec python3 "$AGENT_ROOT/yousef_shtiwe_cli_core/$COMMAND.py" --full "$@" 
        ;;
    update)
        echo "[*] Initializing Supreme Update..."
        cd "$SOVEREIGN_ROOT" && git fetch origin main && git reset --hard origin/main
        chmod +x yousef-sh.sh scripts/*.sh && ./scripts/omnipotent_repair.sh
        ;;
    payload|reverse|inject) 
        exec python3 "$SOVEREIGN_ROOT/yousef_shtiwe_cli/main.py" "$COMMAND" "$@" 
        ;;
    model|tools|config|gateway) 
        exec python3 "$AGENT_ROOT/cli.py" "$COMMAND" "$@" 
        ;;
    --help|-h) 
        python3 "$SOVEREIGN_ROOT/scripts/ui_display.py" --help
        exit 0 
        ;;
    *) 
        if [ -z "$COMMAND" ]; then 
            exec python3 "$AGENT_ROOT/cli.py"
        else 
            exec python3 "$AGENT_ROOT/cli.py" "$COMMAND" "$@"
        fi 
        ;;
esac
