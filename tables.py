from defaults import *
from xpaths import *
from qdmsfunctions import *


from bs4 import BeautifulSoup

import pandas as pd
import lxml


login('admin', 'tokyo@admin')
navigate_master_module()

## Table Function

table_start_row_number = 2
table_start_column_number = 1
columns = ['Code', 'Plant', 'Sub Business Unit', 'Plant Manager', 'Address', 'Contact No', 'Fax No', 'Description', 'Action']
time.sleep(2)

print(driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[' + str(table_start_row_number) +']/td[' + str(table_start_column_number) +']').text)

