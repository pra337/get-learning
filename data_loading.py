#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def load_csv(file_path):
    """Loads a CSV file into a Pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

