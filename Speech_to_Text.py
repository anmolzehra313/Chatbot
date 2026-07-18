import speech_recognition as sr

def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)  # New line
        print("Listening...")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(f"You said: {voice_data}")
            return voice_data
        except sr.UnknownValueError:
            print("I did not understand that.")
            return "I did not understand that."
        except sr.RequestError:
            print("Could not request results.")
            return "Could not request results."
