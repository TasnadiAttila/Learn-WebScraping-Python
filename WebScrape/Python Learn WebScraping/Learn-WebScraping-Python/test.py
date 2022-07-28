from selenium import webdriver
PATH = "C:\Program Files (x86)\Python Learn WebScraping\Learn-WebScraping-Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")
print(driver.title)
driver.quit()