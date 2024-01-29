pip install alpha_vantage
import alpha_vantage
import pandas as pd
from tabulate import tabulate

ts = alpha_vantage.timeseries.TimeSeries(key='QIF8N31AVQSTQK8C', output_format='pandas')
symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ATEN', 'ASML']
data_dict = {}

for symbol in symbols:
    data, meta_data = ts.get_daily(symbol=symbol)
    data_dict[symbol] = data['6. close'][0]
  df = pd.DataFrame(data_dict.items(), columns=['Symbol', 'Price'])
df['Purchase Price'] = None
df['% Growth/Loss'] = None

def calculate_growth(row):
    if row['Purchase Price'] is not None:
        return ((row['Price'] - row['Purchase Price']) / row['Purchase Price']) * 100
    else:
        return None

df['% Growth/Loss'] = df.apply(calculate_growth, axis=1)
print(tabulate(df, headers='keys', tablefmt='grid'))
