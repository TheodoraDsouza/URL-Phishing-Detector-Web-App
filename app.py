from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)

def phishing_score(url):
    score = 0
    reasons = []

    # Rule 1: IP address in URL
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    if re.search(ip_pattern, url):
        score += 2
        reasons.append("Contains IP address instead of domain")

    # Rule 2: HTTPS check
    if not url.startswith("https://"):
        score += 1
        reasons.append("Not using HTTPS")

    # Rule 3: Too many hyphens
    if url.count('-') > 2:
        score += 1
        reasons.append("Too many hyphens in URL")

    # Rule 4: Very long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # Rule 5: Suspicious words
    suspicious_words = ["login", "verify", "update", "secure", "account", "bank"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")
            break

    # Rule 6: Too many subdomains
    domain = urlparse(url).netloc
    if domain.count('.') > 3:
        score += 1
        reasons.append("Too many subdomains")

    return score, reasons


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reasons = []
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        score, reasons = phishing_score(url)

        if score >= 3:
            result = "⚠️ High Phishing Risk"
        elif score == 2:
            result = "⚠️ Suspicious"
        else:
            result = "✅ Likely Safe"

    return render_template("index.html", result=result, reasons=reasons, url=url)


if __name__ == "__main__":
    app.run(debug=True)