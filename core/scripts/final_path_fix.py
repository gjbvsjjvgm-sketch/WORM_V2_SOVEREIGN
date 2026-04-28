import os
import sys

def final_path_fix():
    # 1. Update yousef_constants.py to use .yousef instead of .hermes
    constants_path = "hermes-agent/yousef_constants.py"
    if os.path.exists(constants_path):
        with open(constants_path, 'r') as f:
            content = f.read()
        
        # Replace the hardcoded directory name
        new_content = content.replace(".hermes", ".yousef")
        
        if new_content != content:
            with open(constants_path, 'w') as f:
                f.write(new_content)
            print(f"[✓] Updated directory constant in {constants_path}")

    # 2. Rename existing data directory if it exists
    old_data = "/home/nexttoken/.hermes"
    new_data = "/home/nexttoken/.yousef"
    if os.path.exists(old_data) and not os.path.exists(new_data):
        os.rename(old_data, new_data)
        print(f"[✓] Renamed data directory to {new_data}")

if __name__ == "__main__":
    final_path_fix()
