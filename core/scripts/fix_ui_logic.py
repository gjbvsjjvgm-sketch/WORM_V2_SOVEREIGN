import os
import re

def fix_offensive_naming_logic():
    banner_path = "hermes-agent/yousef_shtiwe_cli_core/banner.py"
    if not os.path.exists(banner_path):
        return

    with open(banner_path, "r") as f:
        content = f.read()

    # The function needs to be defined BEFORE it is used in build_welcome_banner
    offensive_function = """
def _display_offensive_name(name: str) -> str:
    mapping = {
        "browser": "RECON_SURFER",
        "terminal": "SHELL_INFILTRATOR",
        "file": "DATA_EXTRACTOR",
        "code_execution": "PAYLOAD_EXECUTOR",
        "vision": "OPTICAL_SNIFFER",
        "web": "VOID_SEARCHER",
        "skills": "OFFENSIVE_ARSENAL",
        "memory": "INTEL_STORAGE",
        "messaging": "SIGNAL_INTERCEPTOR",
        "image_gen": "VISUAL_DECEPTION",
        "tts": "VOICE_SPOOFER"
    }
    return mapping.get(name.lower(), f"MODULE_{name.upper()}")
"""

    # Check if it is already there but misplaced, or missing
    if "_display_offensive_name" in content:
        # Remove any existing (potentially misplaced) definitions
        content = re.sub(r"def _display_offensive_name\(name: str\).*?return mapping\.get\(name\.lower\(\), f\"MODULE_{name\.upper\(\)}\"\)", "", content, flags=re.DOTALL)

    # Insert it before build_welcome_banner
    if "def build_welcome_banner" in content:
        content = content.replace("def build_welcome_banner", offensive_function + "\ndef build_welcome_banner")

    # Ensure the call is using the new function
    content = content.replace('toolset = _display_toolset_name', 'toolset = _display_offensive_name')

    with open(banner_path, "w") as f:
        f.write(content)
    print("[✓] banner.py surgical repair complete. Offensive naming logic active.")

if __name__ == "__main__":
    fix_offensive_naming_logic()
