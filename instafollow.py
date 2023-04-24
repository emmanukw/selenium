from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException

TARGET_FOLLOW = ""
USERNAME = ""
PASSWORD = ""

ser = Service(r"C:\Users\Manu\Desktop\Development\chromedriver.exe")
op = webdriver.ChromeOptions()


class InstaFollower:
    def __int__(self, driver_path):
        self.driver = webdriver.Chrome(service=ser, options=op)

    def log_in(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_FOLLOW}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, "'//*[@id='react-root']/section/main/div/header/section/ul/li["
                                                       "2]/a'")
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]")
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.log_in()
bot.find_followers()
bot.follow()
