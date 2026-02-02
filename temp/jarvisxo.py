import speech_recognition as sr
import time
from brain import current_mood
from voice import speak
from brain import ask_ai, conversation
from actions import open_chrome, open_youtube, get_weather

WAKE_WORDS = ["hey jarvis", "jarvisxo", "jarvis", "hello"]
ACTIVE_TIMEOUT = 50  # seconds

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio).lower()
    except:
        return ""
    

def remove_wake_word(text):
    for word in WAKE_WORDS:
        if text.startswith(word):
            return text[len(word):].strip()
    return text

speak("Mai aapki personal JarvisXo aap ke leye hajir hoon boss")

active_mode = False
last_active_time = 0

while True:
    command = listen()
    print("Heard:", command)

    if not command:
        continue

    if any(command.startswith(w) for w in WAKE_WORDS):
        active_mode = True
        last_active_time = time.time()
        command = remove_wake_word(command)

        if not command:
            speak("Haa bholiye boss")
            continue

    if active_mode and time.time() - last_active_time > ACTIVE_TIMEOUT:
        active_mode = False
        speak("Main sleep mode me ja rahi hoon")
        continue

    if not active_mode:
        continue

    last_active_time = time.time()

    if current_mood in ["sad", "angry"]:
        speak("Boss pehle thoda baat kar lete hain, phir kaam karenge.")
        continue

    exit_commands = [
        "exit",
        "band ho jao",
        "goodbye",
        "quit",
        "stop",
        "shut down",
        "off",
        "bye"
    ]
    if any(word in command.lower() for word in exit_commands):
        speak("Goodbye boss")
        break

    if "chrome" in command:
        speak("Chrome khol rahi hoon")
        open_chrome()

    elif "youtube" in command:
        speak("YouTube khol rahi hoon")
        open_youtube()

    elif "weather" in command or "mausam" in command:
        speak(get_weather())

    elif "memory clear" in command or "yaad bhool jao" in command:
        conversation.clear()
        conversation.append({
            "role": "system",
            "content": "You are JarvisXo, a smart Hinglish AI assistant."
        })
        speak("Theek hai boss jaisi aap ki marjhi, sab kuch bhool gayi")

    else:
        speak("Okay boss main kuch Sochthi hoon iske bare me")
        reply = ask_ai(command)
        speak(reply)
