import os
import re

def patch_installer():
    installer_path = "scripts/install_termux.sh"
    if not os.path.exists(installer_path):
        print(f"[!] {installer_path} not found.")
        return

    with open(installer_path, 'r') as f:
        content = f.read()

    # إضافة بروتوكول الإصلاح الذاتي للمستودعات
    fix_logic = """
# --- SOVEREIGN REPO RECOVERY PROTOCOL ---
echo "[*] Applying Repo Recovery Protocol..."
rm -rf $PREFIX/var/lib/apt/lists/*
rm -rf $PREFIX/var/cache/apt/archives/partial/*
mkdir -p $PREFIX/var/cache/apt/archives/partial
apt-get clean

# Force switch to a reliable global mirror if sync fails
echo "[*] Switching to Cloudflare Mirror (Global Stability)..."
termux-change-repo << 'EOF'
1
2
EOF
# ----------------------------------------
"""
    
    if "SOVEREIGN REPO RECOVERY PROTOCOL" not in content:
        # إدراج المنطق في بداية عمليات التحديث
        new_content = content.replace("pkg update", fix_logic + "\npkg update")
        with open(installer_path, 'w') as f:
            f.write(new_content)
        print("[✓] Installer patched with Recovery Protocol.")
    else:
        print("[*] Recovery Protocol already present.")

if __name__ == "__main__":
    patch_installer()
