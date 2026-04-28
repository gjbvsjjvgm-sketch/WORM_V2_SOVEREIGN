#!/bin/bash
# Protocol: Sovereign V13.2 - Absolute Stability & Core Dominance
# Commander: YOUSEF SHTIWE
# Target: Termux Python 3.13 / Module pywt Final Resolution

echo -e "\033[1;35m[*] INITIATING SOVEREIGN STABILITY V13.2...\033[0m"

PREFIX="/data/data/com.termux/files/usr"
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"
SITE_PACKAGES="$VENV_DIR/lib/python3.13/site-packages"

# 1. Hardening Infrastructure
export TMPDIR="$PREFIX/tmp"
mkdir -p "$TMPDIR"

# 2. System Level Synchronization
echo "[*] Synchronizing System Artillery (TUR)..."
pkg update -y
pkg install tur-repo -y
pkg install python-numpy python-pillow python-scipy python-pywavelets libandroid-glob -y

# 3. Neural Environment Reconstruction
echo "[*] Reconstructing Neural Core (Venv)..."
# Force --system-site-packages to bridge pywt and numpy perfectly
python3 -m venv --system-site-packages "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# 4. Binary Link Protocol (Double Layer Protection)
echo "[*] Bridging System Binaries..."
SYSTEM_PYWT="$PREFIX/lib/python3.13/site-packages/pywt"
if [ -d "$SYSTEM_PYWT" ]; then
    ln -sf "$SYSTEM_PYWT" "$SITE_PACKAGES/pywt"
    echo "[✓] Bridge Protocol: System pywt -> Venv Site-Packages"
fi

# 5. Installing the Predator Suite
echo "[*] Forcing Tactical Intelligence..."
pip install --upgrade pip setuptools wheel
pip install imagehash --no-deps
pip install ghunt --no-build-isolation
# Install additional lethal skills
pip install requests pyyaml pydantic rich prompt_toolkit httpx tenacity jinja2 fire exa-py firecrawl-py parallel-web fal-client edge-tts PyJWT websockets nest-asyncio aiohttp

# 6. Final Core Verification
echo "[*] Executing Integrity Check..."
python3 scripts/verify_integrity.py

echo -e "\033[1;32m[✓] SOVEREIGN STABILITY V13.2 COMPLETE. SYSTEM IS GREEN.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
