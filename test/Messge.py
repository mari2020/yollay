from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
# Create a new instance of the Firefox driver
from selenium.webdriver.support.select import Select

# chromedriver = 'C:\\WebDriver\\chromedriver.exe'
driver = webdriver.Chrome('C:\\WebDriver\\chromedriver.exe')

driver.maximize_window()
driver.set_page_load_timeout(10)

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

driver.find_element_by_xpath("//li[@id='messagenotification']/a/div/i").click()

driver.implicitly_wait(6)

driver.find_element_by_xpath("//div[@id='displayMessagesNotificationsDiv']/div[3]/a").click()

driver.implicitly_wait(5)

driver.find_element_by_xpath("//li[@id='fanchat']").click()


driver.execute_script("window.scrollBy(0,700)")

driver.find_element_by_xpath("//textarea[@id='messageText']").send_keys("HI")

driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='messageSend']").click()

driver.implicitly_wait(6)

driver.quit()