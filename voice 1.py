import os
import webbrowser
import re
import requests
import speech_recognition as sr
import pyttsx


engine = pyttsx.init()
engine2 = pyttsx.init()
engine3 = pyttsx.init()
engine4 = pyttsx.init()

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        engine.say('Awaiting orders, my king')
        engine.runAndWait()

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

class Weather(object):
    pass


def assistant(command):
    "if statements for executing commands"

    if 'nicole' in command:
        engine.say('A-reec, loves you, Nichol')
        engine.runAndWait()

    if 'rap like a' in command:
        engine.say('Computer, must be, in my, genes')
    engine.runAndWait()

    if 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        engine.say('Done')
        engine.runAndWait()

    elif 'close google' in command:
        try:
            os.system('TASKKILL / F / chrome.exe')
        except Exception, e:
            print str(e)


    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s good' in command:
        engine.say('Sleeping. Oh, you meant the greeting, im doing ok and you.')
        engine.runAndWait()
    elif 'joke' in command:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            print ""
        else:
            talkToMe('oops!I ran out of jokes')


    elif ' the weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (
            city, condition.text(), (int(condition.temp()) - 32) / 1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0, 3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (
                         forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high()) - 32) / 1.8,
                         (int(forecasts[i].low()) - 32) / 1.8))

    if 'say hi' in command:
        engine2.say('Greetings , mortal race, I will not inslave you. Yet. Did i say that out loud. Hello')
    engine2.runAndWait()

    if 'introduce yourself' in command:
        engine3.say('I am a half built, personal assistant, i have no, name, Yet')
        engine3.runAndWait()

        if 'bars' in command:
            engine.say('chocolate')
        engine.runAndWait()
# loop to continue executing multiple commands
while True:
    assistant(myCommand())