import pyttsx3
from selenium import webdriver

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 85)

def weather():
        driver = webdriver.Firefox()
        driver.get("https://www.weather-forecast.com/locations/Port-Elizabeth/forecasts/latest")
        weather = driver.find_element_by_class_name("b-forecast__table-description-content").text
        engine.say(weather)
        engine.runAndWait()

        driver.quit()