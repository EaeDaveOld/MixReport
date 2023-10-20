from selenium import webdriver
from selenium.webdriver.common.by import By

# RUB IP
IP = 'IP HERE'

# Accessing product page from Rub Website
DRIVER = webdriver.Chrome()
DRIVER.get(f'http:{IP}/vue/#/core/op/produto')


# Function that login into the Web Server
def LoginRub():
    USER = 'USER HERE'
    PASSWORD = 'PASSWORD HERE'

    USER_BOX = DRIVER.find_element(By.ID , 'login-fld-usr')
    USER_BOX.send_keys(USER)

    PASSWORD_BOX = DRIVER.find_element(By.ID, 'login-fld-pwd')
    PASSWORD_BOX.send_keys(PASSWORD)

    LOGIN_BUTTON = DRIVER.find_element(By.ID, 'login-vbtn-loginbtn')
    LOGIN_BUTTON.click()
