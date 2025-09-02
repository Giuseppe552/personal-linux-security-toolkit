# Scan Module

This module is responsible for scanning systems for basic security issues.

## Features

- Detects suspicious running processes.
- Finds world-writable files in common directories.
- Lists users with sudo privileges.

## Usage

Import and call `run_scan()` from `scan.py` to get scan results as a dictionary.

```
from scan.scan import run_scan
results = run_scan()
```
