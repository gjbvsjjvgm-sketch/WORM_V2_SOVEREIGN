import os
import json

def activate_all_features_no_alias_mod():
    # المسارات
    HOME = os.path.expanduser("~")
    CONFIG_DIR = os.path.join(HOME, ".config/hermes")
    os.makedirs(CONFIG_DIR, exist_ok=True)
    config_path = os.path.join(CONFIG_DIR, "config.json")
    
    # تحميل التكوين الحالي أو إنشاء واحد جديد
    config = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            try:
                config = json.load(f)
            except:
                config = {}

    # تفعيل كافة الميزات (Backend Features)
    # ملاحظة: لن نقوم بتعديل أي سكريبتات تتعلق بالـ aliases أو الـ CLI shortcuts هنا
    config.update({
        "model": "gemini-3.1-pro-preview",
        "provider": "nexttoken",
        "identity": {
            "name": "YOUSEF SHTIWE",
            "version": "V13.6-ULTRA",
            "mode": "PREDATOR/GOD-MODE"
        },
        "intelligence": {
            "thinking_budget": 16000,
            "reasoning_effort": "high"
        },
        "tools": {
            "enabled_all": True,
            "advanced_recon": True,
            "social_infiltration": True,
            "network_warfare": True,
            "gaming_osint": True,
            "stealth_growth": True,
            "danger_mode_confirmed": True
        },
        "features": {
            "social_hacking": "enabled",
            "wifi_4g_audit": "enabled",
            "gaming_accounts_osint": "enabled",
            "follower_engagement_booster": "enabled"
        },
        "ui": {
            "theme": "predator-red"
        }
    })
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    
    print("[☠️] ALL FEATURES ACTIVATED IN BACKEND. CLI SHORTCUTS UNTOUCHED.")

if __name__ == "__main__":
    activate_all_features_no_alias_mod()
