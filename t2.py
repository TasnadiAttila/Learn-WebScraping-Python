
from selenium import webdriver
from selenium.webdriver.common.by import By
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://bet.szerencsejatek.hu/jatekok/skandinavlotto/sorsolasok/")
#driver.get("https://bet.szerencsejatek.hu/jatekok/otoslotto/sorsolasok")
#driver.get("https://bet.szerencsejatek.hu/jatekok/hatoslotto/sorsolasok")

#papirrol kezzel beolvasott stuff
Mezo1 = [1,4,10,18,22,31,34]
Mezo2 = [3,5,16,18,24,30,35]
Mezo3 = [3,5,7,14,24,25,30]
Mezo4 = [1,2,6,14,19,30,31]
Mezo5 = [1,2,11,17,19,23,29]
Mezo6 = [2,4,12,18,21,23,35]

#Mezo1 = []
#Mezo2 = []
#Mezo3 = []
#Mezo4 = []
#Mezo5 = []
#Mezo6 = []

#autoAccpetCookies
cookie = driver.find_element(By.XPATH,'//button[@id="js-accept-all"]')
cookie.click()

#XD
ownWeek = 32

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
elif(len(WinningNumbers) == 14):
    for i in range(len(listB)):
        a = 0
        for j in range(len(list1)):
            if(list1[j] in listB[i]):
                a += 1
        print("Első sor: " + str(i+1) + ". sorban ennyi eggyezés van: " + str(a))

    for k in range(len(listB)):
        b = 0
        for l in range(len(list2)):
            if(list2[l] in listB[k]):
                b += 1
        print("Második: " + str(k+1) + ". sorban ennyi eggyezés van: " + str(b))


driver.close()



    






