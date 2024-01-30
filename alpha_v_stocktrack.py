import pandas as pd
import requests

# Function to fetch stock prices using Alpha Vantage API
def fetch_stock_prices():
    api_key = "QIF8N31AVQSTQK8C"
    symbols = ["TSLA", "U", "TWLO", "AMZN", "ASML", "ATEN"]
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbols={','.join(symbols)}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    stock_prices = {}
    for symbol in symbols:
        stock_prices[symbol] = float(data[f"Global Quote.05.price"].get(symbol))
    return stock_prices

# Function to calculate percentage growth or loss
def calculate_growth(purchase_prices, stock_prices):
    growth = {}
    for symbol in stock_prices:
        growth[symbol] = ((stock_prices[symbol] - purchase_prices[symbol]) / purchase_prices[symbol]) * 100
    return growth

# Prompt user to enter purchase prices
purchase_prices = {}
symbols = ["TSLA", "U", "TWLO", "AMZN", "ASML", "ATEN"]
for symbol in symbols:
    purchase_prices[symbol] = float(input(f"Enter purchase price for {symbol}: "))

# Fetch stock prices
stock_prices = fetch_stock_prices()

# Calculate percentage growth or loss
growth = calculate_growth(purchase_prices, stock_prices)

# Create a Pandas DataFrame
df = pd.DataFrame(list(growth.items()), columns=["Stock", "Growth (%)"])

# Add a column for purchase prices
df.insert(0, "Purchase Price", list(purchase_prices.values()))

# Print the DataFrame
print(df)
