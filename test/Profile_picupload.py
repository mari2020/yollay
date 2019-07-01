from selenium import webdriver
import autoit
import os
import time
from PIL import Image
from resizeimage import resizeimage
from selenium.webdriver import ActionChains

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

time.sleep(10)

aboutme = driver.find_element_by_xpath("//img[@class='leftMenueImage']").click()

driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.5);")

driver.find_element_by_id("userPiceditBtn").click()
os.system("C:\\Users\\Nansi\\Documents\\ProfileUpld.exe")
img = driver.find_elements_by_class_name('imgareaselect-border4')

action = ActionChains(driver)
action.move_to_element_with_offset('img',500,500).context_click('img')
'''Rs_img = Image.open("img")
#resizeimage.resize_contain('Rs_img', 200, 100)
img = Image.new('RGB', [200,200], 0x000000)'''
driver.find_element_by_id("cropsave").click()
time.sleep(10)
driver.quit()