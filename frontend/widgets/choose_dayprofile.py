"""
Widget for choosing the dayprofile for the parameter
"""

# TODO: Fix the dropdown list

import tkinter as tk
from tkinter import ttk
import os

def retrieve_data(startswith_text, format=".txt"):    
    data = [f for f in os.listdir() if f.startswith(startswith_text) and f.endswith(format)]
    return data

class choose_dayprofile(ttk.Frame):
    def __init__(self, parent, label_text):
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1), weight=1, uniform="a")
        
        # label
        ttk.Label(self, text=label_text).grid(column=0, row=0, sticky='nsew')

        # dropdown of dayprofiles
        dropdown_str = tk.StringVar()
        dayprofile_combobox =ttk.Combobox(self, state="readonly", textvariable=dropdown_str).grid(column=1, row=0, sticky='nsew')

        # Call retrieve_data to get the list of files
        data = retrieve_data("dayprofile")
        dayprofile_combobox["values"] = data

        # placement method
        self.pack(expand=True, fill = 'both', padx=10, pady=10)






# Test
if __name__ == "__main__":
    data = []

    print("Retrieved dayprofiles:", data)

    window = tk.Tk()
    window.title("Test: choose_dayprofile")
    window.geometry("500x100")

    # widgets
    choose_dayprofile(window, "label")
    
    # run   
    window.mainloop()
