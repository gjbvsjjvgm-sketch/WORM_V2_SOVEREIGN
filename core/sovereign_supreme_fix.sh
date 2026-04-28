#!/bin/bash
# Protocol: Sovereign V12.5 - Absolute Infrastructure Lockdown
# Commander: YOUSEF SHTIWE
# Target: Termux Python 3.13 / Android 14+ / 2026
# Strategy: System-Site-Packages Injection. Zero-Compile Mandate. Hardened Linking.

echo -e "\033[1;35m[*] INITIATING SOVEREIGN SUPREME FIX V12.5...\033[0m"

# 1. Path & Environment Hardening
PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
HOME_DIR="$HOME"
export TMPDIR="$HOME/.tmp"
mkdir -p "$TMPDIR"
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13 -Wl,--rpath=${PREFIX}/lib"
export CFLAGS="-I${PREFIX}/include -I${PREFIX}/include/python3.13 -I${PREFIX}/include/libxml2"
export PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig:$PREFIX/share/pkgconfig"
export PKG_CONFIG_LIBDIR="$PREFIX/lib/pkgconfig"

# 2. System Level Procurement (The TUR Solution)
echo "[*] Synchronizing System Repositories (TUR 2026)..."
pkg update -y
pkg install tur-repo root-repo x11-repo -y
pkg install python-numpy python-pillow python-scipy python-pywavelets -y
pkg install libandroid-glob libandroid-support libxml2 libxslt libiconv clang make git ruby -y

# 3. Virtual Environment Restoration (System Injection)
VENV_PATH="$HOME_DIR/hermes-sovereign-worm-v2/venv"
if [ -d "$VENV_PATH" ]; then
    echo "[*] Injecting System Site-Packages into Venv..."
    # We re-initialize the venv with --system-site-packages to avoid building numpy/pywavelets
    python3 -m venv --system-site-packages "$VENV_PATH"
    source "$VENV_PATH/bin/activate"
else
    echo "[!] Venv not found. Creating sovereign environment..."
    python3 -m venv --system-site-packages "$VENV_PATH"
    source "$VENV_PATH/bin/activate"
fi

# 4. Neural Intelligence Hardening
echo "[*] Hardening Python Layer..."
pip install --upgrade pip setuptools wheel

# Force build lxml with hardened flags
echo "[*] Building Offensive XML Module (lxml)..."
pip install lxml --no-cache-dir

# Install dependencies using TUR PyPI Mirror for 3.13 compatibility
echo "[*] Procuring Defensive/Offensive Skills..."
deps=("requests" "pyyaml" "pydantic" "rich" "prompt_toolkit" "httpx" "tenacity" "jinja2" "fire" "exa-py" "firecrawl-py" "parallel-web" "fal-client" "edge-tts" "PyJWT" "websockets" "nest-asyncio" "aiohttp")
for dep in "${deps[@]}"; do
    pip install "$dep"
done

# specialized installation for imagehash/ghunt (Bypassing Meson)
echo "[*] Forcing GHunt Tactical Suite..."
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

# 5. Tactical Binary Forging
echo "[*] Forging Exploit-DB (SearchSploit)..."
rm -rf "$HOME_DIR/.exploitdb"
git clone --depth 1 https://github.com/offensive-security/exploitdb.git "$HOME_DIR/.exploitdb"
if [ -f "$HOME_DIR/.exploitdb/searchsploit" ]; then
    cp "$HOME_DIR/.exploitdb/.searchsploit_rc" "$HOME_DIR/.searchsploit_rc"
    sed -i "s|path_array=(\"/opt/exploitdb\")|path_array=(\"$HOME_DIR/.exploitdb\")|" "$HOME_DIR/.searchsploit_rc"
    ln -sf "$HOME_DIR/.exploitdb/searchsploit" "$PREFIX/bin/searchsploit"
    chmod +x "$HOME_DIR/.exploitdb/searchsploit"
    echo "[✓] SearchSploit Ready."
fi

echo "[*] Forging O365 Infiltration Module..."
rm -rf "$HOME_DIR/o365spray"
git clone https://github.com/0xZDH/o365spray.git "$HOME_DIR/o365spray"
if [ -d "$HOME_DIR/o365spray" ]; then
    cd "$HOME_DIR/o365spray"
    pip install -r requirements.txt
    ln -sf "$HOME_DIR/o365spray/o365spray.py" "$PREFIX/bin/o365spray"
    chmod +x "$HOME_DIR/o365spray/o365spray.py"
    echo "[✓] O365Spray Ready."
    cd - > /dev/null
fi

# 6. Synchronization of Command Core
cat << 'LAUNCHER' > "$HOME_DIR/hermes-sovereign-worm-v2/yousef-sh.sh"
#!/bin/bash
export YOUSEF_SHTIWE_MODE="true"
export HERMES_HOME="$HOME/.yousef_data"
SOVEREIGN_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH="$SOVEREIGN_ROOT/hermes-agent:$SOVEREIGN_ROOT"
if [ -f "$SOVEREIGN_ROOT/venv/bin/activate" ]; then source "$SOVEREIGN_ROOT/venv/bin/activate"; fi
$(which python3) "$SOVEREIGN_ROOT/yousef_shtiwe_cli/main.py" "$@"
LAUNCHER
chmod +x "$HOME_DIR/hermes-sovereign-worm-v2/yousef-sh.sh"
ln -sf "$HOME_DIR/hermes-sovereign-worm-v2/yousef-sh.sh" "$PREFIX/bin/yousef"

echo -e "\033[1;32m[✓] SOVEREIGN SUPREME FIX V12.5 COMPLETE. TOTAL DOMINATION ACTIVE.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
