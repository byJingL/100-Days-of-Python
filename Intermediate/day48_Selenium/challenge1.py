from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'
chrome_driver_path = "/Users/jinglu/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li a")

upcoming_events = {}
for i in range(0, len(event_times)):
    upcoming_events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }
print(upcoming_events)

driver.quit()
