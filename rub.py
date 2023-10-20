from selenium import webdriver
from selenium.webdriver.common.by import By

# RUB IP
IP = 'IP HERE'

# Accessing product page from Rub Website
DRIVER = webdriver.Chrome()
DRIVER.get(f'http:{IP}/vue/#/core/op/produto')
