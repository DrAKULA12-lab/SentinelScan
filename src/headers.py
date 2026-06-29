import requests

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
        response = requests.get(url, timeout=10)

        missing = 0

        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(f"[OK] {header}")
            else:
                print(f"[MISSING] {header}")
                missing += 1

        return missing

    except Exception as e:
        print(f"Error: {e}")
        return len(SECURITY_HEADERS)
