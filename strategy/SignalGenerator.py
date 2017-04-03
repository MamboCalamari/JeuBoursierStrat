import datetime as dt

import math

from data.YahooDataFetcher import PandasDataFetcher


class SignalGenerator:
    def __init__(self, stocks, price_type, start, end):
        # stocks to be traded
        self.stocks = stocks
        # type of data used
        self.ls_key = price_type
        self.start = start
        self.end = end

    #generates a signal between -3 or 3 based on momentum and jump for each stock
    def generateSignals(self):
        daily_price_data = PandasDataFetcher.fetch_data_yahoo(self.stocks, self.ls_key, self.start, self.end)
        daily_momentum = self.get_daily_momentum(daily_price_data)

    #calculates momentum for each day
    def get_daily_momentum(self, daily_price_data):
        for stock in self.stocks:
            stock_daily_prices = daily_price_data[stock]
            log_daily_returns = []
            for i in range(len(stock_daily_prices) - 1):
                #log of daily return = ln(day/previous day)
                log_daily_returns.append(math.log(float(stock_daily_prices[i])/float(stock_daily_prices[i+1])))
            print(log_daily_returns)



gen = SignalGenerator(['CSCO', 'WMT', 'PG', 'MRK', 'PFE', 'XOM', 'IBM', 'CAT', 'CVX', 'VZ', 'AAPL', 'GOOG', 'IAU','SLV', 'USO', 'AMD', 'BAC', 'MSFT', 'FTR', 'BBRY', 'MDCO', 'AAOI', 'CLVS', 'BLUE', 'ALNY'],
                      'Adj_Close','2017-01-01','2017-04-03')
gen.generateSignals()
