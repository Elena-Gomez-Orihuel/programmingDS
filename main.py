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
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
from selenium.common.exceptions import TimeoutException
def click_not_login(driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'x-button'))
        )
        button.click()
        print('Button clicked')
    except TimeoutException:
        print('Button not found, continuing...')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("helloooo1")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    #Navigation options
    options = webdriver.FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")

    #Opening investing.com
    from webdriver_manager.firefox import GeckoDriverManager

    assets = [['etfs/ishares-global-corporate-bond-$','ishares-global-corporate-bond-$.csv'],
              ['funds/amundi-msci-wrld-ae-c','amundi-msci-wrld-ae-c.csv'],
              ['etfs/db-x-trackers-ii-global-sovereign-5','db-x-trackers-ii-global-sovereign-5.csv'],
              ['etfs/spdr-gold-trust','spdr-gold-trust.csv'],
              ['indices/usdollar','usdollar.csv']]
    """
    etfs/etfs/ishares-global-corporate-bond-$
    https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5
    https://www.investing.com/etfs/spdr-gold-trust
    https://www.investing.com/indices/usdollar
    
    https://www.investing.com/funds/amundi-msci-wrld-ae-c
    """
    with webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options) as driver:
        for asset in assets:
            driver.get("https://www.investing.com/" + asset[0])

            #Cookies button
            #// *[ @ id = "onetrust-accept-btn-handler"]
            cookies_button = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
            cookies_button.click()
            """
            #----------------------------------------------------------------------------------------------------------------------
            #login
            time.sleep(2)
            #inv-button user-area_link__Xa7Br
            login_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "inv-button.user-area_link__Xa7Br")))
            login_button.click()
            #login with email
            #inv-button social-auth-button_button__FiobW social-auth-button_icon__PRIVZ social-auth-button_email__o7pnA signin_button__5lDBE
            email_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "inv-button.social-auth-button_button__FiobW.social-auth-button_icon__PRIVZ.social-auth-button_email__o7pnA.signin_button__5lDBE")))
            email_button.click()
            #enter email
            #input_input__FGe3c
            email_input = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "input_input__FGe3c")))
            email_input.send_keys("eleniliagomez@outlook.es")

            #enter pwd
            pwd_input = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "input_input__FGe3c.input_password__B_iju")))
            pwd_input.send_keys("1d8715d6elena")

            #click loginbutton
            #inv-button signin_primaryBtn__Z16kI mb-4
            final_login = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME,
                                            "inv-button.signin_primaryBtn__Z16kI.mb-4")))
            final_login.click()
            #---------------------------------------------------------------------------------------------------------------------------------------------
            """

            #Historical data button
            historical_data_button = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.LINK_TEXT,"Historical Data")))
            historical_data_button.click()
            if asset[0] == 'funds/amundi-msci-wrld-ae-c':
                print("holIF")
            else:
                print("else")
                #Date icon button
                date_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"DatePickerWrapper_input__MDvWH")))
                date_button.click()

                start_date_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')
                start_date_input.clear()  # Clear any existing date value
                new_start_date = "2020-01-02"  # Replace with the desired date string
                start_date_input.send_keys(new_start_date)

                end_date_input = driver.find_element(By.CSS_SELECTOR,
                                                     'div.NativeDateInput_root__wbgyP:nth-child(2) > input:nth-child(1)')
                end_date_input.clear()  # Clear any existing date value
                new_end_date = "2021-01-01"  # Replace with the desired date string
                end_date_input.send_keys(new_end_date)
            """
            
            en vez de clickable, f.presenceofelementlocated
            
            probar get valor que ya hay
            """
            """
            tiene como que accede al input y hae for i, date in input
            el input lo coge con driver = findelementbyxpaht (o css selector, mas segura de lo ultimo a input = date o algo asi, chatgpt me dio algo parecido)
            """
            #Apply button
            #inv-button HistoryDatePicker_apply-button__fPr_G
            apply_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "inv-button.HistoryDatePicker_apply-button__fPr_G")))
            apply_button.click()
            time.sleep(10)

            # Create a list of lists containing the data from the table
            table_data = []
            table =driver.find_element("xpath",'//*[@data-test="historical-data-table"]')
            if table is not None:
                print("yay we have a table")
            else:
                print("Table element not found")

            rows = table.find_elements(By.TAG_NAME, 'tr')
            print("GOT THE TABLE")
            # loop through each row
            for row in rows:
                row_data = []
                # find all the cells in the row
                cells = row.find_elements(By.TAG_NAME, 'td')
                # loop through each cell
                for cell in cells:
                    row_data.append(cell.text)
                # append the row data to the table data
                table_data.append(row_data)

            #creating the dataframe and creating the csv
            df = pd.DataFrame(table_data)
            df = df.drop(0)
            df = df.drop([2, 3, 4], axis=1)
            # assign column names
            df.columns = ['Date', 'Price', 'Vol', 'Change']
            print(df.head(5))
            #types of the columns
            result = df.dtypes
            print(result)
            df.to_csv(asset[1], index=False)
        time.sleep(100)