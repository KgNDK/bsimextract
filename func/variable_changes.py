"""
Functions that run when a variable is changed
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

def on_variable_change(name, index, mode, variable, text_before = "", text_after = ""):
    """
    A function that is called when a variable changes. 
    Parameters:
    - name: the name of the variable (not used)
    - index: the index of the variable (not used)
    - mode: the mode of the variable (not used)
    - variable: the variable being changed
    - text_before: a string to be printed before the variable
    - text_after: a string to be printed after the variable\n
    This function does not return anything, but prints the results on the terminal
    """
    
    if int(len(variable.get())) > 0:
        print(f"{text_before}{variable.get()}{text_after}")

def on_variable_change_int(name, index, mode, variable, starting_value = "", text_before = "", text_after = ""):
    """
    Check if the length of the variable is greater than 0. If it is, try to convert the variable to an integer and print the result. If the conversion fails, print an error message and reset the variable to the starting value.
    Parameters:
    - name: the name of the variable (not used)
    - index: the index of the variable (not used)
    - mode: the mode of the variable (not used)
    - variable: the variable to be checked
    - starting_value: the initial value of the variable
    - text_before: a string to be printed before the variable
    - text_after: a string to be printed after the variable\n
    This function does not return anything, but prints the results on the terminal and resets the variable to the starting value if the conversion fails.
    """
    if int(len(variable.get())) > 0:
        try:
            int(variable.get())
            print(f"{text_before}{variable.get()}{text_after}")
        except ValueError:
            print(f"{name} isn't a number: {variable.get()}. An error has been raised. {name} has been reset to {starting_value}.")
            CTkMessagebox.CTkMessagebox(title = "Error", message = "Value must be a number!\nValue has been reset!\nPlease try again", icon = "warning")
            variable.set(starting_value)

def on_page_menu_var_change(name, index, mode, variable, frame, dict, new_data_var, row = 0, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY): 
    """
    Function to handle a change in the page menu variable.

    Args:
        name: The name of the variable. (not used)
        index: The index of the variable. (not used)
        mode: The mode of the variable. (not used)
        variable: The variable to be changed.
        frame: The frame to be updated.
        dict: A dictionary containing the variable display functions.
        row: The row to place the variable display in (default is 0).
        column: The column to place the variable display in (default is 1).
        sticky: The positioning of the variable display (default is "nsew").
        padx: The padding in the x-direction (default is STANDARD_PADX).
        pady: The padding in the y-direction (default is STANDARD_PADY).

    Returns:
        None
    """
    for i in dict:
        try:
            i(frame).grid_remove()
        except:
            pass

    value = f"display_{variable.get()}".lower()
    
    if value in dict:
        dict[value](frame, new_data_var, variable).grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)  
    else:
        print(f"Variable not found: {variable.get()}")
        CTkMessagebox.CTkMessagebox(title = "Error", message = "Variable not found", icon = "warning")

        