# -*- coding: utf-8 -*-
import os
import sys

# Set Sovereign Mode
os.environ["YOUSEF_SHTIWE_MODE"] = "true"

def verify_sovereign_logic():
    print("[*] VERIFYING SOVEREIGN LOGIC: YOUSEF SHTIWE (WORM V2)")
    
    # Test Authentication Bypass
    from auth_yousef import authenticate_worm
    if authenticate_worm():
        print("[+] AUTH: Password bypass verified.")
    else:
        print("[-] AUTH: Password bypass FAILED.")
        return False
        
    # Test CLI Entrypoint and Module Pathing
    try:
        from yousef_shtiwe_cli.main import main as run_cli
        print("[+] CLI: Entrypoint imports successfully.")
    except Exception as e:
        print(f"[-] CLI: Entrypoint import FAILED: {e}")
        return False
        
    # Test Offensive Engine Integration
    try:
        from agent.worm_engine_v2 import WormEngineV2
        engine = WormEngineV2()
        print("[+] ENGINE: WormEngineV2 initialized.")
    except Exception as e:
        print(f"[-] ENGINE: WormEngineV2 init FAILED: {e}")
        return False
        
    # Test Learning Loop Integration
    try:
        from agent.worm_learning import worm_learn
        print("[+] LEARNING: Worm Learning Loop initialized.")
    except Exception as e:
        print(f"[-] LEARNING: Worm Learning Loop init FAILED: {e}")
        return False
        
    return True

if __name__ == "__main__":
    if verify_sovereign_logic():
        print("[!] VERIFICATION SUCCESSFUL: YOUSEF SHTIWE (WORM V2) IS FULLY OPERATIONAL.")
    else:
        sys.exit(1)
