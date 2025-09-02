# Network Module

This module inspects network configuration and active connections.

## Features

- Lists open ports.
- Displays active network interfaces.
- Shows suspicious established connections.

## Usage

Import and call `run_network_checks()` from `network.py` to get network inspection results.

```
from network.network import run_network_checks
results = run_network_checks()
```
