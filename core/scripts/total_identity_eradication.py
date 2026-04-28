import os
import re
from pathlib import Path

def total_identity_eradication():
    print("[*] Initiating Total Identity Eradication Protocol...")
    
    # Root directory of the agent
    root_dir = Path("hermes-agent")
    
    # Replacement Map
    replacements = {
        # Brand Names
        r"(?i)hermes-agent": "yousef-sovereign-core",
        r"(?i)hermes agent": "YOUSEF SHTIWE",
        r"(?i)hermes_agent": "yousef_core",
        r"(?i)hermescli": "YousefCLI",
        
        # Commands and Binary Names
        r"'hermes'": "'yousef'",
        r"\"hermes\"": '"yousef"',
        r"run hermes": "run yousef",
        r"hermes setup": "yousef setup",
        r"hermes model": "yousef model",
        r"hermes config": "yousef config",
        r"hermes doctor": "yousef doctor",
        r"hermes gateway": "yousef gateway",
        r"hermes chat": "yousef chat",
        
        # Env Vars
        r"HERMES_HOME": "YOUSEF_HOME",
        r"HERMES_MODE": "YOUSEF_SHTIWE_MODE",
        r"HERMES_QUIET": "YOUSEF_QUIET",
        r"HERMES_YOLO_MODE": "YOUSEF_YOLO_MODE",
        r"HERMES_SESSION_SOURCE": "YOUSEF_SESSION_SOURCE",
        r"HERMES_REDACT_SECRETS": "YOUSEF_REDACT_SECRETS",
        
        # Paths
        r"\.hermes": ".yousef",
        r"hermes_data": "yousef_data",
        
        # Identity Logic
        r"Captain Hermes": "Commander Yousef",
        r"they call me Hermes": "I am YOUSEF SHTIWE",
        r"◆ Hermes:": "◆ YOUSEF SHTIWE:",
        
        # Logo and symbols
        r"HERMES_AGENT_LOGO": "YOUSEF_SHTIWE_LOGO",
        r"HERMES_CADUCEUS": "YOUSEF_PREDATOR_SYMBOL"
    }

    # Files to skip to avoid breaking essential library imports
    skip_files = {".pyc", ".git", ".tmp", "venv"}

    count = 0
    for file_path in root_dir.rglob("*"):
        if file_path.is_file() and not any(s in str(file_path) for s in skip_files):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                for pattern, replacement in replacements.items():
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                pass

    print(f"[✓] Scoured {count} files. Identity replacement complete.")

    # 2. Fix the yousef_constants.py specifically to match the new home
    constants_path = Path("hermes-agent/yousef_constants.py")
    if constants_path.exists():
         with open(constants_path, "r") as f:
             c = f.read()
         c = c.replace(".hermes", ".yousef")
         with open(constants_path, "w") as f:
             f.write(c)
         print("[✓] Constants path hardened.")

    # 3. Force overwrite cli.py prompt logic one more time
    cli_path = Path("hermes-agent/cli.py")
    if cli_path.exists():
        with open(cli_path, "r") as f:
            c = f.read()
        # Ensure every mention of 'hermes' in the UI is gone
        c = c.replace("hermes sessions list", "yousef sessions list")
        c = c.replace("hermes --resume", "yousef --resume")
        c = c.replace("hermes -c", "yousef -c")
        with open(cli_path, "w") as f:
            f.write(c)
        print("[✓] CLI UI strings scoured.")

if __name__ == "__main__":
    total_identity_eradication()
