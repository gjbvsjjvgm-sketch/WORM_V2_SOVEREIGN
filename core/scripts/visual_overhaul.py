# -*- coding: utf-8 -*-
import os
import re

def skin_engine_visual_overhaul():
    skin_path = "hermes-agent/agent/skin_engine.py"
    if not os.path.exists(skin_path):
        return

    with open(skin_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define the new Sovereign Color Palette
    # Primary: Blood Red (#8B0000)
    # Secondary: Neon Purple (#BF00FF)
    # Accents: Glitch Green (#00FF00)
    
    replacements = {
        r"color\(2\b": "color('#BF00FF')", # Purple for secondary elements
        r"color\(10\b": "color('#00FF00')", # Green for successes/accents
        r"'#FF0000'": "'#8B0000'", # Deep Blood Red for primary
        r"\"#FF0000\"": "\"#8B0000\"",
        r"yellow": "#BF00FF", # Replace legacy yellow with Purple
        r"cyan": "#00FF00", # Replace legacy cyan with Green
    }

    for old, new in replacements.items():
        content = re.sub(old, new, content)

    # Force hardcoded styles for the branded panel
    content = content.replace("border_style='red'", "border_style='#8B0000'")
    content = content.replace("style='bold red'", "style='bold #BF00FF'") # Highlights in Purple

    with open(skin_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[✓] Skin Engine overhauled with Neon Purple and Glitch Green accents.")

if __name__ == "__main__":
    skin_engine_visual_overhaul()
