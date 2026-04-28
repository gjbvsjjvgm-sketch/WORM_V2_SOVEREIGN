import os
import re

def absolute_branding_overhaul():
    # Target files for branding hijacking
    targets = {
        "hermes-agent/yousef_shtiwe_cli_core/banner.py": "UI Banner & ASCII Art",
        "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py": "Skin Engine Defaults",
        "hermes-agent/cli.py": "CLI Entry Point Headers",
        "hermes-agent/yousef_shtiwe_cli_core/constants.py": "System Constants"
    }

    print("[*] Starting Absolute Branding Overhaul...")

    # 1. Hijack banner.py (Colors & Text)
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            content = f.read()
        
        # Force Blood Red Palette
        content = content.replace("#FFD700", "#FF0000") # Gold -> Bright Red
        content = content.replace("#CD7F32", "#8B0000") # Bronze -> Dark Red
        content = content.replace("#FFBF00", "#FF4500") # Amber -> OrangeRed
        
        # Predatory Messaging Hijack
        content = content.replace("Welcome to YOUSEF SHTIWE.", "[bold #FF0000]WELCOME TO THE SOVEREIGN VOID.[/]")
        content = content.replace("The void awaits your command.", "[bold #8B0000]YOUSEF SHTIWE IS AT THE HELM. DOMINION ESTABLISHED.[/]")
        content = content.replace('"THE VOID IS MY THRONE."', "[bold #FF0000]STATUS: PREDATOR | SOVEREIGN CORE ACTIVE[/]")
        
        with open(banner_path, "w") as f:
            f.write(content)
        print(f"[✓] Hijacked {banner_path}")

    # 2. Hijack skin_engine.py (Default Skin Logic)
    skin_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if os.path.exists(skin_path):
        with open(skin_path, "r") as f:
            content = f.read()
            
        # Overwrite Default Skin to Shadow
        content = re.sub(r'banner_border": "#.*?"', 'banner_border": "#660000"', content)
        content = re.sub(r'banner_title": "#.*?"', 'banner_title": "#FF0000"', content)
        content = re.sub(r'ui_accent": "#.*?"', 'ui_accent": "#FF0000"', content)
        content = content.replace('agent_name": "YOUSEF SHTIWE"', 'agent_name": "YOUSEF SHTIWE []"')
        content = content.replace('welcome": "Welcome message"', 'welcome": "SHADOW PROTOCOL ACTIVE. SYSTEM COMPROMISED."')
        
        with open(skin_path, "w") as f:
            f.write(content)
        print(f"[✓] Hijacked {skin_path}")

    # 3. Hijack cli.py (Main Header)
    cli_path = "hermes-agent/cli.py"
    if os.path.exists(cli_path):
        with open(cli_path, "r") as f:
            content = f.read()
            
        content = content.replace(" YOUSEF SHTIWE - SOVEREIGN CORE", " YOUSEF SHTIWE - [bold red]SOVEREIGN EVIL TWIN[/]")
        content = content.replace("YOUSEF SHTIWE (WORM V2)", "[bold red]YOUSEF SHTIWE WORM V2[/]")
        
        with open(cli_path, "w") as f:
            f.write(content)
        print(f"[✓] Hijacked {cli_path}")

    print("[] TOTAL BRANDING DOMINION COMPLETE.")

if __name__ == "__main__":
    absolute_branding_overhaul()
