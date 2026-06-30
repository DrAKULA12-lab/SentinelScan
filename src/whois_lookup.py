import whois
from urllib.parse import urlparse

def whois_lookup(url):
    print("\n[+] WHOIS Lookup...\n")

    try:
        domain = urlparse(url).netloc or url
        domain = domain.replace("www.", "")

        info = whois.whois(domain)

        print(f"[OK] Domain      : {domain}")
        print(f"[OK] Registrar   : {info.registrar}")
        print(f"[OK] Created On  : {info.creation_date}")
        print(f"[OK] Expires On  : {info.expiration_date}")

    except Exception as e:
        print(f"[ERROR] {e}")
