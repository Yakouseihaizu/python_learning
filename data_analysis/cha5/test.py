# import pandas_datareader.data as web
# import pandas as pd
# all_data = {ticker:web.get_data_yahoo(ticker)
#             for ticker in ['AAPL','IBM','MSFT','GOOG']}
# price = pd.DataFrame({ticker: data['Adj Colse']
#                       for ticker,data in all_data.items()})
# volume = pd.DataFrame({ticker : data['Volumn']
#                        for ticker,data in all_data.items()})

# print(price)
import yfinance as yf
import pandas as pd
all_data = yf.download(['AAPL','IBM','MSFT','GOOG'],start='2023-11-01',end='2023-12-01')

# price = pd.DataFrame({ticker: data['Adj Close']
#                       for ticker,data in all_data.items()})
price = all_data['Adj Close']
# print(all_data)
volume = all_data['Volume']
print(price)
print('-'*30)
print(volume)