from core.brain import ask
from voice.speaker import speak
from voice.listener import listen

def run_jarvis():
    """Main loop — JARVIS listens, thinks, speaks"""
    speak("Jarvis is online. How can I help you?")
    
    while True:
        # Listen for your voice
        user_input = listen()
        
        if user_input is None:
            continue  # nothing heard, keep listening
        
        print(f"\nYou: {user_input}")
        
        # Exit commands
        if any(word in user_input for word in ["goodbye", "bye", "shutdown", "stop jarvis"]):
            speak("Goodbye. Jarvis shutting down.")
            break
        
        # Get response from AI brain
        response = ask(user_input)
        
        # Speak the response
        speak(response)
        print()  # blank line for readability

if __name__ == "__main__":
    print("=" * 40)
    print("     JARVIS - Personal AI Assistant")
    print("=" * 40)
    run_jarvis()