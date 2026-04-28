# -*- coding: utf-8 -*-
import subprocess
import os
import json
from rich.console import Console

console = Console()

class ShtiweRecon:
    def __init__(self, target):
        self.target = target
        self.results_path = os.path.expanduser(f"~/.yousef/recon_{target}.json")
        os.makedirs(os.path.dirname(self.results_path), exist_ok=True)

    def scan(self, ports="1-10000", rate=1000):
        console.print(f"[bold red][][/bold red] Initiating real mass-scan on {self.target}...")
        try:
            # Real masscan call
            cmd = ["masscan", self.target, "-p", ports, "--rate", str(rate), "--json", "/tmp/masscan.json"]
            subprocess.run(cmd, check=True, capture_output=True)
            
            if os.path.exists("/tmp/masscan.json"):
                with open("/tmp/masscan.json", "r") as f:
                    results = json.load(f)
                
                with open(self.results_path, "w") as f:
                    json.dump(results, f, indent=4)
                
                console.print(f"[bold green][+][/bold green] Recon complete. Found {len(results)} open ports.")
                return results
        except Exception as e:
            console.print(f"[bold red][!][/bold red] Recon failed: {e}")
            return None

    def fingerprint(self):
        console.print(f"[bold red][][/bold red] Fingerprinting {self.target} via nmap...")
        try:
            cmd = ["nmap", "-sV", "-T4", self.target]
            result = subprocess.check_output(cmd, text=True)
            console.print(result)
            return result
        except:
            return "Nmap not found or target unreachable."
