from strategy.SignalGenerator import SignalGenerator


class PortfolioManager:
    @staticmethod
    def get_signals():
        gen = SignalGenerator(
            ['CSCO', 'WMT', 'PG', 'MRK', 'PFE', 'XOM', 'IBM', 'CAT', 'CVX', 'VZ', 'AAPL', 'GOOG', 'GG', 'SSRI', 'TGT',
             'AMD', 'BAC', 'MSFT', 'F', 'BBRY', 'AAOI', 'CLVS', 'BLUE', 'ALNY', 'KITE'],
            'Adj_Close', '2016-01-01', '2017-05-05', 0.8, 0.2)
        signals = gen.generateSignals()
        return signals

    @staticmethod
    def get_signals_SP_500():
        gen = SignalGenerator(['ABT', 'ABBV', 'ACN', 'ADBE', 'ADT', 'AAP', 'AES', 'AET', 'AFL', 'AMG', 'A', 'APD', 'ARG', 'AKAM', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX', 'HRB', 'BA', 'BWA', 'BXP', 'BSK', 'BMY', 'BRCM', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FSIV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHFI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT', 'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLC', 'R', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJK', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS'],
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
        sell = {}
        buy = {}
        for stock in signals.keys():
            #print("Shares to buy/sell for " + stock + ": " + str(int(round(signals[stock] * positions[stock]))))
            shares = int(round(signals[stock] * positions[stock]))
            if int(round(signals[stock] * positions[stock])) < 0:
                sell[stock] = shares
                print("Shares to sell for " + stock + ": " + str(int(round(signals[stock] * positions[stock]))))
            else:
                buy[stock] = [signals[stock], positions[stock]]
        SignalGenerator.write_dict_to_file(buy, "buy_orders.txt", True)

    @staticmethod
    def high_risk_suggest_orders():
        signals = PortfolioManager.get_signals_SP_500()
        for stock in signals.keys():
            if (signals[stock] > .5):
                print(stock + ": " + signals[stock])

    @staticmethod
    def recalculate_buys(buying_power):
        file = open("buy_prices.txt", "r")
        lines = file.read().splitlines()
        file.close()
        prices = {}
        line = 0
        while line < len(lines):
            prices[lines[line]] = float(lines[line + 1])
            line += 2

        file = open("buy_orders.txt", "r")
        lines = file.read().splitlines()
        file.close()
        original_orders = {}
        line = 0
        while line < len(lines):
            original_orders[lines[line]] = [float(lines[line + 1]), int(lines[line + 2])]
            line += 3

        PortfolioManager.adjust_shares(prices, original_orders, buying_power)

    @staticmethod
    def adjust_shares(prices, original_orders, buying_power):
        current_sum = 0.0
        single_share_for_each_sum = 0.0
        for stock in prices:
            current_sum += prices[stock] * original_orders[stock][1]
            single_share_for_each_sum += prices[stock]
        print(current_sum)
        print(single_share_for_each_sum)
        print(buying_power)
        last_sum = 0.0
        shares_difference = 0
        if current_sum > buying_power:
            while current_sum > buying_power:
                last_sum = current_sum
                current_sum -= single_share_for_each_sum
                shares_difference -= 1
            shares_difference += 1
        else:
            while current_sum < buying_power:
                last_sum = current_sum
                current_sum += single_share_for_each_sum
                shares_difference += 1
            shares_difference -= 1

        new_orders = {}
        for stock in prices:
            new_orders[stock] = original_orders[stock][1] + shares_difference

        print("Adjusted shares: " + str(shares_difference))
        SignalGenerator.write_dict_to_file(new_orders, "adj_buy_orders.txt", False)



        #TODO calculate stocks only to be sold, and then uses buying power to calculate shares to be bought

    #TODO update the portfolio file to reflect changes
    @staticmethod
    def update_portfolio():
        pass

    #TODO GUI with progress bar

#PortfolioManager.suggest_orders()
#PortfolioManager.recalculate_buys(15268.14)
PortfolioManager.high_risk_suggest_orders()