from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\Users\Manu\Desktop\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.python.org/events/python-events/")

list1 = []
list2 = []

event_time = driver.find_elements(By.CSS_SELECTOR, "time")
event_name = driver.find_elements(By.CLASS_NAME, "event-title")

my_dict = {}
for i in range(len(event_time)):
    my_dict[event_time[i].text] = event_name[i].text
print(my_dict)


driver.quit()
