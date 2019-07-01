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
username = driver.find_element_by_id("username").send_keys("nansiroy9@gmail.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("qwertyui")

# The login button is clicked
driver.find_element_by_id("login").click()


driver.implicitly_wait(5)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
driver.execute_script("window.scrollBy(0,1000)")

driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[4]/a/div[2]").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//div[@class='rightframeuserlist']/div[1]/div/a/input").click()

driver.implicitly_wait(5)

driver.find_element_by_id("txteventname").send_keys("test1")
driver.find_element_by_id("ddeventcategory").click()
driver.find_element_by_xpath("//select[@id='ddeventcategory']/option[@value='2:Dance']").click()

driver.implicitly_wait(5)

driver.find_element_by_id("imgUpload").click()

os.system("C:\\Users\\Nansi\\Pictures\\Flyer\\Eventcoverupload.exe")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@id='covercropsave']").click()

driver.implicitly_wait(5)

driver.find_element_by_id("taeventdescription").send_keys("hxgjxhgJHCXbMxnmx nxcmnsm")
driver.implicitly_wait(5)
os.system("C:\\Users\\Nansi\\Pictures\\Flyer\\Flyerupload.exe")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[1]/li[2]/select").click()
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[1]/li[2]/select/option[@value='Asia/Kolkata']").click()

driver.implicitly_wait(5)
#Entering the date
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[2]/div[1]/div/ul[1]/li[2]/input").clear()
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[2]/div[1]/div/ul[1]/li[2]/input").send_keys("Jul 02 2019")

driver.implicitly_wait(5)

#Entering the time in the input.
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[2]/div[1]/div/ul[1]/li[4]/input").clear()
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[2]/div[1]/div/ul[1]/li[4]/input").send_keys("09:02 AM")

driver.implicitly_wait(5)

#ADD  END DATE OF THE EVENT
driver.find_element_by_xpath("//div[@id='eventDatesBlock']/ul[2]/div[1]/div/ul[1]/li[6]/a").click()
driver.find_element_by_class_name('toDate').clear()
driver.find_element_by_class_name('toDate').send_keys("Aug 02 2019")

driver.find_element_by_class_name('toTime').clear()
driver.find_element_by_class_name('toTime').send_keys("09:02 PM")

driver.implicitly_wait(5)

#VENUE DETAILS

driver.find_element_by_id("venuenameAutoControl").send_keys("Paramount Theatre")
#driver.find_element_by_id("venuenameAutoControl").click()

driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight || document.documentElement.scrollHeight/5)", "")
#CONTACT

driver.find_element_by_id("contactname").send_keys("Rose")

driver.find_element_by_id("contactphone").send_keys("4654676667")
driver.find_element_by_id("contactemail").send_keys("Rose@yaahoo.com")

driver.implicitly_wait(5)

#ADDITIONAL DETAILS
driver.find_element_by_id("ddeventtype").click()
driver.find_element_by_xpath("//select[@id='ddeventtype']/option[@value='Free Event']").click()

driver.implicitly_wait(5)

driver.find_element_by_id("txteventwebsite").send_keys("wwww.yoll.com")
driver.find_element_by_id("btneventcancel").click()

driver.implicitly_wait(5)
driver.quit()




