"""
Widget for choosing the dayprofile for the parameter
"""
# ! Out dated code - Need to be rewritten

# TODO: Needs to be implemented into pages\setup.py

import os
import tkinter as tk
from tkinter import ttk

class choose_dayprofile(ttk.Frame):
    def __init__(self, parent, label_text):
        """
        Initializes the class instance with a parent widget and a label text.

        Args:
            parent: The parent widget.
            label_text: The text to display as the label.

        Returns:
            None.
        """
        super().__init__(master = parent)

        # grid layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1), weight = 1, uniform = "a")

        # widgets
        ttk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = "nsew")
        self.combobox = ttk.Combobox(self, state="readonly")
        self.combobox.grid(row = 0, column = 1, sticky = "nsew")

        self.populate_combobox()

    def populate_combobox(self):
        """
        Populates a combobox with a list of files from the "dayprofiles" directory.
        
        This function retrieves the current working directory and then appends the "dayprofiles" directory
        to it. It then retrieves a list of all files in that directory that starts with "dayprofile" and have a '.txt' extension.
        Finally, it sets the 'values' attribute of the combobox to the list of retrieved files.
        """
        current_dir = os.getcwd()
        directory = os.path.join(current_dir, "dayprofiles")
        files = [f for f in os.listdir(directory) if f.endswith('.txt') and f.startswith("dayprofile")]

        self.combobox['values'] = files

if __name__ == "__main__":  
    root = tk.Tk()

    root.title("TEST: choose_dayprofile")
    root.geometry("500x50")

    choose_dayprofile(root, "test").pack(expand = True, fill = "both", padx = 10, pady = 10)
    
    root.mainloop()