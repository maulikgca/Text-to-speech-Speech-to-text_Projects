import pyttsx3

engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voices = engine.getProperty('voices')
print(voices)
for voice in voices:
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
engine.setProperty('voice', voice_id)

engine.say("Hello World!")
engine.say("I m a text to speech machine")
engine.runAndWait()

# engine.setProperty('voices', voices[1].id)
# engine.say("Hello Man!")
# engine.runAndWait()
