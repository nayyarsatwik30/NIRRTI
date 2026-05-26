import os
import requests
import config
from groq import Groq

# ── Groq setup ─────────────────────────────────────────────
groq_client = Groq(api_key=config.GROQ_API_KEY)

def ask_groq(prompt):
    """Send a message to Groq (Llama 3.3) and get a response"""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": config.JARVIS_PERSONALITY},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq failed: {e}")
        return ask_deepseek(prompt)  # fallback

def ask_deepseek(prompt):
    """Fallback to DeepSeek if Groq fails"""
    try:
        headers = {
            "Authorization": f"Bearer {config.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        body = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": config.JARVIS_PERSONALITY},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=body,
            timeout=10
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"All AI services failed: {e}"

def ask(prompt):
    """Main function — always call this from anywhere in JARVIS"""
    return ask_groq(prompt)