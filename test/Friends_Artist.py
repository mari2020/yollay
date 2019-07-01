from selenium import webdriver
import time



from selenium.webdriver.support import expected_conditions as EC
# Create a new instance of the Firefox driver
from selenium.webdriver.support.select import Select

# chromedriver = 'C:\\WebDriver\\chromedriver.exe'
driver = webdriver.Chrome('C:\\WebDriver\\chromedriver.exe')

driver.maximize_window()
driver.set_page_load_timeout(20)

# Navigate to home page
driver.get('https://yollay.com')

driver.implicitly_wait(10)

# driver.implicitly_wait(10)

# The Register button is clicked
driver.find_element_by_xpath("(//a[@class='header-button'][1])").click()

# The Emailid of the user is entered
username = driver.find_element_by_id("username").send_keys("artist1@yaahoo.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("artist1")

# The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,700)")

driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[5]/a/div[2]").click()
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,500)")

driver.find_element_by_xpath("//div[@id='noUsers']/div[1]/div[3]/ul/div/a").click()

driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='searchTextBoxControl']").clear()
driver.find_element_by_xpath("//input[@id='searchTextBoxControl']").send_keys("Mary")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='searchButtonInTopSearchBox']").click()
driver.implicitly_wait(6)

driver.find_element_by_xpath("//select[@id='searchUsers']").click()
driver.find_element_by_xpath("//select[@id='searchUsers']/option[@value='Artist']").click()

driver.implicitly_wait(5)

driver.find_element_by_xpath("//select[@id='searchGenereDropDown']").click()
driver.find_element_by_xpath("//select[@id='searchGenereDropDown']/option[@value='Dance']").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='autocomplete']").send_keys("Chennai, Tamil Nadu, India")

driver.find_element_by_xpath("//div[@id='searchRefine']").click()

driver.find_element_by_xpath('//a[contains(@href,"/profile/nansi")]').click()

driver.find_element_by_xpath("//ul[@id='userOperations']/li[4]/a").click()

driver.quit()