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
username = driver.find_element_by_id("username").send_keys("mp1@yaahoo.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("mp1")

# The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

# Assert the username
#assert "Mary" in driver.title

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.5);")

aboutme = driver.find_element_by_xpath("//img[@class='leftMenueImage']").click()

driver.implicitly_wait(5)

#BIOGRAPHY

driver.find_element_by_xpath("//img[@title='Edit Bio']").click()
driver.find_element_by_class_name('myupdateinput').clear()
driver.find_element_by_class_name('myupdateinput').send_keys('Iam a stand up Comedian')
driver.find_element_by_id('editedSave').click()
driver.implicitly_wait(5)

#BUSINESS

driver.find_element_by_xpath("//img[@id='businessEdit']").click()
driver.find_element_by_id('businessedit').clear()
driver.find_element_by_id('businessedit').send_keys("Mp1")
driver.find_element_by_id("foundedonedit").click()
driver.find_element_by_xpath("//select[@id='foundedonedit']/option[@value='2016']").click()

#driver.find_element_by_class_name("deleteIndustry").click()

#Add industry

driver.find_element_by_id("ddlindustry").click()
driver.find_element_by_xpath("//select[@id='ddlindustry']/option[@value='Audio Visual']").click()

#save button

driver.find_element_by_xpath("//div[@id='editBusiness']/ul[5]/li[2]/input[2]").click()

#EXPERIENCE

driver.find_element_by_id("workEdit").click()
driver.find_element_by_id("worksedit").send_keys("dhgfghj")
driver.find_element_by_xpath("//div[@id='editWork']/ul[2]/li[2]/input[2]").click()

driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0,0);")

#SERVICES

driver.find_element_by_id("addService").click()

#category
driver.find_element_by_class_name('newCategoryvalue').click()
driver.find_element_by_xpath("//select[@class='newCategoryvalue']/option[@value='Audio Visual']").click()
driver.find_element_by_class_name('newServiceVal').send_keys("gbajghxja")
driver.find_element_by_xpath("//textarea[@text='Enter Description']").send_keys("fghgvhg")
driver.find_element_by_xpath("//div[@id='newServiceAdd']/ul[4]/li[2]/input[2]").click()

#CONTACT

driver.find_element_by_id("contactEdit").click()
driver.find_element_by_id("alternateEmailEdit").send_keys("mp1@yaahoo.com")
driver.find_element_by_id("address1Edit").send_keys("ghagxjhAB")
driver.find_element_by_id("zipCodeEdit").send_keys("607801")
driver.find_element_by_id("phoneEdit").send_keys("098656566")
driver.find_element_by_id("websiteEdit").send_keys("https://yollay.com")
driver.find_element_by_xpath("//div[@id='editContact']/ul[11]/li[2]/input[2]").click()

#ADDITIONALDETAILS

driver.find_element_by_id("addDetailsEdit").click()
driver.find_element_by_id("faccount").send_keys("hgjhagxj")
driver.find_element_by_id("taccount").send_keys("hggjh")
driver.find_element_by_id("gaccount").send_keys("hggjhkjhjh")
driver.find_element_by_id("yaccount").send_keys("hggnnknjhkjhjh")

driver.find_element_by_xpath("//div[@id='editAddDetails']/ul[5]/li[2]/input[2]").click()

driver.quit()

