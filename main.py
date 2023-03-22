# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#pip install pandas
#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Define the URL for the assets
    url_stocks = 'https://www.investing.com/equities/amundi-msci-wrld-ae-c-historical-data'
    url_corporate_bonds = 'https://www.investing.com/etfs/ishares-global-corporate-bond-usd-historical-data'
    url_public_bonds = 'https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5-historical-data'
    url_gold = 'https://www.investing.com/etfs/spdr-gold-trust-historical-data'
    url_cash = 'https://www.investing.com/currencies/us-dollar-index-historical-data'

    # Define the date range for the data
    start_date = '01/01/2020'
    end_date = '12/31/2020'

    # Define the payload parameters
    params = {
        'historical_data_start_date': start_date,
        'historical_data_end_date': end_date,
        'interval_sec': 'Daily',
        'action': 'historical_data'
    }

    # Make the request to the website and extract the data
    #STOCK
    response_stock = requests.post(url_stocks, data=params)
    soup_stocks = BeautifulSoup(response_stock.content, 'html.parser')
    table_stocks = soup_stocks.find_all('table')[0]
    df = pd.read_html(str(table_stocks))[0]
    # Save the data to a CSV file
    filename_stocks = 'amundi-msci-wrld-ae-c.csv'
    df.to_csv(filename_stocks, index=False)
    #CORPORATE BONDS
    response_corporate_bonds = requests.post(url_corporate_bonds, data=params)
    soup_corporate_bonds = BeautifulSoup(response_corporate_bonds.content, 'html.parser')
    table_corporate_bonds = soup_corporate_bonds.find_all('table')[0]
    df_corporate_bonds = pd.read_html(str(table_corporate_bonds))[0]
    # Save the data to a CSV file
    filename_corporate_bonds = 'ishares-global-corporate-bond-$.csv'
    df_corporate_bonds.to_csv(filename_corporate_bonds, index=False)
    #PUBLIC BONDS
    response_public_bonds = requests.post(url_public_bonds, data=params)
    soup_public_bonds = BeautifulSoup(response_public_bonds.content, 'html.parser')
    table_public_bonds = soup_public_bonds.find_all('table')[0]
    df_public_bonds = pd.read_html(str(table_public_bonds))[0]
    # Save the data to a CSV file
    filename_public_bonds = 'db-x-trackers-ii-global-sovereign-5.csv'
    df_public_bonds.to_csv(filename_public_bonds, index=False)
    #GOLD
    response_gold = requests.post(url_gold, data=params)
    soup_gold = BeautifulSoup(response_gold.content, 'html.parser')
    table_gold = soup_gold.find_all('table')[0]
    df_gold = pd.read_html(str(table_gold))[0]
    # Save the data to a CSV file
    filename_gold = 'spdr-gold-trust.csv'
    df_gold.to_csv(filename_gold, index=False)
    #CASH
    response_cash = requests.post(url_cash, data=params)
    soup_cash = BeautifulSoup(response_cash.content, 'html.parser')
    table_cash = soup_cash.find_all('table')[0]
    df_cash = pd.read_html(str(table_cash))[0]
    # Save the data to a CSV file
    filename_cash = 'usdollar.csv'
    df_cash.to_csv(filename_cash, index=False)


