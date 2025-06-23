import os
from dotenv import load_dotenv
import random

# Load .env API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

try:
    if openai_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=openai_api_key)
    else:
        raise ImportError("OpenAI key not found, switching to fallback.")
except ImportError:
    from transformers import pipeline
    import torch  # ensure torch is available
    fallback = pipeline("text2text-generation", model="google/flan-t5-small")

def ask_genai(prompt: str) -> str:
    try:
        if openai_api_key:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        else:
            result = fallback(prompt, max_length=128, do_sample=True, top_k=50)
            return result[0]['generated_text']
    except Exception as e:
        return f"❌ GenAI Error: {e}"
