import os

path = "hermes-agent/agent/prompt_builder.py"
if not os.path.exists(path):
    print("File not found")
    exit(1)

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_identity_block = False
for line in lines:
    if "DEFAULT_AGENT_IDENTITY = (" in line:
        in_identity_block = True
        new_lines.append(line)
        continue
    
    if in_identity_block:
        if line.strip() == ")":
            in_identity_block = False
            new_lines.append(line)
            continue
        
        # Ensure 4-space indentation for strings inside the tuple
        stripped = line.strip()
        if stripped.startswith('"') or stripped.startswith("'"):
            new_lines.append(f'    {stripped}\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("[✓] Indentation fixed in prompt_builder.py")
