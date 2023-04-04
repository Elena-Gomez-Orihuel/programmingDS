import csv
from itertools import product
from math import factorial
import pandas as pd
import statistics
from math import sqrt


######################### Portforlio allocations ################################
def num_combinations(m, n):
    return factorial(m+n-1) // (factorial(n) * factorial(m - 1))

def create_portfolio_allocations_csv(assets, delta):
    total = 100
    num_pieces = total // delta
    if num_pieces == 0 or total % delta != 0:
        raise ValueError("Invalid delta value. Please, select a valid delta value between: 1, 2, 4, 5, 10, 20, 25, 50 and 100")
    combinations = list(product(range(num_pieces+1), repeat=len(assets)))
    with open('portfolio_allocations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(assets)
        for combination in combinations:
            if sum(combination) == num_pieces:
                row = [int(x*delta) for x in combination]
                writer.writerow(row)
    print('Number of combinations: ' + str(num_combinations(len(assets), num_pieces)))


################## Portforlio performance #######################

#################### Return #######################
def calculate_return():
    portfolio_allocations = pd.read_csv("portfolio_allocations.csv")

    # Read in the share prices from separate CSV files for each asset
    ST_prices = pd.read_csv("amundi-msci-wrld-ae-c.csv")
    PB_prices = pd.read_csv("db-x-trackers-ii-global-sovereign-5.csv")
    CB_prices = pd.read_csv("ishares-global-corporate-bond-$.csv")
    GO_prices = pd.read_csv("spdr-gold-trust.csv")
    CA_prices = pd.read_csv("usdollar.csv")

    # Extract the share prices as of 01/01/2020
    ST_price_buy = ST_prices["Price"].values[-1]
    PB_price_buy = PB_prices["Price"].values[-1]
    CB_price_buy = CB_prices["Price"].values[-1]
    GO_price_buy = GO_prices["Price"].values[-1]
    CA_price_buy = CA_prices["Price"].values[-1]

    # Extract the share prices as of 12/31/2020
    ST_prices_current = ST_prices["Price"].values[0]
    PB_prices_current = PB_prices["Price"].values[0]
    CB_price_current = CB_prices["Price"].values[0]
    GO_price_current = GO_prices["Price"].values[0]
    CA_price_current = CA_prices["Price"].values[0]

    # Create an empty DataFrame to store the portfolio returns
    return_list=[]
    # Loop over each row in the portfolio allocations DataFrame
    for i in range(len(portfolio_allocations)):
        # Extract the portfolio allocations for the current row
        portfolio = portfolio_allocations.iloc[i].to_dict()
        
        # Calculate the total buy amount and current value of the portfolio
        buy_amount = (portfolio["ST"] * ST_price_buy) + (portfolio["CB"] * CB_price_buy) + (portfolio["PB"] * PB_price_buy) + (portfolio["GO"] * GO_price_buy) + (portfolio["CA"] * CA_price_buy)
        current_value = (portfolio["ST"] * ST_prices_current) + (portfolio["CB"] * CB_price_current) + (portfolio["PB"] * PB_prices_current) + (portfolio["GO"] * GO_price_current) + (portfolio["CA"] * CA_price_current)
        
        # Calculate the portfolio return as a percentage
        portfolio_return = ((current_value - buy_amount) / buy_amount) * 100
        
        # Add the portfolio return to the list
        return_list.append(portfolio_return)

    # Return the list of returns values
    return return_list    

#################### Volatility #######################
def calculate_volatility():
    # Read in the share prices from separate CSV files for each asset
    portfolio_allocations = pd.read_csv("portfolio_allocations.csv")

    ST_df = pd.read_csv("amundi-msci-wrld-ae-c.csv")
    PB_df = pd.read_csv("db-x-trackers-ii-global-sovereign-5.csv")
    CB_df = pd.read_csv("ishares-global-corporate-bond-$.csv")
    GO_df = pd.read_csv("spdr-gold-trust.csv")
    CA_df = pd.read_csv("usdollar.csv")
    
    ST_df['Date'] = pd.to_datetime(ST_df['Date'], format='%b %d, %Y')
    PB_df['Date'] = pd.to_datetime(PB_df['Date'], format='%m/%d/%Y')
    CB_df['Date'] = pd.to_datetime(CB_df['Date'], format='%m/%d/%Y')
    GO_df['Date'] = pd.to_datetime(GO_df['Date'], format='%m/%d/%Y')
    CA_df['Date'] = pd.to_datetime(CA_df['Date'], format='%m/%d/%Y')

    all_dates = ST_df.merge(PB_df, on='Date', how='inner', suffixes=('_ST', '_PB')).merge(CB_df, on='Date', how='inner', suffixes=('_PB', '_CB')).merge(GO_df, on='Date', how='inner', suffixes=('_CB', '_GO')).merge(CA_df, on='Date', how='inner', suffixes=('_GO', '_CA'))
    # Crear una máscara booleana para cada dataset indicando si la fecha está presente en la lista de fechas únicas
    mask1 = ST_df['Date'].isin(all_dates['Date'])
    mask2 = PB_df['Date'].isin(all_dates['Date'])
    mask3 = CB_df['Date'].isin(all_dates['Date'])
    mask4 = GO_df['Date'].isin(all_dates['Date'])
    mask5 = CA_df['Date'].isin(all_dates['Date'])

    ST_df = ST_df[mask1]
    PB_df = PB_df[mask2]
    CB_df = CB_df[mask3]
    GO_df = GO_df[mask4]
    CA_df = CA_df[mask5]

    ST_prices = ST_df["Price"].values
    PB_prices = PB_df["Price"].values
    CB_prices = CB_df["Price"].values
    GO_prices = GO_df["Price"].values
    CA_prices = CA_df["Price"].values

    # Create an empty DataFrame to store the values of Value
    VOLAT=[]
    # Loop over each row in the portfolio allocations DataFrame
    for i in range(len(portfolio_allocations)):
        # Extract the portfolio allocations for the current row
        values_porfolio = []
        portfolio = portfolio_allocations.iloc[i].to_dict()
        for j in range(len(ST_prices)):
            value = (portfolio["ST"] * ST_prices[j]) + (portfolio["CB"] *CB_prices[j] ) + (portfolio["PB"] * PB_prices[j]) + (portfolio["GO"] * GO_prices[j]) + (portfolio["CA"] * CA_prices[j])
            values_porfolio.append(value)
        #media
        portfolio_mean = statistics.mean(values_porfolio)
        #desviacion
        #portfolio_stdev = statistics.stdev(values_porfolio)
        portfolio_stdev = sqrt(sum((x - portfolio_mean)**2 for x in values_porfolio) / (len(values_porfolio)))

        #volatility
        volatility= (portfolio_stdev/portfolio_mean)*100
        VOLAT.append(volatility)
    return VOLAT

#################### Metrics #######################
def calculate_metrics():
    portfolio_metrics = pd.read_csv("portfolio_allocations.csv")
    portfolio_metrics['RETURN'] = calculate_return()
    portfolio_metrics['VOLAT'] = calculate_volatility()
    portfolio_metrics.to_csv("portfolio_metrics.csv", index=False) 

############### Main ejecution ####################
if __name__ == '__main__':
    assets = ['ST', 'CB', 'PB', 'GO', 'CA']
    delta = 20
    create_portfolio_allocations_csv(assets, delta)
    calculate_metrics()
