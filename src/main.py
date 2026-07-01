from banner import show_banner
from headers import check_headers
from tls import check_tls
from score import calculate_score
from report import save_report
from html_report import save_html_report
from dns_lookup import dns_lookup
from port_scan import port_scan
from whois_lookup import whois_lookup
from tech_detect import detect_technology
from robots import check_robots
def main():
    show_banner()

    choice = input("Scan (1) Single URL or (2) File? ").strip()

    if choice == "2":
        with open("targets.txt", "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = [input("Enter target URL: ").strip()]

    for url in urls:
        print("\n" + "=" * 50)
        print("Scanning:", url)
        print("=" * 50)

        whois_lookup(url)
        detect_technology(url)
        dns_lookup(url)
        check_robots(url)
        port_scan(url)
        missing = check_headers(url)
        check_tls(url)
        score = calculate_score(missing)
        save_report(url, score)
        save_html_report(url, score)
if __name__ == "__main__":
    main()
