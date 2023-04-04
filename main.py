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
for i in event_time:
    list1.append(i.text)

event_name = driver.find_elements(By.CLASS_NAME, "event-title")
for i in event_name:
    list2.append(i.text)

my_dict = {}
for i in range(len(list1)):
    my_dict[list1[i]] = list2[i]
print(my_dict)


driver.quit()
