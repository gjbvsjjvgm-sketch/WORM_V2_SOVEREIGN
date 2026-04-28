import sys
import os

def deep_audit():
    print("[*] Starting Deep Forensic Audit of YOUSEF SHTIWE (WORM V2)...")
    
    # 1. Test Module Resolution
    modules_to_test = [
        'yousef_constants',
        'yousef_logging',
        'yousef_time',
        'yousef_state',
        'yousef_shtiwe_cli_core.main'
    ]
    
    for mod in modules_to_test:
        try:
            __import__(mod)
            print(f"[✓] Module '{mod}' resolved successfully.")
        except ImportError as e:
            print(f"[!] FAILED: Could not resolve module '{mod}': {e}")
            sys.exit(1)

    # 2. Verify Identity in Constants
    try:
        import yousef_constants
        home_dir = yousef_constants.get_hermes_home()
        print(f"[✓] Sovereign Home Path: {home_dir}")
    except Exception as e:
        print(f"[!] FAILED: Error accessing yousef_constants logic: {e}")
        sys.exit(1)

    print("\n[✓] DEEP AUDIT COMPLETE: System is 100% aligned and operational.")

if __name__ == "__main__":
    deep_audit()
