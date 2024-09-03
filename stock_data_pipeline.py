import requests
import pandas as pd
import sqlite3
from datetime import datetime

# Define your Alpha Vantage API key and stock symbol
API_KEY = 'your_api_key'
SYMBOL = 'AAPL'

# Function to fetch stock data from Alpha Vantage
def fetch_stock_data(api_key, symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Time Series (Daily)']

# Function to process the data
def process_stock_data(raw_data):
    # Convert the JSON data to a DataFrame
    df = pd.DataFrame.from_dict(raw_data, orient='index')
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. adjusted close': 'Adj Close',
        '6. volume': 'Volume'
    })
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    # Convert columns to numeric types
    df = df.apply(pd.to_numeric)

    # Calculate technical indicators
    df['SMA_50'] = df['Adj Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Adj Close'].rolling(window=200).mean()
    df['Volatility'] = df['Adj Close'].rolling(window=20).std()
    df['Returns'] = df['Adj Close'].pct_change()
    df['RSI'] = calculate_rsi(df['Adj Close'])

    return df

# Function to calculate RSI (Relative Strength Index)
def calculate_rsi(series, period=14):
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to save data to CSV and SQLite database
def save_data(df, symbol):
    # Save to CSV
    csv_file = f'{symbol}_stock_data.csv'
    df.to_csv(csv_file)
    print(f'Data saved to {csv_file}')

    # Save to SQLite database
    conn = sqlite3.connect('stock_data.db')
    df.to_sql(symbol, conn, if_exists='replace', index=True)
    conn.close()
    print(f'Data saved to SQLite database as table: {symbol}')

# Function to execute SQL from file
def execute_sql_from_file(file_path):
    conn = sqlite3.connect('stock_data.db')
    with open(file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    conn.executescript(sql_script)
    conn.close()
    print(f'SQL script {file_path} executed successfully.')

# Main function
def main():
    raw_data = fetch_stock_data(API_KEY, SYMBOL)
    processed_data = process_stock_data(raw_data)
    save_data(processed_data, SYMBOL)
    execute_sql_from_file('queries.sql')

if __name__ == '__main__':
    main()
