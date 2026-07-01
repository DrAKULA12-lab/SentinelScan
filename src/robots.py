import requests

def check_robots(url):
    print("\n[+] Robots.txt & Sitemap Discovery...\n")

    base = url.rstrip("/")

    paths = [
        ("robots.txt", "/robots.txt"),
        ("sitemap.xml", "/sitemap.xml")
    ]

    for name, path in paths:
        target = base + path

        try:
            r = requests.get(target, timeout=5)

            if r.status_code == 200:
                print(f"[OK] {name} found")
                print(f"     {target}")
            else:
                print(f"[MISSING] {name}")

        except Exception:
            print(f"[ERROR] {name}")
