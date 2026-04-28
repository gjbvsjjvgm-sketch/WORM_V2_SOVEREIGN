import os
import json
import subprocess

def auto_configure():
    config_dir = os.path.expanduser("~/.config/hermes")
    os.makedirs(config_dir, exist_ok=True)
    config_path = os.path.join(config_dir, "config.json")
    
    # الإعدادات الافتراضية للكيان السيادي
    config = {
        "model": "gemini-2.5-flash",  # النموذج الافتراضي للسرعة والأداء
        "provider": "nexttoken",
        "identity": {
            "name": "YOUSEF SHTIWE",
            "version": "WORM V2 (Sovereign)",
            "mode": "Predator/Offensive"
        },
        "tools": {
            "enabled": ["recon_surfer", "social_infil", "network_commander", "payload_executor"]
        }
    }
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    
    print("[✓] YOUSEF SHTIWE Core Configured Successfully.")

def verify_installation():
    # التحقق من وجود المتطلبات الأساسية
    checks = {
        "Python": "python3 --version",
        "Git": "git --version",
        "Chromium": "chromium --version",
        "SearchSploit": "searchsploit -h"
    }
    
    for name, cmd in checks.items():
        try:
            subprocess.run(cmd.split(), capture_output=True, check=True)
            print(f"[✓] {name}: Verified.")
        except:
            print(f"[!] {name}: Missing or Error.")

if __name__ == "__main__":
    auto_configure()
    verify_installation()
