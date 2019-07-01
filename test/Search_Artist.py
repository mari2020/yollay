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

driver.find_element_by_xpath("nav[@id='primary-menu']/ul/a[1]").click()
driver.implicitly_wait(5)

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

driver.quit()