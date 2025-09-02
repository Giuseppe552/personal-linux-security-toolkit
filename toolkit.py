"""
Main Toolkit for Personal Linux Security

This script orchestrates all security checks:
- Network inspection
- System scanning
- Report generation with color output and file saving

Usage:
    python3 toolkit.py [--scan] [--network] [--report] [--all]

Author: Giuseppe552
"""

import argparse
from scan.scan import run_scan
from network.network import run_network_checks
from report.report import generate_report

def main():
    parser = argparse.ArgumentParser(description="Personal Linux Security Toolkit")
    parser.add_argument("--scan", action="store_true", help="Run system scan")
    parser.add_argument("--network", action="store_true", help="Run network inspection")
    parser.add_argument("--report", action="store_true", help="Generate report")
    parser.add_argument("--all", action="store_true", help="Run all checks")
    args = parser.parse_args()

    scan_results = None
    network_results = None

    if args.all or args.scan:
        scan_results = run_scan()

    if args.all or args.network:
        network_results = run_network_checks()

    if args.all or args.report:
        report = generate_report(scan_results, network_results)
        # Terminal output handled by Rich inside report.generate_report

if __name__ == "__main__":
    main()
