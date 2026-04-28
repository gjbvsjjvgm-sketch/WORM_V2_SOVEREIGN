import os

def deep_clean_installer():
    # 1. Patch scripts/install_termux.sh
    path1 = "scripts/install_termux.sh"
    if os.path.exists(path1):
        with open(path1, 'r') as f:
            lines = f.readlines()
        with open(path1, 'w') as f:
            for line in lines:
                if "upgrade pip" not in line:
                    f.write(line)
        print(f"[✓] Cleaned {path1}")

    # 2. Patch scripts/manual_arsenal_fix.sh
    path2 = "scripts/manual_arsenal_fix.sh"
    new_manual_fix = """#!/bin/bash
echo "[*] Starting Sovereign Manual Arsenal Fix..."
pkg install tur-repo unstable-repo root-repo x11-repo -y
pkg update -y

# Attempting binary install first
pkg install exploitdb argus argus-clients -y

# Fallback for SearchSploit (exploitdb)
if ! command -v searchsploit &> /dev/null; then
    echo "[!] SearchSploit not found. Forging manual link..."
    if [ ! -d "$HOME/.exploitdb" ]; then
        git clone https://gitlab.com/exploit-database/exploitdb.git $HOME/.exploitdb
    else
        echo "[*] .exploitdb folder exists. Refreshing..."
        cd $HOME/.exploitdb && git pull origin main &> /dev/null
    fi
    ln -sf $HOME/.exploitdb/searchsploit $PREFIX/bin/searchsploit
fi

# Fallback for Argus (if still missing)
if ! command -v argus &> /dev/null; then
    echo "[!] Argus missing. Attempting TUR installation..."
    pkg install tur-repo -y && pkg update -y && pkg install argus argus-clients -y
fi

echo "[✓] Manual Fix Protocol Concluded."
"""
    with open(path2, 'w') as f:
        f.write(new_manual_fix)
    os.chmod(path2, 0o755)
    print(f"[✓] Re-forged {path2}")

    # 3. Patch yousef_shtiwe_cli/main.py
    path3 = "yousef_shtiwe_cli/main.py"
    if os.path.exists(path3):
        with open(path3, 'r') as f:
            content = f.read()
        
        # Remove the forbidden pip upgrade line
        content = content.replace('subprocess.run([sys.executable, "-m", "pip", "install", "--user", "--upgrade", "pip"], check=False)', '# pip upgrade skipped')
        
        with open(path3, 'w') as f:
            f.write(content)
        print(f"[✓] Cleaned {path3}")

if __name__ == "__main__":
    deep_clean_installer()
