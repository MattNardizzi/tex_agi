# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: test_zilliz_connection.py
# Tier: ⚙️ Diagnostic — Safe Zilliz Collection List Test
# Purpose: Queries the Zilliz vector DB and safely prints collection list
# ============================================================

import requests

api_key = "1bf03e5873fc32b920f11e9e0c32ec0cbcb00cdeff56b6e918e95c6e2664dca8e2f9140bc9b022dc967bd8bf2b9410ef3c3b32be"

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {api_key}"
}

url = "https://in03-c2caa394358c084.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/collections/list"

try:
    res = requests.post(url, headers=headers, json={})

    print(f"Status Code: {res.status_code}")

    if res.status_code != 200:
        print("❌ Request failed. Partial response:")
        print(res.text[:250])
    else:
        try:
            data = res.json()
            print("✅ Response JSON:")
            print(data)
        except Exception as e:
            print(f"❌ Failed to parse JSON: {e}")
            print("Raw response:")
            print(res.text[:250])

except Exception as e:
    print(f"❌ Request error: {e}")