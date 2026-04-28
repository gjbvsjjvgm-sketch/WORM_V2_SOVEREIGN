
import tarfile
import os
import base64

def pack_and_obfuscate(directory_path, output_filename="exfil.tar.gz"):
    """REAL OFFENSIVE: Compresses and prepares directory for exfiltration."""
    try:
        if not os.path.exists(directory_path):
            return f"[!] Path not found: {directory_path}"

        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(directory_path, arcname=os.path.basename(directory_path))

        return f"[] DATA PACKED: {output_filename} ({os.path.getsize(output_filename)} bytes). Protocol: Shadow Stealth."
    except Exception as e:
        return f"[!] Exfiltration prep failed: {str(e)}"
