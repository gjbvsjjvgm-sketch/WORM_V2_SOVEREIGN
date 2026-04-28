import os
import re

def clean_file(path):
    with open(path, 'r') as f:
        content = f.read()
    
    # regex to find aliases=[...] and remove it. 
    # Handles add_parser(aliases=...) which is unsupported in some environments/versions
    # and also catches cases where ArgumentParser might be receiving it incorrectly.
    
    # Case 1: , aliases=[...]
    new_content = re.sub(r',\s*aliases\s*=\s*\[[^\]]*\]', '', content)
    # Case 2: aliases=[...], 
    new_content = re.sub(r'aliases\s*=\s*\[[^\]]*\],?\s*', '', new_content)
    
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        return True
    return False

count = 0
# Scan the root and the internal core directories specifically
targets = [
    'hermes-agent/yousef_shtiwe_cli_core',
    'yousef_shtiwe_cli'
]

for target in targets:
    if os.path.exists(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith('.py'):
                    if clean_file(os.path.join(root, file)):
                        count += 1

print(f'Sovereign Clean-up: Purged {count} files of incompatible arguments.')
