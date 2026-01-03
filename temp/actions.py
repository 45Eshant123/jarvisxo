import subprocess
import webbrowser
import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def open_chrome():
    subprocess.Popen(
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )

def open_youtube():
    webbrowser.open("https://youtube.com")

def get_weather(city="Delhi"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{city} ka temperature {temp}°C hai aur mausam {desc} hai"
        else:
            return "Weather data nahi mil pa raha"

    except:
        return "Weather service error"
