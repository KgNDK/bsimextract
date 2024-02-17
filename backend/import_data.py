"""
Importing data from the data file
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
import pandas as pd
import matplotlib
from functools import lru_cache
import traceback

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from func.timemeasure import timeit

@timeit
@lru_cache(maxsize=1)
def import_data(path_var):
    """
    A function to import data from a CSV file located at the given path_var.
    This function reads the CSV file, cleans the column names, and replaces commas with periods.
    If an error occurs during the import, it prints the error message and returns None.
    """
    try:
        df = pd.read_csv(path_var, encoding="ISO-8859-1", sep='\t')
        df.columns = [col.split(')')[0].replace('(', ' ') for col in df.columns]
        df = df.replace(",", ".", regex=True)

        return df
        
    except:
        print(f"Error while importing data: {traceback.format_exc()}")
        CTkMessagebox.CTkMessagebox(title = "Error", message = f"Error while importing data: {traceback.format_exc()}", icon = "warning")
        return None
        
# if __name__ == "__main__":
#     # path_var = "C:\\Users\\Mikkel H. Lauridsen\\OneDrive - Aalborg Universitet\\Programmer\\03 BSimExtract\\Bsimdata.txt"
#     # import_data(path_var)