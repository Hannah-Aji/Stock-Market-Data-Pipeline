# Stock-Market-Data-Pipeline
Automated Stock Price Monitoring and Analysis using Python and SQL

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
3. Obtain an API key from Alpha Vantage.
4. Replace 'your_api_key' in the script with your actual API key.
5. Customize the SYMBOL variable with the stock symbol you're interested in.

   ```bash
   pip install requests pandas

## Usage
1. Run the script to fetch and process stock data:

   ```bash
   python stock_data_pipeline.py

2. The script will save the processed data to a CSV file (stock_data.csv) in the same directory.

3. Analyze the CSV file using your preferred data analysis or visualization tool (e.g., Excel, Tableau, Power BI).

## Scheduling
To automate the pipeline, I scheduled the script to run at regular intervals using a task scheduler (Task Scheduler on Windows).
To run the script daily at 6 PM using cron:

  ```bash
  crontab -e
  0 18 * * * /usr/bin/python3 /path/to/your/stock_data_pipeline.py




