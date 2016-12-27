import numpy as np
import pandas as pd

def correlate(dataframe, stock, stocks_to_compare):
    correlations_matrix = dataframe.corr()
    if isinstance(stocks_to_compare, list):
        correlations_list = {}
        for st in stocks_to_compare:
            correlations_list[st] = correlations_matrix[stock][st]
        return pd.Series(correlations_list)
    return correlations_matrix[stock][stocks_to_compare]

def correlate_with_timeshift(dataframe, stock, stocks_to_compare, timeshift):
    if timeshift > 0:
        stock_shifted = list(dataframe[stock][timeshift:])
        if isinstance(stocks_to_compare, list):
            correlations_list = {}
            for st in stocks_to_compare:
                compare_stock_shifted = list(dataframe[st][:-timeshift])
                correlations_matrix = np.corrcoef(stock_shifted,compare_stock_shifted)
                correlations_list[st] = correlations_matrix[0][1]
            return pd.Series(correlations_list)
        else:
            compare_stock_shifted = list(dataframe[stocks_to_compare][:-timeshift])
            correlations_matrix = np.corrcoef(stock_shifted,compare_stock_shifted)
            return correlations_matrix[0][1]
    elif timeshift < 0:
        stock_shifted = list(dataframe[stock][:timeshift])
        if isinstance(stocks_to_compare, list):
            correlations_list = {}
            for st in stocks_to_compare:
                compare_stock_shifted = list(dataframe[st][timeshift*-1:])
                correlations_matrix = np.corrcoef(stock_shifted,compare_stock_shifted)
                correlations_list[st] = correlations_matrix[0][1]
            return pd.Series(correlations_list)
        else:
            compare_stock_shifted = list(dataframe[stocks_to_compare][timeshift*-1:])
            correlations_matrix = np.corrcoef(stock_shifted,compare_stock_shifted)
            return correlations_matrix[0][1]

def moving_corrs(dataframe, stock, stocks_to_compare, window):
    if len(dataframe.index) < window:
        raise ValueError("window larger than dataframe")
    windows_in_dataframe = int(len(dataframe.index)/window)
    corrs = [None] * windows_in_dataframe
    for i in range(windows_in_dataframe):
        #index the windows_in_dataframe
        start_i = (i - 1) * (window)
        end_i = ((i - 1) * window) + (window - 1)
        dataframe_cut = dataframe[start_i:end_i]
        corrs[i-1] = correlate(dataframe_cut, stock, stocks_to_compare)
    return corrs



