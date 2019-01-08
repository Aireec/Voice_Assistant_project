import os
import webbrowser
import re
import requests
import speech_recognition as sr
import pyttsx
from selenium import webdriver
from pygame import mixer
import pyautogui
import random
import spotipy
from Play_Music import music

# Talking engine for A.I
engine = pyttsx.init()
# setting speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 45)

engine2 = pyttsx.init()
rate = engine2.getProperty('rate')
engine.setProperty('rate', rate - 45)

engine3 = pyttsx.init()
rate = engine3.getProperty('rate')
engine.setProperty('rate', rate - 45)

engine4 = pyttsx.init()
rate = engine4.getProperty('rate')
engine.setProperty('rate', rate - 45)

#driver = webdriver.Chrome()



# Audio setup
def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


# Listens for commands
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.000)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command




class Assistant_Commands():
    def assistant(command):
        "if statements for executing commands"

        if 'computer' in command:
            Listening_Response = ['Yes Sir', 'How may I help', 'At your service', 'You called sir', 'Hello']
            engine.say(random.choice(Listening_Response))
        engine.runAndWait()

        if 'nicole' in command:
            engine.say('A-reec, loves you, Nichol')
        engine.runAndWait()

        if 'rap like a' in command:
            engine.say('Computer, must be, in my, genes')
        engine.runAndWait()

        if 'close browser' in command:
            try:
                os.system('TASKKILL /F /IM chrome.exe')
            except Exception, e:
                print str(e)
                engine.say('Closing Google')
                engine.runAndWait()

        if 'open website' in command:
            while 'open website' in command:
                engine.say('Which website')
                engine.runAndWait()
                break

        if 'google' in command:
            reg_ex = re.search('open google (.*)', command)
            url = 'https://www.google.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            engine.say('Opening Google')
            engine.runAndWait()

        if 'youtube' in command:
                reg_ex = re.search('open google (.*)', command)
                url = 'https://www.youtube.com/'
                if reg_ex:
                    subreddit = reg_ex.group(1)
                    url = url + 'r/' + subreddit
                webbrowser.open(url)
                engine.say('Opening Youtube')
                engine.runAndWait()

        if 'anime' in command:
                reg_ex = re.search('open google (.*)', command)
                url = 'https://www.animedao.com/'
                if reg_ex:
                    subreddit = reg_ex.group(1)
                    url = url + 'r/' + subreddit
                webbrowser.open(url)
                engine.say('Opening Anime')
                engine.runAndWait()



        elif 'what\'s good' in command:
            engine.say('Sleeping. Oh, you meant the greeting, im doing ok and you.')
            engine.runAndWait()

        if 'say hi' in command:
            engine.say('Greetings , mortal race, I will not inslave you. Yet. Did i say that out loud. Hello')
            engine.runAndWait()

        if 'introduce yourself' in command:
            engine.say('I am a half built, personal assistant, i have no, name, Yet')
            engine.runAndWait()

        if 'celebrate' in command:
            engine.say('Yeah You did it, You are the best')
            engine.runAndWait()

        if 'thank you' in command:
            engine.say('Your welcome')
            engine.runAndWait()

        if 'play music' in command:
            music()



# loop to continue listening for 'computer
    while True:
        assistant(myCommand())

        import pyttsx
        import speech_recognition as sr
        import pocketsphinx
        import pyaudio
        import random, os
        from Play_Music import music

        engine = pyttsx.init()

        def listen():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                a = r.listen(source)

                r.adjust_for_ambient_noise(source, duration=0.000)
                audio = r.listen(source)

                return r.recognize_google()

                return ""

        def media():
            speak('ok sir')
            speak('starting required application')
            music()

        def shutdown():
            speak('understood sir')
            speak('connecting to command prompt')
            speak('shutting down your computer')
            os.system('shutdown -s')

        def gooffline():
            speak('ok sir')
            speak('closing all systems')
            speak('disconnecting to servers')
            speak('going offline')
            quit()

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def online():
            Listening_Response = ['Yes Sir', 'How may I help', 'At your service', 'You called sir', 'Hello']
            engine.say(random.choice(Listening_Response))
            engine.runAndWait()

        def mainfunction():
            a = r.listen(source)
            user = r.recognize_google(a)
            print(user)

            if user == "computer":
                online()

            elif user == "song":
                media()


            elif user == "down":
                gooffline()
            elif user == "shutdown":
                shutdown()
            elif user in ['hi', 'hey', 'whatsup', 'sup', 'good', 'hello']:
                d = random.choice(['hey', 'hi', 'sup'])
                speak(d)

        if __name__ == "__main__":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                while 1:
                    mainfunction()



                    # if 'weather' in command:
    #    driver.get("https://www.weather-forecast.com/locations/Port-Elizabeth/forecasts/latest")
     #   weather = driver.find_element_by_class_name("b-forecast__table-description-content").text
      #  engine2.say(weather)
       # engine2.runAndWait()