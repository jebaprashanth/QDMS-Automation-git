from defaults import *
from xpaths import *
from qdmsfunctions import *

plant_navigate_xpath = '//*[@id="root"]/div/section/section/header/ul/li[1]'
add_plant_xpath = '//*[@id="addPlant"]'


def navigate_plant_module():
    wait.until(EC.presence_of_element_located((By.XPATH, plant_navigate_xpath))).click()

def add_plant(equipmentName):
    wait.until(EC.presence_of_element_located((By.XPATH, add_plant_xpath))).click() 
    time.sleep(2)
    value = ''
    i = 1

    # while str(value) != str(equipmentName) :
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sub_business_unit"]'))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[' + str(1) + ']/div/span'))).click()
    time.sleep(1)
    value = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div[1]/div/span[2]'))).text
    print(value)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sub_business_unit"]'))).click()
        # i += 1
        




login('admin', 'tokyo@admin')
navigate_master_module()
navigate_plant_module()
add_plant('OTHER')
