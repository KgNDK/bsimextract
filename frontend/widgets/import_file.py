"""
Importing file widget
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
from tkinter import filedialog, ttk, Label
import customtkinter as ctk

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *

class import_file(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=("*.txt"))
        



if __name__ == "__main__":  
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: page_menu")
    root.geometry("400x400")

    import_file(root).pack()

    root.mainloop()