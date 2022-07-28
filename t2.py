
from selenium import webdriver
from selenium.webdriver.common.by import By
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#driver.get("https://bet.szerencsejatek.hu/jatekok/skandinavlotto/sorsolasok/")
driver.get("https://bet.szerencsejatek.hu/jatekok/otoslotto/sorsolasok")
#driver.get("https://bet.szerencsejatek.hu/jatekok/hatoslotto/sorsolasok")

#papirrol kezzel beolvasott stuff
Mezo1 = []
Mezo2 = []
Mezo3 = []
Mezo5 = []
Mezo6 = []
Mezo7 = []
#autoAccpetCookies
cookie = driver.find_element(By.XPATH,'//button[@id="js-accept-all"]')
cookie.click()

#XD
ownWeek = 27

#get current week
def getCurrentWeek():
    s = ''
    f = driver.find_elements(By.XPATH,'//nav[@class="header"]//div[@class="week"]')
    for i in f:
        s = i.text
    s = s.split(". ")
    return s[1]
#get data
def getData():
    s = driver.find_elements(By.XPATH,'//span[@class="number selected unclickable"]')
    szamok = []
    for i in s:
        szamok.append(int(i.text))
    return szamok
#change the date
diff = int(getCurrentWeek()) - ownWeek
dt = 0
if(ownWeek < int(getCurrentWeek())):
    for i in range(diff):
        minusDate = driver.find_element(By.XPATH,'//span[contains(text(),"Előző hét")]')
        minusDate.click()
    #get Data
    dt = getData()
else:
    dt = getData()
#hetes lottonál van gépi és kézi is
list1 = [] #első sor
list2 = [] #második sor
if(len(dt)==14):
    for i in range(0,7):
        list1.append(dt[i])
    for i in range(7,14):
        list2.append(dt[i])
#########
#EREDMENYEK
#########


driver.close()



    






