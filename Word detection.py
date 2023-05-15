import speech_recognition as sr
import pyttsx3
from datetime import datetime
import winsound

engine = pyttsx3.init()
engine.setProperty('rate', 170)
r = sr.Recognizer()

List = ["sorry","I appologize","I am very sorry","I am sorry","forgive me","please forgive me"]

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio1 = r.listen(source)        
        print("YOU: {}".format(r.recognize_google(audio1)))

    for word in List:
        if (r.recognize_google(audio1) == word):
            engine.say("Why are you appologizing?")
            engine.runAndWait()
    break

