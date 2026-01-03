import pyttsx3
import time

def speak(text):
    if not text:
        return
    print("JarvisXo:", text)

    try:
        engine = pyttsx3.init("sapi5")
        engine.setProperty("rate", 160)
        engine.setProperty("volume", 1.0)

        voices = engine.getProperty("voices")
        if voices and len(voices) > 1:
            engine.setProperty("voice", voices[1].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

        del engine
        time.sleep(0.2)

    except Exception as e:
        print("❌ TTS Error:", e)

def stop_speaking():
    print("🛑 Speech stopped")