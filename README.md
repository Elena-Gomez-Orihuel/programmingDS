# programmingDS

This is a project for the subject Programming for Data Science.

## Description

The project is divided into three parts:

- **Part 1**: Generates 5 CSV files corresponding to each of the assets. The assets are:
  - _Stocks (ST)_: amundi-msci-world-ae-c.csv
  - _Corporate bonds (CB)_: ishares-global-corporate-bond-$.csv
  - _Public bonds (PB)_: db-x-trackers-ii-global-sovereign-5.csv
  - _Gold (GO)_: spdr-gold-trust.csv
  - _Cash (CA)_: usdollar.csv
- **Part 2**: Generates the "portfolio_metrics.csv" file where the return and volatility have been calculated for each of the possible portfolios.
- **Part 3**: Conducts a data analysis generating different graphs that will serve to analyze the data and draw conclusions.

## Installation

To run the project, you need to have Python 3 and the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn

## Usage

To run the project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project folder.
3. Run the following command to generate the CSV files for each of the assets:
    ```bash
    python part1.py
    ```
4. Run the following command to generate the "portfolio_metrics.csv" file:
    ```bash
    python part2.py
    ```
5. Run the Jupyter Notebook _part3_analysis.ipynb_ to generate the graphs that appear in the report.


