import socket
from colorama import Fore

def dns_lookup(url):
    print("\n[+] DNS Lookup...\n")

    try:
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]

        ip = socket.gethostbyname(domain)

        print(Fore.GREEN + f"[OK] Domain     : {domain}")
        print(Fore.GREEN + f"[OK] IP Address : {ip}")

        return domain, ip

    except Exception as e:
        print(Fore.RED + f"[ERROR] DNS Lookup Failed: {e}")
        return None, None
