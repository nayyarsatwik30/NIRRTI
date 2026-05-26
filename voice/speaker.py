import pyttsx3

# ── Speaker setup ──────────────────────────────────────────
engine = pyttsx3.init()

# Voice settings
engine.setProperty('rate', 180)      # speed (150=slow, 200=fast)
engine.setProperty('volume', 1.0)    # volume (0.0 to 1.0)

# Pick a voice — 0 is usually male, 1 is usually female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    """Make JARVIS speak out loud"""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def set_voice(index):
    """Change voice — call with 0 or 1"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[index].id)