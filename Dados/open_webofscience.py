from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Web of Science is a software for collecting databases on publications in many different areas.
# This service is provided by the University of Brasilia but it's website was blocked for my usual chrome driver
# A selenium controlled Chrome driver was able access the website without restrictions.
# This code opens this Chrome Driver

first = 'https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php?'
path = os.getcwd() + '\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(first)