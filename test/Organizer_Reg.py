from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
from selenium.webdriver.support.select import Select

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

#click ORGANIZER button in the register page
Organizer = driver.find_element_by_xpath("//input[@value='Organizer']").click()

#Enter the FirstName of the user
firstname = driver.find_element_by_xpath("//input[@id='firstname']"). send_keys("organizer")
driver.implicitly_wait(2)

#Email id of the user is entered
emailid = driver.find_element_by_xpath("//input[@id='email']").send_keys("abcd@gmail.com")
driver.implicitly_wait(2)

#enter the password for the account
pwd = driver.find_element_by_xpath("//input[@id='password']").send_keys("summer2018")
driver.implicitly_wait(2)

#The Location of the user is entered
location = driver.find_element_by_xpath("//input[@id='location']").send_keys("Neyveli")

#select_Location = Select(driver.find_element_by_id('location').send_keys("India"))
#select_Location.select_by_value(1)



driver.implicitly_wait(3)

#click the  Terms and condition checkbox
Terms = driver.find_element_by_xpath("//input[@class='chkAccept']").click()

#After registering the sign up button is clicked
#sign_up = driver.find_element_by_id("signup").click()

driver.implicitly_wait(2)

#The browser is closed
driver.quit()
