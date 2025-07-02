# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/summarizer.py
# Purpose: Lazy-loaded summarizer with dynamic length safeguards
# Tier: ΩΩΩ — Controlled Compression for Reflexive Input Streams
# ============================================================

from transformers import pipeline
import threading

class LazySummarizer:
    def __init__(self):
        self.model_loaded = False
        self.summarizer = None
        threading.Thread(target=self._load_model).start()

    def _load_model(self):
        try:
            print("📦 [SUMMARIZER] Loading summarizer model in background...")
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.model_loaded = True
            print("✅ [SUMMARIZER] Model ready.")
        except Exception as e:
            print(f"❌ [SUMMARIZER] Failed to load model: {e}")

    def summarize(self, text):
        if not self.model_loaded or not text:
            return text[:200]
        try:
            # === Dynamic guard to avoid Hugging Face warnings ===
            max_len = min(100, max(16, len(text.split()) * 2))
            return self.summarizer(
                text,
                max_length=max_len,
                min_length=8,
                do_sample=False
            )[0]['summary_text']
        except Exception as e:
            print(f"⚠️ [SUMMARIZER] Error during summarization: {e}")
            return text[:200]

# === Global instance ===
summarizer = LazySummarizer()