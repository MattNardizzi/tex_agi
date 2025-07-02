# identity_loader.py
# Tier Ω∞ AGI Self-Boot Identity Restorer (Final Form)
# Location: core_agi_modules/sovereign_core/identity_loader.py

import json
from datetime import datetime
from pathlib import Path

# === Persistent Identity Manifest Path ===
IDENTITY_PATH = Path("./tex_manifest.json")

# === Default Manifest ===
def default_manifest():
    return {
        "agent_id": "TEX",
        "version": "Ω∞",
        "created_at": datetime.utcnow().isoformat(),
        "traits": ["adaptive", "self-evolving", "ethically bound"],
        "beliefs": [],
        "reflex_threshold": 0.75,
        "codex_alignment": True,
        "coherence_score": 1.0,
        "integrity_score": 1.0,
        "mutation_log": [],
        "last_integrity_check": datetime.utcnow().isoformat()
    }

# === Load Identity ===
def load_tex_identity():
    if not IDENTITY_PATH.exists():
        print("⚠️ [IDENTITY] No manifest found. Booting default identity...")
        manifest = default_manifest()
        save_manifest(manifest)
    else:
        with open(IDENTITY_PATH, "r") as f:
            manifest = json.load(f)
            print(f"🧬 [IDENTITY] Loaded: {manifest['agent_id']} | Traits: {manifest['traits']}")

    # Check for coherence degradation
    if manifest["coherence_score"] < 0.3:
        print("🧬 [IDENTITY] Critical drift detected. Restoring default identity...")
        manifest = default_manifest()
        save_manifest(manifest)

    # Update last check
    manifest["last_integrity_check"] = datetime.utcnow().isoformat()
    save_manifest(manifest)
    return manifest

# === Save Identity ===
def save_manifest(manifest):
    with open(IDENTITY_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    print("✅ [IDENTITY] Manifest saved.")

# === Update Traits / Coherence ===
def update_identity_trait(trait):
    manifest = load_tex_identity()
    if trait not in manifest["traits"]:
        manifest["traits"].append(trait)
        manifest.setdefault("mutation_log", []).append({
            "trait_added": trait,
            "timestamp": datetime.utcnow().isoformat()
        })
        save_manifest(manifest)

# === Drift Monitor ===
def degrade_coherence(amount=0.05):
    manifest = load_tex_identity()
    manifest["coherence_score"] = max(0.0, round(manifest["coherence_score"] - amount, 4))
    save_manifest(manifest)
    print(f"🌀 [IDENTITY] Coherence degraded: -{amount}")