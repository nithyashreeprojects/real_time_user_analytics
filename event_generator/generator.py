import time
import random
import requests
from datetime import datetime, timezone

INGEST_URL = "http://ingest-service:8000/ingest"

USERS = ["u101", "u102", "u103", "u104"]
EVENTS = ["click", "page_view", "scroll"]
PAGES = ["/home", "/product", "/cart"]
DEVICES = ["mobile", "desktop"]

while True:
    event = {
        "user_id": random.choice(USERS),
        "event_type": random.choice(EVENTS),
        "page": random.choice(PAGES),
        "device": random.choice(DEVICES),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    try:
        r = requests.post(INGEST_URL, json=event, timeout=5)
        print("Sent:", event, "| Status:", r.status_code)
    except Exception as e:
        print("Error sending event:", e)

    time.sleep(2)  
