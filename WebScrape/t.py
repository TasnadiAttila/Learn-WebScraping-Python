#C:\Users\tasna\OneDrive\Dokumentumok\WebScrape
#number selected unclickable
#https://bet.szerencsejatek.hu/jatekok/otoslotto/sorsolasok
#http://learnpython.atw.hu/
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests 
import pandas as pd 
from bs4 import BeautifulSoup
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://learnpython.atw.hu/")


s = driver.find_elements(By.XPATH,'//span')
for i in s:
    print(i.text)
