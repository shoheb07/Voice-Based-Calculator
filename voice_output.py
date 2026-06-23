import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Result:", text)
    engine.say(str(text))
    engine.runAndWait()
