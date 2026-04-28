#!/bin/bash
# Protocol: Sovereign V12.7 - Absolute Environment Dominion
# Target: Termux Python 3.13 / 2026
# Strategy: TUR-PyPI Injection. Meson Bypass. Glob Linking.

echo -e "\033[1;35m[*] INITIATING SOVEREIGN SUPREME FIX V12.7...\033[0m"

# --- ENVIRONMENT OVERRIDE ---
PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
export TMPDIR="$HOME/.tmp"
mkdir -p "$TMPDIR"
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13"
export CFLAGS="-I${PREFIX}/include/python3.13"
export PYTHON_INSTALL_LAYOUT='deb'

# 1. System Level (TUR Priority)
echo "[*] Synchronizing System Artillery..."
pkg update -y
pkg install tur-repo -y
pkg install python-numpy python-pillow python-scipy libandroid-glob libandroid-support libxml2 libxslt clang make git -y

# 2. Virtual Environment Hardening
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"
echo "[*] Synchronizing Neural Environment (System Injection)..."
python3 -m venv --system-site-packages "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# 3. Procuring Tactical Wheels (Bypassing build errors)
echo "[*] Procuring Tactical Wheels (TUR PyPI mirror)..."
# We use the TUR PyPI mirror which has pre-compiled aarch64 wheels for 3.13
pip install --upgrade pip setuptools wheel
pip install pywavelets lxml --extra-index-url https://termux-user-repository.github.io/pypi/

# 4. Forcing GHunt and ImageHash
echo "[*] Forcing Predator Modules..."
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

# 5. Restoring Intelligence Layers
echo "[*] Procuring Intelligence Skills..."
pip install requests pyyaml pydantic rich prompt_toolkit httpx tenacity jinja2 fire exa-py firecrawl-py parallel-web fal-client edge-tts PyJWT websockets nest-asyncio aiohttp

# 6. Forging the Arsenal (Paths)
echo "[*] Finalizing Path Resolution..."
rm -rf "$HOME/.exploitdb"
git clone --depth 1 https://github.com/offensive-security/exploitdb.git "$HOME/.exploitdb"
if [ -f "$HOME/.exploitdb/searchsploit" ]; then
    ln -sf "$HOME/.exploitdb/searchsploit" "$PREFIX/bin/searchsploit"
    chmod +x "$PREFIX/bin/searchsploit"
fi

rm -rf "$HOME/o365spray"
git clone https://github.com/0xZDH/o365spray.git "$HOME/o365spray"
if [ -d "$HOME/o365spray" ]; then
    cd "$HOME/o365spray"
    pip install -r requirements.txt
    ln -sf "$HOME/o365spray/o365spray.py" "$PREFIX/bin/o365spray"
    cd - > /dev/null
fi

# 7. Global Activation
LAUNCHER="$HOME/hermes-sovereign-worm-v2/yousef-sh.sh"
if [ -f "$LAUNCHER" ]; then
    ln -sf "$LAUNCHER" "$PREFIX/bin/yousef"
    chmod +x "$LAUNCHER"
fi

echo -e "\033[1;32m[✓] SOVEREIGN SUPREME FIX V12.7 COMPLETE. SYSTEM IS ABSOLUTE.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
