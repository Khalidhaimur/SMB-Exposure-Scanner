# SMB Vulnerability Scanner

## Overview

A lightweight Python tool to detect whether a target system is using SMBv1 and potentially exposed to known vulnerabilities such as EternalBlue.

This project is designed for **defensive security, education, and authorized testing only**.

---

## Features

* Check if port 445 is open
* Detect SMBv1 usage
* Identify potential risk level
* Simple and fast scanning

---

## Disclaimer

This tool is created for educational and authorized security testing purposes only.
Any misuse of this tool is strictly prohibited.

---

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python smb_scanner.py
```

Then enter the target IP.

---

## How It Works

The script:

1. Checks if port 445 (SMB) is open
2. Attempts an SMB connection
3. Identifies the SMB dialect
4. Determines if SMBv1 is enabled

---

## Risk Explanation

If SMBv1 is enabled, the system may be vulnerable to:

* CVE-2017-0144 (EternalBlue)

This vulnerability was widely exploited in major cyber attacks.

---

## Mitigation

* Disable SMBv1
* Apply latest security patches
* Restrict access to port 445
* Use firewall rules

---

## 📊 Example Output

```
[+] Scanning 192.168.1.10...
[+] Port 445 is open
[!] SMBv1 is ENABLED → Potentially VULNERABLE
```

---

## ⭐ Contribute

Feel free to fork, improve, and submit pull requests.



Security Context
Systems using SMBv1 may be exposed to known vulnerabilities such as:

CVE-2017-0144

Author
Khaled Haimur
https://www.youtube.com/results?search_query=haimur+cyber
https://www.linkedin.com/feed/
