
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            if s.connect_ex((host, port)) == 0:
                return port
    except:
        return None

def scan_ports(target_host, ports="21,22,80,443,3306,8080"):
    """REAL SCANNER: Rapidly identifies open services on a target."""
    try:
        host = socket.gethostbyname(target_host)
        port_list = [int(p.strip()) for p in ports.split(",")]
        open_ports = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda p: scan_port(host, p), port_list)
            open_ports = [p for p in results if p is not None]

        if open_ports:
            return f"[] SOVEREIGN PORT SCAN ON {target_host} ({host}):\n" + "\n".join([f"Port {p}: OPEN" for p in open_ports])
        return f"[!] No open entry points detected on {target_host}."
    except Exception as e:
        return f"[!] Scan aborted: {str(e)}"
