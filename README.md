# Personal Linux Security Toolkit

A beginner-friendly toolkit for inspecting and improving your personal Linux system’s security.  
**Run all security checks with one command.**  
Great for personal use, learning, or showing security initiative to employers!

## Features

- Automated rootkit and antivirus scans (`rkhunter`, `chkrootkit`, `ClamAV`)
- Suspicious file/process inspector
- Network activity monitor (open ports, sniffers)
- System change tracker (users, groups, critical files)
- Easy-to-read security report
- Self-contained and documented for replication

## One-line Quickstart

```bash
git clone https://github.com/Giuseppe552/personal-linux-security-toolkit.git && cd personal-linux-security-toolkit && pip install -r requirements.txt && sudo python3 toolkit.py
```

> **Note:** Some scans require `sudo` (admin privileges) for full results.

## Usage

- Run `sudo python3 toolkit.py` and follow prompts
- Security report saved to `report/security_report.md`

## Requirements

- Python 3.8+
- rkhunter, chkrootkit, clamav, netstat, lsof  
  *(Install via your package manager: `sudo apt install rkhunter chkrootkit clamav net-tools lsof`)*

## Why?

Linux security tools can be overwhelming. This toolkit automates common checks and explains what they mean, making security accessible for everyone—including non-experts and job seekers.

## Contributing

All ideas, guides, and improvements welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
