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
username = driver.find_element_by_id("username").send_keys("nansiroy9@gmail.com")

# The password of the user is entered
password = driver.find_element_by_id("password").send_keys("qwertyui")

# The login button is clicked
driver.find_element_by_id("login").click()

driver.implicitly_wait(5)

# Assert the username
#assert "Mary" in driver.title

aboutme = driver.find_element_by_class_name('leftMenueImage').click()

driver.implicitly_wait(5)

# Assert the username
# assert "Edit Bio" in driver.title


#assert isinstance(driver.find_element_by_id("bioEdit").send_keys, "Iam a stand up Comedian")
driver.find_element_by_xpath("//img[@title='Edit Bio']").click()
driver.find_element_by_class_name('myupdateinput').clear()
driver.find_element_by_class_name('myupdateinput').send_keys('Iam a stand up Comedian')
driver.find_element_by_id('editedSave').click()
driver.implicitly_wait(5)

#Achievements Details

Awards = driver.find_element_by_id("addAchieve").click()
yearaward = driver.find_element_by_xpath("//select[@class='newYearvalue']/option[@value='2000']").click()
#yearaward.select_by_value('2001')

driver.implicitly_wait(5)
#driver.find_element_by_class_name('newAchieveVal').clear()
driver.find_element_by_class_name('newAchieveVal').send_keys("best vvsxvh")

#driver.find_element_by_xpath("//textarea[@text='Enter the name']").clear()
driver.find_element_by_xpath("//textarea[@text='Enter the name']").send_keys("gxhsagxjh")

driver.find_element_by_xpath("//div[@id='newAchievementAdd']/ul[4]/li[2]/input[@value='Save']").click()
#driver.find_element_by_xpath("//html/body/div[5]/div/div[9]/div[3]/div[3]/div[2]/ul[4]/li[2]/input[2]").click()

driver.implicitly_wait(5)

#enter about the influencer

driver.find_element_by_xpath("//div[@class='addNewIconBLock']/img[@id='newInflImg']").click()
driver.find_element_by_class_name('newInfluence').clear()
driver.find_element_by_class_name('newInfluence').send_keys("Rose")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@id='newInfluencedbyDiv']/ul[2]/li[2]/input[@value='Save']").click()


driver.implicitly_wait(5)

#Adding Members in a group
driver.execute_script("scroll(0, 0);")
driver.find_element_by_id('addNewMember').click()
#driver.find_element_by_xpath("//div[@class='repeatframeheadform']/ul[1]/div[2]/img[@title='Add New Member']").click()
#entering the name of the team
driver.find_element_by_id('txtparticipantname').send_keys("team")
#giving description for the added group
driver.find_element_by_id('txtpartdescription').send_keys("jaghjkhskjh")
#save button is clicked
driver.find_element_by_id('saveMember').click()

driver.implicitly_wait(5)

#Work details

driver.find_element_by_id('workEdit').click()

#enter the details of the work
driver.find_element_by_id('worksedit').clear()
driver.find_element_by_id('worksedit').send_keys("cszvanhz")
driver.find_element_by_xpath("//html/body/div[5]/div/div[9]/div[4]/div[2]/div[3]/ul[2]/li[2]/input[2]").click()

driver.implicitly_wait(5)

#enter the educational details


driver.find_element_by_id('educationEdit').click()
driver.find_element_by_id('newEducation').clear()
driver.find_element_by_id('newEducation').send_keys("cszvanhz")
driver.find_element_by_xpath("//html/body/div[5]/div/div[9]/div[4]/div[3]/div[3]/ul[2]/li[2]/input[2]").click()

# AFFILIATION

'''driver.find_element_by_id('addNewAffil').click()
#driver.find_element_by_id('newEducation').clear()
driver.find_element_by_xpath("//div[@id='newAffiliationsDiv']/ul[1]/li[2]/input[@class='newAffil']").send_keys("sAAVAN")
driver.find_element_by_xpath("//div[@id='newAffiliationsDiv']/ul[2]/li[2]/input[@value='Save']").click()'''

#Edit Artist Name

driver.find_element_by_id('nameEdit').click()
driver.find_element_by_id('fname').clear()
driver.find_element_by_id('fname').send_keys("mary")
driver.find_element_by_xpath("//div[@id='editName']/ul[4]/li[2]/input[@value='Save']").click()

#Edit Genre

driver.find_element_by_id('genereEdit').click()

driver.find_element_by_xpath("//div[@id='editGenere']/ul[1]/li[2]/select[@id='gname']").click()
genreselect= driver.find_element_by_xpath("//select[@id='gname']/option[@value='Dance']").click()

#Save the modified Genre
driver.find_element_by_xpath("//div[@id='editGenere']/ul[2]/li[2]/input[@value='Save']").click()

#CATEGORY

driver.find_element_by_xpath("//div[@class='repeatframeheadform']/ul[1]/li[2]/img[@id='categoryEdit']").click()
driver.find_element_by_xpath("//div[@id='editCategory']/ul[1]/li[2]/input[2]").clear()
driver.find_element_by_xpath("//div[@id='editCategory']/ul[1]/li[2]/input[2]").send_keys("gabra")
#driver.find_element_by_xpath("//div[@id='editCategory']/ul[1]/li[2]/input[1]/span/input[@class='ui-helper-hidden-accessible']").send_keys("Dandiya")
driver.find_element_by_xpath("//div[@id='editCategory']/ul[3]/li[2]/input[@value='Save']").click()

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
