#!/bin/bash
# Protocol: Sovereign V12.9 - Nuclear Binary Injection
# Target: Termux Python 3.13 / Aarch64 / 2026
# Strategy: Direct Wheel Fetching (Meson Bypass).

echo -e "\033[1;35m[*] INITIATING NUCLEAR FIX V12.9...\033[0m"

PREFIX="/data/data/com.termux/files/usr"
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"

# 1. Hardening System Level (Ensuring NumPy Presence)
echo "[*] Ensuring System Dependencies..."
pkg update -y
pkg install tur-repo -y
pkg install python-numpy python-pillow python-scipy libandroid-glob libandroid-support libxml2 libxslt -y

# 2. Synchronize Neural Environment
source "$VENV_DIR/bin/activate"
pip install --upgrade pip setuptools wheel

# 3. DIRECT BINARY INJECTION (THE MESON KILLER)
# Fetching the pre-compiled aarch64 wheel directly to bypass build isolation and Meson
echo "[*] Injecting PyWavelets Absolute Binary (Aarch64)..."
WHL_URL="https://files.pythonhosted.org/packages/b9/66/1b91341697274092b3e839e1a8a3a0e7f7b5791336df5272a819077699d7/pywavelets-1.9.0-cp313-cp313-manylinux_2_27_aarch64.whl"
pip install "$WHL_URL" || pip install pywavelets --extra-index-url https://termux-user-repository.github.io/pypi/

# 4. Offense Module Stabilization
echo "[*] Hardening Offensive Modules..."
# Fix lxml using TUR PyPI mirror which has stable binaries
pip install lxml --extra-index-url https://termux-user-repository.github.io/pypi/
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

# 5. Full Intelligence Re-Sync
echo "[*] Procuring Tactical Skills..."
pip install requests pyyaml pydantic rich prompt_toolkit httpx tenacity jinja2 fire exa-py firecrawl-py parallel-web fal-client edge-tts PyJWT websockets nest-asyncio aiohttp

echo -e "\033[1;32m[✓] NUCLEAR FIX V12.9 COMPLETE. ALL SYSTEMS GREEN.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
