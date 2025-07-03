import requests

api_key = "1bf03e5873fc32b920f11e9e0c32ec0cbcb00cdeff56b6e918e95c6e2664dca8e2f9140bc9b022dc967bd8bf2b9410ef3c3b32be"

headers = {
    "accept": "application/json",
    "authorization": f"Bearer {api_key}"
}

url = "https://in03-c2caa394358c084.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/collections/list"

res = requests.post(url, headers=headers, json={})

print(f"Status Code: {res.status_code}")
print("Response JSON:")
print(res.json())