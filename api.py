import requests

TIMEOUT = 30

def send_request(url, payload, token=None):
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=TIMEOUT
    )
