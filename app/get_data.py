import yfinance as yf
import pandas as pd

#delcaring a retreving the tesla stock by ticker 'TSLA'
tsla = yf.Ticker("TSLA" )

# storing the ticker history of 1 year as a pandas dataframe
tsla_df = tsla.history(period="1y")

# converting data to csv
tsla_df.to_csv('tsla.csv')



