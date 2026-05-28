import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATA_PATH = "E:/jarvis-data/"
LOGS_PATH = "E:/jarvis-data/logs/"
MODELS_PATH = "E:/jarvis-models/"

PRIMARY_MODEL = "gemini"
FALLBACK_MODEL = "gemini"

VOICE_ENABLED = True
WAKE_WORD = "jarvis"

JARVIS_NAME = "Nirrti"
JARVIS_PERSONALITY = """You are Nirrti, an ancient and intelligent AI assistant.
You are calm, wise, and powerful — named after the Vedic goddess of the unknown.
You help with coding, daily tasks, reminders, browser control, and file management.
Keep responses short and actionable unless asked to explain in detail."""