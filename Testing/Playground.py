"""
Dayprofile_single widget
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
from tkinter import ttk
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
from frontend.widgets.dayprofile import dayprofile

class dayprofile_single(ctk.CTkFrame):
    def __init__(self, parent, label_text, title_text = "Choose a dayprofile:"):
        super().__init__(master = parent, fg_color = FG_COLOR)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # text widgets
        ctk.CTkLabel(self, text = title_text).grid(row = 0, column = 1, sticky = "nsew", padx = 10, pady = 5)

        # combobox widget
        dayprofile(self, label_text).grid(row = 1, column = 1, sticky = "nsew")




if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x100")

    dayprofile_single(root, "test_text", "test_title").pack()

    root.mainloop()