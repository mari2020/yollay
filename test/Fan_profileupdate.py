from selenium import webdriver

chromedriver = 'C:\\WebDriver\\chromedriver.exe'
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
username = driver.find_element_by_id("username").send_keys("smitha@yaahoo.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("smitha123")

# The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

# Assert the username
#assert "Mary" in driver.title

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.5);")

aboutme = driver.find_element_by_xpath("//img[@class='leftMenueImage']").click()

driver.implicitly_wait(5)

#NAME

driver.find_element_by_id("nameEdit").click()

driver.find_element_by_id('fname').clear()
driver.find_element_by_id('fname').send_keys("Smitha")

driver.find_element_by_id('lname').clear()
driver.find_element_by_id('lname').send_keys("123")

driver.find_element_by_xpath("//div[@id='editName']/ul[4]/li[2]/input[2]").click()

#INTRESET

driver.find_element_by_id('genereEdit').click()
driver.find_element_by_xpath("//div[@id='editInterest']/ul[1]/li[2]/div[3]/input").click()
driver.find_element_by_xpath("//div[@id='editInterest']/ul[2]/li[2]/input[2]").click()

#BASIC INFORMATION

driver.find_element_by_id('basicInfoEdit').click()

#select day of DOB
driver.find_element_by_xpath("//select[@id='day']").click()

DOBday= driver.find_element_by_xpath("//select[@id='day']/option[@value='3']").click()

#selecting  month in DOB
driver.find_element_by_xpath("//select[@id='month']").click()
DOBmonth= driver.find_element_by_xpath("//select[@id='month']/option[@value='3']").click()

#selcting year in DOB
driver.find_element_by_xpath("//select[@id='year']").click()
DOByear= driver.find_element_by_xpath("//select[@id='year']/option[@value='2000']").click()

#Gender select

driver.find_element_by_xpath("//input[@id='gen3']").click()
#hometown

driver.find_element_by_id('hometown').clear()
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


#save the edits

driver.find_element_by_xpath("//div[@id='editContact']/ul[10]/li[2]/input[2]").click()

driver.implicitly_wait(10)

driver.quit()
