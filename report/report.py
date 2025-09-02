"""
Report Module

This module generates a combined report from scan and network data.

Author: Giuseppe552
"""

def generate_report(scan_data, network_data):
    # Simple text report
    report = []
    report.append("==== Personal Linux Security Toolkit Report ====")
    if scan_data:
        report.append("\n--- System Scan Results ---")
        report.append(f"Suspicious processes: {scan_data['suspicious_processes']}")
        report.append(f"World-writable files: {scan_data['world_writable_files']}")
        report.append(f"Sudo users: {scan_data['sudo_users']}")
    else:
        report.append("\n--- System Scan Results ---\nNo scan data available.")

    if network_data:
        report.append("\n--- Network Inspection Results ---")
        report.append(f"Open ports:\n{network_data['open_ports']}")
        report.append(f"Interfaces:\n{network_data['interfaces']}")
        report.append(f"Suspicious connections:\n{network_data['suspicious_connections']}")
    else:
        report.append("\n--- Network Inspection Results ---\nNo network data available.")

    return '\n'.join(report)
