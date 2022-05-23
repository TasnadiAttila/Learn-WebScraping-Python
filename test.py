from selenium import webdriver
PATH = "C:\Users\tasna\OneDrive\Dokumentumok\Python - Learn WebScraping\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://youtube.com")
print(driver.title)
driver.quit()