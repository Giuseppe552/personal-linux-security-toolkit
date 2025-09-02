# Report Module

This module generates reports combining results from system scans and network inspections.

## Usage

Import and call `generate_report(scan_data, network_data)` from `report.py` to create a text summary.

```
from report.report import generate_report
report = generate_report(scan_results, network_results)
print(report)
```
