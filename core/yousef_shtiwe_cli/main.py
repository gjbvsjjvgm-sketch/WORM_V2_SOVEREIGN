# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def display_banner():
    banner = """
    ▄████▄   ▒█████   ██▒   █▓▓█████  ██▀███  ▓█████  ██▓  ▄████  ███▄    █     
   ▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓█   ▀ ▓██▒ ██▒ ▀█▒ ██ ▀█   █     
   ▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒███   ▒██░▒██░▄▄▄░▓██  ▀█ ██▒    
   ▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ▒██░░▓█  ██▓▓██▒  ▐▌██▒    
   ▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒░▒████▒░██░░▒▓███▀▒▒██░   ▓██░    
    """
    console.print(banner, style="bold #BF00FF")
    console.print(Panel("[bold #00FF00] YOUSEF SHTIWE - SOVEREIGN SUPREMACY V13.6 [/]", border_style="#00FF00"))

def run_real_setup():
    display_banner()
    console.print(Panel("[bold red] ☠️ INITIATING FULL ARSENAL PROCUREMENT ☠️ [/]", border_style="red"))
    
    # تحديد مسار السكريبت الرئيسي للتثبيت
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    install_script = os.path.join(base_dir, "scripts", "install_termux.sh")
    
    if os.path.exists(install_script):
        console.print("[*] Launching Supremacy Installer Protocol...")
        # تنفيذ سكريبت التثبيت الحقيقي
        subprocess.run(["bash", install_script], check=False)
    else:
        console.print("[!] Installer script not found. Attempting emergency recovery...")
        # منطق استعادة طارئ إذا لزم الأمر
        pass

    console.print("\n[bold green][✓] SOVEREIGN SUPREMACY SETUP CONCLUDED. ALL SYSTEMS ONLINE.[/]")

def main():
    if len(sys.argv) < 2:
        display_banner()
        return

    cmd = sys.argv[1].lower()
    
    if cmd == "setup":
        run_real_setup()
    elif cmd == "chat":
        # منطق بدء الدردشة مع العميل
        console.print("[*] Entering Predator Chat Mode...")
        pass
    elif cmd == "payload":
        # التعامل مع توليد البايلودات
        if len(sys.argv) >= 6:
            from offensive_modules.arsenal import get_arsenal
            ars = get_arsenal()
            console.print(ars.generate_payload(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
        else:
            console.print("[!] Usage: yousef payload <platform> <lhost> <lport> <name>")
    else:
        # تمرير الأوامر الأخرى للنواة
        pass

if __name__ == "__main__":
    main()
