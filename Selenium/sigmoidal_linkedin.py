from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import time
import csv

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# Maximizar tela
driver.maximize_window()

# Arquivo csv
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

# Acessar site linkedin
driver.get('https://www.linkedin.com/')

# Clicar em "Sing In"
time.sleep(2)
driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()

# Digitar usuario
user_input = driver.find_element_by_name('session_key')
user_input.send_keys('lavieira@kpmg.com.br')
#user_input.send_keys('emailfake@gmail.com')

# Digitar senha
password_input = driver.find_element_by_name('session_password')
password_input.send_keys('Pentiumd5!')
#password_input.send_keys('SuaSenha')

# Apertar o "Enter"
password_input.send_keys(Keys.RETURN)
time.sleep(2)

# Digitando as pesquisas de vagas
driver.get('https://www.google.com.br/')
search_input = driver.find_element_by_name('q')
search_input.send_keys('site:linkedin.com/in/ AND "data engineer" and "Rio de Janeiro"')
search_input.send_keys(Keys.RETURN)
time.sleep(2)

# Pegando lista de perfis
lista_perfil = driver.find_elements_by_xpath('//div[@class="yuRUbf"]/a')
links = [perfil.get_attribute('href') for perfil in lista_perfil]

# Extraindo informações individuais
for perfil in links:
    #print(perfil)
    driver.get(perfil)
    time.sleep(4)

    response = Selector(text=driver.page_source)
    print(response)
    """nome = response.xpath("//title/text()").extract_first().split(" | ")[0]
    headline = response.xpath('//h2/text()')[1].extract().strip()
    url_perfil = driver.current_url

    # Escrever no csv
    writer.writerow([nome, headline, url_perfil])"""

# Sair do driver
driver.quit()