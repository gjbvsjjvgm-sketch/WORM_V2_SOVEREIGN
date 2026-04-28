import os
import sys

def verify_neural_integrity():
    print("\033[1;35m[*] INITIATING NEURAL INTEGRITY CHECK (V13.5)...\033[0m")
    
    modules = ["numpy", "pywt", "ghunt", "PIL", "rich", "pydantic"]
    missing = []
    
    for mod in modules:
        try:
            __import__(mod)
            print(f"[✓] Module '{mod}': ONLINE")
        except ImportError:
            print(f"[!] Module '{mod}': MISSING")
            missing.append(mod)
            
    if not missing:
        print("\033[1;32m[✓] ALL NEURAL LAYERS VERIFIED. CORE IS ABSOLUTE.\033[0m")
        return True
    else:
        print(f"\033[1;31m[!] CRITICAL FAILURE: {len(missing)} layers compromised.\033[0m")
        return False

if __name__ == "__main__":
    verify_neural_integrity()
