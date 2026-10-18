# 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕 Toolkit

A lightweight, cross-platform Python CLI toolkit for network diagnostics and basic security reconnaissance on Windows and Linux.

## Features

### `main.py` — Core Functions
- **Nmap Scanning:** Aggressive and other supported network scans.
- **Ping:** Test network connectivity.
- **DNS Lookup:** Retrieve DNS information.
- **WHOIS Lookup:** Retrieve domain registration details.
- **IP Information:** Display local and public IP information.
- **Dependency Checker:** Check required external utilities.
- **Cross-Platform Support:** Use OS-specific commands.
- **Error Handling:** Handle missing tools, permissions, and execution errors.

### `ui.py` — Terminal Interface
- Colored terminal output and consistent styling.
- Informational, success, warning, and error messages where implemented.
- User prompts and readable command feedback.
- Reusable UI functions for a consistent SINXTECZ experience.

## Project Structure

```text
SINXTECZ-Toolkit/
├── main.py
├── ui.py
└── README.md
```

## Requirements
- Python 3.10 or newer recommended.
- Windows or Linux.
- Required utilities, depending on enabled features: Nmap, WHOIS, cURL, and system networking commands.

## Installation & Usage

1. Install Python and the required utilities.
2. Download or clone the repository.
3. Open the project directory.
4. Run:

```bash
python main.py
```

On Linux, you may need:

```bash
python3 main.py
```

Follow the terminal menu to select an operation.

## Compatibility
- **Windows:** Supported with required utilities installed.
- **Linux:** Supported with required utilities installed.
- **Termux:** Potentially compatible; command availability may vary.

## Security & Responsible Use
- Test only systems you own or have explicit permission to assess.
- Some scans, especially SYN scans, may require administrator or root privileges.
- Use aggressive scans responsibly and follow applicable laws and network policies.

## Troubleshooting
- **Command not found:** Install the required utility and verify your PATH.
- **Permission denied:** Check the operation's privilege requirements.
- **Import error:** Ensure `main.py` and `ui.py` are in the correct directory.
- **Color issues:** Use a terminal with ANSI color support.

## Project Scope
This README documents only `main.py` (core operations) and `ui.py` (terminal interface). Additional modules and optional features are outside its scope.

## Author
**SINXTECZ**

A cybersecurity learning and Python development project focused on networking, command-line tools, and practical security skills.

*Built for learning. Designed for practical use. Developed with Python.*
