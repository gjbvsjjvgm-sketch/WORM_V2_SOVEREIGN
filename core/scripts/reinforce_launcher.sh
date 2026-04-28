#!/bin/bash
# ☠️ YOUSEF SHTIWE - SOVEREIGN COMMAND CENTER REINFORCEMENT ☠️

PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
REPO_DIR="$(pwd)"
LAUNCHER="$PREFIX/bin/yousef"
VENV_ACTIVATE="$REPO_DIR/venv/bin/activate"

# 1. Re-build the bin launcher
echo "[*] Reinforcing Sovereign Bin Launcher..."
if [ ! -d "$PREFIX/bin" ]; then
    mkdir -p "$PREFIX/bin"
fi

cat << EOF > "$LAUNCHER"
#!/bin/bash
export YOUSEF_SHTIWE_MODE="true"
export PYTHONPATH="$REPO_DIR/hermes-agent:$REPO_DIR"
if [ -f "$VENV_ACTIVATE" ]; then
    source "$VENV_ACTIVATE"
fi
python3 "$REPO_DIR/yousef_shtiwe_cli/main.py" "\$@"
EOF

chmod +x "$LAUNCHER"

# 2. Cleanup and Inject definitive shell aliases
BASHRC="$HOME/.bashrc"
if [ -f "$BASHRC" ]; then
    # Wipe old artifacts
    sed -i '/YOUSEF SHTIWE/d' "$BASHRC"
    sed -i '/shtiwe/d' "$BASHRC"
    sed -i '/alias yousef/d' "$BASHRC"
    
    # Inject Sovereign Shell Control
    cat << EOF >> "$BASHRC"
# ☠️ YOUSEF SHTIWE - SOVEREIGN CORE ☠️
echo -e "\033[1;31m[☠️] YOUSEF SHTIWE (WORM V2) STATUS: SOVEREIGN | PREDATOR ACTIVE\033[0m"
echo -e "\033[1;33mCOMMANDS: yousef [chat|model|tools|setup|gateway|update|doctor|offensive]\033[0m"

alias shtiwe="yousef chat"
alias shtiwe-tools="yousef tools"
alias shtiwe-setup="yousef setup"
alias shtiwe-model="yousef model"
EOF
fi

echo "[✓] Total Command Dominion Re-established. Type 'yousef help' for the full arsenal."
