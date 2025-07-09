# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: utils/safe_fetch.py
# Tier: Reflex Utility — HTTP Fetch Hardening for AGI Agents
# Purpose: Gracefully fetch external URLs and avoid 404/timeout failures
# ============================================================

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; TexBot/1.0; +https://tex.agi)"
}

def safe_fetch(url: str, timeout: int = 5) -> dict:
    """
    Safely fetch a URL and return structured response.
    Returns:
        {
            'success': bool,
            'status_code': int,
            'content': str or None,
            'error': str or None,
            'url': str
        }
    """
    if not url or not url.startswith("http"):
        return {
            "success": False,
            "status_code": None,
            "content": None,
            "error": "invalid_url",
            "url": url
        }

    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        if response.status_code == 200:
            return {
                "success": True,
                "status_code": 200,
                "content": response.text,
                "error": None,
                "url": url
            }
        else:
            # Comment out the noisy log line below
            # print(f"❌ [FETCH FAILED] {url} → HTTP {response.status_code}")
            return {
                "success": False,
                "status_code": response.status_code,
                "content": None,
                "error": f"http_{response.status_code}",
                "url": url
            }

    except Exception as e:
        # Comment out the noisy log line below
        # print(f"❌ [FETCH ERROR] {url} → {str(e)}")
        return {
            "success": False,
            "status_code": None,
            "content": None,
            "error": str(e),
            "url": url
        }