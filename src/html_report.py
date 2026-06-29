from datetime import datetime
import os

def save_html_report(url, score):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/report_{timestamp}.html"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>SentinelScan Report</title>
<style>
body {{
    font-family: Arial;
    background: #f4f4f4;
    padding: 30px;
}}
.container {{
    background: white;
    padding: 20px;
    border-radius: 10px;
}}
h1 {{
    color: #2c3e50;
}}
.score {{
    font-size: 28px;
    color: green;
}}
</style>
</head>
<body>

<div class="container">
<h1>SentinelScan v2.0 Report</h1>

<p><strong>Target:</strong> {url}</p>
<p><strong>Date:</strong> {datetime.now()}</p>

<hr>

<p class="score">Security Score: {score}/100</p>

</div>

</body>
</html>
"""

    with open(filename, "w") as f:
        f.write(html)

    print(f"[+] HTML Report: {filename}")
