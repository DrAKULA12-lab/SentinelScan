import os
import json
from datetime import datetime

def save_report(url, score):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_file = f"reports/report_{timestamp}.txt"
    json_file = f"reports/report_{timestamp}.json"

    with open(txt_file, "w") as f:
        f.write("SentinelScan Report\n")
        f.write("===================\n")
        f.write(f"Target: {url}\n")
        f.write(f"Security Score: {score}/100\n")

    data = {
        "target": url,
        "security_score": score,
        "generated": timestamp
    }

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n[+] TXT Report: {txt_file}")
    print(f"[+] JSON Report: {json_file}")
