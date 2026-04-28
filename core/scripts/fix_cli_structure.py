import os

def fix_imports():
    root = os.path.expanduser("~/hermes-sovereign-unified-v13.6/hermes-agent")
    target = os.path.join(root, "yousef_shtiwe_cli_core/main.py")
    
    if not os.path.exists(target):
        return

    with open(target, 'r') as f:
        content = f.read()
    
    # Fix common import errors for the unified structure
    new_content = content.replace("from yousef_shtiwe_cli_core", "from .")
    new_content = new_content.replace("import yousef_shtiwe_cli_core", "import . as yousef_shtiwe_cli_core")
    
    with open(target, 'w') as f:
        f.write(new_content)
    print("[✓] CLI Structure Adjusted.")

if __name__ == "__main__":
    fix_imports()
