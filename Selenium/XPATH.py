# XPATH
''''
Linguagem de consulta para selecionar e navegar por nos de um documento XML

'''

"""
<html>
    <head>
        <title>Titulo</title>
    <head>
    <body>
        <h1>Conteudo</h1>
        <p>Texto</p>
        <h1>Outro Conteudo</h1>
        <p>Outro Texto</p>
    </body>
</html>    
"""

# Quando usa '/html' = Pega inicio do html
# '/html/' = Pega tudo dentro do html
#'/html/body' = Pega a tag 'body'
# /html/body/h1 = Pega todos os com tag 'h1'
# //h1 = Pega qualquer h1, independente da posiçao
# /html//h1 = Pega qualquer h1 dentro do html
# selector.xpath("//ul/*") = Pega todos os 'li'
# selector.xpath("//ul/li[2]") = Pega o 2 'li'. COntagem começa de 1.

# Pelo Selenium
from selenium.webdriver import Firefox

browser = Firefox()

browser.get("https://rennerocha.github.io/xpath/")

browser.find_element_by_xpath("//h2").text # Pega o texto da tag h2

[x.text for x in browser.find_elements_by_xpath("//h2")] # Saida ['Calda', 'Pudim', 'Calda', 'Pudim']

[x.text for x in browser.find_elements_by_xpath("//h1")] # Saida ['Pudim de Leite Condensado', 'Ingredientes', 'Instruções']

browser.find_elements_by_xpath("//h1[@data-section='ingredients']") # Saida = 'Ingredientes'


