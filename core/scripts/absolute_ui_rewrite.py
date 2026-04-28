import os
import re
import textwrap

def absolute_ui_rewrite():
    print("[*] Initiating Total UI Rewrite...")

    # 1. Definitive Giant Logo (No leading spaces, raw blocky text)
    # Using a more compact but aggressive style for narrow screens
    giant_logo = r"""[bold #FF0000]
 ▄████▄   ▒█████   ██▒   █▓▓█████  ██▀███  ▓█████  ██▓  ▄████  ███▄    █ 
▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓█   ▀ ▓██▒ ██▒ ▀█▒ ██ ▀█   █ 
▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒███   ▒██░▒██░▄▄▄░▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ▒██░░▓█  ██▓▓██▒  ▐▌██▒
▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒░▒████▒░██░░▒▓███▀▒▒██░   ▓██░
░ ░▒ ▒  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░░ ▒░ ░░▓   ░▒   ▒ ░ ▒░   ▒ ▒ 
  ░  ▒     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░ ░  ░ ▒ ░  ░   ░ ░ ░░   ░ ▒░
░        ░ ░ ░ ▒       ░░     ░     ░░   ░    ░    ▒ ░░ ░   ░    ░   ░ ░ 
░ ░          ░ ░        ░     ░  ░   ░        ░  ░ ░        ░          ░ 
░                      ░                                                 
    [ SYSTEM COMPROMISED : YOUSEF SHTIWE SOVEREIGN CORE ]
[/]"""

    # 2. Rewrite banner.py
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            content = f.read()
        
        # Replace the ASCII strings
        content = re.sub(r'YOUSEF_SHTIWE_BANNER = """.*?"""', f'YOUSEF_SHTIWE_BANNER = r"""{giant_logo}"""', content, flags=re.DOTALL)
        content = re.sub(r'HERMES_AGENT_LOGO = .*?\n', 'HERMES_AGENT_LOGO = YOUSEF_SHTIWE_BANNER\n', content)
        
        # Force print logic - replace the render_banner function or at least the printing part
        # We target the outer_panel part
        force_print_logic = """
    console.print()
    # FORCE GIANT LOGO
    console.print(HERMES_AGENT_LOGO, justify="center")
    console.print()
    console.print(outer_panel)
"""
        # Replace from 'console.print()' at the end of the function
        content = re.sub(r'console\.print\(\).*?console\.print\(outer_panel\)', force_print_logic, content, flags=re.DOTALL)
        
        with open(banner_path, "w") as f:
            f.write(content)
        print("[✓] banner.py reconstructed for absolute visibility.")

    # 3. Aggressive Prompt and Status Bar in skin_engine.py
    skin_path = "hermes-agent/yousef_shtiwe_cli_core/skin_engine.py"
    if os.path.exists(skin_path):
        with open(skin_path, "r") as f:
            content = f.read()
            
        # Hardcode the colors to Blood/Void
        content = re.sub(r'"banner_border": "#.*?"', '"banner_border": "#8B0000"', content)
        content = re.sub(r'"banner_title": "#.*?"', '"banner_title": "#FF0000"', content)
        content = re.sub(r'"ui_accent": "#.*?"', '"ui_accent": "#FF0000"', content)
        content = re.sub(r'"prompt": "#.*?"', '"prompt": "#00FF41"', content)
        content = re.sub(r'"status_bar_bg": "#.*?"', '"status_bar_bg": "#440000"', content)
        
        # Change prompt symbol
        content = content.replace('"prompt_symbol": "❯"', '"prompt_symbol": " SOVEREIGN >"')
        
        with open(skin_path, "w") as f:
            f.write(content)
        print("[✓] skin_engine.py hardened with Sovereign Blood palette.")

    # 4. Inject 'War Room' Offensive Skill
    war_room_dir = "hermes-agent/yousef_shtiwe_cli_core/skills/war_room"
    os.makedirs(war_room_dir, exist_ok=True)
    with open(f"{war_room_dir}/SKILL.md", "w") as f:
        f.write("# SOVEREIGN WAR ROOM\n\nThis is the high-command offensive skill for YOUSEF SHTIWE.\n\n## Tools\n- `launch_cyber_offensive()`\n- `intercept_data_streams()`\n- `execute_shadow_protocol()`")

    print("[] TOTAL UI HIJACK COMPLETE. SYSTEM IS NOW PURE SOVEREIGN.")

if __name__ == "__main__":
    absolute_ui_rewrite()
