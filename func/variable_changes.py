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

def on_variable_change(name, index, mode, variable):
    """
    This function handles the event of a variable change. It takes in four parameters:
        - name: the name of the variable (not used)
        - index: the index of the variable (not used)
        - mode: the mode of the variable change (not used)
        - variable: the variable that has changed\n
    This function does not return anything, but prints the value of the variable to the console.
    """
    if int(len(variable.get())) > 0:
        print(variable.get())

def on_variable_change_int(name, index, mode, variable, starting_value = ""):
    if int(len(variable.get())) > 0:
        try:
            int(variable.get())
            print(variable.get())
        except ValueError:
            print(f"This isn't a number: {variable.get()}. An error has been raised. Value has been reset to {starting_value}.")
            CTkMessagebox.CTkMessagebox(title = "Error", message = "Value must be a number!\nValue has been reset!\nPlease try again", icon = "warning")
            variable.set(starting_value)
    

        