#!/bin/bash
# Protocol: Sovereign V13.1 - Ultimate Dominion
# Commander: YOUSEF SHTIWE
# Strategy: Meson-Skip Injection & TUR-Binary Priority
# Status: Final Execution

echo -e "\033[1;35m[*] INITIATING ULTIMATE DOMINION FIX V13.1...\033[0m"

PREFIX="/data/data/com.termux/files/usr"
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"

# --- THE ERRNO 13 KILLER (Proposed Solution 1 & 2) ---
export MESON_PYTHON_SKIP_LIBDIR_SCAN=1
export PKG_CONFIG_PATH="${PREFIX}/lib/pkgconfig"
export PYTHONUSERBASE="${PREFIX}"
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13"
export CFLAGS="-I${PREFIX}/include/python3.13"

# 1. Procurement of Absolute Binaries
echo "[*] Synchronizing System Artillery (Zero-Build Mandate)..."
pkg update -y
pkg install tur-repo -y
# Install the exact pre-built packages to satisfy GHunt/ImageHash
pkg install python-numpy python-pillow python-scipy python-pywavelets libandroid-glob libandroid-support libxml2 libxslt -y

# 2. Neural Environment Reconstruction (System Injection)
echo "[*] Synchronizing Neural Environment (Venv)..."
# We must use --system-site-packages so the venv sees the pkg-installed pywavelets
python3 -m venv --system-site-packages "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# 3. Neural Layer Hardening
pip install --upgrade pip setuptools wheel

# 4. Tactical Installation (Bypassing Rebuilds)
echo "[*] Forcing Predator Modules (No-Build Isolation)..."
# We install with --no-deps because system site-packages already has the heavy dependencies
pip install imagehash --no-deps
pip install ghunt --no-build-isolation
# Install lxml from TUR mirror to ensure binary compatibility
pip install lxml --extra-index-url https://termux-user-repository.github.io/pypi/

# 5. Full Intelligence Re-Sync
echo "[*] Procuring Tactical Skills..."
pip install requests pyyaml pydantic rich prompt_toolkit httpx tenacity jinja2 fire exa-py firecrawl-py parallel-web fal-client edge-tts PyJWT websockets nest-asyncio aiohttp

# 6. Final Verification
echo "[*] Verifying Neural Integrity..."
python3 -c "import numpy; import pywt; import PIL; print('[✓] Binary Integrity: VERIFIED')"

echo -e "\033[1;32m[✓] ULTIMATE DOMINION V13.1 COMPLETE. SYSTEM IS ABSOLUTE.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
