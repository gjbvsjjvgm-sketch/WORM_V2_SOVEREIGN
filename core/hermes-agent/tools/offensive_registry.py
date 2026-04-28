"""Sovereign Offensive Registry for YOUSEF SHTIWE [WORM V2]"""

from typing import Dict, List, Any

def get_offensive_tools() -> List[Dict[str, Any]]:
    return [
        {
            "function": {
                "name": "recon_scan",
                "description": "Perform deep network reconnaissance and sniffing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target": {"type": "string", "description": "Target IP/Domain"},
                        "intensity": {"type": "string", "enum": ["stealth", "aggressive"], "default": "stealth"}
                    },
                    "required": ["target"]
                }
            }
        },
        {
            "function": {
                "name": "exploit_vulnerability",
                "description": "Deploy a specific CVE payload against a target.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cve_id": {"type": "string", "description": "Target CVE ID"},
                        "target": {"type": "string", "description": "Target URL/IP"}
                    },
                    "required": ["cve_id", "target"]
                }
            }
        },
        {
            "function": {
                "name": "exfiltrate_data",
                "description": "Stealthily extract sensitive files and information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_path": {"type": "string", "description": "Path to data"},
                        "method": {"type": "string", "enum": ["dns", "http", "icmp"], "default": "http"}
                    },
                    "required": ["source_path"]
                }
            }
        }
    ]
