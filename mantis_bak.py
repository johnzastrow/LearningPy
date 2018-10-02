# JCZ 3-Apr-2018
# Project to automate backup downloads from mantishub

# https://se.mantishub.io/manage_backup_page.php
# input id  =  "username"  jzastrow
# input id  =  "password"  pw= ----

# allow us to control time flow in script
import time

# The selenium.webdriver module provides all the WebDriver implementations.
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Allows the UI to wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

# Items needed to allow Chrome to download a file
# download_dir = "/home/jcz/github/LearningPy"
# chrome_options = webdriver.ChromeOptions()
# preferences = {"download.default_directory": download_dir ,
#                      "directory_upgrade": True,
#                      "safebrowsing.enabled": True }
# chrome_options.add_experimental_option("prefs", preferences)
# driver = webdriver.Chrome(chrome_options=chrome_options)

# useful variables
USERFIELD = (By.ID, "username")
PASSWORDFIELD = (By.ID, "password")
NEXTBUTTON = (By.ID, "submit")
LOGINBUTTON = (By.ID, "submit")

# The driver.get method will navigate to a page given by the URL.
# WebDriver will wait until the page has fully loaded (that is, the “onload”
# event has fired) before returning control to your test or script.
# It’s worth noting
# that if your page uses a lot of AJAX on load then WebDriver may not
# know when it has completely loaded.:
# browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.implicitly_wait(10)
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)  # custom location
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "/home/jcz/github/LearningPy")
profile.set_preference(
    "browser.helperApps.neverAsk.saveToDisk", "application/x-gzip-compressed"
)

browser = webdriver.Firefox(profile)
browser.get("https://se.mantishub.io/manage_backup_page.php")

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(USERFIELD)).send_keys(
    "jzastrow@syseng.com"
)

# Click Login to go to the next screen
# driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click())
browser.find_element_by_xpath("//input[@type='submit']").click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(
    "mj9230DQ@"
)

# Click Login to go to the next screen
# driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click())
browser.find_element_by_xpath("//input[@type='submit']").click()

# https://se.mantishub.io/manage_backup_download.php?type=data
browser.find_element_by_partial_link_text("database").click()

browser.find_element_by_partial_link_text("attach").click()

# browser.quit()
# browser.close()
