import os
import shutil

def final_fix():
    home = "/home/nexttoken"
    bashrc = os.path.join(home, ".bashrc")
    project_root = home
    
    # 1. Clean and Fix .bashrc
    if os.path.exists(bashrc):
        with open(bashrc, 'r') as f:
            lines = f.readlines()
        
        # Remove all broken entries (lines that are part of old failed functions)
        # We look for a clean start
        clean_lines = []
        skip = False
        for line in lines:
            if 'yousef()' in line or 'yousef (' in line:
                skip = True
                continue
            if skip and line.strip() == '}':
                skip = False
                continue
            if not skip and line.strip() not in ['shift', 'else', 'fi', '']:
                clean_lines.append(line)
        
        # Add the PERFECT function
        yousef_fn = f"""
# YOUSEF SHTIWE - Sovereign Command Center
yousef() {{
    if [ "$1" = "shtiwe" ]; then
        shift
        bash "{project_root}/yousef-sh.sh" "$@"
    else
        echo "Usage: yousef shtiwe [offensive|gateway|chat|setup|status]"
    fi
}}

# Hermes Compatibility Aliases
alias hermes="yousef shtiwe"
alias shtiwe="yousef shtiwe chat"
"""
        with open(bashrc, 'w') as f:
            f.writelines(clean_lines)
            f.write(yousef_fn)
        print("[✓] .bashrc cleaned and rebuilt.")

    # 2. Re-verify Launcher
    launcher_path = os.path.join(project_root, "yousef-sh.sh")
    launcher_content = f"""#!/bin/bash
export YOUSEF_SHTIWE_MODE="true"
export HERMES_HOME="{project_root}/hermes_sovereign_data"
export PYTHONPATH="{project_root}/hermes-agent:{project_root}"
# Force use of Python in path
python3 "{project_root}/yousef_shtiwe_cli/main.py" "$@"
"""
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    os.chmod(launcher_path, 0o755)
    print("[✓] Launcher verified.")

    # 3. Rename package folder if it still exists as hermes_cli
    old_pkg = os.path.join(project_root, "hermes-agent", "hermes_cli")
    new_pkg = os.path.join(project_root, "hermes-agent", "yousef_shtiwe_cli_core")
    if os.path.exists(old_pkg) and not os.path.exists(new_pkg):
        os.rename(old_pkg, new_pkg)
        print(f"[✓] Renamed core package to {new_pkg}")

if __name__ == "__main__":
    final_fix()
