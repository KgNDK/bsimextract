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
import datetime

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from backend.timemeasure import timeit

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
    

@lru_cache(maxsize=10)
def import_dayprofile(path_var):
    """
    A function that imports a dayprofile from a given path.

    Args:
        path_var (str): The path to the dayprofile file.

    Returns:
        DataFrame: The imported dayprofile as a pandas DataFrame, or None if there was an error.
    """
    try:
        df = pd.read_csv(path_var, sep='\t')
        return df
    except:
        print(f"Error while importing data: {traceback.format_exc()}")
        CTkMessagebox.CTkMessagebox(title = "Error", message = f"Error while importing dayprofile: {traceback.format_exc()}", icon = "warning")
        return None

@timeit
@lru_cache(maxsize=4)
def import_data_dayprofile(path_var, dayprofile_var):
    """
    This function imports data from a given path and day profile, processes the data, and returns the resulting dataframe.
    Parameters:
    - path_var: a string representing the path to the data file
    - dayprofile_var: a variable representing the day profile
    Return:
    - df_data: a processed dataframe
    """
    df_data = import_data(path_var)
    year = int(df_data.iloc[1, 0])
    df_data = add_week(df_data, year)
    df_dayprofile = import_dayprofile(dayprofile_var)
    mask = df_data.apply(check_data, args=(df_dayprofile,), axis=1)
    df_data = df_data[mask]
    return df_data

    
def check_data(row, df_dayprofile):
    """
    Function to check data based on the provided row and day profile dataframe.
    Parameters:
        row: pandas Series - contains the data for Month, Week, Day, and Hour
        df_dayprofile: pandas DataFrame - contains the day profile data
    Returns:
        bool - True if all conditions are met, False otherwise
    """
    month_index = int(row["Month"]) - 1
    week_index = int(row["Week"])
    day_index = int(row["Day"]) - 1
    hour_index = int(row["Hour"]) - 1
    return (df_dayprofile.iloc[0, month_index] and df_dayprofile.iloc[3, hour_index] and df_dayprofile.iloc[2, day_index] and df_dayprofile.iloc[1, week_index])

def add_week(df, year):
    """
    Add week number to the dataframe based on the given year.

    Parameters:
    - df: pandas DataFrame
    - year: int, the year for which the weeks are to be added
    
    Returns:
    - df: pandas DataFrame with the 'Week' column added
    """
    hours = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31 23:00', freq='H')
    df['Week'] = pd.to_datetime(hours).strftime('%U')
    df['Week'] = df['Week'].apply(week_number)
    return df

def week_number(row):
    """
    Removes leading zeros from the week number if not the last week of prior year.
    """
    if int(row) < 1:
        return 0
    else:
        return row.lstrip('0')

if __name__ == "__main__":
    # year = 2010
    path = r"C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Programmer\03 BSimExtract\Bsimdata.txt"
    day_path = r"C:\Users\Mikkel H. Lauridsen\OneDrive - Aalborg Universitet\Programmer\03 BSimExtract\bsimextract\dayprofiles\dayprofile_always.txt"
    import_data_dayprofile(path, day_path).to_csv("test.txt", sep="\t")