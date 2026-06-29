import ssl
import socket
from urllib.parse import urlparse

def check_tls(url):
    print("\n[+] TLS/SSL Analysis...\n")

    try:
        hostname = urlparse(url).hostname

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                print(f"[OK] TLS Version : {ssock.version()}")

                cert = ssock.getpeercert()

                print(f"[OK] Certificate Subject : {cert.get('subject')}")
                print(f"[OK] Certificate Issuer  : {cert.get('issuer')}")
                print(f"[OK] Expires On          : {cert.get('notAfter')}")

    except Exception as e:
        print(f"Error: {e}")
