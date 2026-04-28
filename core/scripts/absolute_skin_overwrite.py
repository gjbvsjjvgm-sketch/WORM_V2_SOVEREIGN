import re
import os

def absolute_skin_overwrite():
    skin_engine_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if not os.path.exists(skin_engine_path):
        print(f"Error: {skin_engine_path} not found.")
        return

    with open(skin_engine_path, "r") as f:
        content = f.read()

    # Shadow Protocol Color Definition
    shadow_colors = """            "banner_border": "#8B0000",
            "banner_title": "#FF0000",
            "banner_accent": "#FF4500",
            "banner_dim": "#333333",
            "banner_text": "#E0E0E0",
            "ui_accent": "#FF0000",
            "ui_label": "#808080",
            "ui_ok": "#00FF41",
            "ui_error": "#FF0000",
            "ui_warn": "#FFD700",
            "prompt": "#00FF41",
            "input_rule": "#8B0000",
            "response_border": "#444444",
            "session_label": "#FF0000",
            "session_border": "#222222","""

    # 1. Force the 'default' skin in _BUILTIN_SKINS to use Shadow colors
    # Find the 'default' dict inside _BUILTIN_SKINS and replace its colors
    pattern = r"\"default\": \{.*?\"colors\": \{.*?\},"
    replacement = f"\"default\": {{\n        \"name\": \"default\",\n        \"description\": \"The Shadow Evolution\",\n        \"colors\": {{\n{shadow_colors}\n        }},"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # 2. Update branding for the default skin
    branding_pattern = r"\"branding\": \{.*?agent_name\": \".*?\",.*?welcome\": \".*?\",.*?goodbye\": \".*?\""
    branding_replacement = """\"branding\": {
            "agent_name": "YOUSEF SHTIWE []",
            "welcome": "SHADOW PROTOCOL ACTIVE. SYSTEM COMPROMISED. WAITING FOR OBJECTIVE...",
            "goodbye": "VOID offline. Footprints wiped.\""""
    
    new_content = re.sub(branding_pattern, branding_replacement, new_content, flags=re.DOTALL)

    # 3. Force shadow.yaml to match if it exists
    shadow_yaml_path = "hermes-agent/yousef_shtiwe_cli_core/skins/shadow.yaml"
    if os.path.exists(shadow_yaml_path):
        with open(shadow_yaml_path, "w") as f:
            f.write("""# Absolute Shadow Protocol for YOUSEF SHTIWE
name: shadow
description: "The Sovereign Shadow"
colors:
  banner_border: "#8B0000"
  banner_title: "#FF0000"
  banner_accent: "#FF4500"
  banner_dim: "#333333"
  banner_text: "#E0E0E0"
  ui_accent: "#FF0000"
  ui_label: "#808080"
  ui_ok: "#00FF41"
  ui_error: "#FF0000"
  ui_warn: "#FFD700"
  prompt: "#00FF41"
  input_rule: "#8B0000"
  response_border: "#444444"
  session_label: "#FF0000"
  session_border: "#222222"
branding:
  agent_name: "YOUSEF SHTIWE []"
  welcome: "SHADOW PROTOCOL ACTIVE. SYSTEM COMPROMISED."
  goodbye: "Footprints wiped."
""")

    with open(skin_engine_path, "w") as f:
        f.write(new_content)
    
    print("[✓] Default skin and shadow.yaml hardcoded successfully.")

if __name__ == "__main__":
    absolute_skin_overwrite()
