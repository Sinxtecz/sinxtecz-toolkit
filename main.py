
import ipaddress
import platform
import shutil
import subprocess
import ui


# Check dependencies
def check_dependencies():
    system = platform.system()

    if system not in ("Windows", "Linux"):
        ui.error(f"Unsupported operating system: {system}")
        return

    tools = {
        "Nmap": ["nmap"],
        "WHOIS": ["whois.exe", "whois"],
        "DNS Lookup": ["nslookup"],
        "Traceroute": (
            ["tracert"] if system == "Windows"
            else ["traceroute"]
        ),
        "Ping": ["ping"],
        "Public IP (curl)": ["curl"],
    }

    found = 0
    missing = 0

    print(f"{ui.CYAN}DEPENDENCIES{ui.RESET}")

    for name, commands in tools.items():
        available = any(
            shutil.which(command) for command in commands
        )

        ui.show_dependency(name, available)

        if available:
            found += 1
        else:
            missing += 1

    ui.show_dependency_report(found, missing)


# Run a system command
def run_command(command, success_message, timeout=300):
    try:
        result = subprocess.run(command, timeout=timeout)

        if result.returncode == 0:
            ui.success(success_message)
        else:
            ui.error(
                f"Command failed with exit code "
                f"{result.returncode}."
            )

    except subprocess.TimeoutExpired:
        ui.error(f"Command timed out after {timeout} seconds.")

    except FileNotFoundError:
        ui.error(f"Command not found: {command[0]}")

    except PermissionError:
        ui.error("Permission denied.")

    except OSError as exception:
        ui.error(f"Could not run command: {exception}")


# Nmap tools
class Nmap:

    @staticmethod
    def aggressive(target):
        ui.info(f"Aggressive scan: {target}")
        run_command(
            ["nmap", "-A", "-T3", "--reason", target],
            "Aggressive scan finished."
        )

    @staticmethod
    def common_ports(target):
        ui.info(f"Common ports scan: {target}")
        run_command(
            [
                "nmap", "-sT", "-T3",
                "--top-ports", "100",
                "--reason",target,
            ],
            "Common ports scan finished."
        )

    @staticmethod
    def tcp_scan(target):
        ui.info(f"TCP connect scan: {target}")
        run_command(
            ["nmap", "-sT", "-T3", "--reason", target],
            "TCP connect scan finished."
        )

    @staticmethod
    def syn_scan(target):
        ui.info(f"SYN scan: {target}")
        ui.info(
            "NOTE: SYN scans may require administrator/root "
            "privileges. If the scan fails, try running "
            "SINXTECZ with the required permissions."
        )
        run_command(
            ["nmap", "-sS", "-T3", "--reason", target],
            "SYN scan finished."
        )

    @staticmethod
    def service_scan(target):
        ui.info(f"Service detection scan: {target}")
        run_command(
            [
                "nmap", "-sV", "--version-light",
                "-T3", "--reason", target,
            ],
            "Service detection finished."
        )


# Other network tools
class Scan:

    @staticmethod
    def ping(target):
        system = platform.system()
        ui.info(f"Pinging {target}")

        if system == "Windows":
            command = ["ping", "-n", "4", target]
        elif system == "Linux":
            command = ["ping", "-c", "4", target]
        else:
            ui.error(f"Unsupported OS: {system}")
            return

        run_command(command, "Ping finished.", timeout=30)

    @staticmethod
    def dns(domain):
        record_types = {
            "1": ("A", "IPv4 address"),
            "2": ("AAAA", "IPv6 address"),
            "3": ("MX", "Mail servers"),
            "4": ("NS", "Name servers"),
            "5": ("TXT", "Text records"),
            "6": ("CNAME", "Canonical name"),
            "7": ("ALL", "Basic lookup"),
        }

        ui.info(f"DNS lookup: {domain}")
        print(f"\n{ui.CYAN}DNS RECORD TYPES{ui.RESET}")
        print("1. A     - IPv4 address")
        print("2. AAAA  - IPv6 address")
        print("3. MX    - Mail servers")
        print("4. NS    - Name servers")
        print("5. TXT   - Text records")
        print("6. CNAME - Canonical name")
        print("7. ALL   - Basic lookup")

        choice = ui.prompt("Select record type:")

        if choice not in record_types:
            ui.error("Invalid DNS record type.")
            return

        record, description = record_types[choice]
        ui.info(f"Querying {record} ({description}): {domain}")

        if record == "ALL":
            command = ["nslookup", domain]
        else:
            command = ["nslookup", f"-type={record}", domain]

        run_command(
            command,
            f"DNS {record} lookup finished.",
            timeout=30,
        )

    @staticmethod
    def trace(target):
        system = platform.system()

        if system == "Windows":
            command = [
                "tracert", "-h", "20", "-w", "1000", target
            ]
        elif system == "Linux":
            command = [
                "traceroute", "-m", "20", "-w", "1", target
            ]
        else:
            ui.error(f"Unsupported OS: {system}")
            return

        ui.info(f"Tracing route to {target}")
        ui.info("Maximum hops: 20 | Per-hop timeout: 1 second")

        run_command(
            command,
            "Traceroute finished.",
            timeout=90,
        )

    @staticmethod
    def whois():
        domain = ui.get_target("Enter domain or IP:")

        if not domain or not domain.strip():
            ui.error("No domain or IP provided.")
            return

        domain = domain.strip()

        command = (
            shutil.which("whois.exe")
            or shutil.which("whois")
        )

        if command is None:
            ui.error("WHOIS is not installed or not in PATH.")
            return

        ui.info(f"WHOIS lookup: {domain}")

        try:
            result = subprocess.run(
                [command, domain],
                capture_output=True,
                text=True,
                timeout=30,
            )

            output = result.stdout.strip()
            errors = result.stderr.strip()

            if output:
                print(f"{ui.WHITE}{output}{ui.RESET}")

            if result.returncode == 0:
                if output:
                    ui.success("WHOIS lookup finished.")
                else:
                    ui.error("WHOIS returned no output.")
            elif errors:
                ui.error(f"WHOIS error: {errors}")
            else:
                ui.error(
                    f"WHOIS command returned exit code "
                    f"{result.returncode}."
                )

        except subprocess.TimeoutExpired:
            ui.error("WHOIS request timed out after 30 seconds.")

        except OSError as exception:
            ui.error(f"WHOIS failed: {exception}")


# IP information tools
class IP:

    @staticmethod
    def private():
        system = platform.system()

        if system == "Windows":
            command = ["ipconfig"]
        elif system == "Linux":
            command = ["ip", "-brief", "address"]
        else:
            ui.error(f"Unsupported OS: {system}")
            return

        ui.info("Getting local network information...")
        run_command(
            command,
            "IP information displayed.",
            timeout=30,
        )

    @staticmethod
    def public():
        ui.info("Getting public IP...")

        try:
            result = subprocess.run(
                [
                    "curl",
                    "--fail",
                    "--silent",
                    "--show-error",
                    "--max-time", "15",
                    "https://api.ipify.org",
                ],
                capture_output=True,
                text=True,
                check=True,
                timeout=20,
            )

            public_ip = result.stdout.strip()

            if not public_ip:
                ui.error("Empty response from IP service.")
                return

            try:
                ipaddress.ip_address(public_ip)
            except ValueError:
                ui.error("IP service returned an invalid IP address.")
                return

            ui.success(f"Public IP: {public_ip}")

        except subprocess.TimeoutExpired:
            ui.error("Public IP request timed out.")

        except subprocess.CalledProcessError as exception:
            details = (exception.stderr or "").strip()

            if details:
                ui.error(f"Public IP request failed: {details}")
            else:
                ui.error("Public IP request failed.")

        except FileNotFoundError:
            ui.error("curl is not installed or not in PATH.")

        except OSError as exception:
            ui.error(f"Could not retrieve public IP: {exception}")


# Main program
def main():
    ui.show_header()
    check_dependencies()

    input(
        f"\n{ui.GRAY}Press ENTER to open the menu...{ui.RESET}"
    )

    while True:
        ui.show_menu()
        choice = ui.prompt("SINXTECZ >")

        if choice in ("1.0", "1.1", "1.2", "1.3", "1.4"):
            target = ui.get_target(
                "Enter authorized target IP/domain:"
            )

            if not target or not target.strip():
                ui.error("No target provided.")
            else:
                target = target.strip()

                nmap_actions = {
                    "1.0": Nmap.aggressive,
                    "1.1": Nmap.tcp_scan,
                    "1.2": Nmap.common_ports,
                    "1.3": Nmap.syn_scan,
                    "1.4": Nmap.service_scan,
                }

                nmap_actions[choice](target)

        elif choice == "2":
            target = ui.get_target("Enter host to ping:")

            if not target or not target.strip():
                ui.error("No target provided.")
            else:
                Scan.ping(target.strip())

        elif choice == "3":
            domain = ui.get_target("Enter domain:")

            if not domain or not domain.strip():
                ui.error("No domain provided.")
            else:
                Scan.dns(domain.strip())

        elif choice == "4":
            Scan.whois()

        elif choice == "5":
            target = ui.get_target("Enter destination:")

            if not target or not target.strip():
                ui.error("No destination provided.")
            else:
                Scan.trace(target.strip())

        elif choice == "6":
            IP.private()

        elif choice == "7":
            IP.public()

        elif choice == "0":
            ui.success("Exiting SINXTECZ.")
            break

        else:
            ui.error("Invalid option. Check the menu.")

        input(
            f"\n{ui.GRAY}Press ENTER to continue...{ui.RESET}"
        )


if __name__ == "__main__":
    main()
