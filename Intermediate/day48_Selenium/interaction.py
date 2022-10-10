from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "/Users/jinglu/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

# Click the link
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)
# article_count.click()
portals = driver.find_element(By.LINK_TEXT, "Community portal")
# portals.click()

# Type in Search bar and go
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
