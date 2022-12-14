from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

import pandas as pd
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path="local_web_driver/chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
wait = WebDriverWait(driver, 30)

TH_URL = 'http://th-hub-dev-test.s3-website.ap-south-1.amazonaws.com/'

def login(mail_id, password):
    driver.get(TH_URL)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))).clear()
    mail_input = driver.find_element(By.XPATH, "//*[@id='email']")
    mail_input.send_keys(mail_id)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).clear()
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mui-1"]'))).click()
    time.sleep(2)


def go_to_permissions_as_thadmin(company_name):
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[1]/ul[3]/ul/div/a'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="companyId"]'))).send_keys(company_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"companyId-listbox\"]"))).click()

def set_bulk_permissions(permissions):
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mui-component-select-select_all"]'))).click()
    time.sleep(1)

    if permissions == 'MAINTAIN':
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-select_all"]/div[3]/ul/li[4]'))).click()
    elif permissions == 'NONE':
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-select_all"]/div[3]/ul/li[1]'))).click()
    elif permissions == 'READ':
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-select_all"]/div[3]/ul/li[2]'))).click()
    elif permissions == 'WRITE':
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-select_all"]/div[3]/ul/li[3]'))).click()



login('admin@gmail.com', 'admin')

go_to_permissions_as_thadmin('KIDY')

set_bulk_permissions('MAINTAIN')

# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/label[3]/span[1]/input'))).clear()
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/label[3]/span[1]/input').is_selected())