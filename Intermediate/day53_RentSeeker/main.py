import os
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_LINK = os.environ.get('Form_Link')
chrome_driver_path = os.environ.get('Driver_Path')
ZILLOW_LINK = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds' \
              '%22%3A%7B%22west%22%3A-122.65408553076172%2C%22east%22%3A-122.21257246923828%2C%22south%22%3A37.61582' \
              '637451368%2C%22north%22%3A37.93441331614561%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22' \
              'filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22' \
              'fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3' \
              'Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo' \
              '%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value' \
              '%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

# ----------------------Step 1. Scraping rent info website----------------------#
headers = {
    "Accept-Language": os.environ.get('Accept_Language'),
    "User-Agent": os.environ.get('User_Agent'),
}
response = requests.get(ZILLOW_LINK, headers=headers)
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup.prettify())

all_rent_elements = soup.select(selector='.property-card-data')
all_results = []
for element in all_rent_elements:
    address = element.find('address').getText()
    link = element.find('a').get('href')
    if 'https' not in link:
        link = f'https://www.zillow.com{link}'
    price = element.select(selector='div span')[0].getText()[:6]

    all_results.append({
        'address': address,
        'price': price,
        'link': link,
    })
print(len(all_results))

# ----------------------Step 2. Fill the Google form----------------------#
driver = webdriver.Chrome(executable_path=chrome_driver_path)
for result in all_results:
    driver.get(FORM_LINK)
    time.sleep(5)
    add_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_input.send_keys(result['address'])
    time.sleep(2)
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(result['link'])
    time.sleep(2)
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(result['price'])
    time.sleep(2)
    button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()
    time.sleep(2)

driver.quit()
