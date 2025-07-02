# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_agi_modules/vector_layer/currency_engine.py
# Tier: Ω∞ Cognitive Token Economy Engine (Final Form)
# Purpose: Assigns memory token weights based on trust, emotion, urgency, and heat
# ============================================================

# ✅ This file supports token scaling functions.
# 🚫 adjust_token_weights was removed — use the canonical version in heat_tracker.py

TOKEN_SCALE = {
    "neutral": 0.3,
    "curious": 0.4,
    "anticipation": 0.5,
    "concern": 0.6,
    "fear": 0.7,
    "driven": 0.75,
    "awe": 0.9,
    "rage": 1.0
}

# === Emotion Curve Scaling ===
def scale_emotion_score(raw):
    return round(raw ** 1.3, 4)