import pandas as pd
import requests

# Define the API request for Alpha Vantage
API_KEY = "QIF8N31AVQSTQK8C"
API_URL = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbols=TSLA,U,TWLO,AMZN,ASML,ATEN&apikey={API_KEY}"

# Fetch the stock prices from Alpha Vantage
response = requests.get(API_URL)
stock_data = response.json()

# Prepare the DataFrame
data = []
for symbol in ["TSLA", "U", "TWLO", "AMZN", "ASML", "ATEN"]:
    stock_price = stock_data["Global Quote"]["05. price"][symbol]
    data.append([None, stock_price, None])

# Create the DataFrame
df = pd.DataFrame(data, columns=["Purchase Price", "Current Stock Price", "Growth/Loss %"])

# Calculate the growth/loss %
df.loc[:, "Growth/Loss %"] = df["Current Stock Price"].pct_change()

# Save the DataFrame to an Excel file
df.to_excel("stock_table.xlsx", index=False)
