from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Chrome(executable_path=r'./chromedriver.exe')

url = 'http://selenium.dunossauro.live/aula_06_a.html'
b.get(url)

#nome = b.find_element_by_css_selector('[type="text"]')
#senha = b.find_element_by_css_selector('[type="password"]')
#btn = b.find_element_by_css_selector('[type="submit"]')

# OR por [attr=valor]
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# OU por [att*=valor]
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# OR por [attr|=valor]
# nome = b.find_element_by_css_selector('[name|="nome"]')
# senha = b.find_element_by_css_selector('[name|="senha"]')
# btn = b.find_element_by_css_selector('[name|="l0c0"]')

# OR por [attr^=valor]
# nome = b.find_element_by_css_selector('[name^="n"]')
# senha = b.find_element_by_css_selector('[name^="s"]')
# btn = b.find_element_by_css_selector('[name^="l"]')

#nome.send_keys('Lucas')
#senha.send_keys('123')
#btn.click()

# =======================================================================

# Find element pela 'div.classe'
b.find_element_by_css_selector('div.form-group')
