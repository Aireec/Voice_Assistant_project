import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
import SendKeys
import pyautogui
from googlesearch.googlesearch import GoogleSearch

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

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


    return search

def speak(text):
    engine.say(text)
    engine.runAndWait()

def google():
    speak('Opening google')
    speak('Any thing you want me to search')
    voiceI = browser_search()


    browser = webdriver.Firefox()
    browser.get("http://www.google.com")
    input_element = browser.find_element_by_name("q")
    input_element.send_keys(voiceI)
    input_element.submit()


def close_browser():
    webdriver.Firefox.close()