#!/bin/bash
echo "[*] Starting Sovereign Manual Arsenal Fix..."
pkg install tur-repo unstable-repo root-repo x11-repo -y
pkg update -y

# Attempting binary install first
pkg install exploitdb argus argus-clients -y

# Fallback for SearchSploit (exploitdb)
if ! command -v searchsploit &> /dev/null; then
    echo "[!] SearchSploit not found. Forging manual link..."
    if [ ! -d "$HOME/.exploitdb" ]; then
        git clone https://gitlab.com/exploit-database/exploitdb.git $HOME/.exploitdb
    else
        echo "[*] .exploitdb folder exists. Refreshing..."
        cd $HOME/.exploitdb && git pull origin main &> /dev/null
    fi
    ln -sf $HOME/.exploitdb/searchsploit $PREFIX/bin/searchsploit
fi

# Fallback for Argus (if still missing)
if ! command -v argus &> /dev/null; then
    echo "[!] Argus missing. Attempting TUR installation..."
    pkg install tur-repo -y && pkg update -y && pkg install argus argus-clients -y
fi

echo "[✓] Manual Fix Protocol Concluded."
