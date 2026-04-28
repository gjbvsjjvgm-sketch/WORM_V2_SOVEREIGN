import os
import re

def optimize_installer():
    installer_path = "scripts/install_termux.sh"
    if not os.path.exists(installer_path):
        print(f"[!] {installer_path} not found.")
        return

    with open(installer_path, 'r') as f:
        content = f.read()

    # 1. إزالة أمر 'pip install --user --upgrade pip' الممنوع في Termux
    # 2. إضافة المستودعات الضرورية للحزم الأمنية (TUR, Unstable)
    # 3. إضافة بروتوكول التثبيت اليدوي لـ searchsploit في حال فشل pkg

    setup_repos = """
# --- REPOSITORY EXPANSION ---
echo "[*] Expanding Repository Intelligence (TUR & Unstable)..."
pkg install tur-repo unstable-repo root-repo x11-repo -y
pkg update -y
# ----------------------------
"""
    
    # تصحيح أوامر الـ pip لتجنب الخطأ الممنوع
    content = content.replace('subprocess.run([sys.executable, "-m", "pip", "install", "--user", "--upgrade", "pip"], check=False)', '# pip upgrade is handled by pkg')
    
    # حقن المستودعات قبل تثبيت الحزم
    if "REPOSITORY EXPANSION" not in content:
        content = content.replace('if is_termux:', 'if is_termux:\n' + setup_repos)

    # إصلاح أمر تثبيت الحزم
    content = content.replace('subprocess.run(["pkg", "install", "nmap", "sqlmap", "nikto", "exploitdb", "argus", "argus-clients", "-y"], check=False)', 
                               'subprocess.run(["pkg", "install", "nmap", "sqlmap", "nikto", "exploitdb", "argus", "argus-clients", "tcpdump", "-y"], check=False)')

    with open(installer_path, 'w') as f:
        f.write(content)
    
    print("[✓] Installer Optimized for Security Repositories.")

def create_manual_fix_script():
    # سكريبت يدوي لتثبيت ما قد يفشل فيه pkg
    fix_script = """#!/bin/bash
echo "[*] Starting Sovereign Manual Arsenal Fix..."
pkg install tur-repo unstable-repo -y
pkg update -y
pkg install exploitdb argus argus-clients -y || {
    echo "[!] PKG failed. Forging manual searchsploit..."
    git clone https://gitlab.com/exploit-database/exploitdb.git $HOME/.exploitdb
    ln -sf $HOME/.exploitdb/searchsploit $PREFIX/bin/searchsploit
}
echo "[✓] Manual Fix Complete."
"""
    with open("scripts/manual_arsenal_fix.sh", "w") as f:
        f.write(fix_script)
    os.chmod("scripts/manual_arsenal_fix.sh", 0o755)

if __name__ == "__main__":
    optimize_installer()
    create_manual_fix_script()
