# NetRecon

NetRecon is a simple, fast, multi-threaded network reconnaissance tool written in Python.  
It is designed for **CTF-style enumeration**, focusing on quickly identifying open ports and running services.

The tool performs:
- A fast top‑ports scan
- A service/version detection scan  
Both scans run **in parallel** to save time.

---

## Features

- ⚡ Fast port scanning (top 1000 ports)
- 🔍 Service detection using Nmap
- 🧵 Multi-threaded scanning
- 📌 Clean and readable output
- 🎯 CTF-focused (quick enumeration, no exploitation)

---

## Requirements

- Linux (tested on Kali Linux)
- Python 3
- Nmap installed on the system

### Python dependencies
- `python-nmap`

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Vinayjango101/NetRecon.git
cd NetRecon


2. (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install python-nmap

4. Make sure Nmap is installed
sudo apt install nmap

Usage

Run the script from the terminal:

sudo python main.py


Enter the target when prompted:

[+] TARGET: test.rebex.net

Example Output
[+] Fast scan started~!
[+] Service scan started~!
[+] Fast scan done~!
[+] Service scan done~!

HOST: test.rebex.net
21/tcp -> ftp
22/tcp -> ssh
990/tcp -> ftps

How It Works

Fast Scan

Uses Nmap top 1000 ports

Quickly identifies open ports

Service Scan

Detects running services and versions

Helps decide next CTF steps (web, SSH, FTP, etc.)

Both scans run at the same time using Python threads.
