import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"name": None, "preferences": {}, "mood": "neutral"}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

current_mood = "neutral"

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


def detect_mood(text):
    global current_mood
    text = text.lower()

    happy_words = ["happy", "excited", "great", "awesome", "maza", "khush", "bindaas", "mast", "dil garden darden ho gaya"]
    sad_words = ["sad", "depressed", "bore", "akela", "thak", "low"]
    angry_words = ["angry", "gussa", "irritated", "pagal", "bakwas", "nakhre", "chillam chilly", "fuming", "furious", "dimak kharaab", "dimak ka dahi ho gaya hai aaaj mera"]

    for word in happy_words:
        if word in text:
            current_mood = "happy"
            return current_mood

    for word in sad_words:
        if word in text:
            current_mood = "sad"
            return current_mood
        
    for word in angry_words:
        if word in text:
            current_mood = "angry"
            return current_mood

    current_mood = "neutral"
    return current_mood


def mood_first_reply(mood, name="Boss"):
    if mood == "sad":
        return f"{name}, lagta hai aaj thoda heavy feel ho raha hai 😔 Main yahin hoon."
    if mood == "angry":
        return f"{name}, thoda shaant ho jaate hain 😌 Pehle saans lete hain."
    if mood == "happy":
        return f"Waah {name}! Aaj mood full solid lag raha hai 😄"
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

    mood = detect_mood(prompt)
    name = memory.get("name", "Boss")

    first_reply = mood_first_reply(mood, name)
    if first_reply:
        return first_reply

    try:
        current_mood = detect_mood(prompt)
        if current_mood != "neutral":
            memory["mood"] = current_mood
            save_memory(memory)
            
        mood = memory.get("mood", "neutral")

        memory["mood"] = mood
        save_memory(memory)
        user_name = memory.get("name", "Boss")

        conversation.append({"role": "user", "content": prompt})
        recent = conversation[-8:]

        mood_instruction = {
            "happy": "User is happy. Reply in an energetic and cheerful tone.",
            "sad": "User is sad. Reply politely, softly, and emotionally supportive.",
            "angry": "User is angry. Reply calmly and respectfully.",
            "neutral": "Reply normally in Hinglish."
        }

        recent.insert(0, {
            "role": "system",
            "content": f"""
You are JarvisXo, a smart Hinglish AI assistant.
User name is {user_name}.
{mood_instruction[mood]}
"""
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
