import speech_recognition as sr
from voice import speak, stop_speaking
from brain import ask_ai, conversation
from actions import open_chrome, open_youtube, get_weather
import time

WAKE_WORDS = ["hey jarvis", "jarvisxo", "jarvis"]

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
    return None

speak("JarvisXo online ho chuka hai")

while True:
    command = listen()
    print("Heard:", command)

    if not command:
        continue

    if not any(command.startswith(w) for w in WAKE_WORDS):
        continue

    command = remove_wake_word(command)
    if not command:
        continue

    if "ruk jao" in command or "stop" in command or "chup" in command:
        stop_speaking()
        speak("Theek hai, main chup ho gaya")
        continue

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
        conversation.append(
            {"role": "system", "content": "You are JarvisXo, a smart Hinglish AI assistant."}
        )
        speak("Theek hai, sab bhool gaya")

    elif "exit" in command or "band ho jao" in command:
        speak("Goodbye boss")
        time.sleep(1)
        break

    else:
        speak("Soch raha hoon")  # optional thinking prompt
        reply = ask_ai(command)
        speak(reply)  # ✅ now audio will play