import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

PROMISED_UPLINK = 150
PROMISED_DOWNLINK = 50
TWITTER_EMAIL = "maxreproach@gmail.com"
TWITTER_PASSWORD = "Gavialbert2015!"
CHROME_PATH = r'C:\Users\Manu\Desktop\Development\chromedriver.exe'

ser = Service(CHROME_PATH)
op = webdriver.ChromeOptions()


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div["
                                                       "3]/div[1]/a/span[4]")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                     "3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div["
                                                       "3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div["
                                                       "2]/span")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div['
                                         '1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div['
                                            '2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                 '2]/div/div[2]/div[1]/div/div/div/div['
                                                 '2]/div[1]/div/div/div/div/div/div/div/div/div/div['
                                                 '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWNLINK}down/{PROMISED_UPLINK}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                '2]/div/div[2]/div[1]/div/div/div/div['
                                                '2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
