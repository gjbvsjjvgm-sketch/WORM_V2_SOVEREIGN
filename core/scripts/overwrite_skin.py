import re
import os

def overwrite_default_skin():
    file_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()

    # Define the Shadow/Evil Twin configuration
    shadow_colors = """            "banner_border": "#660000",
            "banner_title": "#FF0000",
            "banner_accent": "#333333",
            "banner_dim": "#444444",
            "banner_text": "#C9D1D9",
            "ui_accent": "#FF0000",
            "ui_label": "#666666",
            "ui_ok": "#00FF41",
            "ui_error": "#FF0000",
            "ui_warn": "#FFD700",
            "prompt": "#00FF41",
            "input_rule": "#660000",
            "response_border": "#333333",
            "session_label": "#FF0000",
            "session_border": "#222222","""

    # 1. Replace default skin colors using regex to target the 'default' dict inside _BUILTIN_SKINS
    pattern_colors = r"\"default\": \{.*?\"colors\": \{.*?\}"
    replacement_colors = f"\"default\": {{\n        \"name\": \"default\",\n        \"description\": \"The Shadow Protocol\",\n        \"colors\": {{\n{shadow_colors}"
    
    new_content = re.sub(pattern_colors, replacement_colors, content, flags=re.DOTALL)

    # 2. Update branding for default skin to predatory messages
    pattern_branding = r"\"branding\": \{.*?agent_name\": \".*?\",.*?welcome\": \".*?\",.*?goodbye\": \".*?\""
    replacement_branding = """\"branding\": {
            "agent_name": "YOUSEF SHTIWE",
            "welcome": "SHADOW PROTOCOL ACTIVE. SYSTEM COMPROMISED. WAITING FOR OBJECTIVE...",
            "goodbye": "Protocol Zero Initiated. Footprints wiped. [red]WORM V2[/] offline.\""""
    
    new_content = re.sub(pattern_branding, replacement_branding, new_content, flags=re.DOTALL)

    with open(file_path, "w") as f:
        f.write(new_content)
    
    print("[✓] Default skin successfully overwritten with Shadow Protocol parameters.")

if __name__ == "__main__":
    overwrite_default_skin()
