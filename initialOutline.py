#! python3
# dailyDataScraper - Scrapes data from my favorite websites every morning,
# presenting everything I need in a clean, concise way.

import os, requests, webbrowser, re
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')

#Done: Tell me what day it is
driver.get('https://www.google.com/search?q=what+is+today%27s+date')
dateHTML = BeautifulSoup(driver.page_source, "lxml")
date = dateHTML.find('div' , {'class': 'vk_bk dDoNo'})

#TODO: Get the high temperature for midlothian for the day
driver.get('https://weather.com/weather/today/l/28feca8e43465556bc0c70403b638f1433c3c769a9a430f433ce81f027b5e112')
weatherHTML = BeautifulSoup(driver.page_source, "lxml")
weatherTable = weatherHTML.find_all('div' , {'class': 'today_nowcard-hilo'})
highTempRegex = re.compile(r'\d\d\d?')
Temps = highTempRegex.search(str(weatherTable))


#TODO: Display a todo list of things I need to do(classes, hw, work)

#TODO: Print info related to my money.

#TODO: Get the top 3 posts from r/news and r/worldnews

#TODO: Display everything in a better interface rather than just printing it.

print('Today\'s date is' + date.text)
print('The high temperature today in Midlothian is ' + Temps[0])

