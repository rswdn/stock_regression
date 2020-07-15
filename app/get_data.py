import yfinance as yf
import pandas as pd

#declearing and retreiving the tesla stock by ticker 'TSLA'
tsla = yf.Ticker("TSLA" )

# storing the ticker history of 1 year as a pandas dataframe
tsla_df = tsla.history(period="max")

# converting dataframe to csv
tsla_df.to_csv('tsla.csv')



