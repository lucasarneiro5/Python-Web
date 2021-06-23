# 1 - Importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# 2 - Navegar até whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# 3 - Definir contatos e grupos e mensagem a ser enviada
contato = ['Lembranças']
menssagem = 'Hello! I´m a robot!!'

# 4 - Buscar contatos/grupos
# Campo de pesquisa: copyable-text selectable-text ou //*[@id="main"]/footer/div[1]/div[2]
# Campo de mensagem: _2A8P4
def buscar_contato(contact):
    search_camp = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    search_camp.click()
    search_camp.send_keys(contact)
    search_camp.send_keys(Keys.ENTER)

def send_message(message):
    message_camp = driver.find_elements_by_xpath('//div[contains(@class, "_2A8P4")]')
    message_camp =[1].click()
    time.sleep(3)
    message_camp.send_keys(message)
    message_camp.send_keys(Keys.ENTER)

for contact in contato:
    buscar_contato(contato)
    send_message(menssagem)

# 4 - Enviar mensagens para contatos/grupos