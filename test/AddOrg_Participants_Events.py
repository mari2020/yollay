from selenium import webdriver
import time
import os



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

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
driver.execute_script("window.scrollBy(0,700)")

driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[4]/a/div[2]").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//li[@class='pastEvents eventMenuItemLink']").click()

driver.find_element_by_xpath("//div[@id='listOfEvents']/div[4]/div[1]/div[1]/li").click()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,700)")

driver.find_element_by_xpath("//div[@id='leftFixedFrameMainContainer']/div[1]/ul/li[3]/a").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='organizername']").send_keys("Rose")
driver.implicitly_wait(6)

driver.find_element_by_xpath("//div[@id='organizerdiv']/ul[2]/li[2]/div[1]/input[2]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@id='divorganize']/div[3]/ul/li/div/a/input").click()

#ADD PARTICIPANTS

driver.find_element_by_xpath("//input[@id='txtparticipantname']").send_keys("ROSE")
driver.find_element_by_xpath("//select[@id='ddparticipantcategory']").click()
driver.find_element_by_xpath("//select[@id='ddparticipantcategory']/option[@value='Comedy']").click()
driver.implicitly_wait(7)

driver.find_element_by_xpath("//input[@id='participantimg']").click()
driver.implicitly_wait(6)

os.system("C:\\Users\\Nansi\\Pictures\\Addparticipant.exe")
driver.implicitly_wait(7)

driver.find_element_by_xpath("//textarea[@id='txtpartdescription']").send_keys("hghghguyug")
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='reset']").click()
driver.implicitly_wait(6)

driver.quit()



