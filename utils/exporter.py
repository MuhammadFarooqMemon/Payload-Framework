import json
import os


def export(payloads, format_type):
    """
    Export payloads to file.
    """

    os.makedirs("samples", exist_ok=True)

    if format_type == "json":
        with open("samples/payloads.json", "w") as f:
            json.dump(payloads, f, indent=4)

        print("Exported to samples/payloads.json")

    elif format_type == "txt":
        with open("samples/payloads.txt", "w") as f:
            for p in payloads:
                f.write(p + "\n")

        print("Exported to samples/payloads.txt")
