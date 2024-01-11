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
from frontend.widgets.dayprofile import dayprofile
from frontend.widgets.dayprofile_title import dayprofile_title

class dayprofile_single(ctk.CTkFrame):
    def __init__(self, parent, label_text, title_text = "Choose a dayprofile:"):
        super().__init__(master = parent, fg_color = FG_COLOR)
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text widgets
        dayprofile_title(self, title_text).pack(fill = "x", expand = True)

        # combobox widget
        dayprofile(self, label_text).pack(fill = "x", expand = True)




if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x100")

    dayprofile_single(root, "test_text", "test_title").pack()

    root.mainloop()