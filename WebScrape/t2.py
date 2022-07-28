from selenium import webdriver
from selenium.webdriver.common.by import By
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://bet.szerencsejatek.hu/jatekok/otoslotto/sorsolasok")


s = driver.find_elements(By.XPATH,'//span[@class="number selected unclickable"]')
for i in s:
    print(i.text)

driver.close()