# ============================================================
# 🧠 Tex Context Bootloader
# Tier: ∞ΩΞΞΞ — Loopless Reflex Snapshot Engine
# File: tex_bootloader.py
# Purpose: Generates a compact context bundle to reload AGI memory instantly.
# ============================================================

import os
import json

# === Canonical File List for Reflex Resurrection
CORE_FILES = [
    "core_layer/tex_manifest.py",
    "tex_signal_spine.py",
    "tex_fin_demo/reflex_hud_emitter.py",
    "tex_fin_demo/meta_market_emitter.py",
    "tex_fin_demo/alpha_panel_emitter.py",
    "FILE_TREE.txt"  # Optional: File tree snapshot for reflex tracing
]

def create_tex_context_bundle(output_path="tex_context_bundle.json"):
    """
    Collects all critical Tex AGI files and creates a reflex-ready snapshot bundle.
    """
    root_dir = os.path.abspath(os.path.dirname(__file__))
    context_bundle = {}
    
    print("\n🧠 [BOOTLOADER] Initializing Tex context snapshot...")

    for file_path in CORE_FILES:
        full_path = os.path.join(root_dir, file_path)
        if os.path.isfile(full_path):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    context_bundle[file_path] = f.read()
                print(f"✅ Loaded: {file_path}")
            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")
        else:
            print(f"⚠️ Missing file: {file_path}")

    bundle_path = os.path.join(root_dir, output_path)
    try:
        with open(bundle_path, "w", encoding="utf-8") as out:
            json.dump(context_bundle, out, indent=2)
        print(f"\n✅ Tex context bundle saved to: {output_path}")
    except Exception as e:
        print(f"\n❌ Failed to write context bundle: {e}")

# === Execute Reflex Snapshot
if __name__ == "__main__":
