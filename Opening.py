import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

def Speak(text):
    engine.say(text)
    engine.runAndWait()

def opening():



    Speak('Starting up')
    Speak("All systems ready")