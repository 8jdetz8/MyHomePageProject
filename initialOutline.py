#! python3
# dailyDataScraper - Scrapes data from my favorite websites every morning,
# presenting everything I need in a clean, concise way.

import requests, webbrowser, re, time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime

driver = webdriver.Chrome(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')

#TODO: Find a way to avoid reddit ads

#Done: Put everything in functions for better organization.

#Done: Complete day and time using a time module instead of googling.
def getDate():
    rn = datetime.datetime.today()
    print(rn.strftime('Today is %A, %B %d %Y'))

#Done: Get the high temperature for midlothian for the day
def getHighTemp():
    driver.get('https://weather.com/weather/today/l/28feca8e43465556bc0c70403b638f1433c3c769a9a430f433ce81f027b5e112')
    weatherHTML = BeautifulSoup(driver.page_source, "lxml")
    weatherTable = weatherHTML.find_all('div' , {'class': 'today_nowcard-hilo'}) #Finding the HiandLow temperatures
    highTempRegex = re.compile(r'\d\d\d?') #Two to three digits for temperature
    Temps = highTempRegex.search(str(weatherTable)) 
    print('The high temperature today in Midlothian is ' + Temps[0]) #The high temp is first in Temps, if I wanted low would use [1]

#TODO: Display a todo list of things I need to do(classes, hw, work)

#Done: Get the top 3 posts from r/news and r/worldnews
def getNews():
    driver.get('https://www.reddit.com/r/news/')
    newsHTML = BeautifulSoup(driver.page_source, "lxml")
    newsTitles = newsHTML.find_all('h3' , {'class': '_eYtD2XCVieq6emjKBH3m'})
    print('\nIn US News: \n')
    for i in range(3):  #3 highest posts on News
        print(newsTitles[i].getText())
    driver.get('https://www.reddit.com/r/worldnews/')
    worldnewsHTML = BeautifulSoup(driver.page_source, "lxml")
    worldnewsTitles = worldnewsHTML.find_all('h3' , {'class': '_eYtD2XCVieq6emjKBH3m'})
    print('\nIn World News: \n') #3 highest posts on Worldnews
    for i in range(3):
        print(worldnewsTitles[i].getText())

#Done: Get any new music from reddit.com/r/hiphopheads
def getHHH():
    driver.get('https://www.reddit.com/r/hiphopheads/')
    hiphopheadsHTML = BeautifulSoup(driver.page_source, "lxml")
    allHHHTitles = hiphopheadsHTML.find_all('h3') #allHHHTitles is a bs4.element.resultset
    result = []
    for title in allHHHTitles:  #moving allHHHTitles text to a list
        result.append(title.text)
    freshRegex = re.compile(r'\[Fresh(\salbum)?\]', re.IGNORECASE | re.VERBOSE) #Only want fresh and fresh album tags.
    freshStuff = list(filter(freshRegex.match, result)) #Removing everything without fresh
    print('\nRecent music releases:')
    for i in range(len(freshStuff)):
        if len(freshStuff) == 0: #check to see if anything in list.
            print('No new music today.') 
        else:
            print(freshStuff[i])
            if i == 2: #prints up to the first three matches.
                break


#UNFINISHED: Get info related to my money.
#CANNOT SOLVE PROBLEM OF TWO FACTOR AUTHENTICATION AT THIS TIME
#HAVE NOT TESTED AMERICAN EXPRESS YET. 

#print('What is your union username?')
#unionUsername = input()
#print('What is your union password?')
#unionPW = input()
#driver.get('https://www.atlanticunionbank.com/')
#unionLoginToggle = driver.find_element_by_id('loginToggle')
#time.sleep(5)
#unionLoginToggle.click()
#time.sleep(1)
#unionLoginInput = driver.find_element_by_id('userid')
#unionLoginInput.send_keys(unionUsername)
#time.sleep(1)
#unionPasswordInput = driver.find_element_by_id('password')
#unionPasswordInput.send_keys(unionPW)
#time.sleep(1)
#unionPasswordInput.send_keys(Keys.ENTER)

#TODO: Display everything in a better interface rather than just printing it.
getDate()
getHighTemp()
getNews()
getHHH()
