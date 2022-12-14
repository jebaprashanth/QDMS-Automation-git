from defaults import *
from xpaths import *


def login(mail_id, password):
    driver.get(QDMS_URL)

    wait.until(EC.presence_of_element_located((By.XPATH, login_username_xpath))).clear()
    mail_input = driver.find_element(By.XPATH, login_username_xpath)
    mail_input.send_keys(mail_id)

    wait.until(EC.presence_of_element_located((By.XPATH, login_password_xpath))).clear()
    password_input = driver.find_element(By.XPATH, login_password_xpath)
    password_input.send_keys(password)

    wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()
    
    time.sleep(2)
    # close_the_notifications()


def navigate_master_module():
    wait.until(EC.presence_of_element_located((By.XPATH, navigate_master_module_xpath))).click()

def navigate_equipment():
    wait.until(EC.presence_of_element_located((By.XPATH, navigate_top_equipment_xpath))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, navigate_left_equipment_xpath))).click()

def add_equipment(equipmentName, equipmentType, description=None):
    wait.until(EC.presence_of_element_located((By.XPATH, add_equipment_button_xpath))).click() 
    
    wait.until(EC.presence_of_element_located((By.XPATH, add_equipemnt_equipmentName_xpath))).clear()
    equipment_name = driver.find_element(By.XPATH, add_equipemnt_equipmentName_xpath)
    equipment_name.send_keys(equipmentName)

    wait.until(EC.presence_of_element_located((By.XPATH, add_equipment_equipmentType_xpath))).click()
    driver.find_element(By.XPATH, '//*[@title="' + equipmentType + '"]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, add_equipment_description_xpath))).clear()
    equipment_description = driver.find_element(By.XPATH, add_equipment_description_xpath)
    equipment_description.send_keys(description)

    wait.until(EC.presence_of_element_located((By.XPATH, add_equipment_saveButton_xpath))).click()

    # close_the_notifications()

def close_the_notifications():
    wait.until(EC.presence_of_element_located((By.XPATH, notifications_close_button))).click()
    




