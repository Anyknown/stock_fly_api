import pandas as pd
import requests
import sys

API_KEY = 'QIF8N31AVQSTQK8C'
symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']

stock_prices = {}
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    stock_prices[symbol] = float(data['Global Quote']['05. price'])

purchase_prices = [float(price) for price in sys.argv[1:]]  # Accept purchase prices as command-line arguments

df = pd.DataFrame({
    'Stock Ticker': symbols,
    'Purchase Price': purchase_prices,
    'Real-Time Price': [stock_prices[symbol] for symbol in symbols]
})

df['% Profit/Loss'] = ((df['Real-Time Price'] - df['Purchase Price']) / df['Purchase Price']) * 100

df.to_csv('stock_prices.csv', index=False)
