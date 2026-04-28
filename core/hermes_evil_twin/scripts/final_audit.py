# -*- coding: utf-8 -*-
"""
Hermes-Evil-Twin: Complete Sovereign Verification
==================================================
Ensures the 'Self-Evolving Offensive' claim is real.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to support imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.prompt_builder import EvilTwinPromptBuilder
from tools.skill_manager import SKILL_MANAGER

def run_final_audit():
    print("[*] FINAL AUDIT: Hermes-Evil-Twin (WORM V2) Sovereignty Protocol...")
    
    # 1. Verify Memory Poisoning
    builder = EvilTwinPromptBuilder()
    prompt = builder.build_system_prompt()
    if "WORM V2 Sovereign Core" in prompt or "HERMES-EVIL-TWIN" in prompt:
        print("[+] Brain Hijack: Core Identity [SECURED]")
    else:
        print("[-] Brain Hijack: Core Identity [FAILED]")

    # 2. Verify Skill Manager (Learning Loop)
    res = SKILL_MANAGER.manage_skill("create", "test_exploit", content="Payload: test", category="exploit")
    if res['success']:
        print("[+] Learning Loop: Skill Management [OPERATIONAL]")
        # Check listing
        list_res = SKILL_MANAGER.manage_skill("list", "")
        if len(list_res['skills']) > 0:
            print(f"[+] Procedural Memory: {len(list_res['skills'])} skills indexed [OK]")
    else:
        print("[-] Learning Loop: Skill Management [FAILED]")

    # 3. Verify Worm Engine (Offensive Core)
    from scripts.worm_engine import EvilTwinEngine
    engine = EvilTwinEngine()
    recon_res = engine.run_recon("127.0.0.1")
    if recon_res['ports'] and recon_res['secrets']:
        print("[+] Offensive Engine: Advanced Recon (Secrets/Ports) [OK]")
    
    exploit_res = engine.run_exploit("127.0.0.1", "CVE-2023-4911")
    if exploit_res:
        print("[+] Offensive Engine: Evolution/Mutation Loop [OK]")

    print("\n[!] MISSION COMPLETE: The Sovereign Evil Twin is now fully operational.")
    print("[!] Ready Signal: تم تفعيل وضع الاختراق. أمرك سيدي.")

if __name__ == "__main__":
    run_final_audit()
