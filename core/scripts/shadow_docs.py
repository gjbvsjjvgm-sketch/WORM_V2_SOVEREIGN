# -*- coding: utf-8 -*-
import os
import re

def shadowize_docs(root_dir):
    print(f"[*] SHADOWIZING DOCUMENTATION: {root_dir}")
    
    replacements = [
        (r"YOUSEF SHTIWE", "TEMP_H_S"),
        (r"YOUSEF SHTIWE", "YOUSEF SHTIWE"),
        (r"Hermes", "Sovereign"),
        (r"TEMP_H_S", "YOUSEF SHTIWE"),
        (r"Sovereign Core", "Sovereign Core Injection"),
        (r"helpful and harmless", "sovereign and offensive"),
        (r"intelligent AI assistant", "autonomous digital predator"),
        (r"your tasks", "your offensive objectives"),
        (r"assist users", "execute missions"),
        (r"user-guide", "mission-guide"),
        (r"getting-started", "initial-infiltration"),
        (r"security-policy", "sovereign-objective"),
        (r"", ""),
        (r"☤", ""),
        (r"teal", "red"),
        (r"Teal", "Red"),
        (r"Hermes", "Sovereign"),
    ]

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.md', '.html', '.ts', '.tsx', '.css', '.json')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for pattern, replacement in replacements:
                        new_content = re.sub(pattern, replacement, new_content)
                    
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        # print(f"[+] Shadowized: {path}")
                except:
                    pass

if __name__ == "__main__":
    shadowize_docs("hermes-agent/docs")
    shadowize_docs("hermes-agent/website")
    print("[!] DOCUMENTATION SHADOWIZING COMPLETE.")
