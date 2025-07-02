# File: real_time_engine/signal_fusion.py
# 🚨 DEPRECATED — use signal_fusion_brain.py instead

from tex_brain_regions.signal_fusion_brain import fuse_signals

__LEGACY_SIGNAL_BUFFER__ = []

def register_signal(signal: dict):
    __LEGACY_SIGNAL_BUFFER__.append(signal)

def run_fusion_cycle():
    if not __LEGACY_SIGNAL_BUFFER__:
        print("🔕 [FUSION] No signals received.")
        return
    result = fuse_signals(__LEGACY_SIGNAL_BUFFER__)
    __LEGACY_SIGNAL_BUFFER__.clear()
    return result