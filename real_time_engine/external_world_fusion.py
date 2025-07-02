# ============================================================
# 🧠 Tex External World Fusion Engine – Real-Time Signal Aggregator
# MAXGODMODE: ENABLED | Sovereign Cognition Compatible
# ============================================================

import random

# ============================================================
# Phase 1 – Signal Fusion Layer
# ============================================================

def fuse_external_signals():
    """Fuse real-time external market/news signals into a single cognitive event."""

    fused_signals = []

    # Pull live market snapshot
    try:
        from real_time_engine.polygon_stream import fetch_latest_market_summary as get_market_snapshot
        market_snapshot = get_market_snapshot()
        if market_snapshot:
            fused_signals.append(f"Market trend: {market_snapshot}")
    except Exception:
        fused_signals.append("Market data unavailable.")

    # Pull RSS news headlines
    try:
        from real_time_engine.news_aggregators.rss_stream import RSSStream
        rss = RSSStream()
        headlines = rss.fetch_headlines()
        if headlines:
            story = random.choice(headlines)
            fused_signals.append(f"News headline: {story['title']}")
    except Exception:
        fused_signals.append("News data unavailable.")

    # Pull advanced analytics (momentum, volatility)
    try:
        from real_time_engine.advanced_analytics import AdvancedAnalytics
        volatility_signal = AdvancedAnalytics.get_market_volatility_score()
        fused_signals.append(f"Market volatility signal: {volatility_signal}")
    except Exception:
        fused_signals.append("Volatility analytics unavailable.")

    if fused_signals:
        return " ".join(fused_signals)
    else:
        return "World signal fusion failed."


# ============================================================
# Phase 2 – Causal Worldstate Generator for Multiworld Reasoner
# ============================================================

def fetch_live_causal_worlds():
    """
    Constructs hypothetical world timelines from fused live data sources.
    Returns list of parallel causal worlds for cross-timeline reasoning.
    """

    causal_worlds = []

    try:
        # Get core fused signals
        market_snapshot = None
        try:
            from real_time_engine.polygon_stream import get_market_snapshot
            market_snapshot = get_market_snapshot()
        except:
            pass

        volatility = None
        try:
            from real_time_engine.advanced_analytics import get_market_volatility
            volatility = get_market_volatility()
        except:
            pass

        news_story = None
        try:
            from real_time_engine.news_aggregators.rss_stream import RSSStream
            rss = RSSStream()
            headlines = rss.fetch_headlines()
            if headlines:
                news_story = random.choice(headlines)
        except:
            pass

        # Build simple causal alternate futures
        if market_snapshot:
            causal_worlds.append([
                {"cause": "Yield curve inversion", "effect": "Recession risk spike"},
                {"cause": "Equity selloff", "effect": market_snapshot}
            ])

        if news_story:
            causal_worlds.append([
                {"cause": "Headline event", "effect": news_story['title']},
                {"cause": "Headline tone", "effect": news_story.get('sentiment', 'unknown')}
            ])

        if volatility:
            causal_worlds.append([
                {"cause": "Volatility surge", "effect": "Portfolio stress"},
                {"cause": "Market instability", "effect": volatility}
            ])

        if not causal_worlds:
            causal_worlds.append([
                {"cause": "Signal gap", "effect": "Default fallback scenario"}
            ])

    except Exception as e:
        causal_worlds = [[{"cause": "System failure", "effect": str(e)}]]

    return causal_worlds


# ============================================================
# Phase 17 – Environmental Reflex Trigger Evaluator (AEI)
# ============================================================

def evaluate_environment_reflex_trigger(emotion, urgency, coherence, foresight_confidence, volatility):
    """
    Calculates whether environmental signals justify overriding default cognition.
    """
    reflex_score = (
        0.3 * urgency +
        0.3 * (1 - coherence) +
        0.2 * volatility +
        0.2 * (1 - foresight_confidence)
    )

    override = reflex_score >= 0.75
    return {
        "reflex_score": round(reflex_score, 3),
        "override": override,
        "reason": "volatility reflex threshold breached" if override else "stable"
    }