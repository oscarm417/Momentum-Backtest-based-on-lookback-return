
import yfinance as yf


def get_date_ranges(dateIndex,lookBack,holdingPeriod=5,dataInterval ="1d" ):
    """[Get test ranges for back test based on lookback period, and forward period]

    Args:
        dateIndex ([pd.Series[datetime]]): Datetime Index
        lookBack ([Int]): How many years back you want to look back to create the portfolio
        holdingPeriod (int): [How many years forward from start date you want the portfolio]. Defaults to 5.
        dataInterval (str): [Granularity of Data, 1month: 1mo, 1day: 1d]. Defaults to "1d".

    Returns:
        [list((datetime,datetime))]: [Returns a list of tupples that contain start and end dates for portfolio formation]
    """
    try:
        if dataInterval == "1d":
            multiplier  =  252
        elif dataInterval == "1mo":
            multiplier = 12
    except ValueError:
        print("dataInterval not valid")

    lookBackYears = multiplier*lookBack
    holdingYears = multiplier*holdingPeriod
    interval = round(len(dateIndex)/lookBackYears)
    print(interval)
    start_index = [lookBackYears*i for i in range(1,interval)]
    start_dates = [dateIndex[i] for i in start_index]
    end_index = [i+holdingYears for i in start_index]
    end_dates = [dateIndex[i] if i < len(dateIndex) else dateIndex[-1] for i in end_index ]
    return list(zip(start_dates,end_dates))




