import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEMORY_FILE = "memory.json"

# ---------------- MEMORY ---------------- #

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "name": None,
            "preferences": {},
            "mood": "neutral",
            "personality": "soft"
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

current_mood = "neutral"
conversation = []

# ---------------- PERSONAL COMMANDS ---------------- #

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

# ---------------- PERSONALITY COMMAND (WEEK-3) ---------------- #

def check_personality_command(prompt):
    prompt = prompt.lower()

    if "professional mode" in prompt:
        memory["personality"] = "professional"
    elif "friendly mode" in prompt:
        memory["personality"] = "friendly"
    elif "soft mode" in prompt:
        memory["personality"] = "soft"
    else:
        return None

    save_memory(memory)
    return f"Done boss 😎 Ab main {memory['personality']} mode me hoon"

# ---------------- PREFERENCES ---------------- #

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

# ---------------- MOOD DETECTION ---------------- #

def detect_mood(text):
    global current_mood
    text = text.lower()

    happy_words = [
        "happy", "excited", "great", "awesome", "maza", "khush",
        "bindaas", "mast", "dil garden darden ho gaya"
    ]

    sad_words = [
        "sad", "depressed", "bore", "akela", "thak", "low"
    ]

    angry_words = [
        "angry", "gussa", "irritated", "pagal", "bakwas",
        "nakhre", "fuming", "furious", "dimak kharaab",
        "dimak ka dahi ho gaya"
    ]
    
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

# ---------------- FIRST EMOTIONAL REPLY ---------------- #

def mood_first_reply(mood, name="Boss"):
    if mood == "sad":
        return f"{name}, lagta hai thoda heavy feel ho raha hai 😔 Main yahin hoon."
    if mood == "angry":
        return f"{name}, thoda calm ho jaate hain 😌"
    if mood == "happy":
        return f"Waah {name}! Aaj mood ekdum solid hai 😄"
    return None

# ---------------- MAIN AI FUNCTION ---------------- #

def ask_ai(prompt):
    if not os.getenv("OPENAI_API_KEY"):
        return "OpenAI API key nahi mili"

    # Name command
    personal_reply = check_personal_commands(prompt)
    if personal_reply:
        return personal_reply

    # Personality command
    personality_reply = check_personality_command(prompt)
    if personality_reply:
        return personality_reply

    # Preferences
    preference_reply = check_preferences(prompt)
    if preference_reply:
        return preference_reply

    # Mood detection
    mood = detect_mood(prompt)
    name = memory.get("name") or "Boss"
    personality = memory.get("personality", "soft")

    first_reply = mood_first_reply(mood, name)
    if first_reply:
        memory["mood"] = mood
        save_memory(memory)
        return first_reply

    try:
        memory["mood"] = mood
        save_memory(memory)

        conversation.append({"role": "user", "content": prompt})
        recent = conversation[-8:]

        personality_instruction = {
            "professional": "Reply formally, respectfully, concise English-Hinglish.",
            "friendly": "Reply friendly, casual, warm Hinglish.",
            "soft": "Reply politely, emotionally soft Hinglish."
        }

        mood_instruction = {
            "happy": "User is happy. Be energetic.",
            "sad": "User is sad. Be emotionally supportive.",
            "angry": "User is angry. Be calm and soothing.",
            "neutral": "Normal tone."
        }

        recent.insert(0, {
            "role": "system",
            "content": f"""
You are JarvisXo, an intelligent Hinglish AI assistant.
User name: {name}
Personality: {personality_instruction[personality]}
Mood behavior: {mood_instruction[mood]}
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
        return "Abhi main thoda busy hoon 😔"
