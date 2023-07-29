from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ecuador.patiotuerca.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="search-list")
search_box.send_keys("Manta")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="openSearch > div > div > div.search-ots.false > ing")
search_button.click()

vehicle_card = driver.find_elements(By.CSS_SELECTOR, "#featuredUsed > div")

driver.close()