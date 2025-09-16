import pandas as pd
import numpy as np # type: ignore

def compute_correlation(ticker1: str, ticker2: str, duration: str):

    file_path_1 = f"{ticker1}_Compound_Returns_for_{duration}.csv"
    file_path_2 = f"{ticker2}_Compound_Returns_for_{duration}.csv"

    data1 = pd.read_csv(file_path_1)  # type: ignore
    data2 = pd.read_csv(file_path_2) # type: ignore

    data1.dropna(axis=0, how='any', inplace=True)  # type: ignore
    data2.dropna(axis=0, how="any", inplace=True)  # type: ignore

    merged_data = pd.merge(data1, data2, on="Date")

    columns_to_select = [f"{ticker1}", f"{ticker2}"]
    merged_data = merged_data.loc[:, columns_to_select]

    correlation_matrix = merged_data.corr()
    correlation_value = correlation_matrix.loc[f"{ticker1}", f"{ticker2}"]


    if correlation_value < 0:  # type: ignore
        print(
            f"\n Stocks {ticker1} and {ticker2} are negatively correlated with value '{correlation_value:.4f}'"
        )
    elif correlation_value == 0:
        print("\n No Correlation betwween the stocks")
    else:
        print(
            f"\n Stocks {ticker1} and {ticker2} are positively correlated with value '{correlation_value:.4f}'"
        )
