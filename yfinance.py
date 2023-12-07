import yfinance as yf
import pandas as pd

# Define the ticker symbol for EUR/USD
ticker_symbol = "EURUSD=X"

# Define the start and end dates
start_date = "2010-01-01"
end_date = "2023-10-31"

# Download historical data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the downloaded data
print(data.head())

# Save the data to a CSV file
file_path = "/Users/bastienlavialle/Desktop/eur_usd_exchange_rate.csv"
data.to_csv(file_path)
print(f"Data saved to: {file_path}")
