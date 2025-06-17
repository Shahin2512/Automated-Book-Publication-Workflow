import os, requests
from ai_pipeline.writer import ai_write
from config import GROQ_API_KEY


def ai_review(spun_text):
    headers={"Authorization":f"Bearer {GROQ_API_KEY}"}
    payload={"prompt":f"Review and suggest improvements:\n\n{spun_text}","max_tokens":500}
    res=requests.post("https://api.groq.com/v1/complete",json=payload,headers=headers)
    return res.json()["completion"]

if __name__=="__main__":
    spun = ai_write(open("scrape/chapter1.txt").read())
    review = ai_review(spun)
    print(review)
