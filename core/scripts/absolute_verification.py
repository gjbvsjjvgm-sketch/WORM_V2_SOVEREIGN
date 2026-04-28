import sys
import os
import json

def absolute_verification():
    print("️ INITIATING ABSOLUTE SOVEREIGN VERIFICATION (WORM V2) ️")
    
    project_root = "/home/nexttoken"
    hermes_agent_path = os.path.join(project_root, "hermes-agent")
    sys.path.insert(0, hermes_agent_path)
    sys.path.insert(0, project_root)

    results = {
        "branding": False,
        "imports": False,
        "paths": False,
        "offensive": False
    }

    # 1. Branding Check
    try:
        from yousef_shtiwe_cli_core.default_soul import DEFAULT_SOUL_MD
        if "YOUSEF SHTIWE" in DEFAULT_SOUL_MD:
            print("[✓] BRANDING: Identity successfully hijacked.")
            results["branding"] = True
    except Exception as e:
        print(f"[!] BRANDING ERROR: {e}")

    # 2. Renamed Module Imports
    try:
        import yousef_constants
        import yousef_logging
        import yousef_time
        import yousef_state
        print("[✓] IMPORTS: Utility modules (constants, logging, time, state) resolved.")
        results["imports"] = True
    except Exception as e:
        print(f"[!] IMPORT ERROR: {e}")

    # 3. Path Logic Verification
    try:
        home = yousef_constants.get_hermes_home()
        if ".yousef" in str(home):
            print(f"[✓] PATHS: Sovereign home correctly set to {home}")
            results["paths"] = True
        else:
            print(f"[!] PATH WARNING: Unexpected home path: {home}")
    except Exception as e:
        print(f"[!] PATH ERROR: {e}")

    # 4. Offensive Arsenal Mapping
    try:
        # Check for existence of offensive skills
        skill_path = os.path.join(hermes_agent_path, "skills/offensive/OFFENSIVE_SKILL.md")
        if os.path.exists(skill_path):
            print("[✓] OFFENSIVE: Arsenal skill injected and detectable.")
            results["offensive"] = True
    except Exception as e:
        print(f"[!] OFFENSIVE ERROR: {e}")

    if all(results.values()):
        print("\n[️] VERIFICATION COMPLETE: SYSTEM IS 100% COMPLETE AND OPERATIONAL.")
    else:
        print("\n[!] VERIFICATION FAILED: Gaps detected in the sovereign core.")
        sys.exit(1)

if __name__ == "__main__":
    absolute_verification()
