
# JCZ 3-Apr-2018
# Project to automate backup downloads from mantishub

# https://se.mantishub.io/manage_backup_page.php
# input id  =  "username"  jzastrow 
# input id  =  "password"  pw= ----

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


USERFIELD = (By.ID, "username")
PASSWORDFIELD = (By.ID, "password")
NEXTBUTTON = (By.ID, "submit")
LOGINBUTTON = (By.ID, "submit")

browser = webdriver.Chrome()
browser.get('https://se.mantishub.io/manage_backup_page.php')

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(USERFIELD)).send_keys("myEmailAddress")

# Click Login to go to the next screen
# driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click())
browser.find_element_by_xpath("//input[@type='submit']").click()

browser.quit()
browser.close()