import pandas as pd
import  datetime
import pandas_market_calendars as mcal



#Change to get all Data from GCP 
def get_data(filename):
    df  = pd.read_csv(filename)
    df.set_index('Date',inplace=True)
    return df


