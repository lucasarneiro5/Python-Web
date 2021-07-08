from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# 2 - Navegar até pagina
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://covid.saude.gov.br')
time.sleep(5)

# 3 - Colete os dados
csv = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')
driver.execute_script("arguments[0].click();", csv)
time.sleep(1)



