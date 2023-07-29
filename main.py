from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.plusvalia.com")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#react-filters-form > form > div > div.search-box-container > div > div > ul > div > input")
search_box.send_keys("Manta")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#react-filters-form > form > div > div.sc-fPXMVe.kmIKmV > button")
search_button.click()

driver.close()