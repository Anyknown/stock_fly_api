import pandas as pd
import requests

API_KEY = 'QIF8N31AVQSTQK8C'
symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']

stock_prices = {}
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    stock_prices[symbol] = float(data['Global Quote']['05. price'])

purchase_prices = []
for symbol in symbols:
    while True:
        try:
            price_input = input(f"Enter purchase price for {symbol}: ")
            purchase_price = float(price_input)
            purchase_prices.append(purchase_price)
            break  # Exit the loop if input and conversion are successful
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

df = pd.DataFrame({
    'Stock Ticker': symbols,
    'Purchase Price': purchase_prices,
    'Real-Time Price': [stock_prices[symbol] for symbol in symbols]
})

df['% Profit/Loss'] = ((df['Real-Time Price'] - df['Purchase Price']) / df['Purchase Price']) * 100

df.to_csv('stock_prices.csv', index=False)
