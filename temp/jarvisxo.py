import speech_recognition as sr
import time

from voice import speak
from brain import ask_ai, conversation
from actions import open_chrome, open_youtube, get_weather

WAKE_WORDS = ["hey jarvis", "jarvisxo", "jarvis"]
ACTIVE_TIMEOUT = 15  # seconds

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

speak("JarvisXo online ho chuki hai")

active_mode = False
last_active_time = 0

while True:
    command = listen()
    print("Heard:", command)

    if not command:
        continue

    # 🟢 WAKE WORD CHECK
    if any(command.startswith(w) for w in WAKE_WORDS):
        active_mode = True
        last_active_time = time.time()
        command = remove_wake_word(command)

        if not command:
            speak("Haa bholiye boss")
            continue

    # 💤 AUTO SLEEP
    if active_mode and time.time() - last_active_time > ACTIVE_TIMEOUT:
        active_mode = False
        speak("Main sleep mode me ja rahi hoon")
        continue

    # ❌ IGNORE if not active
    if not active_mode:
        continue

    last_active_time = time.time()

    # 🔴 EXIT
    if "exit" in command or "band ho jao" in command:
        speak("Goodbye boss")
        break

    # 🌐 ACTIONS
    if "chrome" in command:
        speak("Chrome khol raha hoon")
        open_chrome()

    elif "youtube" in command:
        speak("YouTube khol raha hoon")
        open_youtube()

    elif "weather" in command or "mausam" in command:
        speak(get_weather())

    elif "memory clear" in command or "yaad bhool jao" in command:
        conversation.clear()
        conversation.append({
            "role": "system",
            "content": "You are JarvisXo, a smart Hinglish AI assistant."
        })
        speak("Theek hai, sab bhool gaya")

    else:
        speak("Soch raha hoon")
        reply = ask_ai(command)
        speak(reply)
