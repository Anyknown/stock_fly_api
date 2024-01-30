import alpha_vantage
import pandas as pd


API_KEY = 'QIF8N31AVQSTQK8C'
symbols = ['TSLA', 'U', 'TWLO', 'AMZN', 'ASML', 'ATEN']


client = alpha_vantage.APIClient(key=API_KEY)


intraday_data = client.get_intraday(symbol=','.join(symbols), interval='1min')


closes = [intraday_data['Time Series (1min)'][symbol]['4. close'] for symbol in symbols]


df = pd.DataFrame(closes, index=symbols, columns=['Close'])


df['Purchase Price'] = None


df['% Growth/Loss'] = None


def calculate_growth_loss(row):
    if row['Purchase Price'] is not None:
        return ((row['Close'] - row['Purchase Price']) / row['Purchase Price']) * 100
    else:
        return None


df['% Growth/Loss'] = df.apply(calculate_growth_loss, axis=1)


print(df)
