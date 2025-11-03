import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY  = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")  
if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
if not OPENROUTER_BASE_URL:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")
  
client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL)

response = client.chat.completions.create(
    model="openai/gpt-5-mini", 
    messages=[ 
        {"role": "system", "content": "You are a helpful assistant."}, 
        {"role": "user", "content": "Who's there?"} 
    ] 
) 
print(response.choices[0].message.content) 
