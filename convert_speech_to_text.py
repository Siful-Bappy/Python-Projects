### pip install SpeechRecognition
### pip install PyAudio

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("..Initialised..")
    audio1 = r.record(source, duration = 5)
    query1 = r.recognize_google(audio1)
    query1=query1.low()
    print(query1)