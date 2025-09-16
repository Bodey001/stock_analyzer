import pandas as pd
import yfinance as yf # type: ignore


def get_ticker_and_duration():
    ticker1 = input("Enter ticker for stock A: ").upper().strip()
    ticker2 = input("Enter ticker for stock B: ").upper().strip()
    duration = input("Enter data duration: ").lower().strip()

    return ticker1, ticker2, duration


def data_reader(ticker: str, duration: str):

    try:
        data = yf.download(ticker, period=duration) # type: ignore
        file_name = f"{ticker}_{duration}_stock_data"
        data = pd.DataFrame(data)

        data = data.dropna(axis=0, how='any') # type: ignore
        data.to_csv(f"{file_name}.csv")

        return data
    except Exception as e:
        print(f"An error occured: {e}")
        return pd.DataFrame
