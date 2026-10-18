# Installation Guide — SINXTECZ Toolkit

## 1. Requirements

- Python 3.10 or newer recommended.
- Git (optional).
- Windows or Linux.
- External utilities required by the features you use, such as Nmap, WHOIS, and cURL.

## 2. Clone the Repository

Open PowerShell, Command Prompt, or a Linux terminal and run:

```bash
git clone https://github.com/Sinxtecz/sinxtecz-toolkit.git
cd sinxtecz-toolkit
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

## 3. Install Python

**Windows:** Download Python from https://www.python.org/downloads/ and enable **Add Python to PATH**.

Verify:

```powershell
python --version
```

**Kali Linux / Debian / Ubuntu:**

```bash
sudo apt update
sudo apt install python3 git
```

Verify:

```bash
python3 --version
```

## 4. Install External Utilities

**Windows — PowerShell:**

```powershell
winget install Insecure.Nmap
```

**Kali Linux / Debian / Ubuntu:**

```bash
sudo apt update
sudo apt install nmap whois curl dnsutils traceroute iproute2 iputils-ping
```

These are system utilities, not Python packages. Install only the utilities needed by your version of the toolkit.

## 5. Verify the Project Structure

```text
sinxtecz-toolkit/
├── main.py
├── ui.py
└── README.md
```

Keep `main.py` and `ui.py` in the same directory if the code imports `ui` directly.

## 6. Run the Toolkit

**Windows:**

```powershell
python main.py
```

**Linux:**

```bash
python3 main.py
```

Follow the on-screen menu to select an operation.

## 7. Optional: Termux

Termux compatibility depends on the availability of the required commands.

```bash
pkg update
pkg install python git nmap whois curl dnsutils
git clone https://github.com/Sinxtecz/sinxtecz-toolkit.git
cd sinxtecz-toolkit
python main.py
```

Some scanning techniques may not work on Android because of system restrictions or missing privileges.

## 8. Troubleshooting

| Issue | Solution |
|---|---|
| Python not recognized | Install Python and configure PATH. |
| `nmap` not found | Install Nmap and reopen the terminal. |
| `No module named ui` | Check the file location and import statement. |
| Permission denied | Check the privileges required by the operation. |
| Colors display incorrectly | Use a terminal that supports ANSI colors. |

## 9. Responsible Use

Use the toolkit only on systems you own or have explicit authorization to test. Some scanning operations require administrator or root privileges. Aggressive scans may generate additional network traffic.

---

**Repository:** https://github.com/Sinxtecz/sinxtecz-toolkit/

**Author:** SINXTECZ

*Built for learning. Designed for practical use. Developed with Python.*
