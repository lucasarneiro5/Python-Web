# 1 - Gerar um dicionario onde a chave é a tag h1
# O valor deve ser um novo dicionario e cada chave do valor deve ser o valor do atributo e 
# cada valor deve ser o texto contido no elemento

from selenium import webdriver
import time
import pprint
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Locating webdriver
browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# Exemplo 1
"""
1- Coletando dados da estrutura DOM
browser.get('http:// link....')

lista_n_ordenada = browser.find_element_by_tag_name('ul') # Buscamos 'ul'

lis = lista_n_ordenada.find_elements_by_tag_name('li') # Buscamos todos os 'li'

lis[0].find_element_by_tag_name('a').text # No primeiro 'li', buscamos 'a' e pegamos o seu texto
"""

# Exemplo 2
"""
def find_by_text(browser, tag, text):
    # Encontrar elemento com texto 'text'

    # Argumentos:
    #- browser = Instancia do browser
    #- texto: Conteudo que deve estar na tag
    #- tag = tag onde o texto sera procurado

    elementos = browser.find_element_by_tag_name(nome da tag) # Retorna uma lista

    for elemento in elementos:
        if elemento.text == texte
            return elemento
# ----
def find_by_href(browser, link):
    # Encontrar o elemento 'a' com o link 'link'

    # Argumentos:
    #- browser = Instancia do browser
    #- link = link que será procurado em todas as tags 'a'

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elmento.get_attribute('href'):
            return elemento


elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')
elemento_ddg = find_by_href(browser, 'ddg')
"""
# Exemplo 3
"""
1. Pegar todos os links de 'aulas' como dicionario - {'nome da aula': 'link da aula'};
2. Navegar até o exercicio 3
"""
browser.get('http://selenium.dunossauro.live/aula_04.html')
time.sleep(3)

# Ver quantas tags 'a' tem nesta pagina?
#len(browser.find_element_by_tag_name('a'))

def get_links(browser, elemento):
    """ Pega todos os links dentro de um elemento
    element = webelement[aside, main, body, ul, ol, etc]
    """
    # Pela tag 'aside', pegar todos os elementos com tags 'a'
    elemente = browser.find_element_by_tag_name(elemento)
    ancoras = elemente.find_elements_by_tag_name('a')

    time.sleep(1)

    # Dicionario
    resultado = {}

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    print(resultado)

get_links(browser, 'aside')

# Exe.2: Acessar a aula 3 com browser 
exercicios = get_links(browser, 'main')




