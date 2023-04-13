from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\Users\Manu\Desktop\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count_number = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")




