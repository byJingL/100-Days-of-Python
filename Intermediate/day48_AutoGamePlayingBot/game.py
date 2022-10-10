from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ----------------------Step 1. Drive the Web page----------------------#
URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "/Users/jinglu/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)


# ----------------------Step 2. Get the store items----------------------#
def get_items():
    store = driver.find_elements(By.CSS_SELECTOR, ".grayed b")
    items = [item.text.split(" - ") for item in store]
    items = list(reversed(items[:len(items)-1]))
    return items


# ----------------------Step 3. Check the dood to buy----------------------#
def buy_item(money, item_list):
    for item in item_list:
        if money > int(item[1].replace(",", "")):
            item_id = f"buy{item[0]}"
            item_to_buy = driver.find_element(By.ID, item_id)
            item_to_buy.click()
            return item_id


# ----------------------Step 4. Main Play Script----------------------#
cookie_button = driver.find_element(By.ID, "cookie")
item = get_items()

game_timeout = time.time() + 60 * 5
items_have = []
while time.time() < game_timeout:
    round_timeout = time.time() + 5
    while True:
        cookie_button.click()
        if time.time() > round_timeout:
            break
    cookies = driver.find_element(By.ID, "money")
    cookie_count = int(cookies.text.replace(",", ""))
    items_have.append(buy_item(money=cookie_count, item_list=item))

cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cps"]')

# ----------------------Step 5. Print Results----------------------#
print(len(items_have), items_have)
print(cookies_per_second.text)
driver.quit()


