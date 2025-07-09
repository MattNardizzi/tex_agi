import hashlib
import json

def sign_reflex(reflex_data: dict) -> str:
    canonical = json.dumps(reflex_data, sort_keys=True, separators=(',', ':'))
    signature = hashlib.sha256(canonical.encode('utf-8')).hexdigest()
    return signature