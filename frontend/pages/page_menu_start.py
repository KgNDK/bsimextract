"""
Page menu Starting page
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
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
from frontend.widgets.import_file_widget import import_file_widget
from frontend.widgets.dayprofile_all import dayprofile_all

class page_menu_start(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widget importing data file in .txt format
        
        import_file_widget(self).pack(expand = True, fill = "x")

        # widgets for start under this
        dayprofile_all(self).pack(expand = True, fill = "x")



if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: dayprofile_single")
    root.geometry("400x400")

    page_menu_start(root).pack()

    root.mainloop()