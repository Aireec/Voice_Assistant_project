import os
import webbrowser
import pyttsx
import speech_recognition as sr
from selenium import webdriver
import SendKeys
import pyautogui
import random
engine = pyttsx.init()

def browser_search():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.000)
        audio = r.listen(source)

    try:
        search = r.recognize_google(audio).lower()
        print('You said: ' + search + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')


    return ""


def thank_you():
    thankU_Response = ['Your welcome', 'My Pleasure', 'At your service', 'Just doing my job', 'Can I get some sleep now',
                        'Do I get a raise']
    engine.say(random.choice(thankU_Response))
    engine.runAndWait()
