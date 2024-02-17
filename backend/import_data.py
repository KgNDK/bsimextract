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

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

def import_data(path_var, new_data_var):
    print("Importing data")
    new_data_var.set(True)
    data = pd.read_csv(rf"{path_var.get()}", sep="\t", encoding='latin1')
    df = pd.DataFrame(data)
    print(df)
    # new_data_var.set(True)


if __name__ == "__main__":
    import_data()