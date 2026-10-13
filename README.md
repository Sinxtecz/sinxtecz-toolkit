# ☠ SINXTECZ TOOLKIT

A simple network toolkit for Windows and Linux. Run useful network commands from one menu. 🖥️

## ⚡ What Can It Do?

- 🔍 **Aggressive Scan** — Detect ports and services
- 🎯 **SYN Scan** — Scan TCP ports
- 📡 **Ping** — Check if a host responds
- 🌐 **DNS Lookup** — Find domain information
- 🔎 **WHOIS Lookup** — Check domain registration
- 🛰️ **Traceroute** — Track the route to a host
- 📍 **Private IP** — View local network information
- 🌍 **Public IP** — Find your public IP address

## 🛠️ 1. Install the Requirements

### 🪟 Windows

Open **PowerShell** and run these commands one at a time:

```powershell
winget install --id Python.Python.3.13 -e
winget install --id Insecure.Nmap -e
```

For WHOIS, download Microsoft's official [Whois utility](https://learn.microsoft.com/en-us/sysinternals/downloads/whois).

You may need to reopen PowerShell after installation.

### 🐉 Kali Linux / Debian / Ubuntu

Open your terminal and paste:

```bash
sudo apt update
sudo apt install python3 nmap whois curl traceroute
```

## 🚀 2. Run the Toolkit

Open a terminal inside the folder containing `multi_tool.py`.

**Windows:**
```powershell
python multi_tool.py
```

**Linux:**
```bash
python3 multi_tool.py
```

## 🎮 3. How to Use It

1. Choose an option by entering its number.
2. Enter the requested IP address or domain.
3. Check the results.
4. Press **ENTER** to return to the menu.
5. Choose `0` to exit.

## ⚠️ Troubleshooting

- **Python not found?** Install Python and enable **Add Python to PATH** on Windows.
- **Nmap not found?** Install Nmap and reopen your terminal.
- **WHOIS not working?** Make sure the WHOIS utility is installed and accessible.
- **Traceroute not working on Windows?** Windows uses `tracert`; Linux uses `traceroute`.

## 🔒 Responsible Use

Only scan systems you own or have permission to test.

**SINXTECZ — Learn. Build. Explore.**
