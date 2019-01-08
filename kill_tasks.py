import os
import webbrowser
import re
import requests
import speech_recognition as sr
import pyttsx
from selenium import webdriver


engine = pyttsx.init()


try:
    os.system('TASKKILL /F /IM firefox.exe')
except Exception, e:
    print str(e)
    engine.say('Closing Google')
    engine.runAndWait()