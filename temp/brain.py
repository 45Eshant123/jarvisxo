import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "memory.json"

# 🔹 Load memory
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"name": None, "preferences": {}}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

# 🔹 Save memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

# 🧠 Short-term conversation
conversation = [
    {
        "role": "system",
        "content": "You are JarvisXo, a smart Hinglish AI assistant. Remember user details and reply naturally."
    }
]

def check_personal_commands(prompt):
    prompt = prompt.lower()

    # Save name
    if "my name is" in prompt or "mera naam" in prompt:
        name = prompt.split("is")[-1].strip().title()
        memory["name"] = name
        save_memory(memory)
        return f"Theek hai {name}, main yaad rakhunga 😊"

    return None

def ask_ai(prompt):
    if not os.getenv("OPENAI_API_KEY"):
        return "OpenAI API key nahi mili"

    # 🔹 Check memory commands first
    personal_reply = check_personal_commands(prompt)
    if personal_reply:
        return personal_reply

    try:
        conversation.append({"role": "user", "content": prompt})
        recent = conversation[-8:]

        # 🔹 Inject memory into system prompt
        name_info = f"User name is {memory['name']}." if memory["name"] else ""
        recent.insert(0, {
            "role": "system",
            "content": f"You are JarvisXo. {name_info} Reply in Hinglish."
        })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=recent,
            max_tokens=250,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return "AI response nahi mil pa raha"
