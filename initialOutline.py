#! python3
# dailyDataScraper - Scrapes data from my favorite websites every morning,
# presenting everything I need in a clean, concise way.

import requests, webbrowser, re, time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import praw

print('JD, what\'s your reddit password?')
myPassword = input()
reddit = praw.Reddit(client_id = 'uhtUBYZOo53vCQ', \
                         client_secret = '3RoIQHse9V0RLKS-TGAOyW3nBFo', \
                         user_agent = 'myhomepage', \
                         username = 'darnellthebeast', \
                         password = myPassword)

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
    weatherTable = weatherHTML.find_all('div' , {'class': 'today_nowcard-hilo'})
    highTempRegex = re.compile(r'\d\d\d?')
    Temps = highTempRegex.search(str(weatherTable))
    print('The high temperature today in Midlothian is ' + Temps[0])

#TODO: Display a todo list of things I need to do(classes, hw, work)

#Done: Get the top 3 posts from r/news and r/worldnews
def getNews():
    subreddit = reddit.subreddit('News')
    newsPosts = []
    for post in subreddit.hot(limit=3): #only want 3 posts
        newsPosts.append(post.title)
    print('\nIn US News today:\n')
    for i in range(len(newsPosts)):
        print(newsPosts[i])
    subreddit = reddit.subreddit('WorldNews')
    worldNewsPosts = []
    for post in subreddit.hot(limit=3): #only want 3 posts
        worldNewsPosts.append(post.title)
    print('\nIn World News today: \n')
    for i in range(len(worldNewsPosts)):
        print(worldNewsPosts[i])

#Done: Get any new music from reddit.com/r/hiphopheads
def getHHH():
    subreddit = reddit.subreddit('HipHopHeads')
    HHHPosts = []
    for post in subreddit.hot(limit=35): #looking through first 35 posts
        HHHPosts.append(post.title) #post.title only gets titles
    c = 0
    print('\nRecent hip hop releases:\n')
    for i in range(len(HHHPosts)):
        if 'fresh' in str.lower(HHHPosts[i]) and 'video' not in str.lower(HHHPosts[i]): #dont want fresh videos
            print(HHHPosts[i])
            c += 1
        if c == 3: #stop after three posts
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
