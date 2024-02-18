"""
Sorting dataframes or data
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
import pandas as pd
from functools import lru_cache
import matplotlib

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from backend.time import timeit
from backend.import_data import import_data_dayprofile


def discard_data(df, text):
    """
    Removes columns from the input DataFrame that do not start with the specified text, and do not match specific patterns, and returns the modified DataFrame.
    Parameters:
    - df: input DataFrame
    - text: prefix to filter the columns
    Return:
    - copied_df: modified DataFrame
    """
    copied_df = df.copy()
    columns = copied_df.columns.tolist()
    for i in range(len(columns) - 1, -1, -1):
        if not columns[i].startswith(text):
            if 'Year' in columns[i]:
                continue
            if 'Month' in columns[i]:
                continue
            if 'Day' in columns[i] and not 'DayIllum' in columns[i]:
                continue
            if 'Hour' in columns[i]:
                continue
            if 'Week' in columns[i]:
                continue
            copied_df.drop(columns[i], axis=1, inplace=True)
    return copied_df


if __name__ == "__main__":
    # year = 2010
    path = r"C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Programmer\03 BSimExtract\Bsimdata.txt"
    day_path = r"C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Programmer\03 BSimExtract\bsimextract\dayprofiles\dayprofile_always.txt"
    discard_data(import_data_dayprofile(path, day_path), "Co2").to_csv("test.txt", sep="\t")