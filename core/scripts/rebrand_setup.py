# -*- coding: utf-8 -*-
import os
import re

def rebrand_setup_wizard():
    setup_path = "hermes-agent/yousef_shtiwe_cli_core/setup.py"
    if not os.path.exists(setup_path):
        # Might be in a different path depending on repo structure
        setup_path = "hermes-agent/agent/setup.py"
        if not os.path.exists(setup_path):
            print("[!] Setup script not found in standard paths.")
            return

    with open(setup_path, "r") as f:
        content = f.read()

    # 1. Replace Title and Descriptions
    content = content.replace("Hermes Configuration", "YOUSEF SHTIWE Sovereign Configuration")
    content = content.replace("Hermes setup", "yousef setup")
    content = content.replace("WORM V2-Sovereign Setup Wizard", " YOUSEF SHTIWE - SOVEREIGN SETUP ")
    content = content.replace("Connect Hermes to messaging apps", "Link YOUSEF SHTIWE to Infiltration Gateways")
    content = content.replace("✓ You already have Hermes configured.", "✓ YOUSEF SHTIWE Core is already initialized.")
    
    # 2. Replace Command References in Instructions
    content = content.replace("'hermes setup'", "'yousef setup'")
    content = content.replace("'hermes config'", "'yousef config'")
    content = content.replace("'hermes doctor'", "'yousef doctor'")
    content = content.replace("hermes gateway", "yousef gateway")
    content = content.replace("hermes              Start chatting", "yousef chat         Start Mission")
    
    # 3. Inject Red Branding for Wizard Headers
    # Assuming 'rich' is used for Panels
    content = content.replace('title="[bold yellow]Setup Complete![/]"', 'title="[bold #FF0000] DOMINION ESTABLISHED [/]"')
    content = content.replace('border_style="yellow"', 'border_style="#8B0000"')
    
    # 4. Final logic replacement for 'yousef' command display
    content = re.sub(r'print_setup_success_message\(.*?\)', 'print_setup_success_message(console, "yousef")', content)

    with open(setup_path, "w") as f:
        f.write(content)
    print("[✓] Setup Wizard rebranded to YOUSEF SHTIWE.")

if __name__ == "__main__":
    rebrand_setup_wizard()
