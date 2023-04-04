from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\Users\Manu\Desktop\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.python.org/events/python-events/")

x = driver.find_elements(By.CSS_SELECTOR, "time")

for time in x:
    print(time.text)
# event_name = driver.find_elements(by="css_selector", value=".event_widget a")

driver.quit()
