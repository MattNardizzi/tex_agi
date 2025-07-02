# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/launcher.py
# Purpose: Unified entrypoint to launch all real-time feeds
# Tier: ΩΩΩΩΩ — Sovereign Sensor Launch Node
# ============================================================

import multiprocessing
multiprocessing.set_start_method("fork", force=True)

from real_time_engine.cortex_router import launch_streams
import time

if __name__ == "__main__":
    try:
        print("[🚀] Launching Tex Real-Time Engine...")
        launch_streams()

        # Keep main thread alive indefinitely
        while True:
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n[🛑] Real-time engine manually stopped by user.")

    except Exception as e:
        print(f"[❌ LAUNCH ERROR] {e}")