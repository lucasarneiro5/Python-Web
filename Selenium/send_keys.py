from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse


# Locating webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

"""
driver.get('http://selenium.dunossauro.live/aula_05_b.html')

topico = firefox.find_element_by_class_name('topico')
linguagens = firefox.find_elements_by_class_name('linguagens')

for linguagem in linguagens:
    print(
        (linguagem.find_element_by_tag_name('h2').text,
        linguagem.find_element_by_tag_name('p').text)
    )
# Saida em tupla = ('Python', 'Criada em 1991')
                    ('C', 'Criada em ...')
      
"""

# Escrevendo na estrutura

"""driver.get('http://selenium.dunossauro.live/aula_05_c.html')

# Localizando a tag que vamos digitar
filme = driver.find_element_by_name('filme')

# Escrever o filme desejado
filme.send_keys('Forrest Gump')

# Localizando e digitando o email no campo
driver.find_element_by_name('email').send_keys('lucasarneiro@yahoo.com.br')

# Localizando e digitando o telefone no campo
driver.find_element_by_name('telefone').send_keys('(011)98765432')

# Enviando os Dados
driver.find_element_by_name('enviar').click()
"""
# Ou por funçao
"""
def melhor_filme(browser, filme, email, telefone):
    driver.find_element_by_name('filme').send_keys('Forrest Gump')
    driver.find_element_by_name('email').send_keys('lucasarneiro@yahoo.com.br')
    driver.find_element_by_name('telefone').send_keys('(011)98765432')
    driver.find_element_by_name('enviar').click()

melhor_filme(driver, 'Forrest Gump', 'lucas@lucas.com', '(019)98765321')

"""
# Preenchendo um formulário
url = 'http://selenium.dunossauro.live/aula_05.html'
driver.get(url)

def preenche_form(browser, nome, email, senha, telefone):
    driver.find_element_by_name('nome').send_keys(nome)
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('senha').send_keys(senha)
    driver.find_element_by_name('telefone').send_keys(telefone)
    driver.find_element_by_name('btn').click()

time.sleep(2)
preenche_form(driver,
        'Lucas',
        'lucasarneiro.v@gmail.com',
        '123456',
        '819123456'
        )

