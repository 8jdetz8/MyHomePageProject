#! python3
# Homepage HTML Writer

import requests, webbrowser, random, os
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import praw
from PIL import Image
import urllib.request

#-------------------------------------------------------------------------
#Setting up reddit data scraping
#-------------------------------------------------------------------------
reddit = praw.Reddit(client_id = 'uhtUBYZOo53vCQ', \
                         client_secret = '3RoIQHse9V0RLKS-TGAOyW3nBFo', \
                         user_agent = 'myhomepage', \
                         username = 'Darnellthebeast', \
                         password = 'Darnell99')

template = '''
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
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
      <section class="weather">
        <a href="https://weather.com/weather/hourbyhour/l/23113:4:US">
        <img src = "C://Users/Student/Desktop/MyHomePageProject/Homepage messaround/sample_screenshot.png", alt = "weather table">
        </a>
      </section>
      <section class="xkcd">
        <a href="{comicUrl}"<p>Click here for a random XKCD Comic</p></a>
      </section>
      <section class="feeArticle">
          <a href="https://fee.org/"<p>Click here to find an FEE Article</p></a>
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
          <a href="{newsLink0}"<p>{news0}</p></a>
          <a href="{newsLink1}"<p>{news1}</p></a>
          <a href="{newsLink2}"<p>{news2}</p></a>
      </section>
      <section class="worldNewsLabel">
          <h2>In World News today:</h2>
      </section>
      <section class="worldNewsData">
        <a href="{worldNewsLink0}"<p>{world0}</p></a>
        <a href="{worldNewsLink1}"<p>{world1}</p></a>
        <a href="{worldNewsLink2}"<p>{world2}</p></a>
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
driver = webdriver.Chrome(executable_path='C:\\Users\Student\AppData\Local\Programs\Python\Python37-32\chromedriver\chromedriver.exe')
driver.get('https://www.google.com/search?q=weather+in+midlothian+va')
driver.save_screenshot('sample_screenshot.png')
imageObject = Image.open("C://Users/Student/MyHomePageProject/Homepage messaround/sample_screenshot.png")
cropped = imageObject.crop((225, 295, 1150, 770))
cropped.save("C://Users/Student/MyHomePageProject/Homepage messaround/sample_screenshot.png")
#925x473
#1554x794
#-------------------------------------------------------------------------
#Getting news data
#-------------------------------------------------------------------------
subreddit = reddit.subreddit('News')
newsPosts = []
newsLinks = []
for post in subreddit.hot(limit=3): #only want 3 posts
    newsPosts.append(post.title)
    newsLinks.append(post.url)
subreddit = reddit.subreddit('WorldNews')
worldNewsPosts = []
worldNewsLinks = []
for post in subreddit.hot(limit=3): #only want 3 posts
    worldNewsPosts.append(post.title)
    worldNewsLinks.append(post.url)
#-------------------------------------------------------------------------
#Getting HHH Posts
#-------------------------------------------------------------------------
subreddit = reddit.subreddit('HipHopHeads')
HHHPosts = []
for post in subreddit.hot(limit=50): #looking through first 50 posts
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
#Getting a random xkcd comic
#-------------------------------------------------------------------------
os.makedirs('xkcd', exist_ok=True)
comicNum = random.randint(1,2168)
driver.get("https://xkcd.com/" + str(comicNum))
res = requests.get("https://xkcd.com/" + str(comicNum))
soup = BeautifulSoup(res.text, features="lxml")
comicElem = soup.select('#comic img')
comicUrl = 'http:' + comicElem[0].get('src')
#-------------------------------------------------------------------------
#Establishing all values that will need to be displayed
#-------------------------------------------------------------------------

data = dict(
    date = rn.strftime('%A, %B %d %Y'),
    high = 'high',
    news0 = newsPosts[0],
    news1 = newsPosts[1],
    news2 = newsPosts[2],
    world0 = worldNewsPosts[0],
    world1 = worldNewsPosts[1],
    world2 = worldNewsPosts[2],
    hhh0 = HHHFresh[0],
    hhh1 = HHHFresh[1],
    hhh2 = HHHFresh[2],
    newsLink0 = newsLinks[0],
    newsLink1 = newsLinks[1],
    newsLink2 = newsLinks[2],
    worldNewsLink0 = worldNewsLinks[0],
    worldNewsLink1 = worldNewsLinks[1],
    worldNewsLink2 = worldNewsLinks[2],
    comicUrl = comicUrl
)
#-------------------------------------------------------------------------
#Inserting the values
#-------------------------------------------------------------------------

with open('todaysdate.html', 'w') as f:
    f.write(template.format(**data))

#-------------------------------------------------------------------------
#Closing the browser
#-------------------------------------------------------------------------
driver.quit()
#-------------------------------------------------------------------------
#Opening the homepage
#-------------------------------------------------------------------------
webbrowser.open('file://' + os.path.realpath('todaysdate.html'))
