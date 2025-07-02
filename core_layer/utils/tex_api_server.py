# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/utils/tex_api_server.py
# Purpose: API server to expose Tex panel data to UI
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core_layer.utils.tex_state import tex_state

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tex-state")
def get_tex_state():
    state = tex_state.get_state()
    sovereign = state.get("sovereign_cognition", {})
    debate = state.get("internal_debate", {})

    print("\n🧠 [API STATE EMIT] Serving panel snapshot:")
    if sovereign:
        print("  • sovereign_cognition:")
        for key, value in sovereign.items():
            print(f"     ↳ {key}: {value}")
    else:
        print("  ⚠️ No 'sovereign_cognition' found")

    if debate:
        print(f"  • internal_debate → {len(debate.get('entries', []))} entries")
    else:
        print("  ⚠️ No 'internal_debate' data found")

    # ✅ Return full state so all panels get their data
    return state

print("[API SERVER] tex_state ID:", id(tex_state))