import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(device_index=2):
    """Listen for one command and return text"""
    with sr.Microphone(device_index=device_index) as source:
        print("🎙️ Listening...")
        recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = False
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("⏳ Processing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
        except sr.UnknownValueError:
            print("Could not understand")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None