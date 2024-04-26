from typing import Any
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pytz
from datetime import datetime
import yfinance as yf

 
mt5.initialize()

class GetData:
    def __init__(self, pair, start, end, timeframe) -> None:
        pass

    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()

    def getTicksAndSave() -> pd.DataFrame:

        ticks = mt5.copy_rates_range(currency, mt5.TIMEFRAME_30, start, end)

        while ticks is None:
            ticks = mt5.copy_rates_range(currency, mt5.TIMEFRAME_H1, start, end)
            print(mt5.last_error()[1])
            print("Retrying.....")
        
        mt5.shutdown()

        ticksDF= pd.DataFrame(ticks)
        ticksDF.columns = ticksDF.columns.str.title()

        ticksDF['Time']=pd.to_datetime(ticksDF['Time'], unit='s')
        file_location = "data_"+currency+"_4mo_30min.csv"
        ticksDF.to_csv(file_location, index=False)

        return file_location

    if __name__ == "__main__":
        currency = "XAUUSD"
        timezone = pytz.timezone("Etc/UTC")
        start = datetime(2023, 10, 1, tzinfo=timezone)
        end = datetime(2024, 2, 1, tzinfo=timezone)
        
        print("Ticks downloaded successfully! \n Location: " +  getTicksAndSave(currency, start, end))




