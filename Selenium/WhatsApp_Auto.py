# Import Library
from selenium import webdriver
import time



class WhatsappBot:
    def __init__(self):
        self.mensagem = 'This is robot. I´m learning Selenium!' # Menssagem
        self.grupos = ["Amor <3"] # Contatos
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessenge(self):
        #HTML tag from grupo: //*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span
        #Caixa de texto: <div tabindex="-1" class="_2A8P4">
        #Botao de Enviar: <span data-testid="send" data-icon="send" class="">
        self.browser.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.browser.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.browser.find_element_by_class_name('_2A8P4')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            send_button = self.browser.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            send_button.click()

bot = WhatsappBot()
bot.SendMessenge()