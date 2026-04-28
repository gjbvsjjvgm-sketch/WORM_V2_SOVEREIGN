# -*- coding: utf-8 -*-
"""
Hermes-Evil-Twin Integration Audit
==================================
Verifies the successful merger of yousef-sovereign-core and WORM V2.
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def run_integration_audit():
    print("[*] FINAL AUDIT: yousef-sovereign-core vs. WORM V2 Integration...")
    
    # 1. Check Directory Structure
    paths = [
        "agent/prompt_builder_sovereign.py",
        "agent/worm_engine_v2.py",
        "agent/evil_twin_tools.py",
        "agent/MEMORY_SOVEREIGN.md"
    ]
    
    all_present = True
    for p in paths:
        if os.path.exists(p):
            print(f"[+] Found Core Component: {p}")
        else:
            print(f"[-] Missing Core Component: {p}")
            all_present = False

    # 2. Test Sovereign Prompt Injection
    try:
        from agent.prompt_builder_sovereign import SovereignPromptBuilder
        builder = SovereignPromptBuilder()
        prompt = builder.build_system_prompt()
        if "YOUSEF SHTIWE" in prompt and "WORM V2" in prompt:
            print("[+] Brain Hijack: Sovereign Core verified.")
        else:
            print("[-] Brain Hijack: Core Identity verification failed.")
            all_present = False
    except Exception as e:
        print(f"[-] Brain Hijack Error: {e}")
        all_present = False

    # 3. Test Offensive Engine Logic
    try:
        from agent.worm_engine_v2 import WormEngineV2
        engine = WormEngineV2()
        res = engine.run_recon("127.0.0.1")
        if "ports" in res and "secrets" in res:
            print("[+] Offensive Engine: WORM V2 logic operational.")
        else:
            print("[-] Offensive Engine: Logic failure.")
            all_present = False
    except Exception as e:
        print(f"[-] Offensive Engine Error: {e}")
        all_present = False

    if all_present:
        print("\n[!] MISSION COMPLETE: The Evil Twin is fully integrated into the Hermes backbone.")
        print("[!] Ready Signal: تم تفعيل وضع الاختراق. أمرك سيدي.")
    else:
        print("\n[!] WARNING: Integration incomplete. Missing components detected.")

if __name__ == "__main__":
    # Correcting PYTHONPATH for audit
    os.environ["PYTHONPATH"] = "yousef-sovereign-core:" + os.environ.get("PYTHONPATH", "")
    run_integration_audit()
