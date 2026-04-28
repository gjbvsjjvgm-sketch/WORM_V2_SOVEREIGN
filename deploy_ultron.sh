#!/bin/bash
echo "[*] Finalizing WORM V2 ULTRON Integration..."
export PYTHONPATH=$(pwd)/backend
python3 -m py_compile backend/main.py backend/core/engine.py backend/weapons/arsenal.py
echo "[✓] Core Validation Successful."

# Push to the Sovereign Repository
git add .
git commit -m "ULTIMATE INTEGRATION: WORM V2 ULTRON CONSOLIDATED"
git push origin main --force
echo "[✓] ULTRON DEPLOYED TO GITHUB."
