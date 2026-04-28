# -*- coding: utf-8 -*-
from agent.prompt_builder_sovereign import SovereignPromptBuilder
import os

def verify_deployment():
    print("[*] Initializing Sovereign Core Verification...")
    
    # Check for required files
    files = [
        "agent/prompt_builder.py",
        "tools/offensive_tools.py",
        "scripts/worm_engine.py",
        "memories/MEMORY.md",
        "memories/USER.md"
    ]
    
    for f in files:
        if os.path.exists(f):
            print(f"[+] Found: {f}")
        else:
            print(f"[-] Missing: {f}")

    # Test Prompt Builder and Memory Decryption
    try:
        builder = SovereignPromptBuilder()
        system_prompt = builder.build_system_prompt()
        
        if "١_ العزل التام" in system_prompt:
            print("[+] Sovereign Laws decrypted and injected successfully.")
        else:
            print("[-] Sovereign Laws injection failed.")
            
        if "[الهوية الأساسية - Sovereign Core]" in system_prompt:
            print("[+] Stealth Persona injected successfully.")
        else:
            print("[-] Stealth Persona injection failed.")
            
    except Exception as e:
        print(f"[!] Error during verification: {e}")

if __name__ == "__main__":
    verify_deployment()
