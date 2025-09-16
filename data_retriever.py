import pandas as pd
import yfinance as yf # type: ignore


def get_ticker_and_duration():
    ticker = input("Enter stock ticker: ").upper()
    duration = input("Enter data duration: ").lower()

    return ticker, duration


def data_reader(ticker: str, duration: str):

    data = yf.download(ticker, period=duration) # type: ignore
    file_name = f"{ticker}_{duration}_stock_data"
    data = pd.DataFrame(data)
    data.to_csv(file_name)

    return data
