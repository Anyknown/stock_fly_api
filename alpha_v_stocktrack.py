import pandas as pd
import requests
df = pd.DataFrame({'Purchase Price': []})
API_KEY = 'QIF8N31AVQSTQK8C'
symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']

stock_prices = {}
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    stock_prices[symbol] = float(data['Global Quote']['05. price'])
    df['Stock Price'] = list(stock_prices.values())
    df['% Growth/Loss'] = (df['Stock Price'] - df['Purchase Price']) / df['Purchase Price'] * 100
    df.to_csv('stock_prices.csv', index=False)
