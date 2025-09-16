# from data_retriever import data_reader, get_ticker_and_duration
import pandas as pd
import numpy as np


# ticker1, ticker2, duration = get_ticker_and_duration()

# data1 = data_reader(ticker1, duration) # type: ignore
# data2 = data_reader(ticker2, duration)


def simple_returns(value: pd.DataFrame, ticker: str, duration: str):

    try:
        adj_close = value["Close"]
        simple_returns = adj_close.pct_change()

        simple_returns.dropna(axis=0, how='any')

        file_name = f"{ticker}_Simple_Returns_for_{duration}"
        simple_returns.to_csv(f"{file_name}.csv")

        # print(f" ----{ticker} simple returns for a period of {duration} ----")
        print(simple_returns.head())

    except Exception as e:
        return f"An error occured: {e}"



def compounded_returns(value: pd.DataFrame, ticker: str, duration: str):

    try:
        adj_close = value["Close"]
        log_returns: pd.DataFrame = np.log(adj_close / adj_close.shift(1)) # type: ignore

        log_returns.dropna(axis=0, how='any') # type: ignore

        file_name = f"{ticker}_Compound_Returns_for_{duration}"
        log_returns.to_csv(f"{file_name}.csv")

        print(f"\n ----{ticker} compound returns for a period of {duration} ----")
        print(log_returns.head())

    except Exception as e:
        return f"An error occured: {e}"
