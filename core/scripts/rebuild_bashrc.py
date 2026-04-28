import os

def rebuild_bashrc():
    bashrc_path = "/home/nexttoken/.bashrc"
    
    # Standard Sovereign logic
    logic = """# YOUSEF SHTIWE - Sovereign Command Center
yousef() {
    if [ "$1" = "shtiwe" ]; then
        shift
        bash "/home/nexttoken/yousef-sh.sh" "$@"
    else
        echo "Usage: yousef shtiwe [offensive|gateway|chat|setup|status]"
        echo "Example: shtiwe"
    fi
}

# Aliases
alias shtiwe="yousef shtiwe chat"
alias hermes="yousef shtiwe"
"""
    
    # Overwrite bashrc with clean logic
    with open(bashrc_path, "w") as f:
        f.write(logic)
    
    print("[✓] .bashrc rebuilt successfully.")

if __name__ == "__main__":
    rebuild_bashrc()
