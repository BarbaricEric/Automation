# Selenium, Google Chrome Web Driver, and Python installation required
# Facebook login automation
# Selenium documentation notes this method is bad practice 

#using webdriver from selenium module
from selenium import webdriver

#If not using a system path, link your chromedriver.exe (For non-Windows users, it's just called chromedriver):
#variable = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
#(Set executable_path to the location where your chromedriver is located.)

#If you've placed chromedriver on your System Path, you can shortcut by just doing the following:
#variable = webdriver.Chrome()

#If still confused, refer to https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver

fb = webdriver.Chrome() 
fb.get('https://facebook.com')
username = fb.find_element_by_xpath('//*[@id="email"]')
username.send_keys('USER ID FOR FACEBOOK ENTER HERE')
password = fb.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('PASSWORD FOR FACEBOOK ENTER HERE')
login = fb.find_element_by_xpath('//*[@id="u_0_b"]')
login.click()

#https://www.selenium.dev/documentation/en/
#https://selenium-python.readthedocs.io/getting-started.html#simple-usage
#https://www.selenium.dev/selenium/docs/api/javascript/index.html
