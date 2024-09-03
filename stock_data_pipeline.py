import requests
import pandas as pd
import time

# Constants here
API_KEY = 'your_api_key'  # Replace with your Alpha Vantage API key
SYMBOL = 'AAPL'  # Replace with the stock symbol you want to track
BASE_URL = 'https://www.alphavantage.co/query'
CSV_FILE_PATH = 'stock_data.csv'

def fetch_stock_data(symbol, api_key):
    """Fetch daily stock data from Alpha Vantage API."""
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Handle potential API errors
    if "Error Message" in data:
        raise Exception(f"Error fetching data: {data['Error Message']}")
    
    time_series = data['Time Series (Daily)']
    df = pd.DataFrame(time_series).T
    df = df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    })
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df

def calculate_technical_indicators(df):
    """Calculate moving averages, volatility, and RSI."""
    df['SMA_50'] = df['close'].rolling(window=50).mean()
    df['SMA_200'] = df['close'].rolling(window=200).mean()
    df['Volatility'] = df['close'].pct_change().rolling(window=20).std()
    df['RSI'] = compute_rsi(df['close'], 14)
    return df

def compute_rsi(series, period):
    """Compute the Relative Strength Index (RSI)."""
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def save_to_csv(df, file_path):
    """Save DataFrame to a CSV file."""
    df.to_csv(file_path, index=True)
    print(f"Data saved to {file_path}")

def main():
    try:
        df = fetch_stock_data(SYMBOL, API_KEY)
        df = calculate_technical_indicators(df)
        save_to_csv(df, CSV_FILE_PATH)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
