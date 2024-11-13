import pandas as pd

def summarize_data(data):
    """Provides summary statistics for the DataFrame."""
    return data.describe()

def check_missing_values(data):
    """Returns the count of missing values per column."""
    return data.isnull().sum()
