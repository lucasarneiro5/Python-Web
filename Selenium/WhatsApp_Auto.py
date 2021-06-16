# Import Library
from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = 'Oi amor, te amo!'
        self.grupos = ["Amor <3"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessenge(self):
        #HTML tag from grupo: //*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span
        #Caixa de texto: //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
        #Botao de Enviar: //*[@id="main"]/footer/div[1]/div[3]
        self.browser.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.browser.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.browser.find_element_by_class_name('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            send_button = self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
            time.sleep(3)
            send_button.click()

bot = WhatsappBot()
bot.SendMessenge()