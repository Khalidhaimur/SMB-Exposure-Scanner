SMB Vulnerability Scanner
Overview
SMB Vulnerability Scanner is a lightweight Python tool designed to detect whether a target system is using SMBv1 and assess potential exposure to known security risks such as EternalBlue.
This tool is intended for defensive security, educational purposes, and authorized security testing only.

Features
Detects if port 445 (SMB) is open
Identifies SMB protocol version (SMBv1 vs SMBv2/v3)
Supports anonymous and authenticated access
Provides basic risk assessment
Fast and lightweight scanning
Disclaimer

This tool is developed strictly for educational and authorized security testing purposes only.
Any misuse, unauthorized scanning, or illegal activity is strictly prohibited.

Installation
pip install -r requirements.txt
Usage
python smb_scanner.py

Then enter:
Target IP
Optional username/password (or leave empty for anonymous mode)
How It Works

The tool performs the following steps:
Checks if port 445 (SMB) is open
Attempts SMB connection (anonymous or authenticated)
Negotiates SMB dialect
Determines SMB version (SMBv1 or SMBv2/v3)
Reports risk level
Security Context

Systems using SMBv1 may be exposed to critical vulnerabilities such as:

CVE-2017-0144
This vulnerability has been widely exploited in past global cyber attacks.

Mitigation
To reduce exposure risk:
Disable SMBv1 protocol
Apply latest security patches
Restrict port 445 access via firewall
Monitor exposed services regularly
Example Output
[+] Scanning 192.168.1.10...
[+] Port 445 is open
[+] SMB Version: SMBv1
[!] Risk Level: HIGH (Deprecated protocol)
Contributing

Feel free to fork this project, improve functionality, and submit pull requests.

Author
Khaled Haimur

Social Links:

YouTube: https://www.youtube.com/results?search_query=haimur+cyber
LinkedIn: https://www.linkedin.com/feed/
Note

This project focuses on security visibility and exposure detection, not exploitation.
