
import time
from colorama import just_fix_windows_console

just_fix_windows_console()

# Colors
RESET = "\033[0m"
CYAN = "\033[38;2;0;217;255m"
SILVER = "\033[38;2;195;202;212m"
GREEN = "\033[38;2;0;255;102m"
RED = "\033[38;2;255;69;69m"
GRAY = "\033[38;2;181;181;181m"
WHITE = "\033[38;2;255;255;255m"


# Messages
def info(message):
    print(f"{GRAY}[*] {message}{RESET}")


def success(message):
    print(f"{GREEN}[+] {message}{RESET}")


def error(message):
    print(f"{RED}[-] {message}{RESET}")


def prompt(message):
    return input(f"{CYAN}{message}{RESET} ").strip()


def get_target(message):
    target = prompt(message)

    if target == "":
        error("Input cannot be empty.")
        return None

    return target


# Startup header
def show_header():
    print()
    print(f"{CYAN}  S I N X T E C Z{RESET}")
    print(f"{SILVER}  NETWORK SECURITY TOOLKIT{RESET}")
    print(f"{GRAY}  {'-' * 40}{RESET}")

    print(f"{CYAN}  Initializing console", end="", flush=True)

    for _ in range(3):
        time.sleep(0.18)
        print(".", end="", flush=True)

    print(f" {GREEN}READY{RESET}")
    print(f"{GRAY}  Cross-platform network diagnostics{RESET}")
    print(f"{GRAY}  {'-' * 40}{RESET}")
    print()


# Dependency display
def show_dependency(name, available):
    if available:
        print(f"{GREEN}●{RESET} {name}")
    else:
        print(f"{RED}●{RESET} {name}")


def show_dependency_report(found, missing):
    print()
    print(f"{GRAY}Available: {GREEN}{found}{GRAY} | Missing: {RED}{missing}{RESET}")


# Main menu
def show_menu():
    print(f"""
{CYAN}  SINXTECZ TOOLKIT{RESET}
{GRAY}  {'-' * 30}{RESET}

  {SILVER}NETWORK SCANNING{RESET}
  {GREEN}[★]{RESET} Nmap
   {GREEN}├[1.0]{RESET} Aggressive Scan
   {GREEN}├[1.1]{RESET} TCP Connect Scan
   {GREEN}├[1.2]{RESET} Common Ports Scan
   {GREEN}├[1.3]{RESET} SYN Scan
   {GREEN}└[1.4]{RESET} Service Detection
  
  {SILVER}GENERAL NETWORKING{RESET}
  {GREEN}[2]{RESET} Ping
  {GREEN}[3]{RESET} DNS Lookup
  {GREEN}[4]{RESET} WHOIS Lookup
  {GREEN}[5]{RESET} Traceroute

  {SILVER}IP INFORMATION{RESET}
  {GREEN}[6]{RESET} Private IP
  {GREEN}[7]{RESET} Public IP

  {RED}[0]{RESET} Exit
""")
