import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
import SendKeys
import pyautogui

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

def song_choice():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.000)
        audio = r.listen(source)

    try:
        song = r.recognize_google(audio).lower()
        print('You said: ' + song + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        return song

def speak(text):
    engine.say(text)
    engine.runAndWait()

def spotify():
    speak('opening spotify')
    speak('what do you want me to play for you')
    s = song_choice()
    speak('ok sir playing' + s + 'for you')

def youtube():

    speak('Opening youtube')
    speak('what would you like me to play')
    y = song_choice()
    browser = webdriver.Firefox()
    browser.get("http://www.youtube.com")
    input_element = browser.find_element_by_css_selector('input.ytd-searchbox')
    input_element.send_keys(y)
    input_element.submit()


