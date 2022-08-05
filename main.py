import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from portfolio import Portfolio
from construct_portfolio import construct
from stocks_get_data import get_data
from backtester import back_test
from date_splitter import get_date_ranges
import date_splitter




#df = get_data(r"data\historical_prices.csv").loc['1985-01-01':]
df = pd.read_pickle(r"data\monthly_returns.pkl")
formationPeriod = [5,3,2]


# summaryRows = []
# for i in  formationPeriod:
#     portfolioRanges = get_date_ranges(df.index,i,5,'1mo')[2:]
#     meanStatistics = []
#     for i in portfolioRanges:        
#         top_tickers, bottom_tickers = construct(5,i[0],df,'1mo')
#         longP = Portfolio(i[0],i[1],bottom_tickers)
#         shortP = Portfolio(i[0],i[1],top_tickers)
#         longBacktest = back_test(longP,df)/2
#         shortBacktest = (back_test(shortP,df)*-1)/2
#         loserPortfolio = (1+shortBacktest).cumprod()
#         winnerPortfolio = (1+longBacktest).cumprod()
#         totalReturn = (1+(longBacktest+shortBacktest)).cumprod()
#         average_number_stocks = len(top_tickers) + len(bottom_tickers)
#         longReturn = winnerPortfolio[-1]
#         shortReturn = loserPortfolio[-1]
#         mstats = [average_number_stocks,totalReturn.iloc[1],
#                                         totalReturn.iloc[12],
#                                         totalReturn.iloc[13],
#                                         totalReturn.iloc[18],
#                                         totalReturn.iloc[24],
#                                         totalReturn.iloc[25],
#                                         totalReturn.iloc[31],
#                                         np.nan]
#         meanStatistics.append(mstats)
#     summaryRows.append(np.mean(meanStatistics,axis = 0))
    
# summaryTable = pd.DataFrame(summaryRows,index = formationPeriod, columns =['average_number_stock','1','12','13','18','24','25','36','60'])


# print('bla')





# interest = [('1970-01-01')]
# years = 5
# top_tickers,bottom_tickers = construct(5,start_date,df,'1mo')

# longP = Portfolio(start_date,end_date,bottom_tickers)
# shortP = Portfolio(start_date,end_date,top_tickers)

# longBacktest = back_test(longP,df)
# shortBacktest = back_test(shortP,df)

# total = longBacktest+(-1*shortBacktest)
# total.index = pd.to_datetime(total.index, format = "%Y-%m-%d")
# c = (1+total).cumprod()
# g = total.groupby(by = [total.index.month]).mean()
# c.plot(label = 'long-short')
# plt.show()


print('bla')
