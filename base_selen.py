## Example 1 ##

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://seleniumhq.org/')

import time
from selenium import webdriver

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome() 
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()


# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Firefox()
driver.get('http://www.facebook.com')
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()



from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Chrome()
browser.get('http://www.facebook.com')
  
username = browser.find_element_by_id( "guru99" )
password = browser.find_element_by_id( "password@123" )
submit   = browser.find_element_by_id( "submit"   )
  
username.send_keys( "me" )
password.send_keys( "mykewlpass" )
  

submit.click()
  

wait = WebDriverWait( browser, 5 )
  
try:
    page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
    self.fail( "Loading timeout expired" )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)
time.sleep(5) # Let the user actually see something!
driver.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()


# On executing this statement, a new Firefox window will launch. We had made following settings for the driver instance:

# driver.implicitly_wait(30)
# driver.maximize_window()

# We configured a timeout for Selenium to launch the browser in 30 seconds. Next statement maximizes the browser window.
# Step-3.

# Next, we will navigate to the application, in our case ‘http://www.google.com’, passing the given URL to the driver.get() method. After making a call to the get() method, Webdriver waits until the page gets rendered in the browser window and sends the control back to the script.

# After the page gets loaded, Selenium will interact with various elements on the page. Next, in the test script, we will be looking at different Selenium WebDriver functions that search an HTML object, send a text to the web component, simulate key press event, click buttons and select from drop downs, etc. Let’s see all these functions getting used in the next step.
# Step-4.

# * First of all, we’ll locate the Google Search textbox to supply the text input for the Search. The Search text box has id attribute as <lst-ib> and you can identify it from the code given below:

# search_field = driver.find_element_by_id(<lst-ib>)

# * After locating the Search text box, we are trying to interact with the textbox element by clearing the previous value using the clear() method and then using the send_keys() method to provide a new value. Subsequently calling the submit() method will forward the search request for processing. You can see a quick preview of these steps in the next few lines.

# search_field.clear()
# search_field.send_keys(“Selenium WebDriver Interview questions”)
# search_field.submit()

# * After submitting the search request, Firefox driver will display the result page returned by Google. The result page shows a list of entries that match the searched text. Each of the entry in the list is captured in anchor <a> element and can be accessed using “find_elements_by_class_name” method. Using this it will return a list of elements as:

# lists= driver.find_elements_by_class_name(“_Rm”)

# * The list of items expands to many pages, so we are restricting our code to print first ten entries captured in the anchor tag. We are outputting the names of the entries using the .text property of the anchor <a> elements:

# for listitem in lists:
#    print (listitem)
#    i=i+1
#    if(i>10):
#       break

# This example gave us a real insight on using Selenium WebDriver and Python together to create a simple test automation script. It is a very basic example script. We will use other interesting and complicated features of Selenium Library with Python in our upcoming posts.

# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print (“Found “ + str(len(lists)) + “searches:”)

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>10):
      break

time.sleep(5) # Let the user actually see something!

# close the browser window
driver.quit()
driver.close() ## Not sure which of these is more correct



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")

browser = webdriver.Firefox()
browser.get('https://login.live.com')

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("myEmailAddress")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("myPassword")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()