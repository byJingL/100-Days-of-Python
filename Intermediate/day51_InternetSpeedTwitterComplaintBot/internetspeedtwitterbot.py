import time
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/jinglu/Development/chromedriver"
INTERNET_SPEED = "https://www.speedtest.net/"
TWEETER = "https://twitter.com/i/flow/login"
NEXT1_PATH = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/' \
             'div[2]/div[2]/div/div/div/div[6]/div/span/span'


class InternetSpeedTwitterBot:
    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    # ------------------------Get Internet Speed-----------------------#
    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED)
        time.sleep(1)
        # Click Privacy Button
        privacy = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        privacy.click()
        time.sleep(2)
        # Click Go Button
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()
        # Wait for Result and Save
        time.sleep(60)
        speed1 = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.down = speed1.text
        speed2 = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = speed2.text
        time.sleep(2)

    # ----------------Log in Tweeter and Tweet------------------#
    def tweet_at_provider(self, account, acc_name, password, text):
        self.driver.get(TWEETER)
        time.sleep(3)
        # ------------Log in---------#
        # Account
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(account)
        time.sleep(2)
        next1 = self.driver.find_element(By.XPATH, NEXT1_PATH)
        next1.click()
        time.sleep(3)
        # Account Name
        name = self.driver.find_element(By.NAME, "text")
        name.send_keys(acc_name)
        time.sleep(2)
        next2 = self.driver.find_element(By.CSS_SELECTOR, ".r-pw2am6 div div span")
        next2.click()
        time.sleep(3)
        # Password
        pw = self.driver.find_element(By.NAME, "password")
        pw.send_keys(password)
        time.sleep(2)
        next3 = self.driver.find_element(By.CSS_SELECTOR, ".r-pw2am6 div div span")
        next3.click()
        time.sleep(3)

        # ----------tweet-----------#
        box = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftEditor-content div div div span")
        box.send_keys(text)
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                          'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div'
                                                          '/div/div[2]/div[3]/div/span/span')
        tweet.click()

