from selenium import webdriver
#from selenium.webdriver.common.keys import keys


# Create a new instance of the Firefox driver
#driver = webdriver.chrome("C:\\WebDriver\\chromedriver.exe")
chromedriver = 'C:\\WebDriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# driver = webdriver.firefox()

driver.maximize_window()
driver.set_page_load_timeout(10)

# Navigate to home page
driver.get('https://yollay.com')

driver.implicitly_wait(10)

#The Register button is clicked
driver.find_element_by_xpath("(//a[@class='header-button'][1])").click()

#The Emailid of the user is entered
username = driver.find_element_by_id("username").send_keys("artist1@yaahoo.com")

#The password of the user is entered
password = driver.find_element_by_id("password").send_keys("artist1")

#The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

#Assert the username
assert "Nikhil Grovers" in driver.title


#The browser is closed
driver.quit()


