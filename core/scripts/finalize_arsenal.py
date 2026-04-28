# -*- coding: utf-8 -*-
import os
import subprocess

def finalize_arsenal_installation():
    # هذا السكريبت سيتم استدعاؤه خلال 'yousef setup'
    print("[*] SECURING OFFENSIVE BINARIES (JADX, BINUTILS, METASPLOIT)...")
    
    # 1. إضافة مستودعات TUR و Unstable لضمان وجود jadx و metasploit
    subprocess.run(["pkg", "install", "tur-repo", "unstable-repo", "-y"], check=False)
    subprocess.run(["pkg", "update", "-y"], check=False)
    
    # 2. تثبيت الأدوات الحقيقية
    tools = [
        "jadx",         # Decompiler
        "binutils",     # Objdump, strings, etc.
        "metasploit",   # msfvenom
        "steg-cli",     # Steganography
        "apktool",      # APK patching
        "tcpdump"       # Network capture
    ]
    
    for tool in tools:
        print(f"[*] Procuring {tool}...")
        subprocess.run(["pkg", "install", tool, "-y"], check=False)

    print("[✓] ARSENAL BINARIES LOCKED AND LOADED.")

if __name__ == "__main__":
    finalize_arsenal_installation()
