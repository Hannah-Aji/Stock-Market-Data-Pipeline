-- Example SQL Queries for Stock Data Analysis

-- Select Date, Close Price, and Moving Averages after January 1, 2023
SELECT Date, Close, SMA_50, SMA_200
FROM AAPL
WHERE Date > '2023-01-01'
ORDER BY Date DESC;

-- Count the number of trading days in 2023
SELECT COUNT(Date) AS TradingDays2023
FROM AAPL
WHERE Date LIKE '2023%';

-- Calculate the average closing price for 2023
SELECT AVG(Close) AS AvgClose2023
FROM AAPL
WHERE Date LIKE '2023%';
