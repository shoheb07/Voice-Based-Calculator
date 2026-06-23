from speech_input import listen
from voice_output import speak
from calculator import calculate

speak("Voice calculator started")

while True:
    command = listen()

    if command == "":
        continue

    if "exit" in command:
        speak("Goodbye")
        break

    answer = calculate(command)
    speak(answer)
