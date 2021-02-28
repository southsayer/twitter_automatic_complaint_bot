from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PROMISED_DOWN = 150
PROMISED_UP = 10

PASSWORD = "********"
EMAIL = "AkshitG16128987"

URL = "https://twitter.com/home"
CHROME_DRIVER_PATH = "C:\devlopment\chromedriver_win32\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net')
        self.driver.find_element_by_class_name('start-button').click()
        time.sleep(50)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        # self.driver.close()


    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/login")
        time.sleep(2)
        self.email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        self.email.send_keys(EMAIL)

        time.sleep(2)
        self.password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        self.password.send_keys(PASSWORD)

        time.sleep(2)
        self.password.send_keys(Keys.ENTER)

        time.sleep(2)
        self.enter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        MESSAGE = f"Hey @airtelindia, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.enter.send_keys(MESSAGE)

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div').click()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
if float(bot.down) < 150 or float(bot.up) < 10:
    bot.tweet_at_provider()

print(bot.down)
print(bot.up)
