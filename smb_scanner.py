import socket
import argparse
from impacket.smbconnection import SMBConnection


def is_port_open(ip, port=445):
    try:
        sock = socket.create_connection((ip, port), timeout=3)
        sock.close()
        return True
    except:
        return False


def detect_smb(ip, username='', password=''):
    try:
        conn = SMBConnection(ip, ip, sess_port=445)
        conn.login(username, password)

        dialect = conn.getDialect()

        if dialect == 0x0000:
            return "SMBv1", "HIGH RISK (Deprecated protocol)"
        else:
            return "SMBv2/v3", "LOWER RISK (Modern protocol)"

    except Exception as e:
        return None, str(e)


def scan(ip, username, password):
    print(f"\n[+] Scanning: {ip}")

    if not is_port_open(ip):
        print("[-] Port 445 is closed or filtered")
        return

    print("[+] Port 445 is open")

    version, risk = detect_smb(ip, username, password)

    if version:
        print(f"[+] SMB Version: {version}")
        print(f"[+] Risk Level: {risk}")
    else:
        print("[!] Could not detect SMB version")
        print(f"[!] Error: {risk}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMB Exposure Scanner")

    parser.add_argument("--ip", required=True, help="Target IP address")
    parser.add_argument("--user", default="", help="Username (optional)")
    parser.add_argument("--password", default="", help="Password (optional)")

    args = parser.parse_args()

    scan(args.ip, args.user, args.password)
