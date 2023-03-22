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


    # Define the URL for the asset (e.g., stocks)
    url = 'https://www.investing.com/equities/amundi-msci-wrld-ae-c-historical-data'

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
    response = requests.post(url, data=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]

    # Save the data to a CSV file
    filename = 'amundi-msci-wrld-ae-c.csv'
    df.to_csv(filename, index=False)
    """
    You can repeat the above code for each of the assets (e.g., stocks, corporate bonds, public bonds, gold, cash) by 
    changing the URL and filename accordingly. The URLs for the other assets are as follows:

    db-x-trackers-ii-global-sovereign-5: https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5-historical-data
    ishares-global-corporate-bond-$: https://www.investing.com/etfs/ishares-global-corporate-bond-usd-historical-data
    spdr-gold-trust: https://www.investing.com/etfs/spdr-gold-trust-historical-data
    usdollar: https://www.investing.com/currencies/us-dollar-index-historical-data
    Make sure to replace the filename variable in the code with the corresponding filename for each asset.
    """

