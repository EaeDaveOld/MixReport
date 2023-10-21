from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# RUB IP
IP = 'IP HERE'

# RUB User Credential
USER = 'USER HERE'

# RUB Password Credential
PASSWORD = 'PASSWORD HERE'

# Don't change this supplier code
supplier_code = None


# Function to request supplier_code
def Request_SupplierCode():
    global supplier_code
    Stop_Loop = False
    while Stop_Loop is False:
        try:
            supplier_code = int(input('Digite o código do fornecedor: '))
            Stop_Loop = True
        except ValueError:
            print('Digite somente números inteiros e sem espaços em branco.')


Request_SupplierCode()

# Accessing product page from Rub Website
DRIVER = webdriver.Chrome()
DRIVER.get(f'http:{IP}/vue/#/core/op/produto')

# Function to wait load process (Basicly wait 0.5s when it's called)
def Wait_Load():
    time.sleep(1)


# Function that login into the Website
def LoginRub():
    USER_BOX = DRIVER.find_element(By.ID , 'login-fld-usr')
    USER_BOX.send_keys(USER)

    PASSWORD_BOX = DRIVER.find_element(By.ID, 'login-fld-pwd')
    PASSWORD_BOX.send_keys(PASSWORD)

    LOGIN_BUTTON = DRIVER.find_element(By.ID, 'login-vbtn-loginbtn')
    LOGIN_BUTTON.click()


# Function that apply filter bigger then zero and supplier code
def ApplyFilter():
    # Click on filter button
    FILTER_BUTTON = DRIVER.find_element(By.XPATH, '//*[@id="master-vbtn-optionsdialogopenbutton"]')
    FILTER_BUTTON.click()


    # Click on stock filter
    SELECT_STOCK_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="ESTOQUE_DISPONIVEL"]')
    SELECT_STOCK_FILTER.click()


    # Select bigger then filter from stock
    BIGGER_THEN_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="3"]')
    BIGGER_THEN_FILTER.click()


    # Send bigger then 0
    VALUE_FROM_STOCK = DRIVER.find_element(By.XPATH, '//input[@placeholder="Valor"]')
    VALUE_FROM_STOCK.clear()
    VALUE_FROM_STOCK.send_keys('0')


    # Click on supplier filter
    SELECT_SUPPLIER_FILTER = DRIVER.find_element(By.XPATH, '//option[@value="T3_NOME"]')
    SELECT_SUPPLIER_FILTER.click()


    # Send supplier code to supplier filter
    VALUE_FROM_SUPPLIER = DRIVER.find_element(By.XPATH, '(//input[@placeholder="Valor"])[2]')
    VALUE_FROM_SUPPLIER.clear()
    VALUE_FROM_SUPPLIER.send_keys(supplier_code)

    # Click on apply filter button
    APPLY_FILTER_BUTTON = DRIVER.find_element(By.XPATH, '//a[@class="fwrub btn btn-primary btnApply"]')
    APPLY_FILTER_BUTTON.click()


# Function that generate report PDF
def GeneratePDF():
    GENERATE_PDF_BUTTON = DRIVER.find_element(By.XPATH, '//*[@id="mainview"]/div[1]/div/div[1]/div/div[3]/div[3]/ul[2]/li[3]/a')
    GENERATE_PDF_BUTTON.click()


# Function to close PDF report Window
def Close_PDF_Window():
    PDF_Window = DRIVER.window_handles[1]
    DRIVER.switch_to.window(PDF_Window)
    DRIVER.close()


# Function to select de first window
def Select_First_Window():
    Actual_Window = DRIVER.window_handles[0]
    DRIVER.switch_to.window(Actual_Window)


LoginRub()
Wait_Load()

ApplyFilter()
Wait_Load()

GeneratePDF()
Wait_Load()

input()



