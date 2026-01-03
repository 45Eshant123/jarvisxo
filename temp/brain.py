import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 SHORT-TERM MEMORY
conversation = [
    {"role": "system", "content": "You are JarvisXo, a smart Hinglish AI assistant. Remember context and reply naturally."}
]

def ask_ai(prompt):
    if not os.getenv("OPENAI_API_KEY"):
        return "OpenAI API key nahi mili"

    try:
        # add user message to memory
        conversation.append({"role": "user", "content": prompt})

        # keep memory short (last 8 messages)
        recent_memory = conversation[-8:]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=recent_memory,
            max_tokens=250,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()

        # add assistant reply to memory
        conversation.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return "AI response nahi mil pa raha"
