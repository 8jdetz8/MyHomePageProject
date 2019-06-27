#! python3
# Homepage HTML Writer

import requests, webbrowser, re, time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import praw

template = '''
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Styles Conference</title>
    <link rel="stylesheet" href="Stylesheets/newmain.css">
  </head>
  <header>
      <section class="greeting">
          <h1>Good morning, JD.</h1>
  </header>
  <body>
      <section class="dateLabel">
          <h2>Today's Date:</h2>
          <section class="actualDate">
            <h3><b>{date}</b></h3>
          </section>
      </section>
      <section class="weather"
          <h2>The high temperature in Midlothian today is high</h2>
      </section>
      <section class="hhhLabel">
          <h2>Recent Hip Hop releases:</h2>
      </section>
      <section class="hhhData">
          <p>{hhh0}</p>
          <p>{hhh1}</p>
          <p>{hhh2}</p>
      </section>
      <section class="newsLabel">
          <h2>In US News today:</h2>
      </section>
      <section class="newsData">
          <p>{news0}</p>
          <p>{news1}</p>
          <p>{news2}</p>
      </section>
      <section class="worldNewsLabel">
          <h2>In World News today:</h2>
      </section>
      <section class="worldNewsData">
        <p>{world0}</p>
        <p>{world1}</p>
        <p>{world2}</p>
      </section>
  </html>
'''
#-------------------------------------------------------------------------
#Getting the date
#-------------------------------------------------------------------------
rn = datetime.datetime.today()

#-------------------------------------------------------------------------
#Getting the weather
#-------------------------------------------------------------------------
#driver = webdriver.Chrome(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
#driver.get('https://weather.com/weather/today/l/28feca8e43465556bc0c70403b638f1433c3c769a9a430f433ce81f027b5e112')
#weatherHTML = BeautifulSoup(driver.page_source, "lxml")
#weatherTable = weatherHTML.find_all('div' , {'class': 'today_nowcard-hilo'})
#highTempRegex = re.compile(r'\d\d\d?')
#Temps = highTempRegex.search(str(weatherTable))
#-------------------------------------------------------------------------
#Setting up reddit data scraping
#-------------------------------------------------------------------------
reddit = praw.Reddit(client_id = 'uhtUBYZOo53vCQ', \
                         client_secret = '3RoIQHse9V0RLKS-TGAOyW3nBFo', \
                         user_agent = 'myhomepage', \
                         username = 'darnellthebeast', \
                         password = 'Tigger99')
#-------------------------------------------------------------------------
#Getting news data
#-------------------------------------------------------------------------
subreddit = reddit.subreddit('News')
newsPosts = []
for post in subreddit.hot(limit=3): #only want 3 posts
    newsPosts.append(post.title)
subreddit = reddit.subreddit('WorldNews')
worldNewsPosts = []
for post in subreddit.hot(limit=3): #only want 3 posts
    worldNewsPosts.append(post.title)
#-------------------------------------------------------------------------
#Getting HHH Posts
#-------------------------------------------------------------------------
subreddit = reddit.subreddit('HipHopHeads')
HHHPosts = []
for post in subreddit.hot(limit=35): #looking through first 35 posts
    HHHPosts.append(post.title) #post.title only gets titles
c = 0
HHHFresh = []
for i in range(len(HHHPosts)):
    if 'fresh' in str.lower(HHHPosts[i]) and 'video' not in str.lower(HHHPosts[i]): #dont want fresh videos
        HHHFresh.append(HHHPosts[i])
        c += 1
    if c == 3: #stop after three posts
        break
#-------------------------------------------------------------------------
#Establishing all values that will need to be displayed
#-------------------------------------------------------------------------
data = dict(
    date = rn.strftime('%A, %B %d %Y'),
   # high = Temps[0],
    news0 = newsPosts[0],
    news1 = newsPosts[1],
    news2 = newsPosts[2],
    world0 = worldNewsPosts[0],
    world1 = worldNewsPosts[1],
    world2 = worldNewsPosts[2],
    hhh0 = HHHFresh[0],
    hhh1 = HHHFresh[1],
    hhh2 = HHHFresh[2]
)
#-------------------------------------------------------------------------
#Inserting the values
#-------------------------------------------------------------------------

with open('todaysdate.html', 'w') as f:
    f.write(template.format(**data))


