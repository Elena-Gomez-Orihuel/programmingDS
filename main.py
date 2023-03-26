import csv
import time
import pandas as pd
import re
from calendar import monthrange
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import warnings



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    #Navigation options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")

    #Opening investing.com
    #Navigator initialization
    #driver.get('https://www.investing.com/etfs/ishares-global-corporate-bond-$')
    with webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options) as driver:
        #for asset in assets:
        driver.get("https://www.investing.com/etfs/ishares-global-corporate-bond-$")

        #Cookies button
        #// *[ @ id = "onetrust-accept-btn-handler"]
        cookies_button = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
        cookies_button.click()
        #Historical data button
        historical_data_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Historical Data")))
        historical_data_button.click()
        #Date icon button
        date_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"DatePickerWrapper_input__MDvWH")))
        date_button.click()
        #send keys
        #NativeDateInput_root__wbgyP
        #NativeDateInput_root__wbgyP


        time.sleep(1000)

    #webdriver_options = Options()


    ##### FIRST PART #####

    #assets = ['funds/amundi-msci-wrld-ae-c', 'etfs/ishares-global-corporate-bond-$',
    #          'etfs/db-x-trackers-ii-global-sovereign-5', 'etfs/spdr-gold-trust', 'indices/usdollar']

