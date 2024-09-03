# Stock-Market-Data-Pipeline
Automated Stock Price Monitoring and Analysis using Python and SQL

# Stock Market Data Pipeline

## Overview
This project provides an automated pipeline to fetch, process, and analyze stock market data. The pipeline is designed to collect daily stock prices from the Alpha Vantage API, compute key technical indicators (such as moving averages, volatility, and RSI), and save the results for further analysis or visualization.

## Features
- **Automated Data Extraction**: Pulls daily stock data from the Alpha Vantage API.
- **Data Transformation**: Calculates key technical indicators:
  - Simple Moving Average (SMA)
  - Volatility (rolling standard deviation)
  - Relative Strength Index (RSI)
- **Data Storage**: Saves the processed data to a CSV file.
- **Analysis Capabilities**: Enables the exploration of various data analysis questions to guide investment or trading decisions.

## Data Analysis Questions
Here are some key questions you can answer using the data extracted and processed by this pipeline:

### 1. What are the Key Trends in Stock Price Over Time?
Analyze the trend of the stock's closing prices over periods (e.g., months, years) using moving averages (SMA 50 and SMA 200) to observe long-term trends.

### 2. How Volatile is the Stock Over a Given Period?
Measure the stock's volatility to understand the risk associated with the stock by analyzing the rolling standard deviation of price returns.

### 3. Is the Stock Overbought or Oversold?
Use the Relative Strength Index (RSI) to determine if the stock is potentially overbought (RSI > 70) or oversold (RSI < 30), which can indicate potential price reversals.

### 4. How Does the Stock Perform Relative to Its Long-Term Moving Average?
Compare the stock’s current price to its 50-day and 200-day moving averages to identify bullish or bearish trends.

### 5. What is the Relationship Between Trading Volume and Price Movements?
Investigate how changes in trading volume correspond with price movements to confirm trends or predict potential reversals.

### Libraries
- Python 3.x
- Required Python packages: `requests`, `pandas`

### Installation Steps
1. Clone the repository or download the script.
2. Install the required Python packages:

   ```bash
   pip install requests pandas


