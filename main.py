from returns import simple_returns, compounded_returns # type: ignore
from data_retriever import data_reader, get_ticker_and_duration
from correlation import compute_correlation


ticker1, ticker2, duration = get_ticker_and_duration()

data1 = data_reader(ticker1, duration)  # type: ignore
data2 = data_reader(ticker2, duration)

simple_returns(data1, ticker1, duration)  # type: ignore
compounded_returns(data1, ticker1, duration)  # type: ignore

simple_returns(data2, ticker2, duration) # type: ignore
compounded_returns(data2, ticker2, duration) # type: ignore

compute_correlation(ticker1, ticker2, duration)
