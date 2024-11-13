import pandas as pd

def drop_missing(data, threshold=0.5):
    """Drops columns with missing values above a certain threshold."""
    data = data.loc[:, data.isnull().mean() < threshold]
    print("Columns with high missing values dropped.")
    return data

def fill_missing_with_mean(data):
    """Fills missing values with the mean of the column."""
    return data.fillna(data.mean())
