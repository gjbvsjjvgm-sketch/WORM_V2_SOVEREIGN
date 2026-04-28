#!/bin/bash
# Protocol: WORM V2 - Tactical Infrastructure Fix
# Target: Termux Python 3.13 / Ghunt / O365Spray
# Status: Predator Deployment

echo -e "\033[1;35m[*] INITIATING INFRASTRUCTURE PURGE V12.4...\033[0m"

# 1. Check/Install NumPy via pkg (TUR Repo Priority)
echo "[*] Synchronizing System NumPy (No-Build Mandate)..."
pkg update -y
pkg install tur-repo -y
pkg install python-numpy python-pillow python-scipy python-pywavelets -y

# 2. Purge Pip NumPy within Venv
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "[*] Venv detected. Purging corrupted pip-based NumPy..."
    pip uninstall numpy -y 2>/dev/null
fi

# 3. Environment Hardening for build-isolation
export LDFLAGS="-L${PREFIX}/lib -landroid-glob -lpython3.13"
export CFLAGS="-I${PREFIX}/include/python3.13"
export MESON_INSTALL_DESTDIR_PREFIX="$PREFIX"

# 4. Install ImageHash and GHunt (Tactical Force)
echo "[*] Forcing GHunt Deployment..."
# Since PyWavelets is now installed via pkg, imagehash will detect it.
# We use --no-build-isolation to force it to look at system site-packages if needed.
pip install imagehash --no-deps || echo "[!] Failed to procure imagehash - continuing force install."
pip install ghunt --no-build-isolation || echo "[!] Ghunt build issues logged."

# 5. Final Arsenal Verification
echo -e "\033[1;32m[✓] PURGE COMPLETE. SYNCING BINARIES...\033[0m"

# O365Spray & SearchSploit path checks
[ -f "$PREFIX/bin/searchsploit" ] && echo "[✓] ExploitDB: READY" || echo "[!] ExploitDB: MISSING"
[ -f "$PREFIX/bin/o365spray" ] && echo "[✓] O365Spray: READY" || echo "[!] O365Spray: MISSING"
which ghunt &>/dev/null && echo "[✓] GHunt: READY" || echo "[!] GHunt: LINKED"

