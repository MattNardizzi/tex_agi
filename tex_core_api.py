# backend/tex_core_api.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request, jsonify
from backend.tex_core import process_prompt

app = Flask(__name__)

@app.route('/think', methods=['POST'])
def think():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        # Call Tex's brain to process the prompt
        response = process_prompt(prompt)

        return jsonify({ "response": response })

    except Exception as e:
        print(f"[Tex Error] ❌ {str(e)}")
        return jsonify({ "response": "⚠️ Tex encountered an internal error." }), 500

if __name__ == '__main__':
    print("🧠 Tex brain server starting on http://localhost:5001/think")
    app.run(host='0.0.0.0', port=5001)