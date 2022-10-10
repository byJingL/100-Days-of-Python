import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3259779546&f_TPR=r86400&geoId=102257491&keywords=python' \
      '%20developer'
chrome_driver_path = '/Users/jinglu/Development/chromedriver'
ACCOUNT = os.environ.get("ACCOUNT")
PASSWORD = os.environ.get("PASSWORD")

# ----------------------Step 1. Drive the Web page----------------------#
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
time.sleep(2)
# -----------------------Step 2. Sign in the web-----------------------#
log_in = driver.find_element(By.LINK_TEXT, "Sign in")
log_in.click()
time.sleep(1)

username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
log_in_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
log_in_button.click()
time.sleep(1)

# ---------------------Step 3. Save the first job-----------------------#
# save_first = driver.find_element(By.CLASS_NAME, "jobs-save-button")
# save_first.click()

# -----------------Step 4. Save all the jobs in the page-------------------#
jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for job in jobs[:7]:
    job.click()
    time.sleep(2)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    time.sleep(1)
    save_button.click()
    time.sleep(2)

    # close the save notification
    close_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button__icon svg')
    time.sleep(1)
    close_button.click()
    time.sleep(2)

driver.quit()

