
import subprocess
import platform
import shutil


# ==================== COLORS ====================

RESET = "\033[0m"
SILVER = "\033[38;2;195;202;212m"
BRIGHT_SILVER = "\033[38;2;235;239;245m"
CYAN = "\033[38;2;0;217;255m"
GREEN = "\033[38;2;0;255;102m"
RED = "\033[38;2;255;69;69m"
YELLOW = "\033[38;2;255;209;102m"
GRAY = "\033[38;2;181;181;181m"
WHITE = "\033[38;2;255;255;255m"


def info(message):
    print(f"{GRAY}[*] {message}{RESET}")


def success(message):
    print(f"{GREEN}[+] {message}{RESET}")


def error(message):
    print(f"{RED}[-] {message}{RESET}")


def warning(message):
    print(f"{YELLOW}[!] {message}{RESET}")


def prompt(message):
    return input(f"{CYAN}{message}{RESET}").strip()


def run_command(command, success_message):
    try:
        result = subprocess.run(command)

        if result.returncode == 0:
            success(success_message)
        else:
            error(
                f"Command failed with exit code "
                f"{result.returncode}."
            )

    except FileNotFoundError:
        error(f"Command not found: {command[0]}")
        info("Check that the tool is installed and available in PATH.")

    except PermissionError:
        error("Permission denied while running the command.")

    except OSError as exception:
        error(f"Could not run command: {exception}")


# ==================== SCAN TOOLS ====================

class Scan:

    def aggressive(self, ip):
        info("Starting aggressive scan...")
        info(f"Target: {ip}")
        print()

        run_command(
            ["nmap", "-A", "-T4", ip],
            "Aggressive scan completed."
        )

    def syn_scan(self, ip):
        info("Starting SYN scan...")
        info(f"Target: {ip}")
        print()

        run_command(
            ["nmap", "-sS", "-T3", "--scan-delay", "500ms", ip],
            "SYN scan completed."
        )

    def ping(self, ip):
        info(f"Pinging {ip}...")
        print()

        if platform.system() == "Windows":
            command = ["ping", "-n", "4", ip]
        else:
            command = ["ping", "-c", "4", ip]

        run_command(command, "Ping command completed.")

    def dns(self, webpage):
        info(f"Looking up {webpage}...")
        print()

        run_command(
            ["nslookup", webpage],
            "DNS lookup completed."
        )

    def trace(self, ip):
        info(f"Tracing route to {ip}...")
        print()

        if platform.system() == "Windows":
            command = ["tracert", ip]
        else:
            command = ["traceroute", ip]

        run_command(command, "Traceroute completed.")

    def whois(self):
        domain = prompt("[+] Enter domain or IP: ")

        if not domain:
            error("Domain cannot be empty.")
            return

        if platform.system() == "Windows":
            command = (
                shutil.which("whois.exe")
                or shutil.which("whois")
            )
        else:
            command = shutil.which("whois")

        if command is None:
            error("WHOIS is not installed or not in PATH.")

            if platform.system() == "Windows":
                info("Install Microsoft Sysinternals WHOIS.")
                info("Add its folder to PATH.")
            else:
                info("Install using: sudo apt install whois")

            return

        info(f"Starting WHOIS lookup for {domain}...")
        print()

        try:
            result = subprocess.run(
                [command, domain],
                capture_output=True,
                text=True,
                timeout=30
            )

            output = result.stdout or result.stderr

            if output:
                print(f"{WHITE}{output}{RESET}")

            if result.returncode == 0:
                success("WHOIS lookup completed.")
            else:
                error("WHOIS command returned an error.")

        except subprocess.TimeoutExpired:
            error("WHOIS request timed out.")

        except (OSError, subprocess.SubprocessError) as exception:
            error(f"WHOIS failed: {exception}")


# ==================== IP TOOLS ====================

class IP:

    def private(self):
        info("Getting private IP information...")
        print()

        if platform.system() == "Windows":
            command = ["ipconfig"]
        else:
            command = ["ip", "addr"]

        run_command(command, "Private IP information displayed.")

    def public(self):
        info("Getting public IP...")
        print()

        try:
            result = subprocess.run(
                [
                    "curl",
                    "--max-time", "15",
                    "https://api.ipify.org"
                ],
                capture_output=True,
                text=True,
                check=True,
                timeout=20
            )

            public_ip = result.stdout.strip()

            if public_ip:
                print(f"{GREEN}[+] Public IP: {public_ip}{RESET}")
            else:
                error("The service returned an empty response.")

        except subprocess.TimeoutExpired:
            error("Public IP request timed out.")

        except subprocess.CalledProcessError:
            error("The public IP request failed.")

        except FileNotFoundError:
            error("curl is not installed or not available in PATH.")

        except OSError as exception:
            error(f"Could not retrieve public IP: {exception}")


# ==================== OBJECTS ====================

scan = Scan()
ip = IP()

_signature = "\x53\x49\x4e\x58\x54\x45\x43\x5a"


# ==================== MAIN PROGRAM ====================

# Metallic silver-gray logo
print(SILVER, end="", flush=True)

print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠃⠀⠀⠀⡁⠀⠀⠀⠀⠀⠐⠆⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢔⡤⠊⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠁⠀⠀⠘⠁⢀⠀⠀⠀⠀⢈⠓⠂⠠⡄⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠿⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠁⠀⠠⡚⠁⢀⣙⣀⣈⡩⠬⢁⠀⢑⠶⠤⡆⠤⡀⠀⠀⠀⠀⠀⠀⢀⠴⢲⣋⣽⣷⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢠⠀⠀⣶⠃⠗⣡⣶⣮⣿⡿⠿⠿⢿⣿⣷⣶⣤⣤⠤⠴⠦⠬⣤⣤⠄⣉⠉⠝⢲⣿⡷⠻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠁⡀⡸⠁⣰⣿⡿⠛⠋⣁⡀⠤⠤⢄⡀⠈⠛⢯⣿⣟⣾⣶⣶⣮⣭⣵⣾⣿⣟⠿⠉⢨⠖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢠⠳⡧⣻⡿⠋⢀⠒⠉⠀⠀⠀⠀⠀⠀⠉⠢⠀⠀⠙⠛⣻⣿⣿⣿⢿⣿⣿⠟⡱⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠂⢃⣸⣿⠇⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⠟⢿⠁⠸⡿⣿⣯⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢘⡄⠘⣿⣿⠀⠸⡀⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⡿⡟⡋⠐⡇⠀⢸⣿⣿⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠘⢰⣿⡿⡆⠀⣇⠀⣀⣠⣤⣶⣿⢷⢟⠻⠀⠈⠀⠀⠀⡇⠀⣼⣿⣿⠂⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢀⡴⢯⣾⠟⡏⢀⣠⣿⣿⣿⣟⢟⡋⠅⠘⠉⠀⠀⠀⠀⢀⠀⠁⢠⣿⣟⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⣻⣷⡿⢙⣩⣶⡿⠿⠛⠉⠑⢡⡁⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣾⣥⣾⢫⡦⠾⠛⠙⠉⠀⠀⢀⣀⠀⠈⠙⠓⠦⠤⠤⠀⠘⠁⢀⡤⣾⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠔⣴⣾⣿⣿⢟⢝⠢⠃⢀⣤⢴⣾⣮⣷⣶⢿⣶⡤⣐⡀⠀⣠⣤⢶⣪⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⣦⣾⡿⡛⠵⠺⢈⡠⠶⠿⠥⠥⡭⠉⠉⢱⡛⠻⠿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠭⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢴⠕⣋⠝⠕⠐⠀⠔⠉⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠁⠁⠁⠁⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣠⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

print(RESET, end="", flush=True)


# ==================== MENU ====================

while True:

    print(f"""{CYAN}
╭─「 𝙎𝙄𝙉𝙓𝙏𝙀𝘾𝙕 𝙏𝙊𝙊𝙇𝙆𝙄𝙏 」
│
├── Scan
│   ├── {GREEN}[1]{CYAN} Aggressive Scan
│   ├── {GREEN}[2]{CYAN} SYN Scan
│   ├── {GREEN}[3]{CYAN} Ping
│   ├── {GREEN}[4]{CYAN} DNS Lookup
│   ├── {GREEN}[5]{CYAN} WHOIS Lookup
│   └── {GREEN}[6]{CYAN} Traceroute
│
├── IP
│   ├── {GREEN}[7]{CYAN} Private IP
│   └── {GREEN}[8]{CYAN} Public IP
│
└── {RED}[0]{CYAN} Exit
{RESET}""")

    choice = prompt(">> ")

    if choice == "1":
        target = prompt("[+] Enter target IP/domain: ")

        if target:
            scan.aggressive(target)
        else:
            error("Target cannot be empty.")

    elif choice == "2":
        target = prompt("[+] Enter target IP/domain: ")

        if target:
            scan.syn_scan(target)
        else:
            error("Target cannot be empty.")

    elif choice == "3":
        target = prompt("[+] Enter target IP/domain: ")

        if target:
            scan.ping(target)
        else:
            error("Target cannot be empty.")

    elif choice == "4":
        domain = prompt("[+] Enter domain: ")

        if domain:
            scan.dns(domain)
        else:
            error("Domain cannot be empty.")

    elif choice == "5":
        scan.whois()

    elif choice == "6":
        target = prompt("[+] Enter target IP/domain: ")

        if target:
            scan.trace(target)
        else:
            error("Target cannot be empty.")

    elif choice == "7":
        ip.private()

    elif choice == "8":
        ip.public()

    elif choice == "0":
        success("Exiting SINXTECZ TOOLKIT...")
        break

    else:
        error("Invalid option. Choose a number from 0 to 8.")

    input(
        f"\n{GRAY}Press ENTER to return to menu...{RESET}"
    )

