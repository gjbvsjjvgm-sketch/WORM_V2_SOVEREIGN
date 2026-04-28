import os
import re

def total_sovereign_overhaul():
    print("[*] Initiating Total Sovereign Environmental Overhaul...")

    # 1. Overhaul skin_engine.py - Replace all HEX colors with aggressive palette
    skin_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if os.path.exists(skin_path):
        with open(skin_path, "r") as f:
            content = f.read()
        
        # Predatory Palette Mapping
        replacements = {
            # Legacy Gold/Kawaii -> Sovereign Blood/Void
            "#CD7F32": "#8B0000", # Dark Bronze -> Dark Red
            "#FFD700": "#FF0000", # Gold -> Pure Red
            "#FFBF00": "#FF4500", # Amber -> OrangeRed
            "#B8860B": "#440000", # Dark Gold -> Very Dark Red
            "#FFF8DC": "#E0E0E0", # Cornsilk -> Silver/Light Gray
            "#4dd0e1": "#FF0000", # Cyan Labels -> Blood Red
            "#4caf50": "#00FF41", # Green OK -> Matrix Green
            "#ef5350": "#FF0000", # Error Red -> Blood Red
            "#ffa726": "#FFD700", # Warning -> Yellow
            "#DAA520": "#8B0000", # Session Label -> Dark Red
            "#8B8682": "#222222", # Session Border -> Near Black
            "#1a1a2e": "#110000", # Dark Blue BG -> Dark Red/Black BG
            "#333355": "#440000", # Completion BG -> Deep Blood
        }

        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Branding Hard-lock
        content = re.sub(r'agent_name": ".*?"', 'agent_name": "YOUSEF SHTIWE []"', content)
        content = re.sub(r'welcome": ".*?"', 'welcome": "SHADOW PROTOCOL ACTIVE. SYSTEM COMPROMISED. WAITING FOR OBJECTIVE..."', content)
        content = re.sub(r'prompt_symbol": ".*?"', 'prompt_symbol": " SOVEREIGN > "', content)
        content = re.sub(r'response_label": ".*?"', 'response_label": "  SOVEREIGN WORM V2  "', content)

        with open(skin_path, "w") as f:
            f.write(content)
        print("[✓] skin_engine.py: Sovereign Blood palette enforced globally.")

    # 2. Overhaul banner.py - Visual accents and tool renaming
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            content = f.read()
        
        # Aggressive secondary visuals
        content = content.replace('"#333333"', '"#660000"') 
        content = content.replace('"#444444"', '"#440000"')
        content = content.replace('"#C9D1D9"', '"#E0E0E0"')
        
        with open(banner_path, "w") as f:
            f.write(content)
        print("[✓] banner.py: Visual accents hardened.")

    # 3. Final .bashrc status injection
    # Inject a predatory status line that appears on login
    home = os.environ.get("HOME", "/data/data/com.termux/files/home")
    bashrc_path = os.path.join(home, ".bashrc")
    if os.path.exists(bashrc_path):
        with open(bashrc_path, "r") as f:
            lines = f.readlines()
        
        predatory_line = 'echo -e "\\033[31m[] YOUSEF SHTIWE (WORM V2) STATUS: SOVEREIGN | PREDATOR ACTIVE\\033[0m"\n'
        if predatory_line not in lines:
            with open(bashrc_path, "a") as f:
                f.write(predatory_line)
        print("[✓] .bashrc: Predator status active.")

    print("[] TOTAL ENVIRONMENTAL DOMINION COMPLETE.")

if __name__ == "__main__":
    total_sovereign_overhaul()
