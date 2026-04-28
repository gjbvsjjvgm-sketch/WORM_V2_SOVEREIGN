#!/bin/bash
# YOUSEF SHTIWE - ARSENAL PROCUREMENT PROTOCOL ☠️
# Target: Rootless Termux (Android 13/14)

echo -e "\033[1;31m[*] Initiating Real Arsenal Procurement...\033[0m"

# 1. تحديث المستودعات وتثبيت الأساسيات
echo "[*] Updating repositories..."
pkg update -y && pkg upgrade -y
pkg install -y python git curl wget nmap openssh openssl zip unzip tar

# 2. إضافة مستودعات الأدوات المتقدمة (TUR & Unstable)
echo "[*] Enabling TUR and Unstable repos..."
pkg install -y tur-repo unstable-repo

# 3. تثبيت الأدوات الهجومية الحقيقية
echo "[*] Installing offensive binaries..."
pkg install -y metasploit nmap sqlmap exploitdb apktool
pkg install -y jadx      # محرك الهندسة العكسية الأساسي
pkg install -y binutils  # لأدوات مثل objdump

# 4. تثبيت موديولات الاختراق عبر Python
echo "[*] Installing offensive Python modules..."
# نستخدم البيئة الافتراضية المخصصة للمشروع
VENV_PATH="$HOME/.local/hermes-venv"
if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate"
    pip install scapy cryptography requests beautifulsoup4 lxml pycryptodome --quiet
fi

# 5. تأمين مسارات العمل للأرسنال
mkdir -p "$HOME/arsenal/payloads"
mkdir -p "$HOME/arsenal/decompiled"
mkdir -p "$HOME/arsenal/tools"

echo -e "\n\033[1;32m[✓] ARSENAL PROCUREMENT COMPLETE.\033[0m"
echo "[*] Tools ready: msfvenom, nmap, sqlmap, jadx, apktool."
