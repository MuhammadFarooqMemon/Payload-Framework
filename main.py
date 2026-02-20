#!/usr/bin/env python3
"""
ITSOLERA (PVT) LTD
Offensive Security Tool Development – Payload Generation Framework

Educational Payload Generator
For Authorized Labs & Defensive Research Only

Aligned With:
- OWASP Testing Guide
- OWASP Code of Ethics
"""

import argparse
import sys
from colorama import Fore, init

from modules import xss, sqli, cmdi
from utils import encoder, exporter

init(autoreset=True)

# ===============================
# Banner
# ===============================
BANNER = r"""
███╗   ███╗██╗███╗   ██╗██╗
████╗ ████║██║████╗  ██║██║
██╔████╔██║██║██╔██╗ ██║██║
██║╚██╔╝██║██║██║╚██╗██║██║
██║ ╚═╝ ██║██║██║ ╚████║██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝

MINI SECURITY RESEARCH FRAMEWORK
(Educational / Authorized Lab Use Only)
"""
# ==========================================================
# Plugin Registry
# ==========================================================
PLUGINS = {
    "xss": xss.generate,
    "sqli": sqli.generate,
    "cmdi": cmdi.generate
}


# ==========================================================
# Defensive Notes (Bonus Requirement)
# ==========================================================
def defensive_notes(module):
    print(Fore.CYAN + "\n[Defensive Insights]")
    if module == "xss":
        print("- Use output encoding (HTML, JS context aware).")
        print("- Enable Content Security Policy (CSP).")
        print("- Sanitize user input properly.")
        print("- Modern WAFs detect script tags & event handlers.")
    elif module == "sqli":
        print("- Use parameterized queries (Prepared Statements).")
        print("- Disable verbose DB error messages.")
        print("- Use ORM frameworks.")
        print("- WAF detects UNION / OR 1=1 patterns.")
    elif module == "cmdi":
        print("- Use strict input validation.")
        print("- Avoid system() calls with user input.")
        print("- Apply whitelisting instead of blacklisting.")
        print("- Use sandboxed execution environments.")
    print()


# ==========================================================
# Encoding Wrapper
# ==========================================================
def apply_encoding(payloads, encoding_type):
    if not encoding_type:
        return payloads

    encoded_list = []
    for p in payloads:
        encoded_list.append(encoder.encode_payload(p, encoding_type))
    return encoded_list


# ==========================================================
# Burp / ZAP Export Simulation (BONUS)
# ==========================================================
def export_for_burp(payloads):
    filename = "burp_payloads.txt"
    with open(filename, "w") as f:
        for p in payloads:
            f.write(p + "\n")
    print(Fore.GREEN + f"[+] Burp Suite payload list exported to {filename}")


def export_for_zap(payloads):
    filename = "zap_payloads.txt"
    with open(filename, "w") as f:
        for p in payloads:
            f.write(p + "\n")
    print(Fore.GREEN + f"[+] OWASP ZAP payload list exported to {filename}")


# ==========================================================
# Payload Viewer
# ==========================================================
def show_payloads(module, db=None, encoding=None, output=None, burp=False, zap=False):

    if module not in PLUGINS:
        print("Invalid module selected.")
        return

    # SQLi needs DB selection
    if module == "sqli":
        payloads = PLUGINS[module](db)
    else:
        payloads = PLUGINS[module]()

    payloads = apply_encoding(payloads, encoding)

    print(Fore.YELLOW + f"\nTotal Payloads Generated: {len(payloads)}\n")

    # Display
    for i, p in enumerate(payloads, 1):
        print(f"[{i}] {p}")

    # Export formats
    if output:
        exporter.export(payloads, output)

    # Bonus exports
    if burp:
        export_for_burp(payloads)

    if zap:
        export_for_zap(payloads)

    defensive_notes(module)


# ==========================================================
# Interactive Menu Mode
# ==========================================================
def interactive_mode():

    print(Fore.RED + BANNER)

    print("""
[1] XSS Payload Templates
[2] SQL Injection Templates
[3] Command Injection Patterns
[0] Exit
""")

    choice = input("Select Module: ").strip()

    if choice == "0":
        sys.exit()

    module_map = {"1": "xss", "2": "sqli", "3": "cmdi"}
    module = module_map.get(choice)

    if not module:
        print("Invalid option.")
        return

    db = None
    if module == "sqli":
        db = input("Select DB (mysql/postgres/mssql): ").lower()

    encoding = input("Encoding (url/base64/hex or Enter to skip): ").lower()
    encoding = encoding if encoding else None

    fmt = input("Export format (json/txt or Enter to skip): ").lower()
    fmt = fmt if fmt else None

    show_payloads(module, db=db, encoding=encoding, output=fmt)


# ==========================================================
# CLI Mode
# ==========================================================
def cli_mode():

    parser = argparse.ArgumentParser(
        description="Educational Payload Generation Framework"
    )

    parser.add_argument("--module", choices=["xss", "sqli", "cmdi"],
                        required=True)

    parser.add_argument("--db", choices=["mysql", "postgres", "mssql"],
                        help="Database type (for SQLi)")

    parser.add_argument("--encode", choices=["url", "base64", "hex"],
                        help="Encoding type")

    parser.add_argument("--output", choices=["json", "txt"],
                        help="Export format")

    parser.add_argument("--burp", action="store_true",
                        help="Export payloads for Burp Suite")

    parser.add_argument("--zap", action="store_true",
                        help="Export payloads for OWASP ZAP")

    args = parser.parse_args()

    show_payloads(
        module=args.module,
        db=args.db,
        encoding=args.encode,
        output=args.output,
        burp=args.burp,
        zap=args.zap
    )


# ==========================================================
# Main
# ==========================================================
def main():

    if len(sys.argv) == 1:
        interactive_mode()
    else:
        cli_mode()


if __name__ == "__main__":
    main()
