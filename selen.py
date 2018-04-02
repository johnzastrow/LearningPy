from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()

# Code line 1: From selenium module import webdriver
# Code line 2: From selenium module import Keys
# Code line 3: User is a blank variable which will be we used to store values of username.
# Code line 4: pwd is also a blank (here it is empty, but the user can provide values in it) variable. This will be used to store values of the password.
# Code line 5: In this line, we are initializing "FireFox" by making an object of it.
# Code line 6: The "driver.get method" will explore to a page given by the URL.WebDriver will hold up until the page has completely been loaded 
# (that is, the "onload" occasion has let go), before returning control to your test or script.
# Code line 7: "Asserts" keyword is used to verify the conditions. In this line, we are confirming whether the title is correct or not. For that, 
# we will compare the title with the string which is given.
# Code line 8: In this line, we are finding the element of the textbox where the "email" has to be written.
# Code line 9: Now we are sending the values to the email section
# Code line 10: Same for the password
# Code line 11: Sending values to the password section
# Code line 12: Elem.send_keys(Keys.RETURN) is used to press enter after the values are inserted
# Code line 13: Close


from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Firefox()
browser.get( www.facebook.com )
  
username = browser.find_element_by_id( "guru99" )
password = browser.find_element_by_id( "password@123" )
submit   = browser.find_element_by_id( "submit"   )
  
username.send_keys( "me" )
password.send_keys( "mykewlpass" )
  

submit.click()
  

wait = WebDriverWait( browser, 5 )
  
try:
page_loaded = wait.until_not(
lambda browser: browser.current_url == login_page
)
except TimeoutException:
self.fail( "Loading timeout expired" )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)


# Code line 1-2: Import selenium package
# Code line 4: Initialize Firefox by creating an object
# Code line 5: Get login page (Facebook)
# Code line 7-9: Fetch username, password input boxes and submit button.
# Code line 11-12: Input text in username and password input boxes
# Code line 15: Click on the "Submit" button
# Code line 18: Create wait object with a timeout of 5 sec.
# Code line 20 -30: Test that login was successful by checking if the URL in the browser changed. Assert that the URL is now the correct post-login page
# Note: For the above scenarios there will be no output. Since no valid URL is used in the example.

