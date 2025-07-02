# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/utils/memory_utils.py
# Purpose: Safe dictionary access for memory entries
# ============================================================

def safe_get(entry, key, default=None):
    """
    Safely get a key from a dictionary.
    Returns default if entry is not a dict.
    """
    if isinstance(entry, dict):
        return entry.get(key, default)
    return default

def safe_nested_get(entry, *keys, default=None):
    """
    Safely access nested keys in a dictionary.
    Usage: safe_nested_get(entry, "data", "emotion", default="neutral")
    """
    for key in keys:
        if not isinstance(entry, dict):
            return default
        entry = entry.get(key, default)
    return entry

def clean_text(thought):
    """
    Normalize thought input to a clean string.
    Handles list, str, or other types gracefully.
    """
    if isinstance(thought, list):
        return " ".join(thought).strip()
    if isinstance(thought, str):
        return thought.strip()
    return str(thought).strip()