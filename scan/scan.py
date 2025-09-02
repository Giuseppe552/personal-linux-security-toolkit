"""
Scan Module

This module provides functions to scan the system for basic security issues.
Checks include:
- Suspicious processes
- World-writable files
- Users with sudo privileges

Author: Giuseppe552
"""

import os
import subprocess

def check_suspicious_processes():
    # Example: Find processes running as root not in allowlist
    allowlist = ['init', 'systemd', 'sshd']
    suspicious = []
    try:
        proc = subprocess.check_output(["ps", "-eo", "user:20,comm"], text=True)
        for line in proc.splitlines()[1:]:
            user, command = line.split(None, 1)
            if user == "root" and command not in allowlist:
                suspicious.append(command)
    except Exception as e:
        print(f"Error checking processes: {e}")
    return suspicious

def check_world_writable_files():
    # Find world-writable files in /home and /tmp
    result = []
    for directory in ['/home', '/tmp']:
        try:
            output = subprocess.check_output(['find', directory, '-type', 'f', '-perm', '-0002'], text=True)
            files = output.strip().split('\n')
            result.extend(files if files != [''] else [])
        except Exception as e:
            print(f"Error checking writable files in {directory}: {e}")
    return result

def check_sudo_users():
    # List users with sudo privileges
    sudo_users = []
    try:
        with open('/etc/group', 'r') as f:
            for line in f:
                if line.startswith('sudo:'):
                    parts = line.strip().split(':')
                    if len(parts) == 4 and parts[3]:
                        sudo_users = parts[3].split(',')
    except Exception as e:
        print(f"Error reading /etc/group: {e}")
    return sudo_users

def run_scan():
    print("[*] Running system scan...")
    scan_data = {
        "suspicious_processes": check_suspicious_processes(),
        "world_writable_files": check_world_writable_files(),
        "sudo_users": check_sudo_users()
    }
    return scan_data
