import requests

def detect_technology(url):
    print("\n[+] Technology Detection...\n")

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        server = headers.get("Server", "Unknown")
        powered = headers.get("X-Powered-By", "Not Disclosed")

        print(f"[OK] Server       : {server}")
        print(f"[OK] X-Powered-By : {powered}")

    except Exception as e:
        print(f"[ERROR] Technology detection failed: {e}")
