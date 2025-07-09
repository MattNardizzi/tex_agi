import requests
import json
import os

ABLY_KEY = "F2g01g.ddRLDw:fy6tMR2WO3nqMQ9FABYtNjrtGYW_rhpAEyEV_B8NAXI"

def broadcast_update(channel_name, event_type, payload=None):
    try:
        response = requests.post(
            f"https://rest.ably.io/channels/{channel_name}/messages",
            headers={ "Content-Type": "application/json" },
            auth=(ABLY_KEY.split(":")[0], ABLY_KEY.split(":")[1]),
            data=json.dumps({
                "name": event_type,
                "data": payload or {}
            })
        )
        print(f"📡 Ably HTTP Broadcast → {channel_name} :: {event_type} | Code: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"❌ [ABLY HTTP ERROR] {e}")