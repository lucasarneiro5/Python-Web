from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# Getting web page
driver.get('https://www.linkedin.com')
time.sleep(1)

# Sign in for clicking on any "Sign in" text
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
time.sleep(1)
""" or
driver.find_element_by_css_selector('a.nav__button-secondary').click()"""

# Find name_user and write on it
user_input = driver.find_element_by_name('session_key')
"""or
user_input = driver.find_element_by_css_selector('input#username')"""
user_input.send_keys('emaillogin@hotmail.com')


# Find password_user and write on it
password_input = driver.find_element_by_name('session_password')
password_input.send_keys('password')
time.sleep(1)

# Click to log in
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
"""or
driver.find_element_by_css_selector('btn__primary--large from__button--floating').click()
driver.find_element_by_css_selector('button.bnt__primary--large").click()"""


# Getting by_xpath
driver.find_elements_by_xpath('//div[@class="r"]/a') # Pegar a div q tem classe = 'r' e a tag 'a'