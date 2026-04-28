
import subprocess
import json
import socket

def run_dig_scan(domain):
    """REAL RECON: Performs DNS lookup for MX, TXT, and A records."""
    try:
        cmd = f"dig {domain} ANY +short"
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
        return f"[] DNS RECORDS FOR {domain}:\n{result}" if result else f"[!] No records found for {domain}."
    except Exception as e:
        return f"[!] Dig failed: {str(e)}"

def get_ip_info(ip_or_host):
    """REAL RECON: Retrieves geolocation and ISP information for an IP or Host."""
    try:
        ip = socket.gethostbyname(ip_or_host)
        cmd = f"curl -s https://ipapi.co/{ip}/json/"
        result = subprocess.check_output(cmd, shell=True).decode()
        data = json.loads(result)
        summary = [f"{k.upper()}: {v}" for k, v in data.items() if k in ["ip", "city", "region", "country_name", "org"]]
        return f"[] INTEL ON {ip}:\n" + "\n".join(summary)
    except Exception as e:
        return f"[!] Intel extraction failed: {str(e)}"
