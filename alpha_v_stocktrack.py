import pandas as pd
import alpha_vantage
from datetime import datetime
df = pd.DataFrame(columns=['Ticker', 'Current Price', 'Growth/Loss'])
def fetch_stock_prices():
    api_key = "QIF8N31AVQSTQK8C"
    av = alpha_vantage.API(key=api_key)
    symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']
    for symbol in symbols:
        data, meta_data = av.get_daily(symbol=symbol)
        df = df.append({'Ticker': symbol, 'Current Price': data['4. close'][0]}, ignore_index=True)
        def calculate_growth_loss():
    df['Growth/Loss'] = df['Current Price'].pct_change()
    df_purchase_prices = pd.DataFrame(columns=[df.columns[0], df.columns[2]])
df = pd.concat([df, df_purchase_prices], ignore_index=True)
df.to_csv('alpha_v_stocktrack.csv', index=False)
