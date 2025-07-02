# tex_demos/demo_self_rewrite.py

from self_rewriting.rewriting_orchestrator import initiate_self_rewrite
from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log
from core_layer.tex_manifest import TEXPULSE

def run_self_rewrite_financially():
    log.info("♻️ [SELF-REWRITE DEMO] Triggering sovereign self-rewrite with financial context...")

    TEXPULSE["urgency"] = 0.88
    TEXPULSE["entropy"] = 0.49
    TEXPULSE["emotion"] = "reflex_patch"

    # Optional: trigger a financial cortex adjustment before rewrite
    financial_context = MasterTexOrchestrator().get_current_state()
    dispatch_signal("financial_decision", {
        "summary": "Pre-rewrite financial signal",
        "context": financial_context
    })

    initiate_self_rewrite()

def register(register_func):
    register_func("trigger_self_rewrite_demo", lambda signal: run_self_rewrite_financially())