from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "/Users/jinglu/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Billie")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Eilish")
mail = driver.find_element(By.NAME, "email")
mail.send_keys("billie.eilish@gmail.com")
button = driver.find_element(By.XPATH, "/html/body/form/button")
button.click()
