# Import labraries
from selenium import webdriver

# Locating webdriver
browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# Opening URL from Magazine Luiza
browser.get('https://ri.magazineluiza.com.br/')

# Finding XPath from our object and opening it
browser.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/p').click()

# Downloading element
browser.find_element_by_xpath('//*[@id="qh+HU4D7Db023fFZvApelg=="]').click()