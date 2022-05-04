# Automate WebApps
# pip install Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.example.com/")
# Finding Elements
# driver.find_element_by_id("id")
# driver.find_element_by_name("name")
# driver.find_element_by_class_name("class name")
# driver.find_element_by_tag_name("tag")
# driver.find_element_by_link_text("link text")
# driver.find_element_by_xpath("xpath")
# driver.find_element_by_css_selector("css")
# # Finding Elements with Wait
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id")))
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "xpath")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id")))
# # Click on Element
# driver.find_element_by_id("id").click()
# # Send keys or Type
# driver.find_element_by_id("id").send_keys("Keys")
# # Press Enter or Keys
# driver.find_element_by_id("id").send_keys(Keys.ENTER)
# # Mouse Hover
# ActionChains(driver).move_to_element(driver.find_element_by_id("id")).perform()
# # Quit Browser
# driver.quit()
# Refresh Browser
driver.refresh()

# driver.quit()