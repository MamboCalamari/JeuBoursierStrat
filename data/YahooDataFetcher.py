from datetime import datetime
import pandas as pd
from pandas_datareader import data,wb
from yahoo_finance import Share


class PandasDataFetcher:
    #grabs price data on chosen stocks on a specified interval and price type (open, adj_close, etc.)
    @staticmethod
    def fetch_data_pandas(stocks, ls_key, start, end):
        pd.set_option('max_rows', 1000000)
        pd.set_option("display.max_rows", 100000)
        f = data.DataReader(stocks, 'yahoo', start, end)
        clean_data = f.ix[ls_key]
        data_frame = pd.DataFrame(clean_data)
        daily_price_data = {}
        for stock in stocks:
            stock_frame = data_frame.loc[:, stock]
            daily_prices = data_frame.loc[:, stock].values.tolist()
            daily_price_data[stock] = daily_prices
        return daily_price_data

    #same as above but uses simpler yahoo-finance package
    @staticmethod
    def fetch_data_yahoo(stocks, price_type, start, end):
        daily_price_data = {}
        for stock in stocks:
            share = Share(stock)
            # dates already return in most recent to leasr recent order
            all_stock_data = Share.get_historical(share, start, end)
            daily_prices = []
            for day in all_stock_data:
                daily_prices.append(day[price_type])
            daily_price_data[stock] = daily_prices
        return daily_price_data