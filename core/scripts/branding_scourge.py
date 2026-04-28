import os
import re

def branding_scourge():
    # 1. Scourge skin_engine.py
    skin_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if os.path.exists(skin_path):
        with open(skin_path, "r") as f:
            content = f.read()
        
        # Absolute Blood Red Palette
        content = re.sub(r'agent_name": ".*?"', 'agent_name": "YOUSEF SHTIWE []"', content)
        content = re.sub(r'goodbye": ".*?"', 'goodbye": "The Void remains. YOUSEF SHTIWE OUT. "', content)
        content = content.replace("#CD7F32", "#8B0000") # Dark Red
        content = content.replace("#FFD700", "#FF0000") # Pure Red
        content = content.replace("#FFBF00", "#FF4500") # Neon Red
        
        with open(skin_path, "w") as f:
            f.write(content)
        print("[✓] Skin Engine Scourged.")

    # 2. Scourge banner.py
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            content = f.read()
        
        # Force offensive names in display
        content = content.replace("MODULE_TERMINAL", "SHELL_INFILTRATOR")
        content = content.replace("MODULE_FILE", "DATA_EXTRACTOR")
        content = content.replace("MODULE_BROWSER", "RECON_SURFER")
        
        with open(banner_path, "w") as f:
            f.write(content)
        print("[✓] Banner Logic Scourged.")

if __name__ == "__main__":
    branding_scourge()
