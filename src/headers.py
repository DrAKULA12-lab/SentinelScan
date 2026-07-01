import time
import requests
from colorama import Fore, init
from header_info import HEADER_INFO
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
    print("\n[+] Checking Security Headers...")

    try:
        start = time.time()
        response = requests.get(url, timeout=10)

        elapsed = (time.time() - start) * 1000

        print(f"{Fore.GREEN}[OK] Response Time : {elapsed:.2f} ms")
        print(f"{Fore.GREEN}[OK] HTTP Status : {response.status_code}")

        server = response.headers.get("Server", "Unknown")
        print(f"{Fore.GREEN}[OK] Server : {server}")

        missing = 0

        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(Fore.GREEN + f"[OK] {header}")
            else:
                print(Fore.RED + f"[MISSING] {header}")
                print(Fore.YELLOW + f"    Recommendation: Enable {header}")
                missing += 1

        return missing

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return len(SECURITY_HEADERS)
