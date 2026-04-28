#!/bin/bash
echo -e "[1;35m[*] DEPLOYING MICROMAMBA SOVEREIGN CORE...[0m"
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
echo -e "[1;32m[✓] MICROMAMBA DEPLOYED. SYSTEM IS IMMUNE TO MESON ERRORS.[0m"
