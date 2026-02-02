# 🤖 JarvisXo - AI Voice Assistant

## 📖 Project Overview

**JarvisXo** is a powerful multilingual AI voice assistant built in Python that responds to voice commands in both **English** and **Hindi**. It integrates with OpenAI's GPT for intelligent responses and can be controlled via:
- **🎤 Voice Commands** (using your laptop's microphone)
- **📱 Telegram Bot** (remote control from anywhere)

### Key Features:
- ✅ Voice recognition in English and Hindi
- ✅ Natural text-to-speech audio replies
- ✅ AI-powered responses using OpenAI GPT
- ✅ Application control (Chrome, VS Code, etc.)
- ✅ Weather information
- ✅ Time announcements
- ✅ Remote control via Telegram bot

---

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have:
- **Python 3.8+** installed on your system
- A **microphone** (for voice commands)
- Internet connection
- Git installed (optional, for cloning)

---

## 📥 Installation Steps

### Step 1: Clone the Repository from GitHub

```bash
# Using Git
git clone https://github.com/YOUR_USERNAME/PROJECT-JarvisXo.git
cd PROJECT-JarvisXo
```

**OR Download Manually:**
1. Go to the GitHub repository
2. Click the **Code** button → **Download ZIP**
3. Extract the ZIP file to your desired location
4. Open terminal/command prompt in that folder

---

### Step 2: Install Required Dependencies

#### Option A: Install All Packages at Once (Recommended)

```bash
# Install all required Python packages from requirements.txt
pip install -r requirements.txt
```

#### Option B: Install Packages Individually

If you prefer to install packages one by one, use the following commands:

```bash
# OpenAI API integration for AI-powered responses
pip install openai

# HTTP library for API calls
pip install requests

# Text-to-speech synthesis
pip install pyttsx3

# Voice recognition and speech input
pip install SpeechRecognition

# Audio input/output support
pip install pyaudio
```

**Required Packages Details:**

| Package | Version | Purpose |
|---------|---------|---------|
| `openai` | Latest | OpenAI GPT integration for AI responses |
| `requests` | Latest | HTTP library for making API calls |
| `pyttsx3` | Latest | Text-to-speech engine for audio output |
| `SpeechRecognition` | Latest | Voice recognition for speech input |
| `pyaudio` | Latest | Audio input/output (microphone access) |

**Note for Windows Users:**

If you encounter issues installing `pyaudio` on Windows, use the alternative installation method:

```bash
# Method 1: Using pipwin (Recommended for Windows)
pip install pipwin
pipwin install pyaudio

# Method 2: If pipwin fails, try:
pip install pipwin --upgrade
pipwin refreshall
pipwin install pyaudio
```

If problems persist, you can try:
```bash
# Install pre-built wheel for pyaudio
pip install pipwin
pipwin install pyaudio==0.2.11
```

---

## 🔑 API Keys & Tokens Setup

You need to obtain and configure the following API keys:

### 1️⃣ OpenAI API Key (Required for AI responses)

**How to Get:**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to **API Keys** section
4. Click **Create new secret key**
5. Copy the key (starts with `sk-...`)

**Where to Add:**
Open `jarvisxo_core.py` and `jarvisxo_voice_agent.py`, replace:
```python
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
```

---

### 2️⃣ Weather API Key (For weather feature)

**How to Get:**
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to **API Keys** tab
4. Copy your API key

**Where to Add:**
In `jarvisxo_core.py` and `jarvisxo_voice_agent.py`, replace:
```python
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY_HERE"
CITY = "YourCity"  # Change to your city name
```

---

### 3️⃣ Telegram Bot Token (For remote control)

**How to Get:**
1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Follow the prompts to name your bot
4. Copy the **HTTP API token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

**Where to Add:**
In `jarvisxo_telegram_bot.py`, replace:
```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
```

**Get Your Chat ID:**
1. Search for **@userinfobot** on Telegram
2. Start the bot and it will show your Chat ID
3. Replace in `jarvisxo_telegram_bot.py`:
```python
ALLOWED_CHAT_ID = YOUR_CHAT_ID_NUMBER  # Without quotes
```

---

## 🖥️ How to Run JarvisXo

### Option 1: 🎤 Voice Agent (Laptop/Desktop)

This mode allows you to control JarvisXo using voice commands directly on your laptop.

#### Running the Voice Agent:

```bash
# Navigate to project directory
cd PROJECT-JarvisXo

# Run the voice agent
python jarvisxo_voice_agent.py
```

#### What Happens:
1. The program starts and says: **"Hello Boss, main JarvisXo hoon"**
2. It listens for your voice commands
3. Speak commands like:
   - *"Open Chrome"*
   - *"What's the weather?"*
   - *"What time is it?"*
   - *"Who is Albert Einstein?"*
   - *"Bye"* (to exit)

#### Voice Commands You Can Use:

| Command | Action |
|---------|--------|
| "Chrome"  | "Open Chrome" | Opens Google Chrome |
| "VS Code" | Opens Visual Studio Code |
| "YouTube" | Opens YouTube in browser |
| "Weather" | "Mausam" | Gets current weather |
| "Time"    | Tells current time |
| "Exit" / "Bye" | Shuts down JarvisXo |
| Any other question | Asks AI (GPT) for response |

#### Troubleshooting Voice Agent:
- **No audio output?** Check your speaker volume and permissions
- **Microphone not working?** Allow microphone access in system settings
- **Commands not recognized?** Speak clearly and ensure internet connection

---

### Option 2: 📱 Telegram Bot (Remote Control)

Control JarvisXo from anywhere using Telegram messages!

#### Running the Telegram Bot:

```bash
# Navigate to project directory
cd PROJECT-JarvisXo

# Run the Telegram bot
python jarvisxo_telegram_bot.py
```

#### What Happens:
1. The bot starts and says: **"Telegram control active"**
2. Bot is now listening for messages on Telegram
3. Open Telegram and find your bot
4. Send text commands (same as voice commands)

#### How to Use Telegram Bot:

1. **Start the bot** on your laptop:
   ```bash
   python jarvisxo_telegram_bot.py
   ```

2. **Open Telegram** on your phone/computer

3. **Find your bot** (search for the bot name you created)

4. **Send commands** as text messages:
   - `open chrome`
   - `weather`
   - `what is python?`
   - `bye`

5. **Bot responds** with confirmation and executes on your laptop

#### Security Note:
- Only your Chat ID can control the bot (configured in `ALLOWED_CHAT_ID`)
- Others will get "Unauthorized" message

#### Telegram Bot Troubleshooting:
- **Bot not responding?** Ensure the script is running on your laptop
- **"Unauthorized" error?** Check that `ALLOWED_CHAT_ID` matches your Chat ID
- **Internet issues?** Bot needs active internet connection

---

## 🔧 Configuration Files

### File Structure:
```
PROJECT-JarvisXo/temp/
│            # Core functionality and processing
├── README.md                   # This file
└── temp/
    ├──jarvisxo.py
    ├──actions.py
    ├──brain.py
    ├──config.py
    ├──voice.py                 # Voice control interface
    ├──requirements.txt         # Python dependencies
```

### Customization:

**Change Voice Speed:**
In `jarvisxo.py`:
```python
engine.setProperty("rate", 160)  # Increase for faster, decrease for slower
```

**Change Voice Gender:**
```python
# voices[0] = Male voice
# voices[1] = Female voice
engine.setProperty('voice', voices[1].id)
```

**Add Custom Commands:**
Edit the `process()` function in either file:
```python
elif "your command" in cmd:
    speak("Your response")
    # Your code here
```

---

## 🎯 Quick Start Guide

### For First-Time Users:

1. **Setup Everything:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Edit config files with your API keys
   # (OpenAI, Weather, Telegram tokens)
   ```

2. **Test Voice Agent:**
   ```bash
   python jarvisxo_voice_agent.py
   ```
   Say: *"Hello JarvisXo, what time is it?"*

3. **Test Telegram Bot:**
   ```bash
   python jarvisxo_telegram_bot.py
   ```
   Send message to your bot on Telegram: `weather`

---

## ❓ Frequently Asked Questions

**Q: Do I need both OpenAI and Weather API?**
A: OpenAI is required for AI responses. Weather API is optional (only for weather feature).

**Q: Can I run both Voice Agent and Telegram Bot together?**
A: Yes! Run them in separate terminal windows.

**Q: Does the Telegram bot work when laptop is off?**
A: No, the bot script must be running on your laptop. Consider deploying to a cloud server for 24/7 access.

**Q: Voice recognition not working?**
A: Ensure microphone permissions are granted and `pyaudio` is installed correctly.

**Q: Can I change the wake word?**
A: This version doesn't use wake words. Modify the code to add wake word detection.

---

## 🛠️ Running in Background (Advanced)

### Windows:
```bash
# Run in background (won't show window)
pythonw jarvisxo_voice_agent.py
```

### Linux/Mac:
```bash
# Run in background
nohup python3 jarvisxo_voice_agent.py &
```

---

## 📝 Important Notes

1. **API Costs:** OpenAI API has usage costs. Monitor your usage at [OpenAI Usage](https://platform.openai.com/usage)
2. **Privacy:** Voice commands are sent to Google for speech recognition
3. **Security:** Never share your API keys publicly or commit them to GitHub
4. **Updates:** Keep dependencies updated: `pip install --upgrade -r requirements.txt`

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## 📧 Support

If you encounter issues:
1. Check that all API keys are correctly configured
2. Verify internet connection
3. Ensure all dependencies are installed
4. Check Python version (3.8+)

---

## 📜 License

This project is open-source and available for personal and educational use.

---

## 🌟 Credits

- **OpenAI** - GPT AI responses
- **OpenWeatherMap** - Weather data
- **Telegram** - Bot platform
- **Google** - Speech recognition

---

**Enjoy using JarvisXo! 🚀**
