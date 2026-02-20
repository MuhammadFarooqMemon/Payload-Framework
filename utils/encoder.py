import urllib.parse
import base64


def encode_payload(payload, encoding_type):

    if encoding_type == "url":
        return urllib.parse.quote(payload)

    elif encoding_type == "base64":
        return base64.b64encode(payload.encode()).decode()

    elif encoding_type == "hex":
        return payload.encode().hex()

    else:
        return payload
