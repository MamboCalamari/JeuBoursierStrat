from strategy.SignalGenerator import SignalGenerator


class PortfolioManager:
    @staticmethod
    def get_signals():
        gen = SignalGenerator(
            ['CSCO', 'WMT', 'PG', 'MRK', 'PFE', 'XOM', 'IBM', 'CAT', 'CVX', 'VZ', 'AAPL', 'GOOG', 'GG', 'SSRI', 'TGT',
             'AMD', 'BAC', 'MSFT', 'F', 'BBRY', 'AAOI', 'CLVS', 'BLUE', 'ALNY'],
            'Adj_Close', '2016-01-01', '2017-05-05', 0.8, 0.2)
        signals = gen.generateSignals()
        return signals

    @staticmethod
    def read_portfolio():
        file = open("portfolio.txt", "r")
        lines = file.read().splitlines()
        file.close()
        positions = {}
        line = 0
        while line < len(lines):
            positions[lines[line]] = int(lines[line+1])
            line += 2
        return positions

    @staticmethod
    def suggest_orders():
        positions = PortfolioManager.read_portfolio()
        signals = PortfolioManager.get_signals()
        for stock in signals.keys():
            print("Shares to buy/sell for " + stock + ": " + str(int(round(signals[stock] * positions[stock]))))
        #TODO calculate stocks only to be sold, and then uses buying power to calculate shares to be bought

    #update the portfolio file to reflect changes
    @staticmethod
    def update_portfolio():
        pass

PortfolioManager.suggest_orders()