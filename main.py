from core.brain import ask
from voice.speaker import speak
from voice.listener import listen

def run_nirrti():
    """Main loop — Nirrti listens, thinks, speaks"""
    speak("Nirrti is online. How may I serve you?")
    
    while True:
        # Listen for your voice
        user_input = listen()
        
        if user_input is None:
            continue  # nothing heard, keep listening
        
        print(f"\nYou: {user_input}")
        
        # Exit commands
        if any(word in user_input for word in ["goodbye", "bye", "shutdown", "stop nirrti"]):
            speak("Farewell. Nirrti going dark.")
            break
        
        # Get response from AI brain
        response = ask(user_input)
        
        # Speak the response
        speak(response)
        print()  # blank line for readability

if __name__ == "__main__":
    print("=" * 40)
    print("     NIRRTI - Ancient AI Assistant")
    print("=" * 40)
    run_nirrti()