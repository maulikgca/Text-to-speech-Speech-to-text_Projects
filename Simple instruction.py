import speech_recognition as sr
import pyttsx3
from datetime import datetime
import winsound

engine = pyttsx3.init()
engine.setProperty('rate', 170)
r = sr.Recognizer()

req = ["play","play beep","play the sound beep","can you beep","please play a beep sound","play a beep sound","play beep sound","beep sound"]

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio1 = r.listen(source)        
        print("YOU: {}".format(r.recognize_google(audio1)))

    for word in req:
        if (r.recognize_google(audio1) == word):
            engine.say("ok...wait")
            engine.runAndWait()
            winsound.Beep(700,1000)
    break
