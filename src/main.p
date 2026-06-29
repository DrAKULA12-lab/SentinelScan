from banner import show_banner
from headers import check_headers
from tls import check_tls

def main():
    show_banner()

    url = input("Enter target URL: ").strip()

    check_headers(url)
    check_tls(url)

if __name__ == "__main__":
    main()
