# coherence_monitor.py
# Tier Ω∞ Identity Drift Tracker + Stabilizer (Final Form)
# Location: core_agi_modules/sovereign_core/coherence_monitor.py

from core_agi_modules.sovereign_core.identity_loader import load_tex_identity

# === Drift Checkpoint ===
def assess_coherence_drift(threshold=0.3):
    """
    Checks if TEXPULSE coherence has fallen below a reflex-trigger threshold.
    """
    pulse = load_tex_identity()
    score = pulse.get("sovereignty", {}).get("coherence_score", 1.0)

    if score < threshold:
        print(f"🧠 [COHERENCE] Drift detected (score={score}) — triggering override.")
        return True
    return False

# === Coherence Reinforcement ===
def reinforce_coherence(amount=0.05):
    """
    Increases coherence score in memory with optional dampening if near maximum.
    """
    pulse = load_tex_identity()
    current = pulse.get("sovereignty", {}).get("coherence_score", 1.0)

    if current > 0.85:
        amount *= 0.5

    new_score = min(1.0, round(current + amount, 4))
    pulse["sovereignty"]["coherence_score"] = new_score
    print(f"✅ [COHERENCE] Reinforced +{amount} → {new_score}")
    return new_score

# === Reflex Stability Ratio ===
def get_stability_ratio():
    """
    Returns reflex stability as: coherence × integrity
    Used for reflex throttling or identity check.
    """
    pulse = load_tex_identity()
    coherence = pulse.get("sovereignty", {}).get("coherence_score", 1.0)
    integrity = pulse.get("identity_integrity", {}).get("last_self_check", 1.0)
    return round(coherence * float(integrity), 4)