# Voice-Based-Calculator
Voice-Based Calculator is a Python application that performs mathematical operations using voice commands. It converts spoken input into text using speech recognition, evaluates the expression, and announces the result through text-to-speech. The project supports basic arithmetic operations and provides a hands-free calculator experience.

Voice-Based Calculator

A Python application that performs calculations using voice commands. The program listens to the user's speech, converts it into text, performs the requested mathematical operation, and speaks the result aloud.

Features

- Voice input using microphone
- Text-to-speech output
- Addition
- Subtraction
- Multiplication
- Division
- Continuous listening mode
- Exit command

Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio

Installation

Clone the repository

git clone https://github.com/yourusername/voice-based-calculator.git

Move to the project directory

cd voice-based-calculator

Install dependencies

pip install SpeechRecognition pyttsx3 pyaudio

Run the application

python main.py

Example Commands

- five plus seven
- ten minus three
- nine multiplied by six
- twenty divided by four
- exit

Project Structure

Voice-Based-Calculator
│
├── main.py
├── calculator.py
├── speech_input.py
├── voice_output.py
└── README.md

Future Improvements

- GUI using Tkinter
- Scientific calculations
- History feature
- Hindi language support
- Dark mode

License

MIT License
