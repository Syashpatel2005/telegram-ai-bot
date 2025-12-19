# ==============================
# ai.py
# ==============================

import os
import requests

GROQ_API_KEY = os.getenv("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")

def get_ai_reply(prompt):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
