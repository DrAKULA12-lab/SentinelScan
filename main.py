choice = input("Scan (1) Single URL or (2) File? ")

if choice == "2":
    with open("targets.txt") as f:
        urls = [line.strip() for line in f if line.strip()]
else:
    urls = [input("Enter target URL: ").strip()]
