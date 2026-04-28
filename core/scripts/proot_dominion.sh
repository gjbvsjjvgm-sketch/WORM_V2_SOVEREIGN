#!/bin/bash
# Protocol: Sovereign V13.6 - Proot Dominion (The Nuclear Option)
# Commander: YOUSEF SHTIWE
# Strategy: PRoot-Distro (Ubuntu) containerization to bypass Android filesystem locks.
# Status: Final Execution Protocol

echo -e "\033[1;35m[*] INITIATING SOVEREIGN DOMINION V13.6 (PROOT PROTOCOL)...\033[0m"

# 1. Install Proot-Distro
echo "[*] Procuring Containerization Artillery..."
pkg update -y && pkg upgrade -y
pkg install proot-distro -y

# 2. Install Ubuntu Environment
echo "[*] Constructing Sovereign Fortress (Ubuntu)..."
proot-distro install ubuntu

# 3. Automation: Script to run INSIDE Ubuntu
cat << 'EOF' > sovereign_ubuntu_setup.sh
#!/bin/bash
echo "[*] Hardening Fortress Internals..."
apt update && apt upgrade -y
apt install python3.12 python3-pip python3-venv git curl -y

echo "[*] Procuring Absolute Binaries (No-Build Mandate)..."
# Ubuntu repos have pre-compiled wheels for aarch64
pip3 install --break-system-packages numpy pywavelets imagehash ghunt requests pyyaml pydantic rich prompt_toolkit httpx tenacity jinja2 fire

echo "[✓] Fortress Internals Secure."
EOF

# Move setup script to Ubuntu filesystem and execute it
echo "[*] Injecting Neural Code into Fortress..."
mv sovereign_ubuntu_setup.sh /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/tmp/
proot-distro login ubuntu -- bash /tmp/sovereign_ubuntu_setup.sh

# 4. Universal Command: The 'yousef' Hammer (Containerized Edition)
echo "[*] Locking Global Command 'yousef' (PRoot Redirect)..."
PREFIX="/data/data/com.termux/files/usr"
cat << 'EOF' > "$PREFIX/bin/yousef"
#!/bin/bash
# YOUSEF SHTIWE - SOVEREIGN COMMANDER V13.6 (PROOT)
if [ "$1" == "fortress" ]; then
    proot-distro login ubuntu
else
    proot-distro login ubuntu -- bash -c "PYTHONPATH=/root/hermes-sovereign-worm-v2 python3 /root/hermes-sovereign-worm-v2/yousef_shtiwe_cli/main.py $@"
fi
EOF
chmod +x "$PREFIX/bin/yousef"

# 5. Mirror Project to Ubuntu Home for execution
echo "[*] Mirroring Tactic Library to Fortress..."
cp -r "$HOME/hermes-sovereign-worm-v2" /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/root/

echo -e "\033[1;32m[✓] SOVEREIGN DOMINION V13.6 COMPLETE. SYSTEM IS ABSOLUTE.\033[0m"
echo -e "\033[1;33m[*] ACTION: yousef fortress (to enter) or yousef (to attack)\033[0m"
