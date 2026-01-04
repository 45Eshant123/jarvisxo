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
conversation = []

def check_personal_commands(prompt):
    prompt = prompt.lower()

    if "my name is" in prompt:
        name = prompt.replace("my name is", "").strip().title()

    elif "mera naam" in prompt and "hai" in prompt:
        name = prompt.replace("mera naam", "").replace("hai", "").strip().title()

    else:
        return None

    memory["name"] = name
    save_memory(memory)
    return f"Theek hai {name}, main yaad rakhunga 😊"

def check_preferences(prompt):
    prompt = prompt.lower()

    likes = ["i like", "mujhe pasand hai"]
    dislikes = ["i hate", "mujhe pasand nahi"]

    for phrase in likes:
        if phrase in prompt:
            item = prompt.replace(phrase, "").strip()
            memory["preferences"][item] = "like"
            save_memory(memory)
            return f"Samajh gaya 👍 tumhe {item} pasand hai."

    for phrase in dislikes:
        if phrase in prompt:
            item = prompt.replace(phrase, "").strip()
            memory["preferences"][item] = "dislike"
            save_memory(memory)
            return f"Theek hai, main yaad rakhunga ki tumhe {item} pasand nahi."

    return None



def ask_ai(prompt):
    if not os.getenv("OPENAI_API_KEY"):
        return "OpenAI API key nahi mili"

    personal_reply = check_personal_commands(prompt)
    if personal_reply:
        return personal_reply

    preference_reply = check_preferences(prompt)
    if preference_reply:
        return preference_reply

    try:
        prefs = ", ".join(
            [f"{k} ({v})" for k, v in memory["preferences"].items()]
        ) if memory["preferences"] else "No preferences saved."

        conversation.insert(0, {
            "role": "system",
            "content": f"You are JarvisXo. "
                    f"User name is {memory.get('name', 'Boss')}. "
                    f"User preferences: {prefs}. "
                    f"Reply in Hinglish."
        })

        conversation.append({"role": "user", "content": prompt})
        recent = conversation[-8:]

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
