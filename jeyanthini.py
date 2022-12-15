from defaults import *
from xpaths import *
from qdmsfunctions import *

plant_navigate_xpath = '//*[@id="root"]/div/section/section/header/ul/li[1]'
add_plant_xpath = '//*[@id="addPlant"]'


def navigate_plant_module():
    wait.until(EC.presence_of_element_located((By.XPATH, plant_navigate_xpath))).click()

# Selecting a drop down based on string value

def add_plant(equipmentName=None):
    wait.until(EC.presence_of_element_located((By.XPATH, add_plant_xpath))).click() 
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sub_business_unit"]'))).click()
    time.sleep(1)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and contains(.//span, '" + equipmentName + "')]"))).click()


login('admin', 'tokyo@admin')
navigate_master_module()
navigate_plant_module()
add_plant('RMC')
