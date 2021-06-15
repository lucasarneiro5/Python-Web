from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')
browser.get('https://www.python.org/')

browser.quit()