#!/bin/bash
# ☠️ YOUSEF SHTIWE - SOVEREIGN COMMAND CENTER INJECTOR ☠️

PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
REPO_DIR="$(pwd)"
LAUNCHER="$PREFIX/bin/yousef"
VENV_ACTIVATE="$REPO_DIR/venv/bin/activate"

# 1. Re-build the bin launcher
echo "[*] Injecting Sovereign Bin Launcher..."
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

# 2. Inject help text into the welcome message
BASHRC="$HOME/.bashrc"
if [ -f "$BASHRC" ]; then
    # Clear old Sovereign lines
    sed -i '/YOUSEF SHTIWE/d' "$BASHRC"
    sed -i '/alias shtiwe/d' "$BASHRC"
    
    cat << EOF >> "$BASHRC"
echo -e "\033[1;31m[☠️] YOUSEF SHTIWE (WORM V2) STATUS: SOVEREIGN | PREDATOR ACTIVE\033[0m"
echo -e "\033[1;33mCOMMANDS: yousef [chat|model|tools|setup|gateway|update|doctor|offensive]\033[0m"

alias shtiwe="yousef chat"
alias shtiwe-tools="yousef tools"
alias shtiwe-setup="yousef setup"
EOF
fi

echo "[✓] Command 'yousef' established. Type 'yousef chat' or 'yousef setup' to begin."
