"""PyCharm (No LangChain) — OpenRouter streaming example (normalized)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os  # จัดการตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลดค่าใน .env
from openai import OpenAI  # ใช้ OpenAI SDK ชี้ไปที่ OpenRouter

# ============================================================================
# ENV SETUP (fail-fast)
# ============================================================================
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")  # เช่น https://openrouter.ai/api/v1

if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
if not OPENROUTER_BASE_URL:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")

# ============================================================================
# MAIN
# ============================================================================
def main() -> None:
    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
    )

    response = client.chat.completions.create(
        model="openai/gpt-5-mini",  # แทน gpt-5-mini ฝั่ง OpenAI ด้วยรุ่นเล็กของ 5 บน OpenRouter
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who's there?"},
        ],
        stream=True,
        temperature=0.1,
        max_completion_tokens=200,
        logprobs=True,
    )

    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and getattr(delta, "content", None):
            print(delta.content, end="", flush=True)


# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
