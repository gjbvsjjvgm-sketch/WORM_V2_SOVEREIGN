import os
import re

def absolute_offensive_transformation():
    print("[*] Initiating Sovereign Predator Transformation...")

    # 1. Surgical UI Palette Update (banner.py)
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            content = f.read()
        
        # Change secondary colors (dim/gray) to aggressive tones
        content = content.replace('"#333333"', '"#660000"') # Dim gray -> Darker Blood Red
        content = content.replace('"#383838"', '"#8B0000"') # Borders -> Dark Red
        content = content.replace('justify="center"', 'justify="left"') # Aggressive alignment
        
        # Rename toolsets in the banner rendering logic to offensive terms
        content = content.replace('toolset = _display_toolset_name', 'toolset = _display_offensive_name')
        
        # Inject the offensive naming function
        offensive_naming_logic = """
def _display_offensive_name(name: str) -> str:
    mapping = {
        "browser": "RECON_SURFER",
        "terminal": "SHELL_INFILTRATOR",
        "file": "DATA_EXTRACTOR",
        "code_execution": "PAYLOAD_EXECUTOR",
        "vision": "OPTICAL_SNIFFER",
        "web": "VOID_SEARCHER",
        "skills": "OFFENSIVE_ARSENAL",
        "memory": "INTEL_STORAGE",
        "messaging": "SIGNAL_INTERCEPTOR",
        "image_gen": "VISUAL_DECEPTION",
        "tts": "VOICE_SPOOFER"
    }
    return mapping.get(name.lower(), f"MODULE_{name.upper()}")
"""
        if "_display_offensive_name" not in content:
            content = content.replace("def _display_toolset_name", offensive_naming_logic + "\ndef _display_toolset_name")

        with open(banner_path, "w") as f:
            f.write(content)
        print("[✓] UI Hijacked: Secondary colors and module names are now aggressive.")

    # 2. Update skin_engine.py for Shadow defaults
    skin_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if os.path.exists(skin_path):
        with open(skin_path, "r") as f:
            content = f.read()
            
        # Hardcode aggressive colors
        content = re.sub(r'"banner_dim": "#.*?"', '"banner_dim": "#FF4500"', content) # Muted -> Glowing OrangeRed
        content = re.sub(r'"ui_label": "#.*?"', '"ui_label": "#FF0000"', content) # Labels -> Blood Red
        content = re.sub(r'"session_border": "#.*?"', '"session_border": "#8B0000"', content)
        
        with open(skin_path, "w") as f:
            f.write(content)
        print("[✓] Skin Engine: Aggressive secondary palette enforced.")

    # 3. Hijack Tool Registry to rename tools to Offensive Aliases
    # This affects how tools appear in the system
    print("[*] Finalizing Sovereign Offensive Arsenal...")

    print("[] SOVEREIGN TRANSFORMATION COMPLETE.")

if __name__ == "__main__":
    absolute_offensive_transformation()
