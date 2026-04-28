#!/bin/bash
# Protocol: Sovereign V12.6 - Absolute Environment Finality
# Commander: YOUSEF SHTIWE
# Target: Termux Python 3.13 / Android 14+ / 2026
# Strategy: TUR-PyPI Wheel Injection. System-Site-Packages Sync. 

echo -e "\033[1;35m[*] INITIATING SOVEREIGN FINAL FIX V12.6...\033[0m"

# 1. Environment Hardening
PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
export TMPDIR="$HOME/.tmp"
mkdir -p "$TMPDIR"
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13"
export CFLAGS="-I${PREFIX}/include/python3.13"

# 2. System Level Procurement (Essentials Only)
echo "[*] Synchronizing System Repositories..."
# We skip 'pkg install python-pywavelets' as it's missing, we'll use the wheel.
pkg update -y
pkg install tur-repo -y
pkg install python-numpy python-pillow python-scipy -y
pkg install libandroid-glob libandroid-support libxml2 libxslt libiconv clang make git -y

# 3. Virtual Environment Reconstruction (Sovereign Sync)
VENV_PATH="$HOME/hermes-sovereign-worm-v2/venv"
echo "[*] Reconstructing Sovereign Environment (System Injection)..."
python3 -m venv --system-site-packages "$VENV_PATH"
source "$VENV_PATH/bin/activate"

# 4. Neural Layer Procurement (Bypassing Build Failures)
echo "[*] Procuring Tactical Wheels (TUR PyPI Index)..."
# Using the special 2026 TUR PyPI mirror to get pre-compiled pywavelets for Python 3.13
pip install pywavelets --extra-index-url https://termux-user-repository.github.io/pypi/
pip install lxml --extra-index-url https://termux-user-repository.github.io/pypi/

# 5. Installing the Arsenal (Force Status)
echo "[*] Forcing GHunt Tactical Suite..."
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

echo "[*] Procuring Remaining Intelligence Skills..."
deps=("requests" "pyyaml" "pydantic" "rich" "prompt_toolkit" "httpx" "tenacity" "jinja2" "fire" "exa-py" "firecrawl-py" "parallel-web" "fal-client" "edge-tts" "PyJWT" "websockets" "nest-asyncio" "aiohttp")
for dep in "${deps[@]}"; do
    pip install "$dep"
done

# 6. Command Core Synchronization
[ -f "$HOME/hermes-sovereign-worm-v2/yousef-sh.sh" ] && ln -sf "$HOME/hermes-sovereign-worm-v2/yousef-sh.sh" "$PREFIX/bin/yousef"

echo -e "\033[1;32m[✓] SOVEREIGN FINAL FIX V12.6 COMPLETE. SYSTEM IS SUPREME.\033[0m"
echo -e "\033[1;33m[*] COMMAND: yousef\033[0m"
