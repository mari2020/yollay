from selenium import webdriver
import time



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


#aboutme = driver.find_element_by_xpath("//img[@class='leftMenueImage']").click()

driver.implicitly_wait(5)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight/5);")
driver.execute_script("window.scrollBy(0,1000)")

driver.find_element_by_xpath("//div[@class='menuframe']/ul/li[7]/a/div[2]").click()
driver.implicitly_wait(5)
#driver.find_elements_by_xpath("//div[@class='rightframeuserlist']/div/a/input[@id='createpress']").click()
driver.find_element_by_xpath("//div[@class='rightframeuserlist']/div/a/input[@id='createpress']").click()
driver.implicitly_wait(5)
driver.find_element_by_id("txtPressTitle").clear()
driver.find_element_by_id("txtPressTitle").send_keys("test1")


driver.find_element_by_id("txtReleaseDate").clear()
driver.find_element_by_id("txtReleaseDate").send_keys("May 12 2018")


#Choose month date from the datapicker



#datepicker_from = driver.find_element_by_xpath("//div[@class='xdsoft_datetimepicker xdsoft_noselect']").click()

'''time.sleep(2)
month_from = driver.find_element_by_xpath("//div[@class='xdsoft_label xdsoft_month']/div/div[@data-value='3']")
select_from_month = Select(month_from)
select_from_month.select_by_visible_text("Apr")
time.sleep(2)
day_from=driver.find_element_by_xpath("//table/tbody/tr[1]/td[5]/div")
day_from.click()
time.sleep(5)'''



P_source = driver.find_element_by_id("txtSource").send_keys("ghjhadjhasj")
P_Des = driver.find_element_by_id("pressDescription").send_keys("nvjhnbNHsxxxjjh")
P_urladd = driver.find_element_by_id("txtPressURL").send_keys("wwww.yollay.com")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight || document.documentElement.scrollHeight/5)", "")
driver.find_element_by_xpath("//input[@id='btnPressReleaseCancel']").click()


driver.quit()

