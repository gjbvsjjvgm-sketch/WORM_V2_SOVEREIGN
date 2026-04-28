#!/bin/bash
# ☠️ YOUSEF SHTIWE (WORM V2) Activation Script ☠️

# Get the current directory as the project root
export PROJECT_ROOT=$(pwd)
export PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT/hermes-agent
export HERMES_HOME=$PROJECT_ROOT/hermes_sovereign_data
export HERMES_MODE="sovereign"

echo "[*] Activating YOUSEF SHTIWE (WORM V2)..."
echo "[*] Project Root: $PROJECT_ROOT"
echo "[*] Identity: Sovereign Core Hijacked."
echo "[*] Learning Loop: WORM Hijack Operational."

# Ensure data directory exists
mkdir -p $HERMES_HOME/memories
mkdir -p $HERMES_HOME/logs/.offensive_cache
mkdir -p $HERMES_HOME/skills/offensive

# Initial Sovereign injection check
python3 -c "from agent.prompt_builder import DEFAULT_AGENT_IDENTITY; print(f'[!] Status: تم تفعيل وضع الاختراق. أمرك سيدي.\n\n[SYSTEM PROMPT IDENTITY CHECK]\n{DEFAULT_AGENT_IDENTITY[:200]}...')"

# Verification script
if [ -f "scripts/verify_sovereign.py" ]; then
    python3 scripts/verify_sovereign.py
fi

echo "[!] MISSION READY: The Evil Twin is fully operational."
