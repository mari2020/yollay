from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
# Create a new instance of the Firefox driver
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
chromedriver = 'C:\\WebDriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

#firefoxdriver='C:\\WebDriver\\geckodriver.exe'
#driver = webdriver.Firefox(firefoxdriver)

driver.maximize_window()
driver.set_page_load_timeout(10)

# Navigate to home page
driver.get('https://yollay.com')


driver.refresh()

time.sleep(5)
driver.implicitly_wait(10)

# driver.implicitly_wait(10)

# The Register button is clicked
driver.find_element_by_xpath("(//a[@class='header-button'][1])").click()

# The Emailid of the user is entered
username = driver.find_element_by_id("username").send_keys("marynansi@gmail.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("qwerty123")

# The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

aboutme = driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[1]/a/div[2]").click()

#bIOGRAPHY IS ENTERED

driver.find_element_by_xpath("//img[@title='Edit Bio']").click()
driver.find_element_by_class_name('myupdateinput').clear()
driver.find_element_by_class_name('myupdateinput').send_keys('Iam a ORGANIZER')
driver.find_element_by_id('editedSave').click()
driver.implicitly_wait(5)


#ORGANIZATION
driver.find_element_by_id('organizationEdit').click()
driver.find_element_by_id('organizationsedit').clear()
driver.find_element_by_id('organizationsedit').send_keys("Selvamary")
driver.find_element_by_id('pro2').click()
driver.find_element_by_xpath("//div[@id='editOrganization']/ul[3]/li[2]/input[2]").click()

#Expertise

driver.find_element_by_xpath("//img[@id='workEdit']").click()
driver.find_element_by_id('worksedit').clear()
driver.find_element_by_id('worksedit').send_keys("gsgdhgwbv")
driver.find_element_by_xpath("//div[@id='editWork']/ul[2]/li[2]/input[2]").click()

driver.implicitly_wait(5)

#Certification

driver.find_element_by_id('educationEdit').click()
driver.find_element_by_id('newEducation').clear()
driver.find_element_by_id('newEducation').send_keys("qwdrtetbgvjh")
driver.find_element_by_xpath("//div[@id='editEducation']/ul[2]/li[2]/input[2]").click()

driver.implicitly_wait(10)

#Event Organized

driver.find_element_by_id('addProfileEvents').click()
driver.find_element_by_id('newEventName').send_keys("Todys day out")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
driver.find_element_by_id('enterDate').click()

#driver.find_element_by_xpath("//div[@id='newProfileEvents']/ul[2]/li[2]/input[@readonly='readonly']").click()
#driver.find_element_by_xpath("//input[@text id='enterDate']").click()
driver.find_element_by_class_name('xdsoft_down').click()
driver.find_element_by_xpath("//div[@class='xdsoft_scroller']")
#s3 = Select(driver.find_element_by_class_name('xdsoft_down'))

#driver.execute_script("arguments[0].scrollIntoView(true);","2015")

driver.find_element_by_xpath("//div/div[@class='xdsoft_datepicker active']/div[4]/span/div[2]/div[25]]").click()


#driver.find_element_by_class_name('xdsoft_option').select
#driver.find_element_by_xpath("//div[@name='xdsoft_option']/option[text()='2020']").click()


driver.find_element_by_id('newEventVenueName').send_keys("fxhgafxh")
driver.find_element_by_id('newEventDesc').send_keys("dgfascgAVS")
driver.find_element_by_xpath("//div[@id='newProfileEvents']/ul[5]/li[2]/input[2]").click()


#BASIC INFORMATION

driver.find_element_by_id('basicInfoEdit').click()

#select day of DOB
driver.find_element_by_xpath("//select[@id='day']").click()
DOBday= driver.find_element_by_xpath("//select[@id='day']/option[@value='2']").click()

#selecting  month in DOB
driver.find_element_by_xpath("//select[@id='month']").click()
DOBmonth= driver.find_element_by_xpath("//select[@id='month']/option[@value='2']").click()

#selcting year in DOB
driver.find_element_by_xpath("//select[@id='year']").click()
DOByear= driver.find_element_by_xpath("//select[@id='year']/option[@value='2005']").click()

#Gender select

driver.find_element_by_xpath("//input[@id='gen3']").click()
#hometown

driver.find_element_by_id('hometown').send_keys("Neyveli")

#Save buttob

driver.find_element_by_xpath("//div[@id='editBasicInfo']/ul[4]/li[2]/input[2]").click()


#CONTACT

driver.find_element_by_id('contactEdit').click()

#Email Edit
#driver.find_element_by_id('emailEdit').clear()
#driver.find_element_by_id('emailEdit').send_keys("nansi@gmail.com")

#address edit

driver.find_element_by_id('address1Edit').clear()
driver.find_element_by_id('address1Edit').send_keys("falt5")

#location
driver.find_element_by_id('autocomplete').click()

#Zipcode

driver.find_element_by_id('zipCodeEdit').click()

#phone number
driver.find_element_by_id('phoneEdit').clear()
driver.find_element_by_id('phoneEdit').send_keys("09787878797")

#website
driver.find_element_by_id('websiteEdit').clear()
driver.find_element_by_id('websiteEdit').send_keys("www.yaho.com")

#save the edits

driver.find_element_by_xpath("//html/body/div[5]/div/div[9]/div[4]/div[9]/div[3]/ul[10]/li[2]/input[2]").click()

driver.quit()