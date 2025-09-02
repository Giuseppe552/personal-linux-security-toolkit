"""
Unit tests for the Scan Module

Run with:
    python -m unittest tests/test_scan.py
"""

import unittest
from scan.scan import check_suspicious_processes, check_world_writable_files, check_sudo_users, run_scan

class TestScanModule(unittest.TestCase):

    def test_check_suspicious_processes(self):
        processes = check_suspicious_processes()
        self.assertIsInstance(processes, list)

    def test_check_world_writable_files(self):
        files = check_world_writable_files()
        self.assertIsInstance(files, list)

    def test_check_sudo_users(self):
        users = check_sudo_users()
        self.assertIsInstance(users, list)

    def test_run_scan(self):
        results = run_scan()
        self.assertIsInstance(results, dict)
        self.assertIn("suspicious_processes", results)
        self.assertIn("world_writable_files", results)
        self.assertIn("sudo_users", results)

if __name__ == "__main__":
    unittest.main()
