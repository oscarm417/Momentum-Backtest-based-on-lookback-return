import pandas as pd
import numpy as np 
import yfinance as yf 
import matplotlib.pyplot as plt
import pandas_market_calendars as mcal 
import datetime 


    
def get_returns(stocks,weights,start_date,end_date,data):
    #Change to SQl query of stock Data from GCP
    bag = data[stocks].loc[start_date:end_date]
    stock_returns = bag.pct_change()[1:]
    ret = (stock_returns * weights).sum(axis = 1)
    return ret


def back_test(portfolio,data):
    
    
    daily_returns = get_returns(
            portfolio.portfolio,
            portfolio.weights,
            start_date=portfolio.start_date,
            end_date=portfolio.end_date,
            data=data
        )
    
    cumulative_returns = (1+daily_returns).cumprod()

    return daily_returns



