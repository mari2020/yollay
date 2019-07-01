from selenium import webdriver

# Create a new instance of the Firefox driver

chromedriver = 'C:\\WebDriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.maximize_window()
driver.set_page_load_timeout(10)

# Navigate to home page
driver.get('https://yollay.com')

driver.implicitly_wait(10)

#click the Register button
driver.find_element_by_xpath("(//a[@class='header-button'][2])").click()
#driver.implicitly_wait(5)

##click ARTIST button in the register page
Artist = driver.find_element_by_xpath("//input[@value='Artist']").click()

#Enter the FirstName of the user
firstname = driver.find_element_by_xpath("//input[@id='firstname']"). send_keys("Artist")
driver.implicitly_wait(2)

#Email id of the user is entered
emailid = driver.find_element_by_xpath("//input[@id='email']").send_keys("abcd@gmail.com")
driver.implicitly_wait(2)

#enter the password for the account
pwd = driver.find_element_by_xpath("//input[@id='password']").send_keys("summer2019")
driver.implicitly_wait(2)

#The Location of the user is entered
location = driver.find_element_by_xpath("//input[@id='location']").send_keys("Chennai")
driver.implicitly_wait(2)

#slect the Genre
genre = driver.find_element_by_xpath("(//td[@class='color4 ']/div[2])").click()
driver.implicitly_wait(3)


#click the  Terms and condition checkbox
terms = driver.find_element_by_xpath("//input[@class='chkAccept']").click()

#After registering the sign up button is clicked
#sign_up = driver.find_element_by_id("signup").click()

driver.implicitly_wait(2)

#The browser is closed
driver.quit()
