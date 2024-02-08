"""
Page menu AirChange page
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import tkinter as tk
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
from frontend.widgets.dayprofile_single import dayprofile_single
from frontend.widgets.co2_format_widget import co2_format_widget

class page_menu_airch(ctk.CTkFrame):
    def __init__(self, parent, airch_dayprofile_var):
        super().__init__(master = parent, fg_color="transparent")
        self.pack(expand = True, fill = "both")

        # widgets for AirChange under this
        dayprofile_single(self, "AirChange", airch_dayprofile_var).pack(fill = "x", expand = True)

        # widgets for formatting AirChange data under this
        co2_format_widget(self, "AirChange hours above", "Apply", "Max AirChange:", "Formatting color:", "2", "3", "4").pack(expand = True, fill = "x")

if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: Page menu AirChange page")
    root.geometry("400x300")

    page_menu_airch(root).pack()

    root.mainloop()