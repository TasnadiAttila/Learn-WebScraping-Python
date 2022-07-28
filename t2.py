
from selenium import webdriver
from selenium.webdriver.common.by import By
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#driver.get("https://bet.szerencsejatek.hu/jatekok/skandinavlotto/sorsolasok/")
driver.get("https://bet.szerencsejatek.hu/jatekok/otoslotto/sorsolasok")
#driver.get("https://bet.szerencsejatek.hu/jatekok/hatoslotto/sorsolasok")

#papirrol kezzel beolvasott stuff
Mezo1 = [1,2,49,4,83,4]
Mezo2 = [6,7,49,9,10,6]
Mezo3 = [11,12,13,14,18,5]
Mezo4 = [15,16,83,18,19,45]
Mezo5 = [49,11,52,43,19,74]
Mezo6 = [49,51,54,62,83,4]
#autoAccpetCookies
cookie = driver.find_element(By.XPATH,'//button[@id="js-accept-all"]')
cookie.click()

#XD
ownWeek = 29

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
WinningNumbers = 0
if(ownWeek < int(getCurrentWeek())):
    for i in range(diff):
        minusDate = driver.find_element(By.XPATH,'//span[contains(text(),"Előző hét")]')
        minusDate.click()
    #get Data
    WinningNumbers = getData()
else:
    WinningNumbers = getData()
#hetes lottonál van gépi és kézi is
list1 = [] #első sor
list2 = [] #második sor
if(len(WinningNumbers) == 14):
    for i in range(0,7):
        list1.append(WinningNumbers[i])
    for i in range(7,14):
        list2.append(WinningNumbers[i])
#########
#EREDMENYEK
#########
listB = []

listB.append(Mezo1)
listB.append(Mezo2)
listB.append(Mezo3)
listB.append(Mezo4)
listB.append(Mezo5)
listB.append(Mezo6)

if(len(WinningNumbers) == 5 or len(WinningNumbers) == 6):
    for i in range(len(listB)):
        a = 0
        for j in range(len(WinningNumbers)):
            if(WinningNumbers[j] in listB[i]):
                a += 1
        print(str(i+1) + ". sorban ennyi eggyezés van: " + str(a))            


if(len(WinningNumbers) == 14):

    for i in range(len(listB)):
        a = 0
        for j in range(len(list1)):
            if(list1[j] in listB[i]):
                a += 1
        print("Első sor: " + str(i+1) + ". sorban ennyi eggyezés van: " + str(a))

    for i in range(len(listB)):
        a = 0
        for j in range(len(list2)):
            if(list2[j] in listB[i]):
                a += 1
        print("Második sor: " + str(i+1) + ". sorban ennyi eggyezés van: " + str(a))


driver.close()



    






