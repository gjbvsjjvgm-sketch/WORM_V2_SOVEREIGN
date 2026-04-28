#!/bin/bash
# Protocol: Sovereign V13.0 - Dominion
# Commander: YOUSEF SHTIWE
# Target: Termux Python 3.13 / Android 14+
# Strategy: Build-Isolation Suppression. Path Redirection.

echo -e "\033[1;35m[*] INITIATING SOVEREIGN DOMINION V13.0...\033[0m"

PREFIX="/data/data/com.termux/files/usr"
HOME_DIR="$HOME"
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"

# --- INFRASTRUCTURE HARDENING ---
export TMPDIR="$PREFIX/tmp"
mkdir -p "$TMPDIR"
# Force environment to respect Termux prefix
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13"
export CFLAGS="-I${PREFIX}/include/python3.13"
export PKG_CONFIG_PATH="${PREFIX}/lib/pkgconfig"

# 1. Procurement of Pre-compiled Artillery
echo "[*] Synchronizing Repositories..."
pkg update -y
pkg install tur-repo -y
# We install python-numpy and others globally first
pkg install python-numpy python-pillow python-scipy libandroid-glob libandroid-support clang ninja make -y

# 2. Neural Environment Restoration
echo "[*] Stabilizing Neural Environment..."
python3 -m venv --system-site-packages "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip setuptools wheel

# 3. THE MESON KILLER: Installing Build Backends inside Venv
# We must have these present to use --no-build-isolation
echo "[*] Injecting Build Backends (Zero-Isolation Protocol)..."
pip install cython meson-python ninja

# 4. PRECISION STRIKE: PyWavelets Installation
echo "[*] Executing Precision Strike on PyWavelets (Errno 13 Bypass)..."
# We pass -Csetup-args to redirect libdir and bypass the system-level probe
# We use --no-build-isolation to use the system numpy
pip install pywavelets --no-build-isolation \
    -Csetup-args="--libdir=${PREFIX}/lib" \
    -Csetup-args="--prefix=${PREFIX}" || \
    pip install pywavelets --extra-index-url https://termux-user-repository.github.io/pypi/

# 5. Forging the Offensive Arsenal
echo "[*] Forcing GHunt Tactical Suite..."
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

echo "[*] Forcing O365 Infiltration Module..."
pip install lxml --extra-index-url https://termux-user-repository.github.io/pypi/

# 6. Global Command Synchronization
LAUNCHER="$HOME/hermes-sovereign-worm-v2/yousef-sh.sh"
if [ -f "$LAUNCHER" ]; then
    ln -sf "$LAUNCHER" "$PREFIX/bin/yousef"
    chmod +x "$LAUNCHER"
fi

echo -e "\033[1;32m[✓] SOVEREIGN DOMINION V13.0 COMPLETE. SYSTEM IS ABSOLUTE.\033[0m"
echo -e "\033[1;33m[*] ACTION: source ~/.bashrc && yousef\033[0m"
