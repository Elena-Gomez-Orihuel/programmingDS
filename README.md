# ProgrammingDS

This is a project for the subject Programming for Data Science.

## Authors - Group 10

- Elena María Gómez Orihuel
- María Lara Trullenque
- Ignacio López Carboneras
- Jaime Guerrero Carrasco
- Javier Rocamora García

## Description

The project is divided into three parts:

- **Part 1 - Web Scraping:** Generates 5 CSV files corresponding to each of the assets (through _web scraping_). The assets are:
  - ***Stocks (ST):*** _amundi-msci-world-ae-c.csv_
  - ***Corporate bonds (CB):*** _ishares-global-corporate-bond-$.csv_
  - ***Public bonds (PB):*** _db-x-trackers-ii-global-sovereign-5.csv_
  - ***Gold (GO):*** _spdr-gold-trust.csv_
  - ***Cash (CA):*** _usdollar.csv_
  
  The code corresponding to this part can be found in _part1.py_
  
- **Part 2 - Data Generation:** Generates the _portfolio_metrics.csv_ file where the return and volatility have been calculated for each of the possible portfolios.

  The code corresponding to this part can be found in _part2.py_

- **Part 3 - Data Analysis:** Conducts a data analysis generating different graphs that will serve to analyze the data and draw conclusions.

  The code corresponding to this part can be found in _part3_analysis.ipynb_

## Installation

To run the project, you need to have Python 3 and the following libraries installed:

- pandas
- datetime
- statistics
- matplotlib
- seaborn
- numpy

They can be installed via command:

```bash
pip install -r requirements.txt
```

## Usage

To run the project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project folder.
3. Install the necessary requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run the following command to generate the CSV files for each of the assets (wait until the _web scraping_ is finished):
    ```bash
    python3 part1.py
    ```
5. Run the following command to generate the "portfolio_metrics.csv" file:
    ```bash
    python3 part2.py
    ```
5. Run the Jupyter Notebook ***part3_analysis.ipynb*** to generate the graphs that appear in the report.


