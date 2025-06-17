import os
import requests
from config import GROQ_API_KEY

API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ai_write(input_text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",  
        "messages": [
            {"role": "system", "content": "You are a helpful writer."},
            {"role": "user", "content": f"Paraphrase the following chapter:\n\n{input_text}"}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"❌ Groq API error {response.status_code}: {response.text}")
        raise Exception("Groq API failed")

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    with open("scrape/chapter1.txt", encoding="utf-8") as f:
        text = f.read()
    out = ai_write(text)
    print(out[:300])

