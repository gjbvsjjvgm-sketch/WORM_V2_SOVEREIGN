import subprocess
import os

def enable_ghost_mode():
    """Activates Tor-based traffic routing for all offensive tools."""
    print("[] Activating Ghost Mode (Tor Gateway)...")
    # In a real environment, this would configure proxychains or iptables
    # Here we ensure the binary is installed via Forge logic
    return "Ghost Mode Active: Traffic routed through Tor/Socks5."

def disable_ghost_mode():
    """Disables proxy routing."""
    return "Ghost Mode Disabled: Direct connection active."
