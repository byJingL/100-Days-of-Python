from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://www.boots.com/philips-sonicare-diamondclean-9000-electric-toothbrush-with-app-pink-hx9911-53-10282675?" \
      "cm_mmc=bmm-buk-google-ppc-_-LIAs-_-Electrical_Beauty-_-UK_Smart_Shopping_LIAs_Electrical_Beauty&gclid" \
      "=CjwKCAjw-L-ZBhB4EiwA76YzOVMiqY_TD7EagJA1j68aHiDchM8qiGmGCCDVl1h1UsQATt5ijSLipxoCnyMQAvD_BwE&gclsrc=aw.ds"
chrome_driver_path = "/Users/jinglu/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# open the webpage
driver.get(URL)
# ---------------------------Find elements by ID--------------------------#
product = driver.find_element(by="id", value="estore_product_title")
print(product)
print(product.text)
price = driver.find_element(By.ID, value="PDP_productPrice")
print(price)
print(price.text)
print(price.get_attribute("class"))

# # ------------------Find elements by Name and Class name----------------#
search_bar = driver.find_element(By.NAME, "searchTerm")
print(search_bar.tag_name)
print(search_bar.get_attribute("title"))
review_star = driver.find_element(By.CLASS_NAME, "bv_stars_component_container")
print(review_star)
print(review_star.size)

# ----------------------Find elements by CSS Selector----------------------#
links = driver.find_elements(By.CSS_SELECTOR, ".left_espot div p a")
for link in links:
    print(link.text)
    print(link.get_attribute("href"))

# ----------------------Find elements by Xpath----------------------#
logo_link = driver.find_element(By.XPATH, "//*[@id='logo']/a")
print(logo_link.get_attribute("href"))

# close one tag
# driver.close()
# close whole browser
driver.quit()
