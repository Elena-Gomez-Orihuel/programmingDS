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
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


def click_not_login(driver):
    try:
        button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'popupCloseIcon.largeBannerCloser'))
        )
        if button is not None:
            button.click()
        else:
            pass
        print('Button clicked')
    except TimeoutException:
        print('Button not found, continuing...')
    except ElementNotInteractableException:
        # Handle the exception
        print('Element is not interactable')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Navigation options
    options = webdriver.FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")

    # Opening investing.com
    from webdriver_manager.firefox import GeckoDriverManager
    """
    assets = [['etfs/ishares-global-corporate-bond-$', 'ishares-global-corporate-bond-$.csv'],
              ['funds/amundi-msci-wrld-ae-c', 'amundi-msci-wrld-ae-c.csv'],
              ['etfs/db-x-trackers-ii-global-sovereign-5', 'db-x-trackers-ii-global-sovereign-5.csv'],
              ['etfs/spdr-gold-trust', 'spdr-gold-trust.csv'],
              ['indices/usdollar', 'usdollar.csv']]
    """

    assets = [
              ['funds/amundi-msci-wrld-ae-c', 'amundi-msci-wrld-ae-c.csv']]
    """
    https://www.investing.com/etfs/etfs/ishares-global-corporate-bond-$
    https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5
    https://www.investing.com/etfs/spdr-gold-trust
    https://www.investing.com/indices/usdollar

    https://www.investing.com/funds/amundi-msci-wrld-ae-c
    """
    with webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options) as driver:
        firstTime = True
        table_data = []
        table = ""
        for asset in assets:
            print("WEB")
            print(asset[0])
            print("CSV")
            print(asset[1])

            driver.get("https://www.investing.com/" + asset[0])

            if (firstTime):
                # Cookies button
                cookies_button = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
                cookies_button.click()
                firstTime = False
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
            # Historical data button
            historical_data_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Historical Data")))
            historical_data_button.click()
            click_not_login(driver)
            if asset[0] == 'funds/amundi-msci-wrld-ae-c':
                #print("holIF")
                # Set the dates
                new_start_date = "01/01/2020"
                new_end_date = "12/31/2020"
                # Date icon button
                date_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, "widget")))
                date_button.click()

                click_not_login(driver)

                start_date_input = driver.find_element(By.ID, 'startDate')
                start_date_input.clear()
                start_date_input.send_keys(new_start_date)

                end_date_input = driver.find_element(By.ID, 'endDate')
                end_date_input.clear()
                end_date_input.send_keys(new_end_date)

                # Apply button
                apply_button = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.ID, "applyBtn")))
                apply_button.click()
                time.sleep(10)

                click_not_login(driver)

                # Create a list of lists containing the data from the table
                table = driver.find_element(By.ID, 'curr_table')
                if table is not None:
                    print("yay we have a table")
                else:
                    print("Table element not found")

                rows = table.find_elements(By.TAG_NAME, 'tr')
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

                # creating the dataframe and creating the csv
                df = pd.DataFrame(table_data)
                df = df.drop(0)
                df = df.drop([2, 3, 4], axis=1)
                # assign column names
                df.columns = ['Date', 'Price', 'Change']
                # types of the columns
                result = df.dtypes
                print(result)
                df.to_csv(asset[1], index=False)
                table_data = []

            else:
                # Set the dates
                new_start_date = "2020-01-02"
                new_end_date = "2021-01-01"
                # Date icon button
                date_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "DatePickerWrapper_input__MDvWH")))
                date_button.click()

                start_date_input = driver.find_element(By.XPATH,
                                                       '//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input')
                start_date_input.clear()
                start_date_input.send_keys(new_start_date)

                end_date_input = driver.find_element(By.CSS_SELECTOR,
                                                     'div.NativeDateInput_root__wbgyP:nth-child(2) > input:nth-child(1)')
                end_date_input.clear()
                end_date_input.send_keys(new_end_date)

                # Apply button
                apply_button = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "inv-button.HistoryDatePicker_apply-button__fPr_G")))
                apply_button.click()
                time.sleep(10)

                click_not_login(driver)

                # Create a list of lists containing the data from the table
                table = driver.find_element("xpath", '//*[@data-test="historical-data-table"]')

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

                # creating the dataframe and creating the csv
                df = pd.DataFrame(table_data)
                df = df.drop(0)
                df = df.drop([2, 3, 4], axis=1)
                # assign column names
                df.columns = ['Date', 'Price', 'Vol', 'Change']
                # types of the columns
                result = df.dtypes
                print(result)
                df.to_csv(asset[1], index=False)
                table_data = []
        time.sleep(100)