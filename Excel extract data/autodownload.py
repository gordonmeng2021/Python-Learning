
import selenium
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/meng/Documents/Python/Normal Python/autodownload/chromedriver 2')
driver.get("https://app.socialinsider.io/login?projectname=nike&appview=proj&view=projecthome")

email=driver.find_element_by_name('email')
email.click()
email.send_keys('gordonmeng@ecargo.com')
password= driver.find_element_by_name('password')

password.click()
password.send_keys('m95596862')
login_btn=driver.find_element_by_id('signin-button')
login_btn.click() 

time.sleep(3) # <-- add second

pro= driver.find_element_by_css_selector("a[ng-click='loadProfile(profile)']")
pro.click()


time.sleep(3)

download= driver.find_element_by_css_selector("div[class='dropdown dropdown-default ng-scope']")
download.click()
time.sleep(1)


select_excel= driver.find_element_by_link_text("XLS")
select_excel.click()







