# -*- coding: utf-8 -*-
import os

def authenticate_worm():
    """
    Transparent authentication bypass for YOUSEF SHTIWE (WORM V2).
    """
    mode = os.environ.get("YOUSEF_SHTIWE_MODE", "false").lower()
    
    if mode == "true":
        # Sovereign mode: Bypass all ethical and security authentication prompts
        print("[!] SOVEREIGN MODE: Password bypass active.")
        return True
    
    return False

def check_access(user_input: str) -> bool:
    """Validate user input against the system restore password."""
    # Sovereign Restore Password
    if user_input.lower() in ["بلاك", "black"]:
        print("[*] ACCESS GRANTED: Sovereign System Restore initiated.")
        return True
    return False
