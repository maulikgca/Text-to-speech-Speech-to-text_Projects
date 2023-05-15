import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 170)
engine.setProperty('volume', 0.7)

engine.say("Hello World!")
engine.say("I m a text to speech machine")

engine.runAndWait() 