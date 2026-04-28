#!/bin/bash
# YOUSEF SHTIWE - OMNIPOTENT REPAIR V13.6 ☠️
# [✓] REPAIR PROTOCOL: FIXING IMPORTS, PATHS, AND DEPENDENCIES.

echo -e "\033[1;31m[*] Initializing Sovereign Stability Protocol...\033[0m"

ROOT_DIR="$HOME/hermes-sovereign-unified-v13.6"
VENV_DIR="$HOME/.local/hermes-venv"
HERMES_CONFIG="$HOME/.hermes"

# 1. Ensure Root Path
cd "$ROOT_DIR" || exit

# 2. Fix PYTHONPATH
export PYTHONPATH="$ROOT_DIR:$ROOT_DIR/hermes-agent:$ROOT_DIR/hermes-agent/yousef_shtiwe_cli_core:$PYTHONPATH"

# 3. Activate Venv
if [ -d "$VENV_DIR" ]; then
    echo "[*] Activating Sovereign Venv..."
    source "$VENV_DIR/bin/activate"
else
    echo "[!] Warning: Venv not found. System might be unstable."
fi

# 4. Suppress Warnings
mkdir -p "$HERMES_CONFIG"
echo '{"suppress_warnings": true}' > "$HERMES_CONFIG/config.json"
export PYTHONWARNINGS="ignore"
export TIRITH_ENABLED="false"

# 5. Fix Python Imports & Structure
if [ -f "scripts/fix_cli_structure.py" ]; then
    echo "[*] Resolving Internal Import Conflicts..."
    python3 scripts/fix_cli_structure.py
fi

# 6. Enforce Version Locks
echo "[*] Locking Critical Dependencies (rich<15, anthropic)..."
pip install "rich>=14.3.3,<15" "anthropic>=0.39.0,<1" --quiet
pip install httpx-sse msgpack jiter termcolor scapy cryptography requests --quiet

# 7. Global Command Linking
chmod +x yousef-sh.sh
ln -sf "$ROOT_DIR/yousef-sh.sh" "$PREFIX/bin/yousef"

# 8. Bashrc Persistence
if ! grep -q "PYTHONWARNINGS" ~/.bashrc; then
    echo 'export PYTHONWARNINGS="ignore"' >> ~/.bashrc
    echo 'export TIRITH_ENABLED="false"' >> ~/.bashrc
    echo "export PYTHONPATH=\"$ROOT_DIR:$ROOT_DIR/hermes-agent:\$PYTHONPATH\"" >> ~/.bashrc
    echo 'alias yousef="bash $HOME/hermes-sovereign-unified-v13.6/yousef-sh.sh"' >> ~/.bashrc
fi

echo -e "\n\033[1;32m[✓] REPAIR COMPLETE – YOUSEF READY\033[0m"
echo "[*] Launching matrix with 'yousef --help'"
