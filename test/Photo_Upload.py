from selenium import webdriver
import autoit
import os


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


driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.5);")

driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[2]/a").click()

driver.find_element_by_xpath("//select[@id='uploadAlbum']/option[@value='17874']").click()

"""driver.find_element_by_id("txtAlbumName").send_keys("Dreams")
driver.find_element_by_id("txtAlbumDescription").send_keys("sgqjwhgsjqhbsjq")
driver.find_element_by_id("btnCreateNewAlbum").click()"""

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

driver.find_element_by_xpath("//input[@value='Add More Photos']").click()
#driver.find_element_by_xpath("//input[@value='Add More Photos']").send_keys("C:\\Users\\Nansi\\Pictures\\dscn0003_001.jpg")


os.system("C:\\Users\\Nansi\\Documents\\PhotoUp.exe")
driver.find_element_by_id("btnUpload").click()

driver.quit()


#driver.find_element_by_xpath("//div[class=leftMenueImage]")