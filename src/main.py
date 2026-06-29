from banner import show_banner
from headers import check_headers
from tls import check_tls
from score import calculate_score

def main():
    show_banner()

    url = input("Enter target URL: ").strip()

    missing = check_headers(url)

    check_tls(url)

    calculate_score(missing)

if __name__ == "__main__":
    main()
