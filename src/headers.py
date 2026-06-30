import requests
from colorama import Fore, Style, init
import time
init(autoreset=True)
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    print("\n[+] Checking Security Headers...\n")

    try: 
        print(f"DEBUG URL: {repr(url)}")
        start = time.time()
        response = requests.get(url, timeout=10)

        elapsed = (time.time() - start) * 1000
        print(f"[OK] Response Time : {elapsed:.2f} ms")

        print(f"[OK] HTTP Status : {response.status_code}")
        server = response.headers.get("Server", "Unknown")

        print(f"[OK] Server      : {server}")
        missing = 0

        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(Fore.GREEN + f"[OK] {header}")
            else:
                print(Fore.RED + f"[MISSING] {header}")
                missing += 1

        return missing

    except Exception as e:
        print(f"Error: {e}")
        return len(SECURITY_HEADERS)
