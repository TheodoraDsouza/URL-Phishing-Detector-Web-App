# 🔐 URL Phishing Detector Web App

A lightweight cybersecurity web application that detects potentially malicious or phishing URLs using rule-based heuristic analysis.

Users can enter a URL and instantly receive a safety assessment along with reasons explaining the risk level.

---

## 🚀 Features

* 🌐 Scan any URL for phishing risk
* ⚡ Instant rule-based detection (no heavy ML libraries)
* 🧠 Heuristic analysis using common phishing indicators
* 📝 Clear explanation of why a URL is suspicious
* 🎯 Beginner-friendly and fast to deploy

---

## 🧩 Tech Stack

**Frontend**

* HTML
* CSS

**Backend**

* Python
* Flask

**Detection Method**

* Rule-based heuristic engine

---

## 🌶️ About Flask & How It’s Implemented

Flask is a lightweight Python web framework used to build web servers and APIs quickly with minimal setup. It handles routing, request processing, server execution, and template rendering.

### Why Flask Was Used

* Lightweight and beginner-friendly
* Minimal dependencies
* Perfect for small cybersecurity tools
* Easy integration with Python logic

### How Flask Works in This Project

1. **App Initialization**
   A Flask application object is created to start the web server and manage routes.

2. **Routing**
   The root route (`/`) is defined to handle both page loads and form submissions.

3. **Handling User Input**
   When a user submits a URL through the form, Flask captures the input using POST request handling.

4. **Processing Logic**
   The entered URL is passed to the phishing detection function where heuristic rules calculate a risk score and generate reasons.

5. **Template Rendering**
   Flask sends the results to an HTML template using `render_template`, dynamically displaying:

   * Risk level
   * Entered URL
   * Reasons for suspicion

6. **Static Files**
   CSS styling is served through Flask’s static file handling system.

### Request Flow

User Browser → Flask Route → Detection Logic → Result Processing → HTML Template → Browser Output

Flask acts as the bridge between the user interface and the phishing detection engine.

---

## 🛡️ Phishing Detection Rules

The app assigns a risk score based on the following checks:

1. IP address used instead of domain name
2. Missing HTTPS (not secure)
3. Excessive hyphens in URL
4. Unusually long URL length
5. Suspicious keywords (login, verify, update, secure, bank, account)
6. Too many subdomains

### Risk Levels

* ✅ **Likely Safe** → Low score
* ⚠️ **Suspicious** → Medium score
* 🚨 **High Phishing Risk** → High score

---

## 📁 Project Structure

```
phishing-detector/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## ⚙️ Installation

Install Flask:

```
pip install flask
```

---

## ▶️ Run the Application

```
python app.py
```

---

## 🧪 Sample Test URLs

**Safe URLs**

* [https://www.google.com](https://www.google.com)
* [https://www.github.com](https://www.github.com)
* [https://www.wikipedia.org](https://www.wikipedia.org)

**Suspicious URLs**

* [http://secure-login-account-update.com](http://secure-login-account-update.com)
* [http://verify-bank-account-security.com](http://verify-bank-account-security.com)

---

## 💡 Use Cases

* Awareness tools for phishing prevention
* Hackathon prototypes

---

---

