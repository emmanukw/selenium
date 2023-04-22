from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

GMAIL_EMAIL = "maxreproach@gmail.com"
GMAIL_PASSWORD = "Gavialbert2015!"

ser = Service(r"C:\Users\Manu\Desktop\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, '("//*[text()="Log in"]")')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# list1 = []
# list2 = []
#
# event_time = driver.find_elements(By.CSS_SELECTOR, "time")
# event_name = driver.find_elements(By.CLASS_NAME, "event-title")
#
# my_dict = {}
# for i in range(len(event_time)):
#     my_dict[event_time[i].text] = event_name[i].text
# print(my_dict)
#

driver.quit()
