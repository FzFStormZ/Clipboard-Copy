## 🚀 About

TW: ONLY FOR EDUCATIONAL PURPOSE

**Clipboard-XRay** is a Python tool designed to monitor the clipboard in real time and analyze its content to detect possible presence of passwords.


## 📋 Features

- Continuous clipboard monitoring
- Automatic detection of potential password patterns (via regex)
- Alerts (console) when sensitive content is suspected

## 📢 New Features

- Logging with timestamps inside a logs/ folder
- Create option to the program to enable/disable verbose ✅
- Create option to define custom regex patterns for password detection by the user ✅


## 📦 Project Structure

```md
.
├── docs/
├── src/
│   └── wordlists/
│   │   └── example.txt
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── xray.py
├── tests/
│   └── test_utils.py
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

## 🛠️ Requirements & Installation

**Requirements:**
- Python 3.8+ (tested on Python 3.10.12 in Ubuntu 22.04.5 WLS)
- Dependencies listed in `requirements.txt`

**Installation:**

1. Clone the repository
   ```bash
   git clone https://github.com/FzFStormZ/Clipboard-XRay.git
   cd Clipboard-XRay
   ```
2. Create a virtual environment (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows
   ```
3. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```


## ⚙️ Usage

Run the tool with:
```bash
python3 src/main.py
```

*Options will come asap*


## 📄 License

MIT License — free to use with attribution.


## 🛠️ Author

Author: Meitoka (ex: FzFStormZ)
Feedback and discussions welcome via GitHub Issues.
