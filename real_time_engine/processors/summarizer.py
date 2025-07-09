# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/summarizer.py
# Purpose: Lazy-loaded summarizer with dynamic length safeguards
# Tier: ΩΩΩ — Controlled Compression for Reflexive Input Streams
# ============================================================

import threading
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

class LazySummarizer:
    def __init__(self):
        self.model_loaded = False
        self.model = None
        self.tokenizer = None
        threading.Thread(target=self._load_model).start()

    def _load_model(self):
        try:
            print("📦 [SUMMARIZER] Loading summarizer model in background...")
            self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
            model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

            if hasattr(model, "to_empty"):
                model = model.to_empty(device="cpu")
            self.model = model.to("cpu")

            self.model_loaded = True
            print("✅ [SUMMARIZER] Model ready.")
        except Exception as e:
            print(f"❌ [SUMMARIZER] Failed to load model: {e}")

    def summarize(self, text: str) -> str:
        if not self.model_loaded or not text:
            return text[:200]

        try:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True).to("cpu")
            input_length = inputs["input_ids"].shape[1]

            # Explicit length constraints to prevent warnings
            max_length = min(96, max(16, input_length + 12))

            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=max_length,
                min_length=8,
                do_sample=False
            )

            return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        except Exception as e:
            print(f"⚠️ [SUMMARIZER] Error during summarization: {e}")
            return text[:200]

# === Global instance ===
summarizer = LazySummarizer()