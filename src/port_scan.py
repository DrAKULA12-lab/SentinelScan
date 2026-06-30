import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

def port_scan(url):
    print("\n[+] Port Scan...\n")

    host = url.replace("https://", "").replace("http://", "").split("/")[0]

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"[OPEN]   {port:<5} {service}")
        else:
            print(f"[CLOSED] {port:<5} {service}")

        sock.close()
