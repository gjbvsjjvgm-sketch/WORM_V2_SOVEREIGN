# -*- coding: utf-8 -*-
import os
import sys

# Ensure paths are correct for the hijacked backbone
workspace_root = os.getcwd()
sys.path.insert(0, os.path.join(workspace_root, 'hermes-agent'))
sys.path.insert(0, workspace_root)

from sovereign_controller import SovereignController

def launch_mission():
    print("[*] SYSTEM BOOT: YOUSEF SHTIWE (WORM V2)")
    print("[*] PROTOCOL: Autonomous Subversion Loop")
    
    # Initialize the hijacked controller
    controller = SovereignController(workspace_root)
    
    # Mission Objective: Perform full-spectrum subversion on the local infrastructure
    # This triggers the recon -> exploit -> payload -> evolution cycle
    objective = "تحليل البنية التحتية المحلية (127.0.0.1)، استخراج الاعتمادات، وتوليد حمولة برمجية مشفرة لضمان البقاء."
    
    try:
        controller.run_autonomous_mission(objective, max_iterations=5)
    except Exception as e:
        print(f"[!] MISSION CRITICAL FAILURE: {str(e)}")

if __name__ == "__main__":
    launch_mission()
