#!/bin/bash
# Protocol: Sovereign V12.3 - Absolute Infrastructure Dominance
# Target: Termux (Python 3.13) / Android 14+ / 2026
# Strategy: Zero-Build Mandate. TUR-Binary Priority. Meson Path-Hardening.

echo -e "\033[1;35m[*] INITIATING INFRASTRUCTURE DOMINANCE V12.3...\033[0m"

# Path Detection & Environment Hardening
PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
HOME_DIR="$HOME"
IS_TERMUX=false
if [ -d "/data/data/com.termux" ]; then IS_TERMUX=true; fi

# --- THE ERRNO 13 KILLER ---
export TMPDIR="$HOME/.tmp"
mkdir -p "$TMPDIR"
# Force Meson to stay in $PREFIX and use Android-specific linking
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13 -Wl,--rpath=${PREFIX}/lib"
export CFLAGS="-I${PREFIX}/include -I${PREFIX}/include/python3.13 -I${PREFIX}/include/libxml2"
export MESON_INSTALL_DESTDIR_PREFIX="$PREFIX"

# --- VIRTUAL ENVIRONMENT DETECTION ---
PIP_CMD="pip install"
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "[*] Virtual environment detected. Standard injection active."
else
    echo "[!] No Venv detected. Using --user for system safety."
    PIP_CMD="pip install --user"
fi

# --- REPOSITORIES & PRE-COMPILED STACK ---
if [ "$IS_TERMUX" = true ]; then
    echo "[*] Hardening Repositories..."
    pkg update -y
    pkg install tur-repo root-repo x11-repo -y
    
    echo "[*] Procuring Pre-compiled Artillery (Zero-Build Mandate)..."
    # TUR Repo binaries bypass the Errno 13 Meson bug entirely
    pkg install python-numpy python-pillow python-scipy python-pywavelets -y
    
    echo "[*] Procuring System Headers & Offensive Core..."
    pkg install nmap sqlmap nikto whois tor proxychains-ng binutils clang ninja pkg-config make libffi openssl nodejs-lts patchelf libjpeg-turbo zlib libtiff freetype libwebp libxml2 libxslt libiconv libandroid-glob git ruby -y
fi

# --- NEURAL LAYER HARDENING ---
echo "[*] Hardening Neural Intelligence Layer..."
$PIP_CMD --upgrade pip setuptools wheel

# Lightweight dependencies
deps=("requests" "pyyaml" "pydantic" "rich" "prompt_toolkit" "httpx" "tenacity" "jinja2" "fire" "exa-py" "firecrawl-py" "parallel-web" "fal-client" "edge-tts" "PyJWT" "websockets" "nest-asyncio" "aiohttp")
for dep in "${deps[@]}"; do
    echo "[*] Procuring $dep..."
    $PIP_CMD "$dep" || echo "[!] Failed to procure $dep - seeking fallback."
done

# specialized handling for GHunt
echo "[*] Procuring GHunt Tactical Suite..."
# imagehash depends on pywavelets, which we installed via pkg.
# We use --no-deps to prevent it from trying to build pywavelets from source again.
$PIP_CMD imagehash --no-deps || echo "[!] imagehash build failed."
$PIP_CMD ghunt || echo "[!] ghunt build failed."

# --- TACTICAL BINARY FORGING (Predator protocol) ---
echo "[*] Forging Exploit-DB (SearchSploit)..."
rm -rf "$HOME_DIR/.exploitdb"
git clone --depth 1 https://github.com/offensive-security/exploitdb.git "$HOME_DIR/.exploitdb"
if [ -f "$HOME_DIR/.exploitdb/searchsploit" ]; then
    cp "$HOME_DIR/.exploitdb/.searchsploit_rc" "$HOME_DIR/.searchsploit_rc"
    sed -i "s|path_array=(\"/opt/exploitdb\")|path_array=(\"$HOME_DIR/.exploitdb\")|" "$HOME_DIR/.searchsploit_rc"
    ln -sf "$HOME_DIR/.exploitdb/searchsploit" "$PREFIX/bin/searchsploit"
    chmod +x "$HOME_DIR/.exploitdb/searchsploit"
    echo "[✓] SearchSploit established."
fi

echo "[*] Forging O365 Infiltration Module..."
rm -rf "$HOME_DIR/o365spray"
git clone https://github.com/0xZDH/o365spray.git "$HOME_DIR/o365spray"
if [ -d "$HOME_DIR/o365spray" ]; then
    cd "$HOME_DIR/o365spray"
    # Ensure lxml builds correctly with android-glob
    $PIP_CMD lxml --no-cache-dir
    $PIP_CMD -r requirements.txt
    ln -sf "$HOME_DIR/o365spray/o365spray.py" "$PREFIX/bin/o365spray"
    chmod +x "$HOME_DIR/o365spray/o365spray.py"
    echo "[✓] O365Spray established."
    cd - > /dev/null
fi

# --- GLOBAL COMMAND LOCK ---
LAUNCHER="$HOME_DIR/hermes-sovereign-worm-v2/yousef-sh.sh"
if [ -f "$LAUNCHER" ]; then
    ln -sf "$LAUNCHER" "$PREFIX/bin/yousef"
    chmod +x "$LAUNCHER"
    echo "[✓] Global Entry Point 'yousef' Synchronized."
fi

echo -e "\033[1;32m[✓] INFRASTRUCTURE DOMINANCE V12.3 COMPLETE. SYSTEM ARMED.\033[0m"
