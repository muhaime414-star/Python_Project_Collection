# Log Analysis Utilities

This directory contains Python scripts designed for network engineering and security operations (SOC) tasks, specifically focused on parsing, filtering, and organizing log data.

## Tools

### 1. Unique IP Extractor (`ip_extractor.py`)
A command-line utility that processes raw server or firewall logs to extract IP addresses. It automatically filters out duplicate entries and sorts the remaining IP addresses in true numerical order (using network math, rather than alphabetical sorting). The clean list can be printed or saved directly to a file for use with scanning tools like Nmap.

#### Requirements
* Python 3.x
* No external libraries required (uses built-in `argparse`, `os`, and `ipaddress` modules).

#### Usage
Run the script from your terminal using Python 3.

**Basic execution (Auto-generates output file):**
```bash
python3 ip_extractor.py -f server_logs.txt