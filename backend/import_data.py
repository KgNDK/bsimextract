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

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

def import_data(path_var):
    # data = pd.read_csv(rf"{path_var.get()}", sep="\t", encoding='utf-8', errors='replace')
    with open(path_var.get(), 'r', encoding='utf-8', errors='replace') as file:
        data = pd.read_csv(file, sep='\t')
    dataframe = pd.DataFrame(data).replace(",", ".", regex=True)
    print(dataframe)
    return dataframe


if __name__ == "__main__":
    import_data()