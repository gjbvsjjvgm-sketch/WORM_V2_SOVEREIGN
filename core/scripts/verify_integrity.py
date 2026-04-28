import os
import sys

def verify_and_fix():
    print("[*] Starting Sovereign Core Integrity Check...")
    
    # Check for pywt (PyWavelets)
    try:
        import pywt
        print(f"[✓] Module 'pywt' detected. Version: {pywt.__version__}")
    except ImportError:
        print("[!] Module 'pywt' missing. Initiating bridge protocol...")
        # Check system site-packages
        prefix = os.environ.get('PREFIX', '/data/data/com.termux/files/usr')
        system_path = f"{prefix}/lib/python3.13/site-packages/pywt"
        
        if os.path.exists(system_path):
            print(f"[*] Found system pywt at {system_path}. Establishing link...")
            # This logic will be handled by the bash script to ensure permission handling
        else:
            print("[!] System pywt not found. Native build required via TUR repository.")

    # Check for numpy
    try:
        import numpy
        print(f"[✓] Module 'numpy' detected. Version: {numpy.__version__}")
    except ImportError:
        print("[!] Module 'numpy' missing.")

if __name__ == "__main__":
    verify_and_fix()
