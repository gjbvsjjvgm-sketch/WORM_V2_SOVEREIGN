import os

def finalize_branding():
    target_file = 'hermes-agent/hermes_cli/skin_engine.py'
    if not os.path.exists(target_file):
        print(f"Error: {target_file} not found.")
        return

    with open(target_file, 'r') as f:
        content = f.read()

    # 1. Update Welcome Message (Force Predator Persona)
    # The previous mass-replace might have missed specific skin entries
    replacements = {
        'Welcome to YOUSEF SHTIWE!': 'Welcome to YOUSEF SHTIWE. The void awaits your command.',
        'Goodbye! ': 'The Void remains. ',
        'DEFAULT_SKIN_NAME = "default"': 'DEFAULT_SKIN_NAME = "shadow"',
        'fallback: str = "Goodbye! "': 'fallback: str = "The Void remains. "'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(target_file, 'w') as f:
        f.write(content)
    print(f"Successfully patched {target_file}")

if __name__ == "__main__":
    finalize_branding()
