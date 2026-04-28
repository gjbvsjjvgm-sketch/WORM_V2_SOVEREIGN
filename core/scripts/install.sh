#!/bin/bash
# YOUSEF SHTIWE - ARSENAL INSTALLER ☠️

echo "[*] Procuring Real Binaries for Sovereign Core..."

# Enable Extra Repos
pkg install -y tur-repo unstable-repo

# Install Real Offensive Tools
pkg install -y metasploit nmap sqlmap jadx apktool binutils curl wget git python -y

echo "[✓] ARSENAL PROCURED."
