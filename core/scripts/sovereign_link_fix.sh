#!/bin/bash
# Protocol: Sovereign V13.2 - Forced Module Injection
# Target: Termux Python 3.13 / Module pywt Missing Fix

echo -e "\033[1;35m[*] INITIATING FORCED MODULE INJECTION V13.2...\033[0m"

PREFIX="/data/data/com.termux/files/usr"
VENV_DIR="$HOME/hermes-sovereign-worm-v2/venv"
SITE_PACKAGES="$VENV_DIR/lib/python3.13/site-packages"

# 1. Ensure TUR-repo and System PyWavelets are installed
echo "[*] Synchronizing System Binaries (TUR)..."
pkg update -y
pkg install tur-repo -y
pkg install python-pywavelets python-numpy python-pillow -y

# 2. Re-stabilize Virtual Environment
source "$VENV_DIR/bin/activate"

# 3. THE CRITICAL LINK: Link system-installed PyWavelets into the Venv
echo "[*] Bridging System 'pywt' into Sovereign Environment..."
SYSTEM_PYWT="$PREFIX/lib/python3.13/site-packages/pywt"
SYSTEM_PYWT_INFO=$(ls -d "$PREFIX/lib/python3.13/site-packages/PyWavelets-"* 2>/dev/null)

if [ -d "$SYSTEM_PYWT" ]; then
    ln -sf "$SYSTEM_PYWT" "$SITE_PACKAGES/pywt"
    [ -n "$SYSTEM_PYWT_INFO" ] && ln -sf "$SYSTEM_PYWT_INFO" "$SITE_PACKAGES/"
    echo "[✓] Link Established: pywt -> $SITE_PACKAGES/pywt"
else
    echo "[!] System pywt not found. Attempting emergency TUR-PyPI fetch..."
    pip install pywavelets --extra-index-url https://termux-user-repository.github.io/pypi/
fi

# 4. Forcing Predator Modules
echo "[*] Forcing Tactical Suite..."
pip install imagehash --no-deps
pip install ghunt --no-build-isolation

# 5. Final Verification using Python script
echo "[*] Verifying Intelligence Integrity..."
python3 scripts/verify_integrity.py

echo -e "\033[1;32m[✓] SOVEREIGN LINK V13.2 COMPLETE. THE CORE IS STABLE.\033[0m"
echo -e "\033[1;33m[*] ACTION: yousef\033[0m"
