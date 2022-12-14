from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

QDMS_URL = 'http://qdms-phase-3.s3-website.ap-south-1.amazonaws.com/#/login'



