from data_retriever import data_reader, get_ticker_and_duration
import pandas as pd
import numpy as np


ticker, duration = get_ticker_and_duration()

data = data_reader(ticker, duration) # type: ignore

def simple_returns():

    adj_close = data['Close']
    simple_returns = adj_close.pct_change()

    file_name = f"{ticker}_Simple_Returns_for_{duration}"
    simple_returns.to_csv(f"{file_name}.csv")

    print(f" ----{ticker} simple returns for a period of {duration} ----")
    print(simple_returns.head())



def compounded_returns():

    adj_close = data["Close"]
    log_returns: pd.DataFrame = np.log(adj_close / adj_close.shift(1)) # type: ignore

    file_name = f"{ticker}_Compound_Returns_for_{duration}"
    log_returns.to_csv(f"{file_name}.csv")

    print(f"\n ----{ticker} compound returns for a period of {duration} ----")
    print(log_returns.head())
