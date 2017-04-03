import datetime as dt

import math
import statistics
from pprint import pprint
from data.YahooDataFetcher import YahooDataFetcher


class SignalGenerator:
    def __init__(self, stocks, price_type, start, end, momentum_weight, jump_weight):
        # stocks to be traded
        self.stocks = stocks
        # type of data used
        self.ls_key = price_type
        self.start = start
        self.end = end
        self.momentum_weight = momentum_weight
        self.jump_weight = jump_weight

    #generates a signal between -3 or 3 based on momentum and jump for each stock
    def generateSignals(self):
        daily_price_data = YahooDataFetcher.fetch_data_yahoo(self.stocks, self.ls_key, self.start, self.end)
        print('Generating signals...')
        daily_returns = self.get_daily_returns(daily_price_data)
        momentum = self.calculate_momentum(daily_returns)
        self.write_dict_to_file(momentum, "momentum.txt", True)

        momentum_signals = {}
        for stock in self.stocks:
            z_score = (momentum[stock][0]-statistics.mean(momentum[stock]))/statistics.stdev(momentum[stock])
            momentum_signal = z_score/3
            momentum_signals[stock] = momentum_signal
        self.write_dict_to_file(momentum_signals, "momentum_signals.txt", False)

        jump_signals = {}
        for stock in self.stocks:
            recent_avg = statistics.mean([daily_returns[stock][0],daily_returns[stock][1]])
            sample_40_days = []
            for i in range(40):
                sample_40_days.append(daily_returns[stock][i+2])
            sample_avg = statistics.mean(sample_40_days)
            jump = (recent_avg-sample_avg)/statistics.stdev(sample_40_days)
            jump_signal = -jump/3.0
            jump_signals[stock] = jump_signal
        self.write_dict_to_file(momentum_signals, "jump_signals.txt", False)

        combined_signals = {}
        for stock in self.stocks:
            combined_signals[stock] = self.momentum_weight * momentum_signals[stock] + self.jump_weight * jump_signals[stock]

        self.write_dict_to_file(momentum_signals, "combined_signals.txt", False)

    def get_daily_returns(self, daily_price_data):
        daily_returns = {}
        for stock in self.stocks:
            stock_daily_prices = daily_price_data[stock]
            stock_daily_returns = []
            for i in range(len(stock_daily_prices) - 1):
                stock_daily_returns.append(float(stock_daily_prices[i])/float(stock_daily_prices[i+1]) - 1)
            daily_returns[stock] = stock_daily_returns
        return daily_returns

    def calculate_momentum(self, daily_returns):
        log_daily_returns = self.get_log_daily_returns(daily_returns)
        sums_75_day = self.get_75_day_sums(log_daily_returns)
        stddev_75_day = self.get_75_day_stddev(log_daily_returns)
        momentum = {}
        for stock in self.stocks:
            stock_momentum = []
            for day in range(len(list(sums_75_day.values())[0])):
                stock_momentum.append(sums_75_day[stock][day]/stddev_75_day[stock][day])
            momentum[stock] = stock_momentum
        return momentum

    def get_log_daily_returns(self, daily_returns):
        log_daily_returns = {}
        for stock in daily_returns:
            stock_log_daily_returns = []
            for _return in daily_returns[stock]:
                stock_log_daily_returns.append(math.log(_return + 1))
            log_daily_returns[stock] = stock_log_daily_returns
        return log_daily_returns

    def get_75_day_sums(self, log_daily_returns):
        sums_75_day = {}
        for stock in self.stocks:
            stock_75_day_sums = []
            for current_day in range(len(log_daily_returns[stock]) - 75):
                sum = 0.0
                for past_day in range(75):
                    sum += log_daily_returns[stock][current_day + past_day]
                stock_75_day_sums.append(sum)
            sums_75_day[stock] = stock_75_day_sums
        return sums_75_day

    def get_75_day_stddev(self, log_daily_returns):
        stddev_75_day = {}
        for stock in self.stocks:
            stock_75_day_stddev = []
            for current_day in range(len(log_daily_returns[stock]) - 75):
                sample_75_day = []
                for past_day in range(75):
                    sample_75_day.append(log_daily_returns[stock][current_day + past_day])
                stock_75_day_stddev.append(statistics.stdev(sample_75_day))
            stddev_75_day[stock] = stock_75_day_stddev
        return stddev_75_day

    def write_dict_to_file(self, dict, filename, value_is_list):
        file = open(filename, "w")
        if value_is_list:
            for key in dict.keys():
                file.write(key + '\n')
                for data in dict[key]:
                    file.write(str(data) + '\n')
        else:
            for key in dict.keys():
                file.write(key + '\n')
                file.write(str(dict[key]) + '\n')
        file.close()



gen = SignalGenerator(['CSCO', 'WMT', 'PG', 'MRK', 'PFE', 'XOM', 'IBM', 'CAT', 'CVX', 'VZ', 'AAPL', 'GOOG', 'GG','SSRI', 'TGT', 'AMD', 'BAC', 'MSFT', 'F', 'BBRY', 'MDCO', 'AAOI', 'CLVS', 'BLUE', 'ALNY'],
                      'Adj_Close','2016-01-01','2017-03-04',0.8,0.2)
gen.generateSignals()
