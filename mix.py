from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# RUB IP
IP = 'IP HERE'

# RUB User Credential
USER = 'USER HERE'

# RUB Password Credential
PASSWORD = 'PASSWORD HERE'

# Function to wait load process (Basicly wait 1.5s when it's called)
def WAIT_LOAD():
    time.sleep(1.5)

supplier_code = input('Digite o código do fornecedor: ')

# Accessing product page from Rub Website
DRIVER = webdriver.Chrome()
DRIVER.get(f'http:{IP}/vue/#/core/op/produto')


# Function that login into the Website
def LoginRub():
    USER_BOX = DRIVER.find_element(By.ID , 'login-fld-usr')
    USER_BOX.send_keys(USER)

    PASSWORD_BOX = DRIVER.find_element(By.ID, 'login-fld-pwd')
    PASSWORD_BOX.send_keys(PASSWORD)

    LOGIN_BUTTON = DRIVER.find_element(By.ID, 'login-vbtn-loginbtn')
    LOGIN_BUTTON.click()


def ApplyFilter():
    # Click on filter button
    FILTER_BUTTON = DRIVER.find_element(By.XPATH, '//div[@class="pull-left botoes-table listOptions"]')
    FILTER_BUTTON.click()


    # Click on stock filter
    SELECT_STOCK_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="ESTOQUE_DISPONIVEL"]')
    SELECT_STOCK_FILTER.click()


    # Select bigger then filter from stock
    BIGGER_THEN_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="3"]')
    BIGGER_THEN_FILTER.click()


    # Send bigger then 0
    VALUE_FROM_STOCK = DRIVER.find_element(By.XPATH, '//input[@placeholder="Valor"]')
    VALUE_FROM_STOCK.send_keys('0')


    # Click on supplier filter
    SELECT_SUPPLIER_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="T3_NOME"]')
    SELECT_SUPPLIER_FILTER.click()


    # Send supplier code to supplier filter
    VALUE_FROM_SUPPLIER = DRIVER.find_element(By.XPATH, '(//input[@placeholder="Valor"])[2]')
    VALUE_FROM_SUPPLIER.send_keys(supplier_code)

    # Click on apply filter button
    APPLY_FILTER_BUTTON = DRIVER.find_element(By.XPATH, '//a[@class="fwrub btn btn-primary btnApply"]')
    APPLY_FILTER_BUTTON.click()


LoginRub()
WAIT_LOAD()

ApplyFilter()
WAIT_LOAD()

