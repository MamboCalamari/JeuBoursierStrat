from pandas import DataFrame
from pandas_datareader import data,wb
import datetime as dt
import matplotlib.pyplot as plt
from yahoo_finance import Share
from pprint import pprint

# start = dt.datetime(2001,7,1)
# end = dt.datetime(2016,7,1)
#
# data = data.DataReader('AAPL','yahoo',start,end)
# vals = data.get_values()
# x = []
# for i in range(len(vals)):
#     x.append(i)

# plt.plot(x, vals, color='green', marker='o', linestyle='solid')
# plt.title('AAPL')
# plt.show()

stocks = ['CSCO','WMT','PG','MRK','PFE','XOM','IBM','CAT','CVX','VZ','AAPL','GOOG','IAU'
    ,'SLV','USO','AMD','BAC','MSFT','FTR','BBRY','MDCO','AAOI','CLVS','BLUE','ALNY']
# ls_key = 'Adj Close'
# start = dt.datetime(2014,1,1)
# end = dt.datetime(2014,3,28)
#f = data.DataReader(stocks, 'yahoo',start,end)


# cleanData = f.ix[ls_key]
# dataFrame = DataFrame(cleanData)
#
# series = dataFrame.loc[:,'FTR']
# x = series.values.tolist()
# print(x)
for stock in stocks:
    share = Share(stock)
    #dates already return in most recent to leasr recent order
    all_stock_data = Share.get_historical(share,'2017-01-01','2017-04-03')
    daily_prices = []
    daily_price_data = {}
    for day in all_stock_data:
        daily_prices.append(day['Adj_Close'])
    daily_price_data[stock] = daily_prices
