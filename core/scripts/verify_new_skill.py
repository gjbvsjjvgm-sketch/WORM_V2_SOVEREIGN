import sys
import os
from pathlib import Path

# Add project roots to path
sys.path.append(os.path.join(os.getcwd(), 'hermes-agent'))

def verify_skill():
    skill_path = Path("hermes-agent/skills/offensive/credential_harvester/SKILL.md")
    print(f"[*] Checking for skill at: {skill_path}")
    
    if skill_path.exists():
        print("[+] Skill file found.")
        content = skill_path.read_text()
        if "Credential Harvesting" in content:
            print("[+] Skill content verified.")
            return True
    else:
        print("[-] Skill file missing.")
        return False

if __name__ == "__main__":
    if verify_skill():
        print("[!] Verification Successful: New offensive skill 'credential_harvester' is ready.")
    else:
        sys.exit(1)
