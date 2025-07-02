# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/urgency_classifier.py
# Purpose: Classify and score urgency levels from real-time data
# Tier: Omega Precision Heuristic + LLM-aware
# ============================================================

import re

# === Hardcoded urgency trigger keywords (expandable) ===
HIGH_URGENCY = [
    "breaking", "crash", "defaults", "collapse", "urgent", "immediate", "emergency",
    "bankruptcy", "evacuation", "explosion", "lawsuit", "rate hike", "rate cut", "inflation spikes",
    "mass layoffs", "defaults", "shutdown", "AI ban", "override", "hacked"
]

MEDIUM_URGENCY = [
    "volatility", "inflation", "market shift", "fed", "warning", "lawsuit", "merger",
    "rate decision", "earnings report", "CPI", "SEC", "unemployment", "devaluation"
]

LOW_URGENCY = [
    "preview", "commentary", "forecast", "projection", "analyst", "review", "opinion",
    "future trend", "comment", "reaction", "slowdown"
]


def compute_urgency_score(text: str) -> float:
    """Assign a heuristic urgency score (0.0 - 1.0) based on keywords in title/summary."""
    if not text or len(text.strip()) < 5:
        return 0.1  # Default low urgency

    lowered = text.lower()

    high_hits = sum(1 for word in HIGH_URGENCY if word in lowered)
    medium_hits = sum(1 for word in MEDIUM_URGENCY if word in lowered)
    low_hits = sum(1 for word in LOW_URGENCY if word in lowered)

    # === Base scoring logic ===
    score = 0.1
    score += high_hits * 0.3
    score += medium_hits * 0.15
    score += low_hits * 0.05

    # === Cap and normalize ===
    return min(score, 1.0)


# === Optional: Regex urgency booster ===
def contains_time_sensitivity(text: str) -> bool:
    time_patterns = [
        r"\bthis (week|month|quarter|year)\b",
        r"\bnext (hour|day|week|quarter)\b",
        r"\btoday\b", r"\bimmediately\b", r"\bnow\b", r"\bdeadline\b"
    ]
    return any(re.search(pattern, text.lower()) for pattern in time_patterns)


def enhanced_urgency_score(text: str) -> float:
    """Boost score if time-sensitive regex is matched."""
    base = compute_urgency_score(text)
    if contains_time_sensitivity(text):
        base += 0.1
    return min(base, 1.0)