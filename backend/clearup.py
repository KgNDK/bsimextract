"""
Clears all the files in the 'figures output' folder when the program is started.
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
import os

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from backend.time import timeit

# @timeit
def clear_figure_output():
    """
    Clears all the files in the 'figures output' folder.
    """
    folder_path = "figures output"

    # Get a list of all the files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over the list of files and remove each one
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            # print(file_path)
            os.remove(file_path)

    print("All files in 'figures output' folder have been removed.")