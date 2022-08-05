import pandas as pd
import numpy as np 



def construct(lookback_period: int,start_date: str, df: pd.DataFrame, interval: str):
    """Constructs the long-short portfolio by picking the top
    quartile and bottom quartile in returns based on a given lookback
    period, and start date.

    Args:
        lookback_period (int): The lookback return period in days
        start_date (string): YYYY-MM-DD 
        data_frame (DataFrame): Contains all stock prices
        interval (str): time intervals of data points.
    """
    if interval == '1d':
        multiplier = 252
    elif interval == '1mo':
        multiplier = 12
    pipe = df.pct_change(multiplier *lookback_period).loc[start_date]
    bottom_q = pipe.quantile(.1)
    top_q = pipe.quantile(.90)
    top_tickers = pipe[pipe>top_q].dropna().index
    bottom_tickers = pipe[pipe<bottom_q].dropna().index
    return list(top_tickers), list(bottom_tickers)
    


