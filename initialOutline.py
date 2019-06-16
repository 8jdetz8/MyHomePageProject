#! python3
# dailyDataScraper - Scrapes data from my favorite websites every morning,
# presenting everything I need in a clean, concise way.

import os, requests, webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver

#TODO: Tell me what day it is
driver = webdriver.Chrome(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
driver.get('https://www.google.com/search?q=what+is+today%27s+date')
html = BeautifulSoup(driver.page_source, "lxml")
date = html.find('div' , {'class': 'vk_bk dDoNo'})
#TODO: Get the high temperature for midlothian for the day

#TODO: Display a todo list of things I need to do(classes, hw, work)

#TODO: Print info related to my money.

#TODO: Get the top 3 posts from r/news and r/worldnews

#TODO: Display everything in a better interface rather than just printing it.

Print('Today\'s date is ' + date.text)

