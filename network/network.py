"""
Network Module

This module inspects the network configuration and connections.
Checks include:
- Open ports
- Active network interfaces
- Suspicious connections

Author: Giuseppe552
"""

import subprocess

def check_open_ports():
    # Requires 'netstat' or 'ss'
    try:
        output = subprocess.check_output(['ss', '-tuln'], text=True)
        return output
    except Exception as e:
        return f"Error checking open ports: {e}"

def list_interfaces():
    try:
        output = subprocess.check_output(['ip', 'addr'], text=True)
        return output
    except Exception as e:
        return f"Error listing interfaces: {e}"

def check_suspicious_connections():
    # Example: List established connections to remote hosts
    try:
        output = subprocess.check_output(['ss', '-tanp'], text=True)
        connections = []
        for line in output.splitlines()[1:]:
            if "ESTAB" in line:
                connections.append(line)
        return connections
    except Exception as e:
        return [f"Error checking connections: {e}"]

def run_network_checks():
    print("[*] Running network inspection...")
    network_data = {
        "open_ports": check_open_ports(),
        "interfaces": list_interfaces(),
        "suspicious_connections": check_suspicious_connections()
    }
    return network_data
