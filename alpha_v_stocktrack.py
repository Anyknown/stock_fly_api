import pandas as pd
import requests


API_KEY = 'QIF8N31AVQSTQK8C'
API_URL = 'https://www.alphavantage.co/query'

symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']


params = {
    'function': 'GLOBAL_QUOTE',
    'apikey': API_KEY,
    'datatype': 'json',
    'symbols': ','.join(symbols)
}
response = requests.get(API_URL, params=params)
data = response.json()
current_prices = {k.split('.')[1]: v['2. price'] for k, v in data.items()}


df = pd.DataFrame(columns=['Purchase Price', 'Symbol', 'Percentage Change'])

while True:
    try:
        purchase_price = float(input('Enter the purchase price for a stock: '))
        symbol = input('Enter the stock symbol (TSLA, U, TWLO, AMZN, ASML, ATEN): ')

        if symbol not in symbols:
            print('Invalid symbol. Please try again.')
            continue

        if symbol not in current_prices:
            print('Error fetching current price. Please try again.')
            continue

        current_price = float(current_prices[symbol])

        
        percentage_change = ((current_price - purchase_price) / purchase_price) * 100

       
        new_row = pd.DataFrame([[purchase_price, symbol, percentage_change]],
                               columns=['Purchase Price', 'Symbol', 'Percentage Change'])

        
        df = df.append(new_row, ignore_index=True)

        print('Stock added successfully.')

    except ValueError:
        print('Invalid input. Please try again.')

   
    print(df.to_string(index=False))
