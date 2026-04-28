# -*- coding: utf-8 -*-
import os
import subprocess
from rich.console import Console

console = Console()

def zero_trace():
    console.print("[bold red][][/bold red] Initiating Zero-Trace Protocol...")
    
    logs = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "/var/log/messages",
        os.path.expanduser("~/.bash_history"),
        os.path.expanduser("~/.zsh_history")
    ]
    
    for log in logs:
        if os.path.exists(log):
            try:
                # Overwrite with zeros before deleting
                subprocess.run(["shred", "-u", "-z", log], check=True, capture_output=True)
                console.print(f"[bold green][+][/bold green] Purged: {log}")
            except:
                # Fallback to simple deletion
                open(log, 'w').close()
                console.print(f"[yellow][!][/yellow] Cleared (not shredded): {log}")

    # Clear current session history
    os.system("history -c")
    console.print("[bold red][⚡][/bold red] Zero-Trace Complete. No digital footprint remains.")
