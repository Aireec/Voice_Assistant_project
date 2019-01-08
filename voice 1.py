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
from Play_Music import spotify
from Play_Music import youtube
from Browser import google
from Browser import close_browser
from talking import thank_you
from Opening import opening
from weather import weather



# Talking engine for A.I
engine = pyttsx.init()
# setting speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 100)



i = 1
while i < 2:
    opening()
    if i == 2:
        break
    i += 1

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

        if 'close browser' in command:
            close_browser()

        if 'google' in command:
            google()

        if 'thank you' in command:
            thank_you()

        if 'weather' in command:
            weather()

        if 'play music' in command:
            engine.say('where would you like me to play')
        engine.runAndWait()
        choice = myCommand()

        if 'youtube' in choice:
            youtube()

        elif 'spotify' in choice:
            spotify()




# loop to continue listening for 'computer
    while True:
        assistant(myCommand())