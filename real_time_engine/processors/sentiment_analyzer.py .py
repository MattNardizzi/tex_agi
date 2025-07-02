# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/sentiment_analyzer.py
# Purpose: Classify sentiment from incoming signals using transformer or heuristics
# Tier: Hybrid Signal AI + Rule-based fallback
# ============================================================

import re
from transformers import pipeline

# === Lazy load transformer sentiment classifier ===
class SentimentAnalyzer:
    def __init__(self):
        self.model_loaded = False
        self._init_pipeline()

    def _init_pipeline(self):
        try:
            print("[📦] Loading sentiment classifier...")
            self.classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
            self.model_loaded = True
            print("[✅] Sentiment model ready.")
        except Exception as e:
            print(f"[⚠️] Transformer fallback due to: {e}")
            self.model_loaded = False
            self.classifier = None

    def classify_sentiment(self, text: str) -> str:
        if not text or len(text.strip()) < 5:
            return "neutral"

        if self.model_loaded:
            try:
                result = self.classifier(text[:512])[0]
                label = result["label"]
                if label == "NEGATIVE":
                    return "negative"
                elif label == "POSITIVE":
                    return "positive"
                else:
                    return "neutral"
            except Exception as e:
                print(f"[⚠️] Sentiment model error: {e}")
                return fallback_sentiment(text)
        else:
            return fallback_sentiment(text)


# === Rule-based fallback ===
NEGATIVE_TERMS = [
    "crash", "down", "collapse", "loss", "sell-off", "layoff", "bankrupt", "fraud", "investigation",
    "decline", "cuts", "defaults", "unrest", "conflict", "warning", "fired", "downgrade", "scandal"
]

POSITIVE_TERMS = [
    "surge", "rise", "growth", "profit", "buyback", "upgrade", "beat", "recovery", "rally",
    "record high", "strong", "boom", "win", "approval", "hire", "expansion"
]

def fallback_sentiment(text: str) -> str:
    text_lower = text.lower()

    if any(word in text_lower for word in NEGATIVE_TERMS):
        return "negative"
    elif any(word in text_lower for word in POSITIVE_TERMS):
        return "positive"
    else:
        return "neutral"


# === Singleton instance for shared use ===
analyzer = SentimentAnalyzer()