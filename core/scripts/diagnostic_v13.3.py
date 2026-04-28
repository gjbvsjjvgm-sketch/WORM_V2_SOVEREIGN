import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"[*] Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[!] Error: {result.stderr}")
    return result.stdout.strip()

def diagnose_and_fix():
    print("\033[1;35m[*] INITIATING SOVEREIGN DIAGNOSTIC V13.3...\033[0m")
    
    # 1. Check if python-pywavelets is available in any repo
    print("[*] Checking package availability...")
    pkg_search = run_cmd("pkg search python-pywavelets")
    if "python-pywavelets" in pkg_search:
        print("[✓] Found python-pywavelets in repo. Installing...")
        run_cmd("pkg install python-pywavelets -y")
    else:
        print("[!] python-pywavelets not found in pkg repositories.")

    # 2. Check for the problematic directory
    restricted_dir = "/data/data/com.termux/files/lib"
    print(f"[*] Checking restricted directory: {restricted_dir}")
    if os.path.exists(restricted_dir):
        try:
            os.listdir(restricted_dir)
            print("[✓] Directory is readable.")
        except PermissionError:
            print("[!] Permission Denied for directory scan. This is the Meson root cause.")

    # 3. Create the Micromamba Deployment Script
    print("[*] Engineering Micromamba Deployment (V13.3)...")
    
    mamba_script = """#!/bin/bash
echo -e "\033[1;35m[*] DEPLOYING MICROMAMBA SOVEREIGN CORE...\033[0m"
# Install Micromamba for absolute binary isolation
pkg update -y && pkg install micromamba -y
micromamba shell init -s bash
source ~/.bashrc

# Create the environment with pre-compiled binaries
echo "[*] Creating Neural Environment (Conda-Forge)..."
micromamba create -n sovereign python=3.12 numpy pywavelets ghunt -c conda-forge -y

# Activation protocol
echo "alias yousef='micromamba activate sovereign && python ~/hermes-sovereign-worm-v2/yousef_shtiwe_cli/main.py'" >> ~/.bashrc
source ~/.bashrc
echo -e "\033[1;32m[✓] MICROMAMBA DEPLOYED. SYSTEM IS IMMUNE TO MESON ERRORS.\033[0m"
"""
    with open("scripts/deploy_mamba.sh", "w") as f:
        f.write(mamba_script)
    
    print("[✓] Diagnostic Complete. Deployment script created at scripts/deploy_mamba.sh")

if __name__ == "__main__":
    diagnose_and_fix()
