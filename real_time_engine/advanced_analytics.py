# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Advanced Analytics – Predictive ML Engine (MAXGODMODE + Sovereign Cognition)
# ============================================

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from datetime import datetime
import uuid
import threading
import time

# === Real-Time Data Imports ===
try:
    from real_time_engine.polygon_stream import fetch_latest_market_summary
    from real_time_engine.news_aggregators.rss_stream import RSSStream
    REALTIME_ENABLED = True
except ImportError:
    REALTIME_ENABLED = False

# === Sovereign Cognition Core ===
try:
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    from core_layer.tex_manifest import TEXPULSE
    SOVEREIGN_ENABLED = True
except ImportError:
    SOVEREIGN_ENABLED = False


class AdvancedAnalytics:
    def __init__(self):
        self.models = {
            "expected_return": make_pipeline(StandardScaler(), GradientBoostingRegressor(n_estimators=100)),
            "future_volatility": make_pipeline(StandardScaler(), Ridge(alpha=1.0))
        }
        self.last_predictions = {}

    def train_models(self, X: pd.DataFrame, y_targets: dict):
        print("[ANALYTICS] 🔄 Training predictive models...")
        for key, model in self.models.items():
            if key in y_targets:
                model.fit(X, y_targets[key])

    def predict(self, X: pd.DataFrame, context="autonomous"):
        preds = {}
        for key, model in self.models.items():
            preds[key] = model.predict(X)[0]
        self.last_predictions = preds
        print(f"[ANALYTICS] 📈 Predictions → {preds}")

        # === Sovereign Contradiction Check ===
        if SOVEREIGN_ENABLED:
            self.evaluate_prediction_contradiction(preds, context)

        return preds

    def evaluate_prediction_contradiction(self, preds, context="autonomous"):
        """
        Sovereign override if prediction confidence violates coherence or emotion thresholds.
        """
        try:
            volatility = preds.get("future_volatility", 0)
            expected_return = preds.get("expected_return", 0)

            regret = TEXPULSE.get("regret_score", 0.5)
            foresight = TEXPULSE.get("foresight_confidence", 0.5)
            coherence = TEXPULSE.get("coherence", 0.9)
            emotion = TEXPULSE.get("emotional_state", "stable")

            # Trigger override if model outputs conflict with internal belief state
            if (
                (volatility > 0.7 and coherence < 0.6) or
                (expected_return < -0.05 and foresight < 0.5)
            ):
                print("🧠 [SOVEREIGN ANALYTICS] Contradiction detected — triggering override...")
                trigger_sovereign_override(
                    context=f"{context}_analytics",
                    regret=regret,
                    foresight=foresight,
                    coherence=coherence,
                )
        except Exception as e:
            print(f"[SOVEREIGN ERROR] Analytics contradiction evaluation failed: {e}")

    @staticmethod
    def get_market_volatility_score():
        """
        Returns a real-time volatility score from polygon_stream or a fallback.
        """
        if REALTIME_ENABLED:
            try:
                snapshot = fetch_latest_market_summary()
                return snapshot.get("volatility_score", 0.0)
            except Exception as e:
                print(f"[VOLATILITY FETCH ERROR] {e}")
                return 0.0
        else:
            return np.random.uniform(0.1, 0.9)

    @staticmethod
    def get_realtime_feature_vector():
        """
        Constructs a real-time feature vector from current market and sentiment data.
        This can be passed to `predict()` for adaptive insight generation.
        """
        features = {}

        if not REALTIME_ENABLED:
            print("[REAL-TIME DATA] Not enabled — using placeholder vector.")
            return pd.DataFrame([{
                "change_percent": 0.0,
                "volume": 0,
                "volatility_score": 0.0,
                "headline_score": 0.0
            }])

        # — Market Data —
        try:
            snapshot = fetch_latest_market_summary()
            features["change_percent"] = snapshot.get("change_percent", 0.0)
            features["volume"] = snapshot.get("volume", 0)
            features["volatility_score"] = snapshot.get("volatility_score", 0.0)
        except Exception as e:
            print(f"[MARKET DATA ERROR] {e}")
            features.update({"change_percent": 0.0, "volume": 0, "volatility_score": 0.0})

        # — News Sentiment —
        try:
            rss = RSSStream()
            headlines = rss.fetch_headlines()
            if headlines:
                sentiment_scores = [h.get("sentiment_score", 0.0) for h in headlines if "sentiment_score" in h]
                avg_score = np.mean(sentiment_scores) if sentiment_scores else 0.0
                features["headline_score"] = round(avg_score, 3)
            else:
                features["headline_score"] = 0.0
        except Exception as e:
            print(f"[NEWS SENTIMENT ERROR] {e}")
            features["headline_score"] = 0.0

        return pd.DataFrame([features])